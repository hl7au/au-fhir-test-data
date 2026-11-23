"""Tests for fhir_validation.py. Run from this folder: python -m pytest -q"""

import argparse
import json
import os
from pathlib import Path

import pytest

import fhir_validation as fv

HERE = Path(__file__).resolve().parent
SAMPLE = HERE / "testdata" / "validator-output.json"
# Validator log (machine paths scrubbed) of a run that aborted on an
# empty file.
FAILED_LOG = HERE / "testdata" / "validator-failed-empty-file.log"


# ---------------------------------------------------------------------------
# Configuration files shipped in the repo


def test_repo_ig_map_is_valid_and_pins_exact_versions():
    version, folders = fv.load_ig_map(fv.DEFAULT_IGS)
    assert version == "4.0.1"
    assert {"au-core", "au-erequesting", "au-patient-summary", "connected-care", "au-base"} <= set(folders)
    for igs in folders.values():
        for ig in igs:
            package, _, pinned = ig.partition("#")
            assert package.startswith("hl7.fhir.au.")
            # Ballot and draft versions are allowed; moving builds are not.
            assert pinned and pinned not in ("current", "dev")


def test_repo_quarantine_parses():
    assert isinstance(fv.load_quarantine(fv.DEFAULT_QUARANTINE), list)


def test_ig_map_rejects_unpinned_entries(tmp_path):
    bad = tmp_path / "igs.json"
    bad.write_text(json.dumps({"folders": {"au-core": ["hl7.fhir.au.core"]}}))
    with pytest.raises(fv.ConfigError):
        fv.load_ig_map(bad)


# ---------------------------------------------------------------------------
# Quarantine


def test_quarantine_requires_justification(tmp_path):
    q = tmp_path / "q"
    q.write_text("# header\n\nau-fhir-test-data-set/au-core/A.json\n")
    with pytest.raises(fv.ConfigError, match="no justification"):
        fv.load_quarantine(q)


def test_quarantine_paths_and_globs(tmp_path):
    q = tmp_path / "q"
    q.write_text(
        "# header comment\n"
        "au-fhir-test-data-set/au-core/A.json  # broken upstream profile\n"
        "au-fhir-test-data-set/connected-care/*/Binary-*.json # binaries are attachments\n"
    )
    entries = fv.load_quarantine(q)
    assert entries[0] == ("au-fhir-test-data-set/au-core/A.json", "broken upstream profile")
    assert fv.is_quarantined("au-fhir-test-data-set/au-core/A.json", entries) == "broken upstream profile"
    assert fv.is_quarantined("au-fhir-test-data-set/connected-care/alex-story/Binary-x.json", entries)
    assert fv.is_quarantined("au-fhir-test-data-set/au-core/B.json", entries) is None


def test_missing_quarantine_file_is_empty(tmp_path):
    assert fv.load_quarantine(tmp_path / "absent") == []


# ---------------------------------------------------------------------------
# Selection and grouping


@pytest.fixture
def repo(tmp_path):
    root = tmp_path / "repo"
    for rel in [
        "au-fhir-test-data-set/au-core/Patient-a.json",
        "au-fhir-test-data-set/au-core/Patient-b.json",
        "au-fhir-test-data-set/connected-care/alex-story/Condition-c.json",
        "au-fhir-test-data-set/connected-care/alex-story/Alex Story Data Set.md",
        "au-fhir-test-data-set/new-folder/Observation-d.json",
        "au-fhir-test-data-set/Loose.json",
        "elsewhere/Patient-x.json",
    ]:
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text('{"resourceType": "Patient"}')
    return root


