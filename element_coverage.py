import json
import os
import csv
from collections import defaultdict

ROOT = r"."  # or the path to your repo

def walk_paths(obj, prefix=""):
    paths = set()
    if isinstance(obj, dict):
        for k, v in obj.items():
            new_prefix = f"{prefix}.{k}" if prefix else k
            paths |= walk_paths(v, new_prefix)
    elif isinstance(obj, list):
        for item in obj:
            paths |= walk_paths(item, prefix)
    else:
        paths.add(prefix)
    return paths

by_type = defaultdict(lambda: defaultdict(set))

for dirpath, _, filenames in os.walk(ROOT):
    for fn in filenames:
        if not fn.endswith(".json"):
            continue
        path = os.path.join(dirpath, fn)
        try:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print("Error loading", path, e)
            continue

        rtype = data.get("resourceType")
        if not rtype:
            continue

        paths = walk_paths(data)
        by_type[rtype][fn] = paths

out_dir = os.path.join(ROOT, "_coverage")
os.makedirs(out_dir, exist_ok=True)

for rtype, files in by_type.items():
    all_paths = sorted(set().union(*files.values()))
    out_path = os.path.join(out_dir, f"{rtype}-coverage.csv")
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["file"] + all_paths)
        for fn, paths in sorted(files.items()):
            row = [fn] + [ "1" if p in paths else "" for p in all_paths ]
            writer.writerow(row)

    print("Wrote", out_path)