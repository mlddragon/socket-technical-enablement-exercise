import csv
import json
from collections import Counter
from pathlib import Path

data_file = (
    Path(__file__).resolve().parent.parent
    / "project/data/activitypulse-activities.csv"
)

with data_file.open(newline="", encoding="utf-8") as file:
    activities = list(csv.DictReader(file))

counts = Counter(row["activity_type"] for row in activities)

summary = {
    "total_records": len(activities),
    "by_activity_type": dict(sorted(counts.items())),
}

print(json.dumps(summary, indent=2))