def test_expand_targets_folders_files_globs_and_missing(repo):
    files = fv.expand_targets(
        [
            "au-fhir-test-data-set/connected-care",
            "au-fhir-test-data-set/au-core/Patient-a.json",
            "au-fhir-test-data-set/au-core/Deleted.json",
            "au-fhir-test-data-set/new-folder/*.json",
            "elsewhere/Patient-x.json",
            "",
        ],
        repo,
    )
    assert files == [
        "au-fhir-test-data-set/au-core/Patient-a.json",
        "au-fhir-test-data-set/connected-care/alex-story/Condition-c.json",
        "au-fhir-test-data-set/new-folder/Observation-d.json",
    ]


def test_group_files_by_top_level_folder(repo):
    ig_map = {"au-core": ["hl7.fhir.au.core#2.0.0"], "connected-care": ["hl7.fhir.au.core#2.0.0", "hl7.fhir.au.ps#1.0.0"]}
    files = fv.expand_targets(["au-fhir-test-data-set"], repo)
    groups = fv.group_files(files, ig_map)
    by_folder = {g.folder: g for g in groups}
    assert set(by_folder) == {"", "au-core", "connected-care", "new-folder"}
    assert by_folder["au-core"].files == [
        "au-fhir-test-data-set/au-core/Patient-a.json",
        "au-fhir-test-data-set/au-core/Patient-b.json",
    ]
    assert by_folder["connected-care"].igs == ["hl7.fhir.au.core#2.0.0", "hl7.fhir.au.ps#1.0.0"]
    assert not by_folder["new-folder"].mapped
    assert by_folder[""].slug == "root"


def test_group_files_with_override():
    groups = fv.group_files(["au-fhir-test-data-set/au-core/A.json"], {"au-core": ["x#1"]}, ["y#2"])
    assert groups[0].igs == ["y#2"]


def test_build_command_includes_every_ig_and_fixed_options(tmp_path):
    group = fv.Group("connected-care", ["a#1", "b#2"], ["f1.json", "f2.json"])
    cmd = fv.build_command(Path("v.jar"), group, "4.0.1", "https://tx", tmp_path / "o.json", tmp_path / "o.html")
    assert cmd[:5] == ["java", "-jar", "v.jar", "f1.json", "f2.json"]
    joined = " ".join(cmd)
    assert "-ig a#1 -ig b#2" in joined
    assert "-version 4.0.1 -tx https://tx -sct au -jurisdiction au" in joined
    assert "-output" in cmd and "-html-output" in cmd


def test_unmapped_group_has_no_ig_flags(tmp_path):
    group = fv.Group("new-folder", [], ["f.json"])
    cmd = fv.build_command(Path("v.jar"), group, "4.0.1", "https://tx", tmp_path / "o.json", tmp_path / "o.html")
    assert "-ig" not in cmd


# ---------------------------------------------------------------------------
# Parsing captured validator output


@pytest.fixture
def sample():
    return json.loads(SAMPLE.read_text(encoding="utf-8"))


def test_parse_captured_bundle(sample, tmp_path):
    results = fv.parse_output(sample, tmp_path)
    assert len(results) == len(sample["entry"])
    assert all(r.path.startswith("au-fhir-test-data-set/") for r in results)
    assert all(not Path(r.path).is_absolute() for r in results)
    assert sum(r.errors for r in results) > 0
    first_error = next(i for r in results for i in r.issues if i.severity == "error")
    assert first_error.message
    assert first_error.line and first_error.line > 0


def test_parse_single_operation_outcome(tmp_path):
    oo = {
        "resourceType": "OperationOutcome",
        "extension": [{"url": fv.EXT_FILE, "valueString": str(tmp_path / "au-fhir-test-data-set/au-core/A.json")}],
        "issue": [
            {
                "extension": [
                    {"url": fv.EXT_LINE, "valueInteger": 7},
                    {"url": fv.EXT_COL, "valueInteger": 3},
                ],
                "severity": "error",
                "code": "processing",
                "details": {"text": "Bad thing"},
                "expression": ["Patient.name[0]"],
            },
            {"severity": "warning", "code": "processing", "diagnostics": "Meh"},
            {"severity": "information", "code": "informational", "details": {"text": "FYI"}},
        ],
    }
    [result] = fv.parse_output(oo, tmp_path)
    assert result.path == "au-fhir-test-data-set/au-core/A.json"
    assert (result.errors, result.warnings) == (1, 1)
    assert result.issues[0].line == 7 and result.issues[0].col == 3
    assert result.issues[1].message == "Meh"


