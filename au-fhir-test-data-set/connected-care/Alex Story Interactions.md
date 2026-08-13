# Alex’s Story Interactions

## 1. Pathology (Collection Centre)

```mermaid
sequenceDiagram
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


## 2. General Practice

```mermaid
sequenceDiagram
    participant RptSvr as eReporting Server
    participant PMS as GP PMS
    participant PMH as PMH Service
    participant CPApp as SMART GPCCMP App
    participant RefApp as SMART eReferral App
    participant ReqSvr as eRequesting Server
    participant PatApp as Consumer App
    
    RptSvr->>PMS: Retrieve Diagnostic Report (HPV pathology result)
    PMH->>PMS: Retrieve Patient Medicines History

    PMS->>CPApp: Pre-populate GP CCMP
    CPApp->>PMS: Submit GP CCMP

    alt native eReferral 
      PMS->>ReqSvr: Submit eReferral
    else SMART eReferral App
      PMS->>RefApp: Pre-populate eReferral
      RefApp->>ReqSvr: Submit eReferral
      RefApp->>PMS: eReferral write back
    end

    RptSvr->>PatApp: Retrieve Diagnostic Report (HPV pathology result)
    PMS->>PatApp: Retrieve GP CCMP
    PMS->>PatApp: Retrieve Patient Summary
    PMS->>PatApp: Retrieve Encounter Record
    ReqSvr->>PatApp: Retrieve eReferral

```


## 3. Specialist (Gynaecological Oncologist – Private Practice)

```mermaid
sequenceDiagram
    participant PMS as Specialist PMS
    participant PSApp as SMART PS App
    participant SEHR as Shared EHR

    participant ReqSvr as eRequesting Server
    participant RptSvr as eReporting Server

    participant PD as Provider Directory
    participant RefApp as SMART eReferral App
    participant EMR as Hospital EMR
    

    participant PMH as PMH Service
    participant PatApp as Consumer App

    ReqSvr->>PMS: Retrieve eReferral

    PMS->>PatApp: Retrieve New Patient Form Task
    PatApp->>PMS: Submit New Patient Form 

    SEHR->>PMS: Retrieve Patient Summary (on-demand)

    PMS->>ReqSvr: Submit eRequest (cervical biopsy specimen)

    RptSvr->>PMS: Retrieve Diagnostic Report (Histopathology result)

    PMS->>PSApp: Pre-populate Patient Summary
    PSApp->>SEHR: Submit Patient Summary

    alt native eReferral 
      PD->>PMS: Retrieve Provider Endpoint
      PMS->>ReqSvr: Submit eReferral
      ReqSvr->>EMR: Retrieve eReferral
    else SMART eReferral App 
      PMS->>RefApp: Pre-populate eReferral
      RefApp->>ReqSvr: Submit eReferral
      RefApp->>EMR: eReferral Message (HL7 V2)
      RefApp->>PMS: eReferral write back
    end

    PMS->>EMR: Book Hospital Theatre Appointment

    SEHR->>PatApp: Retrieve Patient Summary
    ReqSvr->>PatApp: Retrieve eReferral
    PMH->>PatApp: Retrieve Patient Medicines History
    
```
## 4. Private Hospital (Theatre / Inpatient)
```mermaid
sequenceDiagram
    participant EMR as Hospital EMR
    participant eCDS as Medcines eCDS
    participant SEHR as Shared EHR
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

## 5. Pharmacy
```mermaid
sequenceDiagram

    participant PMS as Pharmacy CMS
    participant PMH as PMH Service
    participant PD as Provider Directory
    participant SEHR as Shared EHR
    participant GP as GP PMS
    participant PatApp as Consumer App

    SEHR->>PMS: Retrieve Patient Summary

    PMH->>PMS: Retrieve Patient Medicines History

    PD->>PMS: Retrieve GP Provider Details
    PMS->>SEHR: Submit Pharmacy Encounter Record
    SEHR->>GP: Retrieve Pharmacy Encounter Record

    SEHR->>PatApp: Retrieve Pharmacy Encounter Record
    PMH->>PatApp: Retrieve Patient Medicines History
```

## 6. Allied Health (Physiotherapy & Counselling)
```mermaid
sequenceDiagram

    participant PMS as Allied Health PMS
    participant RefSvr as Referral Server
    participant EHRSvr as Shared EHR

    RefSvr->>PMS: Retrieve eReferral
    
    PMS->>EHRSvr: Update Shared Care Plan
```

## 7. Population Health / Analytics
```mermaid
sequenceDiagram

    participant PMS as GP PMS
    participant AnlSvr as Analytics Server

    PMS->>AnlSvr: PIP QI Bulk FHIR
```
