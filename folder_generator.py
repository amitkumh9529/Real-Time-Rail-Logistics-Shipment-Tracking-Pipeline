from pathlib import Path



FOLDERS = [
    "ingestion/producers",
    "ingestion/generators",
    "ingestion/schemas",
    "databricks/notebooks",
    "databricks/jobs",
    "databricks/src",
    "lakehouse/bronze",
    "lakehouse/silver",
    "lakehouse/gold",
    "quality/expectations",
    "quality/checks",
    "warehouse/dimensions",
    "warehouse/facts",
    "warehouse/marts",
    "airflow/dags",
    "infrastructure/terraform",
    "tests/unit",
    "tests/integration",
    "tests/data_quality",
    "monitoring",
    "docs",
]

FILES = [
    "README.md",
    "pyproject.toml",
    ".gitignore",
    ".env.example",
    "docker-compose.yml",
    "Makefile",
    "docs/architecture.md",
    "docs/data_model.md",
    "docs/data_contracts.md",
    "docs/deployment.md",
    "docs/runbook.md",
]


def main() -> None:
    
    for folder in FOLDERS:
        path = Path(folder)
        path.mkdir(parents=True, exist_ok=True)
        (path / ".gitkeep").touch(exist_ok=True)
        print(f"  + {path}/")

    for file in FILES:
        path = Path(file)
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.touch()
            print(f"  + {path}")

    print(f"\nDone. Structure ready under ./")


if __name__ == "__main__":
    main()