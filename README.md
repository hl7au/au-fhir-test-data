## HL7 AU FHIR Test Data
HL7 AU FHIR Test Data contains sample FHIR instances for testing purposes, and to support developers. This repository includes synthetic (realistic but not real) data that conforms to HL7 AU FHIR Implementation Guides (IGs). The synthetic data covers a broader and expanded content scope over that in the FHIR instance examples included in published HL7 AU FHIR IGs. 

This repository also contains 'test' data for some HL7 AU IGs, used to test fail cases. This data not conform to HL7 AU FHIR Implementation Guides. 

### Synthetic Data Properties
- Patients, Practitioners, PractitionerRoles, Organizations are not generated from a real world set. Any correspondence to real people is entirely accidental.
- Resources with an IHI, HPI-I, or HPI-O have been provided by Services Australia and are present in the HI Vendor Test Environment. These resources may be in tests with that environment.
- Australian phone numbers are from the reserved set provided by the Australian Communications and Media Authority for use in creative works.
- Email addresses use domains set aside for testing and developing: example domain or myownpersonaldomain domain or my-own-personal-domain domain.
- Addresses are valid addresses based on publically available address data from Australia Post.
- Names are randomly generated.
- IHIs, HPI-Os, HPI-Is are provided by Services Australia for test purposes and will pass Luhn check.
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
After initialising the submodule, use the Sparked.Csv2FhirMapping.sln to build Sparked.Csv2FhirMapping project.

### Using Sparked.Csv2FhirMapping
Using a Command Prompt change to the  Sparked.Csv2FhirMapping folder and execute the command as follows:

```
bin\Debug\net7.0\Csv2Fhir.exe resource-type csv-file output-folder
```

For example:
```
bin\Debug\net7.0\Csv2Fhir.exe Patient "..\testdata-csv\AU Core Sample Data - Patient.csv" ..\generated
```

Alternatively, you can use the GenerateData.bat and GenerateAll.bat batch files as described below.
#### GenerateData.bat
The GenerateData.bat command generates test data to the specified output-folder for the specified resource-type using assocaited CSV file located in the testdata-csv folder.

Usage:
```
GenerateData.bat output-folder resource-type
```

Example: 
```
GenerateData.bat generated Patient
```

#### GenerateAll.bat
The GenerateAll.bat command generates test data for all CSV files located in the testdata-csv folder and creates the JSON files in the `generated` folder.

Usage:
```
GenerateAll.bat
```

## Sparked.TestDataClient
The Sparked.TestDataClient is a command line utility that uploads a batch of FHIR JSON files to a FHIR Server.

### Building Sparked.TestDataClient
Use the Sparked.Csv2FhirMapping.sln located in the Sparked.Csv2FhirMapping folder to build the Sparked.TestDataClient project.

### Using Sparked.TestDataClient
Using a Command Prompt terminal execute the following command from the repository root folder:

```
Sparked.TestDataClient\bin\Debug\net7.0\Sparked.TestDataClient.exe resource-type input-folder fhir-server auth-scheme auth-parameter
```

For example:
```
Sparked.TestDataClient\bin\Debug\net7.0\Sparked.TestDataClient.exe Observation generated https://sparked.npd.telstrahealth.com/smile/fhir/DEFAULT Basic {{base64-encouded-userid:password}}
```

Alternatively, you can use the UploadData.bat, UploadGenerated.bat or UploadERequesting.bat batch files as described below.

#### UploadData.bat
The UploadData.bat command uploads test data to the fhir-server of the specified resource-type located in the input-folder. The FHIR server request's Authorization header is generated using the  auth-scheme and auth-parameter arguments.

Usage:
```
UploadData.bat fhir-server auth-scheme auth-parameter input-folder resource-type
```

Example: 
```
UploadData.bat https://sparked.npd.telstrahealth.com/smile/fhir/DEFAULT Basic {{base64-encouded-userid:password}} generated Patient
```

#### UploadGenerated.bat
The UploadGenerated.bat command uploads all the test data located in the `generated` folder to the fhir-server. The FHIR server request's Authorization header is generated using the  auth-scheme and auth-parameter arguments.

Usage:
```
UploadGenerated.bat fhir-server auth-scheme auth-parameter
```

Example: 
```
UploadGenerated.bat https://sparked.npd.telstrahealth.com/smile/fhir/DEFAULT Basic {{base64-encouded-userid:password}}
```

#### UploadERequestiong.bat
The UploadERequestiong.bat command uploads test data located in the `generated` folder to the fhir-server required for ERequesting. This inbcludes resource types Patient, Organization, Pactitioner and PractitionerRole.
The FHIR server request's Authorization header is generated using the  auth-scheme and auth-parameter arguments.
The ERequesting 

Usage:
```
UploadERequesting.bat fhir-server auth-scheme auth-parameter
```

Example: 
```
UploadERequesting.bat https://sparked.npd.telstrahealth.com/smile/fhir/DEFAULT Basic {{base64-encouded-userid:password}}
```
