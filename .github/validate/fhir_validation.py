#!/usr/bin/env python3
"""Run the HL7 FHIR validator over test data and report the results.

Selects FHIR JSON files under au-fhir-test-data-set, drops quarantined
ones, groups the rest by top-level folder, validates each group against
the implementation guides mapped to that folder in igs.json, and turns
the validator's OperationOutcome output into a GitHub job summary and
workflow-command annotations.

Exit codes:
  0  validation ran (findings are reported, not fatal, unless
     --fail-on-errors is set)
  1  validation ran, found errors, and --fail-on-errors is set
  2  infrastructure failure: bad configuration, the validator did not
     start, a package could not be loaded, or no output was written

Standard library only, so it runs on a bare GitHub runner.
"""

from __future__ import annotations

import argparse
import collections
import fnmatch
import json
import os
import re
import shlex
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

DATA_ROOT = "au-fhir-test-data-set"
HERE = Path(__file__).resolve().parent
DEFAULT_IGS = HERE / "igs.json"
DEFAULT_QUARANTINE = HERE / "validator_quarantine"

EXT_FILE = "http://hl7.org/fhir/StructureDefinition/operationoutcome-file"
EXT_LINE = "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line"
EXT_COL = "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col"
EXT_MESSAGE_ID = "http://hl7.org/fhir/StructureDefinition/operationoutcome-message-id"

# GitHub shows at most 10 warning annotations per step; more are dropped
# silently, so emit only that many and say so in the summary.
DEFAULT_MAX_ANNOTATIONS = 10
# Keep the job summary well under GitHub's 1 MiB step summary limit.
MAX_SUMMARY_ROWS = 300
TOP_MESSAGES_PER_FILE = 3
TOP_MESSAGES_OVERALL = 10


class ConfigError(Exception):
    """Bad input or configuration; reported as an infrastructure failure."""


class ValidatorError(Exception):
    """The validator failed to produce results."""


# ---------------------------------------------------------------------------
# Configuration


