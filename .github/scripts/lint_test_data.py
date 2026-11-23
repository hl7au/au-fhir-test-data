"""Lint the test data files.

Every FHIR JSON file under the scanned root is checked against these rules:

- resource-id (error): the resource has an id. A transaction or batch Bundle
  is exempt, since FHIR lets it have none.
- file-name (warning): the file is named <resourceType>-<id>.json.
- contact-phone (warning): every ContactPoint with system phone, fax, sms or
  pager uses a number the ACMA reserves for fictional use.
- contact-email (warning): every email address uses a domain reserved for
  documentation (RFC 2606, RFC 6761). This covers ContactPoints with system
  email, ContactPoints with no system whose value contains @, and any address
  found in another string value, such as narrative text.div, a mailto:
  Endpoint.address or an extension valueString.
- json-indent (warning): the file is indented with 2 spaces.
- line-endings (warning): the file uses LF line endings, not CRLF.

ContactPoints and strings are found anywhere in a resource, including
contained resources and Bundle entries. ContactPoint systems are matched
case-insensitively. Phone numbers in free text are not checked, because
identifiers such as Medicare numbers look like phone numbers.

An error fails the check. A warning is reported but does not, because the
data on master still has violations of that rule; promote it to an error
once they are fixed.

Problems whose rule and subject (the file path, or for contact rules the
normalised number or email domain) match an entry in the exceptions file are
ignored. Problems are printed, written to the GitHub step summary, and
emitted as workflow commands when running in Actions.

With --changed-files (a file listing one path per line, relative to the
current directory, as git diff --name-only prints from the repository root),
workflow commands are emitted only for errors and for problems in the listed
files, and the step summary leads with the problems in those files. This keeps
a pull request's annotations about the files it touches, since GitHub shows
only the first few annotations per step. Errors anywhere still fail the run.
"""

import argparse
import fnmatch
import json
import os
import re
import sys
from dataclasses import dataclass
from email.utils import parseaddr
from pathlib import Path

DEFAULT_EXCEPTIONS = Path(__file__).with_name("lint_test_data_exceptions")

ERROR = "error"
WARNING = "warning"

SEVERITY = {
    "resource-id": ERROR,
    "file-name": WARNING,
    "contact-phone": WARNING,
    "contact-email": WARNING,
    "json-indent": WARNING,
    "line-endings": WARNING,
    "parse": ERROR,
}

# Numbers the ACMA reserves for use in TV shows, films and creative works.
# Source: https://www.acma.gov.au/phone-numbers-use-tv-shows-films-and-creative-works
# (retrieved 2026-11-23, page last updated 2026-09-03).
# Geographic: (0X) 5550 xxxx and (0X) 7010 xxxx for area codes 02, 03, 07, 08.
RESERVED_GEOGRAPHIC = re.compile(r"^0[2378](5550|7010)\d{4}$")
RESERVED_NUMBERS = frozenset({
    # Mobile.
    "0491570006", "0491570156", "0491570157", "0491570158", "0491570159",
    "0491570110", "0491570313", "0491570737", "0491571266", "0491571491",
    "0491571804", "0491572549", "0491572665", "0491572983", "0491573770",
    "0491573087", "0491574118", "0491574632", "0491575254", "0491575789",
    "0491576398", "0491576801", "0491577426", "0491577644", "0491578957",
    "0491578148", "0491578888", "0491579212", "0491579760", "0491579455",
    # Freephone and local rate.
    "1800160401", "1800975707", "1800975708", "1800975709", "1800975710",
    "1800975711", "1300975707", "1300975708", "1300975709", "1300975710",
    "1300975711",
})
PHONE_SYSTEMS = {"phone", "fax", "sms", "pager"}
# A trailing extension such as "ext 12", "x12", "extn. 12" or ";ext=12".
PHONE_EXTENSION = re.compile(r"[\s,;]*(?:extn|ext|x)[.:=]?\s*\d+\s*$", re.IGNORECASE)

# Second-level domains reserved by RFC 2606 section 3, and top-level domains
# reserved by RFC 2606 section 2 and RFC 6761. Subdomains of these are fine.
RESERVED_DOMAINS = ("example.com", "example.net", "example.org")
RESERVED_TLDS = ("example", "test", "invalid", "localhost")
RESERVED_DOMAINS_TEXT = "example.com, example.net, example.org, .example, .test, .invalid, .localhost"

# An email address in free text. Deliberately conservative: the domain needs a
# dot and an alphabetic top-level domain, and an address directly after a
# slash or inside a longer token (such as URL userinfo) is not matched.
EMAIL_IN_TEXT = re.compile(
    r"(?<![\w.%+/-])[\w.%+-]+@(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z]{2,}(?![\w-])"
)

SKIPPED_DIRS = {"node_modules"}


@dataclass(frozen=True)
class Problem:
    path: str
    rule: str
    message: str
    subject: str = ""

    @property
    def severity(self):
        return SEVERITY[self.rule]


