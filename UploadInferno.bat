@echo off

IF %1.==. GOTO No1
IF %2.==. GOTO No1
IF %3.==. GOTO No1

Sparked.TestDataClient\TestDataClient.exe Organization au-core-inferno-tests %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Location au-core-inferno-tests %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Practitioner au-core-inferno-tests %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe PractitionerRole au-core-inferno-tests %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Patient au-core-inferno-tests %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Encounter au-core-inferno-tests %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe AllergyIntolerance au-core-inferno-tests %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Condition au-core-inferno-tests %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Immunization au-core-inferno-tests %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Specimen au-core-inferno-tests %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Observation au-core-inferno-tests %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe MedicationRequest au-core-inferno-tests %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe MedicationStatement au-core-inferno-tests %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Procedure au-core-inferno-tests %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Provenance au-core-inferno-tests %1 %2 %3

GOTO End1

:No1
  echo Usage:
  echo   %~nx0 fhir-server auth-scheme auth-parameter
  echo Example: 
  echo   %~nx0 https://fhir.hl7.org.au/aucore/fhir/DEFAULT Basic Base64-encouded-userid:password

  GOTO End1

:End1