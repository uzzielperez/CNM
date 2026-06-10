# Data Management Plan — CNM

**Template:** Horizon Europe Data Management Plan v1.1 (01.04.2022)  
**Project acronym:** CNM  
**Project name:** Semiconductor Device Characterization Data (180 nm CMOS)  
**Deliverable:** DMP (repository-level; standalone research dataset)  
**Version:** 1.1  
**Date:** 10/06/2025  
**Dissemination level:** Public  
**Author(s):** Uzziel Perez  
**Data steward:** uzzielperez25@gmail.com  
**Repository:** https://github.com/uzzielperez/CNM  

---

## History of changes

| Version | Publication date | Change |
|---------|------------------|--------|
| 1.0 | 10/06/2025 | Initial DMP; FAIR inventory; EU access policy |
| 1.1 | 10/06/2025 | Analysis pipelines (`src/`); formal HE PDF export |

---

## 1. Data summary

### 1.1 Purpose of data generation and relation to project objectives

The CNM repository collects and curates semiconductor device characterization data for 180 nm CMOS technology. The data support device-level and circuit-level research objectives:

- Extraction of DC parameters (threshold voltage, Ion, Ioff, subthreshold swing)
- Validation of process-corner and Monte Carlo simulation setups
- Analysis of 1/f noise and AC frequency response
- Wafer-level yield and figures-of-merit benchmarking

Data enable comparison of measured versus simulated device behaviour, production of publication figures, and documentation of calibration conditions for reproducibility.

**Technology context:** 180 nm PDK; nominal supply 1.8 V; process corners tt, ff, ss, fs, sf.

### 1.2 Re-use of existing data

No third-party datasets are currently reused. External 180 nm PDK model files are referenced in documentation but not redistributed due to foundry intellectual property restrictions (see Sections 2.2 and 6).