def load_list(path):
    """Return the non-comment lines of a list file, or [] if it does not exist."""
    try:
        lines = Path(path).read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        return []
    return [line.strip() for line in lines if line.strip() and not line.strip().startswith("#")]


def parse_exceptions(lines):
    """Return (rule, pattern) pairs from "<rule> <pattern>" lines."""
    exceptions = []
    for line in lines:
        rule, _, pattern = line.partition(" ")
        if rule not in SEVERITY or not pattern.strip():
            raise ValueError(f"Bad exception line '{line}': expected '<rule> <pattern>'.")
        exceptions.append((rule, pattern.strip()))
    return exceptions


def iter_json_files(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIPPED_DIRS and not d.startswith("."))
        for name in sorted(filenames):
            if name.endswith(".json"):
                yield Path(dirpath) / name


def normalise_phone(value):
    """Return value as a national Australian number with only digits."""
    number = value.strip()
    if number.lower().startswith("tel:"):
        number = number[len("tel:"):]
    number = PHONE_EXTENSION.sub("", number)
    digits = re.sub(r"\(0\)|[\s().\-]", "", number)
    if digits.startswith("+61"):
        digits = "0" + digits[3:]
    elif digits.startswith("0061"):
        digits = "0" + digits[4:]
    elif digits.startswith("61") and len(digits) == 11:
        digits = "0" + digits[2:]
    return digits


def is_reserved_phone(number):
    return number in RESERVED_NUMBERS or bool(RESERVED_GEOGRAPHIC.match(number))


def email_domain(value):
    """Return the lower-case domain of an address, a mailto: URI or a "Name <address>" value."""
    address = value.strip()
    if address.lower().startswith("mailto:"):
        address = address[len("mailto:"):].partition("?")[0]
    address = parseaddr(address)[1] or address
    return address.lower().rpartition("@")[2].rstrip(".")


def is_reserved_domain(domain):
    if any(domain == d or domain.endswith("." + d) for d in RESERVED_DOMAINS):
        return True
    return domain.rpartition(".")[2] in RESERVED_TLDS


def child_path(path, key):
    if isinstance(key, int):
        return f"{path}[{key}]"
    return f"{path}.{key}" if path else key


def iter_nodes(node, path=""):
    """Yield (JSON path, value) for node and everything inside it."""
    yield path, node
    if isinstance(node, dict):
        for key, value in node.items():
            yield from iter_nodes(value, child_path(path, key))
    elif isinstance(node, list):
        for index, item in enumerate(node):
            yield from iter_nodes(item, child_path(path, index))


def is_contact_point(node):
    """Return whether node looks like a ContactPoint: a string value and a string or absent system."""
    return (
        isinstance(node, dict) and isinstance(node.get("value"), str)
        and isinstance(node.get("system", ""), str)
    )


def email_problem(rel_path, value, where=""):
    domain = email_domain(value)
    if is_reserved_domain(domain):
        return None
    location = f" in {where}" if where else ""
    return Problem(
        rel_path, "contact-email",
        f"Email '{value}'{location} does not use a reserved domain ({RESERVED_DOMAINS_TEXT}).",
        domain,
    )


def check_contacts(rel_path, resource):
    nodes = list(iter_nodes(resource))
    checked = set()  # JSON paths of ContactPoint values already checked.
    for path, node in nodes:
        if not is_contact_point(node):
            continue
        system, value = node.get("system", "").lower(), node["value"]
        if system in PHONE_SYSTEMS:
            checked.add(child_path(path, "value"))
            number = normalise_phone(value)
            if not is_reserved_phone(number):
                yield Problem(
                    rel_path, "contact-phone",
                    f"{system.capitalize()} number '{value}' is not in the ACMA ranges reserved for fictional use.",
                    number,
                )
        elif system == "email" or ("system" not in node and "@" in value):
            checked.add(child_path(path, "value"))
            problem = email_problem(rel_path, value)
            if problem:
                yield problem

    # Any other string, such as narrative or an extension value. Attachment.data
    # is base64, which cannot contain @, so encoded content is never matched.
    for path, node in nodes:
        if not isinstance(node, str) or path in checked or "@" not in node:
            continue
        for address in dict.fromkeys(m.group(0) for m in EMAIL_IN_TEXT.finditer(node)):
            problem = email_problem(rel_path, address, path)
            if problem:
                yield problem


def check_format(rel_path, text):
    if "\r\n" in text:
        yield Problem(rel_path, "line-endings", "File uses CRLF line endings; use LF.", rel_path)
    indents = [m.group(1) for m in re.finditer(r"^([ \t]*)\S", text, re.MULTILINE)]
    nested = [i for i in indents if i]
    if nested and (nested[0] != "  " or any("\t" in i or len(i) % 2 for i in nested)):
        yield Problem(rel_path, "json-indent", "File is not indented with 2 spaces.", rel_path)


def needs_id(resource):
    """Return whether the resource must have an id; a transaction or batch Bundle need not."""
    return not (resource["resourceType"] == "Bundle" and resource.get("type") in ("transaction", "batch"))


