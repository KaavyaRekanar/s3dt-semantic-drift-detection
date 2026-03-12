#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Export paper reference outputs")
    parser.add_argument("--case-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    case_dir = Path(args.case_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    src_dir = case_dir / "expected_outputs"
    shutil.copy2(src_dir / "paper_drift_scores.json", output_dir / "paper_reference_scores.json")
    shutil.copy2(src_dir / "paper_drift_scores.csv", output_dir / "paper_reference_scores.csv")


if __name__ == "__main__":
    main()
