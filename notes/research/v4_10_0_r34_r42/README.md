# Layers v4.9.0-r34 to r42 on the 4.10 base (source-only)

Continuation of [`../v4_10_0_r32_r33/`](../v4_10_0_r32_r33/README.md). The layers are appended verbatim to
[`sources/research/parts/v490-post-release-layers.tex`](../../../sources/research/parts/v490-post-release-layers.tex). Two status
notes are added to the main body by the patch specification `llm/revision_spec_v490_r36.py` (revision rule C of r25, author
decision 2026-10-23), applied to `sources/research/parts/v470/10_sphaera_and_physics.tex`. This is **not** a release.

- Public baseline: v4.9.0, Version DOI `10.5281/zenodo.23534954`, Concept DOI `10.5281/zenodo.19210728`; working version
  `4.10.0-draft`, no 4.10 DOI reserved.
- Guard and residual vectors are unchanged in every layer: `R_glob = (0,1,1,1,1)`, `Gamma_guard = (1,1,1,1,1)`,
  `beta_4 = 1/256` unspent. No layer claims C5 = 0, C6/T2, a global photon-clock/RH theorem or global all-readout closure.
- Every layer records a test whose note (`llm/Vorab_Notiz_H19` to `H27`) was committed before the computation. For H26 and H27 the
  charge patterns were seen analytically before the note; this is disclosed in the notes, and those computations are checks, not
  predictions. The first run of `k83` reported H27b as refuted because of a rounding error in the script; only that rounding was
  corrected, and both outputs are kept (`k83_out_erstlauf.txt`, `k83_out.txt`).
- The scripts import `omul` from `k69_test_h17.py` in [`../v4_10_0_r32_r33/llm/`](../v4_10_0_r32_r33/llm/); copy it next to them to run.

## Layers

| Layer | Test | Result |
|---|---|---|
| r34 | H19 charges from the Dixon storage | Furey's number operator fits the colour group Stab(e7): sectors 0, 1/3, 2/3, 1 (singlet, triplet, conjugate triplet, singlet); the literal assignment in the outer frame fails; T and J_B map Q to 1 − Q |
| r35 | H20 inner and outer complex unit | the colour and ν_R assignment holds in the inner frame J = L_e7 and translates by P_± = ½(1 ∓ iJ); the anti-triplet sentence of `thm:three-generations` is wrong (frame mixing); Q = ½ − (i/6)L_e7 − (i/3)R_e7 |
| r36 | H21 origin of the colour/generation double use; frame rule; status notes | the cyclic symmetry e4 → e5 → e6 is the only such automorphism and a colour rotation in SU(3); generations need a three-fold structure outside 𝕆; frame rule for complex units adopted; status notes on `thm:three-generations` and `thm:SM` |
| r37 | H22 triality as self-traversal | Re((xy)z) is the Spin(8) triality form; the slot shift is outer triality with fixed group G2 ⊃ SU(3); no prohibition of a fourth generation from the structure alone; periods {1, 2, 3, 4, 6, 12} |
| r38 | H23 frame triole | matter–photon–tachyon has the form of a transposition of the slots (photon = vector slot, 1 ⊕ 7 under Spin(7)) |
| r39 | H24 chains under Hilbert-shift zoom and mixed readouts | from zoom level 2 only the triality circle survives; frames coarse, generations deep; mixed masks see one or three generations depending on the aggregation |
| r40 | H25 two-sided contraction across frames | covariant, not invariant: rule 1 up to conjugation, bilinear rule 2 changes sign under z → iz; no su(2) of triality commutes with colour; centralizer = span(L_e7, R_e7) |
| r41 | H26 roles of the ℍ factor | Lorentz left, weak SU(2) right, generations on triality; with Y/2 = Q − ½, Q_em = T3 + Y/2 gives the left-handed doublets and conjugates; T acts as charge conjugation; weak singlets absent |
| r42 | H27 compensator of the Millennium matrix | C = ½(id + iL_e7) as chirality projector gives the full left-handed content of one generation with ν_R, anomaly-free; construction under choices, not a derivation |

## Contents

| Path | Content |
|---|---|
| `rounds/v490_r34_round.tex` … `v490_r42_round.tex` | each layer as a separate append-only block |
| `llm/Vorab_Notiz_H19` … `H27` | pre-registration notes (German) |
| `llm/Ergebnis_H19` … `H27` | results (German) |
| `llm/k75_test_h19.py` … `k83_test_h27.py`, `*_out.txt` | check scripts and their outputs |
| `llm/revision_spec_v490_r36.py` | patch specification of the two status notes |

Source of the carried blocks: `Quantum_Sphaera_Companion_v4_8_0_source.tex` after layer v4.9.0-r42, SHA256 prefix `54d6d37c96d3401d`,
lines 72640–73760. Block SHA256 prefixes: r34 `1da79f62`, r35 `4053f9b1`, r36 `99a1bfc0`, r37 `4a0788de`, r38 `4a72d584`,
r39 `d8f5b9c0`, r40 `9e7c8c13`, r41 `5869daaf`, r42 `229adf2b`.

Build of the candidate with `.github/scripts/qsc_latex_build.py --source-dir sources/research` under TeX Live, against the same build
of `main`: 1224 → 1248 pages, 3802 → 3853 labels, 0 undefined references or citations, 0 duplicate labels, no rerun warning,
overfull boxes unchanged (45). Guard linter over the new layers: 0 hits.
