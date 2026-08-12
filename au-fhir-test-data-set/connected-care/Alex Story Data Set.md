# Data Set for Alex’s Story

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
| Provider Directory Search | Filters: Bathurst/Sydney, Wait Time <2 weeks; Selected: Dr. Emily Chen, Sydney Private Clinic (HPI-I: 2222-3333-4444-5555) | *Yes |
| Subscription Preferences | GP (Dr. Jane Smith, HPI-I: 5555-6666-7777-8888): Critical updates only (results, bookings) | *Yes |
| Provider Organisation | Bathurst Medical Centre (HPI-O: 6666-7777-8888-9999) | *Yes |
| Organisation Address | 25 Russell St, Bathurst, NSW 2795 | No |
| Clinician | Dr. Chris Lee (GP, HPI-I: 5555-6666-7777-8888) | *Yes |

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
| Booking Details | Sydney Private Hospital (HPI-O: 3333-4444-5555-6666); Date: 2025-11-01; Prep: SMART Form completed | *Yes |
| SMART Form ID | FORM-2025-10-010 | *Yes |
| Form Details | Consent: Signed digitally; Medical History: No comorbidities; Allergies: Penicillin | *Yes |
| ALLIED HEALTH eREFERRALS | Issued: Physio (REF-2025-11-017), Counselling (REF-2025-11-018) electronically | *Yes |
| Structured Data for Payer Approvals | Patient/procedure data structured for instant payer requests |  |
| Payer Pre-Approval | Submitted: Procedure Code CNE001; Cost: $6,000; Insurer: Medibank Private | No |
| Provider Organisation | Sydney Private Clinic (HPI-O: 7777-8888-9999-0000) | *Yes |
| Organisation Address | 100 George St, Sydney, NSW 2000 | No |
| Clinician | Dr. Emily Chen (Gynaecologist, HPI-I: 2222-3333-4444-5555) | *Yes |

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
| Provider Organisation | Sydney Private Hospital (HPI-O: 3333-4444-5555-6666) | *Yes |
| Organisation Address | 50 Pitt St, Sydney, NSW 2000 | No |
| Clinician | Dr. Mark Wilson (Surgeon, HPI-I: 3434-5656-7878-9090) | *Yes |

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
