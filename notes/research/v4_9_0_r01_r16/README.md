# v4.9.0-r01 to r16: local research line after the v4.9.0 release (source-only)

This folder records the layers developed in the local full-monolith working source after the v4.9.0 release on
Zenodo. It is **not** a release. The layers are carried into the research candidate as
[`sources/research/parts/v490-post-release-layers.tex`](../../../sources/research/parts/v490-post-release-layers.tex),
verbatim from the working source.

- Public baseline: v4.9.0, Version DOI `10.5281/zenodo.23534954`, Concept DOI `10.5281/zenodo.19210728`
  (unchanged by this line).
- Guard and residual vectors are unchanged in every layer: `R_glob = (0,1,1,1,1)`,
  `Gamma_guard = (1,1,1,1,1)`, `beta_4 = 1/256` unspent. No layer claims C5 = 0, C6/T2, a global
  photon-clock/RH theorem or global all-readout closure.
- Layer **v4.9.0-r15** is the consolidated register of r01–r14. Layer r16 records author decisions.

## Contents

| Path | Content |
|---|---|
| `rounds/v490_r01_round.tex` … `v490_r16_round.tex` | each layer as a separate append-only block |
| `llm/` | working material in German: check scripts `k37`–`k55`, pre-registration notes and results H14, H15, two exploration protocols (weak mixing angle, mathematical core) with every variant counted, core map (`Kernkarte`, v7.4) |

Source of the carried block: `Quantum_Sphaera_Companion_v4_8_0_source.tex` after layer v4.9.0-r16,
SHA256 `613d9ecb107dccc79f5b686941a352635422e83f378b8f4234aaa537a85352de`, lines 67718–70131; content SHA256 of
the block `ed05bb7ef631a4ae91b91b8789806d5c4ee43a053e5c7266af13d48e31abfb7b`.

Build of the candidate with the carried layers under MiKTeX 25.12, three pdfLaTeX passes: 1173 pages,
3693 labels, 0 undefined references or citations, 0 duplicate labels, no rerun warning, 58 overfull boxes
(unchanged).

## Layers

| Layer | Title |
|---|---|
| r01 | The photon frame as neutral axis and the conversion of constants |
| r02 | The round trip about the photon and the Umkehrwalze |
| r03 | The compensator as a two-arm interferometer |
| r04 | The compensator as a matrix on the electric–magnetic doublet |
| r05 | The Millennium matrix on the doublet, a third axis near rotating black holes, a photon from matter and tachyon |
| r06 | The tachyon hit chain, its acceleration, and the Higgs field |
| r07 | The cone angle and the weak mixing angle (H14, H15) |
| r08 | Frame drift, atomic clocks and the Hubble tension |
| r09 | What the local frame factor can be |
| r10 | A reading of the C5 factor 3/4 and a class of shape-(iii) witnesses |
| r11 | A minimal dynamics for Reading B: kicked duality rotation |
| r12 | A reconstruction of the bound Δ_γ < 1/5 in place of the missing r65 |
| r13 | The time scale of the kicked duality dynamics |
| r14 | Why six kicks per beat: readout directions from the triole and the Umkehrwalze |
| r15 | Consolidated register of r01–r14 and the ways out of v4.8.0-r17 |
| r16 | Author decisions on the open readings of r15 |

## Pre-registration evidence

The pre-registration notes were committed before the comparison; the commits are in the local history, which
is pushed fast-forward to the branch
[`research/v4.8.0-r03-r12-lokalgeschichte`](https://github.com/Moriarty1982/QuantumSphere-Unfold/tree/research/v4.8.0-r03-r12-lokalgeschichte)
(no common ancestor with `main`). Commit dates were set by the local machine; GitHub only attests the push date.

| Test | Note commit | Result |
|---|---|---|
| H14 cone angle = 2θ_W, i.e. sin²θ_W = (1 − β_sym)/2 | `5911161` | refuted as an exact relation (z = +8.2 against the on-shell value from PDG 2025 masses); not decidable at tree level; disclosed as formulated after the closeness was noticed, no support in any case |
| H15 cot θ_W (on-shell) = γ_L, γ_BI from the Meissner counting equation | `62c505d` | prediction fixed before any comparison: m_W = 80.3615 ± 0.0018 GeV; comparison with the first m_W world average or combination published after 2026-10-21 pending; support only if that measurement also excludes the SM value at 3σ |

## Main results

- The conversion law with γ_L does not compose over three frames; a Doppler law does; the tribonacci
  condition of the main body is equivalent to cosh 2η = e^η (r01).
- The round trip about the photon with a change of side acts as charge conjugation; an involutive
  exchange of matter and tachyon must be antilinear (E ↔ B) (r02).
- The compensator is the bright port of a two-arm interferometer; for a static charge it gives a dyon, not a
  photon (r03, r04).
- A drift of the frame factor large enough for the Hubble tension changes α by about six orders of magnitude
  more than atomic clocks allow; `prop:H0-tension` has no working mechanism (r08, r09).
- The C5 factor 3/4 arises from a duality rotation by π/6 followed by compensation; read out at the triole and
  its image under the Umkehrwalze this is the author's intended reading (r10, r11, r14, r16).
- Δ_γ < 1/5 is derived under stated premises; the r65 text is lost (r12).
