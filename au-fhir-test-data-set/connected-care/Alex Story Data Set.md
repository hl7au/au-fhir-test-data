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

See the [Pending / Placeholder Data](#pending--placeholder-data) notes at the bottom of this document for open items and judgment calls made while building this data set.

## 0. MyHealth App

| Data Field | Actual Data | Critical? |
| --- | --- | --- |
| Patient Name | Alex Thompson | *Yes |
| Date of Birth | 15/05/1993 | *Yes |
| IHI | 9876-5432-1098-7654 | *Yes |
| MEDICARE NO | 2345 678 901 1 | *Yes |
| Address (Patient) | 42 Macquarie St, Bathurst, NSW 2795 | No |
| Phone Number | 0412-345-678 | No |
| Email | [alex.thompson@cafe.com](mailto:alex.thompson@cafe.com) | No |
| Notification Source | National Cancer Screening Register (HPI-O: 2222-1111-0000-9999) | *Yes |
| Notification Details | Reminder: Cervical Screening overdue; Issued: 2025-09-30, 08:00 AM; Via: MyHealth App | *Yes |
| e-Request ID | REQ-2025-10-001 | *Yes |
| e-Request Details | Request Type: Cervical Screening (National Cervical Screening Program); Issued by: Dr. Chris Lee (HPI-I: 5555-6666-7777-8888); Date: 2025-09-30 | *Yes |
| Provider Directory Search | National Health Services Directory (powered by Provider Directory Service); Filters: Location (Bathurst, NSW), Service Type (Pathology), Availability (<1 week); Selected: Bathurst Pathology (HPI-O:1111-2222-3333-4444) | *Yes |
| Booking ID | BOOK-2025-10-000 | *Yes |
| Booking Details | Pathology Centre: Bathurst Pathology, 10 George St, Bathurst, NSW 2795; Date: 2025-10-01, 9:00 AM; Prep: Self-collect swab, bring QR code | *Yes |
| MyHealth App View | Displays: eRequest, Booking Confirmation, Prep Notes (“Bring QR code, no appointment needed for self-collect”); Consent: View shared with GP | *Yes |
| Provider Organisation | National Cancer Screening Register (HPI-O: 2222-1111-0000-9999) | *Yes |
| Organisation Address | 1 Oxford St, Canberra, ACT 2601 | No |
| Clinician | Ms. Sarah Taylor (System Administrator, HPI-I: 1010-2020-3030-4040) | *Yes |
| QR CODE VIEW | Displays consumer perspective: eRequest retrieval, sample processing, results notification | *Yes |

### FHIR Resources – MyHealth App

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Patient | Alex Thompson | ✅ Generated | [Patient-thompson-alex.json](Patient-thompson-alex.json) |
| Organization | National Cancer Screening Register | ⏳ Not yet generated | — |
| *Unresolved* | Reminder: Cervical Screening overdue — no AU Core resource identified yet (not a Communication, since AU Core doesn't include that resource; needs a decision) | ⏳ Not yet generated | — |
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
| IHI | 9876-5432-1098-7654 | *Yes |
| MEDICARE NO | 2345 678 901 1 | *Yes |
| Address (Patient) | 42 Macquarie St, Bathurst, NSW 2795 | No |
| Phone Number | 0412-345-678 | No |
| Email | [alex.thompson@cafe.com](mailto:alex.thompson@cafe.com) | No |
| e-Request ID | REQ-2025-10-001 | *Yes |
| Request Type | Cervical Screening (National Cervical Screening Program) | *Yes |
| Booking Details | Pathology Centre: Bathurst Pathology, 10 George St, Bathurst, NSW 2795; 2025-10-01, 9:00 AM; Booked via MyHealth App | *Yes |
| QR Code Data | eRequest ID: REQ-2025-10-001; IHI: 9876-5432-1098-7654; Provider: Bathurst Pathology (HPI-O: 1111-2222-3333-4444) | *Yes |
| Pathology Result ID | PATH-2025-10-002 | *Yes |
| Result Date | 2025-10-08 | *Yes |
| Result Details | High-risk HPV detected; CIN2/3 (pre-cancerous); Status: Urgent | *Yes |
| Notification Recipients | Patient (MyHealth App), GP (Dr. Chris Lee, HPI-I: 5555-6666-7777-8888); Trigger: Immediate alert | *Yes |
| DISCOVERY SERVICE ACCESS | Pathologist views gynaecological/sexual health history via Discovery Service | *Yes |
| COHORT ANALYSIS | Augmented by data from National Screening Register for accurate reference range |  |
| REGISTER UPDATE | System automatically updates National Cervical Screening Register |  |
| Follow-Up Timer | Set: Confirm acceptance by GP within 48 hours | *Yes |
| Provider Organisation | Bathurst Pathology (HPI-O: 1111-2222-3333-4444) | *Yes |
| Organisation Address | 10 George St, Bathurst, NSW 2795 | No |
| Clinician | Ms. Sally Johnson (Phlebotomist, HPI-I: 1212-3434-5656-7878) | *Yes |

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
| IHI | 9876-5432-1098-7654 | *Yes |
| MEDICARE NO | 2345 678 901 1 | *Yes |
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
| Provider Directory Search | Filters: Bathurst/Sydney, Wait Time <2 weeks; Selected: Dr. Emily Chen, Ashfield Private Clinic (HPI-I: 2222-3333-4444-5555) | *Yes |
| Subscription Preferences | GP (Dr. Jane Smith, HPI-I: 5555-6666-7777-8888): Critical updates only (results, bookings) | *Yes |
| Provider Organisation | Bathurst Medical Centre (HPI-O: 6666-7777-8888-9999) | *Yes |
| Organisation Address | 25 Russell St, Bathurst, NSW 2795 | No |
| Clinician | Dr. Chris Lee (GP, HPI-I: 5555-6666-7777-8888) | *Yes |

### FHIR Resources – General Practice

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Patient | Alex Thompson | ✅ Generated | [Patient-thompson-alex.json](Patient-thompson-alex.json) |
| AllergyIntolerance | Penicillin (anaphylaxis) — pre-existing, unrelated to this encounter | ✅ Generated | [AllergyIntolerance-penicillin-thompson-alex.json](AllergyIntolerance-penicillin-thompson-alex.json) |
| MedicationStatement | No active medications — pre-existing, unrelated to this encounter | ✅ Generated | [MedicationStatement-nomedications-thompson-alex.json](MedicationStatement-nomedications-thompson-alex.json) |
| Condition | High-risk cervical screening (high-risk HPV / CIN2/3) | ✅ Generated | [Condition-highriskhpv-thompson-alex.json](Condition-highriskhpv-thompson-alex.json) |
| Encounter | GP consultation, 2025-10-09 | ✅ Generated | [Encounter-gpconsultation-thompson-alex-20251009.json](Encounter-gpconsultation-thompson-alex-20251009.json) |
| Composition (Episode of Care Summary) | GP consultation summary, 2025-10-09 — AU Core Composition profile only (no dedicated AU Encounter Summary IG profile yet), LOINC 34133-9 "Summary of episode note", referencing the Encounter with Problems / Vital Signs / Results / Plan of Care sections (labelled with AU PS section LOINC codes). Note: this is the bare `Composition` resource only, referencing the existing standalone connected-care files by `ResourceType/id` — unlike the AU Patient Summary above, it is **not** wrapped in a self-contained `document`-type Bundle, so no resources are embedded and no narrative was added to `Patient-thompson-alex.json`. | ✅ Generated | [Composition-episodeofcaresummary-thompson-alex-20251009.json](Composition-episodeofcaresummary-thompson-alex-20251009.json) |
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

> **Note:** "Sydney Private Clinic" / "Sydney Private Hospital" have been renamed to **Ashfield Private Clinic** / **Ashfield Private Hospital** throughout this document — see Change Log at the top.

## 3. Specialist (Gynaecological Oncologist – Private Practice)

| Data Field | Actual Data | Critical? |
| --- | --- | --- |
| Patient Name | Alex Thompson | *Yes |
| Date of Birth | 15/05/1993 | *Yes |
| IHI | 9876-5432-1098-7654 | *Yes |
| MEDICARE NO | 2345 678 901 1 | *Yes |
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
| Booking Details | Ashfield Private Hospital (HPI-O: 3333-4444-5555-6666); Date: 2025-11-01; Prep: SMART Form completed | *Yes |
| SMART Form ID | FORM-2025-10-010 | *Yes |
| Form Details | Consent: Signed digitally; Medical History: No comorbidities; Allergies: Penicillin | *Yes |
| ALLIED HEALTH eREFERRALS | Issued: Physio (REF-2025-11-017), Counselling (REF-2025-11-018) electronically | *Yes |
| Structured Data for Payer Approvals | Patient/procedure data structured for instant payer requests |  |
| Payer Pre-Approval | Submitted: Procedure Code CNE001; Cost: $6,000; Insurer: Medibank Private | No |
| Provider Organisation | Ashfield Private Clinic (HPI-O: 7777-8888-9999-0000) | *Yes |
| Organisation Address | 12 Roberts St, Ashfield, NSW 2131 | No |
| Clinician | Dr. Emily Chen (Gynaecologist, HPI-I: 2222-3333-4444-5555) | *Yes |

### FHIR Resources – Specialist (Gynaecological Oncologist – Private Practice)

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Patient | Alex Thompson | ✅ Generated | [Patient-thompson-alex.json](Patient-thompson-alex.json) |
| Encounter | Colposcopy with biopsy visit, 2025-10-15 | ✅ Generated | [Encounter-colposcopy-thompson-alex-20251015.json](Encounter-colposcopy-thompson-alex-20251015.json) |
| ServiceRequest | Colposcopy with Biopsy, requested (REQ-2025-10-005) | ✅ Generated | [ServiceRequest-colposcopybiopsy-thompson-alex-20251010.json](ServiceRequest-colposcopybiopsy-thompson-alex-20251010.json) |
| Procedure | Colposcopy with biopsy, performed in-rooms (specimen sent for histopathology) | ✅ Generated | [Procedure-colposcopybiopsy-thompson-alex-20251015.json](Procedure-colposcopybiopsy-thompson-alex-20251015.json) |
| MedicationRequest | Ibuprofen 400 mg PRN (eScript SCR-2025-10-006) | ✅ Generated | [MedicationRequest-ibuprofen-thompson-alex-20251015.json](MedicationRequest-ibuprofen-thompson-alex-20251015.json) |
| MedicationRequest | Paracetamol 500 mg PRN (eScript SCR-2025-10-006) | ✅ Generated | [MedicationRequest-paracetamol-thompson-alex-20251015.json](MedicationRequest-paracetamol-thompson-alex-20251015.json) |
| ServiceRequest | Histopathology examination of cervical biopsy specimen (REQ-2025-10-007, identifier synthesised — see Pending / Placeholder Data), requested from the colposcopy-directed biopsy | ✅ Generated | [ServiceRequest-histopathology-thompson-alex-20251015.json](ServiceRequest-histopathology-thompson-alex-20251015.json) |
| DiagnosticReport | Histopathology result (PATH-2025-10-007), CIN2/3 confirmed | ✅ Generated | [DiagnosticReport-histopathology-thompson-alex-20251020.json](DiagnosticReport-histopathology-thompson-alex-20251020.json) |
| Encounter | Multidisciplinary meeting / specialist decision encounter (MDM-2025-10-008) | ⏳ Not yet generated | — |
| ServiceRequest | Cone biopsy day surgery, requested following MDM decision (identifier synthesised, see Pending / Placeholder Data) | ✅ Generated | [ServiceRequest-conebiopsydaysurgery-thompson-alex-20251020.json](ServiceRequest-conebiopsydaysurgery-thompson-alex-20251020.json) |
| Appointment | Ashfield Private Hospital booking — Section 3 says BOOK-2025-10-009, Section 4 says BOOK-2025-11-009; one Appointment built using BOOK-2025-11-009 (see Change Log) | ✅ Generated | [Appointment-hospitalbooking-thompson-alex-20251101.json](Appointment-hospitalbooking-thompson-alex-20251101.json) |
| QuestionnaireResponse | SMART Form consent (FORM-2025-10-010) | ⏳ Not yet generated | — |
| ServiceRequest | Allied health eReferral – Physio (REF-2025-11-017) | ✅ Generated | [ServiceRequest-referral-physio-thompson-alex-20251101.json](ServiceRequest-referral-physio-thompson-alex-20251101.json) |
| ServiceRequest | Allied health eReferral – Counselling (REF-2025-11-018) | ✅ Generated | [ServiceRequest-referral-counselling-thompson-alex-20251101.json](ServiceRequest-referral-counselling-thompson-alex-20251101.json) |
| Bundle (AU Patient Summary) | Self-contained AU PS document curated by Dr. Chen after the histopathology result — Problems, Allergies, Medicines, Results (both lab reports), Procedure History; no Vital Signs; Plan of Care is text-narrative only (cone biopsy day surgery, both allied health eReferrals, hospital booking — not linked as coded `entry`s) | ✅ Generated | [Bundle-aups-specialist-thompson-alex-20251101.json](Bundle-aups-specialist-thompson-alex-20251101.json) |
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
| IHI | 9876-5432-1098-7654 | *Yes |
| MEDICARE NO | 2345 678 901 1 | *Yes |
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
| Image Viewer Access | Intra-op images attached; Viewed by: Surgical Team (HPI-O: 3333-4444-5555-6666) | No |
| Publication Status | Published: Shared Care Plan; Notified: GP, Specialist, Patient | *Yes |
| Provider Organisation | Ashfield Private Hospital (HPI-O: 3333-4444-5555-6666) | *Yes |
| Organisation Address | 70 Victoria St, Ashfield, NSW 2131 | No |
| Clinician | Dr. Mark Wilson (Surgeon, HPI-I: 3434-5656-7878-9090) | *Yes |

### FHIR Resources – Private Hospital (Theatre / Inpatient)

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Patient | Alex Thompson | ✅ Generated | [Patient-thompson-alex.json](Patient-thompson-alex.json) |
| Composition (AU Patient Summary) | Patient Summary retrieved by Ashfield Private Hospital at admission (not sent with the referral — pulled independently, e.g. via provider access) | ⏳ Not yet generated | — |
| Appointment | Hospital booking (BOOK-2025-11-009) — shared with Section 3, see note there on the BOOK-2025-10-009/BOOK-2025-11-009 discrepancy | ✅ Generated | [Appointment-hospitalbooking-thompson-alex-20251101.json](Appointment-hospitalbooking-thompson-alex-20251101.json) |
| QuestionnaireResponse | SMART Form pre-admission (FORM-2025-11-011) | ⏳ Not yet generated | — |
| Encounter | Peri-operative encounter (PERI-2025-11-012) | ✅ Generated | [Encounter-periop-thompson-alex-20251101.json](Encounter-periop-thompson-alex-20251101.json) |
| Procedure | Cone Biopsy of cervix (Day Surgery) | ✅ Generated | [Procedure-conebiopsy-thompson-alex-20251101.json](Procedure-conebiopsy-thompson-alex-20251101.json) |
| Composition | Discharge Summary (DS-2025-11-013) — same pattern as the GP Episode of Care Summary (Section 2), LOINC 18842-5 "Discharge summary"; references the peri-operative Encounter, Procedure History, and Hospital Discharge Medications; Plan of Care section is text-narrative only, listing the three follow-up appointments without `entry` references (they aren't otherwise linked to the encounter) | ✅ Generated | [Composition-dischargesummary-thompson-alex-20251101.json](Composition-dischargesummary-thompson-alex-20251101.json) |
| DocumentReference | Discharge Summary (DS-2025-11-013), same identifier as the Composition above — wraps a PDF rendering of that Composition, produced by concatenating a generated Patient narrative banner with the Composition's own narrative and each section narrative, per FHIR document rendering rules | ✅ Generated | [DocumentReference-dischargesummary-thompson-alex-20251101.json](DocumentReference-dischargesummary-thompson-alex-20251101.json) (attachment PDF also saved standalone as [Discharge Summary - Alex Thompson - 2025-11-01.pdf](Discharge%20Summary%20-%20Alex%20Thompson%20-%202025-11-01.pdf)) |
| MedicationRequest | Discharge meds – Ibuprofen x5 days | ✅ Generated | [MedicationRequest-ibuprofen-discharge-thompson-alex-20251101.json](MedicationRequest-ibuprofen-discharge-thompson-alex-20251101.json) |
| MedicationRequest | Discharge meds – Paracetamol x5 days | ✅ Generated | [MedicationRequest-paracetamol-discharge-thompson-alex-20251101.json](MedicationRequest-paracetamol-discharge-thompson-alex-20251101.json) |
| CarePlan | Follow-up plan (heating pad, no lifting >5 kg, GP in 7 days) | ⏳ Not yet generated | — |
| Appointment | Follow-up – GP (2025-11-08, identifier synthesised — see Pending / Placeholder Data) | ✅ Generated | [Appointment-followupgp-thompson-alex-20251108.json](Appointment-followupgp-thompson-alex-20251108.json) |
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
| IHI | 9876-5432-1098-7654 | *Yes |
| MEDICARE NO | 2345 678 901 1 | *Yes |
| Address (Patient) | 42 Macquarie St, Bathurst, NSW 2795 | No |
| Shared Care Plan ID | SCP-2025-10-003 | *Yes |
| Medication Update ID | MED-2025-11-014 | *Yes |
| Updated Medications | Ibuprofen 400 mg every 6–8 hours PRN (max 2.4 g/day) x5 days; Paracetamol 500 mg every 6 hours PRN (max 4 g/day) x5 days, over-the-counter Sertraline 100 mg 1 tablet each morning;  Ibuprofen 400 mg every 6-8 hours PRN (max 3/day);  Short course of Oxycodone 5mg PRN (max 4/day) x 3 days; Paracetamol 500 mg every 6 hours PRN (max 4/day) | *Yes |
| CDS Alert | Check: Ibuprofen + Sertraline (SSRI); Red Flag: GI bleeding risk | *Yes |
| Pharmacist Notes ID | NOTE-2025-11-015 | *Yes |
| Notes Details | Counselling: Take Ibuprofen with food; Alternate with Paracetamol;  Stop date: 2025-11-06; Counselling – 10 tablets only supplied for Oxycodone take only if pain is intense; If oxycodone not necessary, take Ibuprofen with food and alternate with Paracetamol Heating pad, hydration advised; Watch: Nausea, rash | *Yes |
| Dispense Event ID | DISP-2025-11-016 | *Yes |
| Dispense Details | Dispensed: 25 tablets Ibuprofen, 10 tablets Oxycodone, 20 tablets Paracetamol; Date: 2025-11-02 | *Yes |
| Notification Recipients | GP (Dr. Jane Smith, HPI-I: 5555-6666-7777-8888), Surgeon (Dr. Mark Wilson, HPI-I: 3434-5656-7878-9090) | *Yes |
| MyHealth App View | Med List Start/Stop dates; Counselling: “Alternate Ibuprofen/Paracetamol, use heating pad”; Reminders: Set | *Yes |
| Provider Organisation | Bathurst Community Pharmacy (HPI-O: 8888-9999-0000-1111) | *Yes |
| Organisation Address | 15 Keppel St, Bathurst, NSW 2795 | No |
| Clinician | Ms. Sarah Lee (Pharmacist, HPI-I: 4545-6767-8989-0101) | *Yes |

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
| MedicationDispense | Ibuprofen (Nurofen Double Strength) 24 tablets — one standard retail pack, covering the revised 5-day/max-3-per-day course; corrected from the story's "25 tablets" (DISP-2025-11-016, see Change Log) | ✅ Generated | [MedicationDispense-ibuprofen-thompson-alex-20251102.json](MedicationDispense-ibuprofen-thompson-alex-20251102.json) |
| MedicationDispense | Oxycodone 10 tablets (DISP-2025-11-016, no authorizing prescription reference — see Pending / Placeholder Data) | ✅ Generated | [MedicationDispense-oxycodone-thompson-alex-20251102.json](MedicationDispense-oxycodone-thompson-alex-20251102.json) |
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
| IHI | 9876-5432-1098-7654 | *Yes |
| MEDICARE NO | 2345 678 901 1 | *Yes |
| Address (Patient) | 42 Macquarie St, Bathurst, NSW 2795 | No |
| eReferral ID (Physio) | REF-2025-11-017 | *Yes |
| eReferral ID (Counselling) | REF-2025-11-018 | *Yes |
| Booking ID (Physio) | BOOK-2025-11-019 | *Yes |
| Physio Details | Pelvic-Health Physio: 2025-11-10, 14:00 PM, Bathurst Physio Centre (HPI-O: 9999-0000-1111-2222); Balance Training: 2025-10-09, 14:00 PM; Transport: Confirmed digitally; Prep: Wear comfortable clothing | *Yes |
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
| Provider Access | Limited: Physio (observations), Counselling (mental health); HPI-O: 9999-0000-1111-2222 (Physio Centre) | No |
| Provider Organisation | Bathurst Physio Centre (HPI-O: 9999-0000-1111-2222) | *Yes |
| Organisation Address | 30 William St, Bathurst, NSW 2795 | No |
| Clinician (Physio) | Ms. Sarah Evans (Physiotherapist, HPI-I: 5656-7878-9090-1212) | *Yes |
| Clinician (Counselling) | Dr. Rachel Patel (Counsellor, HPI-I: 6767-8989-0101-2323) | *Yes |

### FHIR Resources – Allied Health (Physiotherapy & Counselling)

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Patient | Alex Thompson | ✅ Generated | [Patient-thompson-alex.json](Patient-thompson-alex.json) |
| ServiceRequest | eReferral – Physio (REF-2025-11-017) | ✅ Generated | [ServiceRequest-referral-physio-thompson-alex-20251101.json](ServiceRequest-referral-physio-thompson-alex-20251101.json) |
| ServiceRequest | eReferral – Counselling (REF-2025-11-018) | ✅ Generated | [ServiceRequest-referral-counselling-thompson-alex-20251101.json](ServiceRequest-referral-counselling-thompson-alex-20251101.json) |
| Appointment | Physio booking (BOOK-2025-11-019) — shared with Section 4's follow-up appointments | ✅ Generated | [Appointment-followupphysio-thompson-alex-20251110.json](Appointment-followupphysio-thompson-alex-20251110.json) |
| Appointment | Counselling booking (BOOK-2025-11-020), Telehealth — shared with Section 4 | ✅ Generated | [Appointment-followupcounselling-thompson-alex-20251115.json](Appointment-followupcounselling-thompson-alex-20251115.json) |
| Encounter | Pelvic-health physio visit, 2025-11-10 — the story's "Balance Training: 2025-10-09" entry predates the physio eReferral (2025-11-01) and isn't modelled, see Change Log | ✅ Generated | [Encounter-physiovisit-thompson-alex-20251110.json](Encounter-physiovisit-thompson-alex-20251110.json) |
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
| Provider Organisation | Australian Institute of Health and Welfare (HPI-O: 0000-1111-2222-3333) | *Yes |
| Organisation Address | 1 Oxford St, Canberra, ACT 2601 | No |

### FHIR Resources – Population Health / Analytics

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Organization | Australian Institute of Health and Welfare | ⏳ Not yet generated | — |

> This section describes a de-identified, aggregated population-health view rather than per-patient data — it wouldn't produce Patient-linked clinical resources; a `Measure`/`MeasureReport` pair would be the more natural fit if we model it at all.


## Pending / Placeholder Data

This data set contains IHI, MEDICARE NO, HPI-O, and HPI-I values throughout (patient demographics at the top of every section table, and every "Provider Organisation" / "Clinician" row). **These are placeholder numbers, not valid identifiers**, and have been ignored when building the connected-care FHIR resources — Patient, Organization, Practitioner, and PractitionerRole resources in this set currently carry no `identifier` values for these.

Once real test IHI, Medicare, HPI-O, and HPI-I numbers are available, both this document and the corresponding FHIR resources will need to be updated to include them.

`Bundle-aups-thompson-alex-20251009.json` is a fully self-contained AU Patient Summary (AU PS) document Bundle — the Composition, Patient, custodian Organization, Device, Practitioner/PractitionerRole, Encounter, and every section entry (Condition, AllergyIntolerance, MedicationStatement, DiagnosticReport, 3 vital-sign Observations) are embedded inline with `urn:uuid` references, matching the official au-fhir-ps example pattern, rather than pointing back at the standalone connected-care files. Three judgment calls on scope:

1. The embedded `Patient` carries no `identifier`, consistent with this data set's no-placeholder-IHI policy above — this makes it technically non-conformant with AU PS's strengthened `Patient.identifier` cardinality until a real/placeholder IHI is agreed.
2. Secondary references reached *through* an embedded entry (the DiagnosticReport's `performer`/Bathurst Pathology and `basedOn`/the ServiceRequest) were left as plain relative references to the existing standalone files rather than also being embedded, to avoid the embedding requirement cascading through the whole data set.
3. `Composition.author` is a `Device` ("Bathurst Medical Centre Clinical Information System"), not Dr. Lee's PractitionerRole — this AU PS document is presented as system-generated (auto-compiled from the practice's records at the time of the consultation), matching the "autogen" pattern shown in the AU PS `Joyce 07 November 2024` example. `PractitionerRole/generalpractitioner-lee-chris` (Dr. Chris Lee) is still embedded and used elsewhere (e.g. as `Condition.recorder`/`asserter` and `Observation.performer`), just not as the document author. The `Device` resource's identifier, manufacturer, and model are fictional placeholders.

`Bundle-aups-specialist-thompson-alex-20251101.json` is a second, separate AU PS document Bundle — curated by Dr. Chen (Ashfield Private Clinic) rather than Dr. Lee, reflecting what's known once the histopathology result is back. It's dated 2025-11-01, not immediately after the 2025-10-20 result — that's when the full plan of care (cone biopsy day-surgery request, both allied-health eReferrals, hospital booking) had actually been arranged, so the Plan of Care section isn't referencing anything that didn't exist yet at the document's date. A few scope notes specific to this bundle:

1. `Composition.author` is Dr. Chen's `PractitionerRole` directly, not a `Device` — unlike the GP's "autogen" AU PS above, this document is presented as personally curated by the specialist after reviewing the histopathology result, so no `Device` resource is embedded in this bundle.
2. Vital Signs is omitted entirely (not included as an empty section) — no vitals were captured at the specialist encounter.
3. The embedded `Condition`'s `encounter` and `recorder`/`asserter` still point to the original GP consultation and Dr. Lee (external relative references, not embedded) — the diagnosis was originally recorded there, not at the specialist visit, and re-pointing it to this bundle's encounter/author would misrepresent when it was actually made. A `note` was added noting the biopsy-confirmed CIN2/3 and planned cone biopsy.
4. Plan of Care is text-narrative only, with no `entry` array, per the request — the cone biopsy day-surgery ServiceRequest and the two allied-health ServiceRequests aren't linked as coded entries, only described in the section text alongside the hospital Appointment.
5. The histopathology `DiagnosticReport`'s `performer` is the embedded Ashfield Private Clinic `Organization` (reusing the custodian's `urn:uuid`, since it's the same organisation) rather than an external reference, since it's already embedded in this bundle for other reasons.

The peri-operative `Encounter-periop-thompson-alex-20251101.json` carries no `identifier` (the story's PERI-2025-11-012 notes ID isn't represented as a coded value). `Encounter.appointment` links it to the hospital booking `Appointment` (BOOK-2025-11-009), but the three follow-up `Appointment`s (GP, Physio, Counselling) deliberately do **not** reference this encounter — they're separate future bookings arising from the discharge plan, not part of the admission itself.

The GP follow-up `Appointment` (2025-11-08) uses a synthesised Booking ID (BOOK-2025-11-008) — the source story data doesn't give one for this appointment (unlike the Physio and Counselling follow-ups, which reuse the real BOOK-2025-11-019/BOOK-2025-11-020 values given in Section 6).

The GP consultation's "Alcohol use: Occasional (2 standard drinks/week)" vital is not modelled as an Observation — AU Core does not currently carry an Alcohol Status profile in the current published (v2.0.0) or ballot (v3.0.0-ballot1) releases (it existed only in older preview builds, which this data set avoids). Weight, blood pressure, and heart rate are generated; alcohol use can be added if/when AU Core reintroduces the profile.

For business identifiers that require an AU Base Local Identifier profile (e.g. `identifier.system` on a ServiceRequest/DiagnosticReport, per the [Local Identifier](https://implementer.digitalhealth.gov.au/namespaces/browse-identifiers.html) namespace pattern, where `system` is mandatory), the assigning organisation's real HPI-O is not yet known. Rather than omitting `system` (which the AU Base Local Identifier profile requires), these use a literal `{{hpio}}` placeholder in place of the HPI-O segment of the namespace, e.g. `http://ns.electronichealth.net.au/id/hpio-scoped/order/1.0/{{hpio}}`. Search for `{{hpio}}` across the data set to find every identifier needing a real HPI-O substituted in later.

The two eScript `MedicationRequest` identifiers use the `http://ns.electronichealth.net.au/id/hpio-scoped/prescription/1.0/{{hpio}}` namespace specifically (the prescription-scoped variant, distinct from the order-scoped one used elsewhere), per the [hpio-scoped/prescription/1.0](https://implementer.digitalhealth.gov.au/namespaces/id/hpio-scoped/prescription/1.0/index.html) namespace.

The `Appointment-hospitalbooking-thompson-alex-20251101.json` identifier (BOOK-2025-11-009) does **not** use the `hpio-scoped/order/1.0` namespace like the ServiceRequest/DiagnosticReport placer/filler identifiers elsewhere in this data set — a booking ID is a local scheduling reference, not an order/requisition number, so the ADHA order-scoped namespace doesn't fit. Instead its `identifier.system` is a fictional practice-organisation URI, `http://ashfieldprivatehospital.example.org/id/booking`, following the same pattern already used for the `Device` identifier in the AU PS Bundle (`http://bathurstmedicalcentre.example.net/id/cis`) — a locally-assigned system URI scoped to the organisation, not an ADHA namespace. This should be revisited once Ashfield Private Hospital's real PAS/booking-system identifier namespace is known.

The histopathology `DiagnosticReport`'s `performer` (and its `ServiceRequest`'s identifier `assigner`) is recorded as Ashfield Private Clinic — a simplification, since the source story data doesn't name the anatomical pathology laboratory that would actually process a biopsy specimen for a Sydney-area specialist (unlike Section 1, where Bathurst Pathology is named explicitly). This should be revisited if/when a specific lab is identified for this part of the story.

The three `MedicationDispense` resources (Ibuprofen, Paracetamol, Oxycodone) use a `contained` `Medication` resource with `medicationReference`, coded at Trade Product Pack (TPP) level with the `medication-type` extension (`BPDSF`, "Branded product with strengths and form") — Nurofen Double Strength ibuprofen 400 mg tablet, 24 (`930613011000036109`), Panadol 500 mg tablet, 20 (`56245011000036101`), and Endone 5 mg tablet, 10 (`1496631000168100`) — reflecting that a real dispense event knows the specific manufactured product, pack, and manufacturer supplied, unlike the generic prescriptions/statements upstream. `MedicationRequest`/`MedicationStatement` resources remain at generic/ingredient level (unchanged), consistent with how interaction checking (e.g. the Ibuprofen + Sertraline CDS alert) operates on active ingredient rather than brand.

The five Section 6 allied-health `Observation`s (`Observation-pelvicfloorstrength-thompson-alex-20251110.json`, `Observation-painscore-physio-thompson-alex-20251110.json`, `Observation-mobility-thompson-alex-20251110.json`, `Observation-phq9-thompson-alex-20251115.json`, `Observation-anxietylevel-thompson-alex-20251115.json`) carry no `meta.profile` — AU Core's Observation profiles only cover specific vital-sign/pathology categories (blood pressure, body weight, heart rate, smoking status, etc.), with no profile for functional/psychometric assessment scores like a Modified Oxford Scale, a 0-10 pain score, PHQ-9, or a qualitative anxiety level. These use plain base FHIR R4 `Observation` with verified LOINC/SNOMED codes (LOINC 72514-3 for pain score, LOINC 44261-6 for PHQ-9, LOINC 54522-8 for mobility, SNOMED 249957003 for the Oxford muscle-power scale, SNOMED 405051006/61387006 for anxiety level).

`MedicationDispense-oxycodone-thompson-alex-20251102.json` has no `authorizingPrescription` — the source story data doesn't give a separate order/eScript ID for the Oxycodone short course (unlike the Ibuprofen/Paracetamol dispenses, which reference the existing discharge `MedicationRequest`s). A `MedicationRequest` for the Oxycodone prescription should be built once/if an identifier or prescriber is confirmed for it.

`DocumentReference-dischargesummary-thompson-alex-20251101.json` wraps a real PDF (base64-encoded in `content[0].attachment.data`), rendered by concatenating a Patient narrative banner with `Composition-dischargesummary-thompson-alex-20251101.json`'s own narrative and each of its section narratives, per FHIR document rendering rules. The Patient narrative banner is generated on the fly for this rendering only — `Patient-thompson-alex.json` itself still carries no `text.div`. The two resources share the same business identifier (DS-2025-11-013) but there is no direct FHIR reference from the `DocumentReference` back to the `Composition`.


## Change Log

Changes made to this data set while building the connected-care FHIR test data, kept here for reconciliation with the original story owner.

| Date | Change | Reason |
| --- | --- | --- |
| 2026-08-12 | Renamed "Sydney Private Clinic" (Dr. Emily Chen) to **Ashfield Private Clinic**; address updated from 100 George St, Sydney, NSW 2000 to 12 Roberts St, Ashfield, NSW 2131 | Aligned to the existing Organization already generated from the Services Australia providers/orgs sheet, so Dr. Chen's PractitionerRole didn't need a second, duplicate clinic |
| 2026-08-12 | Renamed "Sydney Private Hospital" (Dr. Mark Wilson) to **Ashfield Private Hospital**; address updated from 50 Pitt St, Sydney, NSW 2000 to 63 Victoria St, Ashfield, NSW 2131 | Same reason — aligns to the existing Organization for Dr. Wilson |
| 2026-08-12 | Section 3 lists "Hospital Booking ID: BOOK-2025-10-009" while Section 4 lists "Booking ID: BOOK-2025-11-009" for what is clearly the same Ashfield Private Hospital day-surgery admission on 2025-11-01. A single `Appointment` resource was built using **BOOK-2025-11-009** (the Section 4 value, which also supplies the 8:00 AM time) | Likely a typo in the source spreadsheet's Section 3 row; using one Appointment resource avoids duplicating the same real-world booking |
| 2026-08-12 | Built a `ServiceRequest` (REQ-2025-11-009) authorising the cone biopsy day surgery that `Appointment-hospitalbooking-thompson-alex-20251101.json` is `basedOn` — this identifier value is **synthesised**, not sourced from the spreadsheet | The story data gives a Hospital Booking ID for the appointment but no separate request/order ID for the surgery itself; a `ServiceRequest` is still needed so the Appointment has something to be `basedOn` |
| 2026-08-13 | `MedicationDispense-ibuprofen-thompson-alex-20251102.json` quantity changed from the story's **25 tablets** to **24 tablets** | 25 doesn't match either real Nurofen Double Strength pack size (12 or 24); a single 24-pack covers the revised 5-day course (max 3 tablets/day = 15 tablets) and matches the real Trade Product Pack, `930613011000036109` |
| 2026-08-13 | Section 6's "Balance Training: 2025-10-09, 14:00 PM" (within the Physio Details field) is not modelled as a separate `Encounter` | This date predates the physio eReferral (2025-11-01) and hospital admission (2025-11-01) entirely — likely a stray/templated entry in the source spreadsheet, not a real event in Alex's pathway. Only the 2025-11-10 pelvic-health physio visit is built |
| 2026-08-19 | Ashfield Private Hospital's address updated from **63 Victoria St** to **70 Victoria St**, Ashfield, NSW 2131 | Services Australia registered the organisation with this address in their test data |
