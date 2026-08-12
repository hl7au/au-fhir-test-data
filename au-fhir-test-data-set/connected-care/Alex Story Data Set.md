# Data Set for Alex’s Story

## Change Log

Changes made to this data set while building the connected-care FHIR test data, kept here for reconciliation with the original story owner.

| Date | Change | Reason |
| --- | --- | --- |
| 2026-08-12 | Renamed "Sydney Private Clinic" (Dr. Emily Chen) to **Ashfield Private Clinic**; address updated from 100 George St, Sydney, NSW 2000 to 12 Roberts St, Ashfield, NSW 2131 | Aligned to the existing Organization already generated from the Services Australia providers/orgs sheet, so Dr. Chen's PractitionerRole didn't need a second, duplicate clinic |
| 2026-08-12 | Renamed "Sydney Private Hospital" (Dr. Mark Wilson) to **Ashfield Private Hospital**; address updated from 50 Pitt St, Sydney, NSW 2000 to 63 Victoria St, Ashfield, NSW 2131 | Same reason — aligns to the existing Organization for Dr. Wilson |

## Pending / Placeholder Data

This data set contains IHI, MEDICARE NO, HPI-O, and HPI-I values throughout (patient demographics at the top of every section table, and every "Provider Organisation" / "Clinician" row). **These are placeholder numbers, not valid identifiers**, and have been ignored when building the connected-care FHIR resources — Patient, Organization, Practitioner, and PractitionerRole resources in this set currently carry no `identifier` values for these.

Once real test IHI, Medicare, HPI-O, and HPI-I numbers are available, both this document and the corresponding FHIR resources will need to be updated to include them.

The GP consultation's "Alcohol use: Occasional (2 standard drinks/week)" vital is not modelled as an Observation — AU Core does not currently carry an Alcohol Status profile in the current published (v2.0.0) or ballot (v3.0.0-ballot1) releases (it existed only in older preview builds, which this data set avoids). Weight, blood pressure, and heart rate are generated; alcohol use can be added if/when AU Core reintroduces the profile.

