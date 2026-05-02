---
layout: page
title: Reproducibility
---

# Reproducibility Notes

## Public Materials

- Selected pre-analysis figures.
- Numerical audit JSON.
- MAST/JWST query JSON.
- Audit scripts.

## How To Use This Page

This public page is meant to help reviewers, collaborators, and readers inspect the scientific basis of the pre-analysis. It provides summary data products and scripts; larger working data products are referenced through archive manifests and can be regenerated or retrieved through the appropriate scientific archives.

The current public reproducibility level is a numerical and archive-source audit. A detector-level JWST rerun can be performed by selecting the relevant `uncal.fits` or `rateints.fits` files from the MAST manifest and processing them with a pinned JWST calibration environment.

## Re-run The Public Audit Scripts

The scripts on this public site are designed to be run inside the full analysis environment where the cached data products and result files exist:

```bash
python3 scripts/audit_numerical_claims.py
python3 scripts/query_primary_sources.py
```

`query_primary_sources.py` performs metadata queries and avoids large downloads by default.

## Suggested Citation Statement

"This repository contains public pre-analysis figures, numerical audit summaries, archive-source manifests, and reproducibility notes for the 3501 starspot timing-systematics project."
