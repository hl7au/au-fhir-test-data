# Test Data Properties

`WIP`

## Base Resources

`Placeholder to describe personas are fake`

- Names are randomly picked.
- Addresses are valid addresses based on publicly available address data from Australia Post.
- Australian phone numbers are from the reserved set provided by the Australian Communications and Media Authority for use in creative works. 
- Email addresses use the following domains set aside for development and testing: 'example', 'myownpersonaldomain domain', and 'my-own-personal-domain domain'. 
- Resources with an IHI, HPI-I, or HPI-O have been provided by Services Australia and are present in the HI Vendor Test Environment. These resources may be in tests within that environment.
- IHIs, HPI-Os, HPI-Is are provided by Services Australia for test purposes and will pass Luhn check. 
- Medicare Card Numbers and DVA numbers are provided by Services Australia for test purposes.
- Australian Health Practitioner Regulation Agency (Ahpra) Registration Numbers are provided by Services Australia for test purposes.
- ABNs present in the data for fictious organisations are not valid ABNs, i.e. they will not pass validity checks.

## Clinical Resources

`Placeholder`

### Patient Summary Document Bundles

`Placeholder`

### Patients

| Patient ID | AU Core | eRequesting | Inferno |
| ------------- | ------------- | -- | -- |
| baratz-toni | Y | N | Y |

## Missing and Suppressed
Test data for verifying missing data and suppressed data test cases are included in the data set, see [Missing and Suppressed Data](/docs/MissingAndSuppressedData_TestData.md).

## Data Integrity
- Relationships between different entities are maintained as accurately as possible. For example, *PractitionerRoles* are appropriately linked to *Practitioners* and *Organizations*, reflecting real-world associations.
- All instances, with the exception of [quarantined instances](/.github/validate/validator_quarantine), pass FHIR validation.
- All references, with the exception of these in [quarantined instances](/.github/scripts/reference_integrity_quarantine), exist in the data set.