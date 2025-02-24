# **HL7 AU FHIR Test Data Release Strategy**

## **1. Overview**
This release strategy establishes a framework for versioning, release management, and iterative development for HL7 AU FHIR Test Data.

## **2. Versioning Strategy**
The versioning approach follows **a modified Semantic Versioning (semver) strategy** aligned with HL7 AU conventions:

### ** Release Version Format: `MAJOR.MINOR.PATCH`**
- **MAJOR** (`X.0.0`) – Indicates a major milestone or significant changes, often aligning with a HL7 AU FHIR Test Data Project Release.
- **MINOR** (`X.Y.0`) – Used for incremental releases within a major version.
- **PATCH** (`X.Y.Z`) – Represents small fixes, technical corrections, and refinements to existing test data without introducing breaking changes.

Each release is also marked with a Git tag using the format `v<MAJOR>.<MINOR>.<PATCH>` (e.g., `v1.0.0`) to capture an immutable snapshot of the repository at a release milestone. 

## 3. Release Process  

### 3.1 Pre-requisites: Development & Testing  
- All changes are merged into `main` following the [project's iterative development process](https://confluence.hl7.org/spaces/HAFWG/pages/265093726/Process+Test+Data+-+iterative+development).  

### 3.2 Release Triggers
- A release may be initiated once `main` reaches a milestone, such as:
  - Meeting the HL7 AU FHIR Test Data Project Scope Statement. The HL7 AU FHIR Test Data Project **R1** - Project Scope Statement can be found [here](https://confluence.hl7.org/spaces/HA/pages/184927329/HL7+Australia+Project+Registry?preview=/184927329/248874957/Test%20Data%20Project%201.2.pdf).
  - Achieving sufficient test data coverage for a formally balloted and published HL7 AU IG.
  - Implementing significant feature enhancements or fixes to test data sets or supporting tooling.

### 3.3 Preparing the Release 
- Perform final testing and apply necessary fixes before proceeding with the release.
- Assign a release version based on the **versioning strategy** outlined above.  
- Create a **Git tag** (e.g., `v1.0.0`) from `main` to mark the release based on the assigned version.
- Generate and package **release artifacts** (e.g., FHIR test data sets and documentation) directly from the tagged commit.
- Attach these packaged artifacts to the corresponding GitHub release.
- Notes:
  - Release artifacts: Releases do not include tools, maps, Postman collections, or intermediary data formats that were used in the process of generating the final FHIR resources in JSON format; however, these remain in the repository to support test data generation.
  - NPM package consideration: No NPM package is published at this stage, but releases are tagged, and artifacts are stored in GitHub. This approach may be revised as the project evolves.
  - Release branching: A dedicated release branch is not required at this stage. However, release branches may be introduced in the future if needed.  
- Finalise **release notes** which includes a summary of features, updates, fixes, and a release-specific README.md.

### 3.4 Post-Release Development and Community Involvement 
- Announce the release e.g., via HL7 AU Infrastructure and Tooling calls and chat.fhir.org.
- Further development continues on `main`, preparing for the next release cycle.  
- Community contributions via GitHub issues.
- Updates based on user feedback, testing event outcomes, and IG changes.
- Continuous improvement to tooling for synthetic test data generation, supporting tooling including CI pipelines.



















