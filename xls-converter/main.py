import pandas as pd
import argparse

sheets =  [
    'Patient',
    'Encounter',
    'Condition',
    'AllergyIntolerance',
    'Immunization',
    'Observation',
    'Organization',
    'HealthcareService',
    'PractitionerRole',
    'Practitioner',
    'Procedure',
    'Location',
    'MedicationRequest',
    'Medication',
    #'Specimen',
    'RelatedPerson',
    'ServiceRequest',
];

parser = argparse.ArgumentParser(
    prog='Test Data converter',
    description='Load XLSX file with test data and convert it to csvs',
)
parser.add_argument('filename')


if __name__ == '__main__':
    args = parser.parse_args()
    xlsx = pd.ExcelFile(args.filename)
    for sheet in sheets:
        df = xlsx.parse(sheet)
        df.to_csv(f"./testdata-csv/AU Core Sample Data - {sheet}.csv",index = None , header=True)
