#!/usr/bin/env python3
"""Query primary archive sources used by the science audit.

The default mode writes metadata/manifests only. It intentionally avoids large
downloads; raw JWST rateints/uncal products for a single system can be many GB.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


AUDIT_DIR = Path(__file__).resolve().parents[1]
MAST_DIR = AUDIT_DIR / "mast_queries"

LIGHTCURVE_QUERIES = [
    {"target": "HAT-P-11", "mission": "Kepler"},
    {"target": "Kepler-17", "mission": "Kepler"},
    {"target": "WASP-19", "mission": "TESS"},
    {"target": "HAT-P-36", "mission": "TESS"},
    {"target": "WASP-52", "mission": "TESS"},
]

JWST_QUERIES = [
    {"objectname": "WASP-52", "obs_collection": "JWST"},
    {"objectname": "GJ 1214", "obs_collection": "JWST"},
]


def cell(value: Any) -> Any:
    if hasattr(value, "item"):
        try:
            return value.item()
        except Exception:
            pass
    if value is None:
        return None
    text = str(value)
    return None if text in {"--", "masked"} else text


def query_lightcurves() -> list[dict[str, Any]]:
    import lightkurve as lk

    out: list[dict[str, Any]] = []
    for query in LIGHTCURVE_QUERIES:
        target = query["target"]
        mission = query["mission"]
        try:
            result = lk.search_lightcurve(target, mission=mission)
            rows = []
            table = result.table
            for row in table[:15]:
                rows.append({name: cell(row[name]) for name in table.colnames})
            out.append(
                {
                    "target": target,
                    "mission": mission,
                    "n_products": len(result),
                    "first_rows": rows,
                    "status": "ok",
                }
            )
        except Exception as exc:
            out.append(
                {
                    "target": target,
                    "mission": mission,
                    "status": "error",
                    "error": f"{type(exc).__name__}: {exc}",
                }
            )
    return out


def product_summary(products: Any) -> dict[str, Any]:
    science = [row for row in products if str(row.get("productType", "")).upper() == "SCIENCE"]
    fits = [row for row in science if str(row.get("productFilename", "")).endswith(".fits")]
    by_subgroup: dict[str, int] = {}
    total_size = 0
    first_fits = []
    for row in fits:
        subgroup = str(row.get("productSubGroupDescription", "UNKNOWN"))
        by_subgroup[subgroup] = by_subgroup.get(subgroup, 0) + 1
        try:
            total_size += int(row.get("size", 0))
        except Exception:
            pass
        if len(first_fits) < 12:
            first_fits.append(
                {
                    "filename": cell(row.get("productFilename")),
                    "calib_level": cell(row.get("calib_level")),
                    "subgroup": subgroup,
                    "size_bytes": cell(row.get("size")),
                }
            )
    return {
        "science_products": len(science),
        "science_fits": len(fits),
        "science_fits_size_bytes": total_size,
        "science_fits_by_subgroup": by_subgroup,
        "first_science_fits": first_fits,
    }


def query_jwst() -> list[dict[str, Any]]:
    from astroquery.mast import Observations

    out: list[dict[str, Any]] = []
    for query in JWST_QUERIES:
        objectname = query["objectname"]
        try:
            obs = Observations.query_criteria(**query)
            entries = []
            for row in obs:
                products = Observations.get_product_list(row)
                entry = {
                    "obs_id": cell(row.get("obs_id")),
                    "target_name": cell(row.get("target_name")),
                    "instrument_name": cell(row.get("instrument_name")),
                    "filters": cell(row.get("filters")),
                    "proposal_id": cell(row.get("proposal_id")),
                    "data_rights": cell(row.get("dataRights")),
                }
                entry.update(product_summary(products))
                entries.append(entry)
            out.append(
                {
                    "objectname": objectname,
                    "n_observations": len(obs),
                    "observations": entries,
                    "status": "ok",
                }
            )
        except Exception as exc:
            out.append(
                {
                    "objectname": objectname,
                    "status": "error",
                    "error": f"{type(exc).__name__}: {exc}",
                }
            )
    return out


def write_markdown(summary: dict[str, Any], path: Path) -> None:
    lines = [
        "# MAST Primary Source Query Summary",
        "",
        f"Generated: {summary['generated_utc']} UTC",
        "",
        "This file records live archive metadata queries. It is a manifest, not a raw data download.",
        "",
        "## Kepler/TESS Light Curves",
        "",
        "| Target | Mission | Products | Status |",
        "| --- | --- | ---: | --- |",
    ]
    for row in summary["lightcurves"]:
        lines.append(f"| {row['target']} | {row['mission']} | {row.get('n_products', 0)} | {row['status']} |")

    lines.extend(["", "## JWST Observations", "", "| Object | Observations | Status |", "| --- | ---: | --- |"])
    for row in summary["jwst"]:
        lines.append(f"| {row['objectname']} | {row.get('n_observations', 0)} | {row['status']} |")

    lines.extend(
        [
            "",
            "## Raw Reanalysis Extension",
            "",
            "For a detector-level JWST rerun, use these manifests to select the exact `uncal.fits` or `rateints.fits` files, then process them with the current JWST calibration pipeline plus a time-series spectroscopy package. Use x1dints only for raw-adjacent verification, not as a substitute for raw detector reduction.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-lightkurve", action="store_true", help="Skip Kepler/TESS light-curve archive queries")
    parser.add_argument("--skip-jwst", action="store_true", help="Skip JWST observation/product archive queries")
    args = parser.parse_args()

    MAST_DIR.mkdir(parents=True, exist_ok=True)
    summary: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "lightcurves": [] if args.skip_lightkurve else query_lightcurves(),
        "jwst": [] if args.skip_jwst else query_jwst(),
    }
    json_path = MAST_DIR / "mast_query_summary.json"
    md_path = MAST_DIR / "MAST_QUERY_SUMMARY.md"
    json_path.write_text(json.dumps(summary, indent=2, ensure_ascii=True), encoding="utf-8")
    write_markdown(summary, md_path)
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")


if __name__ == "__main__":
    main()
