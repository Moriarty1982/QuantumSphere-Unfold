# v4.8.0-r03 to r20: local research line (source-only)

This folder records a research line that was developed in a local working copy of the published
v4.8.0 source after the Zenodo release. It is **not** a release and does not change the frozen payload in
[`release/v4.8.0/`](../../../release/v4.8.0/). Its layers, together with the v4.8.0 release layers r85–r94
and v4.8.0-r01, r02, are carried into the v4.9.0 research candidate in
[`sources/research/`](../../../sources/research/) as appended parts (see *Integration into the v4.9.0
candidate* below). (The folder name keeps its original range r03–r12; it now contains r03–r20.)

- Public baseline: v4.8.0, Version DOI `10.5281/zenodo.23365244`, Concept DOI `10.5281/zenodo.19210728`
  (unchanged by this line).
- Guard and residual vectors are unchanged in every layer: `R_glob = (0,1,1,1,1)`,
  `Gamma_guard = (1,1,1,1,1)`, `beta_4 = 1/256` unspent. No layer claims C5 = 0, C6/T2, a global
  photon-clock/RH theorem or global all-readout closure.

## Contents

| Path | Content |
|---|---|
| `Quantum_Sphaera_Companion_v4_8_0_r20_working_source.tex` | complete working source after layer r20 (local tag `RC25`, SHA256 `a1b988d3c9e3642f93e201bcb56d6ff03020ae6f284339f29c7030f7b092ebe5`) |
| `rounds/v480_r03_round.tex` … `v480_r20_round.tex` | each layer as a separate append-only block |
| `llm/` | working material in German: core map (`Kernkarte`), check scripts `k1`–`k36`, pre-registration notes and results H1–H13, JUNO 2026 re-check, quark check, comparison with the v4.9.0 candidate, separation of colour and generation, review of the Riemann source, training data for a local guard-discipline model |

The working source differs from `release/v4.8.0/Quantum_Sphaera_Companion_v4_8_0_source.tex` only by
(a) the appended layers r03–r20 and (b) a preamble change that re-enables PDF bookmarks
(`bookmarks=true`, removal of the r25 `bookmarks=false` line, `\pdfstringdefDisableCommands` for math in
section titles). Build: three pdfLaTeX passes; audit against the previous layer without hard deviations
(0 undefined references or citations, 0 duplicate labels, no new overfull boxes). Under MiKTeX 25.12 the r20
source gives 1096 pages, 3474 labels and 986 bookmarks; the v4.8.0 tag rebuilt under the same toolchain
gives 1045 pages and 3369 labels.

## Layers

| Layer | Title |
|---|---|
| r03 | Dimensional and numerical audit of the physical-constant layer |
| r04 | Decoupling from the Riemann source and standalone Sphaera transformations |
| r05 | Corrected explicit formula in the field-equation and Theta–R layer |
| r06 | Signature of the biquaternion kernel and the complex-vector reading |
| r07 | Sector assignment and duality angle in the complex-vector reading |
| r08 | Test of prediction P1 (photon-frame unfolding) |
| r09 | Tests of P2 and P3, and re-classification of earlier results |
| r10 | The Koide structure in the complex-vector reading |
| r11 | Pre-registered test of the phase relation δ = K/3 |
| r12 | Pre-registered neutrino tests, octonionic flavour group, PMNS reclassification |
| r13 | JUNO 2026 re-check, associator of the generation triple, colour–generation assignment |
| r14 | Separating colour and generation (sedenions G₂ × S₃; triality form) |
| r15 | The octonionic Hopf fibration as carrier of the triality slots |
| r16 | Pre-registered test of masses from invariants on the triple space |
| r17 | Time direction of the cosmological fractions |
| r18 | Three-frame typing of the frame offset and correction of r17 |
| r19 | Frame cubes, transition group and holonomy |
| r20 | The tachyon frame, complex rapidity and the holonomy test H13 |

## Pre-registration evidence

