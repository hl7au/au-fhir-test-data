## AU Core Test Data Coverage

Disclaimer: While we try to keep this page updated, we cannot guarantee its completeness or accuracy. The summary of test data coverage provided here is for reference only and should not be relied upon for critical purposes. Please use this information alongside your own analysis and judgement.

## au-core-allergyintolerance test data coverage
Profile: AU Core AllergyIntolerance | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-allergyintolerance

| Must Support element                      | HL7 AU FHIR Test Data                                                      |
|:------------------------------------------|:---------------------------------------------------------------------------|
| AllergyIntolerance.clinicalStatus         | Included                                                                   |
| AllergyIntolerance.verificationStatus     | Included                                                                   |
| AllergyIntolerance.code                   | Included                                                                   |
| AllergyIntolerance.patient                | Included                                                                   |
| AllergyIntolerance.onsetDateTime          | Included                                                                   |
| AllergyIntolerance.onsetAge               | Included                                                                   |
| AllergyIntolerance.onsetPeriod            | Included                                                                   |
| AllergyIntolerance.onsetRange             | Included                                                                   |
| AllergyIntolerance.reaction.manifestation | Included                                                                   |
| AllergyIntolerance.reaction.severity      | Included                                                                   |
| AllergyIntolerance.note                   | Included                                                                   |

## au-core-condition test data coverage
Profile: AU Core Condition | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-condition 

| Must Support element         | HL7 AU FHIR Test Data                                             |
|:-----------------------------|:------------------------------------------------------------------|
| Condition.clinicalStatus     | Included                                                          |
| Condition.verificationStatus | Included                                                          |
| Condition.category           | Included                                                          |
| Condition.severity           | Included                                                          |
| Condition.code               | Included                                                          |
| Condition.subject            | Included                                                          |
| Condition.onsetDateTime      | Included                                                          |
| Condition.onsetAge           | Included                                                          |
| Condition.onsetPeriod        | Included                                                          |
| Condition.onsetRange         | Included                                                          |
| Condition.abatementDateTime  | Included                                                          |
| Condition.abatementAge       | Not Included                                                      |
| Condition.abatementPeriod    | Not Included                                                      |
| Condition.abatementRange     | Not Included                                                      |
| Condition.note               | Included                                                          |

## au-core-encounter test data coverage
Profile: AU Core Encounter | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-encounter

| Must Support element             | Type (where there is a choice of data type)                       | HL7 AU FHIR Test Data |
|:---------------------------------|:------------------------------------------------------------------|:----------------------|
| Encounter.status                 |                                                                   | Included              |
| Encounter.class                  |                                                                   | Included              |
| Encounter.serviceType            |                                                                   | Included              |
| Encounter.subject                |                                                                   | Included              |
| Encounter.participant.type       |                                                                   | Included              |
| Encounter.participant.individual | Reference (AU Core Practitioner)                                  | Not Included          |
| Encounter.participant.individual | Reference (AU Core PractitionerRole)                              | Included              |
| Encounter.participant.individual | Reference (AU Base Related Person)                                | Not Included          |
| Encounter.period                 |                                                                   | Included              |
| Encounter.reasonCode             |                                                                   | Included              |
| Encounter.reasonReference        | Reference(AU Core Condition)                                      | Included              |
| Encounter.reasonReference        | Reference(AU Core Observation)                                    | Not Included          |
| Encounter.reasonReference        | Reference(AU Core Procedure)                                      | Not Included          |
| Encounter.location.location      |                                                                   | Included              |
| Encounter.serviceProvider        |                                                                   | Included              |

## au-core-healthcareservice test data coverage
Profile: AU Core HealthcareService | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-healthcareservice

| Must Support element         |  HL7 AU FHIR Test Data |
|:-----------------------------|:-----------------------|
| HealthcareService.identifier | Included               |
| HealthcareService.type       | Included               |
| HealthcareService.name       | Included               |
| HealthcareService.telecom    | Included               |

## au-core-immunization test data coverage
Profile: AU Core Immunization | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-immunization

