@echo off

IF %1.==. GOTO No1
IF %2.==. GOTO No1
IF %3.==. GOTO No1

Sparked.TestDataClient\bin\Debug\net7.0\Sparked.TestDataClient.exe Organization generated %1 %2 %3
pause
Sparked.TestDataClient\bin\Debug\net7.0\Sparked.TestDataClient.exe Practitioner generated %1 %2 %3
pause
Sparked.TestDataClient\bin\Debug\net7.0\Sparked.TestDataClient.exe PractitionerRole generated %1 %2 %3
pause
Sparked.TestDataClient\bin\Debug\net7.0\Sparked.TestDataClient.exe Patient generated %1 %2 %3
pause

GOTO End1

:No1
  echo Usage:
  echo   %~nx0 fhir-server auth-scheme auth-parameter
  echo Example: 
  echo   %~nx0 https://sparked.npd.telstrahealth.com/ereq/fhir Basic Base64-encouded-userid:password

  GOTO End1

:End1