From r11 on, every prediction was committed as a note (`llm/Vorab_Notiz_*.md`) before it was computed.
The original commits are preserved, with their hashes, on the branch
[`research/v4.8.0-r03-r12-lokalgeschichte`](https://github.com/Moriarty1982/QuantumSphere-Unfold/tree/research/v4.8.0-r03-r12-lokalgeschichte)
(complete local history; it shares no ancestor with `main`). In that history each note commit is an
ancestor of the corresponding result commit. Commit dates were set by the local machine; GitHub only
attests the push date.

| Test | Note commit | Result (fixed criterion; NuFIT 6.0 unless stated) |
|---|---|---|
| H1 δ = K/3 for all charged triplets | `81f38d3` | refuted |
| H2 neutrinos as a signed-root r = 1 triole | `434c5a8` | compatible (normal ordering, Σmν = 0.059 eV); JUNO 2026 supports normal ordering |
| H3 triole signs as Majorana CP parities | `e3b140e` | compatible, m_ββ ≤ 3.5 meV, not testable soon |
| H4 TM1 against TM2 | `00d297e` | TM1 strongly preferred over TM2; with JUNO 2026 TM1 alone disfavoured (χ² = 9.6, 2 d.o.f.) |
| H5 Hopf angle as mixing angle | `16eff15` | failed |
| H6 algebraic selection criteria for the TM1 lift | `e1e2393` | main criterion speaks against TM1 |
| H7 Heisenberg compensator as selector | `e6da7db` | no selection |
| H8 Cayley–Dickson involution as CP symmetry | `f6734ab` | tension (χ² = 8.8); with JUNO 2026 disfavoured (χ² = 14.0, 3 d.o.f.) |
| H9 sin²θ₁₂ = β_sym²/cos²θ₁₃ = 0.30862 | `b75170d` | found after the fact; test is the next JUNO release with σ ≤ 0.004 |
| H10 associator as selector | `a6b5bcb` | no selection; [e₄,e₅,e₆] = −2e₇ |
| H11 masses as slot norms at critical points of G₂ × S₃ invariants (degree ≤ 4) | `8e5eaa9` | refuted: at most two distinct norms; degree ≥ 6 necessary (tolerance change disclosed, verdict analytic) |
| H12 assignment of γ_L, Ω_M and the solar angle to rapidity cross terms under broken J-symmetry | `a593f5d` | sin²θ₁₂ = 0.2991 ± 0.0057 against H9's 0.3086; not separable by the fixed criterion (1.36σ at σ = 0.004, limited by Ω_M); no test |
| H13 readout factor as cosine of the Wigner holonomy of a triole boost loop | `645295f` | refuted: δ = 28.56°, cos δ = 0.878, z = −7.9; a post-hoc half-angle observation is recorded as not counting |

The JUNO 2026 data (arXiv:2609.37895) existed when H2–H8 were fixed but had not been used; the re-check
is independent but not a test fixed before the measurement.

## Reclassified earlier statements

- `prop:pmns-z3` and the θ₂₃ line of `thm:op1op4-unified`: refuted (r12). arctan√2 = 54.74° is not the
  maximal mixing angle; the shifted value 52.1° is about 9σ from current data.
- The CKM line of `thm:op1op4-unified` rests on the δ_CL conjecture, classified in r09 as a coincidence.
- The Riemann source is no longer used as a proof source (r04); the Θ-sum conjecture is refuted (r05).
- `thm:dark-energy` (Ω_Λ = 1 − β_sym²) held at all epochs is incompatible with item (2) of
  `prop:saturation`: the measured expansion history requires β_sym to decrease, the proposition lets it rise
  (r17, narrowed in r18; `prop:H0-tension` itself uses the drift only through the frame factor).
- The frame factor γ_L used for converting constants between matter and photon frame is the matter–tachyon
  rapidity cross term (cosh 2η = 1.864); the matter–photon term is cosh η = 1.197. The observer position
  z₋ = 0.422 of `thm:frame-offset` is a halving in velocity instead of rapidity (r18).
- In the complex-vector reading no Lorentz transformation relates matter, tachyon and photon; matter and
  tachyon are related by the duality rotation, which has a ℤ₂ holonomy around the photon (r19). The rapidity of
  a superluminal speed, artanh(1/v) + iπ/2, has the duality angle as imaginary part; with it the matter–tachyon
  cross term is −i sinh 2η, not γ_L (r20).
- `thm:three-generations` places colour and generation on the same octonionic triplet (r13). The octonionic
  flavour analysis of r12 is therefore conditional on reading the triplet as generation space; quark
  statements require separating the two first. Layer r14 proposes generations = the three triality slots of
  Re((xy)z) on 𝕆 ⊕ 𝕆 ⊕ 𝕆 (S₃ commuting with G₂; nine independent coloured states) and withdraws the
  lepton-mixing reading of the order-96 stabilizer of r12, which then lies inside the colour group.

## Relation to the v4.9.0 research candidate

Independent agreement on the Koide equal-norm condition, on the positive phase chambers
|θ − 2πj/3| ≤ π/12, and on not asserting a Riemann or GUE theorem. The candidate admits only non-negative
roots for the physical Koide ratio; H2 and H3 are tests of the signed-root relation. See
`llm/Abgleich_v49_Linie.md`.

## Integration into the v4.9.0 candidate

The v4.9.0 candidate in `sources/research/` was built from the v4.7.0 source and did not contain the v4.8.0
release layers. It now carries, after the last preserved fragment of the support route:

- `parts/v480-release-layers.tex`: v4.7.0-r85 to r94 and v4.8.0-r01, r02, verbatim from the working source;
- `parts/v480-post-release-layers.tex`: v4.8.0-r03 to r20, verbatim from the working source.

The preserved v4.7 fragments are not edited. Two repairs that r85 made inside the full monolith (the unity
theorem's equivalence list ends at item (v); the Stone–von Neumann step is cited at Lemma 13.2, Step 3, and is
withdrawn as a proof step since r04) are carried as qualifications in `parts/premise-audit.tex`, together with
the decided Θ-sum conjecture (r05) and pointers to the registers of r09 and r17–r20.

Build of the integrated candidate (MiKTeX 25.12, three passes): 1124 pages and 3590 labels, against 1044 pages
and 3404 labels for the candidate before integration; 0 undefined references or citations, 0 duplicate labels,
no new overfull boxes. All 87 outward references of the carried layers resolve; no label collides.
