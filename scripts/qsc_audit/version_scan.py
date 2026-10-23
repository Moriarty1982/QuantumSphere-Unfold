#!/usr/bin/env python3
"""Version scanner for Quantum Sphaera release candidates.

Reports version-string occurrences and drift candidates. It does not modify
repository content.
"""

from __future__ import annotations

import argparse
import bisect
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCANNABLE_SUFFIXES = {".tex", ".bib", ".md", ".txt", ".yml", ".yaml", ".json"}
EXCLUDED_DIRS = {".git", ".venv", "venv", "__pycache__", "node_modules", "audits", "build"}  # own reports and build output
VERSION_RE = re.compile(r"\bv\d+\.\d+\.\d+(?:-r\d+)?\b")


@dataclass(frozen=True)
class Occurrence:
    version: str
    path: str
    line: int


def is_scannable(path: Path) -> bool:
    if any(part in EXCLUDED_DIRS for part in path.parts):
        return False
    return path.is_file() and path.suffix.lower() in SCANNABLE_SUFFIXES


_NL_CACHE: tuple[str, list[int]] | None = None


def line_number(text: str, offset: int) -> int:
    """1-based line of `offset`; newline offsets are computed once per text (was quadratic on large sources)."""
    global _NL_CACHE
    if _NL_CACHE is None or _NL_CACHE[0] is not text:
        _NL_CACHE = (text, [m.start() for m in re.finditer("\n", text)])
    return bisect.bisect_left(_NL_CACHE[1], offset) + 1


def scan() -> list[Occurrence]:
    occurrences: list[Occurrence] = []
    for path in sorted(ROOT.rglob("*")):
        if not is_scannable(path):
            continue
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in VERSION_RE.finditer(text):
            occurrences.append(Occurrence(match.group(0), rel, line_number(text, match.start())))
    return occurrences


def render_report(occurrences: list[Occurrence], target_version: str | None) -> str:
    by_version: dict[str, list[Occurrence]] = defaultdict(list)
    for occ in occurrences:
        by_version[occ.version].append(occ)

    drift = sorted(v for v in by_version if target_version and v != target_version)
    internal_revision_versions = sorted(v for v in by_version if "-r" in v)

    lines = [
        "# Version Scan",
        "",
        f"Target version: `{target_version or 'not specified'}`",
        "",
        "## Summary",
        "",
        f"- total version occurrences: {len(occurrences)}",
        f"- unique version tokens: {len(by_version)}",
        f"- drift candidates: {len(drift)}",
        f"- internal revision-style version tokens: {len(internal_revision_versions)}",
        "",
    ]

    if by_version:
        lines.extend(["## Version inventory", ""])
        for version in sorted(by_version):
            lines.append(f"### `{version}`")
            lines.append("")
            for occ in by_version[version]:
                lines.append(f"- `{occ.path}:{occ.line}`")
            lines.append("")

    if drift:
        lines.extend(["## Drift candidates", ""])
        for version in drift:
            lines.append(f"- `{version}`")
        lines.append("")

    lines.extend([
        "## Interpretation notes",
        "",
        "- Drift candidates are not automatically wrong; historical witness material and release comparisons may intentionally mention older versions.",
        "- Public-facing frontmatter should normally use the target release version only.",
        "- This scanner writes a report only and never rewrites paper content.",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan repository version occurrences.")
    parser.add_argument("--version", help="Target version, e.g. v4.6.0")
    parser.add_argument("--output", help="Optional report path")
    args = parser.parse_args()

    occurrences = scan()
    report = render_report(occurrences, args.version)
    folder = args.version or "unversioned"
    output = Path(args.output) if args.output else ROOT / "audits" / folder / "version_scan_report.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")
    print(output.relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()
