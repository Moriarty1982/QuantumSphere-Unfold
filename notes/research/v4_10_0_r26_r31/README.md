# Layers v4.9.0-r26 to r31 on the 4.10 base (source-only)

Continuation of [`../v4_10_0_base/`](../v4_10_0_base/README.md). The layers are appended verbatim to
[`sources/research/parts/v490-post-release-layers.tex`](../../../sources/research/parts/v490-post-release-layers.tex). One status
note in `parts/v470/10_sphaera_and_physics.tex` (under the dark-energy theorem) is extended under the revision rule of r25,
with the same text as in the local full monolith (`llm/revision_spec_v490_r31.py`, applied by `llm/apply_patches.py`). This is
**not** a release.

- Public baseline: v4.9.0, Version DOI `10.5281/zenodo.23534954`, Concept DOI `10.5281/zenodo.19210728`; working version
  `4.10.0-draft`, no 4.10 DOI reserved.
- Guard and residual vectors are unchanged in every layer: `R_glob = (0,1,1,1,1)`, `Gamma_guard = (1,1,1,1,1)`,
  `beta_4 = 1/256` unspent. No layer claims C5 = 0, C6/T2, a global photon-clock/RH theorem or global all-readout
  closure.

## Contents

| Path | Content |
|---|---|
| `rounds/v490_r26_round.tex` … `v490_r31_round.tex` | each layer as a separate append-only block |
| `llm/` | pre-registration note and result H16; check scripts (H16 test, saddle check, kick-measurement dynamics, measuring device, reservoir source, compensator coherence, Markov cascade); patch specification and tool; core map (`Kernkarte`, v8.9) |

Source of the carried block: `Quantum_Sphaera_Companion_v4_8_0_source.tex` after layer v4.9.0-r31,
SHA256 `30ef2084d8363218f8be26ea1f80023fe90e42942f3fa13bfca21c9edb54824c`, lines 71626–72384; content SHA256 of the block
`daa4ea4a4e23d747f9f8bd75ff27e74a4ec1a00929066b79ba39f30bf612cd2a`.

Build of the candidate under MiKTeX 25.12, three pdfLaTeX passes: 1220 pages, 3789 labels, 0 undefined references or
citations, 0 duplicate labels, no rerun warning, 58 overfull boxes (unchanged). Title page: one Version DOI line, one Concept
DOI line.

## Layers

| Layer | Result |
|---|---|
| r26 | pre-registered test H16 (degree-6 potentials on the triple space) refuted; up to degree 6 every critical point with three distinct norms is a saddle |
| r27 | dynamics model: duality rotation plus compensator measurement; 3/4 per selective step, n = 20; one non-selective pi/6 kick from the reference state gives the Hopf state; the photon is the attractor; no finite zero of the score |
| r28 | the tachyon is an ideal measuring device when it couples through time reversal; the closed field does not stabilise itself, a replenished tachyon reservoir does; correction: the tachyon map in r21, r22, r27 is z -> iz, not J_B |
| r29 | source of the reservoir: pair creation from the vacuum supplies tachyons in the reference state; horizon, other modes and hit chain excluded |
| r30 | the compensator replaces the classical one half by a definite port; its partner is the tachyon seen through time reversal; the exchange is coherent by construction |
| r31 | the Markov cascade does not stabilise when closed; with a return path it has a unique stationary state with flux fractions beta^2 and 1 - beta^2 for every rate; status note to the dark-energy theorem extended |
