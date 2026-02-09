## AU eReqeusting Test Data Coverage

Disclaimer: While we try to keep this page updated, we cannot guarantee its completeness or accuracy. The summary of test data coverage provided here is for reference only and should not be relied upon for critical purposes. Please use this information alongside your own analysis and judgement.

## au-erequesting-clinicalcontext-documentreference test data coverage
Profile: AU eRequesting Clinical Context DocumentReference | Profile URL: http://hl7.org.au/fhir/ereq/StructureDefinition/au-erequesting-clinicalcontext-documentreference

| Must Support element                             | HL7 AU FHIR Test Data            |
|:-------------------------------------------------|:---------------------------------|
| DocumentReference.status                         | Included                         |
| DocumentReference.type                           | Included                         |
| DocumentReference.subject                        | Included                         |
| DocumentReference.date                           | Included                         |
| DocumentReference.author                         | Included (1/6 types)             |
| DocumentReference.content                        | Included                         |
| DocumentReference.content.attachment             | Included                         |
| DocumentReference.content.attachment.contentType | Included                         |
| DocumentReference.content.attachment.data        | Included                         |

## au-erequesting-communicationrequest-copyto test data coverage
Profile: AU eRequesting CommunicationRequest CopyTo | Profile URL: http://hl7.org.au/fhir/ereq/StructureDefinition/au-erequesting-communicationrequest-copyto

| Must Support element                 | HL7 AU FHIR Test Data             |
|:-------------------------------------|:----------------------------------|
| CommunicationRequest.groupIdentifier | Included                          |
| CommunicationRequest.status          | Included                          |
| CommunicationRequest.category        | Included                          |
| CommunicationRequest.subject         | Included                          |
| CommunicationRequest.about           | Included (1/2 types)              |
| CommunicationRequest.authoredOn      | Included                          |
| CommunicationRequest.requester       | Included                          |
| CommunicationRequest.recipient       | Included (1/2 types)              |
| CommunicationRequest.sender          | Included                          |

## au-erequesting-communicationrequest-patient test data coverage
Profile: AU eRequesting CommunicationRequest Patient | Profile URL: http://hl7.org.au/fhir/ereq/StructureDefinition/au-erequesting-communicationrequest-patient

| Must Support element                 | HL7 AU FHIR Test Data             |
|:-------------------------------------|:----------------------------------|
| CommunicationRequest.groupIdentifier | Included                          |
| CommunicationRequest.status          | Included                          |
| CommunicationRequest.category        | Included                          |
| CommunicationRequest.doNotPerform    | Included                          |
| CommunicationRequest.medium          | Included                          |
| CommunicationRequest.subject         | Included                          |
| CommunicationRequest.about           | Included (1/2 types)              |
| CommunicationRequest.authoredOn      | Included                          |
| CommunicationRequest.requester       | Included (1/2 types)              |
| CommunicationRequest.recipient       | Included                          |
| CommunicationRequest.sender          | Included                          |

## au-erequesting-communicationrequest-urgentprovider test data coverage
Profile: AU eRequesting CommunicationRequest Urgent Provider | Profile URL: http://hl7.org.au/fhir/ereq/StructureDefinition/au-erequesting-communicationrequest-urgentprovider

| Must Support element                 | HL7 AU FHIR Test Data             |
|:-------------------------------------|:----------------------------------|
| CommunicationRequest.groupIdentifier | Included                          |
| CommunicationRequest.status          | Included                          |
| CommunicationRequest.category        | Included                          |
| CommunicationRequest.priority        | Included                          |
| CommunicationRequest.medium          | Included                          |
| CommunicationRequest.subject         | Included                          |
| CommunicationRequest.about           | Included (1/2 types)              |
| CommunicationRequest.authoredOn      | Included                          |
| CommunicationRequest.requester       | Included                          |
| CommunicationRequest.recipient       | Included                          |
| CommunicationRequest.sender          | Included                          |

## au-erequesting-coverage test data coverage
Profile: AU eRequesting Coverage | Profile URL: http://hl7.org.au/fhir/ereq/StructureDefinition/au-erequesting-coverage