|  Must Support element                          | HL7 AU FHIR Test Data                                                |
|:-----------------------------------------------|:---------------------------------------------------------------------|
| Immunization.status                            | Included                                                             |
| Immunization.vaccineCode                       | Included                                                             |
| Immunization.vaccineCode.coding:amtVaccineCode | Included                                                             |
| Immunization.vaccineCode.coding:airVaccineCode | Included                                                             |
| Immunization.patient                           | Included                                                             |
| Immunization.occurrenceDateTime                | Included                                                             |
| Immunization.occurrenceString                  | Included                                                             |
| Immunization.primarySource                     | Included                                                             |
| Immunization.lotNumber                         | Included                                                             |
| Immunization.note                              | Included                                                             |

## au-core-location test data coverage
Profile: AU Core Location | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-location

|  Must Support element         | HL7 AU FHIR Test Data                                            |
|:------------------------------|:-----------------------------------------------------------------|
| Location.name                 | Included                                                         |
| Location.type                 | Included                                                         |
| Location.address              | Included                                                         |
| Location.physicalType         | Included                                                         |
| Location.managingOrganization | Included                                                         |

## au-core-medication test data coverage
Profile:AU Core Medication | Profile URL:http://hl7.org.au/fhir/core/StructureDefinition/au-core-medication

|  Must Support element      | HL7 AU FHIR Test Data                                              |
|:---------------------------|:-------------------------------------------------------------------|
| Medication.code            | Included                                                           |
| Medication.code.coding:pbs | Included                                                           |
| Medication.code.coding:amt | Included                                                           |

## au-core-medicationrequest test data coverage
Profile: AU Core MedicationRequest | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-medicationrequest

|  Must Support element                                  | Type (where there is a choice of data type)              | HL7 AU FHIR Test Data |
|:-------------------------------------------------------|:---------------------------------------------------------|:----------------------|
| MedicationRequest.status                               |                                                          | Included              |
| MedicationRequest.intent                               |                                                          | Included              |
| MedicationRequest.medicationCodeableConcept            |                                                          | Included              |
| MedicationRequest.medicationCodeableConcept.coding:pbs |                                                          | Included              |
| MedicationRequest.medicationCodeableConcept.coding:amt |                                                          | Included              |
| MedicationRequest.medicationReference                  |                                                          | Included              |
| MedicationRequest.subject                              |                                                          | Included              |
| MedicationRequest.encounter                            |                                                          | Included              |
| MedicationRequest.authoredOn                           |                                                          | Included              |
| MedicationRequest.requester                            | Reference(AU Core Practitioner)                          | Included              |
| MedicationRequest.requester                            | Reference(AU Core PractitionerRole)                      | Included              |
| MedicationRequest.requester                            | Reference(AU Core Organization)                          | Not Included          |
| MedicationRequest.requester                            | Reference(AU Core Patient)                               | Not Included          |
| MedicationRequest.requester                            | Reference(AU Core RelatedPerson)                         | Not Included          |
| MedicationRequest.reasonCode                           |                                                          | Included              |
| MedicationRequest.reasonReference                      | Reference(AU Core Condition)                             | Included              |
| MedicationRequest.reasonReference                      | Reference(AU Core Observation)                           | Included              |
| MedicationRequest.dosageInstruction                    |                                                          | Included              |
| MedicationRequest.dosageInstruction.text               |                                                          | Included              |

## au-core-medicationstatement test data coverage
Profile: AU Core MedicationStatement | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-medicationstatement

|  Must Support element                                    | Type (where there is a choice of data type)              | HL7 AU FHIR Test Data |
|:---------------------------------------------------------|:---------------------------------------------------------|:----------------------|
| MedicationStatement.status                               |                                                          | Included              |
| MedicationStatement.medicationCodeableConcept            |                                                          | Included              |
| MedicationStatement.medicationCodeableConcept.coding:pbs |                                                          | Included              |
| MedicationStatement.medicationCodeableConcept.coding:amt |                                                          | Included              |
| MedicationStatement.medicationReference                  |                                                          | Included              |
| MedicationStatement.subject                              |                                                          | Included              |
| MedicationStatement.effectiveDateTime                    |                                                          | Included              |
| MedicationStatement.effectivePeriod                      |                                                          | Included              |
| MedicationStatement.reasonCode                           |                                                          | Included              |
| MedicationStatement.reasonReference                      | Reference(AU Core Condition)                             | Included              |
| MedicationStatement.reasonReference                      | Reference(AU Core Observation)                           | Not Included          |
| MedicationStatement.reasonReference                      | Reference(AU Base DiagnosticReport)                      | Not Included          |
| MedicationStatement.dosage                               |                                                          | Included              |
| MedicationStatement.dosage.text                          |                                                          | Included              |

