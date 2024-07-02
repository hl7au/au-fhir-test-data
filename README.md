## HL7 AU FHIR Test Data
HL7 AU FHIR Test Data contains sample FHIR instances for testing purposes, and to support developers. This repository includes synthetic (realistic but not real) data that conforms to HL7 AU FHIR Implementation Guides (IGs). The synthetic data covers a broader and expanded content scope over that in the FHIR instance examples included in published HL7 AU FHIR IGs. 

This repository also contains 'test' data for some HL7 AU IGs, used to test fail cases. This data not conform to HL7 AU FHIR Implementation Guides. 

### Synthetic Data Properties
- Patients, Practitioners, PractitionerRoles, Organizations are not generated from a real world set. Any correspondence to real people is entirely accidental.
- Resources with an IHI, HPI-I, or HPI-O have been provided by Services Australia and are present in the HI Vendor Test Environment. These resources may in tests with that environment.
- Australian phone numbers are from the reserved set provided by the Australian Communications and Media Authority for use in creative works.
- Email addresses use domains set aside for testing and developing: example domain or myownpersonaldomain domain or my-own-personal-domain domain.
- Addresses are valid addresses based on publically available address data from Australia Post.
- Names are randomly generated.
- IHIs, HPI-Os, HPI-Is are provided by Services Australia for test purposes and will pass Luhn check.
- ABNs present in the data for fictious organisations are not valid ABNs, i.e. they will not pass validity checks.
- Data in clinical resources e.g. AllergyIntolerance is not generated from a real world set.

## How to navigate this repository
Synthetic FHIR JSON files are located: https://github.com/hl7au/au-fhir-test-data/tree/master/generated

Postman collections are located: https://github.com/hl7au/au-fhir-test-data/tree/master/Postman

Test FHIR JSON files are located in:
* https://github.com/hl7au/au-fhir-test-data/tree/master/au-core-inferno-tests
* coming soon for AU eRequesting

This repository also contains source code for the command line utilities used to generate the FHIR JSON files and upload them to a FHIR Server. These utilities have been developed using DotNet. For further details see [Test Data Command Line Utilities](#test-data-command-line-utilities) below.

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