| Must Support element  | HL7 AU FHIR Test Data             |
|:----------------------|:----------------------------------|
| Coverage.identifier   | Included (3/7 types)              |
| Coverage.status       | Included                          |
| Coverage.type         | Included                          |
| Coverage.beneficiary  | Included                          |
| Coverage.payor        | Included (1/3 types)              |

## au-erequesting-encounter test data coverage
Profile: AU eRequesting Encounter | Profile URL: http://hl7.org.au/fhir/ereq/StructureDefinition/au-erequesting-encounter

| Must Support element             | HL7 AU FHIR Test Data |
|:---------------------------------|-----------------------|
| Encounter.status                 | Included              |
| Encounter.class                  | Included              |
| Encounter.serviceType            | Included              |
| Encounter.subject                | Included              |
| Encounter.participant.type       | Included              |
| Encounter.participant.individual | Included (1/3 types)  |
| Encounter.period                 | Included              |
| Encounter.reasonCode             | Included              |
| Encounter.reasonReference        | Not Included          |
| Encounter.location.location      | Included              |
| Encounter.serviceProvider        | Included              |

## au-erequesting-servicerequest-imag test data coverage
Profile: AU eRequesting Imaging Request | Profile URL: http://hl7.org.au/fhir/ereq/StructureDefinition/au-erequesting-servicerequest-imag

| Must Support element                                | HL7 AU FHIR Test Data             |
|:----------------------------------------------------|:----------------------------------|
| ServiceRequest.extension:sexParameterForClinicalUse | Not Included                      |
| ServiceRequest.extension:statusReason               | Not Included                      |
| ServiceRequest.extension:displaySequence            | Included                          |
| ServiceRequest.extension:fastingPrecondition        | Not Included                      |
| ServiceRequest.identifier                           | Included (1/2 types)              |
| ServiceRequest.requisition                          | Included                          |
| ServiceRequest.status                               | Included                          |
| ServiceRequest.intent                               | Included                          |
| ServiceRequest.category                             | Included                          |
| ServiceRequest.category:imaging                     | Included                          |
| ServiceRequest.priority                             | Not Included                      |
| ServiceRequest.code                                 | Included                          |
| ServiceRequest.code.text                            | Included                          |
| ServiceRequest.subject                              | Included                          |
| ServiceRequest.encounter                            | Included                          |
| ServiceRequest.encounter.reference                  | Included                          |
| ServiceRequest.occurrenceDateTime                   | Not Included                      |
| ServiceRequest.occurrencePeriod                     | Included                          |
| ServiceRequest.occurrenceTiming                     | Not Included                      |
| ServiceRequest.authoredOn                           | Included                          |
| ServiceRequest.requester                            | Included                          |
| ServiceRequest.reasonCode                           | Not Included                      |
| ServiceRequest.insurance                            | Included                          |
| ServiceRequest.supportingInfo:pregnancyStatus       | Included                          |
| ServiceRequest.supportingInfo:clinicalContext       | Not Included                      |
| ServiceRequest.bodySite                             | Included                          |
| ServiceRequest.note                                 | Included                          |

## au-erequesting-mhrconsentwithdrawal test data coverage
Profile: AU eRequesting MHR Consent Withdrawal | Profile URL: http://hl7.org.au/fhir/ereq/StructureDefinition/au-erequesting-mhrconsentwithdrawal

| Must Support element                     | HL7 AU FHIR Test Data             |
|:-----------------------------------------|:----------------------------------|
| Consent.status                           | Included                          |
| Consent.scope                            | Included                          |
| Consent.category                         | Included                          |
| Consent.patient                          | Included                          |
| Consent.dateTime                         | Included                          |
| Consent.performer                        | Included                          |
| Consent.organization                     | Included                          |
| Consent.policy                           | Included                          |
| Consent.policy.authority                 | Included                          |
| Consent.policy.uri                       | Included                          |
| Consent.policyRule                       | Included                          |
| Consent.provision                        | Included                          |
| Consent.provision.type                   | Included                          |
| Consent.provision.action                 | Included                          |
| Consent.provision.class                  | Included                          |
| Consent.provision.class:diagnosticReport | Included                          |
| Consent.provision.data                   | Included                          |
| Consent.provision.data.meaning           | Included                          |
| Consent.provision.data.reference         | Included (1/2 types)              |