## au-core-organization test data coverage
Profile: AU Core Organization | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-organization

|  Must Support element       | Type (where there is a choice of data type)                          | HL7 AU FHIR Test Data |
|:----------------------------|:---------------------------------------------------------------------|:----------------------|
| Organization.identifier     | Identifier                                                           | Included              |
| Organization.identifier     | AUHPIO                                                               | Included              |
| Organization.identifier     | AUAustralianBusinessNumber                                           | Included              |
| Organization.type           |                                                                      | Included              |
| Organization.name           |                                                                      | Included              |
| Organization.telecom        |                                                                      | Included              |
| Organization.telecom.system |                                                                      | Included              |
| Organization.telecom.value  |                                                                      | Included              |
| Organization.address        | Address                                                              | Included              |
| Organization.address        | AustralianAddress                                                    | Included              |

## au-core-patient test data coverage
Profile: AU Core Patient | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-patient

|  Must Support element                | Type (where there is a choice of data type)                     | HL7 AU FHIR Test Data |
|:-------------------------------------|:----------------------------------------------------------------|:----------------------|
| Patient.extension:indigenousStatus   |                                                                 | Included              |
| Patient.extension:genderIdentity     |                                                                 | Included              |
| Patient.extension:individualPronouns |                                                                 | Included              |
| Patient.identifier                   | Identifier                                                      | Included              |
| Patient.identifier                   | AUIHI                                                           | Included              |
| Patient.identifier                   | AUMedicareCardNumber                                            | Included              |
| Patient.identifier                   | AUDVANumber                                                     | Included              |
| Patient.name                         |                                                                 | Included              |
| Patient.name.use                     |                                                                 | Included              |
| Patient.name.text                    |                                                                 | Included              |
| Patient.name.family                  |                                                                 | Included              |
| Patient.name.given                   |                                                                 | Included              |
| Patient.telecom                      |                                                                 | Included              |
| Patient.telecom.system               |                                                                 | Included              |
| Patient.telecom.value                |                                                                 | Included              |
| Patient.telecom.use                  |                                                                 | Included              |
| Patient.gender                       |                                                                 | Included              |
| Patient.birthDate                    |                                                                 | Included              |
| Patient.address                      | AustralianAddress                                               | Included              |
| Patient.address                      | Address                                                         | Included              |
| Patient.communication                |                                                                 | Included              |
| Patient.communication.language       |                                                                 | Included              |
| Patient.communication.preferred      |                                                                 | Included              |

## au-core-practitioner test data coverage
Profile: AU Core Practitioner | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-practitioner

|  Must Support element    | Type (where there is a choice of data type)                          | HL7 AU FHIR Test Data |
|:-------------------------|:---------------------------------------------------------------------|:----------------------|
| Practitioner.identifier  | Identifier                                                           | Included              |
| Practitioner.identifier  | AUHPII                                                               | Included              |
| Practitioner.name        |                                                                      | Included              |
| Practitioner.name.family |                                                                      | Included              |
| Practitioner.name.given  |                                                                      | Included              |

## au-core-practitionerrole test data coverage
Profile: AU Core PractitionerRole | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-practitionerrole

|  Must Support element           | Type (where there is a choice of data type)                              | HL7 AU FHIR Test Data |
|:--------------------------------|:-------------------------------------------------------------------------|:----------------------|
| PractitionerRole.identifier     | Identifier                                                               | Included              |
| PractitionerRole.identifier     | AUMedicareProviderNumber                                                 | Included              |
| PractitionerRole.practitioner   |                                                                          | Included              |
| PractitionerRole.organization   |                                                                          | Included              |
| PractitionerRole.code           |                                                                          | Included              |
| PractitionerRole.specialty      |                                                                          | Included              |
| PractitionerRole.telecom        |                                                                          | Included              |
| PractitionerRole.telecom.system |                                                                          | Included              |
| PractitionerRole.telecom.value  |                                                                          | Included              |

## au-core-procedure test data coverage
Profile: AU Core Procedure | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-procedure

