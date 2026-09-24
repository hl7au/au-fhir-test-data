import json

import pytest

from reference_integrity import Checker, main


@pytest.fixture
def repo(tmp_path):
    def write(name, resource):
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(resource), encoding="utf-8")

    write.root = tmp_path
    return write


def problems(root, quarantine=()):
    return [(p.path, p.message) for p in Checker(root, quarantine).run()]


def patient(id="p1", **fields):
    return {"resourceType": "Patient", "id": id, **fields}


def test_resolves_relative_reference(repo):
    repo("Patient-p1.json", patient())
    repo("Condition-c1.json", {"resourceType": "Condition", "id": "c1", "subject": {"reference": "Patient/p1"}})
    assert problems(repo.root) == []


def test_reports_every_missing_reference_in_a_file(repo):
    repo("Condition-c1.json", {
        "resourceType": "Condition", "id": "c1",
        "subject": {"reference": "Patient/missing"},
        "recorder": {"reference": "Practitioner/missing"},
    })
    assert problems(repo.root) == [
        ("Condition-c1.json", "Reference 'Patient/missing': not found in any resource."),
        ("Condition-c1.json", "Reference 'Practitioner/missing': not found in any resource."),
    ]


def test_ignores_history_suffix(repo):
    repo("Patient-p1.json", patient())
    repo("Condition-c1.json", {"resourceType": "Condition", "id": "c1", "subject": {"reference": "Patient/p1/_history/2"}})
    assert problems(repo.root) == []


def test_checks_attachment_url_to_binary(repo):
    report = {
        "resourceType": "DiagnosticReport", "id": "r1",
        "presentedForm": [{"contentType": "application/pdf", "url": "Binary/pdf-1"}],
    }
    repo("DiagnosticReport-r1.json", report)
    assert problems(repo.root) == [
        ("DiagnosticReport-r1.json", "Reference 'Binary/pdf-1': not found in any resource."),
    ]
    repo("Binary-pdf-1.json", {"resourceType": "Binary", "id": "pdf-1", "contentType": "application/pdf"})
    assert problems(repo.root) == []


def test_ignores_extension_and_canonical_urls(repo):
    repo("Patient-p1.json", patient(
        extension=[
            {"url": "http://hl7.org.au/fhir/StructureDefinition/indigenous-status", "valueCoding": {"code": "4"}},
            {"url": "ahpraProfession", "valueString": "x"},
        ],
        photo=[{"contentType": "image/png", "url": "https://example.org/photo.png"}],
    ))
    assert problems(repo.root) == []


def test_contained_references(repo):
    repo("MedicationRequest-m1.json", {
        "resourceType": "MedicationRequest", "id": "m1",
        "contained": [{"resourceType": "Medication", "id": "med", "ingredient": [{"itemReference": {"reference": "#"}}]}],
        "medicationReference": {"reference": "#med"},
        "reasonReference": [{"reference": "#nope"}],
    })
    assert problems(repo.root) == [
        ("MedicationRequest-m1.json", "Reference '#nope': no contained resource has that id."),
    ]


def test_references_inside_contained_resources_are_checked(repo):
    repo("MedicationRequest-m1.json", {
        "resourceType": "MedicationRequest", "id": "m1",
        "contained": [{"resourceType": "Medication", "id": "med", "manufacturer": {"reference": "Organization/missing"}}],
    })
    assert problems(repo.root) == [
        ("MedicationRequest-m1.json",
         "Reference 'Organization/missing' (in contained '#med'): not found in any resource."),
    ]


def document_bundle(entries, **fields):
    return {"resourceType": "Bundle", "id": "b1", "type": "document", "entry": entries, **fields}


def test_bundle_resolves_urn_uuid_against_entries(repo):
    repo("Bundle-b1.json", document_bundle(
        [
            {"fullUrl": "urn:uuid:aaaa", "resource": {"resourceType": "Composition", "id": "c", "subject": {"reference": "urn:uuid:bbbb"}}},
            {"fullUrl": "urn:uuid:bbbb", "resource": patient()},
        ],
        signature={"who": {"reference": "urn:uuid:bbbb"}},
    ))
    assert problems(repo.root) == []


def test_bundle_reports_unknown_urn_uuid(repo):
    repo("Bundle-b1.json", document_bundle([
        {"fullUrl": "urn:uuid:aaaa", "resource": {"resourceType": "Composition", "id": "c", "subject": {"reference": "urn:uuid:zzzz"}}},
    ]))
    assert problems(repo.root) == [
        ("Bundle-b1.json", "Reference 'urn:uuid:zzzz': no Bundle entry has this fullUrl."),
    ]


