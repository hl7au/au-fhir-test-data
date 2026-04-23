# HL7 AU FHIR Test Data
HL7 AU FHIR Test Data contains sample FHIR instances for testing purposes, and to support developers. This repository includes synthetic (realistic but not real) data that conforms to HL7 AU FHIR Implementation Guides (IGs). The synthetic data covers a broader and expanded content scope over that in the FHIR instance examples included in published HL7 AU FHIR IGs.

>[!WARNING]
>The sample FHIR resources in this repository are intended for testing and demonstration purposes only. Users are advised to not input any personal or sensitive information, including health data, into this repository. The repository does not comply with the requirements for handling personal or sensitive information under the Australian Privacy Act 1988.
>
>All persons and health data are fictional, any resemblance to real persons, living or dead is purely coincidental.
>
>With the exception of representation of federal agencies, all organisations, devices, and healthcare services, are fictional and any resemblance to actual organisations, devices, and healthcare services is purely coincidental.


## Synthetic Data Properties
The [administrative resources](https://hl7.org/fhir/R4/administration-module.html) (Patient, RelatedPerson, Practitioner, PractitionerRole, Organization, Location, HealthcareService) in this data set contain a mixture of synthetic data elements with differing characteristics:

- Names of individuals and organisations are synthetic and fictional. They are designed to resemble realistic naming conventions rather than generic placeholders. Any resemblance to real persons or organisations is coincidental and not intended.
- Physical addresses are constructed using real address components, but are generally not valid or do not correspond to actual locations within the stated suburb or state. **There is no guarantee that all addresses are non-existent or non-attributable to real locations.**
- Australian phone numbers are from [the reserved set](https://www.acma.gov.au/phone-numbers-use-tv-shows-films-and-creative-works) provided by the Australian Communications and Media Authority for use in creative works. 
- Email addresses use the following domains reserved for documentation and testing purposes: 'example', 'myownpersonaldomain domain', and 'my-own-personal-domain domain'. 
- IHI, HPI-I, or HPI-O have been provided by Services Australia. They are valid identifiers reserved for testing purposes in the HI Vendor Test Environment. 
- Australian Health Practitioner Regulation Agency (Ahpra) Registration Numbers are provided by Services Australia. They have a practitioner professions prefix (`HAC`) that is not linked to a real-world profession.
- Medicare Card Numbers, Medicare Provider numbers, PBS provider numbers, and DVA numbers are provided by Services Australia. They are valid identifiers **NOT** reserved for testing purposes. **As a result, there is a possibility that some identifiers may coincide with those assigned to real persons.**
- Australian Business Numbers (ABNs) are intentionally invalid and do not conform to real-world formats.

Users of this dataset are responsible for ensuring that appropriate safeguards are in place to prevent unintended association with real individuals, including (but not limited to) avoiding use in production systems, external integrations, or any other processes involving real-world entities.

## How to navigate this repository
Synthetic FHIR test data (JSON) files are available in the following directories: 
- [au-fhir-test-data-set](https://github.com/hl7au/au-fhir-test-data/tree/master/au-fhir-test-data-set)
  - [/au-base](https://github.com/hl7au/au-fhir-test-data/tree/master/au-fhir-test-data-set/au-base)
    - AU Base examples
  - [/au-core](https://github.com/hl7au/au-fhir-test-data/tree/master/au-fhir-test-data-set/au-core)
    - AU Core examples, some shared with eRequesting, identifiable by additional meta.profile
    - Includes test data for verifying missing data and suppressed data test cases (for details see [MissingAndSuppressedData_TestData.md](https://github.com/hl7au/au-fhir-test-data/blob/master/docs/MissingAndSuppressedData_TestData.md)).
  - [/au-erequesting](https://github.com/hl7au/au-fhir-test-data/tree/master/au-fhir-test-data-set/au-erequesting)
    - AU eRequesting specific examples
  - [/au-patient-summary](https://github.com/hl7au/au-fhir-test-data/tree/master/au-fhir-test-data-set/au-patient-summary)
    - AU Patient Summary document Bundle examples

## Versioning
The versioning approach follows **a modified Semantic Versioning (semver) strategy** aligned with HL7 AU conventions:

### **Version Format: `MAJOR.MINOR.PATCH`**
- **MAJOR** (`X.0.0`) – Indicates a major milestone or significant changes, often aligning with a HL7 AU FHIR Test Data Project Release.
- **MINOR** (`X.Y.0`) – Used for incremental releases within a major version.
- **PATCH** (`X.Y.Z`) – Represents small fixes, technical corrections, and refinements to existing test data without introducing breaking changes.
- **Pre-release** (`X.Y.0-beta`) may be used for testing purposes before an official release.

Tags are used to mark releases, and repository states such as for HL7 AU Connectathons and Sparked Test Events, supporting consistency across testing environments and the reproducibility of test results.

## Did you find an error?
We appreciate your contributions to improving au-fhir-test-data. **If you encounter any bugs or defects, please follow the steps below to report them**:

### 1. Search for Existing Issues
Before submitting a new issue, please search the GitHub [Issues list](https://github.com/hl7au/au-fhir-test-data/issues) to check if your issue has already been reported. If you find an existing issue, you can add your comments or additional information to it.

### 2. Open a New Issue
If you do not find a similar issue, you can open a [new one](https://github.com/hl7au/au-fhir-test-data/issues). Click on the New Issue button and provide the following details:

```
Title: A brief and descriptive title for the issue.
Description: A detailed description of the issue, including:
1. Steps to reproduce the issue.
2. Expected and actual behaviour.
3. Screenshots or another related information (if applicable).
```

### 3. Labelling
Help us categorise the issue by adding relevant labels (e.g., bug). This helps us prioritise and address the issues more efficiently.

### Resolving Issues
To support effective issue resolution, reporters may be engaged in the review process to help confirm that resolutions address their concerns. This can involve notifying the reporter when a fix is implemented and inviting them to validate the solution or provide feedback before the issue is formally closed.

### Questions?
If you have a question, the best place to start is Zulip e.g. the https://chat.fhir.org/#narrow/stream/179173-australia/topic/AU.20FHIR.20Test.20Data topic

## How to Contribute to HL7 AU Test Data
We value contributions to **au-fhir-test-data**. Here’s how you can help:

### 1. Communicate Before You Start
- Before contributing, open a [GitHub issue](https://github.com/hl7au/au-fhir-test-data/issues) to discuss your plans. This helps *avoid duplication of effort, align with project priorities, and ensure your contributions fit within the project's scope. Refer to the [HL7 AU Test Data Project Scope Statement](https://confluence.hl7.org/display/HA/HL7+Australia+Project+Registry?preview=/184927329/248874957/Test%20Data%20Project%201.2.pdf) for guidance.
- Ownership of test data remains with the respective Implementation Guide (IG) projects. As such, all contributions require appropriate review and endorsement from the relevant project teams. 
- Administrative resources are centrally defined and managed to maintain their [Synthetic Data Properties](#Synthetic-Data-Properties). When referencing to these resources, please engage with the project team to require allocation and/or creation.
- Join the monthly HL7 AU Infrastructure and Tooling Community Meetings ([register here](https://confluence.hl7.org/display/HAFWG/Infrastructure+and+Tooling+Contact+List)) where we discuss and triage issues. Feel free to add your issue to the [meeting agenda](https://confluence.hl7.org/pages/viewpage.action?pageId=265492851#CommunityMeetingAgendaandMinutes-MeetingDetails) and we'll aim to discuss your issue/ proposed contribution when you are present at the meeting.
- Use Zulip to connect with the team and community asynchronously: 
  - Specific topic for the HL7 AU Test Data project: [AU FHIR Test Data](https://chat.fhir.org/#narrow/stream/179173-australia/topic/AU.20FHIR.20Test.20Data)
  - General: [Australia Stream](https://chat.fhir.org/#narrow/stream/179173-australia)

### 2. Contribute
1. Fork this repository.
2. Create a branch and use the GitHub issue number followed by a meaningful description as the branch name for your test data contribution, sticking to lowercase and hyphens to separate words. For example, the following is a branch for GitHub issue #123 for adding resources with logical references: `123-logical-refs`
3. Make your contributions/ changes.
4. Submit a pull request (PR) for review.
5.  Once the PR has been reviewed and feedback addressed collaboratively, it will be merged into the master branch.

# HL7 Australia License and Legal

## Licensing Overview

This repository [`hl7au / au-fhir-test-data`](https://github.com/hl7au/au-fhir-test-data) and its release packages for the [HL7 AU FHIR Test Data project](https://confluence.hl7.org/spaces/HA/pages/184927329/HL7+Australia+Project+Registry) are licensed under the [Creative Commons Legal Code (Creative Commons Zero v1.0 Universal)](https://github.com/hl7au/au-fhir-test-data/blob/master/LICENSE.md#CreativeCommonsLegalCode).

## HL7 Australia Intellectual Property Policy

HL7 Australia has an overarching intellectual property policy in place. The [HL7 Australia - Intellectual Property Policy](https://hl7.org.au/fhir/hl7a_ip_policy.pdf) document defines the HL7 Australia organisation's position on many aspects related to copyright, licensing, and liabilities. This policy document is maintained with the current official position of HL7 Australia with respect to these considerations.

## Disclaimer and Warning of Use

HL7 Australia provides HL7 Australia content for informational and reference purposes. While HL7 Australia and the broader HL7 community endeavour to ensure the accuracy and reliability of HL7 Australia content, to the extent permitted by law, HL7 Australia:

1. **Makes no warranties, express or implied:**
    (i) that HL7 Australia content will not infringe upon any third-party intellectual property rights, including patents, copyrights, trademarks, or trade secrets; or
    (ii) that HL7 Australia content is suitable, complete, or applicable for any particular purpose or use contemplated by the User.
2. **Shall not be liable** for any direct, indirect, incidental, special, consequential, or punitive damages arising out of or in connection with the use or reliance on HL7 Australia content.

By accessing or using HL7 Australia content, Users agree to indemnify and hold harmless HL7 Australia, its officers, directors, employees, agents, and contributors of HL7 Australia content from any claims, damages, losses, liabilities, costs, or expenses (including legal fees) arising out of or in connection with the User’s use of or reliance on HL7 Australia content.

## Third-party Artefacts and Terminologies
HL7 Australia materials contain and reference intellectual property owned by third parties ("Third Party IP"). Acceptance of these License Terms does not grant any rights with respect to Third Party IP. The licensee alone is responsible for identifying and obtaining any necessary licences or authorisations to utilise Third Party IP in connection with the specification or otherwise.

Following is a non-exhaustive list of third-party artefacts and terminologies that may require a separate licence:
<table>
  <tr><td>Artefact / Terminology</td><td>Statement</td></tr>
  <tr><td>SNOMED CT</td><td>International Healthcare Terminology Standards Developing Organization (IHTSDO). Where this specification includes or references content from SNOMED CT, which is copyright © 2002+ International Health Terminology Standards Development Organisation (IHTSDO) it is distributed by agreement between IHTSDO and HL7, or the Australian Digital Health Agency via NCTS terms. Implementer use of SNOMED CT is not covered by this agreement</td></tr>
  <tr><td>Logical Observation Identifiers Names & Codes (LOINC)</td><td>This material contains content from LOINC (http://loinc.org). LOINC is copyright © 1995-2020, Regenstrief Institute, Inc. and the Logical Observation Identifiers Names and Codes (LOINC) Committee and is available at no cost under the license at http://loinc.org/license. LOINC® is a registered United States trademark of Regenstrief Institute, Inc.</td></tr>
  <tr><td>National Clinical Terminology Services (NCTS)</td><td>This material contains references to National Clinical Terminology Service artefacts these are Copyright © 2024 Australian Digital Health Agency, implementer user of this content are advised of the NCTS Terms of Use (https://www.healthterminologies.gov.au/ncts-website-terms-of-use/).</td></tr>
</table>
