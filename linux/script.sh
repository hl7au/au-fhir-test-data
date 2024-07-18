pushd .
cd ../Sparked.Csv2FhirMapping
./Csv2Fhir Patient "../testdata-csv/AU Core Sample Data - Patient.csv" ../generated
./Csv2Fhir Organization "../testdata-csv/AU Core Sample Data - Organization.csv" ../generated
./Csv2Fhir Location "../testdata-csv/AU Core Sample Data - Location.csv" ../generated
./Csv2Fhir Practitioner "../testdata-csv/AU Core Sample Data - Practitioner.csv" ../generated
./Csv2Fhir PractitionerRole "../testdata-csv/AU Core Sample Data - PractitionerRole.csv" ../generated
./Csv2Fhir Encounter "../testdata-csv/AU Core Sample Data - Encounter.csv" ../generated
./Csv2Fhir AllergyIntolerance "../testdata-csv/AU Core Sample Data - AllergyIntolerance.csv" ../generated
./Csv2Fhir Condition "../testdata-csv/AU Core Sample Data - Condition.csv" ../generated
./Csv2Fhir Immunization "../testdata-csv/AU Core Sample Data - Immunization.csv" ../generated
./Csv2Fhir Observation "../testdata-csv/AU Core Sample Data - Observation.csv" ../generated
./Csv2Fhir Procedure "../testdata-csv/AU Core Sample Data - Procedure.csv" ../generated
./Csv2Fhir Medication "../testdata-csv/AU Core Sample Data - Medication.csv" ../generated
./Csv2Fhir MedicationRequest "../testdata-csv/AU Core Sample Data - MedicationRequest.csv" ../generated
popd
