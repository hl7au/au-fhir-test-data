# HL7 AU FHIR Test Data Project Release Strategy (WIP)

Release 1.0.0 contains resources from the following directories:
* [au-fhir-test-data/generated](https://github.com/hl7au/au-fhir-test-data/tree/master/generated),
* [au-fhir-test-data/direct-fhir-test-resources](https://github.com/hl7au/au-fhir-test-data/tree/master/direct-fhir-test-resources) which include resource instances with missing data and suppressed data,
* [au-fhir-test-data/erequesting](https://github.com/hl7au/au-fhir-test-data/tree/master/erequesting).


QA 
> QA throughout development process - refer to Confluence page
> Validation report - maybe include in the release package
>>Explain the quarantine file - inline comments
> upload to HL7 AU Sparked reference implementation (SMILE CDR) also used to verify test data 
> running test data against Inferno test suite and comparing to a known previous report can help identify new issues with test data changes, and changes to the IG which impact the conformance of existing test data. 
Mention of release being a snapshot is ok.
Explain when we release - e.g. based on status of test data coverage of a published IG?
No NPM package

---

This document establishes the release management strategy for Test Data Repository software releases, ensuring consistent deployments through version control, release management, and automation within GitHub repositories.

## Repository Structure

The repository maintains several distinct branches, each serving a specific purpose in the release workflow:

- **Main (master) branch**: Contains the current stable version of the codebase.
- **Development branch**: Serves as the primary integration point for ongoing development.
- **Feature branches**: Created from the development branch to facilitate work on specific features or fixes.
- **Release branches**: Used for preparation and refinement of new releases.
- **Hotfix branches**: Created for urgent production fixes and merged into both main and development branches.
- **Git tags**: Mark significant points in the repository history, particularly version releases.

## Version Control Implementation

The project implements **Semantic Versioning (SemVer)** to maintain clear version progression:

- **Major version updates (X.0.0)**: Indicate breaking changes or significant functional modifications.
- **Minor version updates (X.Y.0)**: Signify the addition of backwards-compatible features.
- **Patch version updates (X.Y.Z)**: Encompass bug fixes and minor improvements.

## Release Workflow Process

The branching strategy follows **GitHub Flow** with the following structure:

- **Main Branch**: Houses production-ready code for deployment.
- **Development Branch**: Serves as the integration point for feature testing.
- **Feature Branches**: Temporary branches for specific development tasks.
- **Release Branches**: Preparation branches for release refinement.
- **Hotfix Branches**: Urgent production fix branches, merged to main and development.

## Pull Request Requirements

All code modifications require pull request submission to maintain code quality and consistency. Requirements include:

- Minimum **one reviewer** from the development team.
  - It is the responsibility of the reviewer to consult/coordinate review with members of the Clinical Design Group, Clinical Terminologist, or other appropriate SME as required. 
- Adherence to established **coding standards and best practices**.
- Refer to the HL7 AU FHIR Test Data development process documented in Confluence https\://confluence.hl7.org/spaces/HAFWG/pages/265093726/Process+Test+Data+-+iterative+development 

## Release Candidate Process

Release candidate creation involves:

1. Branch creation from development (`release/vX.Y.Z`).
2. Final testing and necessary fixes.
3. Merger into **main** and **development** branches upon completion.

## Release Tagging Protocol

Release tagging follows Semantic Versioning format:

- **Format**: `vX.Y.Z`
- **Implementation**: `git tag -a v1.2.0 -m "Release version 1.2.0"`
- **Distribution**: `git push origin v1.2.0`

## Release Documentation Requirements

Each release must include documentation covering:

- **Feature additions**
- **Bug resolution details**
- **Enhancement implementations**
- **Known issues and limitations**
- **Breaking changes**

## Implementation Best Practices

Development teams must adhere to the following best practices:

- Maintain **focused, discrete commits**.
- Provide **detailed commit documentation**.
- Implement **comprehensive testing protocols**.
- Maximize automation through **CI/CD implementation**.
- Apply **consistent version control practices**.
- Maintain thorough **release documentation**.

## Process Implementation

This release strategy provides a structured framework for release management within GitHub repositories. Consistent application of these protocols ensures:

- **Reliable versioning**
- **Deployment efficiency**
- **Effective stakeholder communication**

Integration with **GitHub Actions** automation enables development teams to focus on code development while maintaining high release quality.




