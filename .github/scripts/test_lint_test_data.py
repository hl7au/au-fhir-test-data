import json
import os
import subprocess
from pathlib import Path

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


@pytest.mark.parametrize("bundle_type", ["transaction", "batch"])
def test_transaction_and_batch_bundles_need_no_id(repo, bundle_type):
    repo("Bundle-upload.json", {"resourceType": "Bundle", "type": bundle_type, "entry": []})
    assert problems(repo.root) == []


def test_other_bundles_need_an_id(repo):
    repo("Bundle-b1.json", {"resourceType": "Bundle", "type": "collection"})
    assert problems(repo.root) == [("Bundle-b1.json", "resource-id", "error")]


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
    ("tel:+61-2-5550-1234", "0255501234"),
    ("TEL:0255501234", "0255501234"),
    ("0061 2 5550 1234", "0255501234"),
    ("(02) 5550 1234 ext 12", "0255501234"),
    ("(02) 5550 1234 x12", "0255501234"),
    ("(02) 5550 1234 extn. 12", "0255501234"),
    ("02 5550 1234, Ext: 12", "0255501234"),
    ("tel:+61-2-5550-1234;ext=12", "0255501234"),
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
    ("localhost", True),
    ("mail.localhost", True),
    ("example.com.au", False),
    ("myownpersonaldomain.com", False),
    ("notexample.com", False),
    ("email.com", False),
])
def test_reserved_domain(domain, reserved):
    assert is_reserved_domain(domain) is reserved


@pytest.mark.parametrize("value, domain", [
    ("mailto:Jo@Clinic.Example.ORG", "clinic.example.org"),
    ("Jane Doe <jane@example.com>", "example.com"),
    ("\"Doe, Jane\" <jane@example.com>", "example.com"),
    ("mailto:jane@example.com?subject=Referral", "example.com"),
    ("jane@clinic.example.com.", "clinic.example.com"),
])
def test_email_domain(value, domain):
    assert email_domain(value) == domain


def test_named_email_with_reserved_domain_passes(repo):
    repo("Patient-p1.json", patient(telecom=[phone("Jane Doe <jane@example.com>", "email")]))
    assert problems(repo.root) == []


def test_contact_point_systems_match_case_insensitively_and_include_pager(repo):
    repo("Patient-p1.json", patient(telecom=[
        phone("0412 345 678", "Phone"), phone("0412 345 679", "pager"), phone("jo@email.com", "EMAIL"),
        phone("0491 570 006", "pager"),
    ]))
    assert [(p.rule, p.subject) for p in lint(repo.root)] == [
        ("contact-email", "email.com"), ("contact-phone", "0412345679"), ("contact-phone", "0412345678"),
    ]
    assert "Pager number '0412 345 679'" in lint(repo.root)[1].message


def test_contact_point_without_system_is_checked_as_email_only_with_at(repo):
    repo("Patient-p1.json", patient(telecom=[{"value": "jo@email.com"}, {"value": "0412 345 678"}]))
    [problem] = lint(repo.root)
    assert (problem.rule, problem.subject) == ("contact-email", "email.com")
    assert " in " not in problem.message  # Reported once, as a ContactPoint.


def test_emails_in_other_strings(repo):
    organization = {
        "resourceType": "Organization", "id": "o1",
        "text": {"status": "generated", "div": '<div xmlns="http://www.w3.org/1999/xhtml">'
                 '<a href="mailto:a@clinic.com.au">a@clinic.com.au</a>, b@clinic.example.org</div>'},
    }
    endpoint = {"resourceType": "Endpoint", "id": "e1", "address": "mailto:c@realmail.com"}
    repo("Bundle-b1.json", {
        "resourceType": "Bundle", "id": "b1", "type": "collection",
        "entry": [{"resource": organization}, {"resource": endpoint}],
    })
    repo("Patient-p1.json", patient(
        extension=[{"url": "http://example.org/ext", "valueString": "Contact d@gmail.com."}],
        contained=[{"resourceType": "Practitioner", "id": "pr1", "text": {"div": "e@hospital.org.au"}}],
    ))
    assert [p.message.split(" does not")[0] for p in lint(repo.root)] == [
        "Email 'a@clinic.com.au' in entry[0].resource.text.div",
        "Email 'c@realmail.com' in entry[1].resource.address",
        "Email 'd@gmail.com' in extension[0].valueString",
        "Email 'e@hospital.org.au' in contained[0].text.div",
    ]


def test_free_text_scan_ignores_urls_identifiers_and_attachment_data(repo):
    repo("Patient-p1.json", patient(
        identifier=[{"system": "http://www.abs.gov.au/ausstats/abs@.nsf/mf/1220.0", "value": "1"}],
        extension=[
            {"url": "http://example.org/ext", "valueUri": "https://user@real.com.au/fhir"},
            {"url": "http://example.org/ext", "valueString": "Medicare 2123 4567 8 1, phone 0412 345 678"},
        ],
        photo=[{"contentType": "text/plain", "data": "am9AZW1haWwuY29t"}],  # base64 of jo@email.com
    ))
    assert problems(repo.root) == []


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


def git(cwd, *args):
    subprocess.run(["git", "-C", str(cwd), *args], check=True, capture_output=True)