def check_file(path, root):
    rel_path = path.relative_to(root).as_posix()
    try:
        text = path.read_bytes().decode("utf-8")  # Not read_text, which hides CRLF.
        resource = json.loads(text)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        return [Problem(rel_path, "parse", f"Cannot parse file: {exc}", rel_path)]
    if not isinstance(resource, dict) or "resourceType" not in resource:
        return []  # Not a FHIR resource.

    problems = []
    resource_type, resource_id = resource["resourceType"], resource.get("id")
    if not isinstance(resource_id, str) or not resource_id:
        if needs_id(resource):
            problems.append(Problem(rel_path, "resource-id", "Resource has no id.", rel_path))
    elif path.name != f"{resource_type}-{resource_id}.json":
        problems.append(Problem(
            rel_path, "file-name",
            f"File name does not match the resource; expected '{resource_type}-{resource_id}.json'.", rel_path,
        ))
    problems += check_contacts(rel_path, resource)
    problems += check_format(rel_path, text)
    return problems


def lint(root, exceptions=()):
    root = Path(root)
    problems = []
    for path in iter_json_files(root):
        problems += check_file(path, root)
    return sorted(
        (p for p in problems if not any(
            p.rule == rule and fnmatch.fnmatchcase(p.subject, pattern) for rule, pattern in exceptions
        )),
        key=lambda p: (p.path, p.rule, p.message),
    )


def load_changed_files(path):
    """Return the normalised paths listed one per line in path."""
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    return {Path(os.path.normpath(line.strip())).as_posix() for line in lines if line.strip()}


def is_changed(problem, root, changed_files):
    """Return whether problem is in one of changed_files (paths relative to the current directory)."""
    return Path(os.path.relpath(Path(root) / problem.path)).as_posix() in changed_files


def escape_data(value):
    return value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


def escape_property(value):
    return escape_data(value).replace(":", "%3A").replace(",", "%2C")


def workflow_command(problem, root):
    file = escape_property((Path(root) / problem.path).as_posix())
    return f"::{problem.severity} file={file},title={problem.rule}::{escape_data(problem.message)}"


def problem_table(problems):
    return ["| Severity | Rule | File | Problem |", "|---|---|---|---|"] + [
        f"| {p.severity} | {p.rule} | {p.path} | {p.message.replace('|', '&#124;')} |" for p in problems
    ]


def write_step_summary(problems, changed_problems=None):
    """Append the summary; changed_problems, if given, are those in the files a pull request changed."""
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    lines = ["## Test Data Lint", ""]
    if not problems:
        lines.append("No problems found.")
    else:
        counts = {}
        for p in problems:
            counts[(p.severity, p.rule)] = counts.get((p.severity, p.rule), 0) + 1
        lines += ["| Severity | Rule | Problems |", "|---|---|---|"]
        lines += [f"| {severity} | {rule} | {count} |" for (severity, rule), count in sorted(counts.items())]
        lines.append("")
        if changed_problems is None:
            lines += problem_table(problems)
        else:
            lines += ["### Problems in the files changed by this pull request", ""]
            if changed_problems:
                lines += problem_table(changed_problems)
            else:
                lines.append("No problems in the files changed by this pull request.")
            lines += [
                "", f"<details><summary>All {len(problems)} problems in the repository</summary>", "",
                *problem_table(problems), "", "</details>",
            ]
    with open(summary_path, "a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Lint the test data files.")
    parser.add_argument("root", nargs="?", default=".", help="directory to scan (default: current directory)")
    parser.add_argument("--exceptions", default=DEFAULT_EXCEPTIONS, help="file listing problems to ignore")
    parser.add_argument(
        "--changed-files",
        help="file listing the paths a pull request changed, one per line; annotate only errors and "
        "problems in those files",
    )
    args = parser.parse_args(argv)

    problems = lint(args.root, parse_exceptions(load_list(args.exceptions)))
    changed_problems = None
    if args.changed_files is not None:
        changed_files = load_changed_files(args.changed_files)
        changed_problems = [p for p in problems if is_changed(p, args.root, changed_files)]
    annotated = set(problems if changed_problems is None else changed_problems)
    annotated.update(p for p in problems if p.severity == ERROR)
    in_actions = os.environ.get("GITHUB_ACTIONS") == "true"
    for problem in problems:
        print(f"{problem.path}: {problem.severity}: [{problem.rule}] {problem.message}")
        if in_actions and problem in annotated:
            print(workflow_command(problem, args.root))
    write_step_summary(problems, changed_problems)

    errors = sum(p.severity == ERROR for p in problems)
    warnings = len(problems) - errors
    if problems:
        print(f"\n{errors} error(s), {warnings} warning(s).", file=sys.stderr)
        if changed_problems is not None:
            print(f"{len(changed_problems)} problem(s) in the changed files.", file=sys.stderr)
    else:
        print("No problems found.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
