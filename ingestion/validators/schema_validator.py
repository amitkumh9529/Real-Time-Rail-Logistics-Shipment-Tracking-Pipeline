import json
from pathlib import Path

from jsonschema import validate
from jsonschema.exceptions import ValidationError


ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "ingestion" / "schemas"


def load_schema(schema_name: str) -> dict:
    schema_path = SCHEMA_DIR / schema_name

    with schema_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def validate_event(event: dict, schema_name: str) -> bool:
    schema = load_schema(schema_name)

    try:
        validate(instance=event, schema=schema)
        return True
    except ValidationError as exc:
        print(f"Schema validation failed: {exc.message}")
        return False