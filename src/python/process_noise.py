"""Process 1/f noise .dat spectra."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from loaders import load_noise_dat


def summarise_noise(dat_path: Path) -> pd.DataFrame:
    df = load_noise_dat(dat_path)
    freq = df["freq"].astype(float)
    sv = df["Sv"].astype(float)

    # Dummy fit slope on log-log axis (placeholder for proper 1/f extraction).
    slope, intercept = np.polyfit(np.log10(freq), np.log10(sv), 1)

    return pd.DataFrame(
        [
            {
                "source_file": dat_path.name,
                "freq_min_hz": float(freq.min()),
                "freq_max_hz": float(freq.max()),
                "sv_at_1khz": float(sv[freq == 1000].iloc[0]) if (freq == 1000).any() else None,
                "loglog_slope": float(slope),
                "loglog_intercept": float(intercept),
                "n_points": len(df),
            }
        ]
    )