def test_parse_rejects_unexpected_output(tmp_path):
    with pytest.raises(fv.ValidatorError):
        fv.parse_output({"resourceType": "Patient"}, tmp_path)


# ---------------------------------------------------------------------------
# Reporting


def test_annotations_are_warnings_for_errors_only_and_capped(sample, tmp_path):
    results = fv.parse_output(sample, tmp_path)
    notes = fv.annotations(results, 3)
    assert 0 < len(notes) <= 3
    assert all(n.startswith("::warning file=au-fhir-test-data-set/") for n in notes)
    assert all("\n" not in n for n in notes)


def test_annotations_spread_across_files():
    noisy = fv.FileResult("a.json", [fv.Issue("error", f"e{i}", line=i + 1) for i in range(20)])
    quiet = fv.FileResult("b.json", [fv.Issue("error", "only one", line=1)])
    notes = fv.annotations([noisy, quiet], 4)
    assert len(notes) == 4
    assert sum("file=b.json" in n for n in notes) == 1


def test_annotations_skip_repeated_slice_messages():
    result = fv.FileResult(
        "a.json",
        [
            fv.Issue("error", "Unknown code 'X'", location="P.code"),
            fv.Issue("error", "Unknown code 'X' (validating against http://p|1 [P])", location="P.code"),
        ],
    )
    assert len(fv.annotations([result], 10)) == 1


def test_captured_output_reports_unresolved_declared_profile(sample, tmp_path):
    results = fv.parse_output(sample, tmp_path)
    unresolved = fv.unresolved_profiles(results)
    assert unresolved == {
        "http://hl7.org.au/fhir/core/StructureDefinition/au-core-diagnosticreport": {
            "au-fhir-test-data-set/au-core/DiagnosticReport-bmd-report.json"
        }
    }
    groups = [fv.GroupReport(fv.Group("au-core", ["hl7.fhir.au.core#2.0.0"], []), results)]
    text = fv.render_summary("FHIR validation", groups, [], annotated=0, advisory=True)
    assert "### Declared profiles not found in the loaded IGs" in text


def test_normalise_drops_slice_context():
    assert fv.normalise("Bad (validating against http://x|1 [X]) (validating against y)") == "Bad"
    assert fv.normalise("Plain") == "Plain"


def test_annotation_escaping():
    result = fv.FileResult("dir/a,b:c.json")
    issue = fv.Issue("error", "50% wrong\nnext line", location="Patient.x", line=4)
    line = fv.annotation(result, issue)
    assert line.startswith("::warning file=dir/a%2Cb%3Ac.json,line=4,")
    assert line.endswith("::Patient.x: 50%25 wrong%0Anext line")


def test_summary_from_captured_output(sample, tmp_path):
    results = fv.parse_output(sample, tmp_path)
    groups = [
        fv.GroupReport(fv.Group("au-core", ["hl7.fhir.au.core#2.0.0"], [r.path for r in results]), results),
        fv.GroupReport(fv.Group("new-folder", [], []), []),
    ]
    text = fv.render_summary("FHIR validation", groups, [("x.json", "known | issue")], annotated=1, advisory=True)
    assert text.startswith("## FHIR validation")
    assert "advisory" in text
    assert "| `au-core` | `hl7.fhir.au.core#2.0.0` |" in text
    assert "base FHIR R4 only" in text
    assert "### Most frequent errors" in text
    assert "### Files with findings" in text
    assert "known \\| issue" in text
    assert chr(0x2014) not in text and chr(0x2013) not in text


