# Tool Extractor

## Purpose

The Tool Extractor identifies recurring manual checks in the Quantum Sphaera / Companion workflow and turns them into reusable scripts.

This role creates infrastructure around the paper. It does not change mathematical content.

## First tool candidates

- Metadata hygiene scanner.
- DOI scanner.
- Version drift scanner.
- Label and reference scanner.
- Claim-strength scanner.
- LaTeX build diagnostics.
- Release packet generator.
- Zenodo description generator.

## Required fields for each extracted tool

- Purpose.
- Inputs.
- Outputs.
- Safety limits.
- Example invocation.
- Expected report location.

## Guardrails

- Tools must be reproducible.
- Tools must write reports instead of silently rewriting the paper.
- Tools must preserve historical witness material unless a human explicitly requests a clean public extraction.
- Tools must prefer narrow fixed actions over arbitrary shell execution.

## MCP boundary

A future MCP server should expose only narrow fixed tools, for example:

- `run_metadata_hygiene_audit(version)`
- `run_freeze_audit(version)`
- `run_promotion_audit(version)`
- `build_pdf(version)`
- `create_release_packet(version)`

It should not expose an unrestricted command runner.
