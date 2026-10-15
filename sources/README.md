# Quantum Sphaera Companion source tree

This directory is the canonical modular LaTeX source tree.

For the complete v4.7-derived, unreleased v4.8.0-r01 working line, use `research/v480-companion.tex` and `research/README.md`. Unlike this older modular baseline, that entry point retains the complete 1,014-page monolith and the later v4 research chain. The two entry points must not be conflated in length or integration reports.

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

Working modular active-core reading route:

Scope correction: this modular entry is not the complete v4.7.0 monolith. The repository's published v4.7.0 PDF has 1,014 pages; the 655-to-656-page comparison below concerns this older modular working tree only. The full-paper follow-up now has its separate entry at `research/v480-companion.tex` and report at `analysis/V480_Full_Monolith_Integration.md`; do not conflate the two comparisons.

- The main-text QAM interface is `parts/01_qam_mml_mma_pre_v4_infrastructure.tex`.
- Its five original formal modules remain unchanged and are included once through `parts/09_structural_tools_appendices/07_qam_runtime_details.tex`.
- Full proofs, spectral counterexamples and verification limits for the compact MM/HC and exponent sections are in `parts/09_structural_tools_appendices/06_core_proof_details.tex`.
- The main text retains the core construction, spectral hypotheses, master model, mathematical OP statements, physical readouts and live burdens. Historical synthesis, local repair/entry protocols, detailed OP transport, register memory and the computational specification are included once through `parts/09_structural_tools_appendices/08_extended_reading_details.tex`.
- Seven exact-text extractions are in `parts/09_structural_tools_appendices/reading_details/`. Existing whole technical modules are reused without copying them. The single appendix switch belongs to `parts/09_structural_tools_appendices.tex`, not to a computational component.
- `scripts/qsc_audit/reading_length_audit.py` compares settled AUX page counts and checks preservation of baseline labels and protected statement/proof/formula blocks. It rejects stale AUX files. Local before/after manifests are under `build/reading-length-audit/`; the measured result and limitations are in `analysis/Whole_Paper_Readability_Comparison.md`.
- Mathematical hypotheses and open status remain visible in the main text. This is an unreleased working-source reorganization, not a new version or a closure certificate.

Synchronization baseline:

- This initial modular synchronization was produced from the available v3.35.0 release-final bundle.
- Later v3.36.x/r-series working layers should be applied as normal commits to this source tree.