For business identifiers that require an AU Base Local Identifier profile (e.g. `identifier.system` on a ServiceRequest/DiagnosticReport, per the [Local Identifier](https://implementer.digitalhealth.gov.au/namespaces/browse-identifiers.html) namespace pattern, where `system` is mandatory), the assigning organisation's real HPI-O is not yet known. Rather than omitting `system` (which the AU Base Local Identifier profile requires), these use a literal `{{hpio}}` placeholder in place of the HPI-O segment of the namespace, e.g. `http://ns.electronichealth.net.au/id/hpio-scoped/order/1.0/{{hpio}}`. Search for `{{hpio}}` across the data set to find every identifier needing a real HPI-O substituted in later.

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
| Patient | Alex Thompson | ✅ Generated | `Patient-thompson-alex.json` |
| Organization | National Cancer Screening Register | ⏳ Not yet generated | — |
| *Unresolved* | Reminder: Cervical Screening overdue — no AU Core resource identified yet (not a Communication, since AU Core doesn't include that resource; needs a decision) | ⏳ Not yet generated | — |
| ServiceRequest | Cervical Screening e-Request (REQ-2025-10-001) | ✅ Generated | `ServiceRequest-cervicalscreening-thompson-alex-20250930.json` |
| Task (eRequesting fulfilment) | Fulfilment task for the Cervical Screening e-Request (REQ-2025-10-001), owned by Bathurst Pathology | ✅ Generated | `Task-taskfulfilment-cervicalscreening-thompson-alex-20250930.json` |
| Organization | Bathurst Pathology | ✅ Generated | `Organization-bathurst-pathology.json` |
| Location | Bathurst Pathology | ✅ Generated | `Location-bathurst-pathology.json` |
| HealthcareService | Bathurst Pathology – Pathology laboratory service | ✅ Generated | `HealthcareService-pathologylaboratoryservice-bathurst-pathology.json` |
| Appointment | Bathurst Pathology booking (BOOK-2025-10-000) | ⏳ Not yet generated | — |
| Practitioner | Dr. Chris Lee | ✅ Generated | `Practitioner-lee-chris.json` |
| PractitionerRole | Dr. Chris Lee – GP, Bathurst Medical Centre | ✅ Generated | `PractitionerRole-generalpractitioner-lee-chris.json` |
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
| Patient | Alex Thompson | ✅ Generated | `Patient-thompson-alex.json` |
| ServiceRequest | Cervical Screening e-Request (REQ-2025-10-001) | ✅ Generated | `ServiceRequest-cervicalscreening-thompson-alex-20250930.json` |
| Task (eRequesting fulfilment) | Fulfilment task for the Cervical Screening e-Request (REQ-2025-10-001), owned by Bathurst Pathology | ✅ Generated | `Task-taskfulfilment-cervicalscreening-thompson-alex-20250930.json` |
| DiagnosticReport | HPV pathology result (PATH-2025-10-002), high-risk HPV / CIN2/3 | ✅ Generated | `DiagnosticReport-hpvpathology-thompson-alex-20251008.json` |
| Organization | Bathurst Pathology | ✅ Generated | `Organization-bathurst-pathology.json` |
| Location | Bathurst Pathology | ✅ Generated | `Location-bathurst-pathology.json` |
| HealthcareService | Bathurst Pathology – Pathology laboratory service | ✅ Generated | `HealthcareService-pathologylaboratoryservice-bathurst-pathology.json` |
| Practitioner | Sally Johnson | ✅ Generated | `Practitioner-johnson-sally.json` |
| PractitionerRole | Sally Johnson – Phlebotomist, Bathurst Pathology | ✅ Generated | `PractitionerRole-phlebotomist-johnson-sally.json` |

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
| Patient | Alex Thompson | ✅ Generated | `Patient-thompson-alex.json` |
| AllergyIntolerance | Penicillin (anaphylaxis) — pre-existing, unrelated to this encounter | ✅ Generated | `AllergyIntolerance-penicillin-thompson-alex.json` |
| MedicationStatement | No active medications — pre-existing, unrelated to this encounter | ✅ Generated | `MedicationStatement-nomedications-thompson-alex.json` |
| Condition | High-risk cervical screening (high-risk HPV / CIN2/3) | ✅ Generated | `Condition-highriskhpv-thompson-alex.json` |
| Encounter | GP consultation, 2025-10-09 | ✅ Generated | `Encounter-gpconsultation-thompson-alex-20251009.json` |
| Composition (Encounter Summary) | GP consultation summary, 2025-10-09 — pending the emerging AU Encounter Summary IG (alongside AU Patient Summary) | ⏳ Not yet generated | — |
| Observation | Weight | ✅ Generated | `Observation-bodyweight-thompson-alex-20251009.json` |
| Observation | Blood pressure (systolic/diastolic) | ✅ Generated | `Observation-bloodpressure-thompson-alex-20251009.json` |
| Observation | Heart rate | ✅ Generated | `Observation-heartrate-thompson-alex-20251009.json` |
| CarePlan | Shared Care Plan (SCP-2025-10-003) | ⏳ Not yet generated | — |
| QuestionnaireResponse | GP Chronic Condition Management Plan (GP CCMP), per the [AEHRC GP CCMP FHIR IG](https://build.fhir.org/ig/aehrc/gpccmp-fhir-ig/branches/master/StructureDefinition-GPCCMPQuestionnaireResponse.html) — supports the Shared Care Plan | ⏳ Not yet generated | — |
| ServiceRequest | e-Referral to Gynaecologist (REF-2025-10-004) | ✅ Generated | `ServiceRequest-referral-gynaecologist-thompson-alex-20251009.json` |
| Composition (AU Patient Summary) | Patient Summary sent with the e-Referral to Dr. Emily Chen | ⏳ Not yet generated | — |
| Organization | Bathurst Medical Centre | ✅ Generated | `Organization-bathurst-medical-centre.json` |
| Location | Bathurst Medical Centre | ✅ Generated | `Location-bathurst-medical-centre.json` |
| HealthcareService | Bathurst Medical Centre – General medical practitioner service | ✅ Generated | `HealthcareService-generalmedicalpractitionerservice-bathurst-medical-centre.json` |
| Practitioner | Dr. Chris Lee | ✅ Generated | `Practitioner-lee-chris.json` |
| PractitionerRole | Dr. Chris Lee – GP, Bathurst Medical Centre | ✅ Generated | `PractitionerRole-generalpractitioner-lee-chris.json` |
| Practitioner | Dr. Jane Smith | ✅ Generated | `Practitioner-smith-jane.json` |
| PractitionerRole | Dr. Jane Smith – GP, Bathurst Medical Centre | ✅ Generated | `PractitionerRole-generalpractitioner-smith-jane.json` |
| Practitioner | Dr. Emily Chen | ✅ Generated | `Practitioner-chen-emily.json` |
| PractitionerRole | Dr. Emily Chen – Gynaecologist, Ashfield Private Clinic | ✅ Generated | `PractitionerRole-obstetricianandgynaecologist-chen-emily.json` |

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
| Patient | Alex Thompson | ✅ Generated | `Patient-thompson-alex.json` |
| ServiceRequest | Colposcopy with Biopsy, requested (REQ-2025-10-005) | ⏳ Not yet generated | — |
| MedicationRequest | Ibuprofen 400 mg PRN (eScript SCR-2025-10-006) | ⏳ Not yet generated | — |
| MedicationRequest | Paracetamol 500 mg PRN (eScript SCR-2025-10-006) | ⏳ Not yet generated | — |
| DiagnosticReport | Histopathology result (PATH-2025-10-007), CIN2/3 confirmed | ⏳ Not yet generated | — |
| Encounter | Multidisciplinary meeting / specialist decision encounter (MDM-2025-10-008) | ⏳ Not yet generated | — |
| Appointment | Ashfield Private Hospital booking (BOOK-2025-10-009) | ⏳ Not yet generated | — |
| QuestionnaireResponse | SMART Form consent (FORM-2025-10-010) | ⏳ Not yet generated | — |
| ServiceRequest | Allied health eReferral – Physio (REF-2025-11-017) | ⏳ Not yet generated | — |
| ServiceRequest | Allied health eReferral – Counselling (REF-2025-11-018) | ⏳ Not yet generated | — |
| Organization | Ashfield Private Clinic | ✅ Generated | `Organization-ashfield-private-clinic.json` |
| Location | Ashfield Private Clinic | ✅ Generated | `Location-ashfield-private-clinic.json` |
| HealthcareService | Ashfield Private Clinic – Specialist medical clinic service | ✅ Generated | `HealthcareService-specialistmedicalclinicservice-ashfield-private-clinic.json` |
| Organization | Ashfield Private Hospital | ✅ Generated | `Organization-ashfield-private-hospital.json` |
| Location | Ashfield Private Hospital | ✅ Generated | `Location-ashfield-private-hospital.json` |
| HealthcareService | Ashfield Private Hospital – Private acute care hospital | ✅ Generated | `HealthcareService-privateacutecarehospital-ashfield-private-hospital.json` |
| Practitioner | Dr. Emily Chen | ✅ Generated | `Practitioner-chen-emily.json` |
| PractitionerRole | Dr. Emily Chen – Gynaecologist, Ashfield Private Clinic | ✅ Generated | `PractitionerRole-obstetricianandgynaecologist-chen-emily.json` |

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
| Organisation Address | 63 Victoria St, Ashfield, NSW 2131 | No |
| Clinician | Dr. Mark Wilson (Surgeon, HPI-I: 3434-5656-7878-9090) | *Yes |

### FHIR Resources – Private Hospital (Theatre / Inpatient)

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Patient | Alex Thompson | ✅ Generated | `Patient-thompson-alex.json` |
| Composition (AU Patient Summary) | Patient Summary retrieved by Ashfield Private Hospital at admission (not sent with the referral — pulled independently, e.g. via provider access) | ⏳ Not yet generated | — |
| Appointment | Hospital booking (BOOK-2025-11-009) | ⏳ Not yet generated | — |
| QuestionnaireResponse | SMART Form pre-admission (FORM-2025-11-011) | ⏳ Not yet generated | — |
| Procedure | Cone Biopsy (Day Surgery) | ⏳ Not yet generated | — |
| Encounter | Peri-operative encounter (PERI-2025-11-012) | ⏳ Not yet generated | — |
| DocumentReference | Discharge Summary (DS-2025-11-013) | ⏳ Not yet generated | — |
| MedicationRequest | Discharge meds – Ibuprofen x5 days | ⏳ Not yet generated | — |
| MedicationRequest | Discharge meds – Paracetamol x5 days | ⏳ Not yet generated | — |
| CarePlan | Follow-up plan (heating pad, no lifting >5 kg, GP in 7 days) | ⏳ Not yet generated | — |
| Appointment | Follow-up – GP (2025-11-08) | ⏳ Not yet generated | — |
| Appointment | Follow-up – Physio (2025-11-10) | ⏳ Not yet generated | — |
| Appointment | Follow-up – Counselling (2025-11-15) | ⏳ Not yet generated | — |
| Organization | Ashfield Private Hospital | ✅ Generated | `Organization-ashfield-private-hospital.json` |
| Location | Ashfield Private Hospital | ✅ Generated | `Location-ashfield-private-hospital.json` |
| HealthcareService | Ashfield Private Hospital – Private acute care hospital | ✅ Generated | `HealthcareService-privateacutecarehospital-ashfield-private-hospital.json` |
| Practitioner | Dr. Mark Wilson | ✅ Generated | `Practitioner-wilson-mark.json` |
| PractitionerRole | Dr. Mark Wilson – Surgeon, Ashfield Private Hospital | ✅ Generated | `PractitionerRole-surgeon-wilson-mark.json` |

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
| Patient | Alex Thompson | ✅ Generated | `Patient-thompson-alex.json` |
| Composition (AU Patient Summary) | Patient Summary viewed by Bathurst Community Pharmacy as part of medication review | ⏳ Not yet generated | — |
| CarePlan | Shared Care Plan (SCP-2025-10-003) | ⏳ Not yet generated | — |
| MedicationRequest / MedicationStatement | Updated medication list (MED-2025-11-014) | ⏳ Not yet generated | — |
| Encounter | Pharmacy counselling encounter — Ibuprofen/Sertraline interaction check, dosing counselling, red-flag advice (NOTE-2025-11-015) | ⏳ Not yet generated | — |
| MedicationDispense | Ibuprofen 25 tablets (DISP-2025-11-016) | ⏳ Not yet generated | — |
| MedicationDispense | Oxycodone 10 tablets (DISP-2025-11-016) | ⏳ Not yet generated | — |
| MedicationDispense | Paracetamol 20 tablets (DISP-2025-11-016) | ⏳ Not yet generated | — |
| Organization | Bathurst Community Pharmacy | ✅ Generated | `Organization-bathurst-community-pharmacy.json` |
| Location | Bathurst Community Pharmacy | ✅ Generated | `Location-bathurst-community-pharmacy.json` |
| HealthcareService | Bathurst Community Pharmacy | ✅ Generated | `HealthcareService-communitypharmacy-bathurst-community-pharmacy.json` |
| Practitioner | Sarah Lee | ✅ Generated | `Practitioner-lee-sarah.json` |
| PractitionerRole | Sarah Lee – Pharmacist, Bathurst Community Pharmacy | ✅ Generated | `PractitionerRole-retailpharmacist-lee-sarah.json` |

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
| Patient | Alex Thompson | ✅ Generated | `Patient-thompson-alex.json` |
| ServiceRequest | eReferral – Physio (REF-2025-11-017) | ⏳ Not yet generated | — |
| ServiceRequest | eReferral – Counselling (REF-2025-11-018) | ⏳ Not yet generated | — |
| Appointment | Physio booking (BOOK-2025-11-019) | ⏳ Not yet generated | — |
| Appointment | Counselling booking (BOOK-2025-11-020), Telehealth | ⏳ Not yet generated | — |
| Encounter | Pelvic-health physio visit, 2025-11-10 (+ balance training, 2025-10-09) | ⏳ Not yet generated | — |
| Observation | Physio measures – pelvic floor strength, pain score, mobility (OBS-2025-11-021) | ⏳ Not yet generated | — |
| Encounter | Psycho-Oncology counselling, Telehealth, 2025-11-15 | ⏳ Not yet generated | — |
| Observation | Counselling measures – PHQ-9, anxiety (OBS-2025-11-022) | ⏳ Not yet generated | — |
| Observation | Apple Watch data – heart rate, steps | ⏳ Not yet generated | — |
| CarePlan | Shared Care Plan update (physio exercises, counselling notes) | ⏳ Not yet generated | — |
| Organization | Bathurst Physio Centre | ✅ Generated | `Organization-bathurst-physio-centre.json` |
| Location | Bathurst Physio Centre | ✅ Generated | `Location-bathurst-physio-centre.json` |
| HealthcareService | Bathurst Physio Centre | ✅ Generated | `HealthcareService-physiotherapyservices-bathurst-physio-centre.json` |
| Practitioner | Sarah Evans | ✅ Generated | `Practitioner-evans-sarah.json` |
| PractitionerRole | Sarah Evans – Physiotherapist, Bathurst Physio Centre | ✅ Generated | `PractitionerRole-physiotherapist-evans-sarah.json` |
| Organization | Bathurst Psychology | ✅ Generated | `Organization-bathurst-psychology.json` |
| Location | Bathurst Psychology | ✅ Generated | `Location-bathurst-psychology.json` |
| HealthcareService | Bathurst Psychology | ⏳ Not yet generated (no SNOMED service-type match in Type Codes) | — |
| Practitioner | Dr. Rachel Patel | ✅ Generated | `Practitioner-patel-rachel.json` |
| PractitionerRole | Dr. Rachel Patel – Counsellor, Bathurst Psychology | ✅ Generated | `PractitionerRole-counsellorsnec-patel-rachel.json` |

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
