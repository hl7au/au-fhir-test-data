import json
import argparse

def extract_filename(oo):
    for ext in oo['resource']['extension']:
        if ext['url']=='http://hl7.org/fhir/StructureDefinition/operationoutcome-file':
            return ext['valueString']
    raise TypeError("No filename in this OperationOutcome")

# error level: error - 2, warning - 1, pass - 0
def extract_severity_level(oo):
    for issue in oo['resource']['issue']:
        warning = False
        if issue['severity']=='error':
            return 2
        if issue['severity']=='warning':
            warning = True
    return 1 if warning else 0

def format_result(passCount, warningCount, errorCount, quarantineCount):
    template = '''

    '''


if __name__ == '__main__':
    # parse arg
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--report')
    parser.add_argument('-q', '--quarantine')
    args = parser.parse_args()
    
    # read report bundle
    report_file = open(args.report)
    bundle = json.load(report_file)

    # read quarantine file list (ignore comment)
    quarantine_file = open(args.quarantine)
    quarantine = quarantine_file.read().splitlines()
    quarantine = [x for x in quarantine if not x.startswith('#')]
    
    # counters
    passCount = 0
    warningCount = 0
    errorCount = 0
    quarantineCount = 0

    for oo in bundle['entry']:
        if extract_filename(oo) in quarantine:
            quarantineCount += 1
            continue
        severity_level = extract_severity_level(oo)
        if severity_level == 2:
            errorCount += 1
        if severity_level == 1:
            # warning is still a pass
            warningCount += 1
            passCount += 1
        if severity_level == 0:
            passCount += 1

    print("pass={}".format(passCount))
    print("warning={}".format(warningCount))
    print("error={}".format(errorCount))
    print("quarantine={}".format(quarantineCount))