|  Must Support element       | Type (where there is a choice of data type)                       | HL7 AU FHIR Test Data |
|:----------------------------|:------------------------------------------------------------------|:----------------------|
| Procedure.status            |                                                                   | Included              |
| Procedure.code              |                                                                   | Included              |
| Procedure.subject           |                                                                   | Included              |
| Procedure.encounter         |                                                                   | Included              |
| Procedure.performedDateTime |                                                                   | Included              |
| Procedure.performedPeriod   |                                                                   | Included              |
| Procedure.performedString   |                                                                   | Included              |
| Procedure.performedAge      |                                                                   | Not Included          |
| Procedure.performedRange    |                                                                   | Not Included          |
| Procedure.reasonCode        |                                                                   | Included              |
| Procedure.reasonReference   | Reference(AU Core Condition)                                      | Included              |
| Procedure.reasonReference   | Reference(Observation)                                            | Not Included          |
| Procedure.reasonReference   | Reference(AU Core Procedure)                                      | Not Included          |
| Procedure.reasonReference   | Reference(DocumentReference)                                      | Not Included          |

## au-core-sexassignedatbirth test data coverage
Profile: AU Core Sex Assigned At Birth | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-rsg-sexassignedab

|  Must Support element     | HL7 AU FHIR Test Data                                                     |
|:--------------------------|:--------------------------------------------------------------------------|
| Extension.extension:value | Included                                                                  |
| Extension.extension:type  | Included                                                                  |

## au-core-bloodpressure test data coverage
Profile: AU Core Blood Pressure | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-bloodpressure

|  Must Support element                              | HL7 AU FHIR Test Data                                              |
|:---------------------------------------------------|:-------------------------------------------------------------------|
| Observation.status                                 | Included                                                           |
| Observation.category                               | Included                                                           |
| Observation.category:VSCat                         | Included                                                           |
| Observation.code                                   | Included                                                           |
| Observation.subject                                | Included                                                           |
| Observation.effectivedateTime                      | Included                                                           |
| Observation.dataAbsentReason                       | Included                                                           |
| Observation.component.code                         | Not Included                                                       |
| Observation.component.valueQuantity                | Not Included                                                       |
| Observation.component.valueCodeableConcept         | Not Included                                                       |
| Observation.component.valueString                  | Not Included                                                       |
| Observation.component.valueBoolean                 | Not Included                                                       |
| Observation.component.valueInteger                 | Not Included                                                       |
| Observation.component.valueRange                   | Not Included                                                       |
| Observation.component.valueRatio                   | Not Included                                                       |
| Observation.component.valueSampledData             | Not Included                                                       |
| Observation.component.valueTime                    | Not Included                                                       |
| Observation.component.valueDateTime                | Not Included                                                       |
| Observation.component.valuePeriod                  | Not Included                                                       |
| Observation.component.dataAbsentReason             | Included                                                           |
| Observation.component:SystolicBP.code              | Included                                                           |
| Observation.component:SystolicBP.value[x].value    | Included                                                           |
| Observation.component:SystolicBP.value[x].unit     | Included                                                           |
| Observation.component:SystolicBP.value[x].system   | Included                                                           |
| Observation.component:SystolicBP.value[x].code     | Included                                                           |
| Observation.component:SystolicBP.dataAbsentReason  | Included                                                           |
| Observation.component:DiastolicBP.code             | Included                                                           |
| Observation.component:DiastolicBP.value[x].value   | Included                                                           |
| Observation.component:DiastolicBP.value[x].unit    | Included                                                           |
| Observation.component:DiastolicBP.value[x].system  | Included                                                           |
| Observation.component:DiastolicBP.value[x].code    | Included                                                           |
| Observation.component:DiastolicBP.dataAbsentReason | Included                                                           |

## au-core-bodyheight test data coverage
Profile: AU Core Body Height | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-bodyheight

