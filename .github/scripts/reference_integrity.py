"""Check that literal references between the test data files resolve.

Every FHIR JSON file under the scanned root is indexed by resourceType/id.
The checker then resolves every literal reference it finds:

- Reference.reference (a string under a "reference" key).
- Attachment.url, when the value is a relative literal reference such as
  "Binary/abc", or a "urn:uuid:" link on an element with a contentType.
  Other "url" keys (Extension.url, canonical urls, external links) are not
  references and are left alone.

Resolution rules:

- "#id" resolves against the enclosing resource's contained resources, and
  "#" against the enclosing resource itself.
- Inside a Bundle, a reference resolves against an entry's fullUrl or an
  entry resource's type/id before falling back to the repository index.
- "Type/id" (with any "/_history/..." suffix ignored) resolves against the
  resourceType/id of every top-level file in the repository.
- Absolute and conditional references are reported, because nothing in the
  repository can resolve them.

Two files that share a resourceType/id are also reported, because the one
uploaded last overwrites the other on a server, unless the resourceType/id
is listed in the allowed duplicates file.

Problems in files matching the quarantine file are ignored. Problems are
printed, written to the GitHub step summary when running in Actions, and
cause a non-zero exit.
"""

import argparse
import fnmatch
import json
import os
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

DEFAULT_QUARANTINE = Path(__file__).with_name("reference_integrity_quarantine")
DEFAULT_ALLOWED_DUPLICATES = Path(__file__).with_name("reference_integrity_allowed_duplicates")

# Literal reference shape from http://hl7.org/fhir/R4/references.html
RELATIVE_REFERENCE = re.compile(
    r"^(?P<type>[A-Z][A-Za-z]+)/(?P<id>[A-Za-z0-9\-.]{1,64})(/_history/[A-Za-z0-9\-.]{1,64})?$"
)
BUNDLE_LOCAL_REFERENCE = re.compile(r"^urn:(uuid|oid):")

SKIPPED_DIRS = {".git", "node_modules"}


@dataclass(frozen=True)
class Problem:
    path: str
    message: str


@dataclass(frozen=True)
class BundleContext:
    full_urls: frozenset
    keys: frozenset


def load_list(path):
    """Return the non-comment lines of a list file, or [] if it does not exist."""
    try:
        lines = Path(path).read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        return []
    return [line.strip() for line in lines if line.strip() and not line.strip().startswith("#")]


def iter_json_files(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIPPED_DIRS)
        for name in sorted(filenames):
            if name.endswith(".json"):
                yield Path(dirpath) / name


def resource_key(resource):
    return f"{resource.get('resourceType')}/{resource.get('id')}"


def iter_literal_references(node):
    """Yield the literal references in node.

    Stops at "contained" and "entry" so that contained resources and Bundle
    entries are checked in their own context.
    """
    if isinstance(node, dict):
        for key, value in node.items():
            if key in ("contained", "entry"):
                continue
            if key == "reference" and isinstance(value, str):
                yield value
            elif key == "url" and isinstance(value, str) and is_attachment_link(node, value):
                yield value
            else:
                yield from iter_literal_references(value)
    elif isinstance(node, list):
        for item in node:
            yield from iter_literal_references(item)


def is_attachment_link(node, value):
    if RELATIVE_REFERENCE.match(value):
        return True
    return "contentType" in node and bool(BUNDLE_LOCAL_REFERENCE.match(value))


