# QuantumSphere-Unfold

Public repository for the *Quantum Sphaera Companion* project line.

## Current document release reference

- Current public document release: **v3.35.0**
- Current public document DOI: **10.5281/zenodo.19750674**
- Previous public document release: **v3.34.0**
- Previous public document DOI: **10.5281/zenodo.19746821**
- Concept DOI: **10.5281/zenodo.19210728**

## Repository role

This repository is the canonical GitHub mirror for public project states, release preparation metadata, and synchronization of the working line.

The repository itself is **not** the direct Zenodo publication source for final document releases.

## Source-tree direction

The long-term direction of this repository is to hold the real modular TeX source tree of the project, so that tagged repository states remain inspectable and reconstructable.

That means:

- the live modular source should move into the repository directly;
- historical material should remain explicitly recoverable;
- `releases/` should hold release-side metadata, not replace the source tree;
- release tags should freeze reconstructable source states.

See `docs/MODULAR_SOURCE_POLICY.md` for the intended repository architecture and tag policy.

## v3.35.0 source status

Version v3.35.0 has been prepared as a split-bundle release with:

- Active Core final PDF/TEX;
- Historical Witness final PDF/TEX;
- audit report;
- Zenodo description;
- release notes;
- manifest and SHA-256 checksums;
- a modularized source bundle split into section-level TeX files.

The modularized v3.35.0 source passed a lossless flattening check against the final monolithic TeX files. The PDF build is intended to run from the modular source tree through GitHub Actions once the section-level source tree is present in the repository.

## Release workflow policy

- GitHub is used for ongoing synchronization and public project-state tracking.
- Final release documents are prepared outside the repository workflow.
- Zenodo publication is performed manually from the finalized document bundle.
- The document itself carries the concept DOI.
- Version-specific DOIs are recorded in the version history, release metadata, and repository release records.

## Release-preparation payloads

The `releases/` directory is reserved for prepared release notes, audits, Zenodo descriptions, bibliography companions, and related metadata for upcoming or archived public release states.