def test_bundle_attachment_urn_uuid(repo):
    repo("Bundle-b1.json", document_bundle([
        {"fullUrl": "urn:uuid:aaaa", "resource": {
            "resourceType": "DiagnosticReport", "id": "r",
            "presentedForm": [{"contentType": "application/pdf", "url": "urn:uuid:missing"}],
        }},
    ]))
    assert problems(repo.root) == [
        ("Bundle-b1.json", "Reference 'urn:uuid:missing': no Bundle entry has this fullUrl."),
    ]


def test_bundle_relative_reference_falls_back_to_repository(repo):
    repo("Patient-p1.json", patient())
    repo("Bundle-b1.json", document_bundle([
        {"fullUrl": "urn:uuid:aaaa", "resource": {"resourceType": "Composition", "id": "c", "subject": {"reference": "Patient/p1"}}},
    ]))
    assert problems(repo.root) == []


def test_bundle_entries_are_not_visible_outside_the_bundle(repo):
    repo("Bundle-b1.json", document_bundle([{"fullUrl": "urn:uuid:aaaa", "resource": patient("inner")}]))
    repo("Condition-c1.json", {"resourceType": "Condition", "id": "c1", "subject": {"reference": "Patient/inner"}})
    assert problems(repo.root) == [
        ("Condition-c1.json", "Reference 'Patient/inner': not found in any resource."),
    ]


def test_urn_uuid_outside_bundle(repo):
    repo("Condition-c1.json", {"resourceType": "Condition", "id": "c1", "subject": {"reference": "urn:uuid:aaaa"}})
    assert problems(repo.root) == [
        ("Condition-c1.json", "Reference 'urn:uuid:aaaa': only resolvable inside a Bundle."),
    ]


@pytest.mark.parametrize("reference, message", [
    ("https://example.org/fhir/Patient/p1", "not a relative Type/id reference, so it cannot be resolved against the test data."),
    ("Patient?identifier=123", "conditional references cannot be resolved against the test data."),
])
def test_unresolvable_reference_shapes(repo, reference, message):
    repo("Condition-c1.json", {"resourceType": "Condition", "id": "c1", "subject": {"reference": reference}})
    assert problems(repo.root) == [("Condition-c1.json", f"Reference '{reference}': {message}")]


def test_duplicate_resource_ids_across_folders(repo):
    repo("au-core/Patient-p1.json", patient())
    repo("au-erequesting/Patient-p1.json", patient())
    assert problems(repo.root) == [
        ("au-core/Patient-p1.json", "Duplicate resource 'Patient/p1', also defined in au-erequesting/Patient-p1.json."),
        ("au-erequesting/Patient-p1.json", "Duplicate resource 'Patient/p1', also defined in au-core/Patient-p1.json."),
    ]


def test_invalid_json_and_non_fhir_files(repo):
    (repo.root / "broken.json").write_text("{", encoding="utf-8")
    repo("package.json", {"name": "not-fhir"})
    assert [path for path, _ in problems(repo.root)] == ["broken.json"]


def test_quarantine_matches_repo_relative_paths_and_globs(repo):
    repo("au-core/Condition-c1.json", {"resourceType": "Condition", "id": "c1", "subject": {"reference": "Patient/missing"}})
    repo("au-ps/Condition-c1.json", {"resourceType": "Condition", "id": "c2", "subject": {"reference": "Patient/missing"}})
    assert [p for p, _ in problems(repo.root, ["au-core/Condition-c1.json"])] == ["au-ps/Condition-c1.json"]
    assert problems(repo.root, ["au-*/Condition-*.json"]) == []
    assert [p for p, _ in problems(repo.root, ["Condition-c1.json"])] == [
        "au-core/Condition-c1.json", "au-ps/Condition-c1.json",
    ]


def test_main_exit_code_and_step_summary(repo, tmp_path_factory, monkeypatch, capsys):
    summary = tmp_path_factory.mktemp("gh") / "summary.md"
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(summary))
    quarantine = tmp_path_factory.mktemp("q") / "quarantine"
    quarantine.write_text("# comment\n", encoding="utf-8")

    repo("Patient-p1.json", patient())
    assert main([str(repo.root), "--quarantine", str(quarantine)]) == 0
    assert "All references resolve." in summary.read_text()

    repo("Condition-c1.json", {"resourceType": "Condition", "id": "c1", "subject": {"reference": "Patient/missing"}})
    assert main([str(repo.root), "--quarantine", str(quarantine)]) == 1
    assert "| Condition-c1.json | Reference 'Patient/missing': not found in any resource. |" in summary.read_text()
    assert "Condition-c1.json: Reference 'Patient/missing'" in capsys.readouterr().out
