#!/usr/bin/env python3
"""Claim-strength scanner for Quantum Sphaera release candidates.

This scanner identifies claim-language candidates for human review. It does not
promote, weaken, or rewrite claims.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCANNABLE_SUFFIXES = {".tex", ".md", ".txt"}
EXCLUDED_DIRS = {".git", ".venv", "venv", "__pycache__", "node_modules"}

CLAIM_PATTERNS: list[tuple[str, str, re.Pattern[str]]] = [
    ("note", "info", re.compile(r"\bnote\b", re.IGNORECASE)),
    ("hypothesis", "info", re.compile(r"\b(?:hypothesis|hypothesize|conjecture)\b", re.IGNORECASE)),
    ("candidate", "info", re.compile(r"\bcandidate\b", re.IGNORECASE)),
    ("conditional", "info", re.compile(r"\b(?:conditional|provided that|assuming|under the assumptions?)\b", re.IGNORECASE)),
    ("lemma", "info", re.compile(r"\blemma\b", re.IGNORECASE)),
    ("proposition", "info", re.compile(r"\bproposition\b", re.IGNORECASE)),
    ("theorem", "warning", re.compile(r"\btheorem\b", re.IGNORECASE)),
    ("closure", "warning", re.compile(r"\b(?:closure|closed|closes|complete proof|proof of|solves?)\b", re.IGNORECASE)),
    ("physical-overclaim-candidate", "warning", re.compile(r"\b(?:derives? the Standard Model|proves? QCD|proves? confinement|proves? RH|proves? the Riemann Hypothesis|replaces? QFT|replaces? GR)\b", re.IGNORECASE)),
]


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    severity: str
    kind: str
    excerpt: str


def is_scannable(path: Path) -> bool:
    if any(part in EXCLUDED_DIRS for part in path.parts):
        return False
    return path.is_file() and path.suffix.lower() in SCANNABLE_SUFFIXES


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def clean_excerpt(text: str, start: int, end: int, radius: int = 120) -> str:
    lo = max(0, start - radius)
    hi = min(len(text), end + radius)
    excerpt = text[lo:hi].replace("\n", " ")
    return re.sub(r"\s+", " ", excerpt).strip()


def scan() -> list[Finding]:
    findings: list[Finding] = []
    for path in sorted(ROOT.rglob("*")):
        if not is_scannable(path):
            continue
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        for kind, severity, regex in CLAIM_PATTERNS:
            for match in regex.finditer(text):
                findings.append(
                    Finding(
                        path=rel,
                        line=line_number(text, match.start()),
                        severity=severity,
                        kind=kind,
                        excerpt=clean_excerpt(text, match.start(), match.end()),
                    )
                )
    return findings


def render_report(version: str | None, findings: list[Finding]) -> str:
    counts: dict[str, int] = {}
    kind_counts: dict[str, int] = {}
    for finding in findings:
        counts[finding.severity] = counts.get(finding.severity, 0) + 1
        kind_counts[finding.kind] = kind_counts.get(finding.kind, 0) + 1

    lines = [
        "# Claim Scan",
        "",
        f"Target version: `{version or 'not specified'}`",
        "",
        "## Summary",
        "",
        f"- total findings: {len(findings)}",
        f"- warnings: {counts.get('warning', 0)}",
        f"- info: {counts.get('info', 0)}",
        "",
        "## Claim kind counts",
        "",
    ]

    if kind_counts:
        for kind in sorted(kind_counts):
            lines.append(f"- `{kind}`: {kind_counts[kind]}")
    else:
        lines.append("No claim-language findings detected.")

    lines.extend(["", "## Findings", ""])
    for finding in findings:
        lines.append(f"- `{finding.severity}` `{finding.kind}` `{finding.path}:{finding.line}` — {finding.excerpt}")

    lines.extend([
        "",
        "## Interpretation notes",
        "",
        "- This scanner detects language, not proof validity.",
        "- Theorem/closure findings require human review because some theorem language is legitimate.",
        "- Promotion candidates must be handled through a separate promotion audit with assumptions and residuals listed explicitly.",
        "- This scanner writes a report only and never rewrites paper content.",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan claim-strength language.")
    parser.add_argument("--version", help="Target version, e.g. v4.6.0")
    parser.add_argument("--output", help="Optional report path")
    args = parser.parse_args()

    findings = scan()
    report = render_report(args.version, findings)
    folder = args.version or "unversioned"
    output = Path(args.output) if args.output else ROOT / "audits" / folder / "claim_scan_report.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")
    print(output.relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()
