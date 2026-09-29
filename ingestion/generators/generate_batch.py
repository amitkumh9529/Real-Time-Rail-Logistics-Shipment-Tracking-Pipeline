import json
from pathlib import Path

from ingestion.generators.rail_data_generator import generate_dataset


OUTPUT_DIR = Path("./data/raw")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

freight_events = []
telemetry_events = []

for _ in range(100000):
    data = generate_dataset()

    freight_events.append(data["freight_event"])
    telemetry_events.append(data["telemetry_event"])


with open(OUTPUT_DIR / "freight_events.json", "w", encoding="utf-8") as f:
    for event in freight_events:
        f.write(json.dumps(event) + "\n")


with open(OUTPUT_DIR / "telemetry_events.json", "w", encoding="utf-8") as f:
    for event in telemetry_events:
        f.write(json.dumps(event) + "\n")


print(f"Generated {len(freight_events)} freight events")
print(f"Generated {len(telemetry_events)} telemetry events")