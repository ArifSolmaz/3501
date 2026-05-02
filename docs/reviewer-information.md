---
layout: page
title: Reviewer Information
---

# Reviewer Information

This page gives a compact route through the public pre-analysis material.

## Scientific Claim

Starspot occultations and unocculted active regions can introduce apparent transit mid-time shifts at the seconds-to-minutes level. These shifts can mimic or contaminate TTV, orbital-decay, apsidal-precession, and ephemeris-update analyses if they are not explicitly modelled or flagged.

The proposed work develops a decision framework rather than a black-box correction: it asks when correction is justified, when uncertainty inflation is more defensible, and when a transit should be excluded.

## Evidence Level In The Current Public Package

The public package currently supports:

- numerical consistency checks for the main pre-analysis timing claims;
- cross-method timing comparison across the four timing validation systems;
- MAST/Lightkurve/JWST archive-source manifests;
- selected pre-analysis figures;
- scripts that reproduce the audit when run inside the full local analysis environment.

The most important scientific caution is HAT-P-36b: it is intentionally treated as a harder validation case because the method spread is larger than in HAT-P-11b, WASP-19b, and WASP-52b.

## What Reviewers Should Check First

1. The RMS timing values in [Science Audit](science-audit.md).
2. The method-agreement table, especially the HAT-P-36b caution case.
3. The injection-recovery result and its limitations.
4. The MAST/JWST archive manifest for source traceability.
5. The domain-gap discussion for machine-learning generalization.

## Planned Public Updates

If the project is accepted, this site will be updated with accepted-scope summaries, code releases, additional validation products, publications, conference materials, and corrected ephemeris/data products as they become ready for public release.

