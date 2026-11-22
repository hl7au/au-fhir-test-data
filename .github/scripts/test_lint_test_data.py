import json

import pytest

from lint_test_data import (
    Problem, email_domain, is_reserved_domain, is_reserved_phone, lint, main, normalise_phone,
    parse_exceptions, workflow_command,
)


@pytest.fixture
def repo(tmp_path):
    def write(name, resource, text=None):
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((text if text is not None else json.dumps(resource, indent=2)).encode("utf-8"))

    write.root = tmp_path
    return write


def problems(root, exceptions=()):
    return [(p.path, p.rule, p.severity) for p in lint(root, exceptions)]


def patient(id="p1", **fields):
    return {"resourceType": "Patient", "id": id, **fields}


def phone(value, system="phone"):
    return {"system": system, "value": value}


def test_clean_file_passes(repo):
    repo("Patient-p1.json", patient(telecom=[phone("0491 570 006"), phone("p@example.org", "email")]))
    assert problems(repo.root) == []


def test_missing_id_is_an_error(repo):
    repo("Patient-p1.json", {"resourceType": "Patient"})
    assert problems(repo.root) == [("Patient-p1.json", "resource-id", "error")]


def test_file_name_must_match_resource(repo):
    repo("Patient-other.json", patient())
    assert problems(repo.root) == [("Patient-other.json", "file-name", "warning")]
    [problem] = lint(repo.root)
    assert "expected 'Patient-p1.json'" in problem.message


def test_ignores_non_fhir_json_and_dot_dirs(repo):
    repo("package.json", {"name": "x"})
    repo(".claude/worktrees/Patient-wrong.json", patient())
    assert problems(repo.root) == []


def test_unparseable_file_is_an_error(repo):
    repo("Patient-p1.json", None, text="{")
    assert problems(repo.root) == [("Patient-p1.json", "parse", "error")]


@pytest.mark.parametrize("value, expected", [
    ("(02) 5550 1234", "0255501234"),
    ("+61 2 7010 1234", "0270101234"),
    ("+61 (0)2 5550 1234", "0255501234"),
    ("61491570006", "0491570006"),
    ("0491-570-006", "0491570006"),
    ("1800.975.707", "1800975707"),
])
def test_normalise_phone(value, expected):
    assert normalise_phone(value) == expected


@pytest.mark.parametrize("number, reserved", [
    ("0255501234", True),
    ("0370109999", True),
    ("0755500000", True),
    ("0870101111", True),
    ("0455501234", False),  # 04 is mobile; only the listed mobiles are reserved.
    ("0262348907", False),
    ("0491570006", True),
    ("0491570007", False),
    ("1800975711", True),
    ("1300975712", False),
    ("270107520", False),  # Missing the leading 0.
])
def test_reserved_phone(number, reserved):
    assert is_reserved_phone(number) is reserved


@pytest.mark.parametrize("domain, reserved", [
    ("example.com", True),
    ("clinic.example.net", True),
    ("example.org", True),
    ("mail.example", True),
    ("x.test", True),
    ("foo.invalid", True),
    ("example.com.au", False),
    ("myownpersonaldomain.com", False),
    ("notexample.com", False),
    ("email.com", False),
])
def test_reserved_domain(domain, reserved):
    assert is_reserved_domain(domain) is reserved


def test_email_domain():
    assert email_domain("mailto:Jo@Clinic.Example.ORG") == "clinic.example.org"


def test_reports_contacts_in_contained_resources_and_bundle_entries(repo):
    practitioner = {"resourceType": "Practitioner", "id": "pr1", "telecom": [phone("0412 345 678")]}
    organization = {
        "resourceType": "Organization", "id": "o1",
        "contact": [{"telecom": [phone("(02) 6234 8907", "fax"), phone("a@email.com", "email")]}],
    }
    repo("Patient-p1.json", patient(contained=[practitioner]))
    repo("Bundle-b1.json", {"resourceType": "Bundle", "id": "b1", "entry": [{"resource": organization}]})
    assert problems(repo.root) == [
        ("Bundle-b1.json", "contact-email", "warning"),
        ("Bundle-b1.json", "contact-phone", "warning"),
        ("Patient-p1.json", "contact-phone", "warning"),
    ]


def test_ignores_identifier_and_url_systems(repo):
    repo("Patient-p1.json", patient(
        identifier=[{"system": "http://ns.electronichealth.net.au/id/medicare-number", "value": "1234567890"}],
        telecom=[phone("https://real.example.au", "url")],
    ))
    assert problems(repo.root) == []


def test_exceptions_match_rule_and_subject(repo):
    repo("Organization-o1.json", {"resourceType": "Organization", "id": "o1", "telecom": [phone("13 14 50")]})
    exceptions = parse_exceptions(["contact-phone 131450"])
    assert problems(repo.root, exceptions) == []
    assert problems(repo.root, parse_exceptions(["contact-email 131450"])) == [
        ("Organization-o1.json", "contact-phone", "warning"),
    ]


def test_bad_exception_line_is_rejected():
    with pytest.raises(ValueError):
        parse_exceptions(["no-such-rule x"])


