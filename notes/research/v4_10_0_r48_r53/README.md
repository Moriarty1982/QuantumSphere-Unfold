# Layers v4.9.0-r48 to r53 on the 4.10 base (source-only)

Continuation of [`../v4_10_0_r34_r47/`](../v4_10_0_r34_r47/README.md). The layers are appended verbatim to
[`sources/research/parts/v490-post-release-layers.tex`](../../../sources/research/parts/v490-post-release-layers.tex). This is **not** a release.

- Public baseline: v4.9.0, Version DOI `10.5281/zenodo.23534954`, Concept DOI `10.5281/zenodo.19210728`; working version
  `4.10.0-draft`, no 4.10 DOI reserved.
- Guard and residual vectors unchanged: `R_glob = (0,1,1,1,1)`, `Gamma_guard = (1,1,1,1,1)`, `beta_4 = 1/256` unspent.
- r48 makes no new prediction and therefore has no pre-registration note. It formalises results of r34, r35, r42, r43 and r47.
- r49 to r53 record the tests H33 to H37, whose notes (`llm/Vorab_Notiz_H33` … `H37`) were committed before the computation (local commits
  `ec06de3`, `8d8b761`, `42e4fcc`, `66c12ab`, `e1ee9ec`, reachable from this branch). The outcomes of H33 and H35 were seen analytically before the notes, as disclosed there.
- r51 corrects the frame rows of r41, r43, r47–r49: where they call "the frame T" the charge conjugation, the time reversal T (port exchange) is meant, not the tachyon frame.
- The scripts import `omul` from `k69_test_h17.py` in [`../v4_10_0_r32_r33/llm/`](../v4_10_0_r32_r33/llm/); copy it next to them to run.

## Layers

| Layer | Content | Result |
|---|---|---|
| r48 | charge sectors from the octonion product, in Lean | with the outer unit i on ℂ⊗𝕆: (iL)² = (iR)² = 1, iL iR = iR iL; the four P_s = ¼(1 + ℓ iL)(1 + r iR) are orthogonal projectors summing to 1; tr(LR) = 4 and tr P_s = 1, 3, 3, 1; 6Q and the r47 mask weights act as the tabulated numbers on the sectors; T P_(ℓ,r) = P_(−ℓ,−r) T; σ stays inside each sector |
| r49 | H33: is e7 the photon axis? | no: span_ℂ(1, e7) is the sum of the sectors Q = 0 and 1; 2(Q − ½) = B − L, Y/2 = T3_R + (B − L)/2, Q_em = T3_L + T3_R + (B − L)/2 (left–right symmetric form); Q_em cannot be built from L_e7, R_e7 alone. The main body uses span(1, e7) both as photon kernel K3 and as carrier of ν_R |
| r50 | H34: mixing from the r47 mask with one ε | refuted: the mass hierarchy bounds ε (≲ 0.06 for up quarks); no combination gives \|V_us\|, \|V_cb\|, \|V_ub\| within ±20 %; the leptons alone never reach the NuFIT 3σ ranges. The shape of the mask stands, the perturbation reading for mixing is withdrawn |
| r51 | H35: is e7 the reference axis of the frames? | in part: the tachyon map z ↦ iz (outer unit) fixes every sector and has the colour-compatible inner counterpart L_e7; time reversal T and J_B swap the sectors and have no inner counterpart on the colour triplet; on span(1, e7) all three frame maps have one. Charges are frame-free between matter and tachyon |
| r52 | H36: exact coupling forms D C D and D C D⁻¹, D = exp(εW) | refuted with one ε and circulant couplings; closest quark case 36 % off, but the ordering \|V_us\| ≫ \|V_cb\| ≫ \|V_ub\| comes out; the leptons alone do not fit either |
| r53 | H37: couplings from the triality form | a coupling from the triality form alone is traceless and requires m3 = m1 + m2: violated by u, d, e, and for Dirac neutrinos it needs Σm ≈ 0.115 eV, above the DESI DR2 bound (a prohibition from the structure); norm plus triality gives no quark mixing and lepton mixing only for excluded neutrino masses; the H/H̃ reading of forms K and S is refuted |

## Contents

| Path | Content |
|---|---|
| `rounds/v490_r48_round.tex` … `v490_r53_round.tex` | each layer as a separate append-only block |
| `llm/Vorab_Notiz_H33` … `H37`, `llm/Ergebnis_H33` … `H37` | pre-registration notes and results (German) |
| `llm/k89_test_h33.py` … `llm/k93_test_h37.py`, `*_out.txt` | check scripts and outputs; `k90_out_erstlauf.txt` is the first run of k90, which stopped in a diagnostic print after H34a; `k92_out_erstlauf.txt` and `k93_out_erstlauf.txt` lack parts of the after-evaluation checks |
| `../../../formal/QSFormal/Sektoren.lean` | Lean 4 (core only, no Mathlib, standard axioms): the statements above. The tables `sectors`, `colourDim`, `q6` and `weights` of `Ladungen.lean` become properties of `O.mul`. Not formalised: rank = trace of a projector; extension of the σ statement from the basis to all x by linearity. For r49: `b_minus_l`, `qem_not_sector_function`; for r51: `R_iL`, `R_iR`, `R_P4` |

Source of the carried blocks: `Quantum_Sphaera_Companion_v4_8_0_source.tex` after layer v4.9.0-r53, SHA256 prefix `6d91ada940dae9aa`.
Block SHA256 prefixes: r48 `277ba621`, r49 `07537e94`, r50 `4ca26ad4`, r51 `885df35b`, r52 `12f6b2f0`, r53 `640eba2e`. Local build of the monolith (three pdfLaTeX passes): 1231 → 1244
pages, 0 undefined references or citations, 0 duplicate labels, no rerun warning, overfull boxes unchanged (45). Build of the candidate with
`.github/scripts/qsc_latex_build.py --source-dir sources/research` under TeX Live: 1259 → 1271 pages, 3883 → 3919 labels, same hard values,
overfull unchanged (45). Guard linter over the new layers: 0 hits. `Sektoren.lean` was checked with Lean 4.35.0 without Mathlib (standard
axioms only, no `sorry`); the full `lake build` with Mathlib runs in the Lean workflow.