| Asset ID | Filename | Generated / Reused | Origin | Purpose |
|----------|----------|-------------------|--------|---------|
| D1 | march8.csv | Generated | Lab IV measurement | DC sweep validation |
| D2 | copy of copy of IV_curves.xlsx.csv | Generated | Spreadsheet export | Raw IV reference |
| D3 | noise_NEW2.dat | Generated | Noise analyser | 1/f noise characterisation |
| D4 | asdfgraph.png.csv | Generated | Plot export | Trace archival |
| D5 | data1.csv | Generated | Bench measurement | Sample V–I curve |
| D6 | Measurements - Juan - version2 - corrected.csv | Generated | Post-processed lab data | Calibrated DC parameters |
| D7 | untitled2.csv | Generated | Switch bench | Ron/Roff ratios |
| D8 | FINAL_v3_USETHIS.csv | Generated | AC analyser + processing | Figure-ready frequency response |
| D9 | definitive_DEFINITIVE.csv | Generated | Wafer test | Yield / fmax benchmarking |
| D10 | docs/*.txt | Generated | Lab notes | Provenance and methods |

### 1.3 Types and formats of data

| Data type | Format | Generation software | Open format |
|-----------|--------|---------------------|-------------|
| Tabular measurements | CSV (UTF-8, comma-separated) | Instruments, spreadsheets, Python/pandas | Yes |
| Noise spectra | DAT (ASCII, whitespace-delimited) | Noise analyser export | Yes |
| Lab notes | TXT (UTF-8) | Plain text editor | Yes |
| Analysis code | PY, M, OGS | Python, MATLAB, Origin LabTalk | Yes |

Preferred formats follow UK Data Service recommendations: plain text and non-proprietary tabular formats.

### 1.4 Provenance

| Pipeline stage | Repository path | Rule |
|----------------|-----------------|------|
| Raw instrument output | data/01_raw/ | Read-only; append dated exports only |
| Calibrated / filtered | data/02_processed/ | Document transformations in src/ or docs/ |
| Figure-ready matrices | data/03_final/ | Versioned; cite in publications |
| Methods and calibration | docs/ | Linked from dataset metadata |

Each dataset records who collected it, when, with which instrument, under which bias/temperature, and what processing was applied.

### 1.5 Expected data size

| Category | Approximate size |
|----------|------------------|
| Current repository | < 5 MB |
| Per measurement campaign | < 50 MB |
| Full project (estimated) | < 500 MB |

### 1.6 Data utility

Target users: semiconductor device researchers, analog/RF circuit designers, reliability and yield engineers, reproducibility reviewers, and EOSC metadata harvesters.

Keywords: semiconductor characterization, CMOS, 180nm, IV curves, 1/f noise, threshold voltage, wafer yield, process corners, Monte Carlo, FAIR data.

---

## 2. FAIR data

### 2.1 Making data findable, including provisions for metadata

| Measure | Status | Planned action |
|---------|--------|----------------|
| Persistent identifier (DOI) | Planned | Zenodo deposition (EOSC-aligned) |
| Version control | Active | Git tags per release (e.g. v1.0.0) |
| Descriptive metadata | Active | README + this DMP |
| Sidecar metadata | Planned | metadata/ YAML per DataCite Schema 4.4 |
| Discovery indexing | Partial | GitHub; full after Zenodo DOI |

Minimum metadata per deposition: title, creators, description, keywords, licence (CC-BY-4.0), version, publication date, related identifiers. Dublin Core and DataCite-compatible fields will be used. Metadata will be harvestable via Zenodo and GitHub.

### 2.2 Making data accessible

#### 2.2.1 Repository

Primary working repository: GitHub (https://github.com/uzzielperez/CNM).  
Archival repository (planned): Zenodo — trusted, metadata-ready, EOSC-federated general-purpose repository.

#### 2.2.2 Data

Principle: *As open as possible, as closed as necessary* (Horizon Europe Programme Guide).

| Data class | Access | Licence | Restriction |
|------------|--------|---------|-------------|
| Measurement CSV/DAT/TXT | Open | CC-BY-4.0 | None; no personal data |
| Lab notes | Open | CC-BY-4.0 | Redact third-party names on request |
| 180 nm PDK / foundry models | Not distributed | N/A | IPR / contractual (foundry NDA) |
| Pre-publication embargo | None currently | — | Max. embargo if patents filed |

Access protocol: HTTPS git clone and direct download. No authentication for open datasets.

#### 2.2.3 Metadata

Metadata openly available under CC0. Metadata includes access conditions and contact point even if datasets are later restricted.

Contact: uzzielperez25@gmail.com

### 2.3 Making data interoperable

Repository structure:

- data/01_raw/ — factory and instrument outputs (read-only)
- data/02_processed/ — calibrated tables
- data/03_final/ — publication-ready matrices
- src/ — analysis pipelines (Python, MATLAB, Origin)
- DataManagementPlan/ — formal DMP (this document)
- docs/ — calibration sheets and lab notes
- metadata/ — DataCite sidecars (planned)

Interoperability: UTF-8 encoding; SI units in headers; consistent column naming (vgs, vds, ids, freq_hz, temp_c); CSV RFC 4180 compliance.

### 2.4 Increase data re-use

| Output | Licence | Citation requirement |
|--------|---------|---------------------|
| Datasets | CC-BY-4.0 | DOI + version tag |
| Software (src/) | MIT | Repository + release tag |
| Documentation | CC-BY-4.0 | Same as datasets |

Reuse tools: Python 3.10+ (pandas), MATLAB R2021a+, Origin 2021+. See repository README Section 9 and src/ for pipelines.

Downstream users must cite the DOI, not redistribute PDK content, and document derivative processing.

---

## 3. Other research outputs

| Output | Location | Preservation |
|--------|----------|--------------|
| Analysis scripts | src/ | Git + Zenodo archive |
| Figures from 03_final/ | Publications / Zenodo | Link to source CSV |
| SPICE netlists | src/ or docs/ | Git; exclude NDA decks |
| Presentations | DataManagementPlan/ or Zenodo | Supplementary material |

Software documentation follows Lee et al. (2014) Ten simple rules for documenting scientific software.

---

## 4. Allocation of resources

| Activity | Responsible | Effort |
|----------|-------------|--------|
| Data curation | Data steward | ~2 h/month |
| DMP / README updates | Data steward | Quarterly |
| Zenodo DOI registration | Data steward | ~1 h per release |
| Backup verification | Data steward | Annually |
| Storage | GitHub + Zenodo free tier | €0 at current volume |

---

## 5. Data security

| Risk | Mitigation |
|------|------------|
| Overwrite of raw data | data/01_raw/ append-only; Git history |
| Data loss | GitHub remote + Zenodo snapshots |
| Unauthorised modification | Branch protection; immutable release tags |
| Confidential leakage | No PDK/foundry files in repository |
| Local workstation loss | Push after each curated batch |

Standard institutional IT policies apply. No sensitive personal data stored (Section 6).

---

## 6. Ethics

| Topic | Assessment |
|-------|------------|
| Human subjects | Not applicable — device measurements only |
| GDPR | Not applicable for current assets; reassess if personal data added |
| Intellectual property | Measurement data CC-BY-4.0; PDK is third-party IP |
| Export control | Characterization results only; review if fabrication details added |
| Ethics committee | Not required for ex vivo device testing |

---

## 7. Other issues

- Legacy path datasets/ is being migrated to data/01_raw/, data/02_processed/, data/03_final/.
- Zenodo DOI and ORCID to be added before formal grant submission.
- Grant agreement number and institution to be inserted when CNM is linked to a funded Horizon Europe project.
- This DMP is a living document; review annually or before each Zenodo release.

---

**End of Data Management Plan**
