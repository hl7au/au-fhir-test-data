# Contributing to HL7 AU FHIR Test Data

Thanks for helping improve the test data. This page describes how a change gets from an idea to `master`: issue, triage, branch, pull request (PR), checks, review and merge. Test data belongs to the IG projects that use it, so every change is reviewed and approved by the owner of the folder it touches.

## Ownership and approval

| Area | Folder | Owner (GitHub login) | Approval needed before merge |
| --- | --- | --- | --- |
| AU Core | `au-fhir-test-data-set/au-core` | Sparked: Danielle Tavares-Rixon (`dt-r`), Dusica Bojicic (`dbojicic`) | Danielle Tavares-Rixon or Dusica Bojicic |
| AU Patient Summary | `au-fhir-test-data-set/au-patient-summary` | Sparked: Danielle Tavares-Rixon (`dt-r`), Dusica Bojicic (`dbojicic`) | Danielle Tavares-Rixon or Dusica Bojicic |
| AU Encounter Record (future) | `au-fhir-test-data-set/au-encounter-record` | Sparked: Danielle Tavares-Rixon (`dt-r`), Dusica Bojicic (`dbojicic`) | Danielle Tavares-Rixon or Dusica Bojicic |
| AU eRequesting | `au-fhir-test-data-set/au-erequesting` | Michael Osborne (`mjosborne1`); second reviewer to be confirmed | Michael Osborne, or the second reviewer (to be confirmed) when Michael is the author |
| Connected care | `au-fhir-test-data-set/connected-care` | Connectathon track leads, currently Heath Frankel (`heathfrankel`) and Brett Esler (`brettesler-ext`, HL7 AU) | A track lead |
| Services Australia data | Services Australia derived data and its CSV exports in `testdata-csv/` | Heath Frankel (`heathfrankel`) | Heath Frankel |
| Tooling and CI | `.github/`, docs and process | Kyle Pettigrew (`KyleOps`) | Kyle Pettigrew |

Anyone may review any PR; the table lists whose approval is required. An author cannot approve their own PR.

Other projects may add and manage their own starter test data in their own folder under `au-fhir-test-data-set/`. Open an issue first so the folder and its owner can be added to this table.

### Services Australia data

The Services Australia identifiers (IHI, HPI-I, HPI-O, Ahpra numbers, Medicare and DVA numbers, prescriber numbers) come from a formula-based source spreadsheet kept in the HL7 AU SharePoint IMT library. Exported CSVs are committed to `testdata-csv/` so that changes can be reviewed as text in a PR. The generated FHIR JSON in this repository is what consumers use.

## 1. Raise an issue

