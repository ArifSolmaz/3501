---
layout: page
title: MAST/JWST Manifest
---

# MAST Primary Source Query Summary

This page records live archive metadata queries. It is a manifest, not a raw data download.

## Kepler/TESS Light Curves

| Target | Mission | Products | Status |
| --- | --- | ---: | --- |
| HAT-P-11 | Kepler | 52 | ok |
| Kepler-17 | Kepler | 47 | ok |
| WASP-19 | TESS | 25 | ok |
| HAT-P-36 | TESS | 12 | ok |
| WASP-52 | TESS | 4 | ok |

## JWST Observations

| Object | Observations | Status |
| --- | ---: | --- |
| WASP-52 | 6 | ok |
| GJ 1214 | 4 | ok |

## Raw Reanalysis Extension

For a detector-level JWST rerun, select the exact `uncal.fits` or `rateints.fits` products from the JSON manifest, then process them with a pinned JWST calibration pipeline and CRDS context. Use `x1dints` only for raw-adjacent verification, not as a substitute for detector-level reduction.

The full manifest is available as [mast_query_summary.json](data/mast_query_summary.json).

