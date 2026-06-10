#!/usr/bin/env python3
"""Dummy CNM processing pipeline — reads CSV/DAT, writes summaries to data/02_processed/."""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

from paths import PROCESSED_DIR, ensure_output_dirs, input_dir
from process_ac import summarise_ac
from process_iv import summarise_iv
from process_noise import summarise_noise
from process_yield import summarise_yield

IV_FILES = ("march8.csv", "data1.csv")
NOISE_FILES = ("noise_NEW2.dat",)
AC_FILES = ("FINAL_v3_USETHIS.csv",)
YIELD_FILES = ("definitive_DEFINITIVE.csv",)


def _run_group(label: str, paths: list[Path], fn) -> pd.DataFrame | None:
    frames: list[pd.DataFrame] = []
    for path in paths:
        print(f"  [{label}] {path.name}")
        frames.append(fn(path))
    return pd.concat(frames, ignore_index=True) if frames else None


def main() -> int:
    src = input_dir()
    ensure_output_dirs()

    print(f"Input directory:  {src}")
    print(f"Output directory: {PROCESSED_DIR}\n")

    summaries: dict[str, pd.DataFrame] = {}

    iv_paths = [src / name for name in IV_FILES if (src / name).exists()]
    noise_paths = [src / name for name in NOISE_FILES if (src / name).exists()]
    ac_paths = [src / name for name in AC_FILES if (src / name).exists()]
    yield_paths = [src / name for name in YIELD_FILES if (src / name).exists()]

    if iv_paths:
        print("IV summaries")
        summaries["iv_summary"] = _run_group("IV", iv_paths, summarise_iv)

    if noise_paths:
        print("Noise summaries")
        summaries["noise_summary"] = _run_group("noise", noise_paths, summarise_noise)

    if ac_paths:
        print("AC summaries")
        summaries["ac_summary"] = _run_group("AC", ac_paths, summarise_ac)

    if yield_paths:
        print("Yield summaries")
        summaries["yield_summary"] = _run_group("yield", yield_paths, summarise_yield)

    if not summaries:
        print("No known input files found.", file=sys.stderr)
        return 1

    for name, frame in summaries.items():
        out = PROCESSED_DIR / f"{name}.csv"
        frame.to_csv(out, index=False)
        print(f"Wrote {out}")

    print("\nPipeline complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