def load_ig_map(path: Path) -> tuple[str, dict[str, list[str]]]:
    """Return (fhirVersion, {folder: [package#version, ...]})."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ConfigError(f"cannot read IG mapping {path}: {exc}") from exc
    folders = data.get("folders")
    if not isinstance(folders, dict):
        raise ConfigError(f"{path}: 'folders' must be an object")
    for folder, igs in folders.items():
        if not isinstance(igs, list) or not all(isinstance(i, str) and "#" in i for i in igs):
            raise ConfigError(f"{path}: folder {folder!r} must map to a list of 'package#version' strings")
    return str(data.get("fhirVersion", "4.0.1")), folders


def load_quarantine(path: Path) -> list[tuple[str, str]]:
    """Return [(pattern, justification)]; every entry needs a justification."""
    if not path.exists():
        return []
    entries = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        pattern, sep, reason = line.partition("#")
        pattern, reason = pattern.strip(), reason.strip()
        if not sep or not reason:
            raise ConfigError(
                f"{path}:{lineno}: quarantine entry {pattern!r} has no justification; "
                "add '  # <reason>' after the path"
            )
        entries.append((pattern, reason))
    return entries


def is_quarantined(rel_path: str, quarantine: list[tuple[str, str]]) -> str | None:
    for pattern, reason in quarantine:
        if fnmatch.fnmatchcase(rel_path, pattern):
            return reason
    return None


# ---------------------------------------------------------------------------
# File selection


def expand_targets(targets: list[str], repo_root: Path) -> list[str]:
    """Expand files, folders and globs into sorted repo-relative JSON paths.

    Paths that do not exist (for example a file deleted in a PR) are
    skipped. Only files under au-fhir-test-data-set are kept.
    """
    found: set[str] = set()
    for target in targets:
        target = target.strip()
        if not target:
            continue
        if any(ch in target for ch in "*?["):
            candidates = [p for p in repo_root.glob(target) if p.is_file()]
        else:
            path = repo_root / target
            if path.is_dir():
                candidates = [p for p in path.rglob("*.json") if p.is_file()]
            elif path.is_file():
                candidates = [path]
            else:
                candidates = []
        for p in candidates:
            try:
                rel = p.resolve().relative_to(repo_root.resolve()).as_posix()
            except ValueError:
                continue  # outside the repo, e.g. via '..' or a symlink
            if rel.endswith(".json") and rel.startswith(DATA_ROOT + "/"):
                found.add(rel)
    return sorted(found)


def folder_of(rel_path: str) -> str:
    """Top-level folder under the data root, or '' for files at the root."""
    parts = rel_path.split("/")
    return parts[1] if len(parts) > 2 else ""


@dataclass
class Group:
    folder: str
    igs: list[str]
    files: list[str] = field(default_factory=list)

    @property
    def mapped(self) -> bool:
        return bool(self.igs)

    @property
    def slug(self) -> str:
        return self.folder or "root"


def group_files(files: list[str], ig_map: dict[str, list[str]], ig_override: list[str] | None = None) -> list[Group]:
    groups: dict[str, Group] = {}
    for rel in files:
        folder = folder_of(rel)
        if folder not in groups:
            igs = ig_override if ig_override else ig_map.get(folder, [])
            groups[folder] = Group(folder, list(igs))
        groups[folder].files.append(rel)
    return [groups[k] for k in sorted(groups)]


# ---------------------------------------------------------------------------
# Running the validator


def build_command(jar: Path, group: Group, fhir_version: str, tx: str, json_out: Path, html_out: Path) -> list[str]:
    cmd = ["java", "-jar", str(jar)]
    cmd += group.files
    cmd += ["-version", fhir_version, "-tx", tx, "-sct", "au", "-jurisdiction", "au"]
    for ig in group.igs:
        cmd += ["-ig", ig]
    cmd += ["-level", "warnings", "-output", str(json_out), "-html-output", str(html_out)]
    return cmd


def log_tail(log_path: Path, lines: int = 15) -> str:
    """Last log lines without Java stack frames, which bury the cause."""
    try:
        text = log_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return "(no log)"
    kept = [line for line in text.splitlines() if not re.match(r"\s+at |\s*\.\.\. \d+ more", line)]
    return "\n".join(kept[-lines:])


def run_validator(cmd: list[str], log_path: Path, cwd: Path) -> int:
    print(f"::group::{shlex.join(cmd[:3])} <{len(cmd)} args>", flush=True)
    with log_path.open("w", encoding="utf-8") as log:
        proc = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        assert proc.stdout is not None
        for line in proc.stdout:
            log.write(line)
            sys.stdout.write(line)
        code = proc.wait()
    print("::endgroup::", flush=True)
    return code


# ---------------------------------------------------------------------------
# Parsing validator output


@dataclass
class Issue:
    severity: str
    message: str
    location: str = ""
    line: int | None = None
    col: int | None = None
    message_id: str = ""


@dataclass
class FileResult:
    path: str
    issues: list[Issue] = field(default_factory=list)

    def count(self, *severities: str) -> int:
        return sum(1 for i in self.issues if i.severity in severities)

    @property
    def errors(self) -> int:
        return self.count("fatal", "error")

    @property
    def warnings(self) -> int:
        return self.count("warning")


def _ext(element: dict, url: str):
    for ext in element.get("extension", []) or []:
        if ext.get("url") == url:
            for key, value in ext.items():
                if key.startswith("value"):
                    return value
    return None


def _relative(path: str, repo_root: Path) -> str:
    if not path:
        return path
    p = Path(path)
    if p.is_absolute():
        try:
            return p.resolve().relative_to(repo_root.resolve()).as_posix()
        except ValueError:
            return path
    return p.as_posix()


def parse_operation_outcome(oo: dict, repo_root: Path) -> FileResult:
    path = _relative(_ext(oo, EXT_FILE) or "", repo_root)
    result = FileResult(path)
    for issue in oo.get("issue", []) or []:
        severity = issue.get("severity", "error")
        details = issue.get("details") or {}
        message = details.get("text") or issue.get("diagnostics") or issue.get("code", "")
        location = ", ".join(issue.get("expression") or issue.get("location") or [])
        line = _ext(issue, EXT_LINE)
        col = _ext(issue, EXT_COL)
        result.issues.append(
            Issue(
                severity=severity,
                message=str(message),
                location=location,
                line=int(line) if line is not None else None,
                col=int(col) if col is not None else None,
                message_id=str(_ext(issue, EXT_MESSAGE_ID) or ""),
            )
        )
    return result


def parse_output(data: dict, repo_root: Path) -> list[FileResult]:
    """Parse validator -output JSON: one OperationOutcome or a Bundle of them."""
    rtype = data.get("resourceType")
    if rtype == "OperationOutcome":
        outcomes = [data]
    elif rtype == "Bundle":
        outcomes = [e.get("resource", {}) for e in data.get("entry", []) or []]
        outcomes = [o for o in outcomes if o.get("resourceType") == "OperationOutcome"]
    else:
        raise ValidatorError(f"unexpected validator output resourceType {rtype!r}")
    return [parse_operation_outcome(oo, repo_root) for oo in outcomes]


# ---------------------------------------------------------------------------
# Reporting


def escape_data(value: str) -> str:
    return value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


def escape_property(value: str) -> str:
    return escape_data(value).replace(":", "%3A").replace(",", "%2C")


def annotation(result: FileResult, issue: Issue) -> str:
    props = [f"file={escape_property(result.path)}"]
    if issue.line:
        props.append(f"line={issue.line}")
    if issue.col:
        props.append(f"col={issue.col}")
    props.append(f"title={escape_property('FHIR validation error')}")
    message = issue.message
    if issue.location:
        message = f"{issue.location}: {message}"
    return f"::warning {','.join(props)}::{escape_data(message)}"


def normalise(message: str) -> str:
    """Drop the slice-evaluation context the validator appends.

    When an element is checked against several slice profiles, the same
    root message is repeated once per candidate with a trailing
    "(validating against <profile>)"; grouping on the root message keeps
    the summary readable.
    """
    return message.split(" (validating against ", 1)[0]


def annotations(results: list[FileResult], limit: int) -> list[str]:
    """One annotation per distinct error, spread across files.

    Takes each file's first distinct error, then each file's second, and
    so on, so a single noisy file cannot use up GitHub's per-step limit.
    """
    per_file: list[list[Issue]] = []
    for result in results:
        seen = set()
        distinct = []
        for issue in result.issues:
            if issue.severity not in ("fatal", "error"):
                continue
            key = (normalise(issue.message), issue.location)
            if key not in seen:
                seen.add(key)
                distinct.append(issue)
        per_file.append(distinct)
    lines: list[str] = []
    rank = 0
    while len(lines) < limit and any(rank < len(d) for d in per_file):
        for result, distinct in zip(results, per_file):
            if rank < len(distinct) and len(lines) < limit:
                lines.append(annotation(result, distinct[rank]))
        rank += 1
    return lines


def _cell(text: str, width: int = 160) -> str:
    text = " ".join(text.split())
    if len(text) > width:
        text = text[: width - 3] + "..."
    return text.replace("|", "\\|")


def top_messages(issues: list[Issue], n: int) -> list[tuple[str, int]]:
    counter = collections.Counter(normalise(i.message) for i in issues)
    return counter.most_common(n)


PROFILE_UNKNOWN = re.compile(r"Profile reference '([^']+)' has not been checked")


def unresolved_profiles(results: list[FileResult]) -> dict[str, set[str]]:
    """Declared meta.profile URLs the loaded IGs do not define: {url: {file}}."""
    found: dict[str, set[str]] = collections.defaultdict(set)
    for result in results:
        for issue in result.issues:
            if issue.message_id.upper().startswith("VALIDATION_VAL_PROFILE_UNKNOWN"):
                match = PROFILE_UNKNOWN.search(issue.message)
                found[match.group(1) if match else normalise(issue.message)].add(result.path)
    return dict(found)


@dataclass
class GroupReport:
    group: Group
    results: list[FileResult]


def render_summary(
    title: str,
    reports: list[GroupReport],
    skipped: list[tuple[str, str]],
    annotated: int,
    advisory: bool,
) -> str:
    all_results = [r for rep in reports for r in rep.results]
    total_errors = sum(r.errors for r in all_results)
    total_warnings = sum(r.warnings for r in all_results)
    out = [f"## {title}", ""]
    out.append(
        f"Validated **{len(all_results)}** file(s): **{total_errors}** error(s), **{total_warnings}** warning(s)."
    )
    if advisory:
        out.append("")
        out.append(
            "This check is advisory: findings do not fail the job. "
            "Errors are also shown as warning annotations on the changed files."
        )
    out.append("")
    out.append("| Folder | Implementation guides | Files | Errors | Warnings |")
    out.append("| --- | --- | ---: | ---: | ---: |")
    for rep in reports:
        g = rep.group
        igs = ", ".join(f"`{i}`" for i in g.igs) if g.igs else "base FHIR R4 only (folder not in igs.json)"
        out.append(
            f"| `{g.folder or DATA_ROOT}` | {igs} | {len(rep.results)} | "
            f"{sum(r.errors for r in rep.results)} | {sum(r.warnings for r in rep.results)} |"
        )
    unmapped = [rep.group for rep in reports if not rep.group.mapped]
    if unmapped:
        out.append("")
        out.append(
            "> [!NOTE]\n> "
            + ", ".join(f"`{g.folder or DATA_ROOT}`" for g in unmapped)
            + " has no entry in `.github/validate/igs.json`, so it was validated against base FHIR R4 only."
        )
    if skipped:
        out.append("")
        out.append(f"Skipped {len(skipped)} quarantined file(s) (see `.github/validate/validator_quarantine`):")
        out.append("")
        for path, reason in skipped:
            out.append(f"- `{path}`: {_cell(reason)}")

    unresolved = unresolved_profiles(all_results)
    if unresolved:
        out.append("")
        out.append("### Declared profiles not found in the loaded IGs")
        out.append("")
        out.append(
            "These `meta.profile` URLs are not defined by the pinned IG versions, so the files were not checked "
            "against them. Either the data claims a profile from a newer or unpublished IG version, or the "
            "folder needs another IG in `.github/validate/igs.json`."
        )
        out.append("")
        out.append("| Profile | Files |")
        out.append("| --- | ---: |")
        for url in sorted(unresolved, key=lambda u: (-len(unresolved[u]), u)):
            out.append(f"| `{_cell(url, 200)}` | {len(unresolved[url])} |")

    error_issues =[i for r in all_results for i in r.issues if i.severity in ("fatal", "error")]
    if error_issues:
        out.append("")
        out.append("### Most frequent errors")
        out.append("")
        out.append("| Count | Message |")
        out.append("| ---: | --- |")
        for message, count in top_messages(error_issues, TOP_MESSAGES_OVERALL):
            out.append(f"| {count} | {_cell(message, 300)} |")

    with_findings = [r for r in all_results if r.errors or r.warnings]
    with_findings.sort(key=lambda r: (-r.errors, -r.warnings, r.path))
    if with_findings:
        out.append("")
        out.append("### Files with findings")
        out.append("")
        out.append("| File | Errors | Warnings | Top messages |")
        out.append("| --- | ---: | ---: | --- |")
        for r in with_findings[:MAX_SUMMARY_ROWS]:
            ranked = [i for i in r.issues if i.severity in ("fatal", "error")] or r.issues
            msgs = "<br>".join(
                _cell(m) + (f" (x{c})" if c > 1 else "") for m, c in top_messages(ranked, TOP_MESSAGES_PER_FILE)
            )
            out.append(f"| `{r.path}` | {r.errors} | {r.warnings} | {msgs} |")
        if len(with_findings) > MAX_SUMMARY_ROWS:
            out.append("")
            out.append(
                f"{len(with_findings) - MAX_SUMMARY_ROWS} more file(s) with findings are listed in the HTML report artifact."
            )
    clean = len(all_results) - len(with_findings)
    out.append("")
    out.append(f"{clean} file(s) had no errors or warnings.")
    if total_errors > annotated:
        out.append("")
        out.append(
            f"Annotations show {annotated} of {total_errors} errors (GitHub displays at most "
            f"{DEFAULT_MAX_ANNOTATIONS} per step); the full list is in the HTML report artifact."
        )
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# Entry point


def read_targets(args: argparse.Namespace) -> list[str]:
    targets = list(args.paths)
    if args.paths_env and os.environ.get(args.paths_env):
        targets += os.environ[args.paths_env].splitlines()
    if args.paths_from:
        raw = Path(args.paths_from).read_bytes().decode("utf-8")
        sep = "\0" if "\0" in raw else "\n"
        targets += [t for t in raw.split(sep) if t.strip()]
    return targets


def write_summary(text: str, summary_path: str | None) -> None:
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as fh:
            fh.write(text)
    else:
        sys.stdout.write(text)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="*", help="files, folders or globs relative to the repo root")
    parser.add_argument("--paths-env", help="environment variable holding newline-separated targets")
    parser.add_argument("--paths-from", help="file of NUL- or newline-separated targets")
    parser.add_argument("--jar", required=True, type=Path, help="path to validator_cli.jar")
    parser.add_argument("--tx", default="https://tx.dev.hl7.org.au/fhir")
    parser.add_argument("--ig", default="", help="space-separated -ig override for every folder")
    parser.add_argument("--igs", type=Path, default=DEFAULT_IGS)
    parser.add_argument("--quarantine", type=Path, default=DEFAULT_QUARANTINE)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--out-dir", type=Path, default=Path("validation-output"))
    parser.add_argument("--title", default="FHIR validation")
    parser.add_argument("--max-annotations", type=int, default=DEFAULT_MAX_ANNOTATIONS)
    parser.add_argument("--fail-on-errors", action="store_true")
    parser.add_argument("--summary", default=os.environ.get("GITHUB_STEP_SUMMARY"))
    args = parser.parse_args(argv)

    try:
        fhir_version, ig_map = load_ig_map(args.igs)
        quarantine = load_quarantine(args.quarantine)
        if not args.jar.is_file():
            raise ConfigError(f"validator jar not found: {args.jar}")
        files = expand_targets(read_targets(args), args.repo_root)
    except ConfigError as exc:
        print(f"::error title=FHIR validation setup::{escape_data(str(exc))}")
        return 2

    skipped = []
    selected = []
    for rel in files:
        reason = is_quarantined(rel, quarantine)
        if reason is None:
            selected.append(rel)
        else:
            skipped.append((rel, reason))

    if not selected:
        write_summary(
            f"## {args.title}\n\nNo FHIR JSON files to validate"
            + (f" ({len(skipped)} quarantined)" if skipped else "")
            + ".\n",
            args.summary,
        )
        return 0

    override = args.ig.split() if args.ig.strip() else None
    groups = group_files(selected, ig_map, override)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    reports: list[GroupReport] = []
    for group in groups:
        json_out = (args.out_dir / f"{group.slug}.json").resolve()
        html_out = (args.out_dir / f"{group.slug}.html").resolve()
        log_out = (args.out_dir / f"{group.slug}.log").resolve()
        json_out.unlink(missing_ok=True)
        cmd = build_command(args.jar.resolve(), group, fhir_version, args.tx, json_out, html_out)
        code = run_validator(cmd, log_out, args.repo_root)
        # The validator exits non-zero when it finds errors, so the exit
        # code alone does not separate findings from a crash; missing or
        # unreadable output does.
        try:
            data = json.loads(json_out.read_text(encoding="utf-8"))
            results = parse_output(data, args.repo_root)
        except (OSError, json.JSONDecodeError, ValidatorError) as exc:
            tail = log_tail(log_out)
            print(
                f"::error title=FHIR validator failed ({group.slug})::"
                + escape_data(f"exit code {code}, no usable output ({exc}). Last log lines:\n{tail}")
            )
            write_summary(
                f"## {args.title}\n\nThe validator failed for `{group.folder or DATA_ROOT}` "
                f"(exit code {code}). Last log lines:\n\n```\n{tail}\n```\n",
                args.summary,
            )
            return 2
        if len(results) != len(group.files):
            print(
                f"::notice title=FHIR validation::{group.slug}: {len(group.files)} file(s) submitted, "
                f"{len(results)} result(s) returned"
            )
        reports.append(GroupReport(group, results))

    all_results = [r for rep in reports for r in rep.results]
    notes = annotations(all_results, args.max_annotations)
    for line in notes:
        print(line)
    write_summary(
        render_summary(args.title, reports, skipped, len(notes), advisory=not args.fail_on_errors),
        args.summary,
    )
    total_errors = sum(r.errors for r in all_results)
    if args.fail_on_errors and total_errors:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
