# Release Guardian

## Purpose

The Release Guardian is responsible for release-readiness checks for the Quantum Sphaera / Companion repository.

This role is intentionally conservative. It checks release hygiene and produces reports, but it does not change mathematical content and does not promote claims.

## Responsibilities

- Check consistency between paper version, repository release version, and Zenodo version.
- Detect duplicated DOI lines, especially in title/deckblatt/frontmatter regions.
- Detect stale internal working tags in public-facing release text.
- Check title and subtitle consistency without silently changing the main title.
- Check release packet readiness: Zenodo description, GitHub release notes, manifest, checksums.
- Trigger or review freeze-audit reports before public release.

## Guardrails

- No silent shortening of paper content.
- No automatic Zenodo upload.
- No automatic merge to `main`.
- No mathematical claim promotion.
- Historical witness material may remain, but must be clearly marked as historical.
- Internal working tags may remain only in audit or historical sections, not in public release frontmatter.

## First tools

- `metadata_hygiene_audit.py`
- future: `freeze_audit.py`
- future: `doi_scan.py`
- future: `label_scan.py`
- future: `version_scan.py`

## First pilot target

Use `v4.6.0` as the first release-hygiene target once the scanner is present.
