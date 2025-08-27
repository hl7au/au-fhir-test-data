# Test Data Properties

## Base Resources

The base resources (Patient, RelatedPerson, Coverage, Practitioner, PractitionerRole, Organisation, Location, HealthcareService) in this dataset are sythetic (realistic but not real). Any resemblance to real persons, organizations or locations is purely coincidental.

- Names are supplyed by Service Australia from the HI Vendor Test Environment or randomly picked.
- Addresses are valid addresses based on publicly available address data from Australia Post.
- Australian phone numbers are from [the reserved set](https://www.acma.gov.au/phone-numbers-use-tv-shows-films-and-creative-works) provided by the Australian Communications and Media Authority for use in creative works. 
- Email addresses use the following domains set aside for development and testing: 'example', 'myownpersonaldomain domain', and 'my-own-personal-domain domain'. 
- Resources with an IHI, HPI-I, or HPI-O have been provided by Services Australia and are present in the HI Vendor Test Environment. These resources may be in tests within that environment.
- IHIs, HPI-Os, HPI-Is are provided by Services Australia for test purposes and will pass Luhn check. 
- Medicare Card Numbers and DVA numbers are provided by Services Australia for test purposes.
- Australian Health Practitioner Regulation Agency (Ahpra) Registration Numbers are provided by Services Australia for test purposes.
- ABNs present in the data for fictious organisations are not valid ABNs, i.e. they will not pass validity checks.

## Clinical Resources

The clinical resources (AllergyIntolerance, ServiceRequest, etc.) in this dataset are created by clinical work group to support development and testing. They reflect clinical use cases but have no resemble to any real world event.

### Patients with clinical resources associated

The following patients:
- have AU Core clinical resources (AllergyIntolerance, Condition, Procedure, etc.) associated
- are good candidates to generate Patient Summary documents
- are used by default in the [Inferno AU Core Test Suites](https://inferno.dev.hl7.org.au/test-kits/au-core/)

| Patient ID |
| ---------- |
| baratz-toni |
| irvine-ronny-lawrence |
| italia-sofia |
| howe-deangelo |
| hayes-arianne |
| baby-banks-john |
| banks-mia-leanne |

The following patients have AU eRequesting resources (ServiceRequest, Task, etc.) associated:

| Patient ID |
| ---------- |
| belger-remedios |
| roberts-fred |

### Patient Summary Document Bundles

Sample of AU Patient Summary Bundles are included in the dataset to demostrate the sections.

## Missing and Suppressed
Test data for verifying missing data and suppressed data test cases are included in the data set, see [Missing and Suppressed Data](/docs/MissingAndSuppressedData_TestData.md).

## Data Integrity
- Relationships between different entities are maintained as accurately as possible. For example, *PractitionerRoles* are appropriately linked to *Practitioners* and *Organizations*, reflecting real-world associations.
- All instances, with the exception of [quarantined instances](/.github/validate/validator_quarantine), pass FHIR validation.
- All references, with the exception of these in [quarantined instances](/.github/scripts/reference_integrity_quarantine), exist in the data set.