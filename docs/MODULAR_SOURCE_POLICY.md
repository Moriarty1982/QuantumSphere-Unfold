# Modular source policy for QuantumSphere-Unfold

## Purpose

This repository is intended to become the canonical modular source tree for the *Quantum Sphaera Companion* working line.

The main goal is that every tagged version should be inspectable and, if needed, reconstructable from the repository itself. This supports:

- reliable history inspection
- tag-based reconstruction of older states
- safer recovery after local drift or merge mistakes
- finer diffs across mathematical and editorial changes

## Core policy

1. The repository should contain the real modular TeX source tree, not only release wrapper material.
2. Every release tag should point to a reconstructable source state.
3. The `releases/` directory should contain release-side metadata only, not replace the source tree.
4. Final public Zenodo releases are still built outside the repository workflow and uploaded manually, but the repository should make those releases reproducible from tagged source states.

## Target directory layout

A preferred long-term layout is:

```text
src/
  frontmatter/
  core/
  pre_op/
  op/
  appendix/
  wrappers/

historical/

bibliography/

assets/

releases/
  vX.Y.Z-release/
```

### Meaning of the top-level directories

- `src/` — current modular TeX source tree for the live document line
- `historical/` — inherited historical blocks that must remain recoverable
- `bibliography/` — bibliography files, snapshots, and release-side bibliography companions
- `assets/` — figures, diagrams, static support files, and other non-TeX sources
- `releases/` — release notes, audits, Zenodo descriptions, and other release-side metadata

## Tag policy

Release tags should be treated as authoritative repository snapshots.

Recommended rule:

- working commits may move freely
- release tags freeze reconstructable source states
- the tagged state should contain enough source material to rebuild the corresponding document state later

## Practical working rule

For future work, prefer:

- syncing the modular TeX components into `src/` and related directories
- keeping historical material explicitly recoverable under `historical/`
- keeping release metadata under `releases/`
- treating the monolithic release document as a build/output artifact, not as the only source of truth

## Why this policy matters

With this structure, later inspection can proceed directly from GitHub:

- look up a tag
- inspect the exact modular state at that tag
- reconstruct the corresponding document if needed

This reduces dependence on ad hoc local monolith recovery and makes the project line more robust over time.