def test_json_indent(repo):
    repo("Patient-p1.json", None, text=json.dumps(patient(), indent=4))
    repo("Patient-p2.json", None, text='{\n  "resourceType": "Patient",\n   "id": "p2"\n}')
    repo("Patient-p3.json", None, text='{\n\t"resourceType": "Patient",\n\t"id": "p3"\n}')
    repo("Patient-p4.json", None, text=json.dumps(patient("p4")))
    assert problems(repo.root) == [
        ("Patient-p1.json", "json-indent", "warning"),
        ("Patient-p2.json", "json-indent", "warning"),
        ("Patient-p3.json", "json-indent", "warning"),
    ]


def test_crlf_line_endings(repo):
    repo("Patient-p1.json", None, text=json.dumps(patient(), indent=2).replace("\n", "\r\n"))
    assert problems(repo.root) == [("Patient-p1.json", "line-endings", "warning")]


def test_trailing_newline_is_not_checked(repo):
    repo("Patient-p1.json", None, text=json.dumps(patient(), indent=2) + "\n")
    assert problems(repo.root) == []


def test_workflow_command_escapes():
    problem = Problem("a,b:c.json", "file-name", "50%\r\nnext")
    assert workflow_command(problem, ".") == "::warning file=a%2Cb%3Ac.json,title=file-name::50%25%0D%0Anext"


def test_main_exits_zero_on_warnings_and_writes_outputs(repo, tmp_path, monkeypatch, capsys):
    repo("data/Patient-other.json", patient())
    summary = tmp_path / "summary.md"
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(summary))
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    assert main([str(repo.root / "data"), "--exceptions", str(tmp_path / "none")]) == 0
    out = capsys.readouterr().out
    assert "Patient-other.json: warning: [file-name]" in out
    assert f"::warning file={(repo.root / 'data' / 'Patient-other.json').as_posix()}" in out
    assert "| warning | file-name | 1 |" in summary.read_text()


def test_main_exits_one_on_errors(repo, tmp_path, monkeypatch):
    monkeypatch.delenv("GITHUB_STEP_SUMMARY", raising=False)
    repo("Patient-p1.json", {"resourceType": "Patient"})
    assert main([str(repo.root), "--exceptions", str(tmp_path / "none")]) == 1


@pytest.fixture
def pr_repo(repo, tmp_path, monkeypatch):
    """A repo with a warning in a changed and an unchanged file, run from its root as in Actions."""
    repo("data/Patient-changed.json", patient())
    repo("data/Patient-unchanged.json", patient())
    monkeypatch.chdir(repo.root)
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(tmp_path / "summary.md"))
    (tmp_path / "changed.txt").write_text("data/Patient-changed.json\nREADME.md\n\n")
    return repo


def run_pr(tmp_path, capsys, root="."):
    status = main([root, "--exceptions", str(tmp_path / "none"), "--changed-files", str(tmp_path / "changed.txt")])
    out = capsys.readouterr().out
    annotations = [line for line in out.splitlines() if line.startswith("::")]
    return status, out, annotations, (tmp_path / "summary.md").read_text()


def test_changed_files_limit_annotations(pr_repo, tmp_path, capsys):
    status, out, annotations, _ = run_pr(tmp_path, capsys)
    assert status == 0
    assert annotations == [
        "::warning file=data/Patient-changed.json,title=file-name::"
        "File name does not match the resource; expected 'Patient-p1.json'.",
    ]
    # Every problem is still printed.
    assert "data/Patient-unchanged.json: warning: [file-name]" in out


def test_changed_files_match_when_scanning_a_subdirectory(pr_repo, tmp_path, capsys):
    _, _, annotations, _ = run_pr(tmp_path, capsys, root="data")
    assert [a.split(",")[0] for a in annotations] == ["::warning file=data/Patient-changed.json"]


def test_errors_in_unchanged_files_are_annotated_and_fail(pr_repo, tmp_path, capsys):
    pr_repo("data/Patient-noid.json", {"resourceType": "Patient"})
    status, _, annotations, _ = run_pr(tmp_path, capsys)
    assert status == 1
    assert [a.split(",")[0] for a in annotations] == [
        "::warning file=data/Patient-changed.json",
        "::error file=data/Patient-noid.json",
    ]


def test_changed_files_summary_sections(pr_repo, tmp_path, capsys):
    *_, summary = run_pr(tmp_path, capsys)
    counts = summary.index("| warning | file-name | 2 |")
    changed = summary.index("### Problems in the files changed by this pull request")
    details = summary.index("<details><summary>All 2 problems in the repository</summary>")
    assert counts < changed < details
    changed_section = summary[changed:details]
    assert "| data/Patient-changed.json |" in changed_section
    assert "Patient-unchanged.json" not in changed_section
    assert "| data/Patient-unchanged.json |" in summary[details:]
    assert summary.rstrip().endswith("</details>")


def test_changed_files_summary_when_changed_files_are_clean(pr_repo, tmp_path, capsys):
    (tmp_path / "changed.txt").write_text("README.md\n")
    _, _, annotations, summary = run_pr(tmp_path, capsys)
    assert annotations == []
    assert "No problems in the files changed by this pull request." in summary
    assert "<details><summary>All 2 problems in the repository</summary>" in summary


def test_without_changed_files_everything_is_annotated(pr_repo, tmp_path, capsys):
    assert main([".", "--exceptions", str(tmp_path / "none")]) == 0
    out = capsys.readouterr().out
    assert len([line for line in out.splitlines() if line.startswith("::")]) == 2
    summary = (tmp_path / "summary.md").read_text()
    assert "<details>" not in summary and "###" not in summary
