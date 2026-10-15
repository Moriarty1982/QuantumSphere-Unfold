# Quantum Sphaera Companion

Structure-first mathematical companion material for the Quantum Sphaera / Sphere Framework project.

## Current public baseline

- Public version: `v4.8.0` (2026-10-14)
- Version DOI: `10.5281/zenodo.23365244`
- Concept DOI: `10.5281/zenodo.19210728`
- Previous version: `v4.7.0`, DOI `10.5281/zenodo.20232911`
- Release files: [`release/v4.8.0/`](release/v4.8.0/) (PDF, TeX source, SHA256 manifest)
- Repository and source history: [Moriarty1982/QuantumSphere-Unfold](https://github.com/Moriarty1982/QuantumSphere-Unfold)

The current public baseline is the Zenodo-published `v4.8.0` release. It carries the full v4.7.0 monolith, the source-only layers v4.7.0-r85 to r94 recorded after the v4.7.0 release, and the opening layer of the v4.8.0 line, v4.8.0-r01 (Planck-Readout Metric Layer). Guard and residual vectors are unchanged from v4.7.0. Repository changes after this release should be treated as post-release maintenance, research notes, or explicitly versioned follow-up work.

## Scope guard

This repository records a structure-first mathematical companion with guarded local/effective readout claims. It is not a peer-reviewed proof of global physical closure, global all-readout terminality, the Riemann Hypothesis, or a global QFT/GR unification theorem.

Allowed public-facing language should remain local, bounded, effective, or readout-dependent unless a later release supplies a separately audited proof.

## Release-line discipline

### `v4.8.x` stabilization line

Use this line only for public-facing hygiene:

- README and repository metadata;
- citation metadata;
- DOI and Zenodo text consistency;
- broken links or obvious public-facing wording defects;
- release-note cleanup.

Do not silently mutate the published `v4.8.0` or `v4.7.0` TeX/PDF payloads.

### `v4.8.0` research line: Planck-Readout Metric Layer

> Planck-Readout Metric Layer and MM/HC Field-Equation Refactor

The first part is published as v4.8.0-r01. It defines the readout-calibrated Planck scale

```tex
\ell_{\mathrm{eff}}(R)=\ell_P\lambda_R
```

with an orientation code $o_R=\operatorname{sgn}\lambda_R$, recovers the matter-frame Planck scale up to a declared calibration error, and identifies the photon-frame Planck length of the main corpus as the instance $\lambda_\gamma=\gamma_L^{-3/2}$.

A negative sign is an orientation code. It is kept separate from the interval signature of the r82 tachyon-frame scale and must not be presented as a directly observable negative physical distance.

Still open on this line: the MM/HC field-equation refactor.

The [full-source research working copy](sources/research/README.md) now has a separate entry point, `sources/research/v480-companion.tex`, derived from the complete 1,014-page v4.7.0 monolith. It retains the entire baseline source with a byte-level map, separates the human reading route from complete technical support, and proposes the guarded v4.8 integration interface. This is not a published v4.8 release, a complete correction of all inherited arguments, or a replacement of the frozen v4.7.0 payload. The older modular `sources/active-core.tex` is a different source/version scope.

## Citation

Use the `CITATION.cff` file in this repository, or cite the public Zenodo record through the version DOI above.

## Status

Post-`v4.8.0` work is tracked through GitHub issues and separated into metadata-only stabilization work versus research-only follow-up branches.

The [analysis notes](analysis/README.md), [historical working states](working_state/README.md), and [project savepoints](project_state/README.md) document research and development history. Their presence in the repository does not make them part of a published release or promote their stated mathematical status. Two findings of the OP5/QAM analysis notes, the provenance of the C5 factor 3/4 and the interval to which the detector stage fixes it, were taken into v4.8.0 as layer r94.

## Research audit tools

The [QAM/MML/MMA framework interface](scripts/qsc_audit/FRAMEWORK_INTERFACE.md) provides a shared conceptual object, relation, guard and residual context, with fixed `EXPORT` and `SCRUB` requests. The tensor role checker is its first audit adapter; mathematical equivalence remains a separate declared relation.

The standalone interface package is available at [Moriarty1982/qam-framework-interface](https://github.com/Moriarty1982/qam-framework-interface), including a rule catalog for use without this repository's TeX sources.

The [QAM tensor role checker](scripts/qsc_audit/TENSOR_GRAMMAR.md) checks explicit role data, index pairings, declared comparisons, finite readout masks, and recorded guard assumptions. It produces reproducible audit reports; it does not establish mathematical admissibility or closure. This is post-release research infrastructure.
