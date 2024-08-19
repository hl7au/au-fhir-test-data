#!/usr/bin/env bash

# directory location of CSV source files
export SOURCE=../testdata-csv

# directory location of FHIR target files
export TARGET=../mixed

# the directory where the distribution is located
# this script by default assumes it is located
# and executed in the 'linux' directory
export DIST=..

# This script will create an explicit target script
# and subsequently execute, much like a compiler.

# The generated script can be edited by hand if this
# is desirable. It can also be used for debugging.
export SCRIPT=compiledUploadScript.sh

# array of FHIR resource type names to process

declare -a resources=(
"Patient"
"Organization"
"Location"
"Practitioner"
"PractitionerRole"
"Encounter"
"AllergyIntolerance"
"Condition"
"Immunization"
"Observation"
"Procedure"
"Medication"
"MedicationRequest"
)

rm ${SCRIPT}

echo pushd . >> ${SCRIPT}
echo cd ${DIST}/Sparked.TestDataClient >> ${SCRIPT}
echo chmod +x TestDataClient >> ${SCRIPT}

## now loop through the above resourcesay
for resource in "${resources[@]}"
do
echo "$resource"
echo ./TestDataClient ${resource} ${TARGET} \$1 Basic \$2 >> ${SCRIPT} 
# Sparked.TestDataClient\TestDataClient.exe Organization generated %1 %2 %3
# https://fhir.hl7.org.au/aucore/fhir/DEFAULT Basic Base64-encouded-userid:password
done
echo popd >> ${SCRIPT}

chmod +x ${SCRIPT}
#./${SCRIPT}