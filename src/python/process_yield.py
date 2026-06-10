"""Summarise wafer yield CSV files."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from loaders import load_csv


def summarise_yield(csv_path: Path) -> pd.DataFrame:
    df = load_csv(csv_path)
    if "yield" not in df.columns:
        raise ValueError(f"{csv_path.name} has no yield column")

    return pd.DataFrame(
        [
            {
                "source_file": csv_path.name,
                "n_dies": len(df),
                "yield_fraction": float(df["yield"].mean()),
                "fmax_mean_ghz": float(df["fmax_ghz"].mean()) if "fmax_ghz" in df else None,
                "power_mean_mw": float(df["power_mw"].mean()) if "power_mw" in df else None,
            }
        ]
    )
