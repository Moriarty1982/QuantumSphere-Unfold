# v4.9.0-r17 to r19: local research line after the v4.9.0 release (source-only)

Continuation of [`../v4_9_0_r01_r16/`](../v4_9_0_r01_r16/README.md). The layers are appended verbatim from the local
full-monolith working source to
[`sources/research/parts/v490-post-release-layers.tex`](../../../sources/research/parts/v490-post-release-layers.tex).
This is **not** a release.

- Public baseline: v4.9.0, Version DOI `10.5281/zenodo.23534954`, Concept DOI `10.5281/zenodo.19210728`
  (unchanged by this line).
- Guard and residual vectors are unchanged in every layer: `R_glob = (0,1,1,1,1)`,
  `Gamma_guard = (1,1,1,1,1)`, `beta_4 = 1/256` unspent. No layer claims C5 = 0, C6/T2, a global
  photon-clock/RH theorem or global all-readout closure.
- No new prediction and no comparison with new data. The class split of r18/r19 is an offered reading; the choice of
  conversion way (decision 5 of r15) stays with the author.

## Contents

| Path | Content |
|---|---|
| `rounds/v490_r17_round.tex` … `v490_r19_round.tex` | each layer as a separate append-only block |
| `llm/` | working material in German: check scripts `k56`–`k58`, core map (`Kernkarte`, v7.7), exploration protocol on the weak mixing angle with the corrected E14 bound |

Source of the carried block: `Quantum_Sphaera_Companion_v4_8_0_source.tex` after layer v4.9.0-r19,
SHA256 `f160eb6789944f3283debc57ff7c1f61909ffc98ba91555dbc48fa5497c6c610`, lines 70132–70549; content SHA256 of
the block `a72d58537df65d07b123f8515ff1ee4f67fec4ecaf5d0b0506cdbd84431d7f14`.

Build of the candidate with the carried layers under MiKTeX 25.12, three pdfLaTeX passes: 1182 pages,
3711 labels, 0 undefined references or citations, 0 duplicate labels, no rerun warning, 58 overfull boxes
(unchanged).

## Layers

| Layer | Title | Result |
|---|---|---|
| r17 | Entropy between the frames, the photon as information singularity, and a scale dimension | `gL = 1/|b|`; eigenvalues `1/(1+beta^2)`, `beta^2/(1+beta^2)` (Hopf 3/4 and 1/4); photon = maximally mixed state at Bures distance pi/4 with undefined direction; a composable scale dimension requires the Doppler law |
| r18 | The old conversions on the scale line, and how ways A and C can hold together | `1/beta`, `e^eta`, `gL` are three readings of one offset, equal at the tribonacci point; scale quantities follow way C, readout quantities way A as state function |
| r19 | The class split applied to the main body | scale places change by 0.55–2.7 %, no statement flips; P5 = 1/2 exactly; P3 match lost (−0.15 %); P6 holds to −0.55 %; P2, H15, Omega_M unchanged |
