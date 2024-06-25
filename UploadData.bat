@echo off

IF %1.==. GOTO No1
IF %2.==. GOTO No1
IF %3.==. GOTO No1
IF %4.==. GOTO No1
IF %5.==. GOTO No1

Sparked.TestDataClient\TestDataClient.exe %5 %4 %1 %2 %3

GOTO End1

:No1
    echo USAGE:
    echo   %~nx0 fhir-server auth-scheme auth-parameter input-folder resource-type
    echo Example:
    echo   %~nx0 https://fhir.hl7.org.au/aucore/fhir/DEFAULT Basic Base64-encouded-userid:password generated Observation

GOTO End1

:End1