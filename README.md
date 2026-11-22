# HL7 AU FHIR Test Data

Synthetic (realistic but not real) FHIR test data for the HL7 AU FHIR Implementation Guides (IGs). The data is broader than the examples published in the IGs and is used for Connectathons, Sparked test events and developer testing.

> [!WARNING]
> The resources in this repository are for testing and demonstration only. Do not add any real personal or health information. All persons and health data are fictional; see [Synthetic Data Properties](docs/README.md#synthetic-data-properties) for how names, addresses, contact details and identifiers were made, including the Services Australia identifiers that may coincide with real ones.

## Folder layout

All FHIR JSON lives under [`au-fhir-test-data-set/`](au-fhir-test-data-set/). Each folder has an owner who reviews and approves changes to it (details in [CONTRIBUTING.md](CONTRIBUTING.md#ownership-and-approval)).

| Folder | IG | Owner |
| --- | --- | --- |
| `au-core` | AU Core | Sparked |
| `au-patient-summary` | AU Patient Summary | Sparked |
| `au-erequesting` | AU eRequesting | Michael Osborne |
| `connected-care` | AU Core, AU Patient Summary and AU eRequesting, per story | Connectathon track leads |
| `au-base` | AU Base | Not yet assigned (folder is empty) |

Services Australia derived data (such as Medicare, IHI and HPI identifiers) and its CSV exports are owned by Heath Frankel. Other projects may add and manage their own starter test data in their own folder.

## Reporting a problem or asking for data

Search the [existing issues](https://github.com/hl7au/au-fhir-test-data/issues) first, then open a [new issue](https://github.com/hl7au/au-fhir-test-data/issues/new/choose) and pick the form that fits: a problem with existing test data, a request for new test data, or a problem with the tooling and checks. Questions are welcome on the [AU FHIR Test Data topic](https://chat.fhir.org/#narrow/stream/179173-australia/topic/AU.20FHIR.20Test.20Data) on chat.fhir.org.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how issues are triaged, how to raise a pull request, the checks that run on it, and who approves it.

## Releases

Releases are tagged from `master` as described in the [release strategy](docs/HL7AUFHIRTestDataReleaseStrategy.md). The JSON on `master` and in tagged releases is what consumers should use.

## More information

- [docs/README.md](docs/README.md): synthetic data properties, versioning, licensing and legal notices.
- [Missing and suppressed data test cases](docs/MissingAndSuppressedData_TestData.md).
- [HL7 AU FHIR Test Data project page](https://confluence.hl7.org/spaces/HAFWG/pages/273942754) on HL7 Confluence.

This repository is licensed under [CC0 1.0 Universal](LICENSE).