## au-erequesting-organization test data coverage
Profile: AU eRequesting Organization | Profile URL: http://hl7.org.au/fhir/ereq/StructureDefinition/au-erequesting-organization

| Must Support element         | HL7 AU FHIR Test Data |
|:-----------------------------|:----------------------|
| Organization.identifier      | Included              |
| Organization.identifier:hpio | Included              |
| Organization.identifier:abn  | Included              |
| Organization.type            | Included              |
| Organization.name            | Included              |
| Organization.telecom         | Included              |
| Organization.telecom.system  | Included              |
| Organization.telecom.value   | Included              |
| Organization.address         | Included (2/2 types)  |

## au-erequesting-servicerequest-path test data coverage
Profile: AU eRequesting Pathology Request | Profile URL: http://hl7.org.au/fhir/ereq/StructureDefinition/au-erequesting-servicerequest-path

| Must Support element                                | HL7 AU FHIR Test Data             |
|:----------------------------------------------------|:----------------------------------|
| ServiceRequest.extension:sexParameterForClinicalUse | Included                          |
| ServiceRequest.extension:statusReason               | Included                          |
| ServiceRequest.extension:displaySequence            | Included                          |
| ServiceRequest.extension:fastingPrecondition        | Included                          |
| ServiceRequest.identifier                           | Included (1/2 types)              |
| ServiceRequest.requisition                          | Included                          |
| ServiceRequest.status                               | Included                          |
| ServiceRequest.intent                               | Included                          |
| ServiceRequest.category                             | Included                          |
| ServiceRequest.category:path                        | Included                          |
| ServiceRequest.priority                             | Included                          |
| ServiceRequest.code                                 | Included                          |
| ServiceRequest.code.text                            | Included                          |
| ServiceRequest.subject                              | Included                          |
| ServiceRequest.encounter                            | Included                          |
| ServiceRequest.encounter.reference                  | Included                          |
| ServiceRequest.occurrenceDateTime                   | Included                          |
| ServiceRequest.occurrencePeriod                     | Not Included                      |
| ServiceRequest.occurrenceTiming                     | Not Included                      |
| ServiceRequest.authoredOn                           | Included                          |
| ServiceRequest.requester                            | Included                          |
| ServiceRequest.reasonCode                           | Included                          |
| ServiceRequest.insurance                            | Included                          |
| ServiceRequest.supportingInfo:pregnancyStatus       | Included                          |
| ServiceRequest.supportingInfo:clinicalContext       | Included                          |
| ServiceRequest.note                                 | Included                          |

## au-erequesting-patient test data coverage
Profile: AU eRequesting Patient | Profile URL: http://hl7.org.au/fhir/ereq/StructureDefinition/au-erequesting-patient

|  Must Support element                | HL7 AU FHIR Test Data |
|:-------------------------------------|:----------------------|
| Patient.extension:indigenousStatus   | Included              |
| Patient.extension:genderIdentity     | Included              |
| Patient.extension:individualPronouns | Included              |
| Patient.identifier                   | Included              |
| Patient.identifier:ihi               | Included              |
| Patient.identifier:medicare          | Included              |
| Patient.identifier:dva               | Included              |
| Patient.name                         | Included              |
| Patient.name.use                     | Included              |
| Patient.name.text                    | Not Included          |
| Patient.name.family                  | Included              |
| Patient.name.given                   | Included              |
| Patient.telecom                      | Included              |
| Patient.telecom.system               | Included              |
| Patient.telecom.value                | Included              |
| Patient.telecom.use                  | Included              |
| Patient.gender                       | Included              |
| Patient.birthDate                    | Included              |
| Patient.address                      | Included (2/2 types)  |
| Patient.communication                | Not Included          |
| Patient.communication.language       | Not Included          |
| Patient.communication.preferred      | Not Included          |

## au-erequesting-practitioner test data coverage
Profile: AU eRequesting Practitioner | Profile URL: http://hl7.org.au/fhir/ereq/StructureDefinition/au-erequesting-practitioner

