---
layout: home
title: 3501 Pre-Analysis
---

# 3501 Pre-Analysis

Public pre-analysis materials for the project:

**Comprehensive Characterization and Correction of Starspot-Induced Systematic Effects on Exoplanet Transit Mid-Time Measurements**

This site publishes a public-safe subset of the pre-analysis work: selected figures, numerical audit results, MAST/JWST source manifests, and reproducibility scripts.

It does **not** publish the full TUBITAK application forms, budget files, personal/provenance files, or large cached raw/archive data.

## Key Audit Results

| Quantity | Audit result |
| --- | ---: |
| HAT-P-11b O-C RMS | 62.55 s |
| WASP-19b O-C RMS | 80.27 s |
| HAT-P-36b O-C RMS | 144.98 s |
| WASP-52b O-C RMS | 22.18 s |
| Homogeneous timing sample | 193 transits |
| Injection-recovery improvement | 32.4% |
| GJ 1214b white-light depth | 13,775 ppm |
| GJ 1214b white-light residual RMS | 293 ppm |

## Figures

### HAT-P-11b Spot-Crossing Examples

![HAT-P-11b spot crossing examples](assets/figures/hatp11b_spot_crossings.png)

### HAT-P-11b O-C Diagram

![HAT-P-11b O-C diagram](assets/figures/hatp11b_oc_diagram.png)

### Synthetic CNN Metrics

![CNN synthetic metrics](assets/figures/cnn_synthetic_metrics.png)

### GJ 1214b JWST/MIRI White-Light Curve

![GJ 1214b JWST white-light curve](assets/figures/gj1214b_jwst_white_light.png)

### Simulation-Observation Validation

![Simulation observation validation](assets/figures/simulation_observation_validation.png)

### Additional Validation Targets

![New target pre-analysis](assets/figures/new_targets_preanalysis.png)

## Public Materials

- [Science audit](science-audit.md)
- [MAST/JWST archive manifest](mast-query-summary.md)
- [Reproducibility notes](reproducibility.md)
- [Numerical audit JSON](data/numerical_claim_audit.json)
- [MAST query JSON](data/mast_query_summary.json)
- [Audit script](scripts/audit_numerical_claims.py)
- [Archive query script](scripts/query_primary_sources.py)

