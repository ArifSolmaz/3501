---
layout: page
title: Science Audit
---

# Independent Science Audit

Generated from the local application bundle on 2026-05-02.

## Bottom Line

This is a reproducibility and numerical-consistency audit. It re-derives the main quantitative claims from cached analysis products and checks JWST raw-adjacent `x1dints` products where available.

The audit is intended to make the pre-analysis easier to inspect by reviewers and collaborators. Detector-level JWST reruns can be extended from the archive manifests.

## Verified Numerical Claims

| Claim | Audit value | Status |
| --- | ---: | --- |
| HAT-P-11b O-C RMS | 62.55 s | verified |
| WASP-19b O-C RMS | 80.27 s | verified |
| HAT-P-36b O-C RMS | 144.98 s | verified |
| WASP-52b O-C RMS | 22.18 s | verified |
| Total homogeneous T0 sample | 193 transits | verified |
| Injection-recovery | 270 trials; MAE 48.4 -> 32.7 s; improvement 32.4% | verified |
| Synthetic CNN cached test | F1=0.993, ROC-AUC=0.99956, ECE=0.068 | verified from cache |
| GJ 1214b white-light depth/RMS | depth=13,775 ppm; RMS=293 ppm | verified |
| WASP-52b JWST/NIRISS x1dints anchor | 265 integrations | raw-adjacent verified |

## Cross-Method Timing Agreement

| System | Common epochs | Median absolute delta from epoch median | Median pairwise delta | Interpretation |
| --- | ---: | ---: | ---: | --- |
| HAT-P-11b | 20 | 0.11 s | 0.26 s | sub-second typical agreement |
| HAT-P-36b | 43 | 2.59 s | 5.37 s | caution: method spread is non-negligible |
| WASP-19b | 116 | 0.52 s | 1.49 s | sub-second typical agreement |
| WASP-52b | 14 | 0.26 s | 0.63 s | sub-second typical agreement |

The phrase "sub-second package-to-package differences in most systems" is defensible only under a median-absolute-deviation criterion. HAT-P-36b remains a hard validation case and should be discussed explicitly as such.

## Current Audit Scope

- Numerical timing claims are rechecked from local result products.
- JWST white-light products are checked at the raw-adjacent `x1dints`/derived-product level where available.
- MAST/JWST archive metadata are queried and recorded for source traceability.
- CNN cached metrics are validated; retraining requires the machine-learning environment described in the full analysis workflow.

## Scientific Assessment

The preliminary-science logic is coherent: observed active-star O-C scatter is large enough to matter, the scatter is mostly robust to transit-fitting package choice, and the simulation-observation gap motivates multi-spot and unocculted-spot modelling rather than undermining the project.

The weakest scientific point is the machine-learning domain-gap/generalization claim, not the existence of the starspot timing effect. The proposed staged thresholds, blind validation, uncertainty inflation, and exclusion pathway are therefore essential parts of the method.
