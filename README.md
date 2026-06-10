# CNM — Semiconductor Device Characterization Data

| Field | Value |
|-------|-------|
| **Repository** | [github.com/uzzielperez/CNM](https://github.com/uzzielperez/CNM) |
| **Data steward** | Uzziel Perez ([uzzielperez25@gmail.com](mailto:uzzielperez25@gmail.com)) |
| **DMP version** | 1.0 |
| **Last reviewed** | 2025-06-10 |
| **Dissemination** | Public (measurement data); restricted elements noted in §2.2 |
| **Policy basis** | Horizon Europe GA Art. 17 · FAIR principles · *as open as possible, as closed as necessary* |

Semiconductor device characterization data for **180 nm CMOS** devices: IV curves, 1/f noise spectra, AC frequency response, and wafer-level yield summaries. This README serves as the **repository landing page** and a **condensed Data Management Plan (DMP)** aligned with EU research-data requirements (Horizon Europe DMP template v1.1, Science Europe core requirements).

**Technology context:** 180 nm PDK · nominal supply 1.8 V · process corners `tt`, `ff`, `ss`, `fs`, `sf`

---

## 1. Data summary

### 1.1 Purpose and relation to research objectives

These datasets support **device-level and circuit-level characterization** of 180 nm CMOS technology: extracting DC parameters (Vth, Ion, Ioff, subthreshold swing), validating corner and Monte Carlo simulation setups, analysing noise performance, and tracking wafer yield. Data are used to:

- Compare measured vs. simulated device behaviour
- Produce publication figures (Bode plots, IV curves, yield maps)
- Document calibration and experimental conditions for reproducibility

### 1.2 Data reuse

| Asset ID | Name | Generated / Reused | Origin | Purpose |
|----------|------|-------------------|--------|---------|
| D1 | `march8.csv` | Generated | Lab IV measurement export | DC sweep validation |
| D2 | `copy of copy of IV_curves.xlsx.csv` | Generated | Spreadsheet instrument export | Raw IV reference |
| D3 | `noise_NEW2.dat` | Generated | Noise analyser export | 1/f noise characterisation |
| D4 | `asdfgraph.png.csv` | Generated | Plot/trace export | Trace archival |
| D5 | `data1.csv` | Generated | Bench measurement | Sample V–I curve |
| D6 | `Measurements - Juan - version2 - corrected.csv` | Generated | Post-processing of lab data | Calibrated DC parameters |
| D7 | `untitled2.csv` | Generated | Switch characterisation bench | Ron/Roff ratios |
| D8 | `FINAL_v3_USETHIS.csv` | Generated | AC analyser + post-processing | **Figure-ready** frequency response |
| D9 | `definitive_DEFINITIVE.csv` | Generated | Wafer test summary | Yield / fmax benchmarking |
| D10 | `docs/*.txt` | Generated | Lab notes & meeting records | Provenance & methods documentation |

No third-party datasets are currently reused. External PDK model files (180 nm) are **referenced but not redistributed** — see §2.2 and §6.

### 1.3 Data types and formats

| Type | Format | Software / instrument | Open format? |
|------|--------|----------------------|--------------|
| Tabular measurements | `.csv` | Spreadsheet, Python/pandas | Yes |
| Noise spectra | `.dat` (ASCII, header comments) | Noise analyser export | Yes |
| Lab notes | `.txt` (UTF-8) | Plain text editor | Yes |
| Analysis code (planned) | `.py`, `.m`, or SPICE netlists | TBD under `src/` | Yes (target) |

Preferred formats follow [UK Data Service recommended formats](https://ukdataservice.ac.uk/learning-hub/research-data-management/format-your-data/): plain text and non-proprietary tabular formats for long-term readability.

### 1.4 Provenance

| Stage | Location | Rule |
|-------|----------|------|
| Raw instrument output | `data/01_raw/` | **Read-only.** Never overwrite; append dated exports. |
| Calibrated / filtered | `data/02_processed/` | Document transformation in `src/` or `documentation/`. |
| Figure-ready matrices | `data/03_final/` | Versioned; cite in publications. |
| Methods & calibration | `documentation/` | Linked from dataset README sidecars. |

Each dataset should carry a companion `README` or metadata row stating: **who** collected it, **when**, **with which instrument**, **under which bias/temperature**, and **what processing** was applied.

### 1.5 Expected data volume

| Category | Approx. size | Growth rate |
|----------|-------------|-------------|
| Current repository | < 5 MB | — |
| Per measurement campaign | < 50 MB | Low (tabular ASCII) |
| Full project (estimated) | < 500 MB | Unless raw waveform dumps are added |

### 1.6 Data utility (target users)

| User group | Expected use |
|------------|--------------|
| Semiconductor device researchers | Benchmark 180 nm device parameters |
| Analog/RF circuit designers | Validate simulation corners and noise models |
| Reliability & yield engineers | Compare wafer-level fmax and power figures |
| Reproducibility reviewers | Audit methods and reproduce figures |
| EU Open Science / EOSC harvesters | Discover metadata via repository DOI (planned) |

**Keywords:** `semiconductor characterization`, `CMOS`, `180nm`, `IV curves`, `1/f noise`, `threshold voltage`, `wafer yield`, `process corners`, `Monte Carlo`, `FAIR data`

---

## 2. FAIR data management

### 2.1 Findable — identifiers and metadata

| Measure | Status | Action |
|---------|--------|--------|
| Persistent identifier (DOI) | Planned | Deposit release snapshots on [Zenodo](https://zenodo.org) (EOSC-aligned, general-purpose repository) |
| Version control | Active | Git tags per release (e.g. `v1.0.0`) |
| Descriptive metadata | This README | Dublin Core / DataCite-compatible fields below |
| Sidecar metadata | Planned | `metadata/` YAML or JSON per dataset (DataCite Schema 4.4) |
| Discovery indexing | Partial | GitHub search; full indexing after Zenodo DOI registration |

**Minimum metadata record (per deposition):**

```yaml
title: "CNM — <dataset name>"
creators:
  - name: "Perez, Uzziel"
    affiliation: "<institution>"
    orcid: "<ORCID>"          # add when available
description: "<abstract>"
keywords: [CMOS, 180nm, IV, noise, characterization]
license: CC-BY-4.0
version: "1.0.0"
date: "YYYY-MM-DD"
related_identifier:
  - identifier: "10.xxxx/zenodo.xxxxx"   # after archival
    relationType: IsVersionOf
```

### 2.2 Accessible — repository, embargo, and restrictions

**Principle:** *As open as possible, as closed as necessary* (Horizon Europe Programme Guide).

| Data class | Access | Repository | Licence | Restriction rationale |
|------------|--------|------------|---------|----------------------|
| Measurement CSV/DAT/TXT | Open | GitHub + Zenodo (planned) | **CC-BY-4.0** | None — no personal data |
| Lab notes (`documentation/`) | Open | Same | CC-BY-4.0 | Redact third-party names if requested |
| 180 nm PDK / foundry models | **Not included** | N/A | Foundry NDA | **IPR / contractual** — refer to vendor licence only |
| Pre-publication embargo | None currently | — | — | Apply max. embargo needed for IP review if patents filed |

**Access protocol:** HTTPS clone (`git`) and direct file download from GitHub/Zenodo. No authentication required for open datasets. Metadata will remain openly available under **CC0** even if a future dataset requires restricted access (per Grant Agreement practice).

**Contact for access questions:** [uzzielperez25@gmail.com](mailto:uzzielperez25@gmail.com)

### 2.3 Interoperable — standards, vocabularies, and structure

```
CNM/
├── README.md                 # Landing page + condensed DMP (this file)
├── LICENSE                   # CC-BY-4.0 (data) + MIT (code) — add before release
├── CITATION.cff              # Machine-readable citation (planned)
├── data/
│   ├── 01_raw/               # READ-ONLY factory / instrument outputs
│   ├── 02_processed/         # Calibrated, noise-filtered tables
│   └── 03_final/             # Matrices for figures and reports
├── src/                      # Analysis pipelines and automation
├── documentation/            # Calibration sheets, datasheets, lab notes
└── metadata/                 # DataCite / Dublin Core sidecars (planned)
```

**Interoperability measures:**

- UTF-8 encoding; decimal point `.`; SI units in column headers where possible (`vdd_v`, `freq_hz`, `temp_c`)
- Consistent column naming across related tables (`vgs`, `vds`, `ids`)
- CSV RFC 4180 compliance (quoted fields where names contain spaces)
- Link to [FAIRsharing](https://fairsharing.org) entry when discipline standard is adopted

### 2.4 Reusable — licences, tools, and provenance chain

| Output | Licence | Citation |
|--------|---------|----------|
| Datasets | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) | DOI + version tag |
| Software (`src/`) | [MIT](https://opensource.org/licenses/MIT) | Repository + release tag |
| Documentation | CC-BY-4.0 | Same as datasets |

**Reuse requirements for downstream users:**

1. Cite the repository DOI and dataset version used.
2. Do not redistribute foundry PDK content not included in this repo.
3. Document any further processing in a fork or derivative dataset.

**Tools for validation / reuse (planned under `src/`):**

- Python 3.x + pandas for tabular ingestion
- SPICE simulator (vendor-specific) for simulation replay — document version in `documentation/`

---

## 3. Other research outputs

| Output type | Location | Preservation |
|-------------|----------|--------------|
| Analysis scripts | `src/` (planned) | Git + Zenodo code archive |
| Figures derived from `03_final/` | Publications / Zenodo | Link back to source CSV |
| SPICE netlists | `src/` or `documentation/` | Git; exclude NDA-restricted foundry decks |
| Presentations | External / `documentation/` | Zenodo supplementary material |

Software should follow [Ten simple rules for documenting scientific software](https://doi.org/10.1371/journal.pcbi.1003285) (Lee et al., 2014).

---

## 4. Allocation of resources

| Activity | Responsible | Effort (est.) |
|----------|-------------|---------------|
| Data curation & naming | Data steward | Ongoing, ~2 h/month |
| README / DMP updates | Data steward | Quarterly review |
| Zenodo deposition & DOI | Data steward | Per major release (~1 h) |
| Backup verification | Data steward | Annually |
| Storage cost | GitHub (free tier) + Zenodo (free) | €0 at current volume |

Costs are negligible at current scale (< 500 MB). Budget for institutional repository fees if volume exceeds free-tier limits.

---

## 5. Data security and backup

| Risk | Mitigation |
|------|------------|
| Accidental overwrite of raw data | `01_raw/` is append-only; Git history preserves prior states |
| Data loss | Primary: GitHub remote; secondary: Zenodo archival snapshot per release |
| Unauthorised modification | Branch protection on `main`; tagged releases immutable |
| Confidential leakage | Pre-commit review; no PDK/foundry files in repo |
| Ransomware / local loss | Push to remote after each curated batch |

No sensitive personal data are stored (see §6). Standard institutional IT security policies apply to workstations used for data collection.

---

## 6. Ethics, legal compliance, and GDPR

| Topic | Assessment |
|-------|------------|
| **Human subjects / personal data** | **Not applicable.** Datasets contain device measurements only; no names, health data, or identifiers. GDPR processing basis not required for current assets. |
| **GDPR** | If future datasets include personal data (e.g. operator logs with names), a separate GDPR assessment, lawful basis, and retention schedule will be added; data minimisation and pseudonymisation will apply. |
| **Intellectual property** | Measurement data: project-owned, released under CC-BY-4.0. **180 nm PDK models are third-party IP** — cite vendor documentation; do not commit NDA-protected files. |
| **Export control** | Review institutional policy if sharing detailed fabrication parameters; current files are characterization results only. |
| **Ethics committee** | Not required for ex vivo device testing; reassess if human or animal data are introduced. |

---

## 7. Dataset inventory (current files)

Legacy paths are being migrated to the standard tree below.

| File | Description | Target path | FAIR stage |
|------|-------------|-------------|------------|
| `march8.csv` | IV sweep (`vgs`, `vds`, `ids`, `temp_c`) | `data/01_raw/` | Raw |
| `copy of copy of IV_curves.xlsx.csv` | Raw IV export | `data/01_raw/` | Raw |
| `noise_NEW2.dat` | Noise spectra (`freq`, `Sv`, `Si`) | `data/01_raw/` | Raw |
| `asdfgraph.png.csv` | Exported trace data | `data/01_raw/` | Raw |
| `data1.csv` | Sample V–I sweep | `data/02_processed/` | Processed |
| `Measurements - Juan - version2 - corrected.csv` | Calibrated Vth, DIBL, Ion, Ioff | `data/02_processed/` | Processed |
| `untitled2.csv` | Ron/Roff ratios | `data/02_processed/` | Processed |
| `FINAL_v3_USETHIS.csv` | AC gain & phase vs. frequency | `data/03_final/` | **Final — use for figures** |
| `definitive_DEFINITIVE.csv` | Wafer yield summary | `data/03_final/` | Final |
| `docs/aaa.txt` | Simulation setup (PDK, corners, MC) | `documentation/` | Provenance |
| `docs/results_copy.txt` | Vth summary extract | `documentation/` | Provenance |
| `docs/meeting_notes_also_has_data.txt` | Meeting notes, leakage table | `documentation/` | Provenance |

> Never edit `01_raw/` in place. Derive new tables in `02_processed/` or `03_final/` and log the transformation.

---

## 8. Key reference results

nMOS, W/L = 10/0.18 µm (`documentation/results_copy.txt`):

| Parameter | Value |
|-----------|-------|
| Vth | 0.42 V |
| Ioff | 1.2 nA |
| Ion | 580 µA |
| Subthreshold swing | 68 mV/dec |

Corner leakage (`documentation/meeting_notes_also_has_data.txt`):

| Corner | Temp (°C) | Ileak |
|--------|-----------|-------|
| tt | 27 | 1.2 nA |
| ff | −40 | 0.3 nA |
| ss | 125 | 18.7 nA |
| fs | 27 | 1.4 nA |
| sf | 27 | 1.1 nA |

**Simulation context** (`documentation/aaa.txt`): 180 nm PDK · corners `tt ff ss fs sf` · VDD = 1.8 V · Monte Carlo = 500 runs.

---

## 9. How to access and cite

### Clone

```bash
git clone git@github.com:uzzielperez/CNM.git
cd CNM
```

### Cite (until DOI is registered)

```bibtex
@misc{perez2025cnm,
  author       = {Perez, Uzziel},
  title        = {{CNM}: Semiconductor Device Characterization Data (180 nm CMOS)},
  year         = {2025},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/uzzielperez/CNM}},
  note         = {DMP v1.0; dataset version: git tag or commit SHA}
}
```

After Zenodo deposition, replace `howpublished` with `doi = {10.xxxx/zenodo.xxxxx}`.

---

## 10. Contributing and data quality

1. Raw exports → `data/01_raw/` with date-stamped filenames (`iv_sweep_2025-03-08.csv`).
2. Processing scripts → `src/`; outputs → `02_processed/` or `03_final/`.
3. Commit messages state **pipeline stage** and **transformation** (e.g. `processed: calibrate Vth from march8 raw`).
4. Open a GitHub Issue for data-quality flags (outliers, instrument drift, relabelling).

FAIR principles do not guarantee intrinsic data quality — always inspect `01_raw/` provenance before citing processed values.

---

## 11. DMP revision history

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-06-10 | Uzziel Perez | Initial DMP-compliant README; FAIR inventory; EU access policy |

*This DMP is a living document. Review and update at least once per project year or before each Zenodo release.*

---

## 12. Contact

**Data steward:** Uzziel Perez — [uzzielperez25@gmail.com](mailto:uzzielperez25@gmail.com)

For Horizon Europe reporting: reference this repository in the project DMP deliverable and keep both documents synchronised on version and access conditions.
