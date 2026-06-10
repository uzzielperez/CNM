"""Summarise AC frequency-response CSV files."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from loaders import load_csv


def summarise_ac(csv_path: Path) -> pd.DataFrame:
    df = load_csv(csv_path)
    required = {"freq_hz", "gain_db", "phase_deg"}
    if not required.issubset(df.columns):
        raise ValueError(f"{csv_path.name} missing columns: {required - set(df.columns)}")

    grouped = df.groupby("id", dropna=False)
    rows = []
    for device_id, chunk in grouped:
        peak_idx = chunk["gain_db"].idxmax()
        rows.append(
            {
                "source_file": csv_path.name,
                "device_id": device_id,
                "gain_peak_db": float(chunk.loc[peak_idx, "gain_db"]),
                "phase_at_peak_deg": float(chunk.loc[peak_idx, "phase_deg"]),
                "freq_at_peak_hz": float(chunk.loc[peak_idx, "freq_hz"]),
                "vdd_v": float(chunk["vdd"].iloc[0]) if "vdd" in chunk else None,
                "n_points": len(chunk),
            }
        )
    return pd.DataFrame(rows)
