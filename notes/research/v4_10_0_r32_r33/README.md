# Layers v4.9.0-r32 and r33 on the 4.10 base (source-only)

Continuation of [`../v4_10_0_r26_r31/`](../v4_10_0_r26_r31/README.md). The layers are appended verbatim to
[`sources/research/parts/v490-post-release-layers.tex`](../../../sources/research/parts/v490-post-release-layers.tex). Two Lean
modules are added to [`formal/`](../../../formal/). This is **not** a release.

- Public baseline: v4.9.0, Version DOI `10.5281/zenodo.23534954`, Concept DOI `10.5281/zenodo.19210728`; working version
  `4.10.0-draft`, no 4.10 DOI reserved.
- Guard and residual vectors are unchanged: `R_glob = (0,1,1,1,1)`, `Gamma_guard = (1,1,1,1,1)`, `beta_4 = 1/256` unspent.
  The layer claims no C5 = 0, C6/T2, global photon-clock/RH theorem or global all-readout closure.

## Contents

| Path | Content |
|---|---|
| `rounds/v490_r32_round.tex`, `v490_r33_round.tex` | each layer as a separate append-only block |
| `llm/` | pre-registration notes and results H17 and H18; check scripts k69–k74 (H17 test, axis saddle check, Dixon storage, left-invariant labels, H18 test and check); Dixon check note; core map (`Kernkarte`, v9.7) |
| `../../../formal/QSFormal/Dixon.lean` | octonions (Cayley–Dickson as in k22), triality form, A₄ characterisation, Dixon masks, algebraic cores of r26.1 and r32.1, J_B = R ∘ T on the storage |
| `../../../formal/QSFormal/Lesarten.lean` | readout-dependent readings of the ℂ factor (D₄ keeps the matter/tachyon label), ℍ factor: left and right actions, A₄ = conjugation by the binary tetrahedral group, left-invariant labels |

Source of the carried blocks: `Quantum_Sphaera_Companion_v4_8_0_source.tex`.
- r32: after layer v4.9.0-r32, SHA256 `533f0f25e05bfc6edef9266b851b94250e2b7f9b27b2b9abe6250aef245abd09`, lines 72385–72506; block
  SHA256 `9a87ff4c15aa98aaeb931780b5909ea0239d6384eda3b25db443d1de2a47bd58`.
- r33: after layer v4.9.0-r33, SHA256 `f8fd14bd5aa1d4924d14a549e9c0f4744c176fdca589cc16bc7503cd2748e672`, lines 72507–72639; block
  SHA256 `36c08c2520c7251bfc1c63fa9689ba39029c40b731b559426a768f4fe7c01a94`.

Build of the candidate under TeX Live, three pdfLaTeX passes, against the same build of `main`: 1219 → 1224 pages,
3789 → 3802 labels, 0 undefined references or citations, 0 duplicate labels, no rerun warning, overfull boxes unchanged.
The Lean modules do not import Mathlib; they were checked with Lean 4.35.0 (standard axioms only, no `sorry`); the full
`lake build` with Mathlib was not run for this change.

## Layer and checks

| Item | Result |
|---|---|
| v4.9.0-r32 | pre-registered test H17 (real-part invariants on the triple space) refuted; on the real axis the potential is linear in e₃, so critical points with three distinct norms are saddles; most minima lie on the real axis and leave G₂ unbroken |
| Dixon check (no prediction) | the generation triple fits the Dixon storage as (Im ℍ) ⊗ 𝕆 (24 of 64 bits, colour as a 9-bit submask); joint symmetry with the triality form is A₄; conflict with the Lorentz spinor of `thm:three-generations`; mixed readouts are defined in the Companion but never evaluated |
| frames on the storage | with the ℂ factor read as the amplitude plane, J_B = R ∘ T swaps the two halves; slot norms are frame-free; only D₄ keeps the matter/tachyon label (a general clock rotation mixes the sectors) |
| v4.9.0-r33 | records the Dixon check and the left-invariant labels; pre-registered test H18 (masses from the labels at the minima of the tested potentials) refuted: the angle between two slots is a flat direction (H11 family) or the slots lie parallel (H17 family) |
| left-invariant labels | with Lorentz acting from the left, the three imaginary components of the quaternionic Gram matrix are invariant labels on the right; μ_i = 2(|x_j|²|x_k|² − ⟨x_j,x_k⟩²); the right action of 2T permutes them cyclically; no mass comparison has been made |

Pre-registration: H18 was committed locally before computing (`6130814`). H17 was fixed in a container commit (2026-10-22 21:11 CEST) while the author's computer was unreachable,
sent to the author before the computation, and carried into the local history with its original time stamp (`1a39d6f` on
[`research/v4.8.0-r03-r12-lokalgeschichte`](https://github.com/Moriarty1982/QuantumSphere-Unfold/tree/research/v4.8.0-r03-r12-lokalgeschichte)).
