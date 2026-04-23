# QuantumSphere-Unfold

Public repository for the *Quantum Sphaera Companion* project line.

## Current document release reference

- Current public document release: **v3.31.0**
- Current public document DOI: **10.5281/zenodo.19699827**
- Previous public document release: **v3.30.0**
- Previous public document DOI: **10.5281/zenodo.19682951**
- Concept DOI: **10.5281/zenodo.19210728**

## Repository role

This repository is the canonical GitHub mirror for public project states, release preparation metadata, and synchronization of the working line.

The repository itself is **not** the direct Zenodo publication source for final document releases.

## Source-tree direction

The long-term direction of this repository is to hold the real modular TeX source tree of the project, so that tagged repository states remain inspectable and reconstructable.

That means:

- the live modular source should move into the repository directly
- historical material should remain explicitly recoverable
- `releases/` should hold release-side metadata, not replace the source tree
- release tags should freeze reconstructable source states

See `docs/MODULAR_SOURCE_POLICY.md` for the intended repository architecture and tag policy.

## Release workflow policy

- GitHub is used for ongoing synchronization and public project-state tracking.
- Final release documents are prepared outside the repository workflow.
- Zenodo publication is performed manually from the finalized document bundle.
- The document itself carries the concept DOI.
- The new version-specific DOI is read back from Zenodo after publication and inserted into the version history in the next maintained document state.

## Release-preparation payloads

The `releases/` directory is reserved for prepared release notes, audits, Zenodo descriptions, bibliography companions, and related metadata for upcoming or archived public release states.
