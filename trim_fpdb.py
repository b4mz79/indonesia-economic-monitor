#!/usr/bin/env python3
"""Trim World Bank Indonesia RTFP CSV to 2016 onward and dashboard fields.

Usage:
    py -3 trim_fpdb.py fpdb.csv fpdb_2016.csv

Keeps the location/date fields used by dashboard-mikro.html plus every c_*
(close-price estimate) column so the dashboard commodity selector remains
fully populated. Rows before 2016-01-01 are excluded. If ISO3 exists, only IDN
rows are kept.
"""

from __future__ import annotations

import csv
import os
import sys
from pathlib import Path

CUTOFF = "2016-01-01"
BASE_COLUMNS = [
    "ISO3",
    "country",
    "adm1_name",
    "adm2_name",
    "mkt_name",
    "lat",
    "lon",
    "geo_id",
    "price_date",
    "year",
    "month",
    "currency",
    "data_coverage",
    "data_coverage_recent",
    "index_confidence_score",
    "spatially_interpolated",
]


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: py -3 trim_fpdb.py <input.csv> <output.csv>")
        return 2

    source = Path(sys.argv[1]).expanduser().resolve()
    target = Path(sys.argv[2]).expanduser().resolve()

    if not source.is_file():
        print(f"ERROR: input file not found: {source}")
        return 2
    if source == target:
        print("ERROR: output must be a different file; source is never overwritten.")
        return 2

    source_size = source.stat().st_size
    total_rows = 0
    kept_rows = 0
    skipped_date = 0
    skipped_country = 0

    try:
        with source.open("r", encoding="utf-8-sig", newline="") as src:
            reader = csv.DictReader(src)
            if not reader.fieldnames:
                raise ValueError("CSV has no header row")

            headers = [h.strip() for h in reader.fieldnames]
            available = set(headers)
            required = {"price_date", "adm1_name", "adm2_name", "mkt_name"}
            missing = sorted(required - available)
            if missing:
                raise ValueError("missing required columns: " + ", ".join(missing))

            close_columns = [h for h in headers if h.startswith("c_")]
            if not close_columns:
                raise ValueError("no c_* close-estimate columns found")

            keep_columns = [c for c in BASE_COLUMNS if c in available] + close_columns
            # Preserve original column order and avoid duplicates.
            keep_set = set(keep_columns)
            keep_columns = [h for h in headers if h in keep_set]

            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("w", encoding="utf-8-sig", newline="") as dst:
                writer = csv.DictWriter(
                    dst,
                    fieldnames=keep_columns,
                    extrasaction="ignore",
                    lineterminator="\n",
                )
                writer.writeheader()

                for row in reader:
                    total_rows += 1
                    date_value = (row.get("price_date") or "").strip()
                    # Dataset dates are documented as YYYY-MM-DD; lexical
                    # comparison is therefore safe after shape validation.
                    if len(date_value) < 10 or date_value[:10] < CUTOFF:
                        skipped_date += 1
                        continue
                    if "ISO3" in available and (row.get("ISO3") or "").strip().upper() != "IDN":
                        skipped_country += 1
                        continue
                    writer.writerow({k: row.get(k, "") for k in keep_columns})
                    kept_rows += 1

        output_size = target.stat().st_size
        reduction = (1 - output_size / source_size) * 100 if source_size else 0
        print("\nFPDB TRIM COMPLETE")
        print(f"Input       : {source}")
        print(f"Output      : {target}")
        print(f"Cutoff      : {CUTOFF} onward")
        print(f"Columns     : {len(keep_columns)} ({len(close_columns)} c_* close-estimate fields)")
        print(f"Rows read   : {total_rows:,}")
        print(f"Rows kept   : {kept_rows:,}")
        print(f"Before date : {skipped_date:,}")
        print(f"Non-IDN     : {skipped_country:,}")
        print(f"Input size  : {source_size:,} bytes")
        print(f"Output size : {output_size:,} bytes")
        print(f"Size change : {reduction:.1f}% smaller")
        print("\nOriginal file was not modified.")
        return 0

    except Exception as exc:
        try:
            if target.exists():
                target.unlink()
        except OSError:
            pass
        print(f"ERROR: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
