# Data Set for Yuri's Story

Yuri Petrov is a Kalgoorlie, WA resident whose story traces a connected-care journey from a hypoglycaemic episode in Canberra through to fall prevention and allied health follow-up. It starts with a suspected hypoglycaemia notification via MyHealth App while visiting family in the ACT, which triggers a Healthdirect call and ambulance dispatch. Yuri is admitted to Canberra Hospital, treated for the hypoglycaemic event, and discharged with medication adjustments. Follow-up care involves a local WA nurse practitioner, telehealth endocrinologist consultation, and aged-care services (occupational therapy and physiotherapy) for fall prevention. The journey ultimately feeds into population health analytics on remote/traveller patient outcomes and cross-border handovers.

The data set is organised into 8 steps, each representing a different point of care and the FHIR resources generated for it:

0. [MyHealth App](#0-myhealth-app)
1. [Healthdirect](#1-healthdirect)
2. [Ambulance](#2-ambulance)
3. [ED / Inpatient (ACT)](#3-ed--inpatient-act)
4. [Local Health Service (WA Nurse Practitioner)](#4-local-health-service-wa-nurse-practitioner)
5. [Endocrinologist (WA)](#5-endocrinologist-wa)
6. [Aged-Care Service (WA)](#6-aged-care-service-wa)
7. [Population Health / Analytics](#7-population-health--analytics)

See [Pending / Placeholder Data](#pending--placeholder-data) for known gaps and modelling notes.

## 0. MyHealth App

| Data Field | Actual Data | Critical? |
| --- | --- | --- |
| Patient Name | Yuri Petrov | *Yes |
| Date of Birth | 10/04/1949 | *Yes |
| IHI | 1234-5678-9012-3456 | *Yes |
| MEDICARE NO | 3456 789 012 1 | *Yes |
| Address (Patient, Home) | 17 Goldfields Rd, Kalgoorlie, WA 6430 | No |
| Address (Temporary) | 25 Canberra Ave, Griffith, ACT 2603 | No |
| Family Contact | Sofia Petrov (Daughter); Phone: 0413-456-789; Email: sofia.petrov@email.com | *Yes |
| Consent Management | Access: Sofia granted view-only for ED episode, discharge, bookings; Scope: T2DM management, emergency care; Consent Date: 2025-09-30 | *Yes |
| Notification ID | NOTIF-2025-10-000 | *Yes |
| Notification Details | Alert: ED Admission; Location: Canberra Hospital (HPI-O: 2222-3333-4444-5555); Status: Admitted, suspected hypoglycaemia; Time: 2025-10-01, 15:30 PM; Via: MyHealth App; Note: Possible drug interaction, review meal timing | *Yes |
| ED Episode ID | ED-2025-10-001 | *Yes |
| ED Episode Details | Status: In-progress; Imaging Requested: Hip X-ray; Vitals: Glucose 3.0 mmol/L, BP 135/85 mmHg; Updated: 2025-10-01, 15:40 PM | *Yes |
| Subscription Setup | Recipients: Sofia Petrov (daughter), WA GP (Dr. Ravi Kumar, HPI-I: 4444-5555-6666-7777); Triggers: Admission updates, discharge, bookings | *Yes |
| Discharge Summary ID | DS-2025-10-029 | *Yes |
| Discharge Details | Date: 2025-10-02, 10:00 AM; Diagnosis: Hypoglycaemic episode; Instructions: Monitor glucose, GP follow-up; ensure regular meals | *Yes |
| Follow-Up Booking ID | BOOK-2025-10-031 | *Yes |
| Booking Details | Diabetes Education: Kalgoorlie Community Health Service (HPI-O: 9999-0000-1111-2222), 2025-10-10, 10:00 AM; Prep: Bring glucose monitor | *Yes |
| MyHealth App View | Displays: ED Episode (real-time), Discharge Summary, Bookings; Notifications: Enabled for Sofia (admission, discharge, bookings) | *Yes |
| Provider Organisation | Canberra Hospital (HPI-O: 2222-3333-4444-5555) | *Yes |
| Organisation Address | 1 Hospital Rd, Garran, ACT 2605 | No |
| Clinician | Dr. Susan Green (ED Physician, HPI-I: 0101-2323-4545-6767) | *Yes |

### FHIR Resources – MyHealth App

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Patient | Yuri Petrov | ⏳ Not yet generated | — |
| Organization | Canberra Hospital | ⏳ Not yet generated | — |
| Practitioner | Dr. Susan Green | ⏳ Not yet generated | — |
| PractitionerRole | Dr. Susan Green – ED Physician, Canberra Hospital | ⏳ Not yet generated | — |

## 1. Healthdirect

| Data Field | Actual Data | Critical? |
| --- | --- | --- |
| Patient Name | Yuri Petrov | *Yes |
| Date of Birth | 10/04/1949 | *Yes |
| IHI | 1234-5678-9012-3456 | *Yes |
| MEDICARE NO | 3456 789 012 1 | *Yes |
| Address (Patient) | 17 Goldfields Rd, Kalgoorlie, WA 6430 | No |
| Phone Number | 08-9022-5678 | No |
| Emergency Contact | Daughter: Sofia Petrov, 0413-456-789 | *Yes |
| Call Date/Time | 2025-10-01, 14:30 PM | *Yes |
| Reason for Encounter | Fall after dizzy spell; Suspected hypoglycaemia | *Yes |
| Shared Care Plan ID | SCP-2025-10-023 | *Yes |
| Plan Access | Meds: Metformin 500mg BD, Gliclazide diamicron 60mg; Ramipril 5mg daily, Conditions: T2DM, CKD Stage 3; Non-Med: fall risk assessment, regular meal timing | *Yes |
| Options Discussed | Urgent Care Clinic, GP Helpline, Virtual ED, Ambulance (selected) | *Yes |
| Encounter Summary ID | ENC-2025-10-024 | *Yes |
| Summary Details | Advice: Call ambulance; Symptoms: Dizziness, no injury reported; Notified: GP, Daughter | *Yes |
| Notification Recipients | GP (Dr. Ravi Kumar, HPI-I: 4444-5555-6666-7777), Daughter (Sofia Petrov, MyHealth App) | *Yes |
| Provider Organisation | HealthDirect Australia (HPI-O: 1111-2222-3333-4444) | *Yes |
| Organisation Address | 10 Moore St, Canberra, ACT 2601 | No |
| Clinician | Ms. Linda Hayes (Nurse Practitioner, HPI-I: 7878-9090-1212-3434) | *Yes |

### FHIR Resources – Healthdirect

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Patient | Yuri Petrov | ⏳ Not yet generated | — |
| Encounter | Healthdirect call encounter, 2025-10-01 | ⏳ Not yet generated | — |
| ServiceRequest | Shared Care Plan (SCP-2025-10-023) | ⏳ Not yet generated | — |
| Practitioner | Ms. Linda Hayes | ⏳ Not yet generated | — |
| PractitionerRole | Ms. Linda Hayes – Nurse Practitioner, HealthDirect Australia | ⏳ Not yet generated | — |
| Organization | HealthDirect Australia | ⏳ Not yet generated | — |

## 2. Ambulance

| Data Field | Actual Data | Critical? |
| --- | --- | --- |
| Patient Name | Yuri Petrov | *Yes |
| Date of Birth | 10/04/1949 | *Yes |
| IHI | 1234-5678-9012-3456 | *Yes |
| MEDICARE NO | 3456 789 012 1 | *Yes |
| Address (Temporary) | 25 Canberra Ave, Griffith, ACT 2603 | No |
| AUPS Key Allergies | None known | *Yes |
| AUPS Medications | Metformin 500mg BD, Gliclazide diamicron 60mg; Ramipril 5mg daily | *Yes |
| AUPS Conditions | Type 2 Diabetes, Chronic Kidney Disease Stage 3 | *Yes |
| Dispatch Details | Fall, suspected hypo; Time: 2025-10-01, 15:00 PM; Location: Griffith, ACT | *Yes |
| Reason for Encounter ID | RFE-2025-10-025 | *Yes |
| Vitals Captured | BP: 115/60 mmHg; HR: 119 bpm; Glucose: 3.0 mmol/L | *Yes |
| Pre-Arrival Data ID | PRE-2025-10-026 | *Yes |
| Pre-Arrival Details | Sent: Vitals, AUPS, Reason: Fall/hypo; To: Canberra Hospital ED (HPI-O: 2222-3333-4444-5555) | *Yes |
| Provider Organisation | ACT Ambulance Service (HPI-O: 5555-6666-7777-8888) | *Yes |
| Organisation Address | 15 Hindmarsh Dr, Garran, ACT 2605 | No |
| Clinician | Mr. Tom Bradley (Paramedic, HPI-I: 8989-0101-2323-4545) | *Yes |

### FHIR Resources – Ambulance

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Patient | Yuri Petrov | ⏳ Not yet generated | — |
| Encounter | Ambulance dispatch and transport, 2025-10-01 | ⏳ Not yet generated | — |
| Observation | Vital signs captured (BP, HR, Glucose) | ⏳ Not yet generated | — |
| Practitioner | Mr. Tom Bradley | ⏳ Not yet generated | — |
| PractitionerRole | Mr. Tom Bradley – Paramedic, ACT Ambulance Service | ⏳ Not yet generated | — |
| Organization | ACT Ambulance Service | ⏳ Not yet generated | — |

## 3. ED / Inpatient (ACT)

| Data Field | Actual Data | Critical? |
| --- | --- | --- |
| Patient Name | Yuri Petrov | *Yes |
| Date of Birth | 10/04/1949 | *Yes |
| IHI | 1234-5678-9012-3456 | *Yes |
| MEDICARE NO | 3456 789 012 1 | *Yes |
| Address (Temporary) | 25 Canberra Ave, Griffith, ACT 2603 | No |
| AUPS Access | Meds: Metformin 500mg BD, Gliclazide diamicron 60mg; Ramipril 5mg daily; Conditions: T2DM, CKD | *Yes |
| Pre-Arrival Data ID | PRE-2025-10-026 (Vitals: Glucose 3.0 mmol/L; Reason: Fall) | *Yes |
| Triage Time | Arrival: 2025-10-01, 15:30 PM; Completed: 15:40 PM | *Yes |
| Observations ID | OBS-2025-10-027 | *Yes |
| Observation Details | Imaging: Hip X-ray normal; Glucose: Stabilised to 6.5 mmol/L post-dextrose | *Yes |
| Admission Summary ID | ADMS-2025-10-028 | *Yes |
| Admission Date | 2025-10-01, 16:00 PM | *Yes |
| Discharge Summary ID | DS-2025-10-029 | *Yes |
| Discharge Date | 2025-10-02, 10:00 AM | *Yes |
| Summary Key Points | Diagnosis: Hypoglycaemic episode; Meds: Continue metformin, Ramipril, reduce Gliclazide diamicron to 30mg; Instructions: Monitor glucose, GP follow-up, regular meals, fall prevention education | *Yes |
| Subscription Setup | Notified: GP Dr. Ravi Kumar, (HPI-I: 4444-5555-6666-7777), Aged Care Home Help (HPI-O: 6666-7777-8888-9999), Daughter (Sofia Petrov) | *Yes |
| Provider Organisation | Canberra Hospital (HPI-O: 2222-3333-4444-5555) | *Yes |
| Organisation Address | 1 Hospital Rd, Garran, ACT 2605 | No |
| Clinician | Dr. Susan Green (ED Physician, HPI-I: 0101-2323-4545-6767) | *Yes |

### FHIR Resources – ED / Inpatient (ACT)

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Patient | Yuri Petrov | ⏳ Not yet generated | — |
| Encounter | ED admission and inpatient stay, 2025-10-01 to 2025-10-02 | ⏳ Not yet generated | — |
| Observation | Hip X-ray imaging result | ⏳ Not yet generated | — |
| Observation | Glucose monitoring pre- and post-treatment | ⏳ Not yet generated | — |
| Composition | Discharge Summary (DS-2025-10-029) | ⏳ Not yet generated | — |
| DocumentReference | Discharge Summary PDF | ⏳ Not yet generated | — |
| Organization | Canberra Hospital | ⏳ Not yet generated | — |

## 4. Local Health Service (WA Nurse Practitioner)

| Data Field | Actual Data | Critical? |
| --- | --- | --- |
| Patient Name | Yuri Petrov | *Yes |
| Date of Birth | 10/04/1949 | *Yes |
| IHI | 1234-5678-9012-3456 | *Yes |
| MEDICARE NO | 3456 789 012 1 | *Yes |
| Address (Patient) | 17 Goldfields Rd, Kalgoorlie, WA 6430 | No |
| Discharge Summary ID | DS-2025-10-029 | *Yes |
| AUPS Update | Added: Hypo event (2025-10-01); Glucose trends: Night lows 3.0-3.4 mmol/L | *Yes |
| Glucose Monitor Data | Consent: Via MyHealth App; Last 2 Weeks: Avg 7.0 mmol/L; Lows: 3.0 mmol/L on 2025-09-30 | *Yes |
| Medication Reconciliation | Metformin 500mg BD, Gliclazide diamicron 30mg; Ramipril 5mg daily | *Yes |
| eReferral ID | REF-2025-10-030 | *Yes |
| Referral Details | To: Endocrinologist (telehealth) Dr. Natalie Tench (HPI-I: 1111-2222-3333-4444); Include: Discharge, glucose data; Issued: 2025-10-03 | *Yes |
| Shared Care Plan ID | SCP-2025-10-023 | *Yes |
| Care Plan Updates | Goals: Prevent hypos, fall prevention; Team: NP, GP, Endo, Aged Care; Alerts: Low glucose to daughter; Non-Med: regular meals, home safety | *Yes |
| Booking ID | BOOK-2025-10-031 | *Yes |
| Booking Details | Diabetes Education: 2025-10-10, Kalgoorlie Community Health Service (HPI-O: 9999-0000-1111-2222) | *Yes |
| Subscription Setup | Notified: GP Dr. Ravi Kumar, (HPI-I: 4444-5555-6666-7777), Aged Care Home Help (HPI-O: 6666-7777-8888-9999), Daughter (Sofia Petrov) | *Yes |
| Provider Organisation | Kalgoorlie Community Health Service (HPI-O: 9999-0000-1111-2222) | *Yes |
| Organisation Address | 20 Hannan St, Kalgoorlie, WA 6430 | No |
| Clinician | Ms. Sarah Brown (Nurse Practitioner, HPI-I: 7777-8888-9999-0000) | *Yes |

### FHIR Resources – Local Health Service (WA Nurse Practitioner)

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Patient | Yuri Petrov | ⏳ Not yet generated | — |
| Encounter | NP consultation for post-discharge follow-up | ⏳ Not yet generated | — |
| ServiceRequest | eReferral to Endocrinologist (REF-2025-10-030) | ⏳ Not yet generated | — |
| Observation | Glucose monitoring data | ⏳ Not yet generated | — |
| Practitioner | Ms. Sarah Brown | ⏳ Not yet generated | — |
| PractitionerRole | Ms. Sarah Brown – Nurse Practitioner, Kalgoorlie Community Health Service | ⏳ Not yet generated | — |
| Organization | Kalgoorlie Community Health Service | ⏳ Not yet generated | — |

## 5. Endocrinologist (WA)

| Data Field | Actual Data | Critical? |
| --- | --- | --- |
| Patient Name | Yuri Petrov | *Yes |
| Date of Birth | 10/04/1949 | *Yes |
| IHI | 1234-5678-9012-3456 | *Yes |
| MEDICARE NO | 3456 789 012 1 | *Yes |
| Address (Patient) | 17 Goldfields Rd, Kalgoorlie, WA 6430 | No |
| Discharge Summary ID | DS-2025-10-029 | *Yes |
| Glucose Monitor Data | Last 2 Weeks: Night lows 3.0-3.4 mmol/L; Avg Day: 7.5 mmol/L; Consent: Via MyHealth App | *Yes |
| AUPS Access | Conditions: T2DM, CKD; Meds: Metformin 500mg BD, Gliclazide diamicron 30mg; Ramipril 5mg daily | *Yes |
| Telehealth Appointment | Date: 2025-10-05, 10:00 AM; Support: Aboriginal Health Worker (Ms. Narelle King, HPI-I: 8888-9999-0000-1111) | *Yes |
| Treatment Adjustment ID | TA-2025-10-032 | *Yes |
| Adjustments | Targets: 5-12 mmol/L; eRequest: Bloods (HbA1c, Lipids, eGFR); Monitor: Volume status | *Yes |
| eReferral ID | REF-2025-10-033 | *Yes |
| Referral Details | Pharmacist for medicine review Joy Sullivan (HPI-I: 1234-2424-3535-4646); Include: Discharge, glucose data; Issued: 2025-10-03 | *Yes |
| eRequest ID | REQ-2025-10-033 | *Yes |
| Booking ID | BOOK-2025-10-034 (Diabetes Education, 2025-10-10) | *Yes |
| Shared Care Plan Update | Added: New targets, education, non-med: regular meals exercise plan; Notified: GP, Aged Care, Pharmacy, Daughter (Sofia Petrov) | *Yes |
| Low-Glucose Alerts | Threshold: 4.0 mmol/L; Recipient: Daughter (Sofia Petrov, MyHealth App) | *Yes |
| Provider Organisation | Kalgoorlie Specialist Clinic (HPI-O: 0000-1111-2222-3333) | *Yes |
| Organisation Address | 5 Egan St, Kalgoorlie, WA 6430 | No |
| Clinician | Dr. Natalie Tench (Endocrinologist, HPI-I: 1111-2222-3333-4444) | *Yes |

### FHIR Resources – Endocrinologist (WA)

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Patient | Yuri Petrov | ⏳ Not yet generated | — |
| Encounter | Telehealth endocrinologist consultation, 2025-10-05 | ⏳ Not yet generated | — |
| ServiceRequest | eRequest for bloods (HbA1c, Lipids, eGFR) | ⏳ Not yet generated | — |
| Observation | Treatment adjustment targets and monitoring plan | ⏳ Not yet generated | — |
| Practitioner | Dr. Natalie Tench | ⏳ Not yet generated | — |
| Practitioner | Ms. Narelle King (Aboriginal Health Worker) | ⏳ Not yet generated | — |
| PractitionerRole | Dr. Natalie Tench – Endocrinologist, Kalgoorlie Specialist Clinic | ⏳ Not yet generated | — |
| Organization | Kalgoorlie Specialist Clinic | ⏳ Not yet generated | — |

## 6. Aged-Care Service (WA)

| Data Field | Actual Data | Critical? |
| --- | --- | --- |
| Patient Name | Yuri Petrov | *Yes |
| Date of Birth | 10/04/1949 | *Yes |
| IHI | 1234-5678-9012-3456 | *Yes |
| MEDICARE NO | 3456 789 012 1 | *Yes |
| Address (Patient) | 17 Goldfields Rd, Kalgoorlie, WA 6430 | No |
| Provider Directory Filters | Availability: <48 hours; Cultural Safety: Aboriginal-trained; Distance: <50km | *Yes |
| Selected Providers | OT: Ms. Lisa Wong (HPI-I: 2222-3333-4444-5555); Physio: Mr. John Smith (HPI-I: 3333-4444-5555-6666) | *Yes |
| Consent Management | Access: AUPS, Shared Care Plan; Scope: Fall prevention; Giver: Sofia Petrov (daughter) | *Yes |
| Booking ID (OT) | BOOK-2025-10-035 | *Yes |
| OT Details | Home Assessment: 2025-10-07, 9:00 AM; Prep: Clear pathways | *Yes |
| Booking ID (Physio) | BOOK-2025-10-036 | *Yes |
| Physio Details | Balance Training: 2025-10-09, 14:00 PM; Transport: Arranged | *Yes |
| Shared Care Plan ID | SCP-2025-10-023Z | *Yes |
| Plan Access | Limited: OT/Physio view fall-related data; Non-med: Home safety modifications, low-carb diet; Notified: Updates to GP, Daughter (Sofia Petrov) | *Yes |
| Low-Glucose Alerts | Threshold: 4.0 mmol/L; Recipient: Daughter (Sofia Petrov, MyHealth App) | *Yes |
| Provider Organisation | Kalgoorlie Aged Care Service (HPI-O: 6666-7777-8888-9999) | *Yes |
| Organisation Address | 12 Boulder Rd, Kalgoorlie, WA 6430 | No |
| Clinician (Coordinator) | Ms. Karen Mitchell (Care Coordinator, HPI-I: 9090-1212-3434-5656) | *Yes |

### FHIR Resources – Aged-Care Service (WA)

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Patient | Yuri Petrov | ⏳ Not yet generated | — |
| ServiceRequest | eReferral – OT (fall prevention) | ⏳ Not yet generated | — |
| ServiceRequest | eReferral – Physio (balance training) | ⏳ Not yet generated | — |
| Appointment | OT home assessment booking (BOOK-2025-10-035) | ⏳ Not yet generated | — |
| Appointment | Physio balance training booking (BOOK-2025-10-036) | ⏳ Not yet generated | — |
| Encounter | OT home assessment visit, 2025-10-07 | ⏳ Not yet generated | — |
| Encounter | Physio balance training visit, 2025-10-09 | ⏳ Not yet generated | — |
| Observation | Fall risk assessment observations | ⏳ Not yet generated | — |
| Practitioner | Ms. Lisa Wong (Occupational Therapist) | ⏳ Not yet generated | — |
| Practitioner | Mr. John Smith (Physiotherapist) | ⏳ Not yet generated | — |
| PractitionerRole | Ms. Lisa Wong – OT, Kalgoorlie Aged Care Service | ⏳ Not yet generated | — |
| PractitionerRole | Mr. John Smith – Physio, Kalgoorlie Aged Care Service | ⏳ Not yet generated | — |
| Organization | Kalgoorlie Aged Care Service | ⏳ Not yet generated | — |

## 7. Population Health / Analytics

| Data Field | Actual Data | Critical? |
| --- | --- | --- |
| De-Identified Cohort | Remote/Traveller Patients (n=250, WA/ACT, 2025) | *Yes |
| IHI (Sample, De-Identified) | Not linked; Aggregated only | *Yes |
| Referral to Booking Time | Median: 3 days; 90th Percentile: 7 days | *Yes |
| Cross-Border Handovers | 98% same-day notifications; Lost to Follow-Up: <1% | *Yes |
| Wait Times by Service | Endo: 5 days; OT/Physio: 2 days (Kalgoorlie) | *Yes |
| Travel Burden | Avg Distance: 1,500 km (WA-ACT); High Burden: 15% cases >2,000 km | *Yes |
| Outcome Metrics | Hypo-Related Falls: Reduced 20%; Telehealth Uptake: 45% | *Yes |
| Dashboard Insights | Target: Add outreach for high-wait areas; Update: Directory with cultural safety flags | *Yes |
| Update Cadence | Nightly; Source: FHIR via Health Connect Australia | No |
| Provider Organisation | Australian Institute of Health and Welfare (HPI-O: 3333-2222-1111-0000) | *Yes |
| Organisation Address | 1 Oxford St, Canberra, ACT 2601 | No |

### FHIR Resources – Population Health / Analytics

| Resource Type | Description | Status | Reference |
| --- | --- | --- | --- |
| Organization | Australian Institute of Health and Welfare | ⏳ Not yet generated | — |

> This section describes a de-identified, aggregated population-health view rather than per-patient data — it wouldn't produce Patient-linked clinical resources; a `Measure`/`MeasureReport` pair would be the more natural fit if we model it at all.

## Pending / Placeholder Data

**Update Notification:** Yuri's last name changed to Petrov on 10 October 2025; all references updated throughout.

**Source-table identifiers.** IHI, MEDICARE NO, HPI-O, and HPI-I values in this document's own tables match Services Australia / Healthcare Identifiers Service test data for entities with FHIR resources generated. Placeholders remain for entities without resources yet built.

**Resource references.** FHIR resources for Yuri's story are not yet generated; all entries show status "⏳ Not yet generated". The data set outline is ready to receive resource files once development begins.