class Checker:
    def __init__(self, root, quarantine_patterns=(), allowed_duplicates=()):
        self.root = Path(root)
        self.quarantine = list(quarantine_patterns)
        self.allowed_duplicates = set(allowed_duplicates)
        self.index = defaultdict(list)
        self.resources = {}
        self.problems = []

    def run(self):
        for path in iter_json_files(self.root):
            self._load(path)
        self._check_duplicates()
        for rel_path, resource in self.resources.items():
            self._check_resource(rel_path, resource, bundle=None)
        return sorted(
            (p for p in self.problems if not self._is_quarantined(p.path)),
            key=lambda p: (p.path, p.message),
        )

    def _is_quarantined(self, rel_path):
        return any(fnmatch.fnmatchcase(rel_path, pattern) for pattern in self.quarantine)

    def _load(self, path):
        rel_path = path.relative_to(self.root).as_posix()
        try:
            resource = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            self.problems.append(Problem(rel_path, f"Cannot parse file: {exc}"))
            return
        if not isinstance(resource, dict) or "resourceType" not in resource:
            return  # Not a FHIR resource.
        if "id" in resource:
            self.index[resource_key(resource)].append(rel_path)
        else:
            self.problems.append(Problem(rel_path, "Resource has no id, so nothing can reference it."))
        self.resources[rel_path] = resource

    def _check_duplicates(self):
        for key, paths in self.index.items():
            if len(paths) < 2 or key in self.allowed_duplicates:
                continue
            for path in paths:
                others = ", ".join(p for p in paths if p != path)
                self.problems.append(Problem(path, f"Duplicate resource '{key}', also defined in {others}."))

    def _check_resource(self, rel_path, resource, bundle):
        """Check resource and its contained resources, then any Bundle entries.

        A Bundle's own elements (e.g. Bundle.signature.who) and its entries
        resolve against the Bundle's entries.
        """
        inner = []
        if resource.get("resourceType") == "Bundle":
            entries = [e for e in resource.get("entry", []) if isinstance(e, dict)]
            inner = [e["resource"] for e in entries if isinstance(e.get("resource"), dict)]
            bundle = BundleContext(
                full_urls=frozenset(e["fullUrl"] for e in entries if "fullUrl" in e),
                keys=frozenset(resource_key(r) for r in inner),
            )

        for container in [resource, *resource.get("contained", [])]:
            where = "" if container is resource else f" (in contained '#{container.get('id')}')"
            for reference in iter_literal_references(container):
                problem = self._resolve(reference, resource, bundle)
                if problem:
                    self.problems.append(Problem(rel_path, f"Reference '{reference}'{where}: {problem}"))

        for entry_resource in inner:
            self._check_resource(rel_path, entry_resource, bundle)

    def _resolve(self, reference, resource, bundle):
        """Return None when reference resolves, otherwise why it does not."""
        if reference.startswith("#"):
            target = reference[1:]
            if not target or any(c.get("id") == target for c in resource.get("contained", [])):
                return None
            return "no contained resource has that id."

        match = RELATIVE_REFERENCE.match(reference)
        key = f"{match['type']}/{match['id']}" if match else None

        if bundle is not None and (reference in bundle.full_urls or key in bundle.keys):
            return None
        if BUNDLE_LOCAL_REFERENCE.match(reference):
            return "no Bundle entry has this fullUrl." if bundle else "only resolvable inside a Bundle."
        if key:
            return None if key in self.index else "not found in any resource."
        if "?" in reference:
            return "conditional references cannot be resolved against the test data."
        return "not a relative Type/id reference, so it cannot be resolved against the test data."


def write_step_summary(problems):
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    lines = ["## Reference Integrity Check", ""]
    if problems:
        lines += [f"{len(problems)} problem(s) found.", "", "| File | Problem |", "|---|---|"]
        lines += [f"| {p.path} | {p.message.replace('|', '&#124;')} |" for p in problems]
    else:
        lines.append("All references resolve.")
    with open(summary_path, "a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check that references between test data files resolve.")
    parser.add_argument("root", nargs="?", default=".", help="directory to scan (default: current directory)")
    parser.add_argument("--quarantine", default=DEFAULT_QUARANTINE, help="file listing paths to ignore")
    parser.add_argument(
        "--allowed-duplicates", default=DEFAULT_ALLOWED_DUPLICATES,
        help="file listing resourceType/id values that may be defined in more than one file",
    )
    args = parser.parse_args(argv)

    problems = Checker(
        args.root, load_list(args.quarantine), load_list(args.allowed_duplicates)
    ).run()
    for problem in problems:
        print(f"{problem.path}: {problem.message}")
    write_step_summary(problems)
    if problems:
        print(f"\n{len(problems)} reference integrity problem(s) found.", file=sys.stderr)
        return 1
    print("All references resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