@pytest.fixture
def pr_repo(repo, tmp_path, monkeypatch):
    """A git repo whose base commit has a warning in two files, run from its root as in Actions.

    The test adds a second commit, then runs with --base-ref HEAD^1.
    """
    git(repo.root, "init", "-q")
    git(repo.root, "config", "user.email", "lint@example.com")
    git(repo.root, "config", "user.name", "Lint Test")
    git(repo.root, "config", "commit.gpgsign", "false")
    repo("data/Patient-changed.json", patient(telecom=[phone("0412 345 678")]))
    repo("data/Patient-unchanged.json", patient())
    git(repo.root, "add", "-A")
    git(repo.root, "commit", "-q", "-m", "base")
    monkeypatch.chdir(repo.root)
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(tmp_path / "summary.md"))

    def commit(*changes):
        for name, resource in changes:
            repo(name, resource)
        git(repo.root, "add", "-A")
        git(repo.root, "commit", "-q", "--allow-empty", "-m", "change")

    repo.commit = commit
    return repo


def run_pr(capsys, root="."):
    status = main([root, "--exceptions", "none", "--base-ref", "HEAD^1"])
    out = capsys.readouterr().out
    annotations = [line for line in out.splitlines() if line.startswith("::")]
    summary_path = Path(os.environ["GITHUB_STEP_SUMMARY"])
    return status, out, annotations, summary_path.read_text() if summary_path.exists() else ""


def test_unrelated_change_does_not_annotate_existing_problems(pr_repo, capsys):
    pr_repo.commit(("data/Patient-changed.json", patient(gender="female", telecom=[phone("0412 345 678")])))
    status, out, annotations, summary = run_pr(capsys)
    assert status == 0
    assert annotations == []
    # Every problem is still printed and counted.
    assert "data/Patient-changed.json: warning: [contact-phone]" in out
    assert "data/Patient-unchanged.json: warning: [file-name]" in out
    assert "| warning | file-name | 2 |" in summary
    assert "This pull request introduces no problems." in summary


def test_new_problem_in_a_changed_file_is_annotated(pr_repo, capsys):
    pr_repo.commit(("data/Patient-changed.json", patient(telecom=[phone("0412 345 678"), phone("jo@email.com", "email")])))
    _, _, annotations, _ = run_pr(capsys)
    assert annotations == [
        "::warning file=data/Patient-changed.json,title=contact-email::"
        "Email 'jo@email.com' does not use a reserved domain "
        "(example.com, example.net, example.org, .example, .test, .invalid, .localhost).",
    ]


def test_a_second_copy_of_an_existing_problem_is_introduced(pr_repo, capsys):
    pr_repo.commit(("data/Patient-changed.json", patient(telecom=[phone("0412 345 678")] * 2)))
    _, _, annotations, _ = run_pr(capsys)
    assert [a.split("::")[1] for a in annotations] == ["warning file=data/Patient-changed.json,title=contact-phone"]


def test_added_file_problems_are_annotated(pr_repo, capsys):
    pr_repo.commit(("data/Patient-added.json", patient()))
    _, _, annotations, _ = run_pr(capsys)
    assert [a.split(",")[0] for a in annotations] == ["::warning file=data/Patient-added.json"]


def test_rename_that_keeps_a_wrong_name_is_not_annotated(pr_repo, capsys):
    git(pr_repo.root, "mv", "data/Patient-unchanged.json", "data/Patient-still-wrong.json")
    pr_repo.commit()
    _, _, annotations, _ = run_pr(capsys)
    assert annotations == []


def test_rename_to_a_wrong_name_is_annotated(pr_repo, capsys):
    pr_repo.commit(("data/Patient-p9.json", patient("p9")))
    git(pr_repo.root, "mv", "data/Patient-p9.json", "data/Patient-wrong.json")
    pr_repo.commit()
    _, _, annotations, _ = run_pr(capsys)
    assert [a.split(",")[0] for a in annotations] == ["::warning file=data/Patient-wrong.json"]


def test_base_ref_matches_when_scanning_a_subdirectory(pr_repo, capsys):
    pr_repo.commit(("data/Patient-added.json", patient()))
    _, out, annotations, _ = run_pr(capsys, root="data")
    assert [a.split(",")[0] for a in annotations] == ["::warning file=data/Patient-added.json"]
    assert "Patient-added.json: warning: [file-name]" in out


def test_errors_are_annotated_and_fail(pr_repo, capsys):
    pr_repo.commit(("data/Patient-noid.json", {"resourceType": "Patient"}))
    status, _, annotations, _ = run_pr(capsys)
    assert status == 1
    assert [a.split(",")[0] for a in annotations] == ["::error file=data/Patient-noid.json"]


def test_base_ref_summary_sections(pr_repo, capsys):
    pr_repo.commit(("data/Patient-added.json", patient()))
    *_, summary = run_pr(capsys)
    counts = summary.index("| warning | file-name | 3 |")
    introduced = summary.index("### Problems introduced by this pull request")
    details = summary.index("<details><summary>All 4 problems in the repository</summary>")
    assert counts < introduced < details
    introduced_section = summary[introduced:details]
    assert "| data/Patient-added.json |" in introduced_section
    assert "Patient-unchanged.json" not in introduced_section
    assert "| data/Patient-unchanged.json |" in summary[details:]
    assert summary.rstrip().endswith("</details>")


def test_bad_base_ref_exits_with_git_message(pr_repo, capsys):
    with pytest.raises(SystemExit, match="git .* failed"):
        main([".", "--exceptions", "none", "--base-ref", "no-such-ref"])


def test_without_base_ref_everything_is_annotated(pr_repo, tmp_path, capsys):
    assert main([".", "--exceptions", "none"]) == 0
    out = capsys.readouterr().out
    assert len([line for line in out.splitlines() if line.startswith("::")]) == 3
    summary = (tmp_path / "summary.md").read_text()
    assert "<details>" not in summary and "###" not in summary
