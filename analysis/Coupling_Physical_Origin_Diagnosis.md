# Physical-Origin Diagnosis of the Coupling Discrepancy

Date: 2026-10-15. Status: conditional discrimination between mechanisms, not an identification of a physical cause. This follow-up is kept outside the main TeX document until a native mechanism is determined. It uses the same rounded frame input, assumed radius/phase law and historical mass benchmark as the preceding coupling audit.

## Conclusion First

The most direct candidate within the written architecture is a mode-dependent response of the triadic interaction: virtual transitions can change the effective coupling phase or weight different complementary modes differently. This is a structural preference among hypotheses, not evidence that a matter/tachyon sector or a gravitational mediator exists.

Three simpler explanations do not work in their specified scope:

- The QAM namespace migration or a covariantly transported coordinate change cannot change a physical spectrum.
- A universal redshift of the entire operator cannot change co-located mass ratios. Changing only a selected coupling while leaving other energy blocks fixed is a physical modification, not that universal redshift.
- In the earlier canonical positive-gap finite model, kinetic dressing induced by the same Planck-gapped complement is many orders too small. Ordinary one-loop QED matching also has the wrong sign pattern to repair both discrepancies.

The important positive result is that the previously fitted comparison weights have a possible dynamical interpretation: an **inverse-gap response tensor**, rather than an arbitrarily changed Hilbert norm. Its entries remain unevaluated native data.

The subsequent [triadic-propagator identification attempt](Triadic_Propagator_Identification.md) now derives the exact effective link from the paper's three-probe architecture. It identifies the invariant cycle phase and the mandatory diagonal/norm responses, tests pure frame rephasings and gives a guarded connection/holonomy route. It does not determine the native interaction coefficients or a gravitational phase.

## What Is Already in the Paper

The retained source `sources/research/parts/v470/10_sphaera_and_physics.tex`, under `thm:master-field-equation`, writes the effective operator schematically as

```text
Omega = m0 I + alpha P M P + c_T T + gamma H_C.
```

Here `c_T` denotes the source product `beta g_Y`, not the frame input `beta_sym=0.5493`. The source's `prop:triadic-two-probe` also supplies symbolic inter-probe and complementary-channel couplings; `thm:variational-form` places these in a proposed effective action. The source does not provide their numerical generation matrix elements or a derived Standard Model interaction. Probe-sector labels are not automatically the three lepton generations.

On the declared positive common carrier with orthogonal `P`, the bare scalar and projected `P M P` terms have no `P -> I-P` block. For the minimal defect penalty already analyzed in `parts/native-operator-link.tex`, `[H_C,P]=0` also holds. Under **that restricted realization**, therefore,

```text
V = (I-P) Omega P = c_T (I-P) T P.
```

This singles out the triadic interaction as the existing source of off-sector mixing. A more general compensator with a nonzero cross block changes this conclusion and must be supplied explicitly. The generation embedding and physical mass readout remain extra obligations.

## Deriving a Response Tensor Rather Than Fitting a Metric

Consider the same additional finite canonical Hermitian model

```text
Omega = [[A, V*], [V, D]],       D >= Delta_min I > 0.
```

For a real energy `E` below the complementary spectrum, eliminate the complementary coordinate:

```text
y = -(D-E I)^(-1) V x,
[A-N(E)] x = E x,
N(E) = V* (D-E I)^(-1) V.
```