# ---------------------------------------------------------------------------
# End to end with a stub validator


def _stub_jar(tmp_path, body):
    """A fake 'java' on PATH that runs the given Python body."""
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    java = bin_dir / "java"
    java.write_text("#!/usr/bin/env python3\nimport sys, json\nargs = sys.argv[1:]\n" + body)
    java.chmod(0o755)
    jar = tmp_path / "validator_cli.jar"
    jar.write_text("")
    return bin_dir, jar


def _run_main(monkeypatch, tmp_path, repo, body, *extra):
    bin_dir, jar = _stub_jar(tmp_path, body)
    monkeypatch.setenv("PATH", f"{bin_dir}:{os.environ['PATH']}")
    summary = tmp_path / "summary.md"
    code = fv.main(
        [
            "au-fhir-test-data-set/au-core",
            "--jar", str(jar),
            "--repo-root", str(repo),
            "--igs", str(fv.DEFAULT_IGS),
            "--quarantine", str(tmp_path / "none"),
            "--out-dir", str(tmp_path / "out"),
            "--summary", str(summary),
            *extra,
        ]
    )
    return code, summary.read_text() if summary.exists() else ""


WRITE_ONE_ERROR = """
out = args[args.index("-output") + 1]
files = [a for a in args[2:] if a.endswith(".json") and not a.startswith("-")]
files = files[: len(files)]
oos = [{"resourceType": "OperationOutcome",
        "extension": [{"url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-file", "valueString": f}],
        "issue": [{"severity": "error", "code": "processing", "details": {"text": "Bad"},
                   "extension": [{"url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line", "valueInteger": 1}]}]}
       for f in files if f != out]
json.dump({"resourceType": "Bundle", "type": "collection", "entry": [{"resource": o} for o in oos]}, open(out, "w"))
sys.exit(1)
"""


def test_main_findings_are_advisory(monkeypatch, tmp_path, repo, capsys):
    code, summary = _run_main(monkeypatch, tmp_path, repo, WRITE_ONE_ERROR)
    assert code == 0
    assert "**2** error(s)" in summary
    assert capsys.readouterr().out.count("::warning file=au-fhir-test-data-set/au-core/") == 2


def test_main_fail_on_errors(monkeypatch, tmp_path, repo):
    code, _ = _run_main(monkeypatch, tmp_path, repo, WRITE_ONE_ERROR, "--fail-on-errors")
    assert code == 1


def test_main_validator_crash_is_infrastructure_failure(monkeypatch, tmp_path, repo, capsys):
    code, summary = _run_main(
        monkeypatch,
        tmp_path,
        repo,
        "print('Unable to find package hl7.fhir.au.core#9.9.9')\n"
        "for n in range(40): print(f'\\tat org.hl7.Frame{n}(X.java:1)')\n"
        "sys.exit(1)\n",
    )
    assert code == 2
    assert "Unable to find package" in summary
    assert "Frame" not in summary
    assert "::error title=FHIR validator failed" in capsys.readouterr().out


def test_main_nothing_to_validate(monkeypatch, tmp_path, repo):
    bin_dir, jar = _stub_jar(tmp_path, "sys.exit(99)\n")
    summary = tmp_path / "s.md"
    code = fv.main(["au-fhir-test-data-set/absent", "--jar", str(jar), "--repo-root", str(repo), "--summary", str(summary)])
    assert code == 0
    assert "No FHIR JSON files to validate" in summary.read_text()


# ---------------------------------------------------------------------------
# Literal path lists (--paths-from)


@pytest.fixture
def odd_names(repo):
    names = ["Patient-[1].json", "Patient-?.json", "Patient-*.json", "Patient with space.json"]
    for name in names:
        (repo / "au-fhir-test-data-set/au-core" / name).write_text('{"resourceType": "Patient"}')
    return [f"au-fhir-test-data-set/au-core/{n}" for n in names]


