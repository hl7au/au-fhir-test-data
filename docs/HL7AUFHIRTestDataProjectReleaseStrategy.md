# HL7 AU FHIR Test Data Project Release Strategy

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
