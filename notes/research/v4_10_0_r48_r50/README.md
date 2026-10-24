# Layers v4.9.0-r48 to r50 on the 4.10 base (source-only)

Continuation of [`../v4_10_0_r34_r47/`](../v4_10_0_r34_r47/README.md). The layers are appended verbatim to
[`sources/research/parts/v490-post-release-layers.tex`](../../../sources/research/parts/v490-post-release-layers.tex). This is **not** a release.

- Public baseline: v4.9.0, Version DOI `10.5281/zenodo.23534954`, Concept DOI `10.5281/zenodo.19210728`; working version
  `4.10.0-draft`, no 4.10 DOI reserved.
- Guard and residual vectors unchanged: `R_glob = (0,1,1,1,1)`, `Gamma_guard = (1,1,1,1,1)`, `beta_4 = 1/256` unspent.
- r48 makes no new prediction and therefore has no pre-registration note. It formalises results of r34, r35, r42, r43 and r47.
- r49 and r50 record the tests H33 and H34, whose notes (`llm/Vorab_Notiz_H33`, `H34`) were committed before the computation (local commits
  `ec06de3`, `8d8b761`, reachable from this branch). The outcome of H33 was seen analytically before the note, as disclosed there.
- The scripts import `omul` from `k69_test_h17.py` in [`../v4_10_0_r32_r33/llm/`](../v4_10_0_r32_r33/llm/); copy it next to them to run.

## Layers

| Layer | Content | Result |
|---|---|---|
| r48 | charge sectors from the octonion product, in Lean | with the outer unit i on ℂ⊗𝕆: (iL)² = (iR)² = 1, iL iR = iR iL; the four P_s = ¼(1 + ℓ iL)(1 + r iR) are orthogonal projectors summing to 1; tr(LR) = 4 and tr P_s = 1, 3, 3, 1; 6Q and the r47 mask weights act as the tabulated numbers on the sectors; T P_(ℓ,r) = P_(−ℓ,−r) T; σ stays inside each sector |
| r49 | H33: is e7 the photon axis? | no: span_ℂ(1, e7) is the sum of the sectors Q = 0 and 1; 2(Q − ½) = B − L, Y/2 = T3_R + (B − L)/2, Q_em = T3_L + T3_R + (B − L)/2 (left–right symmetric form); Q_em cannot be built from L_e7, R_e7 alone. The main body uses span(1, e7) both as photon kernel K3 and as carrier of ν_R |
| r50 | H34: mixing from the r47 mask with one ε | refuted: the mass hierarchy bounds ε (≲ 0.06 for up quarks); no combination gives \|V_us\|, \|V_cb\|, \|V_ub\| within ±20 %; the leptons alone never reach the NuFIT 3σ ranges. The shape of the mask stands, the perturbation reading for mixing is withdrawn |

## Contents

| Path | Content |
|---|---|
| `rounds/v490_r48_round.tex` … `v490_r50_round.tex` | each layer as a separate append-only block |
| `llm/Vorab_Notiz_H33`, `H34`, `llm/Ergebnis_H33`, `H34` | pre-registration notes and results (German) |
| `llm/k89_test_h33.py`, `llm/k90_test_h34.py`, `*_out.txt` | check scripts and outputs; `k90_out_erstlauf.txt` is the first run, which stopped in a diagnostic print after H34a |
| `../../../formal/QSFormal/Sektoren.lean` | Lean 4 (core only, no Mathlib, standard axioms): the statements above. The tables `sectors`, `colourDim`, `q6` and `weights` of `Ladungen.lean` become properties of `O.mul`. Not formalised: rank = trace of a projector; extension of the σ statement from the basis to all x by linearity. For r49: `b_minus_l`, `qem_not_sector_function` |

Source of the carried blocks: `Quantum_Sphaera_Companion_v4_8_0_source.tex` after layer v4.9.0-r50, SHA256 prefix `d363c098397076ab`.
Block SHA256 prefixes: r48 `277ba621`, r49 `07537e94`, r50 `4ca26ad4`. Local build of the monolith (three pdfLaTeX passes): 1231 → 1238
pages, 0 undefined references or citations, 0 duplicate labels, no rerun warning, overfull boxes unchanged (45). Build of the candidate with
`.github/scripts/qsc_latex_build.py --source-dir sources/research` under TeX Live: 1259 → 1265 pages, 3883 → 3901 labels, same hard values,
overfull unchanged (45). Guard linter over the new layers: 0 hits. `Sektoren.lean` was checked with Lean 4.35.0 without Mathlib (standard
axioms only, no `sorry`); the full `lake build` with Mathlib runs in the Lean workflow.
