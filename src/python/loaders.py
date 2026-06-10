"""Load CNM CSV and DAT exports."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def load_noise_dat(path: Path) -> pd.DataFrame:
    """Parse whitespace-delimited .dat files with optional # comment header."""
    rows: list[list[str]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            rows.append(stripped.split())

    if not rows:
        raise ValueError(f"No numeric rows found in {path}")

    header, *data = rows
    frame = pd.DataFrame(data, columns=header)
    return frame.apply(pd.to_numeric, errors="coerce")
