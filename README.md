# HL7 AU FHIR Test Data
HL7 AU FHIR Test Data contains sample FHIR instances for testing purposes, and to support developers. This repository includes synthetic (realistic but not real) data that conforms to HL7 AU FHIR Implementation Guides (IGs). The synthetic data covers a broader and expanded content scope over that in the FHIR instance examples included in published HL7 AU FHIR IGs. 

This repository also contains 'test' data for some HL7 AU IGs, used to test fail cases. This data not conform to HL7 AU FHIR Implementation Guides. 

## Synthetic Data Properties
- Patients, Practitioners, PractitionerRoles, Organizations are not generated from a real world set. Any correspondence to real people is entirely accidental.
- Resources with an IHI, HPI-I, or HPI-O have been provided by Services Australia and are present in the HI Vendor Test Environment. These resources may be in tests within that environment.
- Australian phone numbers are from the reserved set provided by the Australian Communications and Media Authority for use in creative works.
- Email addresses use the following domains set aside for development and testing: 'example', 'myownpersonaldomain domain', and 'my-own-personal-domain domain'.
- Addresses are valid addresses based on publically available address data from Australia Post.
- Names are randomly generated.
- IHIs, HPI-Os, HPI-Is are provided by Services Australia for test purposes and will pass Luhn check.
- Medicare Card Numbers and DVA numbers are provided by Services Australia for test purposes.
- Australian Health Practitioner Regulation Agency (Ahpra) Registration Numbers are provided by Services Australia for test purposes.
- ABNs present in the data for fictious organisations are not valid ABNs, i.e. they will not pass validity checks.
- Data in clinical resources e.g. AllergyIntolerance is not generated from a real world set.

## How to navigate this repository
Synthetic FHIR JSON files are located: https://github.com/hl7au/au-fhir-test-data/tree/master/generated

Postman collections are located: https://github.com/hl7au/au-fhir-test-data/tree/master/Postman

Test FHIR JSON files are located in:
* https://github.com/hl7au/au-fhir-test-data/tree/master/au-core-inferno-tests
* coming soon for AU eRequesting