|  Must Support element        | HL7 AU FHIR Test Data |
|:-----------------------------|:----------------------|
| Practitioner.identifier      | Included              |
| Practitioner.identifier:hpii | Included              |
| Practitioner.name            | Included              |
| Practitioner.name.family     | Included              |
| Practitioner.name.given      | Included              |

## au-erequesting-practitionerrole test data coverage
Profile: AU eRequesting PractitionerRole | Profile URL: http://hl7.org.au/fhir/ereq/StructureDefinition/au-erequesting-practitionerrole

|  Must Support element                       | HL7 AU FHIR Test Data |
|:--------------------------------------------|:----------------------|
| PractitionerRole.identifier                 | Included              |
| PractitionerRole.identifier:medicareProvier | Included              |
| PractitionerRole.practitioner               | Included              |
| PractitionerRole.organization               | Included              |
| PractitionerRole.code                       | Included              |
| PractitionerRole.specialty                  | Included              |
| PractitionerRole.telecom                    | Included              |
| PractitionerRole.telecom.system             | Included              |
| PractitionerRole.telecom.value              | Included              |

## au-erequesting-task-communicationrequest test data coverage
Profile: AU eRequesting Task Communication Request | Profile URL: http://hl7.org.au/fhir/ereq/StructureDefinition/au-erequesting-task-communicationrequest
| Must Support element                    | HL7 AU FHIR Test Data             |
|:----------------------------------------|:----------------------------------|
| Task.meta                               | Included                          |
| Task.meta.tag:eRequestingFulfilmentTask | Included                          |
| Task.identifier                         | Not Included                      |
| Task.groupIdentifier                    | Included                          |
| Task.partOf                             | Included                          |
| Task.status                             | Included                          |
| Task.statusReason                       | Not Included                      |
| Task.businessStatus                     | Not Included                      |
| Task.intent                             | Included                          |
| Task.priority                           | Included                          |
| Task.code                               | Included                          |
| Task.focus                              | Included (3/3 types)              |
| Task.for                                | Included                          |
| Task.authoredOn                         | Included                          |
| Task.lastModified                       | Included                          |
| Task.requester                          | Included                          |
| Task.owner                              | Included                          |

## au-erequesting-task-diagnosticrequest test data coverage
Profile: AU eRequesting Task Diagnostic Request | Profile URL: http://hl7.org.au/fhir/ereq/StructureDefinition/au-erequesting-task-diagnosticrequest
| Must Support element                    | HL7 AU FHIR Test Data             |
|:----------------------------------------|:----------------------------------|
| Task.meta                               | Included                          |
| Task.meta.tag:eRequestingFulfilmentTask | Included                          |
| Task.identifier                         | Not Included                      |
| Task.groupIdentifier                    | Included                          |
| Task.partOf                             | Included                          |
| Task.status                             | Included                          |
| Task.statusReason                       | Included                          |
| Task.businessStatus                     | Included                          |
| Task.intent                             | Included                          |
| Task.priority                           | Included                          |
| Task.code                               | Included                          |
| Task.focus                              | Included (2/2 types)              |
| Task.for                                | Included                          |
| Task.authoredOn                         | Included                          |
| Task.lastModified                       | Included                          |
| Task.requester                          | Included                          |
| Task.owner                              | Included                          |

## au-erequesting-task-group test data coverage
Profile: AU eRequesting Task Group Request | Profile URL: http://hl7.org.au/fhir/ereq/StructureDefinition/au-erequesting-task-group
| Must Support element                    | HL7 AU FHIR Test Data             |
|:----------------------------------------|:----------------------------------|
| Task.meta                               | Included                          |
| Task.meta.tag:eRequestingFulfilmentTask | Included                          |
| Task.identifier                         | Not Included                      |
| Task.groupIdentifier                    | Included                          |
| Task.partOf                             | Included                          |
| Task.status                             | Included                          |
| Task.statusReason                       | Not Included                      |
| Task.businessStatus                     | Included                          |
| Task.intent                             | Included                          |
| Task.priority                           | Included                          |
| Task.code                               | Included                          |
| Task.for                                | Included                          |
| Task.authoredOn                         | Included                          |
| Task.lastModified                       | Included                          |
| Task.requester                          | Included                          |
| Task.owner                              | Included                          |
