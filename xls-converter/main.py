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

def remove_time(data):
    if not isinstance(data,str):
        return data
    parts = data.split(' ')
    return parts[0]

if __name__ == '__main__':
    args = parser.parse_args()
    xlsx = pd.ExcelFile(args.filename)
    for sheet in sheets:
        df = xlsx.parse(sheet, dtype=str)
        if sheet == 'Patient':
            df['birthDate'] = df['birthDate'].apply(remove_time)

        df.to_csv(f"./testdata-csv/AU Core Sample Data - {sheet}.csv",
                  index = None , header=True,
                  encoding='utf-8-sig')