|  Must Support element                              | HL7 AU FHIR Test Data                                              |
|:---------------------------------------------------|:-------------------------------------------------------------------|
| Observation.status                                 | Included                                                           |
| Observation.category                               | Included                                                           |
| Observation.category:VSCat                         | Included                                                           |
| Observation.code                                   | Included                                                           |
| Observation.subject                                | Included                                                           |
| Observation.effectivedateTime                      | Included                                                           |
| Observation.value[x]:valueQuantity.value           | Included                                                           |
| Observation.value[x]:valueQuantity.unit            | Included                                                           |
| Observation.value[x]:valueQuantity.system          | Included                                                           |
| Observation.value[x]:valueQuantity.code            | Included                                                           |
| Observation.dataAbsentReason                       | Included                                                           |
| Observation.component.code                         | Included                                                           |
| Observation.component.valueQuantity                | Not Included                                                       |
| Observation.component.valueCodeableConcept         | Included                                                           |
| Observation.component.valueString                  | Not Included                                                       |
| Observation.component.valueBoolean                 | Not Included                                                       |
| Observation.component.valueInteger                 | Not Included                                                       |
| Observation.component.valueRange                   | Not Included                                                       |
| Observation.component.valueRatio                   | Not Included                                                       |
| Observation.component.valueSampledData             | Not Included                                                       |
| Observation.component.valueTime                    | Not Included                                                       |
| Observation.component.valueDateTime                | Not Included                                                       |
| Observation.component.valuePeriod                  | Not Included                                                       |
| Observation.component.dataAbsentReason             | Included                                                           |

## au-core-bodytemp test data coverage
Profile: AU Core Body Temperature | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-bodytemp

|  Must Support element                      | HL7 AU FHIR Test Data                                            |
|:-------------------------------------------|:-----------------------------------------------------------------|
| Observation.status                         | Included                                                         |
| Observation.category                       | Included                                                         |
| Observation.category:VSCat                 | Included                                                         |
| Observation.code                           | Included                                                         |
| Observation.subject                        | Included                                                         |
| Observation.effectivedateTime              | Included                                                         |
| Observation.value[x]:valueQuantity.value   | Included                                                         |
| Observation.value[x]:valueQuantity.unit    | Included                                                         |
| Observation.value[x]:valueQuantity.system  | Included                                                         |
| Observation.value[x]:valueQuantity.code    | Included                                                         |
| Observation.dataAbsentReason               | Included                                                         |
| Observation.component.code                 | Included                                                         |
| Observation.component.valueQuantity        | Not Included                                                     |
| Observation.component.valueCodeableConcept | Included                                                         |
| Observation.component.valueString          | Not Included                                                     |
| Observation.component.valueBoolean         | Not Included                                                     |
| Observation.component.valueInteger         | Not Included                                                     |
| Observation.component.valueRange           | Not Included                                                     |
| Observation.component.valueRatio           | Not Included                                                     |
| Observation.component.valueSampledData     | Not Included                                                     |
| Observation.component.valueTime            | Not Included                                                     |
| Observation.component.valueDateTime        | Not Included                                                     |
| Observation.component.valuePeriod          | Not Included                                                     |
| Observation.component.dataAbsentReason     | Included                                                         |

## au-core-bodyweight test data coverage
Profile: AU Core Body Weight | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-bodyweight

|  Must Support element                      | HL7 AU FHIR Test Data                                              |
|:-------------------------------------------|:-------------------------------------------------------------------|
| Observation.status                         | Included                                                           |
| Observation.category                       | Included                                                           |
| Observation.category:VSCat                 | Included                                                           |
| Observation.code                           | Included                                                           |
| Observation.subject                        | Included                                                           |
| Observation.effectivedateTime              | Included                                                           |
| Observation.value[x]:valueQuantity.value   | Included                                                           |
| Observation.value[x]:valueQuantity.unit    | Included                                                           |
| Observation.value[x]:valueQuantity.system  | Included                                                           |
| Observation.value[x]:valueQuantity.code    | Included                                                           |
| Observation.dataAbsentReason               | Included                                                           |
| Observation.component.code                 | Included                                                           |
| Observation.component.valueQuantity        | Not Included                                                       |
| Observation.component.valueCodeableConcept | Included                                                           |
| Observation.component.valueString          | Not Included                                                       |
| Observation.component.valueBoolean         | Not Included                                                       |
| Observation.component.valueInteger         | Not Included                                                       |
| Observation.component.valueRange           | Not Included                                                       |
| Observation.component.valueRatio           | Not Included                                                       |
| Observation.component.valueSampledData     | Not Included                                                       |
| Observation.component.valueTime            | Not Included                                                       |
| Observation.component.valueDateTime        | Not Included                                                       |
| Observation.component.valuePeriod          | Not Included                                                       |
| Observation.component.dataAbsentReason     | Included                                                           |

