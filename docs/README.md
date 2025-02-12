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

- **Coverage of an Implementation Guide (IG)**: The test dataset aims to provide comprehensive coverage of IG profiles and extensions. For [AU Core Test Data Coverage](https://github.com/hl7au/au-fhir-test-data?tab=readme-ov-file#au-core-test-data-coverage) this means coverage of the *Must Support* elements of AU Core profiles and extensions.

## How to navigate this repository
Synthetic FHIR test data (JSON) files are located in: 
* [generated](https://github.com/hl7au/au-fhir-test-data/tree/master/generated) directory
* [direct-fhir-test-resources](https://github.com/hl7au/au-fhir-test-data/tree/master/direct-fhir-test-resources) directory
* [erequesting](https://github.com/hl7au/au-fhir-test-data/tree/master/erequesting) directory (stub - to be expanded)
* [aups](https://github.com/hl7au/au-fhir-test-data/tree/master/aups) directory (stub - to be expanded)

Postman collection import files containing a selection of AU Core and AU eRequesting Test Data are located in the [Postman](https://github.com/hl7au/au-fhir-test-data/tree/master/Postman) directory
* [Sparked AUCore Test Data.postman_collection.json](https://github.com/hl7au/au-fhir-test-data/tree/master/Postman/Sparked%20AUCore%20Test%20Data.postman_collection.json)
* [Sparked AUeRequesting Test Data.postman_collection.json](https://github.com/hl7au/au-fhir-test-data/tree/master/Postman/Sparked%20AUeRequesting%20Test%20Data.postman_collection.json)

Sample Postman environment import files are also located in the [Postman](https://github.com/hl7au/au-fhir-test-data/tree/master/Postman) directory:
* [Sparked AUCore Test Data.postman_environment.json](https://github.com/hl7au/au-fhir-test-data/tree/master/Postman/Sparked%20AUCore%20Test%20Data.postman_environment.json)
* [Sparked eReq FHIR Server Filler.postman_environment.json](https://github.com/hl7au/au-fhir-test-data/tree/master/Postman/Sparked%20eReq%20FHIR%20Server%20Filler.postman_environment.json)
* [Sparked eReq FHIR Server Placer.postman_environment.json](https://github.com/hl7au/au-fhir-test-data/tree/master/Postman/Sparked%20eReq%20FHIR%20Server%20Placer.postman_environment.json)

## Sparked AU Core Testing
We suggest using the [Sparked Test Data Postman collection](https://github.com/hl7au/au-fhir-test-data/blob/master/Postman/Sparked%20Test%20Data.postman_collection.json) which contains:
* AU Core profiles, a selection of resources from the [generated](https://github.com/hl7au/au-fhir-test-data/tree/master/generated) and [direct-fhir-test-resources](https://github.com/hl7au/au-fhir-test-data/tree/master/direct-fhir-test-resources) directorys, including resource instances with missing data and suppressed data.
* AU Base Coverage resources.
* AU Base Healthcare Service resources.
* AU Base Related Person resources.
* AU Base Specimen resource(s).

Currently, this Postman collection does not contain non-conformant resources for negative testing.

### AU Core Test Data Coverage
For Release v1.0.0 of the HL7 FHIR AU Test Data community project, the test data coverage of the Must Support elements in AU Core profiles and extensions is reported in [AUCoreTestDataCoverage.md](https://github.com/hl7au/au-fhir-test-data/blob/master/AUCoreTestDataCoverage.md).

### Significant Test Data Test Cases
The following test data files within the [direct-fhir-test-resources](https://github.com/hl7au/au-fhir-test-data/tree/master/direct-fhir-test-resources) directory support testing of significant test cases including missing and suppressed data.

File Name | Resource Id | Test Case | Expected Outcome 
--- | --- | --- | ---
Patient-italia-sofia-suppressed-birthDate.json | italia-sofia-suppressed-birthDate | Patient with a suppressed birthDate | A Responder SHALL correctly populate a Data Absent Reason extension within a primitate data type extension and a Requester SHALL accept this extension without error. 
Patient-italia-sofia-suppressed-gender.json | italia-sofia-suppressed-gender | Patient with a suppressed gender | A Responder SHALL correctly populate using value of 'unknown' and a Requester SHALL accept the 'unknown' value without error.
Patient-italia-sofia-suppressed-identifier.json | italia-sofia-suppressed-identifier | Patient with suppressed identifiers | A Responder SHALL correctly populate a Data Absent Reason extension within Identifier.extension and a Requester SHALL accept this extension without error. **Currently validation using the Sparked Reference FHIR Server rejects this instance due to rule au-core-pat-01.**
Patient-italia-sofia-suppressed-name.json | italia-sofia-suppressed-name | Patient with suppressed names | A Responder SHALL correctly populate a Data Absent Reason extension within HumanName.extension and a Requester SHALL accept this extension without error. **Currently validation using the Sparked Reference FHIR Server rejects this instance due to rules au-core-pat-02 and au-core-pat-04.**
Observation-pathresult-missing-effective.json | pathresult-missing-effective | Pathology Result Observation with missing effectiveDateTime | A Responder SHALL correctly populate a Data Absent Reason extension represented using a primitate data type extension, and a Requester SHALL accept this extension without error. **Currently validation using the Sparked Reference FHIR Server rejects this instance due to rule Rule au-core-obs-01.**
Observation-pathresult-missing-status.json | pathresult-missing-status | Pathology Result Observation with missing status | A Responder SHALL correctly populate using value of 'unknown', and a Requester SHALL accept this value without error.
Observation-pathresult-suppressed-code.json | pathresult-suppressed-code | Pathology Result Observation with suppressed code | A Responder SHALL correctly populate the coding using a code (masked or unknown) from the Data Absent Reason value set, and a Requester SHALL accept this coding without error. 
Observation-pathresult-suppressed-dataAbsentReason.json | pathresult-suppressed-dataAbsentReason | Pathology Result Observation with suppressed value using dataAbsentReason | Using dataAbsentReason is NOT the recommended representation of a suppressed test result value in AU Core. 
Observation-pathresult-suppressed-subject.json | pathresult-suppressed-subject | Pathology Result Observation with suppressed subject | A Responder SHALL correctly populate a Data Absent Reason extension within Reference.extension and a Requester SHALL accept this extension without error.
Observation-pathresult-suppressed-valueCodeableConcept.json | pathresult-suppressed-valueCodeableConcept | Pathology Result Observation with suppressed codeable value | A Responder SHALL correctly populate the coding with a code (masked or unknown) from the Data Absent Reason value set, and a Requester SHALL accept this coding without error. 
Observation-pathresult-suppressed-valueQuantity.json | pathresult-suppressed-valueQuantity | Pathology Result Observation with suppressed non-coded value (complex data types) | A Responder SHALL correctly populate a Data Absent Reason extension within the value[x].extension and a Requester SHALL accept this extension without error. 

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

There is basic [documentation for the development process and tooling here](https://confluence.hl7.org/display/HAFWG/Process%3A+Test+Data+-+iterative+development).