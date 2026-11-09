#!/usr/bin/env python3
"""Narrow MCP server for Quantum Sphaera audit tools.

This server exposes the repository-side audit scripts as fixed MCP tools. It is
intentionally conservative: no arbitrary shell execution, no paper rewriting, no
Zenodo upload, and no automatic claim promotion.

Works with the Model Context Protocol Python SDK 1.x (FastMCP) and 2.x (MCPServer).
"""

from __future__ import annotations

import json
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
MAX_QAM_OUTPUT_CHARS = 100000
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
PARTS_DIR = SOURCES_DIR / "research" / "parts"
# Layer files are found by name, so a new release line (e.g. v4110-post-release-layers.tex) is picked up without edits.
LAYER_FILE_RE = re.compile(r"^v(\d)(\d+)(\d)-(release|post-release)-layers\.tex$")
LAYER_RE = re.compile(r"\\label\{(sec:(?:v\d{3,5}-)?r\d+[a-z]?-[^}]*)\}")


def _layer_files() -> list[Path]:
    """Layer files under sources/research/parts/, oldest release line first; release layers before post-release."""
    found = []
    for f in PARTS_DIR.glob("*-layers.tex"):
        m = LAYER_FILE_RE.match(f.name)
        if m:
            found.append(((int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4) == "post-release"), f))
    return [f for _, f in sorted(found)]
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
def run_guard_lint(path: str = "", start_line: int | None = None, end_line: int | None = None) -> dict[str, Any]:
    """Check a .tex file under sources/ for the five forbidden claims (C5 = 0, 0_termdata => 0_all, C6/T2 closure,
    W_gamma^glob, W_all) and for RH stated as proved. Report only; a hit is suppressed if the same sentence negates it.
    Without a path, the newest layer file is checked. Optional 1-based line range, e.g. the newest layer."""
    if not path.strip():
        files = _layer_files()
        if not files:
            raise AuditError("No layer file found under sources/research/parts/.")
        path = files[-1].relative_to(PROJECT_ROOT).as_posix()
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
    for f in _layer_files():
        name = f.name
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


def _qam_command(args, *, read_only=True, lines=False, input_text=None):
    command = [sys.executable, "-X", "utf8", "-m", "qam.tools.readout_db"]
    if read_only:
        command.append("--read-only")
    result = subprocess.run(
        [*command, *args], cwd=PROJECT_ROOT, capture_output=True, text=True,
        encoding="utf-8", timeout=60, check=False, input=input_text,
    )
    output = result.stdout.strip()
    if len(output) > MAX_QAM_OUTPUT_CHARS:
        return {"returncode": result.returncode, "error": "Response exceeds MCP limit; use a narrower query or the local CLI."}
    try:
        data = ([json.loads(line) for line in output.splitlines()] if lines
                else json.loads(output))
    except ValueError:
        return {"returncode": result.returncode, "output": output,
                "error": result.stderr.strip()[-MAX_OUTPUT_CHARS:]}
    return {"returncode": result.returncode, "data": data}


def _qam_limit(limit):
    if type(limit) is not int or not 1 <= limit <= 50:
        raise AuditError("QAM query limit must be between 1 and 50.")
    return str(limit)


def _qam_json_path(path):
    candidate = (PROJECT_ROOT / path).resolve()
    roots = (PROJECT_ROOT / "qam/examples", PROJECT_ROOT / "scripts/qsc_audit/examples",
             PROJECT_ROOT / "notes/research")
    if (candidate.suffix != ".json" or not candidate.is_file()
            or not any(root.resolve() in candidate.parents for root in roots)):
        raise AuditError("Use an existing JSON file under qam/examples, scripts/qsc_audit/examples or notes/research.")
    return str(candidate)


@mcp.tool()
def rebuild_qam_index() -> dict[str, Any]:
    """Rebuild the local QAM claim index in build/qam.sqlite3, preserving results and receipts."""
    return _qam_command(["index"], read_only=False)


@mcp.tool()
def find_qam_claims(query: str, limit: int = 10) -> dict[str, Any]:
    """Find hash-indexed QAM claims in the local database."""
    if not query.strip() or len(query) > 256:
        raise AuditError("Use a nonempty QAM query of at most 256 characters.")
    return _qam_command(["find", "--limit", _qam_limit(limit), "--", query], lines=True)


@mcp.tool()
def list_qam_receipts(instruction: str | None = None, status: str | None = None,
                      premise_hash: str | None = None, limit: int = 10) -> dict[str, Any]:
    """Find saved MMA receipts, optionally by transitive premise, instruction or status."""
    args = ["receipts", "--limit", _qam_limit(limit)]
    if instruction is not None:
        if instruction not in ("EXPORT", "SCRUB", "READOUT", "SEARCH_ROUTE"):
            raise AuditError("Unsupported MML instruction filter.")
        args.extend(["--instruction", instruction])
    if status is not None:
        if status not in ("continue", "guard", "reject"):
            raise AuditError("Unsupported MMA status filter.")
        args.extend(["--status", status])
    if premise_hash is not None:
        if not re.fullmatch(r"[0-9a-fA-F]{32}", premise_hash):
            raise AuditError("Use a 32-digit QAM premise hash.")
        args.extend(["--premise", premise_hash])
    return _qam_command(args)


