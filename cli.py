#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from s3dt.pipeline import events_to_dicts, run_pipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the S3DT pipeline on a thread graph")
    parser.add_argument("--thread", required=True)
    parser.add_argument("--constraints", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(args.thread, "r", encoding="utf-8") as f:
        thread = json.load(f)

    events = run_pipeline(thread, args.constraints)
    payload = events_to_dicts(events)

    with open(output_dir / "events.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    with open(output_dir / "events.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["constraint_id", "source", "target", "severity", "drift_type", "explanation"],
        )
        writer.writeheader()
        for row in payload:
            writer.writerow(row)

    with open(output_dir / "summary.md", "w", encoding="utf-8") as f:
        f.write("# Pipeline output\n\n")
        if not payload:
            f.write("No drift events detected.\n")
        for row in payload:
            f.write(
                f"- `{row['constraint_id']}` {row['source']} -> {row['target']} | "
                f"severity={row['severity']:.3f} | type={row['drift_type']}\n"
            )


if __name__ == "__main__":
    main()
