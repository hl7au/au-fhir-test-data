import pandas as pd
import argparse

sheets = [
    "Patient",
    "Encounter",
    "Condition",
    "AllergyIntolerance",
    "Immunization",
    "Observation",
    "Organization",
    "HealthcareService",
    "PractitionerRole",
    "Practitioner",
    "Procedure",
    "Location",
    "MedicationRequest",
    "Medication",
    #'Specimen',
    "RelatedPerson",
    "ServiceRequest",
]

parser = argparse.ArgumentParser(
    prog="Test Data converter",
    description="Load XLSX file with test data and convert it to csvs",
)
parser.add_argument("filename")


def remove_time(data):
    if not isinstance(data, str):
        return data
    parts = data.split(" ")
    return parts[0]


def replace_substring_in_file(file_path, target_substring, replacement_substring):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    modified_lines = []

    for line in lines:
        if target_substring in line:
            modified_lines.append(line.replace(target_substring, replacement_substring))
        else:
            modified_lines.append(line)

    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(modified_lines)


def replace_substrings_in_file(file_path, substring_pairs):
    for substring_pair in substring_pairs:
        replace_substring_in_file(file_path, substring_pair[0], substring_pair[1])


def add_symbol_to_lines(file_path, symbol="!"):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    modified_lines = [line.rstrip("\n") + symbol + "\n" for line in lines]

    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(modified_lines)


def add_empty_columns(file_path, number_of_columns):
    for _i in range(number_of_columns):
        add_symbol_to_lines(file_path, ",")


if __name__ == "__main__":
    args = parser.parse_args()
    xlsx = pd.ExcelFile(args.filename)
    for sheet in sheets:
        df = xlsx.parse(sheet, dtype=str, keep_default_na=False)
        if sheet == "Patient":
            df["birthDate"] = df["birthDate"].apply(remove_time)
        if sheet == "RelatedPerson":
            df["birthDate"] = df["birthDate"].apply(remove_time)
            df["patient_dob"] = df["patient_dob"].apply(remove_time)
        if sheet == "AllergyIntolerance":
            df = df.rename(
                columns={
                    "asserter_reference_identifier_type.1": "asserter_reference_identifier_type",
                    "asserter_reference_identifier_type.2": "asserter_reference_identifier_type",
                }
            )
        file_path = f"../testdata-csv/AU Core Sample Data - {sheet}.csv"

        df.to_csv(
            file_path, index=None, header=True, encoding="utf-8-sig", quotechar='"'
        )

        if sheet == "Immunization":
            replace_substring_in_file(file_path, "Unnamed: 45", "")
        if sheet == "HealthcareService":
            replace_substrings_in_file(
                file_path,
                [
                    ("	Surgical service", '"	Surgical service"'),
                    ("	Pathology service", '"	Pathology service"'),
                    ("	Optometry service", '"	Optometry service"'),
                    ("	Thoracic surgery", '"	Thoracic surgery"'),
                ],
            )
            add_empty_columns(file_path, 2)
        if sheet == "Organization":
            replace_substrings_in_file(
                file_path,
                [
                    ("	Surgical service", '"	Surgical service"'),
                    ("	Pathology service", '"	Pathology service"'),
                    ("	Optometry service", '"	Optometry service"'),
                ],
            )
            add_empty_columns(file_path, 2)
        if sheet == "PractitionerRole":
            replace_substrings_in_file(
                file_path,
                [
                    ("	Clinical psychology", '"	Clinical psychology"'),
                    ("General practitioner	", '"General practitioner	"'),
                    ("Community pharmacist	", '"Community pharmacist	"'),
                    ("Cardiothoracic surgery	", '"Cardiothoracic surgery	"'),
                ],
            )
        if sheet == "RelatedPerson" or sheet == "Practitioner":
            add_empty_columns(file_path, 1)
