from pathlib import Path



FOLDERS = [
    "ingestion/generators",
    "ingestion/producers",
    "schemas",
    "streaming",
    "transformations/bronze",
    "transformations/silver",
    "transformations/gold",
    "quality",
    "geospatial",
    "lakehouse",
    "warehouse",
    "trino",
    "airflow",
    "monitoring",
    "tests/unit",
    "tests/integration",
    "infrastructure/terraform",
    "docker",
    "docs",
    ".github/workflows",
]




def main() -> None:
    
    for folder in FOLDERS:
        path = Path(folder)
        path.mkdir(parents=True, exist_ok=True)
        # keep empty dirs in git
        (path / ".gitkeep").touch(exist_ok=True)
        print(f"  + {path}")
    print(f"\nDone. Structure ready under ./")


if __name__ == "__main__":
    main()