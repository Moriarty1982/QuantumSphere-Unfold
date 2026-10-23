#!/usr/bin/env python3
"""Narrow MCP server for Quantum Sphaera audit tools.

This server exposes the repository-side audit scripts as fixed MCP tools. It is
intentionally conservative: no arbitrary shell execution, no paper rewriting, no
Zenodo upload, and no automatic claim promotion.

Works with the Model Context Protocol Python SDK 1.x (FastMCP) and 2.x (MCPServer).
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from typing import Any

try:  # MCP Python SDK 2.x renamed FastMCP to MCPServer
    from mcp.server.mcpserver import MCPServer as FastMCP
except ImportError:  # SDK 1.x
    from mcp.server.fastmcp import FastMCP

PROJECT_ROOT = Path(__file__).resolve().parents[1]
VERSION_RE = re.compile(r"^v\d+\.\d+\.\d+(?:-[A-Za-z0-9._-]+)?$")
DEFAULT_TIMEOUT_SECONDS = 900
MAX_OUTPUT_CHARS = 20000
DEFAULT_VERSION = "v4.9.0"  # current public release; pass e.g. "v4.10.0-draft" for the candidate

mcp = FastMCP("qsc-audit")


class AuditError(ValueError):
    """Raised when an audit request is invalid."""


def _validate_version(version: str) -> str:
    """Validate a semver-like version string used for report folders."""
    version = version.strip()
    if not VERSION_RE.match(version):
        raise AuditError(
            "Invalid version. Expected format like 'v4.9.0' or 'v4.10.0-draft'."
        )
    return version


def _run_script(script: str, version: str, extra_args: list[str] | None = None) -> dict[str, Any]:
    """Run one fixed audit script without invoking a shell."""
    version = _validate_version(version)
    script_path = PROJECT_ROOT / script
    if not script_path.is_file():
        raise AuditError(f"Audit script not found: {script}")

    command = [sys.executable, str(script_path), "--version", version]
    if extra_args:
        command.extend(extra_args)

    result = subprocess.run(
        command,
        cwd=PROJECT_ROOT,
        text=True,
        capture_output=True,
        timeout=DEFAULT_TIMEOUT_SECONDS,
        check=False,
    )

    stdout = result.stdout.strip()
    stderr = result.stderr.strip()
    combined = "\n".join(part for part in [stdout, stderr] if part)
    if len(combined) > MAX_OUTPUT_CHARS:
        combined = combined[-MAX_OUTPUT_CHARS:]

    return {
        "tool": script,
        "version": version,
        "returncode": result.returncode,
        "ok": result.returncode == 0,
        "output_tail": combined,
    }


@mcp.tool()
def run_metadata_hygiene_audit(version: str = DEFAULT_VERSION) -> dict[str, Any]:
    """Run the report-only metadata hygiene audit for a target release version."""
    return _run_script("scripts/qsc_audit/metadata_hygiene_audit.py", version)


@mcp.tool()
def run_version_scan(version: str = DEFAULT_VERSION) -> dict[str, Any]:
    """Run the report-only version drift scanner for a target release version."""
    return _run_script("scripts/qsc_audit/version_scan.py", version)


@mcp.tool()
def run_doi_scan(version: str = DEFAULT_VERSION, target_doi: str | None = None) -> dict[str, Any]:
    """Run the report-only DOI scanner.

    If `target_doi` is supplied, non-target DOI candidates are listed in the
    generated report.
    """
    extra_args: list[str] = []
    if target_doi:
        if not re.match(r"^10\.5281/zenodo\.\d+$", target_doi.strip()):
            raise AuditError("Invalid target DOI. Expected format like 10.5281/zenodo.20181842.")
        extra_args.extend(["--target-doi", target_doi.strip()])
    return _run_script("scripts/qsc_audit/doi_scan.py", version, extra_args)


@mcp.tool()
def run_claim_scan(version: str = DEFAULT_VERSION) -> dict[str, Any]:
    """Run the report-only claim-strength language scanner."""
    return _run_script("scripts/qsc_audit/claim_scan.py", version)


@mcp.tool()
def run_freeze_audit(version: str = DEFAULT_VERSION) -> dict[str, Any]:
    """Run the report-only freeze-audit orchestrator for a target release."""
    return _run_script("scripts/qsc_audit/freeze_audit.py", version)


@mcp.tool()
def list_audit_reports(version: str = DEFAULT_VERSION) -> dict[str, Any]:
    """List generated audit report files for a target release version."""
    version = _validate_version(version)
    audit_dir = PROJECT_ROOT / "audits" / version
    if not audit_dir.exists():
        return {"version": version, "exists": False, "reports": []}

    reports = [
        path.relative_to(PROJECT_ROOT).as_posix()
        for path in sorted(audit_dir.rglob("*"))
        if path.is_file()
    ]
    return {"version": version, "exists": True, "reports": reports}


# ---------------------------------------------------------------------------- research-line tools (2026-10-23)

SOURCES_DIR = PROJECT_ROOT / "sources"
LAYER_FILES = ("v480-release-layers.tex", "v480-post-release-layers.tex", "v490-post-release-layers.tex")
LAYER_RE = re.compile(r"\\label\{(sec:(?:v4\d0-)?r\d+[a-z]?-[^}]*)\}")
TITLE_RE = re.compile(r"\\section\*?\{([^}]*)\}")


def _source_path(path: str) -> Path:
    """Resolve a .tex path under sources/ and refuse anything outside it."""
    candidate = (PROJECT_ROOT / path.strip()).resolve()
    if candidate.suffix != ".tex" or not candidate.is_file():
        raise AuditError(f"Not an existing .tex file: {path}")
    if SOURCES_DIR.resolve() not in candidate.parents:
        raise AuditError("Only files under sources/ may be linted.")
    return candidate


@mcp.tool()
def run_guard_lint(path: str = "sources/research/parts/v490-post-release-layers.tex",
                   start_line: int | None = None, end_line: int | None = None) -> dict[str, Any]:
    """Check a .tex file under sources/ for the five forbidden claims (C5 = 0, 0_termdata => 0_all, C6/T2 closure,
    W_gamma^glob, W_all) and for RH stated as proved. Report only; a hit is suppressed if the same sentence negates it.
    Optional 1-based line range, e.g. the newest layer."""
    target = _source_path(path)
    command = [sys.executable, str(PROJECT_ROOT / "scripts/qsc_audit/guard_linter.py"), str(target)]
    if start_line is not None:
        command += ["--start", str(int(start_line))]
    if end_line is not None:
        command += ["--end", str(int(end_line))]
    result = subprocess.run(command, cwd=PROJECT_ROOT, text=True, capture_output=True,
                            timeout=DEFAULT_TIMEOUT_SECONDS, check=False)
    out = "\n".join(part for part in [result.stdout.strip(), result.stderr.strip()] if part)
    return {"tool": "guard_linter", "path": target.relative_to(PROJECT_ROOT).as_posix(),
            "clean": result.returncode == 0, "returncode": result.returncode, "output_tail": out[-MAX_OUTPUT_CHARS:]}


@mcp.tool()
def list_layers() -> dict[str, Any]:
    """List the append-only layers (label, title, file, line) in the research candidate's layer files."""
    layers = []
    for name in LAYER_FILES:
        f = SOURCES_DIR / "research" / "parts" / name
        if not f.is_file():
            continue
        lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
        for i, line in enumerate(lines):
            m = LAYER_RE.search(line)
            if not m:
                continue
            title = next((TITLE_RE.search(lines[j]).group(1) for j in range(i, max(i - 4, -1), -1)
                          if TITLE_RE.search(lines[j])), "")
            layers.append({"label": m.group(1), "title": title, "file": f"sources/research/parts/{name}", "line": i + 1})
    return {"count": len(layers), "last": layers[-1]["label"] if layers else None, "layers": layers}