Thus the self-energy in the pole equation is `Sigma(E)=-N(E)`. This is direct block elimination. Low/high-sector effective Hamiltonians are also the setting of the [Schrieffer-Wolff method studied by Bravyi, DiVincenzo and Loss](https://arxiv.org/abs/1105.0675); no native Sphaera interpretation follows from that methodological connection.

If `V=mu B`, choose a declared energy reference `Delta_ref` and define

```text
H_resp(E) = Delta_ref (D-E I)^(-1),
N(E) = (mu^2/Delta_ref) B* H_resp(E) B.
```

This derives a dimensionless positive response tensor in the complementary output space. Modes with a lower positive excitation gap contribute more strongly. In a geometrical interpretation, different internal mode overlaps or spectra could change these gaps, but the relevant operator and geometry-to-spectrum relation must be exhibited. A tensor tag or a single universal curvature factor does not supply them.

`H_resp` is **not** the kinetic metric `H` of the previous weighted-Hilbert model. The same leading Gram form can arise from these two different mechanisms; their exact energy dependence differs. In particular, the flat-gap mass formula with a newly selected Hilbert metric is not the exact equation for a canonical model with non-flat `D`.

For the historical leading-ratio fit, the earlier weights

```text
h = (1.146019066893, 0.987511261324, 1)
```

would correspond, in the aligned output basis and at `E=0`, to

```text
Delta_i/Delta_ref = 1/h_i
                 = (0.872585831152, 1.012646679754, 1).
```

This is the same leading inverse-gap freedom seen in the earlier non-flat-gap fit. It is a dynamically interpretable candidate, not a derivation of those numbers: the benchmark still fixes the gap ratios. It also does not repair the absolute suppression for Planck gaps and electroweak mixing. The previously tau-calibrated intermediate mixing is needed in that fitted Planck-gap example, or a different direct-block/scale mechanism must be provided.

## Why Pure Planck-Induced Norm Dressing Is Too Small

Differentiation gives

```text
N'(E) = V* (D-E I)^(-2) V >= 0.
```

The reconstructed full state has exact norm

```text
||x||^2 + ||y||^2 = x* [I+N'(E)] x.
```

Expanding the pole equation about zero gives the first-order generalized problem

```text
[A-N(0)] x = E [I+N'(0)] x + O(E^2).
```

Consequently a physical norm dressing and an induced mass response are linked by the same propagator, not independently adjustable comparison entries. In this finite positive-gap setting,

```text
||N'(E)|| <= ||V||^2/(Delta_min-|E|)^2,      |E| < Delta_min,
||N(E)-N(0)-E N'(0)||
    <= ||V||^2 E^2/[Delta_min^2 (Delta_min-|E|)].
```

The first inequality follows from the resolvent bound; the second follows from the exact second-order resolvent remainder. These justify the stated low-energy expansion, not a general interacting-field-theory approximation.

With the previous `B` and a flat Planck gap:

| Explicit mixing choice | Largest induced norm correction at zero |
| --- | ---: |
| Electroweak reference `mu=174.10358... GeV` | `1.91763e-34` |
| Previously tau-calibrated `mu=4.79638e9 GeV` | `1.45538e-19` |

For comparison, an aligned **kinetic-only** fit at fixed mass numerator, with `K=I+positive dressing`, requires at least `||K-I|| >= max(h)/min(h)-1 = 0.1605124...`. To see this, `q_i/k_i` must have the fitted ratios, hence `k_i` is proportional to `1/h_i`; its maximum/minimum ratio is `max(h)/min(h)`, and its minimum is at least one. This restricted mechanism is incompatible with either small norm correction above.

This does not exclude an independent microscopic kinetic tensor, a low-lying resonance, a gapless sector, stronger mixing or an indefinite realization. Those change the hypotheses and require a separate physical stability/normalization analysis. It also does not exclude an order-one *relative inverse-gap response*, whose derivative can still be tiny at Planck gaps.

## Relative Phase: Small Coupling Change, Large Small-Root Response

The local cyclic root candidate has

```text
B = a I + z U + conjugate(z) U*,       z = exp(i theta)/sqrt(12).
```

The earlier benchmark inversion gave `delta theta=-0.002566002463 rad`, or approximately `-0.147021 degrees`. Holding the imposed radius fixed, this changes the matrix by

```text
||delta B||_F/||B||_F = 0.001814437244 = 0.18144...%,
||delta B||_op/||B||_op = 0.001457435962.
```

The resulting leading ratios are `(0.0002874630623,0.0594619634192,1)`. Their remaining relative errors against the historical benchmark are about `-0.04274%` and `-0.002286%`. This is not an experimental fit at that accuracy, and the phase was selected from the benchmark. It does show why a weak coherent modification of a coupling can produce a large *relative* change near the small-root cancellation. A 14.6% effective electron-mode weight does not require a 14.6% change of every matrix entry.

This changes relative cyclic coefficients, not a common factor `exp(i phi) B`. The singular spectrum changes, so it cannot be removed by left/right unitary rephasing. It is not by itself an observable CP-violation claim: that would require the other interactions and rephasing invariants of a full model.

### When Independently Shifted Sectors Can Interfere

For two orthogonal complementary channels, put

```text
V = [V_m; exp(i phi) V_t],       D = diag(D_m,D_t).
```

Then `N(E)=V_m* R_m V_m + V_t* R_t V_t`; the constant relative phase cancels exactly. Independent frame offsets do not by themselves supply the desired correction.

If the sectors interact, the resolvent has an off-diagonal block `R_mt`, and the response additionally contains

```text
exp(i phi) V_m* R_mt V_t + exp(-i phi) V_t* R_tm V_m.
```

These coherent cross terms can change the eigenvalues. A shared final/intermediate channel is another way to obtain nonzero interference. The numerical report includes both disconnected and coupled positive toy complements, not native frame matrices. Phase gradients in a spacetime-dependent field would also require the kinetic connection to be transformed; this constant-phase test is not a treatment of that separate dynamics.

One explicit mediator construction makes the requirement precise. With a third positive complementary block `D_med` and couplings `X` from input to mediator and `Y` from output to mediator, eliminating that mediator produces

```text
V_eff(E) = V0 - Y* (D_med-E I)^(-1) X.
```

This correction can carry a relative complex phase. The same elimination also changes `A` by `-X* R X`, the output block by `-Y* R Y`, and the energy-dependent normalization. Selecting the vertex correction alone would not be a consistent elimination. Calling the mediator gravitational additionally requires a specified action, conserved currents and the actual mixed-sector matrix elements. The calculation does not establish tachyonic propagation, a photon rest frame or a wormhole.

## Ordinary Radiative Matching Does Not Explain This Pattern Alone

[Sumino, equation (2)](https://arxiv.org/html/0812.2090v2#S0.E2) gives the one-loop QED pole/running-mass relation. As a diagnostic only, suppose the candidate represents common-scale MSbar running masses. To first order, their ratios acquire

```text
delta(m_i/m_tau)/(m_i/m_tau)
    = [3 alpha/(2 pi)] log(m_tau/m_i).
```

Using the candidate's ratios and illustrative `alpha=1/137.036` gives approximately `(+2.889%,+0.979%,0)`. The needed corrections are `(+14.602%,-1.249%,0)`. Thus ordinary one-loop QED matching has the wrong sign for the middle/largest correction and too small an electron correction in this assignment. Reversing the conversion reverses both signs and still fails. The native mass scheme and matching scale are not specified, so this is a test of a proposed explanation, not an applied radiative correction to the paper.

Additional nonuniversal vertex/threshold corrections are not excluded by this test. Sumino's family-gauge construction is an example of an extra interaction, not evidence that that particular interaction is present here.

## What Would Actually Identify the Cause

The strongest next calculation is not another unconstrained metric fit. It is the projected, generation-resolved inverse propagator from the already proposed action, including its mixed-channel blocks. Its pole locations, energy derivatives and vertex structure must be computed together. Different gap and phase models can have the same three eigenmasses but different residues or transition amplitudes; the masses alone do not identify which mechanism produced them.

For physical charged leptons, the finite Hermitian block calculation is not yet sufficient. A gauge-consistent chiral interaction must specify kinetic matrices `Z_L,Z_R` and a Yukawa matrix `Y` with its matching correction. After symmetry breaking, the physical Dirac masses are singular values of `Z_L^(-1/2) M_LR Z_R^(-1/2)`, with `M_LR` proportional to the Higgs expectation value times `Y`; the particular quadratic mass law used here is an added ansatz. A positive comparison on a bookkeeping space is not automatically either chiral kinetic matrix.

The present ranking is therefore:

1. Within this source architecture, test the triadic coupling and its complementary propagator first. A small coherent relative-phase correction is economical for the shape, while mode-dependent gaps offer a separate viable response mechanism.
2. Determine whether the proposed frame/gravitational mechanism really supplies coherent mixed blocks. Without those blocks, the independent-shift explanation vanishes in the phase test.
3. Keep the absolute mass scale separate. Neither the small phase correction nor the moderate inverse-gap weights generates the missing scale in the old electroweak/Planck, zero-direct-block model.

## Reproduction and Scope

Run `python -B analysis/Coupling_Scale_Candidate.py --output analysis/Coupling_Scale_Candidate.json`. The `physical_origin_diagnosis` record separates source candidates, norm bounds, inverse-gap response, phase interference and QED matching assumptions. No measured value is used in the construction of the original `B`; fitted diagnostics are marked separately.

Twenty tests in `scripts/qsc_audit/tests/test_coupling_physical_origin.py` verify the Schur response and derivative sign, reconstructed-state norm, exact eigenproblem, decoupling and remainder bounds, input guards, minimal-penalty block selection, inverse-gap identity, phase sensitivity/invariants, connected versus disconnected channels, simultaneous mediator-block corrections, QED sign pattern, universal rescaling and report reproduction. These finite checks do not establish a native interaction or a physical observation. The main TeX source and its measured 1,031-page build are unchanged by this diagnostic.
