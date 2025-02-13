# HL7 AU FHIR Test Data
HL7 AU FHIR Test Data contains sample FHIR instances for testing purposes, and to support developers. This repository includes synthetic (realistic but not real) data that conforms to HL7 AU FHIR Implementation Guides (IGs). The synthetic data covers a broader and expanded content scope over that in the FHIR instance examples included in published HL7 AU FHIR IGs.

## Synthetic Data Properties

- **Conformance**: The synthetic data generated aims to conform to the structures and constraints defined in the corresponding HL7 AU FHIR Implementation Guides, as indicated. Some data may be intentionally non-conformant to support negaitve testing scenarios.

- **Anonymity and Realism**: All data is synthetic, containing no personally identifiable information (PII) or protected health information (PHI). It is generated to approximate real-world properties and relationships found in actual healthcare data to support testing and development. The dataset includes Patients, Practitioners, PractitionerRoles, Organizations, Healthcare Services, and clinical resources such as *AllergyIntolerance*. Any resemblance to real entities is purely coincidental. Specifically,
  - Names are randomly generated.
  - Addresses are valid addresses based on publicly available address data from Australia Post.
  - Australian phone numbers are from the reserved set provided by the Australian Communications and Media Authority for use in creative works. 
  - Email addresses use the following domains set aside for development and testing: 'example', 'myownpersonaldomain domain', and 'my-own-personal-domain domain'. 
  - Resources with an IHI, HPI-I, or HPI-O have been provided by Services Australia and are present in the HI Vendor Test Environment. These resources may be in tests within that environment.
  - IHIs, HPI-Os, HPI-Is are provided by Services Australia for test purposes and will pass Luhn check. 
  - Medicare Card Numbers and DVA numbers are provided by Services Australia for test purposes.
  - Australian Health Practitioner Regulation Agency (Ahpra) Registration Numbers are provided by Services Australia for test purposes.
  - ABNs present in the data for fictious organisations are not valid ABNs, i.e. they will not pass validity checks.

- **Unbiased**: The dataset is intended to avoid biases in data representation.

- **Consistency**: Relationships between different entities are maintained as accurately as possible. For example, *PractitionerRoles* are appropriately linked to *Practitioners* and *Organizations*, mirroring real-world associations.

## How to navigate this repository
Synthetic FHIR test data (JSON) files are available in the following directories: 
* [generated](https://github.com/hl7au/au-fhir-test-data/tree/master/generated) – contains test data generated from other source formats (e.g., XLS/CSV, QuestionnaireResponse) using tooling that includes mappings and utilities for conversion and validation,
* [direct-fhir-test-resources](https://github.com/hl7au/au-fhir-test-data/tree/master/direct-fhir-test-resources) - includes test data for verifying missing data and suppressed data test cases (for details see ),
* [erequesting](https://github.com/hl7au/au-fhir-test-data/tree/master/erequesting) _(stub - to be expanded)_,
* [aups](https://github.com/hl7au/au-fhir-test-data/tree/master/aups) _(stub - to be expanded)_.

Postman collection import files containing a selection of AU Core and AU eRequesting Test Data are located in the [Postman](https://github.com/hl7au/au-fhir-test-data/tree/master/Postman) directory
* [Sparked AUCore Test Data.postman_collection.json](https://github.com/hl7au/au-fhir-test-data/tree/master/Postman/Sparked%20AUCore%20Test%20Data.postman_collection.json)
* [Sparked AUeRequesting Test Data.postman_collection.json](https://github.com/hl7au/au-fhir-test-data/tree/master/Postman/Sparked%20AUeRequesting%20Test%20Data.postman_collection.json)

Sample Postman environment import files are also located in the [Postman](https://github.com/hl7au/au-fhir-test-data/tree/master/Postman) directory:
* [Sparked AUCore Test Data.postman_environment.json](https://github.com/hl7au/au-fhir-test-data/tree/master/Postman/Sparked%20AUCore%20Test%20Data.postman_environment.json)
* [Sparked eReq FHIR Server Filler.postman_environment.json](https://github.com/hl7au/au-fhir-test-data/tree/master/Postman/Sparked%20eReq%20FHIR%20Server%20Filler.postman_environment.json)
* [Sparked eReq FHIR Server Placer.postman_environment.json](https://github.com/hl7au/au-fhir-test-data/tree/master/Postman/Sparked%20eReq%20FHIR%20Server%20Placer.postman_environment.json)

### Test Data Coverage of HL7 AU FHIR Implementation Guides
The test dataset is developed on a best-effort basis, aiming to provide broad coverage of HL7 AU IG profiles and extensions. The extent of coverage evolves iteratively, shaped by the maturity of the IGs, shifting priorities of HL7 AU projects, available resources, and community contributions. For example, in the case of the AU Core IG, the dataset includes coverage of Must Support elements within AU Core profiles and extensions. The current coverage is documented in [AUCoreTestDataCoverage.md](https://github.com/hl7au/au-fhir-test-data/blob/master/AUCoreTestDataCoverage.md).

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
- Open a [GitHub issue](https://github.com/hl7au/au-fhir-test-data/issues) to discuss your plans to help avoid duplication of effort, align and prioritise your contributions based on the scope of the project - refer to the [HL7 AU Test Data Project Scope Statement](https://confluence.hl7.org/display/HA/HL7+Australia+Project+Registry?preview=/184927329/248874957/Test%20Data%20Project%201.2.pdf).
- Join the fortnightly HL7 AU Infrastructure and Tooling Community Meetings ([register here](https://confluence.hl7.org/display/HAFWG/Infrastructure+and+Tooling+Contact+List)) where we discuss and triage issues. Feel free to add your issue to the [meeting agenda](https://confluence.hl7.org/pages/viewpage.action?pageId=265492851#CommunityMeetingAgendaandMinutes-MeetingDetails) and we'll aim to discuss your issue/ proposed contribution when you are present at the meeting.
- Use Zulip to connect with the team and community asynchronously: 
  - Specific topic for the HL7 AU Test Data project: [AU FHIR Test Data](https://chat.fhir.org/#narrow/stream/179173-australia/topic/AU.20FHIR.20Test.20Data)
  - General: [Australia Stream](https://chat.fhir.org/#narrow/stream/179173-australia)

### 2. Contribute
1. Fork this repository.
2. Create a branch and use the GitHub issue number followed by a meaningful description as the branch name for your test data contribution, sticking to lowercase and hyphens to separate words. For example, the following is a branch for GitHub issue #123 for adding resources with logical references: `123-logical-refs`
3. Make your contributions/ changes.
4. Submit a pull request (PR) for review.
5.  Once the PR has been reviewed and feedback addressed collaboratively, it will be merged into the main branch.

## Development Process

[Documentation for the development process and tooling here](https://confluence.hl7.org/display/HAFWG/Process%3A+Test+Data+-+iterative+development).

**_include info on what source data - resource types, fields etc. are linked/derived from Service Australia provided data and therefore are protected / cannot be changed with governance controls/reviews. Other commits involving changes to quarantined files also require careful review. 
Explain the what, why and how in relation to the quarantine files. i.e. process is that reported validator errors that can be explained i.e. not actual test data errors and related to tooling etc. are moved to quarantine directory and not included in the validate workflows._**