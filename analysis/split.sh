#!/usr/bin/env bash

# https://www.hl7.org/fhir/resource.html#:~:text=The%20logical%20id%20is%20unique%20within%20the%20space,by%20the%20server%2C%20the%20id%20is%20never%20changed.
# Each resource has an id element which contains the "logical id" of the resource assigned by the server responsible for storing it. Resources always have a known logical id except for a few special cases (e.g. when a new resource is being sent to a server to assign a logical id in the create interaction). The logical id is unique within the space of all resources of the same type on the same server. Once assigned by the server, the id is never changed.

# https://www.hl7.org/fhir/http.html#create
# The request body SHALL be a FHIR Resource of the named type. The resource does not need to have an id element (this is one of the few cases where a resource exists without an id element). If an id is provided, the server SHALL ignore it.

# https://fhir-drills.github.io/patient-with-references.html#:~:text=In%20FHIR%20resources%20are%20referenced%2C%20or%20linked%2C%20in,all%20Observations%20will%20be%20linked%20to%20the%20Patient.
# In FHIR resources are referenced, or linked, in one direction only. For example, if you have two resources - a Patient and an Observation - a Patient will not be linked to any of the Observations; instead all Observations will be linked to the Patient.

# Seems this whole approach is busted. We need to map and replace in creation order. The sync operation may `create` resources, but 

TARGET_DIRECTORY=..

TARGET=${TARGET_DIRECTORY}/out.csv
SORTED_TARGET=${TARGET_DIRECTORY}/out.sorted.csv
UNIQ_TARGET=${TARGET_DIRECTORY}/out.uniq.csv

SOURCE_DIRECTORY=../generated

rm ${TARGET}
rm ${SORTED_TARGET}
rm ${UNIQ_TARGET}

for resource in ${SOURCE_DIRECTORY}/*.json
do
 ID=`jq --raw-output .id ${resource}`
 jq --raw-output .resourceType ${resource}
 echo "$ID,${resource}" >> ${TARGET} 
done

sort ${TARGET} > ${SORTED_TARGET}
sort --unique --field-separator=, --key=1,1 ${SORTED_TARGET} > ${UNIQ_TARGET}

SORTED_LINES=`wc --lines < ${SORTED_TARGET}`
UNIQ_LINES=`wc --lines < ${UNIQ_TARGET}`

echo ${SORTED_LINES} resources present
echo ${UNIQ_LINES} unique resource identifiers found within resources

if (( ${SORTED_LINES} > ${UNIQ_LINES} ));
then
  echo "Some resources have the same identifier. Local dataset is NOT SANE and not feasible for upload."
else
  echo "Local dataset looks sane. Please be aware upload can still fail due to server side IDs being present."
fi
