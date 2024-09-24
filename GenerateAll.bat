@echo off
set "OUTFOLDER=..\generated"
set "INFOLDER=..\testdata-csv"

CD Sparked.Csv2FhirMapping

set "RESOURCETYPE=Patient"
Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=RelatedPerson"
Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=Organization"
Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=Location"
Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=HealthcareService"
Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=Practitioner"
Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=PractitionerRole"
Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=Encounter"
Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=AllergyIntolerance"
Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=Condition"
Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=Immunization"
Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=Observation"
Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=Procedure"
Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=Medication"
Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=MedicationRequest"
Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

CD ..
