@echo off

set "OUTFOLDER=..\%1"
set "INFOLDER=..\testdata-csv"

CD Sparked.Csv2FhirMapping

IF %1.==. GOTO No1
IF %2.==. GOTO No1

set "RESOURCETYPE=%2"
Csv2Fhir.exe %RESOURCETYPE% "%INFOLDER%\AU Core Sample Data - %RESOURCETYPE%.csv" %OUTFOLDER%

GOTO End1

:No1
  echo Usage:
  echo   %~nx0 output-folder resource-type
  echo Example: 
  echo   %~nx0 generated Patient

  GOTO End1

:End1
CD ..