# **HL7 AU FHIR Test Data Release Strategy**

## **1. Overview**
This release strategy establishes a framework for versioning, release management, and iterative development for HL7 AU FHIR Test Data.

## **2. Versioning Strategy**
The versioning approach follows **a modified Semantic Versioning (semver) strategy** aligned with HL7 AU conventions:

### **Version Format: `MAJOR.MINOR.PATCH`**
- **MAJOR** (`X.0.0`) – Indicates a major milestone or significant changes, often aligning with a HL7 AU FHIR Test Data Project Release.
- **MINOR** (`X.Y.0`) – Used for incremental releases within a major version.
- **PATCH** (`X.Y.Z`) – Represents small fixes, technical corrections, and refinements to existing test data without introducing breaking changes.
- **Pre-release** (`X.Y.0-beta`) may be used for testing purposes before an official release.

Each release is tagged in the repository using the format:
> `v<MAJOR>.<MINOR>.<PATCH>` format (e.g., `v1.0.0`).

Additionally, tags may be used to mark repository states, such as for HL7 AU Connectathons and Sparked Test Events, supporting consistency across testing environments and the reproducibility of test results.

## 3. Release Process  

### 3.1 Development & Testing  
- All changes are merged into `main` following the [project's iterative development workflow](https://confluence.hl7.org/spaces/HAFWG/pages/265093726/Process+Test+Data+-+iterative+development).  
- `main` is considered the stable branch.  

### 3.2 Release Triggers
- A release may be initiated once `main` reaches a milestone, such as:
  - Meeting the HL7 AU FHIR Test Data Project mission and scope.
  - Achieving sufficient test data coverage for a formally balloted and published HL7 AU IG.
  - Implementing significant feature enhancements or fixes to test data sets or supporting tooling.

### 3.4 Preparing the Release 
- Perform final testing and apply necessary fixes before proceeding with the release.
- Create a **Git tag** (e.g., `v1.0.0`) from `main` to mark the release.
- Assign a release version based on the **versioning strategy** outlined above.  
- Generate **release artifacts** (e.g., FHIR test data sets, QA reports, and documentation) from `main`.
- Attach generated artifacts to the release in GitHub.
- NPM Package Consideration: No NPM package is published at this stage, but releases are tagged, and artifacts are stored in GitHub. This approach may be revised as the project evolves.
- Release Branching: A dedicated release branch is not required at this stage. However, release branches may be introduced in the future if needed.  
- Finalise **release notes** which may include:
  - A summary of features, updates, and fixes.
  - A QA/validation report summarizing test data conformance status.
  - A test data coverage report evaluating coverage against relevant IG(s).
- **QA process**
  - To maintain data quality and conformance, the following QA steps are embedded in the development workflow. This workflow includes a CI pipeline that integrates FHIR tooling for validation and automates uploads to a target reference implementation, helping to identify issues early before release.
    - **Validation against HL7 AU IGs** (e.g., AU Core, AU Base, AU eRequesting).
      - Automated GitHub validation workflow flags validation errors before merging updates.
      - Contributors and reviewers verify that validation parameters are appropriate and up to date.
    - Comparison with previous validation workflow runs helps detect regressions and new issues and may assist in identifying the cause of errors.
    - **Quarantine process** for test data instances that are assessed as valid but report errors that can be justified (e.g., tooling-related errors, terminology service errors). These instances are quarantined to avoid confounding future QA/validation report reviews. These justifications are documented via inline comments to clarify the reasoning.
  - The HL7 AU FHIR Test Data Project Lead should review the QA report and verify the reasoning behind quarantined instances prior to release.

### 3.5 Post-Release Development and Community Involvement 
- Announce the release e.g., via HL7 AU Infrastructure and Tooling calls and chat.fhir.org.
- Further development continues on `main`, preparing for the next release cycle.  
- Community contributions via GitHub issues.
- Updates based on user feedback, testing event outcomes, and IG changes.
- Continuous improvement to tooling for synthetic test data generation, supporting tooling including CI pipelines.



















