#!/usr/bin/env python3
"""Build Quantum Sphaera Companion LaTeX PDFs in GitHub Actions.

Source-tree policy:
- `sources/` is the canonical current source tree.
- Git tags, not version folders, define release snapshots.
- The script never edits source TEX files.
- It builds into an isolated output directory.
- It separates active-core and historical-witness builds.
- It writes logs, summaries, and checksums for release audits.

The old `--version-dir` argument is retained as a backwards-compatible alias.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Iterable


ACTIVE_HINTS = ("active-core", "active_core", "active", "router_normal", "physical_readout")
HISTORICAL_HINTS = ("historical-witness", "historical_witness", "historical", "witness")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def decode_process_bytes(data: bytes | None) -> str:
    """Decode process output without allowing locale bytes to crash the build."""
    if not data:
        return ""
    return data.decode("utf-8", errors="replace")


def clean_auxiliary_files(directory: Path) -> None:
    suffixes = {
        ".aux", ".bbl", ".bcf", ".blg", ".fdb_latexmk", ".fls",
        ".log", ".out", ".run.xml", ".toc", ".lof", ".lot", ".synctex.gz",
    }
    for path in directory.glob("**/*"):
        if path.is_file() and path.suffix in suffixes:
            path.unlink(missing_ok=True)


def run_latexmk(tex_path: Path, out_dir: Path) -> dict:
    job_out = out_dir / tex_path.stem
    job_out.mkdir(parents=True, exist_ok=True)
    cmd = [
        "latexmk",
        "-pdf",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        "-shell-escape",
        f"-outdir={job_out}",
        str(tex_path.resolve()),
    ]
    proc = subprocess.run(cmd, cwd=str(tex_path.parent), text=False, capture_output=True)

    stdout_text = decode_process_bytes(proc.stdout)
    stderr_text = decode_process_bytes(proc.stderr)

    log_path = job_out / f"{tex_path.stem}.build.stdout.log"
    log_path.write_text(stdout_text + "\n\n--- STDERR ---\n" + stderr_text, encoding="utf-8", errors="replace")

    pdf_candidates = list(job_out.glob("*.pdf"))
    log_candidates = list(job_out.glob("*.log"))
    pdf_path = pdf_candidates[0] if pdf_candidates else None
    tex_log_path = log_candidates[0] if log_candidates else None

    result = {
        "tex": str(tex_path),
        "returncode": proc.returncode,
        "pdf": str(pdf_path) if pdf_path else None,
        "stdout_log": str(log_path),
        "tex_log": str(tex_log_path) if tex_log_path else None,
        "undefined_refs": None,
        "undefined_citations": None,
        "overfull_hbox": None,
        "overfull_vbox": None,
        "fatal_errors": None,
    }

    if tex_log_path and tex_log_path.exists():
        text = tex_log_path.read_text(encoding="utf-8", errors="replace")
        result.update({
            "undefined_refs": text.count("undefined references"),
            "undefined_citations": text.count("undefined citations"),
            "overfull_hbox": text.count("Overfull \\hbox"),
            "overfull_vbox": text.count("Overfull \\vbox"),
            "fatal_errors": text.count("Fatal error") + text.count("Emergency stop"),
        })

    if pdf_path and pdf_path.exists():
        result["pdf_sha256"] = sha256(pdf_path)
        result["pdf_bytes"] = pdf_path.stat().st_size

    return result


def classify_tex_files(tex_files: Iterable[Path], build_historical: bool) -> list[Path]:
    active: list[Path] = []
    historical: list[Path] = []
    other: list[Path] = []

    for path in tex_files:
        name = path.name.lower()
        if any(h in name for h in HISTORICAL_HINTS):
            historical.append(path)
        elif any(h in name for h in ACTIVE_HINTS):
            active.append(path)
        else:
            other.append(path)

    selected = active or other
    if build_historical:
        selected += historical
    return selected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", default=None, help="Canonical source directory, usually sources/")
    parser.add_argument("--version-dir", default=None, help="Backward-compatible alias for --source-dir")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--build-historical", default="true")
    args = parser.parse_args()

    source_arg = args.source_dir or args.version_dir or "sources"
    source_dir = Path(source_arg)
    output_dir = Path(args.output_dir)
    build_historical = args.build_historical.lower() in {"1", "true", "yes", "y"}

    output_dir.mkdir(parents=True, exist_ok=True)

    if not source_dir.exists():
        (output_dir / "build-summary.json").write_text(json.dumps({
            "status": "failed",
            "reason": f"source_dir does not exist: {source_dir}",
        }, indent=2), encoding="utf-8")
        print(f"ERROR: source_dir does not exist: {source_dir}", file=sys.stderr)
        return 2

    tex_files = sorted(source_dir.glob("*.tex"))
    selected = classify_tex_files(tex_files, build_historical=build_historical)

    if not selected:
        (output_dir / "build-summary.json").write_text(json.dumps({
            "status": "failed",
            "reason": f"no entry-point .tex files found directly in {source_dir}",
        }, indent=2), encoding="utf-8")
        print(f"ERROR: no entry-point .tex files found directly in {source_dir}", file=sys.stderr)
        return 3

    clean_auxiliary_files(source_dir)

    results = []
    for tex in selected:
        print(f"Building {tex}")
        results.append(run_latexmk(tex, output_dir))

    checksums = []
    for pdf in output_dir.glob("**/*.pdf"):
        checksums.append(f"{sha256(pdf)}  {pdf.relative_to(output_dir)}")
    (output_dir / "SHA256SUMS.txt").write_text("\n".join(sorted(checksums)) + "\n", encoding="utf-8")

    status = "ok" if all(r["returncode"] == 0 and r["pdf"] for r in results) else "failed"
    summary = {
        "status": status,
        "source_dir": str(source_dir),
        "build_historical": build_historical,
        "selected_tex_files": [str(p) for p in selected],
        "results": results,
    }
    (output_dir / "build-summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    markdown_lines = [
        "# QSC LaTeX Build Summary",
        "",
        f"Status: **{status}**",
        f"Source directory: `{source_dir}`",
        f"Build historical: `{build_historical}`",
        "",
        "| TEX | return code | PDF | overfull hbox | overfull vbox | fatal errors |",
        "|---|---:|---|---:|---:|---:|",
    ]
    for r in results:
        markdown_lines.append(
            f"| `{Path(r['tex']).name}` | {r['returncode']} | `{Path(r['pdf']).name if r['pdf'] else 'missing'}` | "
            f"{r['overfull_hbox']} | {r['overfull_vbox']} | {r['fatal_errors']} |"
        )
    (output_dir / "build-summary.md").write_text("\n".join(markdown_lines) + "\n", encoding="utf-8")

    return 0 if status == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())
