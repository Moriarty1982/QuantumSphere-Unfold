#!/usr/bin/env python3
"""Metadata hygiene audit for Quantum Sphaera release candidates.

This script is intentionally conservative. It scans text-like repository files and
writes a report; it does not rewrite paper content.
"""

from __future__ import annotations

import argparse
import bisect
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INCLUDE_SUFFIXES = {".tex", ".bib", ".md", ".txt", ".yml", ".yaml", ".json"}
DEFAULT_EXCLUDED_DIRS = {".git", ".venv", "venv", "__pycache__", "node_modules", "audits", "build"}

DOI_RE = re.compile(r"10\.5281/zenodo\.\d+")
INTERNAL_REVISION_RE = re.compile(r"\bv\d+\.\d+\.\d+-r\d+\b|\br\d{2,}\b")
UNDEFINED_MARKER_RE = re.compile(r"\b(?:Proposition|Theorem|Lemma|Figure|Table|Section)\s*\?\?|\?\?")
DRAFT_MARKER_RE = re.compile(r"\b(?:draft|working candidate|source/audit candidate|TODO|FIXME)\b", re.IGNORECASE)
VERSION_RE = re.compile(r"\bv\d+\.\d+\.\d+\b")
ZERO_MARKER_SUMMARY_RE = re.compile(
    r"^\s*-\s+Visible\s+`\?\?`\s*/\s*`\[\?\]`\s*:\s*0\s*/\s*0\b[^?]*$"
)


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    severity: str
    kind: str
    detail: str


def is_scannable(path: Path) -> bool:
    if any(part in DEFAULT_EXCLUDED_DIRS for part in path.parts):
        return False
    return path.is_file() and path.suffix.lower() in DEFAULT_INCLUDE_SUFFIXES


_NL_CACHE: tuple[str, list[int]] | None = None


def line_number(text: str, offset: int) -> int:
    """1-based line of `offset`; newline offsets are computed once per text (was quadratic on large sources)."""
    global _NL_CACHE
    if _NL_CACHE is None or _NL_CACHE[0] is not text:
        _NL_CACHE = (text, [m.start() for m in re.finditer("\n", text)])
    return bisect.bisect_left(_NL_CACHE[1], offset) + 1


def add_regex_findings(
    findings: list[Finding],
    rel: str,
    text: str,
    regex: re.Pattern[str],
    severity: str,
    kind: str,
    detail_prefix: str,
) -> None:
    for match in regex.finditer(text):
        findings.append(
            Finding(
                path=rel,
                line=line_number(text, match.start()),
                severity=severity,
                kind=kind,
                detail=f"{detail_prefix}: {match.group(0)!r}",
            )
        )


def scan_file(path: Path, target_version: str | None) -> list[Finding]:
    rel = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8", errors="replace")
    findings: list[Finding] = []

    if target_version and path.suffix.lower() in {".tex", ".md"}:
        versions = set(VERSION_RE.findall(text))
        other_versions = sorted(v for v in versions if v != target_version)
        for version in other_versions:
            # This is a warning, not an error: historical witness sections may be valid.
            for match in re.finditer(re.escape(version), text):
                findings.append(
                    Finding(
                        path=rel,
                        line=line_number(text, match.start()),
                        severity="warning",
                        kind="version-drift-candidate",
                        detail=f"found version {version!r} while target is {target_version!r}",
                    )
                )

    dois = DOI_RE.findall(text)
    seen: set[str] = set()
    for doi in dois:
        if doi in seen:
            first = text.find(doi)
            second = text.find(doi, first + 1)
            findings.append(
                Finding(
                    path=rel,
                    line=line_number(text, second if second >= 0 else first),
                    severity="warning",
                    kind="duplicate-doi-candidate",
                    detail=f"duplicate DOI occurrence {doi!r}",
                )
            )
        seen.add(doi)

    add_regex_findings(findings, rel, text, INTERNAL_REVISION_RE, "info", "internal-revision-token", "internal revision token")
    # A zero-count build summary documents the absence of unresolved references.
    # Mask only that complete Markdown line; retain offsets and all other markers.
    marker_text = "".join(
        " " * len(line.rstrip("\r\n")) + line[len(line.rstrip("\r\n")):]
        if path.suffix.lower() == ".md" and ZERO_MARKER_SUMMARY_RE.fullmatch(line.rstrip("\r\n"))
        else line
        for line in text.splitlines(keepends=True)
    )
    add_regex_findings(findings, rel, marker_text, UNDEFINED_MARKER_RE, "error", "undefined-marker", "undefined reference marker")
    add_regex_findings(findings, rel, text, DRAFT_MARKER_RE, "warning", "draft-marker", "draft marker")

    return findings


def render_report(target_version: str | None, findings: list[Finding]) -> str:
    counts: dict[str, int] = {}
    for finding in findings:
        counts[finding.severity] = counts.get(finding.severity, 0) + 1

    lines = [
        "# Metadata Hygiene Audit",
        "",
        f"Target version: `{target_version or 'not specified'}`",
        "",
        "## Summary",
        "",
        f"- errors: {counts.get('error', 0)}",
        f"- warnings: {counts.get('warning', 0)}",
        f"- info: {counts.get('info', 0)}",
        "",
    ]

    if not findings:
        lines.append("No findings detected.")
        lines.append("")
        return "\n".join(lines)

    lines.extend(["## Findings", ""])
    for finding in findings:
        lines.append(
            f"- `{finding.severity}` `{finding.kind}` `{finding.path}:{finding.line}` — {finding.detail}"
        )

    lines.extend(
        [
            "",
            "## Interpretation notes",
            "",
            "- `internal-revision-token` findings are informational because historical witness sections may intentionally preserve old revision tags.",
            "- `version-drift-candidate` findings require human review; they may be valid in historical or comparative sections.",
            "- `undefined-marker` findings should block public release until reviewed or fixed.",
            "- This script writes reports only and never rewrites paper content.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run metadata hygiene audit.")
    parser.add_argument("--version", help="Target version, for example v4.6.0")
    parser.add_argument("--output", help="Optional output report path")
    args = parser.parse_args()

    findings: list[Finding] = []
    for path in sorted(ROOT.rglob("*")):
        if is_scannable(path):
            findings.extend(scan_file(path, args.version))

    report = render_report(args.version, findings)
    output = Path(args.output) if args.output else ROOT / "audits" / (args.version or "unversioned") / "metadata_hygiene_report.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")
    print(output.relative_to(ROOT).as_posix())

    # Release-blocking markers should return non-zero for CI while warnings remain reviewable.
    if any(f.severity == "error" for f in findings):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