@mcp.tool()
def get_qam_receipt(receipt_hash: str, trace: bool = False,
                    replay: bool = False, summary: bool = False) -> dict[str, Any]:
    """Read a verified MMA receipt. Summary also supports replay, with comparison fields only."""
    digest = "".join(receipt_hash.split())
    if not re.fullmatch(r"[0-9a-fA-F]{128}", digest):
        raise AuditError("Use a 128-digit SHA-512 receipt hash.")
    args = ["receipt", digest]
    if summary:
        if trace:
            raise AuditError("Use summary without trace.")
        args.append("--summary")
    if trace:
        args.append("--trace")
    if replay:
        args.append("--replay")
    return _qam_command(args)


@mcp.tool()
def run_qam_mml(context: str, request: str, summary: bool = False) -> dict[str, Any]:
    """Run a declared MML request, store its full receipt, and optionally return only diagnostics."""
    args = ["mma", _qam_json_path(context), _qam_json_path(request)]
    if summary:
        args.append("--summary")
    return _qam_command(args, read_only=False)


@mcp.tool()
def run_qam_mml_batch(context: str, batch: str, workers: int = 2) -> dict[str, Any]:
    """Run a saved MML pair batch and store its individual receipts."""
    if type(workers) is not int or not 1 <= workers <= 4:
        raise AuditError("Use between 1 and 4 batch workers.")
    return _qam_command(
        ["mma-batch", _qam_json_path(context), _qam_json_path(batch), "--workers", str(workers)],
        read_only=False,
    )


def run_qam_pair_batch(
    batch_json: str, workers: int = 2,
    context: str = "scripts/qsc_audit/examples/framework_context.json",
) -> dict[str, Any]:
    """Run inline JSON with requests and optional depends_on, and store the receipts."""
    if type(workers) is not int or not 1 <= workers <= 4:
        raise AuditError("Use between 1 and 4 batch workers.")
    if len(batch_json) > 100_000:
        raise AuditError("Inline MML batches must fit in 100,000 JSON characters.")
    return _qam_command(
        ["mma-batch", _qam_json_path(context), "-", "--workers", str(workers)],
        read_only=False, input_text=batch_json,
    )


def read_qam_batch_report(report_hash: str) -> dict[str, Any]:
    """Return a saved MMA batch report after verifying it and its original MML input."""
    digest = "".join(report_hash.split())
    if not re.fullmatch(r"[0-9a-fA-F]{128}", digest):
        raise AuditError("Use a 128-digit SHA-512 batch report hash.")
    return _qam_command(["batch-report", digest, "--report-only"])


def list_qam_batch_reports(limit: int = 10, request_id: str | None = None,
                           status: str | None = None) -> dict[str, Any]:
    """List recent verified batch reports, optionally matching one entry by ID and status."""
    args = ["batch-reports", "--limit", _qam_limit(limit)]
    if request_id is not None:
        if not request_id.strip() or len(request_id) > 256:
            raise AuditError("Use a nonempty request ID of at most 256 characters.")
        args.append(f"--request-id={request_id}")
    if status is not None:
        if status not in ("continue", "guard", "reject", "blocked"):
            raise AuditError("Unsupported MMA batch status.")
        args.append(f"--status={status}")
    return _qam_command(args)


def compare_qam_batch_reports(previous_hash: str, current_hash: str) -> dict[str, Any]:
    """Compare two verified stored reports, matching entries by request ID."""
    hashes = ["".join(value.split()) for value in (previous_hash, current_hash)]
    if any(not re.fullmatch(r"[0-9a-fA-F]{128}", value) for value in hashes):
        raise AuditError("Use two 128-digit SHA-512 batch report hashes.")
    return _qam_command(["compare-batches", *hashes])


def audit_qam_batch_report(report_hash: str) -> dict[str, Any]:
    """Verify a saved batch, context, individual receipt links and blocked entries."""
    digest = "".join(report_hash.split())
    if not re.fullmatch(r"[0-9a-fA-F]{128}", digest):
        raise AuditError("Use a 128-digit SHA-512 batch report hash.")
    return _qam_command(["audit-batch", digest])


def replay_qam_batch_report(report_hash: str, workers: int = 2) -> dict[str, Any]:
    """Recompute a saved batch against current indexed premises without saving new receipts."""
    digest = "".join(report_hash.split())
    if not re.fullmatch(r"[0-9a-fA-F]{128}", digest):
        raise AuditError("Use a 128-digit SHA-512 batch report hash.")
    if type(workers) is not int or not 1 <= workers <= 4:
        raise AuditError("Use between 1 and 4 batch workers.")
    return _qam_command(["replay-batch", digest, "--workers", str(workers)])


if __name__ == "__main__":
    mcp.run()
