# v4.8.0-r03 to r16: local research line (source-only)

This folder records a research line that was developed in a local working copy of the published
v4.8.0 source after the Zenodo release. It is **not** a release, does not change the frozen payload in
[`release/v4.8.0/`](../../../release/v4.8.0/), and has not been merged into the full-source working copy in
[`sources/research/`](../../../sources/research/) or into the v4.9.0 research candidate. (The folder name
keeps its original range r03–r12; it now also contains r13–r16.)

- Public baseline: v4.8.0, Version DOI `10.5281/zenodo.23365244`, Concept DOI `10.5281/zenodo.19210728`
  (unchanged by this line).
- Guard and residual vectors are unchanged in every layer: `R_glob = (0,1,1,1,1)`,
  `Gamma_guard = (1,1,1,1,1)`, `beta_4 = 1/256` unspent. No layer claims C5 = 0, C6/T2, a global
  photon-clock/RH theorem or global all-readout closure.

## Contents

| Path | Content |
|---|---|
| `Quantum_Sphaera_Companion_v4_8_0_r16_working_source.tex` | complete working source after layer r16 |
| `rounds/v480_r03_round.tex` … `v480_r16_round.tex` | each layer as a separate append-only block |
| `llm/` | working material in German: core map (`Kernkarte`), check scripts `k1`–`k30`, pre-registration notes and results H1–H11, JUNO 2026 re-check, quark check, comparison with the v4.9.0 candidate, separation of colour and generation, review of the Riemann source, training data for a local guard-discipline model |

The working source differs from `release/v4.8.0/Quantum_Sphaera_Companion_v4_8_0_source.tex` only by
(a) the appended layers r03–r16 and (b) a preamble change that re-enables PDF bookmarks
(`bookmarks=true`, removal of the r25 `bookmarks=false` line, `\pdfstringdefDisableCommands` for math in
section titles). Build: three pdfLaTeX passes; audit against the previous layer without hard deviations
(0 undefined references or citations, 0 duplicate labels, no new overfull boxes).

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

The JUNO 2026 data (arXiv:2609.37895) existed when H2–H8 were fixed but had not been used; the re-check
is independent but not a test fixed before the measurement.

## Reclassified earlier statements

- `prop:pmns-z3` and the θ₂₃ line of `thm:op1op4-unified`: refuted (r12). arctan√2 = 54.74° is not the
  maximal mixing angle; the shifted value 52.1° is about 9σ from current data.
- The CKM line of `thm:op1op4-unified` rests on the δ_CL conjecture, classified in r09 as a coincidence.
- The Riemann source is no longer used as a proof source (r04); the Θ-sum conjecture is refuted (r05).
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
