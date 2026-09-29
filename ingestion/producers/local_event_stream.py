import json
import time
import os

from ingestion.generators.rail_data_generator import generate_dataset
from ingestion.validators.schema_validator import validate_event


def main():
    print("Starting rail freight event stream...")

    while True:
        data = generate_dataset()

        freight_event = data["freight_event"]
        telemetry_event = data["telemetry_event"]

        freight_valid = validate_event(
            freight_event,
            "freight_event.json",
        )

        telemetry_valid = validate_event(
            telemetry_event,
            "telemetry_event.json",
        )

        if freight_valid:
            print(
                "FREIGHT:",
                json.dumps(freight_event),
            )

        if telemetry_valid:
            print(
                "TELEMETRY:",
                json.dumps(telemetry_event),
            )

        time.sleep(2)


if __name__ == "__main__":
    main()