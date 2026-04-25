# Quantum Sphaera Companion v3.35.0 modular source

This folder contains a chapter/section-level modularization of the v3.35.0 release-final TeX sources.

- Concept DOI: `10.5281/zenodo.19210728`
- Version-specific DOI: `10.5281/zenodo.19750674`

## Structure

- `active_core/main.tex` inputs `61` section files from `active_core/sections/`.
- `historical_witness/main.tex` inputs `42` section files from `historical_witness/sections/`.
- `release_metadata/` contains the release audit, Zenodo description, release notes, manifest, checksums, and diffs.
- `.github/workflows/build-v3-35-0.yml` builds both PDFs on GitHub Actions and uploads them as workflow artifacts.

The split is intentionally conservative: the master files use `\input`, not `\include`, so no extra page breaks are inserted by the modularization.

## Local build

```bash
cd active_core && pdflatex -interaction=nonstopmode -halt-on-error main.tex
cd ../historical_witness && pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Run each document three times for stable references and table of contents.
