@echo off

IF %1.==. GOTO No1
IF %2.==. GOTO No1
IF %3.==. GOTO No1

Sparked.TestDataClient\TestDataClient.exe Organization generated %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Location generated %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Practitioner generated %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe PractitionerRole generated %1 %2 %3
pause
Sparked.TestDataClient\TestDataClient.exe Patient generated %1 %2 %3
pause

GOTO End1

:No1
  echo Usage:
  echo   %~nx0 fhir-server auth-scheme auth-parameter
  echo Example: 
  echo   %~nx0 https://fhir.hl7.org.au/ereq/fhir/DEFAULT Basic Base64-encouded-userid:password

  GOTO End1

:End1