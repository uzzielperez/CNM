"""Resolve input/output paths (supports legacy datasets/ and target data/ layout)."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

LEGACY_DATASETS = REPO_ROOT / "datasets"
RAW_DIR = REPO_ROOT / "data" / "01_raw"
PROCESSED_DIR = REPO_ROOT / "data" / "02_processed"
FINAL_DIR = REPO_ROOT / "data" / "03_final"


def input_dir() -> Path:
    if RAW_DIR.exists() and any(RAW_DIR.iterdir()):
        return RAW_DIR
    return LEGACY_DATASETS


def ensure_output_dirs() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    FINAL_DIR.mkdir(parents=True, exist_ok=True)