## au-core-diagnosticresult-path test data coverage
Profile: AU Core Pathology Result Observation | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-diagnosticresult-path

|  Must Support element                      | Type (where there is a choice of data type)                                 | HL7 AU FHIR Test Data |
|:-------------------------------------------|:----------------------------------------------------------------------------|:----------------------|
| Observation.status                         |                                                                             | Included              |
| Observation.category                       |                                                                             | Included              |
| Observation.code                           |                                                                             | Included              |
| Observation.subject                        |                                                                             | Included              |
| Observation.effectiveDateTime              |                                                                             | Included              |
| Observation.effectivePeriod                |                                                                             | Not Included          |
| Observation.performer                      | Reference(AU Core Practitioner)                                             | Not Included          |
| Observation.performer                      | Reference(AU Core PractitionerRole)                                         | Included              |
| Observation.performer                      | Reference(AU Core Organization)                                             | Included              |
| Observation.performer                      | Reference(AU Core Patient )                                                 | Not Included          |
| Observation.performer                      | Reference(AU Base Related Person)                                           | Not Included          |
| Observation.valueQuantity                  |                                                                             | Included              |
| Observation.valueCodeableConcept           |                                                                             | Included              |
| Observation.valueString                    |                                                                             | Not Included          |
| Observation.valueBoolean                   |                                                                             | Not Included          |
| Observation.valueInteger                   |                                                                             | Not Included          |
| Observation.valueRange                     |                                                                             | Not Included          |
| Observation.valueRatio                     |                                                                             | Not Included          |
| Observation.valueSampledData               |                                                                             | Not Included          |
| Observation.valueTime                      |                                                                             | Not Included          |
| Observation.valueDateTime                  |                                                                             | Not Included          |
| Observation.valuePeriod                    |                                                                             | Not Included          |
| Observation.dataAbsentReason               |                                                                             | Included              |
| Observation.interpretation                 |                                                                             | Included              |
| Observation.specimen                       |                                                                             | Included              |
| Observation.referenceRange.low             |                                                                             | Included              |
| Observation.referenceRange.high            |                                                                             | Included              |
| Observation.referenceRange.type            |                                                                             | Included              |
| Observation.referenceRange.text            |                                                                             | Included              |
| Observation.hasMember                      |                                                                             | Included              |
| Observation.component.code                 |                                                                             | Included              |
| Observation.component.valueQuantity        |                                                                             | Included              |
| Observation.component.valueCodeableConcept |                                                                             | Included              |
| Observation.component.valueString          |                                                                             | Not Included          |
| Observation.component.valueBoolean         |                                                                             | Not Included          |
| Observation.component.valueInteger         |                                                                             | Not Included          |
| Observation.component.valueRange           |                                                                             | Not Included          |
| Observation.component.valueRatio           |                                                                             | Not Included          |
| Observation.component.valueSampledData     |                                                                             | Not Included          |
| Observation.component.valueTime            |                                                                             | Not Included          |
| Observation.component.valueDateTime        |                                                                             | Not Included          |
| Observation.component.valuePeriod          |                                                                             | Not Included          |
| Observation.component.dataAbsentReason     |                                                                             | Included              |

## au-core-diagnosticresult test data coverage
Profile: AU Core Diagnostic Result Observation | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-diagnosticresult

