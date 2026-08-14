# Alex’s Story Interactions

This page describes Alex's Story as a sequence of possible system interactions, one sequence diagram per point of care from [Alex Story Data Set.md](Alex%20Story%20Data%20Set.md). Each diagram's participants are system roles; the Test Data File links tie individual interactions back to the sample FHIR resources provided in the test data set.

Each sequence diagram is followed by an Interaction Summary table. Interaction numbers match the diagram's sequence numbers.

The diagram arrow shows data flow direction, not the interaction initiator. Initiator and Responder depend on interaction type:

| Interaction type | Initiator | Responder |
| --- | --- | --- |
| Submit, Book, Update, Write back, Send | arrow source | arrow target |
| Retrieve, Pre-populate, Search | arrow target | arrow source |

## 1. Pathology (Collection Centre)

```mermaid
sequenceDiagram
    autonumber
    participant PMS as GP PMS
    participant ReqSvr as eRequesting Server
    participant PatApp as Consumer App
    participant Lab as Lab System
    participant RptSvr as eReporting Server
    participant VT as Virtual Triage
    
    PMS->>ReqSvr: Submit eRequest (Cervical Screening Test)

    ReqSvr->>PatApp: Retrieve eRequest (Cervical Screening Test)
    ReqSvr->>Lab: Retrieve eRequest (Cervical Screening Test)
    Lab->>RptSvr: Submit Diagnostic Report (HPV pathology result)
    
```

### Interaction Summary – Pathology (Collection Centre)

| # | Interaction | Initiator | Responder | Test Data File |
| --- | --- | --- | --- | --- |
| 1 | Submit eRequest (Cervical Screening Test) | GP PMS | eRequesting Server | [ServiceRequest-cervicalscreening-thompson-alex-20250930.json](ServiceRequest-cervicalscreening-thompson-alex-20250930.json) |
| 2 | Retrieve eRequest (Cervical Screening Test) | Consumer App | eRequesting Server | [ServiceRequest-cervicalscreening-thompson-alex-20250930.json](ServiceRequest-cervicalscreening-thompson-alex-20250930.json) |
| 3 | Retrieve eRequest (Cervical Screening Test) | Lab System | eRequesting Server | [ServiceRequest-cervicalscreening-thompson-alex-20250930.json](ServiceRequest-cervicalscreening-thompson-alex-20250930.json) |
| 4 | Submit Diagnostic Report (HPV pathology result) | Lab System | eReporting Server | [DiagnosticReport-hpvpathology-thompson-alex-20251008.json](DiagnosticReport-hpvpathology-thompson-alex-20251008.json) |

## 2. General Practice

```mermaid
sequenceDiagram
    autonumber
    participant RptSvr as eReporting Server
    participant PMS as GP PMS
    participant PMH as Shared Medicines History
    participant CPApp as SMART GPCCMP App
    participant PD as Provider Directory
    participant RefApp as SMART eReferral App
    participant RefSvr as eReferral Server
    participant PatApp as Consumer App
    
    RptSvr->>PMS: Retrieve Diagnostic Report (HPV pathology result)
    PMH->>PMS: Retrieve Prescription and Dispensing History

    PMS->>CPApp: Pre-populate GP CCMP
    CPApp->>PMS: Submit GP CCMP

    alt native eReferral 
      PD->>PMS: Retrieve Provider Endpoint
      PMS->>RefSvr: Submit eReferral
    else SMART eReferral App
      PMS->>RefApp: Pre-populate eReferral
      RefApp->>RefSvr: Submit eReferral
      RefApp->>PMS: Write back eReferral 
    end

    RptSvr->>PatApp: Retrieve Diagnostic Report (HPV pathology result)
    PMS->>PatApp: Retrieve GP CCMP
    PMS->>PatApp: Retrieve Patient Summary
    PMS->>PatApp: Retrieve Encounter Record
    RefSvr->>PatApp: Retrieve eReferral

```

### Interaction Summary – General Practice

