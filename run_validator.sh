#!/usr/bin/env bash

java -jar validator_cli.jar hand-written/*.json -version 4.0.1 -tx https://tx.dev.hl7.org.au/fhir -ig hl7.fhir.au.core#0.4.0-preview -sct au -level errors -jurisdiction au -html-output h_validation.html -output h_validation.xml
java -jar validator_cli.jar generated/*.json -version 4.0.1 -tx https://tx.dev.hl7.org.au/fhir -ig hl7.fhir.au.core#0.4.0-preview -sct au -level errors -jurisdiction au -html-output g_validation.html -output g_validation.xml   
java -jar validator_cli.jar mixed/*.json -version 4.0.1 -tx https://tx.dev.hl7.org.au/fhir -ig hl7.fhir.au.core#0.4.0-preview  -sct au -level errors -jurisdiction au -html-output m_validation.html -output m_validation.xml       