|  Must Support element                      | Type (where there is a choice of data type)                            | HL7 AU FHIR Test Data |
|:-------------------------------------------|:-----------------------------------------------------------------------|:----------------------|
| Observation.status                         |                                                                        | Included              |
| Observation.category                       |                                                                        | Included              |
| Observation.code                           |                                                                        | Included              |
| Observation.subject                        |                                                                        | Included              |
| Observation.effectiveDateTime              |                                                                        | Included              |
| Observation.effectivePeriod                |                                                                        | Not Included          |
| Observation.effectiveTiming                |                                                                        | Not Included          |
| Observation.effectiveInstant               |                                                                        | Not Included          |
| Observation.performer                      | Reference(AU Core Practitioner)                                        | Not Included          |
| Observation.performer                      | Reference(AU Core PractitionerRole)                                    | Not Included          |
| Observation.performer                      | Reference(AU Core Organization)                                        | Included              |
| Observation.performer                      | Reference(AU Core Patient)                                             | Not Included          |
| Observation.performer                      | Reference(AU Base Related Person)                                      | Not Included          |
| Observation.valueQuantity                  |                                                                        | Included              |
| Observation.valueCodeableConcept           |                                                                        | Included              |
| Observation.valueString                    |                                                                        | Not Included          |
| Observation.valueBoolean                   |                                                                        | Not Included          |
| Observation.valueInteger                   |                                                                        | Not Included          |
| Observation.valueRange                     |                                                                        | Not Included          |
| Observation.valueRatio                     |                                                                        | Not Included          |
| Observation.valueSampledData               |                                                                        | Not Included          |
| Observation.valueTime                      |                                                                        | Not Included          |
| Observation.valueDateTime                  |                                                                        | Not Included          |
| Observation.valuePeriod                    |                                                                        | Not Included          |
| Observation.dataAbsentReason               |                                                                        | Included              |
| Observation.bodySite                       |                                                                        | Included              |
| Observation.hasMember                      |                                                                        | Included              |
| Observation.component.code                 |                                                                        | Included              |
| Observation.component.valueQuantity        |                                                                        | Not Included          |
| Observation.component.valueCodeableConcept |                                                                        | Included              |
| Observation.component.valueString          |                                                                        | Not Included          |
| Observation.component.valueBoolean         |                                                                        | Not Included          |
| Observation.component.valueInteger         |                                                                        | Not Included          |
| Observation.component.valueRange           |                                                                        | Not Included          |
| Observation.component.valueRatio           |                                                                        | Not Included          |
| Observation.component.valueSampledData     |                                                                        | Not Included          |
| Observation.component.valueTime            |                                                                        | Not Included          |
| Observation.component.valueDateTime        |                                                                        | Not Included          |
| Observation.component.valuePeriod          |                                                                        | Not Included          |
| Observation.component.dataAbsentReason     |                                                                        | Included              |

## au-core-heartrate test data coverage
Profile: AU Core Heart Rate | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-heartrate

|  Must Support element                      | HL7 AU FHIR Test Data                                             |
|:-------------------------------------------|:------------------------------------------------------------------|
| Observation.status                         | Included                                                          |
| Observation.category                       | Included                                                          |
| Observation.category:VSCat                 | Included                                                          |
| Observation.code                           | Included                                                          |
| Observation.subject                        | Included                                                          |
| Observation.effectiveDateTime              | Included                                                          |
| Observation.value[x]:valueQuantity.value   | Included                                                          |
| Observation.value[x]:valueQuantity.unit    | Included                                                          |
| Observation.value[x]:valueQuantity.system  | Included                                                          |
| Observation.value[x]:valueQuantity.code    | Included                                                          |
| Observation.dataAbsentReason               | Included                                                          |
| Observation.component.code                 | Included                                                          |
| Observation.component.valueQuantity        | Not Included                                                      |
| Observation.component.valueCodeableConcept | Included                                                          |
| Observation.component.valueString          | Not Included                                                      |
| Observation.component.valueBoolean         | Not Included                                                      |
| Observation.component.valueInteger         | Not Included                                                      |
| Observation.component.valueRange           | Not Included                                                      |
| Observation.component.valueRatio           | Not Included                                                      |
| Observation.component.valueSampledData     | Not Included                                                      |
| Observation.component.valueTime            | Not Included                                                      |
| Observation.component.valueDateTime        | Not Included                                                      |
| Observation.component.valuePeriod          | Not Included                                                      |
| Observation.component.dataAbsentReason     | Included                                                          |

## au-core-resprate test data coverage
Profile: AU Core Respiration Rate | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-resprate