| # | Interaction | Initiator | Responder | Test Data File |
| --- | --- | --- | --- | --- |
| 1 | Retrieve Diagnostic Report (HPV pathology result) | GP PMS | eReporting Server | [DiagnosticReport-hpvpathology-thompson-alex-20251008.json](DiagnosticReport-hpvpathology-thompson-alex-20251008.json) |
| 2 | Retrieve Prescription and Dispensing History | GP PMS | Shared Medicines History | *TBD — dispense record for Sertraline?* |
| 3 | Pre-populate GP CCMP | SMART GPCCMP App | GP PMS | *Various* |
| 4 | Submit GP CCMP | SMART GPCCMP App | GP PMS | _TBD — QuestionnaireResponse ?_|
| 5 | Retrieve Provider Endpoint | GP PMS | Provider Directory | [PractitionerRole-obstetricianandgynaecologist-chen-emily.json](PractitionerRole-obstetricianandgynaecologist-chen-emily.json) |
| 6 | Submit eReferral | GP PMS | eReferral Server | [ServiceRequest-referral-gynaecologist-thompson-alex-20251009.json](ServiceRequest-referral-gynaecologist-thompson-alex-20251009.json) |
| 7 | Pre-populate eReferral | SMART eReferral App | GP PMS | *Various* |
| 8 | Submit eReferral | SMART eReferral App | eReferral Server | [ServiceRequest-referral-gynaecologist-thompson-alex-20251009.json](ServiceRequest-referral-gynaecologist-thompson-alex-20251009.json) |
| 9 | Write back eReferral | SMART eReferral App | GP PMS | [ServiceRequest-referral-gynaecologist-thompson-alex-20251009.json](ServiceRequest-referral-gynaecologist-thompson-alex-20251009.json) |
| 10 | Retrieve Diagnostic Report (HPV pathology result) | Consumer App | eReporting Server | [DiagnosticReport-hpvpathology-thompson-alex-20251008.json](DiagnosticReport-hpvpathology-thompson-alex-20251008.json) |
| 11 | Retrieve GP CCMP | Consumer App | GP PMS | _TBD — QuestionnaireResponse ?_|
| 12 | Retrieve Patient Summary | Consumer App | GP PMS | [Bundle-aups-thompson-alex-20251009.json](Bundle-aups-thompson-alex-20251009.json) |
| 13 | Retrieve Encounter Record | Consumer App | GP PMS | [Composition-episodeofcaresummary-thompson-alex-20251009.json](Composition-episodeofcaresummary-thompson-alex-20251009.json) |
| 14 | Retrieve eReferral | Consumer App | eReferral Server | [ServiceRequest-referral-gynaecologist-thompson-alex-20251009.json](ServiceRequest-referral-gynaecologist-thompson-alex-20251009.json) |

## 3. Specialist (Gynaecological Oncologist – Private Practice)

```mermaid
sequenceDiagram
    autonumber
    participant PMS as Specialist PMS
    participant PSApp as SMART PS App
    participant SEHR as Shared EHR/HIE
    participant SHLSS as SHL Sharing Server 

    participant RefSvr as eReferral Server
    participant ReqSvr as eRequesting Server
    participant RptSvr as eReporting Server

    participant PD as Provider Directory
    participant RefApp as SMART eReferral App
    participant EMR as Hospital EMR
    

    participant PMH as Shared Medicines History
    participant PatApp as Consumer App

    RefSvr->>PMS: Retrieve eReferral

    PMS->>PatApp: Retrieve New Patient Questionnaire Task
    PatApp->>PMS: Submit New Patient Questionnaire Response

    SEHR->>PMS: Retrieve Patient Summary (on-demand)

    PMS->>ReqSvr: Submit eRequest (cervical biopsy specimen)

    RptSvr->>PMS: Retrieve Diagnostic Report (Histopathology result)

    PMS->>PSApp: Pre-populate Patient Summary
    PSApp->>SHLSS: Submit Patient Summary

    alt native eReferral 
      PD->>PMS: Retrieve Provider Endpoint
      PMS->>RefSvr: Submit eReferral
      RefSvr->>EMR: Retrieve eReferral
    else SMART eReferral App 
      PMS->>RefApp: Pre-populate eReferral
      RefApp->>RefSvr: Submit eReferral
      RefApp->>EMR: Send eReferral (HL7 V2)
      RefApp->>PMS: Write back eReferral 
    end

    PMS->>EMR: Book Hospital Theatre Appointment

    SHLSS->>PatApp: Retrieve Patient Summary
    RefSvr->>PatApp: Retrieve eReferral
    PMH->>PatApp: Retrieve Prescription and Dispensing History
    
```

### Interaction Summary – Specialist (Gynaecological Oncologist – Private Practice)

