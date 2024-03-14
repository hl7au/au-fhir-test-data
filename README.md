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
