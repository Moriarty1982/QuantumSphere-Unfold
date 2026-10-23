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
| `run_guard_lint(path, start_line, end_line)` | `scripts/qsc_audit/guard_linter.py` on a `.tex` file under `sources/`: the five forbidden claims and RH stated as proved | — |
| `list_layers()` | lists the append-only layers (label, title, file, line) in `sources/research/parts/*-layers.tex` | — |
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
