"""Summarise IV sweep CSV files."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from loaders import load_csv


def summarise_iv(csv_path: Path) -> pd.DataFrame:
    df = load_csv(csv_path)

    if {"vgs", "ids"}.issubset(df.columns):
        on_mask = df["vgs"] == df["vgs"].max()
        off_mask = df["vgs"] == df["vgs"].min()
        summary = pd.DataFrame(
            [
                {
                    "source_file": csv_path.name,
                    "ids_on_a": float(df.loc[on_mask, "ids"].iloc[-1]),
                    "ids_off_a": float(df.loc[off_mask, "ids"].iloc[-1]),
                    "temp_c": float(df["temp_c"].iloc[0]) if "temp_c" in df else None,
                    "n_points": len(df),
                }
            ]
        )
        return summary

    if {"v", "i"}.issubset(df.columns):
        return pd.DataFrame(
            [
                {
                    "source_file": csv_path.name,
                    "v_max": float(df["v"].max()),
                    "i_max": float(df["i"].max()),
                    "n_points": len(df),
                }
            ]
        )

    return pd.DataFrame([{"source_file": csv_path.name, "n_points": len(df), "columns": ",".join(df.columns)}])
