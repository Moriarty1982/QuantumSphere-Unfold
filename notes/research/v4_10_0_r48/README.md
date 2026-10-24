# Layer v4.9.0-r48 on the 4.10 base (source-only)

Continuation of [`../v4_10_0_r34_r47/`](../v4_10_0_r34_r47/README.md). The layer is appended verbatim to
[`sources/research/parts/v490-post-release-layers.tex`](../../../sources/research/parts/v490-post-release-layers.tex). This is **not** a release.

- Public baseline: v4.9.0, Version DOI `10.5281/zenodo.23534954`, Concept DOI `10.5281/zenodo.19210728`; working version
  `4.10.0-draft`, no 4.10 DOI reserved.
- Guard and residual vectors unchanged: `R_glob = (0,1,1,1,1)`, `Gamma_guard = (1,1,1,1,1)`, `beta_4 = 1/256` unspent.
- r48 makes no new prediction and therefore has no pre-registration note. It formalises results of r34, r35, r42, r43 and r47.

## Layer

| Layer | Content | Result |
|---|---|---|
| r48 | charge sectors from the octonion product, in Lean | with the outer unit i on ℂ⊗𝕆: (iL)² = (iR)² = 1, iL iR = iR iL; the four P_s = ¼(1 + ℓ iL)(1 + r iR) are orthogonal projectors summing to 1; tr(LR) = 4 and tr P_s = 1, 3, 3, 1; 6Q and the r47 mask weights act as the tabulated numbers on the sectors; T P_(ℓ,r) = P_(−ℓ,−r) T; σ stays inside each sector |

## Contents

| Path | Content |
|---|---|
| `rounds/v490_r48_round.tex` | the layer as a separate append-only block |
| `../../../formal/QSFormal/Sektoren.lean` | Lean 4 (core only, no Mathlib, standard axioms): the statements above. The tables `sectors`, `colourDim`, `q6` and `weights` of `Ladungen.lean` become properties of `O.mul`. Not formalised: rank = trace of a projector; extension of the σ statement from the basis to all x by linearity |

Source of the carried block: `Quantum_Sphaera_Companion_v4_8_0_source.tex` after layer v4.9.0-r48, SHA256 prefix `87913252607c6c4f`.
Block SHA256 prefix: r48 `277ba621`. Local build of the monolith (three pdfLaTeX passes): 1231 → 1234 pages, 3766 → 3772 labels, 0 undefined
references or citations, 0 duplicate labels, no rerun warning, overfull boxes unchanged (45). Build of the candidate with `.github/scripts/qsc_latex_build.py --source-dir sources/research` under TeX Live: 1259 → 1261 pages, 3883 → 3889
labels, same hard values, overfull boxes unchanged (45). Guard linter over the new layer: 0 hits. `Sektoren.lean` was checked with Lean 4.35.0 without
Mathlib (standard axioms only, no `sorry`); the full `lake build` with Mathlib runs in the Lean workflow.
