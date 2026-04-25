#!/usr/bin/env python3

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path


def read_optional(path: Path) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""


def main() -> int:
    if len(sys.argv) != 5:
        print(
            "Usage: write_unpack_report.py <version> <source_dir> <unpacked_dir> <logs_dir>",
            file=sys.stderr,
        )
        return 1

    version = sys.argv[1]
    source_dir = Path(sys.argv[2])
    unpacked_dir = Path(sys.argv[3])
    logs_dir = Path(sys.argv[4])

    logs_dir.mkdir(parents=True, exist_ok=True)

    zip_files = sorted(source_dir.glob("*.zip"))
    unpacked_files = sorted(p for p in unpacked_dir.rglob("*") if p.is_file())

    ignored_pdfs = read_optional(logs_dir / "ignored_pdfs.txt").strip()

    report = logs_dir / "unpack_report.txt"

    lines: list[str] = []
    lines.append("Source ZIP unpack report")
    lines.append("========================")
    lines.append("")
    lines.append(f"Version: {version}")
    lines.append(f"Source dir: {source_dir}")
    lines.append(f"Unpacked dir: {unpacked_dir}")
    lines.append(f"Date UTC: {datetime.now(timezone.utc).isoformat()}")
    lines.append("")
    lines.append("ZIP files:")
    for zip_file in zip_files:
        lines.append(f"- {zip_file}")
    lines.append("")
    lines.append("Ignored PDFs:")
    if ignored_pdfs:
        for item in ignored_pdfs.splitlines():
            lines.append(f"- {item}")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("Unpacked files:")
    for path in unpacked_files:
        lines.append(f"- {path}")

    report.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote report: {report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
