# Origin / OriginPro workflow

[OriginLab Origin](https://www.originlab.com/) is used in many characterization labs for IV curves, noise spectra, and publication figures. This folder holds **LabTalk scripts** (`.ogs`) that mirror the Python/MATLAB dummy pipelines.

## Versions tested (reference)

| Product | Version | Notes |
|---------|---------|-------|
| Origin | 2024b | `impASC`, log axes, script window |
| OriginPro | 2024b | Same scripts; Pro-only templates optional |

Record the exact build in your DMP methods section when publishing figures.

## One-time setup

1. Clone the CNM repo and note the absolute path, e.g. `/Users/you/Desktop/CNM`.
2. In Origin: **Window → Script Window**, then run:

   ```labtalk
   CNM_DATA_DIR$ = "/Users/you/Desktop/CNM/";
   ```

   (Trailing slash required. Use forward slashes on macOS/Linux.)

3. Optional: **Set As Default** in the script window so `CNM_DATA_DIR$` persists for the session.

## Scripts

| Script | Input | Action |
|--------|-------|--------|
| `import_iv.ogs` | `datasets/march8.csv` | Import IV sweep, log Y axis |
| `import_noise.ogs` | `datasets/noise_NEW2.dat` | Log-log noise spectrum |
| `plot_bode.ogs` | `datasets/FINAL_v3_USETHIS.csv` | Bode gain vs frequency |

Run via **File → Script → Run Script** or paste into the Script Window.

## Recommended GUI workflow (no scripting)

1. **File → Import → Single ASCII** → select CSV/DAT.
2. For `.dat` files: set delimiter to **space**, skip rows starting with `#`.
3. Set column designations (X, Y, Y error) on the worksheet.
4. **Plot → Line + Symbol**; use **Axis → Scale** for log10 where needed.
5. Export figures: **File → Export Graphs** → PNG/PDF at 300 DPI for papers.

## Project files

Store reusable graph templates as `docs/origin_templates/` (not committed until cleaned). Binary `.opju` projects are poor for Git; prefer CSV in `datasets/` plus `.ogs` scripts in this folder.

## Licence

Origin is commercial software. Scripts in this directory are MIT-licensed (see repo `LICENSE`); Origin itself requires a separate OriginLab licence.
