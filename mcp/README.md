# QSC audit MCP server

`qsc_mcp_server.py` exposes the repository's audit and check scripts as fixed MCP tools. It is deliberately narrow:
no arbitrary shell, no rewriting of the paper, no Zenodo upload, no claim promotion, no merge. Every tool runs one
fixed script with validated arguments and a time limit, and reports; nothing in the sources is changed.

## Tools

| Tool | What it runs | Writes |
|---|---|---|
| `run_metadata_hygiene_audit(version)` | `scripts/qsc_audit/metadata_hygiene_audit.py` | `audits/<version>/` |
| `run_version_scan(version)` | `scripts/qsc_audit/version_scan.py` (version drift) | `audits/<version>/` |
| `run_doi_scan(version, target_doi)` | `scripts/qsc_audit/doi_scan.py` (non-target DOIs) | `audits/<version>/` |
| `run_claim_scan(version)` | `scripts/qsc_audit/claim_scan.py` (claim-strength language) | `audits/<version>/` |
| `run_freeze_audit(version)` | `scripts/qsc_audit/freeze_audit.py` (the four scans above, with an index) | `audits/<version>/` |
| `list_audit_reports(version)` | lists `audits/<version>/` | — |
| `run_guard_lint(path, start_line, end_line)` | `scripts/qsc_audit/guard_linter.py` on a `.tex` file under `sources/`: the five forbidden claims and RH stated as proved; without `path`, the newest layer file | — |
| `list_layers()` | lists the append-only layers (label, title, file, line) in `sources/research/parts/v*-release-layers.tex` and `v*-post-release-layers.tex`, found by name and ordered by release line, so a new layer file needs no code change | — |
| `build_research_candidate()` | `.github/scripts/qsc_latex_build.py` on `sources/research` and the CI research gate | `build/mcp-research/` |

`version` defaults to `v4.9.0`, the current public release; use for example `v4.10.0-draft` for the candidate. Paths for
`run_guard_lint` must lie under `sources/`. `build_research_candidate` needs a LaTeX installation with `latexmk` on `PATH`
(on Windows: MiKTeX's `bin\x64` folder) and takes several minutes.

`guard_linter.py` is a copy of `notes/research/v4_8_0_r03_r12/llm/training/guard_linter.py`.

## Install and register

Requires Python 3.10 or later and the MCP Python SDK; both SDK 1.x (`FastMCP`) and 2.x (`MCPServer`) work.

```
pip install "mcp>=1.2"
```

Claude Code, from the repository root:

```
claude mcp add qsc-audit -- python mcp/qsc_mcp_server.py
```

Claude Desktop (`claude_desktop_config.json`), with the absolute path of your clone:

```json
{
  "mcpServers": {
    "qsc-audit": {
      "command": "python",
      "args": ["C:\\path\\to\\QuantumSphere-Unfold\\mcp\\qsc_mcp_server.py"]
    }
  }
}
```

The server resolves the repository root from its own location, so it must stay in `mcp/` of a full clone.

## QAM database and MMA tools

These tools use the local `build/qam.sqlite3` database through the same
CLI as the QAM examples.

| Tool | What it does | Writes |
|---|---|---|
| `rebuild_qam_index()` | Rebuilds the claim index while preserving receipts and cached calculations | SQLite |
| `find_qam_claims(query, limit)` | Finds indexed claims with their frames, status and premises | None |
| `list_qam_receipts(instruction, status, premise_hash, limit)` | Lists receipts and can follow recorded indirect premise dependencies | None |
| `get_qam_receipt(receipt_hash, trace, replay)` | Checks stored hashes, optionally returns the premise trace or recomputes without cache | None |
| `run_qam_mml(context, request)` | Executes a declared MML JSON request, including READOUT and SEARCH_ROUTE, with MMA guards | SQLite |

Use `get_qam_receipt(receipt_hash, summary=true)` for the verified hash,
instruction, MMA status, errors, obligations and declared guards. The
summary supports `replay=true` and adds the result and receipt comparisons,
the new hash and changed field names. Request the trace separately.
Use `run_qam_mml(context, request, summary=true)` for the same concise
diagnostics on execution. SQLite stores the full receipt in either mode.
For route searches, the summary also reports the number of candidates and
the distinct open guards across them. It also lists the operations and guards
for the candidates with the fewest open guards, including ties.
For checked channels, the summary includes any exclusion reasons and available
input, output, declared environment and minimum environment dimensions.

Run the index tool first if the local database does not exist.
MML inputs must be existing JSON files under `qam/examples/`,
`scripts/qsc_audit/examples/`, or `notes/research/`. These tools run a
fixed Python module with a 60-second timeout. Search limits range from
one to 50. The response preserves the MMA status and exit code, so
a guarded route can return a valid result with code 1.