Search the [existing issues](https://github.com/hl7au/au-fhir-test-data/issues) first. If nothing matches, open a [new issue](https://github.com/hl7au/au-fhir-test-data/issues/new/choose) and pick a form:

- **Test data problem**: something in the existing data is wrong (invalid, inconsistent, wrong code, broken reference).
- **New test data request**: data you need that does not exist yet.
- **Tooling or CI**: a check, workflow or script misbehaves.

The test data forms ask for the **Area**, which labels the issue so it reaches the right owner. Please raise an issue before starting non-trivial work, so effort is not duplicated and the approach fits the IG.

## 2. Triage

New issues are labelled `needs-triage`. The tooling owner triages them and routes each by area to the owner in the table above. The owner agrees the approach with the reporter before work starts.

## 3. Branch

Work on a branch, either in this repository (if you have write access) or in a fork. Name it after the issue, in lowercase with hyphens, for example `123-fix-condition-display`.

## 4. Open a pull request

Open the PR against `master`, fill in the PR template, link the issue (`Fixes #123`), and request review from the owner of each folder you touched. Keep a PR to one area where you can; a PR that touches several folders needs approval from each folder's owner.

## 5. Checks

These checks run on every PR:

- **`Reference integrity`** (blocking): every literal reference must resolve to a resource in the repository. A `resourceType/id` defined in more than one file fails, unless it is listed in `.github/scripts/reference_integrity_allowed_duplicates` with a comment giving the reason. A document Bundle must contain every resource its Composition references; other references that leave a document Bundle are reported as warnings.
- **`Lint`** (some rules blocking, some warnings): each file name must match `<resourceType>-<id>.json`, and contact details (phone numbers, email addresses) must be obviously synthetic, using the reserved fictional phone ranges and example domains described in [Synthetic Data Properties](docs/README.md#synthetic-data-properties).
- **`FHIR validation`** (advisory for now, does not block): the changed files are validated with the HL7 FHIR Validator against the IG for their folder. Results are in the job summary and as annotations on the changed files. Please fix what it reports where you can, or say in the PR why a finding is expected.

If a check fails and you cannot see why, comment on the PR and mention the tooling owner (Kyle Pettigrew, `KyleOps`). The failure may be a limitation of the tooling, for example a resource shape the check has not seen before, rather than a problem with your data.

### Quarantine lists

Two lists let known problems through the checks:

- `.github/scripts/reference_integrity_quarantine`: files skipped by the reference integrity check.
- `.github/validate/validator_quarantine`: files skipped by FHIR validation.

Fixing the data is always preferred. Each new entry needs a comment above it that justifies it (what is wrong, why it cannot be fixed now, and the issue that tracks the fix), and the tooling owner must approve the PR that adds it. Remove the entry in the PR that fixes the data.

## 6. Review and merge

The folder owner reviews the change; others may review too. Address the feedback by pushing more commits to the branch.

Once the required owner has approved and the checks pass (or an advisory finding is explained), the tooling owner merges the PR. The process is expected to move to automatic merge after owner approval once that is configured.

## Data conventions

- **Synthetic only**: never add real personal or health information. Names, addresses, contact details and identifiers follow [Synthetic Data Properties](docs/README.md#synthetic-data-properties).
- **File names**: one resource per file, named `<resourceType>-<id>.json`, with `id` matching the file name.
- **Administrative resources** (Patient, Practitioner, PractitionerRole, Organization, Location, HealthcareService, RelatedPerson) are managed centrally. Reuse an existing one where you can, and ask in your issue before adding a new one.
- **SNOMED CT**: concepts must be active, and `display` should be the preferred term, not the fully specified name (FSN). For example, `195967001` has the display `Asthma`, not `Asthma (disorder)`. Check codes against a terminology server such as the [NCTS](https://www.healthterminologies.gov.au/) before committing.

## PR author checklist

- [ ] The PR links an issue, or explains why none is needed.
- [ ] Review is requested from the owner of every folder touched.
- [ ] Each file is named `<resourceType>-<id>.json` and its `id` matches.
- [ ] Contact details and identifiers are synthetic.
- [ ] SNOMED CT concepts are active and use the preferred term as the display.
- [ ] Checks are green, or each failure or advisory finding is explained in the PR.
- [ ] Any new quarantine or allowed-duplicate entry has a justification comment.

## Releases

Releases are tagged from `master`; see the [release strategy](docs/HL7AUFHIRTestDataReleaseStrategy.md).

## Escalation and help

- A check fails and you cannot see why: comment on the PR and mention the tooling owner (see [Checks](#5-checks)).
- An issue or PR is waiting on a review: mention the folder owner on it; if it is still stuck, mention the tooling owner, who triages and merges.
- Anything still stuck, or a disagreement about the approach: add it to the agenda of the monthly HL7 AU Infrastructure and Tooling community meeting, where issues are discussed and triaged.
- General questions: the [AU FHIR Test Data topic](https://chat.fhir.org/#narrow/stream/179173-australia/topic/AU.20FHIR.20Test.20Data) on chat.fhir.org, or the [project page](https://confluence.hl7.org/spaces/HAFWG/pages/273942754) on HL7 Confluence.