|  Must Support element                      | HL7 AU FHIR Test Data                                            |
|:-------------------------------------------|:-----------------------------------------------------------------|
| Observation.status                         | Included                                                         |
| Observation.category                       | Included                                                         |
| Observation.category:VSCat                 | Included                                                         |
| Observation.code                           | Included                                                         |
| Observation.subject                        | Included                                                         |
| Observation.effectiveDateTime              | Included                                                         |
| Observation.value[x]:valueQuantity.value   | Included                                                         |
| Observation.value[x]:valueQuantity.unit    | Included                                                         |
| Observation.value[x]:valueQuantity.system  | Included                                                         |
| Observation.value[x]:valueQuantity.code    | Included                                                         |
| Observation.dataAbsentReason               | Included                                                         |
| Observation.component.code                 | Included                                                         |
| Observation.component.valueQuantity        | Not Included                                                     |
| Observation.component.valueCodeableConcept | Included                                                         |
| Observation.component.valueString          | Not Included                                                     |
| Observation.component.valueBoolean         | Not Included                                                     |
| Observation.component.valueInteger         | Not Included                                                     |
| Observation.component.valueRange           | Not Included                                                     |
| Observation.component.valueRatio           | Not Included                                                     |
| Observation.component.valueSampledData     | Not Included                                                     |
| Observation.component.valueTime            | Not Included                                                     |
| Observation.component.valueDateTime        | Not Included                                                     |
| Observation.component.valuePeriod          | Not Included                                                     |
| Observation.component.dataAbsentReason     | Included                                                         |

## au-core-smokingstatus test data coverage
Profile: AU Core Smoking Status | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-smokingstatus

|  Must Support element            | HL7 AU FHIR Test Data                                                 |
|:---------------------------------|:----------------------------------------------------------------------|
| Observation.status               | Included                                                              |
| Observation.category             | Included                                                              |
| Observation.code                 | Included                                                              |
| Observation.subject              | Included                                                              |
| Observation.effectiveDateTime    | Included                                                              |
| Observation.valueCodeableConcept | Included                                                              |
| Observation.dataAbsentReason     | Included                                                              |

## au-core-waistcircum test data coverage
Profile: AU Core Waist Circumference | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-waistcircum

|  Must Support element                      | HL7 AU FHIR Test Data                                               |
|:-------------------------------------------|:--------------------------------------------------------------------|
| Observation.status                         | Included                                                            |
| Observation.category                       | Included                                                            |
| Observation.category:VSCat                 | Included                                                            |
| Observation.code                           | Included                                                            |
| Observation.subject                        | Included                                                            |
| Observation.effectiveDateTime              | Included                                                            |
| Observation.valueQuantity                  | Included                                                            |
| Observation.valueCodeableConcept           | Not Included                                                        |
| Observation.valueString                    | Not Included                                                        |
| Observation.valueBoolean                   | Not Included                                                        |
| Observation.valueInteger                   | Not Included                                                        |
| Observation.valueRange                     | Not Included                                                        |
| Observation.valueRatio                     | Not Included                                                        |
| Observation.valueSampledData               | Not Included                                                        |
| Observation.valueTime                      | Not Included                                                        |
| Observation.valueDateTime                  | Not Included                                                        |
| Observation.valuePeriod                    | Not Included                                                        |
| Observation.value[x]:valueQuantity         | Not Included                                                        |
| Observation.dataAbsentReason               | Included                                                            |
| Observation.component.code                 | Included                                                            |
| Observation.component.valueQuantity        | Not Included                                                        |
| Observation.component.valueCodeableConcept | Included                                                            |
| Observation.component.valueString          | Not Included                                                        |
| Observation.component.valueBoolean         | Not Included                                                        |
| Observation.component.valueInteger         | Not Included                                                        |
| Observation.component.valueRange           | Not Included                                                        |
| Observation.component.valueRatio           | Not Included                                                        |
| Observation.component.valueSampledData     | Not Included                                                        |
| Observation.component.valueTime            | Not Included                                                        |
| Observation.component.valueDateTime        | Not Included                                                        |
| Observation.component.valuePeriod          | Not Included                                                        |
| Observation.component.dataAbsentReason     | Included                                                            |

## au-core-sab test data coverage
Profile: AU Core Sex Assigned at Birth | Profile URL: http://hl7.org.au/fhir/core/StructureDefinition/au-core-rsg-sexassignedab

|  Must Support element     | HL7 AU FHIR Test Data   |
|:--------------------------|:------------------------|
| Extension.extension:value | Included                |
| Extension.extension:type  | Included                |

## au-core-missing-suppressed test data coverage

|  Missing Data and Suppressed Data for Mandatory elements    | HL7 AU FHIR Test Data |
|:------------------------------------------------------------|:----------------------|
| Missing Data - non-coded elements                           | Included              |
| Missing Data - coded elements                               | Included              |
| Supressed Data - non-coded elements                         | Included              |
| Suppressed Data - coded elements                            | Included              |