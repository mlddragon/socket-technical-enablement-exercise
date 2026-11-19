import csv
import json
import sys
import yaml
from collections import Counter
from pathlib import Path

default_file = Path(__file__).resolve().parent / "data/activitypulse-activities.csv"

data_file = Path(sys.argv[1]) if len(sys.argv) > 1 else default_file

if data_file.suffix.lower() in (".yaml", ".yml"):
    with data_file.open(encoding="utf-8") as file:
        activities = yaml.safe_load(file) or []
else:
    with data_file.open(newline="", encoding="utf-8") as file:
        activities = list(csv.DictReader(file))

counts = Counter(row["activity_type"] for row in activities)

summary = {
    "total_records": len(activities),
    "by_activity_type": dict(sorted(counts.items())),
}

print(json.dumps(summary, indent=2))
