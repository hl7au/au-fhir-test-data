from pathlib import Path
import json

# Get the reference (resourceType/resourceId eg Patient/donaldd) of the resource
def get_reference(resource):
    resource_type = resource.get('resourceType', 'Unknown')
    resource_id = resource.get('id', 'Unknown')
    return f"{resource_type}/{resource_id}"

# Find all outgoing references in the resource
def find_references(obj, refs=None):
        if refs is None:
            refs = []
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == 'reference' and isinstance(v, str):
                    refs.append(v)
                else:
                    find_references(v, refs)
        elif isinstance(obj, list):
            for item in obj:
                find_references(item, refs)
        return refs

# Load the quarantine list
def load_quarantine_list(path):
    quarantine = set()
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    quarantine.add(line)
    except FileNotFoundError:
        pass
    return quarantine

def main():
    json_files = list(Path('.').rglob('*.json'))
    references = set()
    references_list = {}
    errors = {}

    for file_path in json_files:
        try:
            with file_path.open('r', encoding='utf-8') as f:
                resource = json.load(f)
                reference_this = get_reference(resource)
                references.add(reference_this)
                if file_path not in references_list:
                    references_list[file_path] = set()
                found_references = find_references(resource)
                for ref in found_references:
                    if ref and not ref.startswith('#'): # Ignore local references
                        references_list[file_path].add(ref)
        except json.JSONDecodeError as e:
            errors[str(file_path)] = f"JSON decode error."
        except Exception as e:
            errors[str(file_path)] = f"Error reading file."

    for file_path, refs in references_list.items():
        for ref in refs:
            if ref not in references:
                errors[str(file_path)] = f"Reference '{ref}' not found in any resource."

    quarantine = load_quarantine_list(".github/scripts/reference_integrity_quarantine")
    # Remove errors for quarantined files (by filename, not path)
    errors = {k: v for k, v in errors.items() if Path(k).name not in quarantine}

    if errors:
        with open("reference_errors.json", "w") as f:
            json.dump(errors, f)
    else:
        # Remove error file if exists from previous runs
        error_file = Path("reference_errors.json")
        if error_file.exists():
            error_file.unlink()

if __name__ == "__main__":
    main()