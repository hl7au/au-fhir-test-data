#!/usr/bin/env bash

# directory location of CSV source files
export SOURCE=../testdata-csv

# directory location of FHIR target files
export TARGET=../generated

# the directory where the distribution is located
# this script by default assumes it is located
# and executed in the 'linux' directory
export DIST=..

# This script will create an explicit target script
# and subsequently execute, much like a compiler.

# The generated script can be edited by hand if this
# is desirable. It can also be used for debugging.
export SCRIPT=compiledScript.sh

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

echo set -e >> ${SCRIPT}
echo mkdir --parent ${TARGET} >> ${SCRIPT}
echo pushd . >> ${SCRIPT}
echo cd ${DIST}/Sparked.Csv2FhirMapping >> ${SCRIPT}
echo chmod +x Csv2Fhir >> ${SCRIPT}

## now loop through the above resourcesay
for resource in "${resources[@]}"
do
echo "$resource"
echo ./Csv2Fhir $resource \""${SOURCE}/AU Core Sample Data - $resource.csv"\" "${TARGET}" >> ${SCRIPT}
done
echo popd >> ${SCRIPT}

chmod +x ${SCRIPT}
./${SCRIPT}