@mcp.tool()
def build_research_candidate() -> dict[str, Any]:
    """Build the research candidate under sources/research/ exactly as CI does (qsc_latex_build.py) and apply the
    research gate (no fatal errors, no undefined references or citations, no duplicate labels, no rerun warning).
    Needs a LaTeX installation with latexmk on PATH. Writes only to build/mcp-research/."""
    out_dir = PROJECT_ROOT / "build" / "mcp-research"
    build = subprocess.run([sys.executable, str(PROJECT_ROOT / ".github/scripts/qsc_latex_build.py"),
                            "--source-dir", "sources/research", "--output-dir", str(out_dir), "--build-historical", "false"],
                           cwd=PROJECT_ROOT, text=True, capture_output=True, timeout=2 * DEFAULT_TIMEOUT_SECONDS, check=False)
    summary_file = out_dir / "build-summary.json"
    summary = summary_file.read_text(encoding="utf-8") if summary_file.is_file() else None
    gate = subprocess.run([sys.executable, str(PROJECT_ROOT / ".github/scripts/qsc_research_gate.py"), str(summary_file)],
                          cwd=PROJECT_ROOT, text=True, capture_output=True, timeout=120, check=False) if summary else None
    tail = lambda r: "\n".join(p for p in [r.stdout.strip(), r.stderr.strip()] if p)[-MAX_OUTPUT_CHARS:]
    return {"build_returncode": build.returncode, "gate_ok": bool(gate and gate.returncode == 0),
            "gate_output": tail(gate) if gate else "no build summary written", "summary": summary,
            "build_output_tail": tail(build)[-4000:]}


if __name__ == "__main__":
    mcp.run()
