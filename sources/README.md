# Quantum Sphaera Companion source tree

This directory is the canonical modular LaTeX source tree.

Versioning rule:

- `sources/` contains the current working source state.
- Git tags such as `v3.37.0` define release snapshots.
- Build artifacts are produced by GitHub Actions and should not be committed as source.

Entry points:

- `active-core.tex` builds the current active Companion core.
- `historical-witness.tex` builds the preserved historical witness.
- `qsc-common.tex` contains the shared package, theorem, macro, and layout layer.
- `parts/` contains active-core document parts.
- `historical/` contains historical-witness document parts.

Synchronization baseline:

- This initial modular synchronization was produced from the available v3.35.0 release-final bundle.
- Later v3.36.x/r-series working layers should be applied as normal commits to this source tree.