def test_literal_paths_keep_glob_characters(repo, odd_names):
    assert fv.expand_targets(odd_names, repo, literal=True) == sorted(odd_names)
    # As a glob, "[1]" is a character class, so the file is not matched.
    assert "au-fhir-test-data-set/au-core/Patient-[1].json" not in fv.expand_targets([odd_names[0]], repo)


def test_literal_paths_still_expand_folders(repo):
    assert fv.expand_targets(["au-fhir-test-data-set/au-core"], repo, literal=True) == [
        "au-fhir-test-data-set/au-core/Patient-a.json",
        "au-fhir-test-data-set/au-core/Patient-b.json",
    ]


@pytest.mark.parametrize("sep", ["\0", "\n"])
def test_paths_from_file_is_literal(tmp_path, repo, odd_names, sep):
    listing = tmp_path / "paths"
    listing.write_text(sep.join(odd_names + ["au-fhir-test-data-set/au-core/Deleted.json"]) + sep)
    args = argparse.Namespace(paths=[], paths_env=None, paths_from=str(listing))
    patterns, literals = fv.read_targets(args)
    assert patterns == []
    assert fv.expand_targets(literals, repo, literal=True) == sorted(odd_names)


def test_main_reads_a_large_path_list_from_file(monkeypatch, tmp_path, repo, odd_names, capsys):
    # Over 128 KiB, the most one environment variable can hold on Linux.
    padding = [f"au-fhir-test-data-set/au-core/deleted-{n:05d}.json" for n in range(4000)]
    listing = tmp_path / "paths"
    listing.write_text("".join(p + "\0" for p in padding + odd_names))
    assert listing.stat().st_size > 128 * 1024
    bin_dir, jar = _stub_jar(tmp_path, WRITE_ONE_ERROR)
    monkeypatch.setenv("PATH", f"{bin_dir}:{os.environ['PATH']}")
    summary = tmp_path / "summary.md"
    code = fv.main(
        ["--paths-from", str(listing), "--jar", str(jar), "--repo-root", str(repo),
         "--quarantine", str(tmp_path / "none"), "--out-dir", str(tmp_path / "out"), "--summary", str(summary)]
    )
    assert code == 0
    assert "Validated **4** file(s)" in summary.read_text()
    assert "Patient-%5B1%5D" not in capsys.readouterr().out  # paths are passed through unescaped
    assert "Patient-[1].json" in (tmp_path / "out" / "au-core.json").read_text()


# ---------------------------------------------------------------------------
# Files the validator cannot load


@pytest.mark.parametrize(
    ("content", "expected", "line"),
    [
        (b"", "File is empty", 1),
        (b"  \n", "File is empty", 1),
        (b'{\n  "resourceType": "Patient",\n', "not valid JSON", 3),
        (b"[1, 2]", "not a JSON object", 1),
        (b'{"id": "x"}', "no resourceType", 1),
        (b'{"resourceType": ""}', "no resourceType", 1),
        (b"\xff\xfe{}", "not valid UTF-8", None),
    ],
)
def test_prescreen_reports_unloadable_files(tmp_path, content, expected, line):
    (tmp_path / "f.json").write_bytes(content)
    issue = fv.prescreen("f.json", tmp_path)
    assert issue is not None and issue.severity == "error"
    assert expected in issue.message
    assert issue.line == line
    assert issue.message_id == fv.PRESCREEN_MESSAGE_ID


@pytest.mark.parametrize("content", [b'{"resourceType": "Patient"}', b'\xef\xbb\xbf{"resourceType": "Bundle"}'])
def test_prescreen_accepts_resources(tmp_path, content):
    (tmp_path / "f.json").write_bytes(content)
    assert fv.prescreen("f.json", tmp_path) is None


