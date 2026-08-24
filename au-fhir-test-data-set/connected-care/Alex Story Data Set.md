# Data Set for Alex’s Story

Alex Thompson is a Bathurst, NSW resident whose story traces a connected-care journey from a routine screening reminder through to population-level reporting. It starts with a cervical screening overdue notification in Alex's MyHealth App, which leads to a pathology collection and a high-risk HPV result. The GP reviews the result and refers Alex to a gynaecological specialist, who performs a colposcopy with biopsy and, once histopathology confirms CIN2/3, arranges a cone biopsy day surgery at a private hospital. Discharge triggers a pharmacy medication update and allied health follow-up (physiotherapy and counselling), and the de-identified journey ultimately feeds into population health analytics on the cervical cancer care pathway.

The data set is organised into 8 steps, each representing a different point of care and the FHIR resources generated for it:

0. [MyHealth App](#0-myhealth-app)
1. [Pathology (Collection Centre)](#1-pathology-collection-centre)
2. [General Practice](#2-general-practice)
3. [Specialist (Gynaecological Oncologist – Private Practice)](#3-specialist-gynaecological-oncologist--private-practice)
4. [Private Hospital (Theatre / Inpatient)](#4-private-hospital-theatre--inpatient)
5. [Pharmacy](#5-pharmacy)
6. [Allied Health (Physiotherapy & Counselling)](#6-allied-health-physiotherapy--counselling)
7. [Population Health / Analytics](#7-population-health--analytics)

See [Pending / Placeholder Data](#pending--placeholder-data) for known gaps and modelling notes, and the [Change Log](#change-log) for deviations from the original story data.

## 0. MyHealth App

| Data Field | Actual Data | Critical? |
| --- | --- | --- |
| Patient Name | Alex Thompson | *Yes |
| Date of Birth | 15/05/1993 | *Yes |
| IHI | 8003608500344031 | *Yes |
| MEDICARE NO | 29548194011 | *Yes |
| Address (Patient) | 42 Macquarie St, Bathurst, NSW 2795 | No |
| Phone Number | 0412-345-678 | No |
| Email | [alex.thompson@cafe.com](mailto:alex.thompson@cafe.com) | No |
| Notification Source | National Cancer Screening Register (HPI-O: TBD) | *Yes |
| Notification Details | Reminder: Cervical Screening overdue; Issued: 2025-09-30, 08:00 AM; Via: MyHealth App | *Yes |
| e-Request ID | REQ-2025-10-001 | *Yes |
| e-Request Details | Request Type: Cervical Screening (National Cervical Screening Program); Issued by: Dr. Chris Lee (HPI-I: 8003616566728310); Date: 2025-09-30 | *Yes |
| Provider Directory Search | National Health Services Directory (powered by Provider Directory Service); Filters: Location (Bathurst, NSW), Service Type (Pathology), Availability (<1 week); Selected: Bathurst Pathology (HPI-O: 8003629900046190) | *Yes |
| Booking ID | BOOK-2025-10-000 | *Yes |
| Booking Details | Pathology Centre: Bathurst Pathology, 10 George St, Bathurst, NSW 2795; Date: 2025-10-01, 9:00 AM; Prep: Self-collect swab, bring QR code | *Yes |
| MyHealth App View | Displays: eRequest, Booking Confirmation, Prep Notes (“Bring QR code, no appointment needed for self-collect”); Consent: View shared with GP | *Yes |
| Provider Organisation | National Cancer Screening Register (HPI-O: TBD) | *Yes |
| Organisation Address | 1 Oxford St, Canberra, ACT 2601 | No |
| Clinician | Ms. Sarah Taylor (System Administrator, HPI-I: TBD) | *Yes |
| QR CODE VIEW | Displays consumer perspective: eRequest retrieval, sample processing, results notification | *Yes |

### FHIR Resources – MyHealth App

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Patient | Alex Thompson | ✅ Generated | [Patient-thompson-alex.json](Patient-thompson-alex.json) |
| Organization | National Cancer Screening Register | ⏳ Not yet generated | — |
| *Unresolved* | Reminder: Cervical Screening overdue — no AU Core resource identified for this | ⏳ Not yet generated | — |
| ServiceRequest | Cervical Screening e-Request (REQ-2025-10-001) | ✅ Generated | [ServiceRequest-cervicalscreening-thompson-alex-20250930.json](ServiceRequest-cervicalscreening-thompson-alex-20250930.json) |
| Task (eRequesting fulfilment) | Fulfilment task for the Cervical Screening e-Request (REQ-2025-10-001), owned by Bathurst Pathology | ✅ Generated | [Task-taskfulfilment-cervicalscreening-thompson-alex-20250930.json](Task-taskfulfilment-cervicalscreening-thompson-alex-20250930.json) |
| Organization | Bathurst Pathology | ✅ Generated | [Organization-bathurst-pathology.json](Organization-bathurst-pathology.json) |
| Location | Bathurst Pathology | ✅ Generated | [Location-bathurst-pathology.json](Location-bathurst-pathology.json) |
| HealthcareService | Bathurst Pathology – Pathology laboratory service | ✅ Generated | [HealthcareService-pathologylaboratory-bathurst-pathology.json](HealthcareService-pathologylaboratory-bathurst-pathology.json) |
| Appointment | Bathurst Pathology booking (BOOK-2025-10-000) | ⏳ Not yet generated | — |
| Practitioner | Dr. Chris Lee | ✅ Generated | [Practitioner-lee-chris.json](Practitioner-lee-chris.json) |
| PractitionerRole | Dr. Chris Lee – GP, Bathurst Medical Centre | ✅ Generated | [PractitionerRole-generalpractitioner-lee-chris.json](PractitionerRole-generalpractitioner-lee-chris.json) |
| Practitioner | Sarah Taylor | ⏳ Not yet generated | — |
| PractitionerRole | Sarah Taylor – System Administrator, National Cancer Screening Register | ⏳ Not yet generated | — |

## 1. Pathology (Collection Centre)

| Data Field | Actual Data | Critical? |
| --- | --- | --- |
| Patient Name | Alex Thompson | *Yes |
| Date of Birth | 15/05/1993 | *Yes |
| IHI | 8003608500344031 | *Yes |
| MEDICARE NO | 29548194011 | *Yes |
| Address (Patient) | 42 Macquarie St, Bathurst, NSW 2795 | No |
| Phone Number | 0412-345-678 | No |
| Email | [alex.thompson@cafe.com](mailto:alex.thompson@cafe.com) | No |
| e-Request ID | REQ-2025-10-001 | *Yes |
| Request Type | Cervical Screening (National Cervical Screening Program) | *Yes |
| Booking Details | Pathology Centre: Bathurst Pathology, 10 George St, Bathurst, NSW 2795; 2025-10-01, 9:00 AM; Booked via MyHealth App | *Yes |
| QR Code Data | eRequest ID: REQ-2025-10-001; IHI: 8003608500344031; Provider: Bathurst Pathology (HPI-O: 8003629900046190) | *Yes |
| Pathology Result ID | PATH-2025-10-002 | *Yes |
| Result Date | 2025-10-08 | *Yes |
| Result Details | High-risk HPV detected; CIN2/3 (pre-cancerous); Status: Urgent | *Yes |
| Notification Recipients | Patient (MyHealth App), GP (Dr. Chris Lee, HPI-I: 8003616566728310); Trigger: Immediate alert | *Yes |
| DISCOVERY SERVICE ACCESS | Pathologist views gynaecological/sexual health history via Discovery Service | *Yes |
| COHORT ANALYSIS | Augmented by data from National Screening Register for accurate reference range |  |
| REGISTER UPDATE | System automatically updates National Cervical Screening Register |  |
| Follow-Up Timer | Set: Confirm acceptance by GP within 48 hours | *Yes |
| Provider Organisation | Bathurst Pathology (HPI-O: 8003629900046190) | *Yes |
| Organisation Address | 10 George St, Bathurst, NSW 2795 | No |
| Clinician | Ms. Sally Johnson (Phlebotomist, HPI-I: 8003616566728328) | *Yes |

### FHIR Resources – Pathology (Collection Centre)

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Patient | Alex Thompson | ✅ Generated | [Patient-thompson-alex.json](Patient-thompson-alex.json) |
| ServiceRequest | Cervical Screening e-Request (REQ-2025-10-001) | ✅ Generated | [ServiceRequest-cervicalscreening-thompson-alex-20250930.json](ServiceRequest-cervicalscreening-thompson-alex-20250930.json) |
| Task (eRequesting fulfilment) | Fulfilment task for the Cervical Screening e-Request (REQ-2025-10-001), owned by Bathurst Pathology | ✅ Generated | [Task-taskfulfilment-cervicalscreening-thompson-alex-20250930.json](Task-taskfulfilment-cervicalscreening-thompson-alex-20250930.json) |
| DiagnosticReport | HPV pathology result (PATH-2025-10-002), high-risk HPV / CIN2/3 | ✅ Generated | [DiagnosticReport-hpvpathology-thompson-alex-20251008.json](DiagnosticReport-hpvpathology-thompson-alex-20251008.json) |
| Organization | Bathurst Pathology | ✅ Generated | [Organization-bathurst-pathology.json](Organization-bathurst-pathology.json) |
| Location | Bathurst Pathology | ✅ Generated | [Location-bathurst-pathology.json](Location-bathurst-pathology.json) |
| HealthcareService | Bathurst Pathology – Pathology laboratory service | ✅ Generated | [HealthcareService-pathologylaboratory-bathurst-pathology.json](HealthcareService-pathologylaboratory-bathurst-pathology.json) |
| Practitioner | Sally Johnson | ✅ Generated | [Practitioner-johnson-sally.json](Practitioner-johnson-sally.json) |
| PractitionerRole | Sally Johnson – Phlebotomist, Bathurst Pathology | ✅ Generated | [PractitionerRole-medicaltechnician-johnson-sally.json](PractitionerRole-medicaltechnician-johnson-sally.json) |

## 2. General Practice

| Data Field | Actual Data | Critical? |
| --- | --- | --- |
| Patient Name | Alex Thompson | *Yes |
| Date of Birth | 15/05/1993 | *Yes |
| IHI | 8003608500344031 | *Yes |
| MEDICARE NO | 29548194011 | *Yes |
| Address (Patient) | 42 Macquarie St, Bathurst, NSW 2795 | No |
| AUPS Key Allergies | Penicillin (anaphylaxis) | *Yes |
| AUPS Current Medications | None active | *Yes |
| AUPS Recent Conditions | High-risk cervical screening (2025-10-08) | *Yes |
| Consultation Date | 2025-10-09 | *Yes |
| Vitals Captured | Weight: 65 kg; BP: 120/80 mmHg; HR: 78 bpm; Alcohol use: Occasional (2 standard drinks/week) | No |
| Pathology Result ID | PATH-2025-10-002 (High-risk HPV, CIN2/3) | *Yes |
| Shared Care Plan ID | SCP-2025-10-003 | *Yes |
| Care Plan Details | Goals: Coordinate gynaecology referral, monitor results; Team: GP, Specialist; Prepopulated from national guidelines template | *Yes |
| e-Referral ID | REF-2025-10-004 | *Yes |
| Referral Details | To: Gynaecologist (no named provider); Include: Screening result, AUPS; Issued: 2025-10-09 | *Yes |
| Provider Directory Search | Filters: Bathurst/Sydney, Wait Time <2 weeks; Selected: Dr. Emily Chen, Ashfield Private Clinic (HPI-I: 8003616566728344) | *Yes |
| Subscription Preferences | GP (Dr. Jane Smith, HPI-I: 8003618233394732): Critical updates only (results, bookings) | *Yes |
| Provider Organisation | Bathurst Medical Centre (HPI-O: 8003629900046240) | *Yes |
| Organisation Address | 25 Russell St, Bathurst, NSW 2795 | No |
| Clinician | Dr. Chris Lee (GP, HPI-I: 8003616566728310) | *Yes |

### FHIR Resources – General Practice

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Patient | Alex Thompson | ✅ Generated | [Patient-thompson-alex.json](Patient-thompson-alex.json) |
| AllergyIntolerance | Penicillin (anaphylaxis) — pre-existing, unrelated to this encounter | ✅ Generated | [AllergyIntolerance-penicillin-thompson-alex.json](AllergyIntolerance-penicillin-thompson-alex.json) |
| MedicationStatement | No active medications — pre-existing, unrelated to this encounter | ✅ Generated | [MedicationStatement-nomedications-thompson-alex.json](MedicationStatement-nomedications-thompson-alex.json) |
| Condition | High-risk cervical screening (high-risk HPV / CIN2/3) | ✅ Generated | [Condition-highriskhpv-thompson-alex.json](Condition-highriskhpv-thompson-alex.json) |
| Encounter | GP consultation, 2025-10-09 | ✅ Generated | [Encounter-gpconsultation-thompson-alex-20251009.json](Encounter-gpconsultation-thompson-alex-20251009.json) |
| Composition (Episode of Care Summary) | GP consultation summary, 2025-10-09 — base AU Core `Composition`, LOINC 34133-9 "Summary of episode note"; references the Encounter with Problems / Vital Signs / Results / Plan of Care sections. Standalone resource, not wrapped in a document Bundle; references other resources by `ResourceType/id`. | ✅ Generated | [Composition-episodeofcaresummary-thompson-alex-20251009.json](Composition-episodeofcaresummary-thompson-alex-20251009.json) |
| Observation | Weight | ✅ Generated | [Observation-bodyweight-thompson-alex-20251009.json](Observation-bodyweight-thompson-alex-20251009.json) |
| Observation | Blood pressure (systolic/diastolic) | ✅ Generated | [Observation-bloodpressure-thompson-alex-20251009.json](Observation-bloodpressure-thompson-alex-20251009.json) |
| Observation | Heart rate | ✅ Generated | [Observation-heartrate-thompson-alex-20251009.json](Observation-heartrate-thompson-alex-20251009.json) |
| CarePlan | Shared Care Plan (SCP-2025-10-003) | ⏳ Not yet generated | — |
| QuestionnaireResponse | GP Chronic Condition Management Plan (GP CCMP), per the [AEHRC GP CCMP FHIR IG](https://build.fhir.org/ig/aehrc/gpccmp-fhir-ig/branches/master/StructureDefinition-GPCCMPQuestionnaireResponse.html) — supports the Shared Care Plan | ⏳ Not yet generated | — |
| ServiceRequest | e-Referral to Gynaecologist (REF-2025-10-004) | ✅ Generated | [ServiceRequest-referral-gynaecologist-thompson-alex-20251009.json](ServiceRequest-referral-gynaecologist-thompson-alex-20251009.json) |
| Bundle (AU Patient Summary) | Self-contained AU PS document — what the GP knows as of the 2025-10-09 consultation (Problems, Allergies, Medications, Results, Vital Signs), sent with the e-Referral to Dr. Emily Chen | ✅ Generated | [Bundle-aups-thompson-alex-20251009.json](Bundle-aups-thompson-alex-20251009.json) |
| Organization | Bathurst Medical Centre | ✅ Generated | [Organization-bathurst-medical-centre.json](Organization-bathurst-medical-centre.json) |
| Location | Bathurst Medical Centre | ✅ Generated | [Location-bathurst-medical-centre.json](Location-bathurst-medical-centre.json) |
| HealthcareService | Bathurst Medical Centre – General medical practitioner service | ✅ Generated | [HealthcareService-generalmedical-bathurst-medical-centre.json](HealthcareService-generalmedical-bathurst-medical-centre.json) |
| Practitioner | Dr. Chris Lee | ✅ Generated | [Practitioner-lee-chris.json](Practitioner-lee-chris.json) |
| PractitionerRole | Dr. Chris Lee – GP, Bathurst Medical Centre | ✅ Generated | [PractitionerRole-generalpractitioner-lee-chris.json](PractitionerRole-generalpractitioner-lee-chris.json) |
| Practitioner | Dr. Jane Smith | ✅ Generated | [Practitioner-smith-jane.json](Practitioner-smith-jane.json) |
| PractitionerRole | Dr. Jane Smith – GP, Bathurst Medical Centre | ✅ Generated | [PractitionerRole-generalpractitioner-smith-jane.json](PractitionerRole-generalpractitioner-smith-jane.json) |
| Practitioner | Dr. Emily Chen | ✅ Generated | [Practitioner-chen-emily.json](Practitioner-chen-emily.json) |
| PractitionerRole | Dr. Emily Chen – Gynaecologist, Ashfield Private Clinic | ✅ Generated | [PractitionerRole-obstetrician-chen-emily.json](PractitionerRole-obstetrician-chen-emily.json) |

## 3. Specialist (Gynaecological Oncologist – Private Practice)

| Data Field | Actual Data | Critical? |
| --- | --- | --- |
| Patient Name | Alex Thompson | *Yes |
| Date of Birth | 15/05/1993 | *Yes |
| IHI | 8003608500344031 | *Yes |
| MEDICARE NO | 29548194011 | *Yes |
| Address (Patient) | 42 Macquarie St, Bathurst, NSW 2795 | No |
| Referral ID | REF-2025-10-004 | *Yes |
| Acceptance Date | 2025-10-10 | *Yes |
| Procedure Request ID | REQ-2025-10-005 | *Yes |
| Procedure Type | Colposcopy with Biopsy; Date: 2025-10-15, 11:00 AM | *Yes |
| eScript ID | SCR-2025-10-006 | *Yes |
| eScript Details | Ibuprofen 400 mg every 6–8 hours PRN (max 2.4 g/day), Paracetamol 500 mg every 6 hours PRN (max 4 g/day), over-the-counter; Issued: 2025-10-15 | *Yes |
| Histopathology Result ID | PATH-2025-10-007 | *Yes |
| Result Details | CIN2/3 confirmed; Recommend: Cone biopsy surgery; Date: 2025-10-20 | *Yes |
| Multidisciplinary Meeting ID | MDM-2025-10-008 | *Yes |
| MDM Decision | Plan: Day surgery (cone procedure); Shared Care Plan Updated: 2025-10-20 | *Yes |
| Hospital Booking ID | BOOK-2025-10-009 | *Yes |
| Booking Details | Ashfield Private Hospital (HPI-O: 8003628233379211); Date: 2025-11-01; Prep: SMART Form completed | *Yes |
| SMART Form ID | FORM-2025-10-010 | *Yes |
| Form Details | Consent: Signed digitally; Medical History: No comorbidities; Allergies: Penicillin | *Yes |
| ALLIED HEALTH eREFERRALS | Issued: Physio (REF-2025-11-017), Counselling (REF-2025-11-018) electronically | *Yes |
| Structured Data for Payer Approvals | Patient/procedure data structured for instant payer requests |  |
| Payer Pre-Approval | Submitted: Procedure Code CNE001; Cost: $6,000; Insurer: Medibank Private | No |
| Provider Organisation | Ashfield Private Clinic (HPI-O: 8003624900045276) | *Yes |
| Organisation Address | 12 Roberts St, Ashfield, NSW 2131 | No |
| Clinician | Dr. Emily Chen (Gynaecologist, HPI-I: 8003616566728344) | *Yes |

### FHIR Resources – Specialist (Gynaecological Oncologist – Private Practice)

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Patient | Alex Thompson | ✅ Generated | [Patient-thompson-alex.json](Patient-thompson-alex.json) |
| Encounter | Colposcopy with biopsy visit, 2025-10-15 | ✅ Generated | [Encounter-colposcopy-thompson-alex-20251015.json](Encounter-colposcopy-thompson-alex-20251015.json) |
| ServiceRequest | Colposcopy with Biopsy, requested (REQ-2025-10-005) | ✅ Generated | [ServiceRequest-colposcopybiopsy-thompson-alex-20251010.json](ServiceRequest-colposcopybiopsy-thompson-alex-20251010.json) |
| Procedure | Colposcopy with biopsy, performed in-rooms (specimen sent for histopathology) | ✅ Generated | [Procedure-colposcopybiopsy-thompson-alex-20251015.json](Procedure-colposcopybiopsy-thompson-alex-20251015.json) |
| MedicationRequest | Ibuprofen 400 mg PRN (eScript SCR-2025-10-006) | ✅ Generated | [MedicationRequest-ibuprofen-thompson-alex-20251015.json](MedicationRequest-ibuprofen-thompson-alex-20251015.json) |
| MedicationRequest | Paracetamol 500 mg PRN (eScript SCR-2025-10-006) | ✅ Generated | [MedicationRequest-paracetamol-thompson-alex-20251015.json](MedicationRequest-paracetamol-thompson-alex-20251015.json) |
| ServiceRequest | Histopathology examination of cervical biopsy specimen (REQ-2025-10-007, synthesised identifier), requested from the colposcopy-directed biopsy | ✅ Generated | [ServiceRequest-histopathology-thompson-alex-20251015.json](ServiceRequest-histopathology-thompson-alex-20251015.json) |
| DiagnosticReport | Histopathology result (PATH-2025-10-007), CIN2/3 confirmed | ✅ Generated | [DiagnosticReport-histopathology-thompson-alex-20251020.json](DiagnosticReport-histopathology-thompson-alex-20251020.json) |
| Encounter | Multidisciplinary meeting / specialist decision encounter (MDM-2025-10-008) | ⏳ Not yet generated | — |
| ServiceRequest | Cone biopsy day surgery, requested following MDM decision (REQ-2025-11-009, synthesised identifier) | ✅ Generated | [ServiceRequest-conebiopsydaysurgery-thompson-alex-20251020.json](ServiceRequest-conebiopsydaysurgery-thompson-alex-20251020.json) |
| Appointment | Ashfield Private Hospital booking (BOOK-2025-11-009) | ✅ Generated | [Appointment-hospitalbooking-thompson-alex-20251101.json](Appointment-hospitalbooking-thompson-alex-20251101.json) |
| QuestionnaireResponse | SMART Form consent (FORM-2025-10-010) | ⏳ Not yet generated | — |
| ServiceRequest | Allied health eReferral – Physio (REF-2025-11-017) | ✅ Generated | [ServiceRequest-referral-physio-thompson-alex-20251101.json](ServiceRequest-referral-physio-thompson-alex-20251101.json) |
| ServiceRequest | Allied health eReferral – Counselling (REF-2025-11-018) | ✅ Generated | [ServiceRequest-referral-counselling-thompson-alex-20251101.json](ServiceRequest-referral-counselling-thompson-alex-20251101.json) |
| Bundle (AU Patient Summary) | Self-contained AU PS document, curated by Dr. Chen, dated 2025-11-01 — Problems, Allergies, Medicines, Results (both lab reports), Procedure History; no Vital Signs; Plan of Care is text-narrative only | ✅ Generated | [Bundle-aups-specialist-thompson-alex-20251101.json](Bundle-aups-specialist-thompson-alex-20251101.json) |
| Organization | Ashfield Private Clinic | ✅ Generated | [Organization-ashfield-private-clinic.json](Organization-ashfield-private-clinic.json) |
| Location | Ashfield Private Clinic | ✅ Generated | [Location-ashfield-private-clinic.json](Location-ashfield-private-clinic.json) |
| HealthcareService | Ashfield Private Clinic – Specialist medical clinic service | ✅ Generated | [HealthcareService-specialistmedical-ashfield-private-clinic.json](HealthcareService-specialistmedical-ashfield-private-clinic.json) |
| Organization | Ashfield Private Hospital | ✅ Generated | [Organization-ashfield-private-hospital.json](Organization-ashfield-private-hospital.json) |
| Location | Ashfield Private Hospital | ✅ Generated | [Location-ashfield-private-hospital.json](Location-ashfield-private-hospital.json) |
| HealthcareService | Ashfield Private Hospital – Private acute care hospital | ✅ Generated | [HealthcareService-privateacute-ashfield-private-hospital.json](HealthcareService-privateacute-ashfield-private-hospital.json) |
| Practitioner | Dr. Emily Chen | ✅ Generated | [Practitioner-chen-emily.json](Practitioner-chen-emily.json) |
| PractitionerRole | Dr. Emily Chen – Gynaecologist, Ashfield Private Clinic | ✅ Generated | [PractitionerRole-obstetrician-chen-emily.json](PractitionerRole-obstetrician-chen-emily.json) |

## 4. Private Hospital (Theatre / Inpatient)

| Data Field | Actual Data | Critical? |
| --- | --- | --- |
| Patient Name | Alex Thompson | *Yes |
| Date of Birth | 15/05/1993 | *Yes |
| IHI | 8003608500344031 | *Yes |
| MEDICARE NO | 29548194011 | *Yes |
| Address (Patient) | 42 Macquarie St, Bathurst, NSW 2795 | No |
| Booking ID | BOOK-2025-11-009 | *Yes |
| Procedure Type | Cone Biopsy (Day Surgery); Date: 2025-11-01, 8:00 AM | *Yes |
| SMART Form ID | FORM-2025-11-011 | *Yes |
| Pre-Admission Details | Completed: Bloods normal; Consent: Signed digitally, 2025-10-30 | *Yes |
| Peri-Operative Notes ID | PERI-2025-11-012 | *Yes |
| Notes Details | Anaesthesia: General; Procedure: Successful; Blood Loss: 100 mL; Complications: None | *Yes |
| Discharge Summary ID | DS-2025-11-013 | *Yes |
| Discharge Date | 2025-11-01, 16:00 PM | *Yes |
| Summary Key Points | Meds: Ibuprofen 400 mg every 6–8 hours PRN (max 2.4 g/day) x5 days; Paracetamol 500 mg every 6 hours PRN (max 4 g/day) x5 days; Non-Pharmacologic: Heating pad, deep breathing, hydration; Restrictions: No lifting >5 kg; Follow-up: GP in 7 days | *Yes |
| Follow-Up Appointments | Auto-generated: GP (2025-11-08), Physio (2025-11-10), Counselling (2025-11-15); In MyHealth App | *Yes |
| Image Viewer Access | Intra-op images attached; Viewed by: Surgical Team (HPI-O: 8003628233379211) | No |
| Publication Status | Published: Shared Care Plan; Notified: GP, Specialist, Patient | *Yes |
| Provider Organisation | Ashfield Private Hospital (HPI-O: 8003628233379211) | *Yes |
| Organisation Address | 70 Victoria St, Ashfield, NSW 2131 | No |
| Clinician | Dr. Mark Wilson (Surgeon, HPI-I: 8003616566728351) | *Yes |

### FHIR Resources – Private Hospital (Theatre / Inpatient)

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Patient | Alex Thompson | ✅ Generated | [Patient-thompson-alex.json](Patient-thompson-alex.json) |
| Composition (AU Patient Summary) | Patient Summary retrieved by Ashfield Private Hospital at admission (pulled independently, not sent with the referral) | ⏳ Not yet generated | — |
| Appointment | Hospital booking (BOOK-2025-11-009) | ✅ Generated | [Appointment-hospitalbooking-thompson-alex-20251101.json](Appointment-hospitalbooking-thompson-alex-20251101.json) |
| QuestionnaireResponse | SMART Form pre-admission (FORM-2025-11-011) | ⏳ Not yet generated | — |
| Encounter | Peri-operative encounter (PERI-2025-11-012) | ✅ Generated | [Encounter-periop-thompson-alex-20251101.json](Encounter-periop-thompson-alex-20251101.json) |
| Procedure | Cone Biopsy of cervix (Day Surgery) | ✅ Generated | [Procedure-conebiopsy-thompson-alex-20251101.json](Procedure-conebiopsy-thompson-alex-20251101.json) |
| Composition | Discharge Summary (DS-2025-11-013), LOINC 18842-5 "Discharge summary"; references the peri-operative Encounter, Procedure History, and Hospital Discharge Medications; Plan of Care section is text-narrative only, listing the three follow-up appointments | ✅ Generated | [Composition-dischargesummary-thompson-alex-20251101.json](Composition-dischargesummary-thompson-alex-20251101.json) |
| DocumentReference | Discharge Summary (DS-2025-11-013), same identifier as the Composition above — wraps a PDF rendering of that Composition, produced by concatenating a generated Patient narrative banner with the Composition's own narrative and each section narrative, per FHIR document rendering rules | ✅ Generated | [DocumentReference-dischargesummary-thompson-alex-20251101.json](DocumentReference-dischargesummary-thompson-alex-20251101.json) (attachment PDF also saved standalone as [Discharge Summary - Alex Thompson - 2025-11-01.pdf](Discharge%20Summary%20-%20Alex%20Thompson%20-%202025-11-01.pdf)) |
| MedicationRequest | Discharge meds – Ibuprofen x5 days | ✅ Generated | [MedicationRequest-ibuprofen-discharge-thompson-alex-20251101.json](MedicationRequest-ibuprofen-discharge-thompson-alex-20251101.json) |
| MedicationRequest | Discharge meds – Paracetamol x5 days | ✅ Generated | [MedicationRequest-paracetamol-discharge-thompson-alex-20251101.json](MedicationRequest-paracetamol-discharge-thompson-alex-20251101.json) |
| CarePlan | Follow-up plan (heating pad, no lifting >5 kg, GP in 7 days) | ⏳ Not yet generated | — |
| Appointment | Follow-up – GP (2025-11-08, BOOK-2025-11-008, synthesised identifier) | ✅ Generated | [Appointment-followupgp-thompson-alex-20251108.json](Appointment-followupgp-thompson-alex-20251108.json) |
| Appointment | Follow-up – Physio (2025-11-10, BOOK-2025-11-019) — shared with Section 6 | ✅ Generated | [Appointment-followupphysio-thompson-alex-20251110.json](Appointment-followupphysio-thompson-alex-20251110.json) |
| Appointment | Follow-up – Counselling (2025-11-15, BOOK-2025-11-020, Telehealth) — shared with Section 6 | ✅ Generated | [Appointment-followupcounselling-thompson-alex-20251115.json](Appointment-followupcounselling-thompson-alex-20251115.json) |
| Organization | Ashfield Private Hospital | ✅ Generated | [Organization-ashfield-private-hospital.json](Organization-ashfield-private-hospital.json) |
| Location | Ashfield Private Hospital | ✅ Generated | [Location-ashfield-private-hospital.json](Location-ashfield-private-hospital.json) |
| HealthcareService | Ashfield Private Hospital – Private acute care hospital | ✅ Generated | [HealthcareService-privateacute-ashfield-private-hospital.json](HealthcareService-privateacute-ashfield-private-hospital.json) |
| Practitioner | Dr. Mark Wilson | ✅ Generated | [Practitioner-wilson-mark.json](Practitioner-wilson-mark.json) |
| PractitionerRole | Dr. Mark Wilson – Surgeon, Ashfield Private Hospital | ✅ Generated | [PractitionerRole-obstetrician-wilson-mark.json](PractitionerRole-obstetrician-wilson-mark.json) |

## 5. Pharmacy

| Data Field | Actual Data | Critical? |
| --- | --- | --- |
| Patient Name | Alex Thompson | *Yes |
| Date of Birth | 15/05/1993 | *Yes |
| IHI | 8003608500344031 | *Yes |
| MEDICARE NO | 29548194011 | *Yes |
| Address (Patient) | 42 Macquarie St, Bathurst, NSW 2795 | No |
| Shared Care Plan ID | SCP-2025-10-003 | *Yes |
| Medication Update ID | MED-2025-11-014 | *Yes |
| Updated Medications | Ibuprofen 400 mg every 6–8 hours PRN (max 2.4 g/day) x5 days; Paracetamol 500 mg every 6 hours PRN (max 4 g/day) x5 days, over-the-counter Sertraline 100 mg 1 tablet each morning;  Ibuprofen 400 mg every 6-8 hours PRN (max 3/day);  Short course of Oxycodone 5mg PRN (max 4/day) x 3 days; Paracetamol 500 mg every 6 hours PRN (max 4/day) | *Yes |
| CDS Alert | Check: Ibuprofen + Sertraline (SSRI); Red Flag: GI bleeding risk | *Yes |
| Pharmacist Notes ID | NOTE-2025-11-015 | *Yes |
| Notes Details | Counselling: Take Ibuprofen with food; Alternate with Paracetamol;  Stop date: 2025-11-06; Counselling – 10 tablets only supplied for Oxycodone take only if pain is intense; If oxycodone not necessary, take Ibuprofen with food and alternate with Paracetamol Heating pad, hydration advised; Watch: Nausea, rash | *Yes |
| Dispense Event ID | DISP-2025-11-016 | *Yes |
| Dispense Details | Dispensed: 25 tablets Ibuprofen, 10 tablets Oxycodone, 20 tablets Paracetamol; Date: 2025-11-02 | *Yes |
| Notification Recipients | GP (Dr. Jane Smith, HPI-I: 8003618233394732), Surgeon (Dr. Mark Wilson, HPI-I: 8003616566728351) | *Yes |
| MyHealth App View | Med List Start/Stop dates; Counselling: “Alternate Ibuprofen/Paracetamol, use heating pad”; Reminders: Set | *Yes |
| Provider Organisation | Bathurst Community Pharmacy (HPI-O: 8003629900046257) | *Yes |
| Organisation Address | 15 Keppel St, Bathurst, NSW 2795 | No |
| Clinician | Ms. Sarah Lee (Pharmacist, HPI-I: 8003616566728377) | *Yes |

### FHIR Resources – Pharmacy

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Patient | Alex Thompson | ✅ Generated | [Patient-thompson-alex.json](Patient-thompson-alex.json) |
| Composition (AU Patient Summary) | Patient Summary viewed by Bathurst Community Pharmacy as part of medication review | ⏳ Not yet generated | — |
| CarePlan | Shared Care Plan (SCP-2025-10-003) | ⏳ Not yet generated | — |
| Encounter | Medication review encounter, Bathurst Community Pharmacy, 2025-11-02 | ✅ Generated | [Encounter-medicationreview-thompson-alex-20251102.json](Encounter-medicationreview-thompson-alex-20251102.json) |
| MedicationStatement | Sertraline 100 mg each morning — newly disclosed regular medication | ✅ Generated | [MedicationStatement-sertraline-thompson-alex-20251102.json](MedicationStatement-sertraline-thompson-alex-20251102.json) |
| MedicationStatement | Ibuprofen 400 mg PRN — revised to max 3 tablets/day following the Sertraline interaction alert | ✅ Generated | [MedicationStatement-ibuprofen-postdischarge-thompson-alex-20251102.json](MedicationStatement-ibuprofen-postdischarge-thompson-alex-20251102.json) |
| MedicationStatement | Paracetamol 500 mg PRN — reconfirmed | ✅ Generated | [MedicationStatement-paracetamol-postdischarge-thompson-alex-20251102.json](MedicationStatement-paracetamol-postdischarge-thompson-alex-20251102.json) |
| MedicationStatement | Oxycodone 5 mg PRN — short course, breakthrough pain only | ✅ Generated | [MedicationStatement-oxycodone-thompson-alex-20251102.json](MedicationStatement-oxycodone-thompson-alex-20251102.json) |
| Composition | Medication Review episode (MED-2025-11-014), LOINC 56445-0 "Medication summary Document" — follows the AU PS section pattern even though it's a plain `au-core-composition`: Active Problems, Active Allergies, Current Medicines (all 4 MedicationStatements), Procedure History (colposcopy + cone biopsy), Plan of Care (counselling notes, NOTE-2025-11-015, text-only) | ✅ Generated | [Composition-medicationreview-thompson-alex-20251102.json](Composition-medicationreview-thompson-alex-20251102.json) |
| MedicationDispense | Ibuprofen (Nurofen Double Strength) 24 tablets — one standard retail pack, covering the 5-day/max-3-per-day course (DISP-2025-11-016) | ✅ Generated | [MedicationDispense-ibuprofen-thompson-alex-20251102.json](MedicationDispense-ibuprofen-thompson-alex-20251102.json) |
| MedicationDispense | Oxycodone 10 tablets, no `authorizingPrescription` (DISP-2025-11-016) | ✅ Generated | [MedicationDispense-oxycodone-thompson-alex-20251102.json](MedicationDispense-oxycodone-thompson-alex-20251102.json) |
| MedicationDispense | Paracetamol 20 tablets (DISP-2025-11-016) | ✅ Generated | [MedicationDispense-paracetamol-thompson-alex-20251102.json](MedicationDispense-paracetamol-thompson-alex-20251102.json) |
| Organization | Bathurst Community Pharmacy | ✅ Generated | [Organization-bathurst-community-pharmacy.json](Organization-bathurst-community-pharmacy.json) |
| Location | Bathurst Community Pharmacy | ✅ Generated | [Location-bathurst-community-pharmacy.json](Location-bathurst-community-pharmacy.json) |
| HealthcareService | Bathurst Community Pharmacy | ✅ Generated | [HealthcareService-communitypharmacy-bathurst-community-pharmacy.json](HealthcareService-communitypharmacy-bathurst-community-pharmacy.json) |
| Practitioner | Sarah Lee | ✅ Generated | [Practitioner-lee-sarah.json](Practitioner-lee-sarah.json) |
| PractitionerRole | Sarah Lee – Pharmacist, Bathurst Community Pharmacy | ✅ Generated | [PractitionerRole-retailpharmacist-lee-sarah.json](PractitionerRole-retailpharmacist-lee-sarah.json) |

## 6. Allied Health (Physiotherapy & Counselling)

| Data Field | Actual Data | Critical? |
| --- | --- | --- |
| Patient Name | Alex Thompson | *Yes |
| Date of Birth | 15/05/1993 | *Yes |
| IHI | 8003608500344031 | *Yes |
| MEDICARE NO | 29548194011 | *Yes |
| Address (Patient) | 42 Macquarie St, Bathurst, NSW 2795 | No |
| eReferral ID (Physio) | REF-2025-11-017 | *Yes |
| eReferral ID (Counselling) | REF-2025-11-018 | *Yes |
| Booking ID (Physio) | BOOK-2025-11-019 | *Yes |
| Physio Details | Pelvic-Health Physio: 2025-11-10, 14:00 PM, Bathurst Physio Centre (HPI-O: 8003628233379229); Balance Training: 2025-10-09, 14:00 PM; Transport: Confirmed digitally; Prep: Wear comfortable clothing | *Yes |
| Booking ID (Counselling) | BOOK-2025-11-020 | *Yes |
| Counselling Details | Psycho-Oncology: 2025-11-15, 11:00 AM, Telehealth; Prep: List anxiety concerns | *Yes |
| Provider Directory Filters | Wait Time: <1 week; Accessibility: Wheelchair-friendly; Selected: Bathurst Physio, Telehealth Counselling | *Yes |
| Observations ID (Physio) | OBS-2025-11-021 | *Yes |
| Physio Measures | Pelvic Floor Strength: 3/5; Pain Score: 3/10; Mobility: Improving | *Yes |
| Observations ID (Counselling) | OBS-2025-11-022 | *Yes |
| Counselling Measures | PHQ-9: 10 (mild-moderate depression); Anxiety: Moderate | *Yes |
| Apple Watch Data | Consent: Shared via MyHealth App; Heart Rate: Avg 80 bpm; Steps: 5,000/day; Date Range: 2025-11-01 to 2025-11-10 | *Yes |
| MYHEALTH APP VIEW | Displays: Appointments, transport details, prep notes | *Yes |
| Shared Care Plan Update | Added: Physio exercises, counselling notes; Notified: GP, Specialist | *Yes |
| Provider Access | Limited: Physio (observations), Counselling (mental health); HPI-O: 8003628233379229 (Physio Centre) | No |
| Provider Organisation | Bathurst Physio Centre (HPI-O: 8003628233379229) | *Yes |
| Organisation Address | 30 William St, Bathurst, NSW 2795 | No |
| Clinician (Physio) | Ms. Sarah Evans (Physiotherapist, HPI-I: 8003613233394519) | *Yes |
| Clinician (Counselling) | Dr. Rachel Patel (Counsellor, HPI-I: 8003611566727867) | *Yes |

### FHIR Resources – Allied Health (Physiotherapy & Counselling)

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Patient | Alex Thompson | ✅ Generated | [Patient-thompson-alex.json](Patient-thompson-alex.json) |
| ServiceRequest | eReferral – Physio (REF-2025-11-017) | ✅ Generated | [ServiceRequest-referral-physio-thompson-alex-20251101.json](ServiceRequest-referral-physio-thompson-alex-20251101.json) |
| ServiceRequest | eReferral – Counselling (REF-2025-11-018) | ✅ Generated | [ServiceRequest-referral-counselling-thompson-alex-20251101.json](ServiceRequest-referral-counselling-thompson-alex-20251101.json) |
| Appointment | Physio booking (BOOK-2025-11-019) — shared with Section 4's follow-up appointments | ✅ Generated | [Appointment-followupphysio-thompson-alex-20251110.json](Appointment-followupphysio-thompson-alex-20251110.json) |
| Appointment | Counselling booking (BOOK-2025-11-020), Telehealth — shared with Section 4 | ✅ Generated | [Appointment-followupcounselling-thompson-alex-20251115.json](Appointment-followupcounselling-thompson-alex-20251115.json) |
| Encounter | Pelvic-health physio visit, 2025-11-10 | ✅ Generated | [Encounter-physiovisit-thompson-alex-20251110.json](Encounter-physiovisit-thompson-alex-20251110.json) |
| Observation | Physio measures (OBS-2025-11-021) – pelvic floor strength (Modified Oxford Scale, 3/5) | ✅ Generated | [Observation-pelvicfloorstrength-thompson-alex-20251110.json](Observation-pelvicfloorstrength-thompson-alex-20251110.json) |
| Observation | Physio measures (OBS-2025-11-021) – pain score (3/10) | ✅ Generated | [Observation-painscore-physio-thompson-alex-20251110.json](Observation-painscore-physio-thompson-alex-20251110.json) |
| Observation | Physio measures (OBS-2025-11-021) – mobility (Improving) | ✅ Generated | [Observation-mobility-thompson-alex-20251110.json](Observation-mobility-thompson-alex-20251110.json) |
| Encounter | Psycho-Oncology counselling, Telehealth, 2025-11-15 | ✅ Generated | [Encounter-counsellingvisit-thompson-alex-20251115.json](Encounter-counsellingvisit-thompson-alex-20251115.json) |
| Observation | Counselling measures (OBS-2025-11-022) – PHQ-9 total score (10, mild-moderate depression) | ✅ Generated | [Observation-phq9-thompson-alex-20251115.json](Observation-phq9-thompson-alex-20251115.json) |
| Observation | Counselling measures (OBS-2025-11-022) – anxiety level (Moderate) | ✅ Generated | [Observation-anxietylevel-thompson-alex-20251115.json](Observation-anxietylevel-thompson-alex-20251115.json) |
| Observation | Apple Watch data – heart rate, steps | ⏳ Not yet generated | — |
| CarePlan | Shared Care Plan update (physio exercises, counselling notes) | ⏳ Not yet generated | — |
| Organization | Bathurst Physio Centre | ✅ Generated | [Organization-bathurst-physio-centre.json](Organization-bathurst-physio-centre.json) |
| Location | Bathurst Physio Centre | ✅ Generated | [Location-bathurst-physio-centre.json](Location-bathurst-physio-centre.json) |
| HealthcareService | Bathurst Physio Centre | ✅ Generated | [HealthcareService-physiotherapyservices-bathurst-physio-centre.json](HealthcareService-physiotherapyservices-bathurst-physio-centre.json) |
| Practitioner | Sarah Evans | ✅ Generated | [Practitioner-evans-sarah.json](Practitioner-evans-sarah.json) |
| PractitionerRole | Sarah Evans – Physiotherapist, Bathurst Physio Centre | ✅ Generated | [PractitionerRole-physiotherapist-evans-sarah.json](PractitionerRole-physiotherapist-evans-sarah.json) |
| Organization | Bathurst Psychology | ✅ Generated | [Organization-bathurst-psychology.json](Organization-bathurst-psychology.json) |
| Location | Bathurst Psychology | ✅ Generated | [Location-bathurst-psychology.json](Location-bathurst-psychology.json) |
| HealthcareService | Bathurst Psychology | ✅ Generated | [HealthcareService-clinicalpsychology-bathurst-psychology.json](HealthcareService-clinicalpsychology-bathurst-psychology.json) |
| Practitioner | Dr. Rachel Patel | ✅ Generated | [Practitioner-patel-rachel.json](Practitioner-patel-rachel.json) |
| PractitionerRole | Dr. Rachel Patel – Counsellor, Bathurst Psychology | ✅ Generated | [PractitionerRole-counsellor-patel-rachel.json](PractitionerRole-counsellor-patel-rachel.json) |

## 7. Population Health / Analytics

| Data Field | Actual Data | Critical? |
| --- | --- | --- |
| De-Identified Cohort | Cervical Cancer Pathway (n=200, Regional NSW, 2025) | *Yes |
| IHI (Sample, De-Identified) | Not linked; Aggregated only | *Yes |
| Referral to Acceptance Time | Median: 2 days; 90th Percentile: 6 days | *Yes |
| Result Turnaround | Median: 7 days; High-Risk Alerts: 100% within 24 hours | *Yes |
| Surgery Timing | Median: 20 days; Outliers: 40 days (targeted reduction) | *Yes |
| Allied Health Uptake | Physio: 88%; Counselling: 70%; Regional Gap: 12% vs. Metro | *Yes |
| Outcome Metrics | Complications: 10% (linked to delays >30 days); Readmissions: 5% | *Yes |
| Dashboard Insights | Bottlenecks: Pathology wait times; Equity: Regional access improved 15% | *Yes |
| Update Cadence | Daily; Source: FHIR via Health Connect Australia | No |
| Provider Organisation | Australian Institute of Health and Welfare (HPI-O: TBD) | *Yes |
| Organisation Address | 1 Oxford St, Canberra, ACT 2601 | No |

### FHIR Resources – Population Health / Analytics

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Organization | Australian Institute of Health and Welfare | ⏳ Not yet generated | — |

> This section describes a de-identified, aggregated population-health view rather than per-patient data — it wouldn't produce Patient-linked clinical resources; a `Measure`/`MeasureReport` pair would be the more natural fit if we model it at all.


## Pending / Placeholder Data

**Source-table identifiers.** IHI, MEDICARE NO, HPI-O, and HPI-I values in this document's own tables (patient demographics, every "Provider Organisation"/"Clinician" row) match the real Services Australia / Healthcare Identifiers Service test data used in the FHIR resources, for every entity that has one built. Three entities have no FHIR resource yet and still show placeholder numbers: National Cancer Screening Register (HPI-O), Sarah Taylor (HPI-I), Australian Institute of Health and Welfare (HPI-O).

**Resource identifiers.** Alex's `Patient`, `Organization`, `HealthcareService`, `Practitioner`, and `PractitionerRole` resources — standalone and embedded — carry `identifier` values from the Services Australia / Healthcare Identifiers Service test data:
- `Patient`: IHI + Medicare Number
- `Organization`: HPI-O + ABN
- `HealthcareService`: HPI-O
- `Practitioner`: HPI-I + Medicare Prescriber Number + AHPRA registration `qualification`
- `PractitionerRole`: HPI-I + Medicare Provider Number

**`Bundle-aups-thompson-alex-20251009.json`** (GP AU Patient Summary document Bundle):
- Composition, Patient, custodian Organization, Device, Practitioner/PractitionerRole, Encounter, and every section entry (Condition, AllergyIntolerance, MedicationStatement, DiagnosticReport, 3 vital-sign Observations) embedded inline via `urn:uuid`.
- Embedded `Patient`: IHI + Medicare Number identifier, matching `Patient-thompson-alex.json`.
- DiagnosticReport `performer`/Bathurst Pathology and `basedOn`/ServiceRequest: plain relative references to the standalone files, not embedded.
- `Composition.author`: `Device` ("Bathurst Medical Centre Clinical Information System"). `PractitionerRole/generalpractitioner-lee-chris` embedded, used as `Condition.recorder`/`asserter` and `Observation.performer`, not as author. `Device` identifier, manufacturer, model: fictional.

**`Bundle-aups-specialist-thompson-alex-20251101.json`** (specialist AU PS document Bundle, curated by Dr. Chen, dated 2025-11-01):
- `Composition.author`: Dr. Chen's `PractitionerRole` directly. No `Device` embedded.
- Vital Signs section: omitted.
- Embedded `Condition`'s `encounter` and `recorder`/`asserter`: external relative references to the GP consultation and Dr. Lee. `note`: records the biopsy-confirmed CIN2/3 and planned cone biopsy.
- Plan of Care: text-narrative only, no `entry` array.
- Histopathology `DiagnosticReport.performer`: embedded Ashfield Private Clinic `Organization` (same `urn:uuid` as the custodian).

**Other resource-level facts:**
- `Encounter-periop-thompson-alex-20251101.json`: no `identifier`. `Encounter.appointment` → `Appointment` BOOK-2025-11-009. GP/Physio/Counselling follow-up `Appointment`s: do not reference this encounter.
- GP follow-up `Appointment`: Booking ID BOOK-2025-11-008 (synthesised). Physio/Counselling follow-ups: real BOOK-2025-11-019/BOOK-2025-11-020 values from Section 6.
- GP consultation "Alcohol use" vital: not modelled as an Observation. Weight, blood pressure, heart rate: modelled. AU Core Alcohol Status profile: absent from current published (v2.0.0) and ballot (v3.0.0-ballot1) releases.
- ServiceRequest/DiagnosticReport/Task business identifiers (AU Base Local Identifier profile): `identifier.system` carries the assigning organisation's real HPI-O, e.g. `http://ns.electronichealth.net.au/id/hpio-scoped/order/1.0/8003629900046240` (Bathurst Medical Centre).
- Two eScript `MedicationRequest` identifiers: `http://ns.electronichealth.net.au/id/hpio-scoped/prescription/1.0/{HPI-O}` namespace, Ashfield Private Clinic's HPI-O. `MedicationRequest.identifier`: no `assigner` field.
- `Appointment-hospitalbooking-thompson-alex-20251101.json` identifier (BOOK-2025-11-009): fictional URI `http://ashfieldprivatehospital.example.org/id/booking`, not the `hpio-scoped/order/1.0` namespace.
- Histopathology `DiagnosticReport.performer` and its `ServiceRequest.identifier.assigner`: Ashfield Private Clinic. No specific anatomical pathology laboratory named.
- Three `MedicationDispense` resources (Ibuprofen, Paracetamol, Oxycodone): `contained` `Medication` resource, `medicationReference`, Trade Product Pack level, `medication-type` extension `BPDSF`. Nurofen Double Strength ibuprofen 400 mg tablet, 24 (`930613011000036109`); Panadol 500 mg tablet, 20 (`56245011000036101`); Endone 5 mg tablet, 10 (`1496631000168100`). `MedicationRequest`/`MedicationStatement`: generic/ingredient level.
- Five Section 6 allied-health `Observation`s (`Observation-pelvicfloorstrength-thompson-alex-20251110.json`, `Observation-painscore-physio-thompson-alex-20251110.json`, `Observation-mobility-thompson-alex-20251110.json`, `Observation-phq9-thompson-alex-20251115.json`, `Observation-anxietylevel-thompson-alex-20251115.json`): no `meta.profile`, plain base FHIR R4 `Observation`. Codes: LOINC 72514-3 (pain score), 44261-6 (PHQ-9), 54522-8 (mobility); SNOMED 249957003 (Oxford muscle-power scale), 405051006/61387006 (anxiety level).
- `MedicationDispense-oxycodone-thompson-alex-20251102.json`: no `authorizingPrescription`.
- `DocumentReference-dischargesummary-thompson-alex-20251101.json`: wraps a PDF (base64 in `content[0].attachment.data`), rendered from a generated Patient narrative banner plus the Composition's narrative and section narratives. `Patient-thompson-alex.json`: no `text.div`. Shares business identifier DS-2025-11-013 with the Composition; no direct FHIR reference between them.


## Change Log

**Purpose:** deviations between this data set and the original source story/spreadsheet only — renamed entities, corrected values, resolved conflicts, invented data. For story-owner review and confirmation. Excludes: document edits, FHIR-modelling/terminology decisions (see [Pending / Placeholder Data](#pending--placeholder-data)).

| Date | Change | Reason |
| --- | --- | --- |
| 2026-08-12 | Renamed "Sydney Private Clinic" (Dr. Emily Chen) to **Ashfield Private Clinic**; address updated from 100 George St, Sydney, NSW 2000 to 12 Roberts St, Ashfield, NSW 2131 | Aligned to the existing Organization already generated from the Services Australia providers/orgs sheet, so Dr. Chen's PractitionerRole didn't need a second, duplicate clinic |
| 2026-08-12 | Renamed "Sydney Private Hospital" (Dr. Mark Wilson) to **Ashfield Private Hospital**; address updated from 50 Pitt St, Sydney, NSW 2000 to 63 Victoria St, Ashfield, NSW 2131 | Same reason — aligns to the existing Organization for Dr. Wilson |
| 2026-08-12 | Section 3 lists "Hospital Booking ID: BOOK-2025-10-009" while Section 4 lists "Booking ID: BOOK-2025-11-009" for what is clearly the same Ashfield Private Hospital day-surgery admission on 2025-11-01. A single `Appointment` resource was built using **BOOK-2025-11-009** (the Section 4 value, which also supplies the 8:00 AM time) | Likely a typo in the source spreadsheet's Section 3 row; using one Appointment resource avoids duplicating the same real-world booking |
| 2026-08-12 | Built a `ServiceRequest` (REQ-2025-11-009) authorising the cone biopsy day surgery that `Appointment-hospitalbooking-thompson-alex-20251101.json` is `basedOn` — this identifier value is **synthesised**, not sourced from the spreadsheet | The story data gives a Hospital Booking ID for the appointment but no separate request/order ID for the surgery itself; a `ServiceRequest` is still needed so the Appointment has something to be `basedOn` |
| 2026-08-13 | `MedicationDispense-ibuprofen-thompson-alex-20251102.json` quantity changed from the story's **25 tablets** to **24 tablets** | 25 doesn't match either real Nurofen Double Strength pack size (12 or 24); a single 24-pack covers the revised 5-day course (max 3 tablets/day = 15 tablets) and matches the real Trade Product Pack, `930613011000036109` |
| 2026-08-13 | Section 6's "Balance Training: 2025-10-09, 14:00 PM" (within the Physio Details field) is not modelled as a separate `Encounter` | This date predates the physio eReferral (2025-11-01) and hospital admission (2025-11-01) entirely — likely a stray/templated entry in the source spreadsheet, not a real event in Alex's pathway. Only the 2025-11-10 pelvic-health physio visit is built |
| 2026-08-19 | Ashfield Private Hospital's address updated from **63 Victoria St** to **70 Victoria St**, Ashfield, NSW 2131 | Services Australia registered the organisation with this address in their test data |
| 2026-08-20 | All IHI/MEDICARE NO/HPI-O/HPI-I placeholders in the section tables replaced with the real Services Australia / Healthcare Identifiers Service test data values used in the FHIR resources | Story's placeholders were not valid identifiers |
| 2026-08-20 | National Cancer Screening Register (HPI-O), Sarah Taylor (HPI-I), Australian Institute of Health and Welfare (HPI-O): placeholders (2222-1111-0000-9999 / 1010-2020-3030-4040 / 0000-1111-2222-3333) → **TBD** | No FHIR resource built yet for these three entities |
| 2026-08-20 | Dr. Chris Lee and Dr. Jane Smith's shared placeholder HPI-I (5555-6666-7777-8888) → distinct real HPI-I values | Two clinicians cannot share one HPI-I |
