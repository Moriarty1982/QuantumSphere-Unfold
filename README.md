# Quantum Sphaera Companion

Structure-first mathematical companion material for the Quantum Sphaera / Sphere Framework project.

## Current public baseline

- Public version: `v4.7.0`
- Version DOI: `10.5281/zenodo.20232911`
- Concept DOI: `10.5281/zenodo.19210728`
- Repository: `Moriarty1982/QuantumSphere-Unfold`

The current public baseline is the Zenodo-published `v4.7.0` release. Repository changes after that release should be treated as post-release maintenance, research notes, or explicitly versioned follow-up work.

## Scope guard

This repository records a structure-first mathematical companion with guarded local/effective readout claims. It is not a peer-reviewed proof of global physical closure, global all-readout terminality, the Riemann Hypothesis, or a global QFT/GR unification theorem.

Allowed public-facing language should remain local, bounded, effective, or readout-dependent unless a later release supplies a separately audited proof.

## Release-line discipline

### `v4.7.x` stabilization line

Use this line only for public-facing hygiene:

- README and repository metadata;
- citation metadata;
- DOI and Zenodo text consistency;
- broken links or obvious public-facing wording defects;
- release-note cleanup.

Do not silently mutate the published `v4.7.0` TeX/PDF payload.

### `v4.8.0-r01` research line

The next research branch is reserved for the guarded internal program:

> Planck-Readout Metric Layer and MM/HC Field-Equation Refactor

Initial working formula:

```tex
\ell_{\mathrm{eff}}(R)=\ell_P\lambda_R
```

For tachyonic, opposite-orientation, or dual-readout contexts, a negative sign must be read as an orientation, phase, or order code unless a later formal proof explicitly upgrades the interpretation. It must not be presented as a directly observable negative physical distance.

## Citation

Use the `CITATION.cff` file in this repository, or cite the public Zenodo record through the version DOI above.

## Status

Post-`v4.7.0` work is tracked through GitHub issues and separated into metadata-only stabilization work versus research-only follow-up branches.

## Research audit tools

The [QAM/MML/MMA framework interface](scripts/qsc_audit/FRAMEWORK_INTERFACE.md) provides a shared conceptual object, relation, guard and residual context, with fixed `EXPORT` and `SCRUB` requests. The tensor role checker is its first audit adapter; mathematical equivalence remains a separate declared relation.

The standalone interface package is available at [Moriarty1982/qam-framework-interface](https://github.com/Moriarty1982/qam-framework-interface), including a rule catalog for use without this repository's TeX sources.

The [QAM tensor role checker](scripts/qsc_audit/TENSOR_GRAMMAR.md) checks explicit role data, index pairings, declared comparisons, finite readout masks, and recorded guard assumptions. It produces reproducible audit reports; it does not establish mathematical admissibility or closure. This is post-release research infrastructure.