| # | Interaction | Initiator | Responder | Test Data File |
| --- | --- | --- | --- | --- |
| 1 | Retrieve eReferral | Specialist PMS | eReferral Server | [ServiceRequest-referral-gynaecologist-thompson-alex-20251009.json](ServiceRequest-referral-gynaecologist-thompson-alex-20251009.json) |
| 2 | Retrieve New Patient Questionnaire Task | Consumer App | Specialist PMS | _TBD_ |
| 3 | Submit New Patient Questionnaire Response | Consumer App | Specialist PMS | _TBD_ |
| 4 | Retrieve Patient Summary (on-demand) | Specialist PMS | Shared EHR/HIE | [Bundle-aups-thompson-alex-20251009.json](Bundle-aups-thompson-alex-20251009.json) |
| 5 | Submit eRequest (cervical biopsy specimen) | Specialist PMS | eRequesting Server | [ServiceRequest-histopathology-thompson-alex-20251015.json](ServiceRequest-histopathology-thompson-alex-20251015.json) |
| 6 | Retrieve Diagnostic Report (Histopathology result) | Specialist PMS | eReporting Server | [DiagnosticReport-histopathology-thompson-alex-20251020.json](DiagnosticReport-histopathology-thompson-alex-20251020.json) |
| 7 | Pre-populate Patient Summary | SMART PS App | Specialist PMS | *Various* |
| 8 | Submit Patient Summary | SMART PS App | SHL Sharing Server | [Bundle-aups-specialist-thompson-alex-20251101.json](Bundle-aups-specialist-thompson-alex-20251101.json) |
| 9 | Retrieve Provider Endpoint | Specialist PMS | Provider Directory | [PractitionerRole-surgeon-wilson-mark.json](PractitionerRole-surgeon-wilson-mark.json) |
| 10 | Submit eReferral | Specialist PMS | eReferral Server | [ServiceRequest-conebiopsydaysurgery-thompson-alex-20251020.json](ServiceRequest-conebiopsydaysurgery-thompson-alex-20251020.json) |
| 11 | Retrieve eReferral | Hospital EMR | eReferral Server | [ServiceRequest-conebiopsydaysurgery-thompson-alex-20251020.json](ServiceRequest-conebiopsydaysurgery-thompson-alex-20251020.json) |
| 12 | Pre-populate eReferral | SMART eReferral App | Specialist PMS | *Various* |
| 13 | Submit eReferral | SMART eReferral App | eReferral Server | [ServiceRequest-conebiopsydaysurgery-thompson-alex-20251020.json](ServiceRequest-conebiopsydaysurgery-thompson-alex-20251020.json) |
| 14 | Send eReferral (HL7 V2) | SMART eReferral App | Hospital EMR | _TBD_|
| 15 | Write back eReferral  | SMART eReferral App | Specialist PMS | [ServiceRequest-conebiopsydaysurgery-thompson-alex-20251020.json](ServiceRequest-conebiopsydaysurgery-thompson-alex-20251020.json) |
| 16 | Book Hospital Theatre Appointment | Specialist PMS | Hospital EMR | [Appointment-hospitalbooking-thompson-alex-20251101.json](Appointment-hospitalbooking-thompson-alex-20251101.json) |
| 17 | Retrieve Patient Summary | Consumer App | SHL Sharing Server | [Bundle-aups-specialist-thompson-alex-20251101.json](Bundle-aups-specialist-thompson-alex-20251101.json) |
| 18 | Retrieve eReferral | Consumer App | eReferral Server | [ServiceRequest-conebiopsydaysurgery-thompson-alex-20251020.json](ServiceRequest-conebiopsydaysurgery-thompson-alex-20251020.json) |
| 19 | Retrieve Prescription and Dispensing History | Consumer App | Shared Medicines History | [MedicationRequest-ibuprofen-thompson-alex-20251015.json](MedicationRequest-ibuprofen-thompson-alex-20251015.json)<br/>[MedicationRequest-paracetamol-thompson-alex-20251015.json](MedicationRequest-paracetamol-thompson-alex-20251015.json) |

## 4. Private Hospital (Theatre / Inpatient)
```mermaid
sequenceDiagram
    autonumber
    participant EMR as Hospital EMR
    participant eCDS as Medicines eCDS
    participant SEHR as Shared EHR/HIE
    participant PMS as GP PMS
    participant AHPMS as Allied Health PMS
    participant PD as Provider Directory

    participant PatApp as Consumer App

    SEHR->>EMR: Retrieve Patient Summary
    EMR->>eCDS: Pre-populate Medicines eCDS

    EMR->>SEHR: Submit Discharge Summary

    PatApp->>PMS: Book GP Appointment
    PD->>PatApp: Search Allied Health Provider
    PatApp->>AHPMS: Book Allied Health Appointment
    SEHR->>PatApp: Retrieve Discharge Summary
```

