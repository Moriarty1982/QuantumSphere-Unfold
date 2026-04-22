# Bibliography for v3.31.0-release

This file is the release-side bibliography companion for the GitHub/Zenodo publication workflow.

## Why this file exists

The `.zenodo.json` metadata is well suited for a compact set of `related_identifiers`, but it is not the right place to maintain the full working bibliography of the document. This file is therefore intended to carry the release-side bibliography snapshot or bibliography checklist for the versioned release payload.

## Core release identifiers

- Concept DOI: **10.5281/zenodo.19210728**
- Previous public release DOI: **10.5281/zenodo.19682951**
- Current release tag: **v3.31.0-release**
- Current version DOI: assigned by Zenodo after archive

## Recommended bibliography structure

### 1. Project lineage and release history

List prior project records, version-specific DOIs, repository milestones, or other internal lineage documents that are cited or referenced in the release notes and historical sections.

- [ ] prior public release records
- [ ] concept DOI record
- [ ] repository release milestones

### 2. Core mathematical / structural references

List the external mathematical references actually cited in the current document, for example foundational literature on operator theory, spectral theory, geometry, dynamics, normalization methods, or any other central framework used in the release line.

- [ ] external reference 1
- [ ] external reference 2
- [ ] external reference 3

### 3. Physics / interpretive references

List the external physics references actually cited in the current document, if applicable.

- [ ] external reference 1
- [ ] external reference 2

### 4. Software / repository / tooling references

List repository, software, or workflow references that should remain visible at release level.

- GitHub repository: https://github.com/Moriarty1982/QuantumSphere-Unfold
- [ ] additional software or tooling reference

## Minimal release rule

For GitHub→Zenodo releases, keep the most important persistent external identifiers mirrored in `.zenodo.json` under `related_identifiers`, and keep the fuller bibliography snapshot in this file or in an attached `.bib` file included in the release payload.
