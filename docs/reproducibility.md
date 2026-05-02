---
layout: page
title: Reproducibility
---

# Reproducibility Notes

## Included Public Materials

- Selected pre-analysis figures.
- Numerical audit JSON.
- MAST/JWST query JSON.
- Audit scripts.

## Intentionally Excluded

- TUBITAK application DOCX/PDF forms.
- Budget files.
- Personal/provenance files.
- Large cached archive products, including FITS, HDF5, and NPZ data caches.
- Any data product that should remain private until paper submission or archive release.

## Re-run The Public Audit Scripts

The scripts on this public site are designed to be copied into the full local analysis bundle, where the cached data products exist:

```bash
python3 scripts/audit_numerical_claims.py
python3 scripts/query_primary_sources.py
```

`query_primary_sources.py` performs metadata queries and avoids large downloads by default.

## Suggested Public Statement

"This repository contains selected pre-analysis figures, numerical audit summaries, and archive-source manifests for reproducibility. It is not a complete detector-level reanalysis package and does not include the full TUBITAK application files or large raw/archive data caches."

