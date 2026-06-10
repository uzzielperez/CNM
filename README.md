# CNM

Semiconductor device characterization data for 180 nm CMOS devices. This repository holds measurement exports, processed summaries, and supporting notes for IV characterization, noise analysis, AC frequency response, and wafer-level yield tracking.

**Technology:** 180 nm PDK · nominal supply 1.8 V · process corners `tt`, `ff`, `ss`, `fs`, `sf`

---

## Repository layout

This project follows a standardized data-repo structure. Directories below reflect the target layout; some paths are still being migrated from the legacy `datasets/` and `docs/` folders.

```
CNM/
├── README.md              # Repository landing page (this file)
├── LICENSE                # Usage rights (MIT or CC-BY-4.0 — add before public release)
├── data/
│   ├── 01_raw/            # READ-ONLY. Factory and instrument outputs
│   ├── 02_processed/      # Noise-filtered, calibrated, and corrected tables
│   └── 03_final/          # Publication-ready matrices for figures and reports
├── src/                   # Analysis scripts and automation pipelines
└── documentation/         # Calibration sheets, datasheets, lab notes
```

### Current file map (legacy → target)

| File | Description | Target location |
|------|-------------|-----------------|
| `march8.csv` | IV sweep (`vgs`, `vds`, `ids`, temperature) | `data/01_raw/` |
| `copy of copy of IV_curves.xlsx.csv` | Raw IV curve export from spreadsheet | `data/01_raw/` |
| `noise_NEW2.dat` | 1/f noise spectra (`freq`, `Sv`, `Si`) | `data/01_raw/` |
| `asdfgraph.png.csv` | Exported plot/trace data | `data/01_raw/` |
| `data1.csv` | Simple V–I sample sweep | `data/02_processed/` |
| `Measurements - Juan - version2 - corrected.csv` | Corrected device parameters (Vth, DIBL, Ion, Ioff) | `data/02_processed/` |
| `untitled2.csv` | Switch/resistance ratio measurements | `data/02_processed/` |
| `FINAL_v3_USETHIS.csv` | AC gain and phase vs. frequency (use for figures) | `data/03_final/` |
| `definitive_DEFINITIVE.csv` | Wafer/die yield summary (`fmax`, power) | `data/03_final/` |
| `docs/aaa.txt` | Simulation setup notes (PDK, corners, Monte Carlo) | `documentation/` |
| `docs/results_copy.txt` | Extracted threshold-voltage summary | `documentation/` |
| `docs/meeting_notes_also_has_data.txt` | Lab meeting notes and leakage table | `documentation/` |

> **Rule of thumb:** never edit files in `01_raw/`. Derive new tables in `02_processed/` or `03_final/` and record the transformation in `src/` or a short note in `documentation/`.

---

## Datasets at a glance

### IV and DC characterization

- **`march8.csv`** — Multi-point IV sweep across bias and temperature.
- **`Measurements - Juan - version2 - corrected.csv`** — Per-device DC parameters for nMOS and pMOS (Vth, DIBL, Ion, Ioff).
- **`data1.csv`** — Small-sample V–I curve at fixed temperature.

### Noise

- **`noise_NEW2.dat`** — Voltage and current noise spectral density vs. frequency.

### AC / small-signal

- **`FINAL_v3_USETHIS.csv`** — Frequency response: gain (dB) and phase (deg) vs. `freq_hz` at VDD = 3.3 V. **Preferred source for Bode plots.**

### Yield and benchmarking

- **`definitive_DEFINITIVE.csv`** — Per-die figures of merit (`fmax_ghz`, `power_mw`, yield flag).
- **`untitled2.csv`** — On-resistance and off-resistance ratios.

---

## Key extracted results

From `documentation/results_copy.txt` (nMOS, W/L = 10/0.18 µm):

| Parameter | Value |
|-----------|-------|
| Vth | 0.42 V |
| Ioff | 1.2 nA |
| Ion | 580 µA |
| Subthreshold swing | 68 mV/dec |

Corner leakage summary (27 °C unless noted) — see `documentation/meeting_notes_also_has_data.txt`:

| Corner | Temp (°C) | Ileak |
|--------|-----------|-------|
| tt | 27 | 1.2 nA |
| ff | −40 | 0.3 nA |
| ss | 125 | 18.7 nA |
| fs | 27 | 1.4 nA |
| sf | 27 | 1.1 nA |

---

## Simulation context

From lab notes (`documentation/aaa.txt`):

- SPICE netlist uses the **180 nm PDK**
- Process corners: `tt`, `ff`, `ss`, `fs`, `sf`
- Nominal supply: **1.8 V**
- Monte Carlo: **500 runs**

---

## Getting started

```bash
git clone git@github.com:uzzielperez/CNM.git
cd CNM
```

No build step is required today — data are plain CSV/DAT/TXT. When analysis scripts are added under `src/`, document dependencies here (e.g. Python + pandas, or your SPICE simulator).

### Suggested workflow

1. Pull raw exports into `data/01_raw/` and leave them unchanged.
2. Run calibration or filtering scripts from `src/` → write outputs to `data/02_processed/`.
3. Aggregate figure-ready tables into `data/03_final/`.
4. Keep instrument settings, datasheets, and meeting notes in `documentation/`.

---

## Contributing

- Do not rename or overwrite `01_raw/` files; add a new dated export instead.
- Prefer descriptive filenames (`iv_sweep_2025-03-08.csv` over `untitled2.csv`).
- Commit messages should state what changed and at which pipeline stage.

---

## License

Add a `LICENSE` file before distributing this repository publicly. Recommended options:

- **MIT** — permissive use of code and scripts
- **CC-BY-4.0** — attribution-required sharing of datasets and documentation

---

## Contact

Uzziel Perez — [uzzielperez25@gmail.com](mailto:uzzielperez25@gmail.com)
