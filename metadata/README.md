# CNM experiment metadata (JSON)

Sidecar JSON files bridge **human-readable lab records** and **automated pipelines** (Python, MATLAB, Origin, agentic tools). Each file sits beside its dataset and follows a shared schema.

## Schema (v1.0.0)

| Key | Type | Description |
|-----|------|-------------|
| `metadata_version` | string | Semver of this schema (e.g. `1.0.0`) |
| `experiment_id` | string | Unique run ID: `YYYY-CNM-<TYPE>-NNN` |
| `hardware_setup` | object | Instruments, DUT, gain, sampling |
| `experimental_conditions` | object | Bias, temperature, corner, geometry |
| `data_files` | object | Paths to raw/processed/final files (repo-relative) |

**Conventions:** lowercase keys with underscores; SI units in key names (`_v`, `_a`, `_hz`, `_c`, `_db`); paths relative to repository root.

## Files

| JSON | Dataset | Experiment type |
|------|---------|-----------------|
| `march8_iv_sweep.json` | `datasets/march8.csv` | DC IV sweep |
| `noise_NEW2.json` | `datasets/noise_NEW2.dat` | 1/f noise spectrum |
| `final_ac_response.json` | `datasets/FINAL_v3_USETHIS.csv` | AC / Bode response |
| `definitive_yield.json` | `datasets/definitive_DEFINITIVE.csv` | Wafer yield summary |
| `index.json` | — | Catalogue of all experiment records |

## Load in Python

```python
import json
from pathlib import Path

meta = json.loads(Path("metadata/march8_iv_sweep.json").read_text())
raw = Path(meta["data_files"]["raw_tabular"])
```

## Regenerate

Add a new JSON when a new raw export lands in `data/01_raw/`. Bump `metadata_version` only when the schema itself changes.