This repository also contains source code for the command line utilities used to generate the FHIR JSON files and upload them to a FHIR Server. These utilities have been developed using DotNet. For further details see [Test Data Command Line Utilities](#test-data-command-line-utilities) below.

## Sparked AU Core Testing
We suggest using the [Sparked Test Data Postman collection](https://github.com/hl7au/au-fhir-test-data/blob/master/Postman/Sparked%20Test%20Data.postman_collection.json).

This collection contains a selection of resources from the [generated](https://github.com/hl7au/au-fhir-test-data/tree/master/generated) and [direct-fhir-test-resources](https://github.com/hl7au/au-fhir-test-data/tree/master/direct-fhir-test-resources) folders.

If you would like to upload all the Sparked Test Data set to your FHIR server, use the UploadGenerated.bat and UploadDirect.bat batch files. Refer to the instructions below in the section [Upload Data](https://github.com/hl7au/au-fhir-test-data/blob/master/README.md#upload-data).

## Significant Test Data Test Cases
The following test data files within the direct-fhir-test-resources folder support testing of significant test cases including missing and suppressed data.

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
Search the Issues list in [GitHub](https://github.com/hl7au/au-fhir-test-data/issues) to ensure the error was not already reported.

If you're unable to find an open bug addressing the problem, please create a bug report or issue in this project. 

## Contributing to HL7 AU Test Data

### 1. Discuss an issue in chat.fhir.org

If you have a question, feature request, or proposed change, the best place to start is Zulip i.e. the https://chat.fhir.org/#narrow/stream/179173-australia/topic/AU.20FHIR.20Test.20Data topic. 

### 2. Log an issue in GitHub

Search the Issues list in [GitHub](https://github.com/hl7au/au-fhir-test-data/issues) to check if this has already been reported. 

If you're unable to find an open request, please create a [GitHub](https://github.com/hl7au/au-fhir-test-data/issues) to:
- contribute test data to the repository: state your details and the nature of the test data to be contributed
- suggest improvements or enhancements to the synthetic or test data set 

# Test Data Command Line Utilities
There are two command line utilities to generate the FHIR JSON files and upload the generated test data to a FHIR Server. These utilites are developed using DotNet.

## Sparked.Csv2FhirMapping
The Sparked.Csv2FhirMapping is a utility that maps the CSV files located in the testdata-csv folder and generates the FHIR JSON files. 
The Sparked.Csv2FhirMapping.sln has a dependency on the `fhir-net-mappinglanguage` submodule, which needs to be initialised as part of cloning this repo, or if you have already clone this repository you can initialise the submodule retrospectively.

### Initialise submodules as part of cloning the repo
```
$ git clone --recurse-submodules https://github.com/hl7au/au-fhir-test-data.git

```

### Retrospectively initialise submodules after cloning the repo
```
$ git submodule update --init

```
After executing the submodule update command, the `fhir-net-mappinglanguage` will no longer be empty.

### Building Sparked.Csv2FhirMapping

0. Install the dotnet framework in the appropriate version.
1. Open a Command Prompt `cmd` ([advice](https://www.digitalcitizen.life/open-cmd/))
2. Type `BuildCsvFhirMapping.bat`. This will execute a batch file that builds.


### Generate data

#### Generate Specific Data

1. Open a Command Prompt `cmd` ([advice](https://www.digitalcitizen.life/open-cmd/))
2. Type `GenerateData.bat ` followed by an output directory and resource type. This will execute a batch file that generates.

Usage:
```
GenerateData.bat output-folder resource-type
```

Example with local directory `generated` and resource type `Patient`: 
```
GenerateData.bat generated Patient
```

#### Generate All Data

1. Open a Command Prompt `cmd` ([advice](https://www.digitalcitizen.life/open-cmd/))
2. Type `GenerateAll.bat `. This will execute a batch file that generates all.

Usage:
```
GenerateAll.bat
```

## Upload Data
The Sparked.TestDataClient is a command line utility that uploads a batch of FHIR JSON files to a FHIR Server.

### Building Sparked.TestDataClient

0. Install the dotnet framework in the appropriate version.
1. Open a Command Prompt `cmd` ([advice](https://www.digitalcitizen.life/open-cmd/))
2. Type `BuildTestDataClient.bat`. This will execute a batch file that builds.

### Uploading

#### Upload specific data

1. Open a Command Prompt `cmd` ([advice](https://www.digitalcitizen.life/open-cmd/))
2. Type `UploadData.bat `. This will execute a batch file that uploads all to the fhir-server of the specified resource-type located in the input-folder. The FHIR server request's Authorization header is generated using the  auth-scheme and auth-parameter arguments.

Usage:
```
UploadData.bat fhir-server auth-scheme auth-parameter input-folder resource-type
```

Example: 
```
UploadData.bat https://sparked.npd.telstrahealth.com/smile/fhir/DEFAULT Basic {{base64-encouded-userid:password}} generated Patient
```

#### Upload all generated data
1. Open a Command Prompt `cmd` ([advice](https://www.digitalcitizen.life/open-cmd/))
2. Type `UploadGenerated.bat `. This will execute a batch file that uploads all to the fhir-server all data located in the folder `generated`. The FHIR server request's Authorization header is generated using the  auth-scheme and auth-parameter arguments.

Usage:
```
UploadGenerated.bat fhir-server auth-scheme auth-parameter
```

Example: 
```
UploadGenerated.bat https://sparked.npd.telstrahealth.com/smile/fhir/DEFAULT Basic {{base64-encouded-userid:password}}
```

#### Upload all generated eRequesting data
1. Open a Command Prompt `cmd` ([advice](https://www.digitalcitizen.life/open-cmd/))
2. Type `UploadERequesting.bat `. This will execute a batch file that uploads all to the fhir-server all eRequesting data located in the folder `generated`. The FHIR server request's Authorization header is generated using the  auth-scheme and auth-parameter arguments.

Usage:
```
UploadERequesting.bat fhir-server auth-scheme auth-parameter
```

Example: 
```
UploadERequesting.bat https://sparked.npd.telstrahealth.com/smile/fhir/DEFAULT Basic {{base64-encouded-userid:password}}
```
