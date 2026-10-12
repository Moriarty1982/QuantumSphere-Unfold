#!/usr/bin/env python3
"""Coordinating freeze-audit runner for Quantum Sphaera release candidates.

This pilot runner executes conservative report-only scanners and writes a compact
index report. It does not compile LaTeX yet and does not modify paper content.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Step:
    name: str
    command: list[str]
    report_path: Path


@dataclass(frozen=True)
class StepResult:
    name: str
    returncode: int
    report_path: Path
    output: str


def run_step(step: Step) -> StepResult:
    result = subprocess.run(
        step.command,
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=900,
    )
    output = (result.stdout + "\n" + result.stderr).strip()
    return StepResult(step.name, result.returncode, step.report_path, output)


def render_index(version: str, results: list[StepResult]) -> str:
    lines = [
        "# Freeze Audit Pilot",
        "",
        f"Target version: `{version}`",
        "",
        "## Summary",
        "",
    ]

    for result in results:
        status = "pass" if result.returncode == 0 else "needs-review"
        rel_report = result.report_path.relative_to(ROOT).as_posix()
        lines.append(f"- `{status}` `{result.name}` → `{rel_report}`")

    lines.extend(["", "## Step output", ""])
    for result in results:
        lines.append(f"### {result.name}")
        lines.append("")
        lines.append("```text")
        lines.append(result.output or "<no output>")
        lines.append("```")
        lines.append("")

    lines.extend([
        "## Interpretation notes",
        "",
        "- This is a pilot freeze audit and currently coordinates report-only scanners.",
        "- LaTeX compilation, bibliography checks, PDF page accounting, and checksum generation are intentionally deferred to later pilot stages.",
        "- Any non-zero scanner exit is treated as `needs-review`, not as an automatic content change.",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run pilot freeze audit.")
    parser.add_argument("--version", required=True, help="Target version, e.g. v4.6.0")
    args = parser.parse_args()

    audit_dir = ROOT / "audits" / args.version
    audit_dir.mkdir(parents=True, exist_ok=True)

    steps = [
        Step(
            "metadata hygiene",
            [sys.executable, "scripts/qsc_audit/metadata_hygiene_audit.py", "--version", args.version],
            audit_dir / "metadata_hygiene_report.md",
        ),
        Step(
            "version scan",
            [sys.executable, "scripts/qsc_audit/version_scan.py", "--version", args.version],
            audit_dir / "version_scan_report.md",
        ),
        Step(
            "doi scan",
            [sys.executable, "scripts/qsc_audit/doi_scan.py", "--version", args.version],
            audit_dir / "doi_scan_report.md",
        ),
        Step(
            "claim scan",
            [sys.executable, "scripts/qsc_audit/claim_scan.py", "--version", args.version],
            audit_dir / "claim_scan_report.md",
        ),
    ]

    results = [run_step(step) for step in steps]
    index = render_index(args.version, results)
    index_path = audit_dir / "freeze_audit_report.md"
    index_path.write_text(index, encoding="utf-8")
    print(index_path.relative_to(ROOT).as_posix())

    if any(result.returncode != 0 for result in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
