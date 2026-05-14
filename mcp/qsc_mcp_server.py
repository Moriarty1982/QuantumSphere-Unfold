#!/usr/bin/env python3
"""Narrow MCP server for Quantum Sphaera audit tools.

This server exposes the repository-side audit scripts as fixed MCP tools. It is
intentionally conservative: no arbitrary shell execution, no paper rewriting, no
Zenodo upload, and no automatic claim promotion.

Expected SDK style: Model Context Protocol Python SDK with FastMCP.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

PROJECT_ROOT = Path(__file__).resolve().parents[1]
VERSION_RE = re.compile(r"^v\d+\.\d+\.\d+(?:-[A-Za-z0-9._-]+)?$")
DEFAULT_TIMEOUT_SECONDS = 900
MAX_OUTPUT_CHARS = 20000

mcp = FastMCP("qsc-audit")


class AuditError(ValueError):
    """Raised when an audit request is invalid."""


def _validate_version(version: str) -> str:
    """Validate a semver-like version string used for report folders."""
    version = version.strip()
    if not VERSION_RE.match(version):
        raise AuditError(
            "Invalid version. Expected format like 'v4.6.0' or 'v4.7.0-RC3'."
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
def run_metadata_hygiene_audit(version: str = "v4.6.0") -> dict[str, Any]:
    """Run the report-only metadata hygiene audit for a target release version."""
    return _run_script("scripts/qsc_audit/metadata_hygiene_audit.py", version)


@mcp.tool()
def run_version_scan(version: str = "v4.6.0") -> dict[str, Any]:
    """Run the report-only version drift scanner for a target release version."""
    return _run_script("scripts/qsc_audit/version_scan.py", version)


@mcp.tool()
def run_doi_scan(version: str = "v4.6.0", target_doi: str | None = None) -> dict[str, Any]:
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
def run_claim_scan(version: str = "v4.6.0") -> dict[str, Any]:
    """Run the report-only claim-strength language scanner."""
    return _run_script("scripts/qsc_audit/claim_scan.py", version)


@mcp.tool()
def run_freeze_audit(version: str = "v4.6.0") -> dict[str, Any]:
    """Run the report-only freeze-audit orchestrator for a target release."""
    return _run_script("scripts/qsc_audit/freeze_audit.py", version)


@mcp.tool()
def list_audit_reports(version: str = "v4.6.0") -> dict[str, Any]:
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


if __name__ == "__main__":
    mcp.run()
