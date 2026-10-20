# v4.8.0-r03 to r12: local research line (source-only)

This folder records a research line that was developed in a local working copy of the published
v4.8.0 source after the Zenodo release. It is **not** a release, does not change the frozen payload in
[`release/v4.8.0/`](../../../release/v4.8.0/), and has not been merged into the full-source working copy in
[`sources/research/`](../../../sources/research/) or into the v4.9.0 research candidate.

- Public baseline: v4.8.0, Version DOI `10.5281/zenodo.23365244`, Concept DOI `10.5281/zenodo.19210728`
  (unchanged by this line).
- Guard and residual vectors are unchanged in every layer: `R_glob = (0,1,1,1,1)`,
  `Gamma_guard = (1,1,1,1,1)`, `beta_4 = 1/256` unspent. No layer claims C5 = 0, C6/T2, a global
  photon-clock/RH theorem or global all-readout closure.

## Contents

| Path | Content |
|---|---|
| `Quantum_Sphaera_Companion_v4_8_0_r12_working_source.tex` | complete working source after layer r12 |
| `rounds/v480_r03_round.tex` … `v480_r12_round.tex` | each layer as a separate append-only block |
| `llm/` | working material in German: core map (`Kernkarte`), check scripts `k1`–`k26`, pre-registration notes and results H1–H8, review of the Riemann source, training data for a local guard-discipline model |

The working source differs from `release/v4.8.0/Quantum_Sphaera_Companion_v4_8_0_source.tex` only by
(a) the appended layers r03–r12 and (b) a preamble change that re-enables PDF bookmarks
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

## Pre-registration evidence

From r11 on, every prediction was committed as a note (`llm/Vorab_Notiz_*.md`) before it was computed.
The original commits are preserved, with their hashes, on the branch
[`research/v4.8.0-r03-r12-lokalgeschichte`](https://github.com/Moriarty1982/QuantumSphere-Unfold/tree/research/v4.8.0-r03-r12-lokalgeschichte)
(complete local history; it shares no ancestor with `main`). In that history each note commit is an
ancestor of the corresponding result commit. Commit dates were set by the local machine; GitHub only
attests the push date.

| Test | Note commit | Result (fixed criterion) |
|---|---|---|
| H1 δ = K/3 for all charged triplets | `81f38d3` | refuted |
| H2 neutrinos as an r = 1 triole | `434c5a8` | compatible (normal ordering, Σmν = 0.0592 eV), weakly discriminating |
| H3 triole signs as Majorana CP parities | `e3b140e` | compatible, m_ββ ≤ 3.5 meV, not testable soon |
| H4 TM1 against TM2 | `00d297e` | TM1 strongly preferred (Δχ² = 10.3) |
| H5 Hopf angle as mixing angle | `16eff15` | failed |
| H6 algebraic selection criteria for the TM1 lift | `e1e2393` | main criterion speaks against TM1 |
| H7 Heisenberg compensator as selector | `e6da7db` | no selection |
| H8 Cayley–Dickson involution as CP symmetry | `f6734ab` | tension (χ² = 8.8, 3 d.o.f.); predicts θ₂₃ = 45°, δ_CP = 270° |

## Reclassified earlier statements

- `prop:pmns-z3` and the θ₂₃ line of `thm:op1op4-unified`: refuted (r12). arctan√2 = 54.74° is not the
  maximal mixing angle; the shifted value 52.1° is about 9σ from current data.
- The CKM line of `thm:op1op4-unified` rests on the δ_CL conjecture, classified in r09 as a coincidence.
- The Riemann source is no longer used as a proof source (r04); the Θ-sum conjecture is refuted (r05).
