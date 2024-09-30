@echo off

IF %1.==. GOTO No1
IF %2.==. GOTO No1
IF %3.==. GOTO No1

Sparked.TestDataClient\TestDataClient.exe Organization generated %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Location generated %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe HealthcareService generated %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Practitioner generated %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe PractitionerRole generated %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Patient generated %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe RelatedPerson generated %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Encounter generated %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe AllergyIntolerance generated %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Condition generated %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Immunization generated %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Observation generated %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Procedure generated %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Medication generated %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe MedicationRequest generated %1 %2 %3

GOTO End1

:No1
  echo Usage:
  echo   %~nx0 fhir-server auth-scheme auth-parameter
  echo Example: 
  echo   %~nx0 https://fhir.hl7.org.au/aucore/fhir/DEFAULT Basic Base64-encouded-userid:password

  GOTO End1

:End1