### Interaction Summary – Private Hospital (Theatre / Inpatient)

| # | Interaction | Initiator | Responder | Test Data File |
| --- | --- | --- | --- | --- |
| 1 | Retrieve Patient Summary | Hospital EMR | Shared EHR/HIE | _TBD_|
| 2 | Pre-populate Medicines eCDS | Medicines eCDS | Hospital EMR | *Various* |
| 3 | Submit Discharge Summary | Hospital EMR | Shared EHR/HIE | [DocumentReference-dischargesummary-thompson-alex-20251101.json](DocumentReference-dischargesummary-thompson-alex-20251101.json) |
| 4 | Book GP Appointment | Consumer App | GP PMS | [Appointment-followupgp-thompson-alex-20251108.json](Appointment-followupgp-thompson-alex-20251108.json) |
| 5 | Search Allied Health Provider | Consumer App | Provider Directory | [PractitionerRole-physiotherapist-evans-sarah.json](PractitionerRole-physiotherapist-evans-sarah.json)<br/>[PractitionerRole-counsellorsnec-patel-rachel.json](PractitionerRole-counsellorsnec-patel-rachel.json) |
| 6 | Book Allied Health Appointment | Consumer App | Allied Health PMS | [Appointment-followupphysio-thompson-alex-20251110.json](Appointment-followupphysio-thompson-alex-20251110.json)<br/>[Appointment-followupcounselling-thompson-alex-20251115.json](Appointment-followupcounselling-thompson-alex-20251115.json) |
| 7 | Retrieve Discharge Summary | Consumer App | Shared EHR/HIE | [DocumentReference-dischargesummary-thompson-alex-20251101.json](DocumentReference-dischargesummary-thompson-alex-20251101.json) |

## 5. Pharmacy
```mermaid
sequenceDiagram
    autonumber
    participant PCMS as Pharmacy CMS
    participant PDMS as Pharmacy Dispense
    participant PMH as Shared Medicines History
    participant PD as Provider Directory
    participant SEHR as Shared EHR/HIE
    participant GPPMS as GP PMS
    participant PatApp as Consumer App

    SEHR->>PCMS: Retrieve Patient Summary

    PMH->>PCMS: Retrieve Prescription and Dispensing History

    PD->>PCMS: Retrieve GP Provider Details
    PCMS->>SEHR: Submit Pharmacy Encounter Record
    SEHR->>GPPMS: Retrieve Pharmacy Encounter Record
    SEHR->>PatApp: Retrieve Pharmacy Encounter Record

    PMH->>PDMS: Retrieve Prescription and Dispensing History

    PMH->>GPPMS: Retrieve Prescription and Dispensing History

    PDMS->>PatApp: Retrieve dispensed medicines
    PMH->>PatApp: Retrieve Prescription and Dispensing History
```

### Interaction Summary – Pharmacy

