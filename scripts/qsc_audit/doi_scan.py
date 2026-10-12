#!/usr/bin/env python3
"""DOI scanner for Quantum Sphaera release candidates.

The script reports DOI occurrences and duplicate DOI candidates. It does not
modify repository content.
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCANNABLE_SUFFIXES = {".tex", ".bib", ".md", ".txt", ".yml", ".yaml", ".json"}
EXCLUDED_DIRS = {".git", ".venv", "venv", "__pycache__", "node_modules"}
DOI_RE = re.compile(r"10\.5281/zenodo\.\d+")


@dataclass(frozen=True)
class Occurrence:
    doi: str
    path: str
    line: int


def is_scannable(path: Path) -> bool:
    if any(part in EXCLUDED_DIRS for part in path.parts):
        return False
    return path.is_file() and path.suffix.lower() in SCANNABLE_SUFFIXES


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def scan() -> list[Occurrence]:
    occurrences: list[Occurrence] = []
    for path in sorted(ROOT.rglob("*")):
        if not is_scannable(path):
            continue
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in DOI_RE.finditer(text):
            occurrences.append(Occurrence(match.group(0), rel, line_number(text, match.start())))
    return occurrences


def render_report(occurrences: list[Occurrence], target_doi: str | None) -> str:
    by_doi: dict[str, list[Occurrence]] = defaultdict(list)
    for occ in occurrences:
        by_doi[occ.doi].append(occ)

    duplicate_dois = {doi: occs for doi, occs in by_doi.items() if len(occs) > 1}
    other_dois = sorted(doi for doi in by_doi if target_doi and doi != target_doi)

    lines = [
        "# DOI Scan",
        "",
        f"Target DOI: `{target_doi or 'not specified'}`",
        "",
        "## Summary",
        "",
        f"- total DOI occurrences: {len(occurrences)}",
        f"- unique DOIs: {len(by_doi)}",
        f"- duplicate DOI candidates: {len(duplicate_dois)}",
        f"- non-target DOI candidates: {len(other_dois)}",
        "",
    ]

    if by_doi:
        lines.extend(["## DOI inventory", ""])
        for doi in sorted(by_doi):
            lines.append(f"### `{doi}`")
            lines.append("")
            for occ in by_doi[doi]:
                lines.append(f"- `{occ.path}:{occ.line}`")
            lines.append("")

    if duplicate_dois:
        lines.extend(["## Duplicate DOI candidates", ""])
        for doi, occs in sorted(duplicate_dois.items()):
            lines.append(f"- `{doi}` occurs {len(occs)} times")
        lines.append("")

    if other_dois:
        lines.extend(["## Non-target DOI candidates", ""])
        for doi in other_dois:
            lines.append(f"- `{doi}`")
        lines.append("")

    lines.extend([
        "## Interpretation notes",
        "",
        "- Duplicate DOI occurrences are not automatically wrong; title pages, release notes, and bibliographic sections may intentionally repeat a DOI.",
        "- Non-target DOI occurrences require human review because concept DOIs and historical version DOIs may be legitimate.",
        "- This scanner writes a report only and never rewrites paper content.",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan repository DOI occurrences.")
    parser.add_argument("--version", default="unversioned", help="Report version folder, e.g. v4.6.0")
    parser.add_argument("--target-doi", help="Expected release DOI, if known")
    parser.add_argument("--output", help="Optional report path")
    args = parser.parse_args()

    occurrences = scan()
    report = render_report(occurrences, args.target_doi)
    output = Path(args.output) if args.output else ROOT / "audits" / args.version / "doi_scan_report.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")
    print(output.relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()