def test_main_reports_unloadable_files_and_validates_the_rest(monkeypatch, tmp_path, repo, capsys):
    core = repo / "au-fhir-test-data-set/au-core"
    (core / "empty.json").write_text("")
    (core / "broken.json").write_text('{"resourceType": ')
    # This stub aborts, like the real validator, if it is given the empty file.
    body = "if any(a.endswith('empty.json') for a in args): sys.exit(1)\n" + WRITE_ONE_ERROR
    code, summary = _run_main(monkeypatch, tmp_path, repo, body)
    assert code == 0
    out = capsys.readouterr().out
    assert "empty.json" not in (tmp_path / "out" / "au-core.json").read_text()
    assert "file=au-fhir-test-data-set/au-core/empty.json,line=1," in out
    assert "File is empty" in out and "File is not valid JSON" in out
    assert "Validated **4** file(s): **4** error(s)" in summary
    assert "| `au-core` | `hl7.fhir.au.core#3.0.0-ballot1`, `hl7.fhir.au.ereq#1.0.1` | 4 | 4 |" in summary


def test_main_skips_the_validator_when_no_file_is_loadable(monkeypatch, tmp_path, repo):
    for name in ("Patient-a.json", "Patient-b.json"):
        (repo / "au-fhir-test-data-set/au-core" / name).write_text("")
    code, summary = _run_main(monkeypatch, tmp_path, repo, "sys.exit(99)\n")
    assert code == 0
    assert "**2** error(s)" in summary


# ---------------------------------------------------------------------------
# Validator failures


def test_failed_file_from_captured_log():
    log = FAILED_LOG.read_text()
    files = [
        "au-fhir-test-data-set/au-erequesting/probe/broken.json",
        "au-fhir-test-data-set/au-erequesting/probe/empty.json",
    ]
    assert fv.failed_file(log, files) == "au-fhir-test-data-set/au-erequesting/probe/empty.json"
    assert fv.failure_reason(log).startswith("org.hl7.fhir.exceptions.FHIRException: Unable to find/resolve/read")


def test_failed_file_uses_last_validate_line():
    log = "Loading\n  Load a#1 - 3 resources\nValidating\n  Validate x.json\n 00:01\n  Validate y.json\nboom\n"
    assert fv.failed_file(log, ["x.json", "y.json"]) == "y.json"


def test_failed_file_is_none_when_failure_is_before_validation():
    log = "Loading\nUnable to find package hl7.fhir.au.core#9.9.9\n"
    assert fv.failed_file(log, ["x.json"]) is None


CRASH_ON_PATIENT_B = """
files = [a for a in args[2:] if a.endswith(".json") and "-output" not in a]
print("Validating")
for f in files:
    print("  Validate " + f)
    if f.endswith("Patient-b.json"):
        print("java.lang.NullPointerException: boom")
        sys.exit(1)
""" + WRITE_ONE_ERROR


def test_main_retries_once_without_the_file_the_validator_failed_on(monkeypatch, tmp_path, repo, capsys):
    code, summary = _run_main(monkeypatch, tmp_path, repo, CRASH_ON_PATIENT_B)
    assert code == 0
    out = capsys.readouterr().out
    assert "retrying the folder without it" in out
    assert "Validated **2** file(s)" in summary
    assert "The validator failed on this file: java.lang.NullPointerException: boom" in summary
    assert (tmp_path / "out" / "au-core-retry.log").exists()


def test_main_second_failure_is_infrastructure_failure_naming_the_file(monkeypatch, tmp_path, repo, capsys):
    body = """
print("Validating")
for f in [a for a in args[2:] if a.endswith(".json") and "-output" not in a]:
    print("  Validate " + f)
    print("java.lang.OutOfMemoryError: heap")
    sys.exit(1)
"""
    code, summary = _run_main(monkeypatch, tmp_path, repo, body)
    assert code == 2
    assert "while processing `au-fhir-test-data-set/au-core/Patient-b.json`" in summary
    assert "::error title=FHIR validator failed" in capsys.readouterr().out