| # | Interaction | Initiator | Responder | Test Data File |
| --- | --- | --- | --- | --- |
| 1 | Retrieve Patient Summary | Pharmacy CMS | Shared EHR/HIE | _TBD_ |
| 2 | Retrieve Prescription and Dispensing History | Pharmacy CMS | Shared Medicines History | [MedicationRequest-ibuprofen-discharge-thompson-alex-20251101.json](MedicationRequest-ibuprofen-discharge-thompson-alex-20251101.json)<br/>[MedicationRequest-paracetamol-discharge-thompson-alex-20251101.json](MedicationRequest-paracetamol-discharge-thompson-alex-20251101.json) |
| 3 | Retrieve GP Provider Details | Pharmacy CMS | Provider Directory | [PractitionerRole-generalpractitioner-smith-jane.json](PractitionerRole-generalpractitioner-smith-jane.json) |
| 4 | Submit Pharmacy Encounter Record | Pharmacy CMS | Shared EHR/HIE | [Composition-medicationreview-thompson-alex-20251102.json](Composition-medicationreview-thompson-alex-20251102.json) |
| 5 | Retrieve Pharmacy Encounter Record | GP PMS | Shared EHR/HIE | [Composition-medicationreview-thompson-alex-20251102.json](Composition-medicationreview-thompson-alex-20251102.json) |
| 6 | Retrieve Pharmacy Encounter Record | Consumer App | Shared EHR/HIE | [Composition-medicationreview-thompson-alex-20251102.json](Composition-medicationreview-thompson-alex-20251102.json) |
| 7 | Retrieve Prescription and Dispensing History | Pharmacy Dispense | Shared Medicines History | [MedicationRequest-ibuprofen-discharge-thompson-alex-20251101.json](MedicationRequest-ibuprofen-discharge-thompson-alex-20251101.json)<br/>[MedicationRequest-paracetamol-discharge-thompson-alex-20251101.json](MedicationRequest-paracetamol-discharge-thompson-alex-20251101.json) |
| 8 | Retrieve Prescription and Dispensing History | GP PMS | Shared Medicines History | [MedicationStatement-sertraline-thompson-alex-20251102.json](MedicationStatement-sertraline-thompson-alex-20251102.json)<br/>[MedicationStatement-ibuprofen-postdischarge-thompson-alex-20251102.json](MedicationStatement-ibuprofen-postdischarge-thompson-alex-20251102.json)<br/>[MedicationStatement-paracetamol-postdischarge-thompson-alex-20251102.json](MedicationStatement-paracetamol-postdischarge-thompson-alex-20251102.json)<br/>[MedicationStatement-oxycodone-thompson-alex-20251102.json](MedicationStatement-oxycodone-thompson-alex-20251102.json) |
| 9 | Retrieve dispensed medicines | Consumer App | Pharmacy Dispense | [MedicationDispense-ibuprofen-thompson-alex-20251102.json](MedicationDispense-ibuprofen-thompson-alex-20251102.json)<br/>[MedicationDispense-oxycodone-thompson-alex-20251102.json](MedicationDispense-oxycodone-thompson-alex-20251102.json)<br/>[MedicationDispense-paracetamol-thompson-alex-20251102.json](MedicationDispense-paracetamol-thompson-alex-20251102.json) |
| 10 | Retrieve Prescription and Dispensing History | Consumer App | Shared Medicines History | [MedicationStatement-sertraline-thompson-alex-20251102.json](MedicationStatement-sertraline-thompson-alex-20251102.json)<br/>[MedicationStatement-ibuprofen-postdischarge-thompson-alex-20251102.json](MedicationStatement-ibuprofen-postdischarge-thompson-alex-20251102.json)<br/>[MedicationStatement-paracetamol-postdischarge-thompson-alex-20251102.json](MedicationStatement-paracetamol-postdischarge-thompson-alex-20251102.json)<br/>[MedicationStatement-oxycodone-thompson-alex-20251102.json](MedicationStatement-oxycodone-thompson-alex-20251102.json) |

## 6. Allied Health (Physiotherapy & Counselling)
```mermaid
sequenceDiagram
    autonumber
    participant PMS as Allied Health PMS
    participant RefSvr as eReferral Server
    participant EHRSvr as Shared EHR/HIE

    RefSvr->>PMS: Retrieve eReferral
    
    PMS->>EHRSvr: Update Shared Care Plan
```

### Interaction Summary – Allied Health (Physiotherapy & Counselling)

| # | Interaction | Initiator | Responder | Test Data File |
| --- | --- | --- | --- | --- |
| 1 | Retrieve eReferral | Allied Health PMS | eReferral Server | [ServiceRequest-referral-physio-thompson-alex-20251101.json](ServiceRequest-referral-physio-thompson-alex-20251101.json)<br/>[ServiceRequest-referral-counselling-thompson-alex-20251101.json](ServiceRequest-referral-counselling-thompson-alex-20251101.json) |
| 2 | Update Shared Care Plan | Allied Health PMS | Shared EHR/HIE | _TBD_ |

## 7. Population Health / Analytics
```mermaid
sequenceDiagram
    autonumber
    participant PMS as GP PMS
    participant AnlSvr as Analytics Server
    actor Analyst

    PMS->>AnlSvr: Retrieve PIP QI Bulk FHIR
    AnlSvr->>Analyst: Population Health Insights
```

### Interaction Summary – Population Health / Analytics

| # | Interaction | Initiator | Responder | Test Data File |
| --- | --- | --- | --- | --- |
| 1 | Retrieve PIP QI Bulk FHIR | Analytics Server | GP PMS | _TBD_ |
| 2 | Population Health Insights | Analytics Server | Analyst | _N/A_|
