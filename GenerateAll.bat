@echo off
set "OUTFOLDER=..\generated"
set "INFOLDER=..\testdata-csv"

CD Sparked.Csv2FhirMapping

set "RESOURCETYPE=Patient"
bin\Debug\net7.0\Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=Organization"
bin\Debug\net7.0\Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=Location"
bin\Debug\net7.0\Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=Practitioner"
bin\Debug\net7.0\Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=PractitionerRole"
bin\Debug\net7.0\Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=Encounter"
bin\Debug\net7.0\Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=AllergyIntolerance"
bin\Debug\net7.0\Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=Condition"
bin\Debug\net7.0\Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=Immunization"
bin\Debug\net7.0\Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

set "RESOURCETYPE=Observation"
bin\Debug\net7.0\Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

CD ..
