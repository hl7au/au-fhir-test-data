"""Lint the test data files.

Every FHIR JSON file under the scanned root is checked against these rules:

- resource-id (error): the resource has an id.
- file-name (warning): the file is named <resourceType>-<id>.json.
- contact-phone (warning): every ContactPoint with system phone, fax or sms
  uses a number the ACMA reserves for fictional use.
- contact-email (warning): every ContactPoint with system email uses a
  domain reserved for documentation (RFC 2606, RFC 6761).
- json-indent (warning): the file is indented with 2 spaces.
- line-endings (warning): the file uses LF line endings, not CRLF.

ContactPoints are found anywhere in a resource, including contained
resources and Bundle entries.

An error fails the check. A warning is reported but does not, because the
data on master still has violations of that rule; promote it to an error
once they are fixed.

Problems whose rule and subject (the file path, or for contact rules the
normalised number or email domain) match an entry in the exceptions file are
ignored. Problems are printed, written to the GitHub step summary, and
emitted as workflow commands when running in Actions.
"""

import argparse
import fnmatch
import json
import os
import re
import sys
from dataclasses import dataclass
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
PHONE_SYSTEMS = {"phone", "fax", "sms"}

# Second-level domains reserved by RFC 2606 section 3, and top-level domains
# reserved by RFC 2606 section 2 and RFC 6761. Subdomains of these are fine.
RESERVED_DOMAINS = ("example.com", "example.net", "example.org")
RESERVED_TLDS = ("example", "test", "invalid")

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
    digits = re.sub(r"\(0\)|[\s().\-]", "", value)
    if digits.startswith("+61"):
        digits = "0" + digits[3:]
    elif digits.startswith("61") and len(digits) == 11:
        digits = "0" + digits[2:]
    return digits


def is_reserved_phone(number):
    return number in RESERVED_NUMBERS or bool(RESERVED_GEOGRAPHIC.match(number))


def email_domain(value):
    address = value.strip().lower()
    if address.startswith("mailto:"):
        address = address[len("mailto:"):]
    return address.rpartition("@")[2].rstrip(".")


def is_reserved_domain(domain):
    if any(domain == d or domain.endswith("." + d) for d in RESERVED_DOMAINS):
        return True
    return domain.rpartition(".")[2] in RESERVED_TLDS


def iter_contact_points(node):
    """Yield every ContactPoint-shaped object (system and string value) in node."""
    if isinstance(node, dict):
        if isinstance(node.get("system"), str) and isinstance(node.get("value"), str):
            yield node
        for value in node.values():
            yield from iter_contact_points(value)
    elif isinstance(node, list):
        for item in node:
            yield from iter_contact_points(item)


def check_contacts(rel_path, resource):
    for contact in iter_contact_points(resource):
        system, value = contact["system"], contact["value"]
        if system in PHONE_SYSTEMS:
            number = normalise_phone(value)
            if not is_reserved_phone(number):
                yield Problem(
                    rel_path, "contact-phone",
                    f"{system.capitalize()} number '{value}' is not in the ACMA ranges reserved for fictional use.",
                    number,
                )
        elif system == "email":
            domain = email_domain(value)
            if not is_reserved_domain(domain):
                yield Problem(
                    rel_path, "contact-email",
                    f"Email '{value}' does not use a reserved domain (example.com, example.net, example.org, "
                    ".example, .test, .invalid).",
                    domain,
                )


def check_format(rel_path, text):
    if "\r\n" in text:
        yield Problem(rel_path, "line-endings", "File uses CRLF line endings; use LF.", rel_path)
    indents = [m.group(1) for m in re.finditer(r"^([ \t]*)\S", text, re.MULTILINE)]
    nested = [i for i in indents if i]
    if nested and (nested[0] != "  " or any("\t" in i or len(i) % 2 for i in nested)):
        yield Problem(rel_path, "json-indent", "File is not indented with 2 spaces.", rel_path)


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


def escape_data(value):
    return value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


def escape_property(value):
    return escape_data(value).replace(":", "%3A").replace(",", "%2C")


def workflow_command(problem, root):
    file = escape_property((Path(root) / problem.path).as_posix())
    return f"::{problem.severity} file={file},title={problem.rule}::{escape_data(problem.message)}"


def write_step_summary(problems):
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    lines = ["## Test Data Lint", ""]
    if problems:
        counts = {}
        for p in problems:
            counts[(p.severity, p.rule)] = counts.get((p.severity, p.rule), 0) + 1
        lines += ["| Severity | Rule | Problems |", "|---|---|---|"]
        lines += [f"| {severity} | {rule} | {count} |" for (severity, rule), count in sorted(counts.items())]
        lines += ["", "| Severity | Rule | File | Problem |", "|---|---|---|---|"]
        lines += [
            f"| {p.severity} | {p.rule} | {p.path} | {p.message.replace('|', '&#124;')} |" for p in problems
        ]
    else:
        lines.append("No problems found.")
    with open(summary_path, "a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Lint the test data files.")
    parser.add_argument("root", nargs="?", default=".", help="directory to scan (default: current directory)")
    parser.add_argument("--exceptions", default=DEFAULT_EXCEPTIONS, help="file listing problems to ignore")
    args = parser.parse_args(argv)

    problems = lint(args.root, parse_exceptions(load_list(args.exceptions)))
    in_actions = os.environ.get("GITHUB_ACTIONS") == "true"
    for problem in problems:
        print(f"{problem.path}: {problem.severity}: [{problem.rule}] {problem.message}")
        if in_actions:
            print(workflow_command(problem, args.root))
    write_step_summary(problems)

    errors = sum(p.severity == ERROR for p in problems)
    warnings = len(problems) - errors
    if problems:
        print(f"\n{errors} error(s), {warnings} warning(s).", file=sys.stderr)
    else:
        print("No problems found.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
