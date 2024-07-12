@echo off

IF %1.==. GOTO No1
IF %2.==. GOTO No1
IF %3.==. GOTO No1

Sparked.TestDataClient\TestDataClient.exe Encounter direct-fhir-test-resources %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Observation direct-fhir-test-resources %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Procedure direct-fhir-test-resources %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe MedicationRequest direct-fhir-test-resources %1 %2 %3

GOTO End1

:No1
  echo Usage:
  echo   %~nx0 fhir-server auth-scheme auth-parameter
  echo Example: 
  echo   %~nx0 https://fhir.hl7.org.au/aucore/fhir/DEFAULT Basic Base64-encouded-userid:password

  GOTO End1

:End1