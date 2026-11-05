# Quantum Sphaera Companion

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23991357.svg)](https://doi.org/10.5281/zenodo.23991357)

Structure-first mathematical companion material for the Quantum Sphaera / Sphere Framework project.

## Current public baseline

- Public version: `v4.10.0` (2026-11-06)
- Version DOI: [`10.5281/zenodo.23991357`](https://doi.org/10.5281/zenodo.23991357) ([Zenodo record](https://zenodo.org/records/23991357))
- Concept DOI: [`10.5281/zenodo.19210728`](https://doi.org/10.5281/zenodo.19210728)
- Previous version: `v4.9.0`, DOI `10.5281/zenodo.23534954`; earlier `v4.8.0`, DOI `10.5281/zenodo.23365244`, and `v4.7.0`, DOI `10.5281/zenodo.20232911`
- Release files: [`release/v4.10.0/`](release/v4.10.0/) (PDF, single-file TeX source, SHA256 manifest)
- Repository and source history: [Moriarty1982/QuantumSphere-Unfold](https://github.com/Moriarty1982/QuantumSphere-Unfold)

The current public baseline is the Zenodo-published `v4.10.0` release, built from the full-source research line in [`sources/research/`](sources/research/README.md). It continues `v4.9.0` on the 4.10 base: the inherited main body is revised under the rule of layer v4.9.0-r25 (dead ends archived word for word in `parts/v4100-archive.tex` with number and label kept in place, known errors corrected with status notes, open statements marked), the 30 October consolidation adds state/mediator and clock comparisons and OP5 field slices, and the layers v4.9.0-r01 to r86 are appended verbatim in `parts/v490-post-release-layers.tex`. The layers record frame typing, a construction of one generation from the Dixon algebra under named choices, tests of masses and mixing, the OP5 comparison model (closed in r80), and a joint action W1/W2 with the tachyon part as a second reading of the same field; pre-registered tests H14 to H89 are listed in [`notes/research/predictions/`](notes/research/predictions/README.md). The release source in `release/v4.10.0/` is a single file flattened from the modular sources. Guard and residual vectors are unchanged; OP5 is not closed. Repository changes after this release are post-release research; new layers are named `v4.10.0-rNN`.

## Scope guard

This repository records a structure-first mathematical companion with guarded local/effective readout claims. It is not a peer-reviewed proof of global physical closure, global all-readout terminality, the Riemann Hypothesis, or a global QFT/GR unification theorem.

Allowed public-facing language should remain local, bounded, effective, or readout-dependent unless a later release supplies a separately audited proof.

## Release-line discipline

### `v4.10.x` stabilization line

Use this line only for public-facing hygiene:

- README and repository metadata;
- citation metadata;
- DOI and Zenodo text consistency;
- broken links or obvious public-facing wording defects;
- release-note cleanup.

Do not silently mutate the published `v4.10.0`, `v4.9.0`, `v4.8.0` or `v4.7.0` TeX/PDF payloads.

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

## Full-source research line

The **v4.9.0 release** comes from the full-source research line in `sources/research/`. It integrates the
conditional neutral Cartan comparison and finite normal-source compatibility into the main reading route, with
proofs of the finite inverse/source laws, explicit assumptions and numerical negative controls; it does not claim
full regional existence or native physical identification. See the
[change record](analysis/V490_Research_Candidate.md). The historical entry filename remains
`sources/research/v480-companion.tex`; the modular sources stay the working form for later layers.

## Citation

Use the `CITATION.cff` file in this repository, or cite the public Zenodo record through the version DOI above.

The Zenodo upload helper (`tools/zenodo_publish.py`) always includes this GitHub
repository in the related-work metadata, including when a future metadata file
omits the link. Existing DOI relations are preserved. The manual Zenodo Release
workflow defaults to the v4.8.0 metadata and files; select the new release's paths
when preparing a later version. A dry run validates locally without uploading.

## Status

Post-`v4.8.0` work is tracked through GitHub issues and separated into metadata-only stabilization work versus research-only follow-up branches.

The [analysis notes](analysis/README.md), [historical working states](working_state/README.md), and [project savepoints](project_state/README.md) document research and development history. Their presence in the repository does not make them part of a published release or promote their stated mathematical status. Two findings of the OP5/QAM analysis notes, the provenance of the C5 factor 3/4 and the interval to which the detector stage fixes it, were taken into v4.8.0 as layer r94.

## Research audit tools

The [QAM/MML/MMA framework interface](scripts/qsc_audit/FRAMEWORK_INTERFACE.md) provides a shared conceptual object, relation, guard and residual context, with fixed `EXPORT` and `SCRUB` requests. The tensor role checker is its first audit adapter; mathematical equivalence remains a separate declared relation.

The standalone interface package is available at [Moriarty1982/qam-framework-interface](https://github.com/Moriarty1982/qam-framework-interface), including a rule catalog for use without this repository's TeX sources.

The [QAM tensor role checker](scripts/qsc_audit/TENSOR_GRAMMAR.md) checks explicit role data, index pairings, declared comparisons, finite readout masks, and recorded guard assumptions. It produces reproducible audit reports; it does not establish mathematical admissibility or closure. This is post-release research infrastructure.
