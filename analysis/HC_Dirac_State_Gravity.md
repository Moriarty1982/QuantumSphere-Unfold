# Common-Metric Massive Dirac Sources and First-Order Backreaction

Date: 2026-10-16. Status: common tetrad/spin/stress dictionary, an explicit massive-source obstruction to the old pure-null branch, and a local first-order Einstein--Dirac solution of a declared finite triadic comparison. No scalar matter is added. The native composite coframe, HC matrix and closure/gauge/projector package are not solved or silently replaced in the paper. The main TeX remains unchanged.

## Result and the Model Change

The [previous state-source analysis](HC_Quantum_State_Gravity.md) used a distinct scalar carrier and left the positive homogeneous part of its massive source unsolved. This continuation uses **the already prepared three-channel Dirac carrier and its Hermitian internal coupling matrix** instead. It includes both the diagonal positive stress and the phase-sensitive interference, and computes the gravitational reaction on the spinor.

The comparison now gives the metric its own independent Einstein equation and couples the real Dirac action to that same metric. This changes the previous fixed-reference probe action. In particular, it does **not** impose the native bilinear reconstruction as an additional coframe constraint. That constraint is tested separately and fails for the selected zeroth-order modes. Thus this is a constructive common-action comparison, not a native solution disguised as a metric redefinition.

There are three definite results:

1. The unchanged polynomial reference probe is not on shell after installing the spin connection and gamma matrices of its effective curved metric. Merely changing the dictionary is insufficient.
2. A nonzero on-shell mass bilinear requires a nonzero stress trace. The previous pure-null curvature, with zero scalar curvature and otherwise traceless sources, cannot support it.
3. A general weak metric and an explicitly computed spinor correction solve the declared local Einstein--Dirac equations through **first gravitational order**, without adding a scalar. Full nonlinear residuals fall quadratically with the coupling, not identically to zero.

## 1. One Tetrad, One Spin Connection and One Real Action

Keep the previous constant spin matrices `beta=diag(1,1,-1,-1)`, `K^a=(I,alpha_i)`, `Gamma^a=beta K^a`, with

```text
eta=diag(-1,1,1,1),     {Gamma^a,Gamma^b}=-2 eta^{ab} I,
barPsi=Psi^dagger beta.
```

For a real invertible coframe `E^a_mu`, define `g=E^T eta E`, `Gamma^mu=(E^{-1})^mu_a Gamma^a`. Take the connection to be torsion-free and determined by this metric, not an independently varied Einstein--Cartan field. The tetrad postulate and its spin lift are

```text
omega_mu=eta [E GammaChristoffel_mu-partial_mu E] E^{-1},
omega_mu,ab=-omega_mu,ba,
S_mu=-omega_mu,ab Gamma^a Gamma^b/4,
D_mu Psi=partial_mu Psi+S_mu Psi,
D_mu barPsi=partial_mu barPsi-barPsi S_mu.                         (1)
```

The minus sign in the spin lift belongs to the stated **negative** Clifford convention. It is checked by `partial_mu Gamma^nu+GammaChristoffel^nu_mu_rho Gamma^rho+[S_mu,Gamma^nu]=0` and `S_mu^dagger beta+beta S_mu=0`. The coordinate gammas, volume and spin connection therefore use the same effective metric.

With a constant Hermitian internal matrix `M` commuting with the spin action, the declared comparison is

```text
S=integral sqrt|g(E)| [R(g)/(2 epsilon)+L_D],
L_D=i/2 [barPsi Gamma^mu D_mu Psi-(D_mu barPsi)Gamma^mu Psi]
    -barPsi M Psi.                                               (2)
```

All three Dirac channels and the tetrad are varied. There is no added scalar, dynamical internal gauge connection, HC field or native closure projector in (2). The internal triadic coupling is retained in `M`; this neutral/global-phase model does not solve a missing native Gauss equation. A covariant native theory could require further fields and stress contributions.

Variation gives the curved Dirac equation and its adjoint, plus `G=epsilon T`. The symmetric on-shell stress is

```text
T_mu_nu=-i/4 [barPsi Gamma_mu <->D_nu Psi
             +barPsi Gamma_nu <->D_mu Psi],
Tr_g T=-barPsi M Psi.                                           (3)
```

The off-shell extension used for the independent tetrad-variation check retains `+g_mu_nu L_D`. This term vanishes on shell. The sign in (3) gives positive `T_00=m Psi^dagger Psi` for a positive-mass rest mode with the stated metric/gamma conventions. Using a mostly-minus formula without transporting its lowered gamma would reverse that sign.

**Trace proof.** The Dirac and adjoint equations give `barPsi Gamma.D Psi=-i barPsi M Psi` and `(D barPsi).Gamma Psi=+i barPsi M Psi`. Contracting (3) proves its trace. The Einstein trace then requires `R=epsilon barPsi M Psi`. Hermiticity does not make this Lorentzian mass bilinear positive for every spinor; no such general claim is needed.

Consequently, on a pure-null metric with `R=0`, a nonzero mass bilinear is incompatible with Einstein's equation if all other included stresses are traceless and the cosmological term vanishes. An additional traceful sector, different geometry or vanishing bilinear changes this conclusion. It is not a no-go for all massive backgrounds.

## 2. Test of the Existing Polynomial Background

The previous exact triadic polynomial probe still solves its **reference** Dirac equation. Computing (1) from its selected cross-readout null coframe and retaining the unchanged probe gives, at `(0.01,0.02,-0.03,0.01)`,

```text
reference Dirac residual norm       = 1.38e-15
effective-metric Dirac residual norm= 4.88e2
reference stress trace             = -1.1936411754334137
mass bilinear                      = +1.1936411754334166.
```

The common-metric spin lift passes its compatibility check; both metric jets agree with the earlier independent pullback calculation. The large second number is a coordinate/component diagnostic in a near-degenerate chart, not an invariant physical discrepancy or a measured instability. It establishes that the unchanged field does not solve the newly specified equation. The nonzero mass bilinear would also violate the on-shell pure-null trace requirement if that unchanged field were supposed to be completed solely by the traceless neutral HC source.

This identifies why switching gammas is not itself a solution. The matter field and geometry must change together.

## 3. Massive Modes in the Same Prepared Triadic Carrier

Retain, without refitting,

```text
M=[[0.6,0,4],[0,0.6,0.7],[4,0.7,0.6]].                          (4)
```

Let `g0=sqrt(4^2+0.7^2)`, `mu=0.6+g0`, and choose its normalized eigenvector `v=(4/g0,0.7/g0,1)/sqrt(2)`. All three channels participate, including the prepared orthogonal mediator. The chosen eigenvalue is `mu=4.660788100849389`. This is a declared dimensionless eigenchannel of the existing comparison matrix, not a native predicted mass or an extracted C7 representation.

Choose spatial momenta `k_1=(1,0,0)`, `k_2=(0,1,0)`, the same positive energy `E0=sqrt(mu^2+1)=4.766859104380919`, and normalized positive-energy spinors

```text
H(k)=alpha.k+beta mu,
u(k)=[(I+H(k)/E0)e_1]/||(I+H(k)/E0)e_1||,
c=(sqrt(0.8),sqrt(0.2) exp(i delta)),
Psi0=v tensor sum_r c_r u(k_r) exp(i p_r.x)/sqrt(V),
p_r=(-E0,k_r),     V=(2 pi)^3.                                  (5)
```

This exactly solves the flat, coupled three-channel Dirac equation. It is a new local mode background, not the earlier polynomial solution. The volume fixes the flat-box mode normalization; the later gravitational metric is **not** assumed periodic.

There is also a legitimate quantum source interpretation at zeroth order. A one-particle fermionic superposition has `N_rs=<a_r^dagger a_s>=conj(c_r)c_s`; its field mean is zero, but its normal-ordered stress is nonzero. The CAR/Fock regression uses fermionic annihilators, not bosonic coherent states. The symmetric mode stress is

```text
T_rs,mu nu=[(p_r+p_s)_nu bar u_r Gamma_mu u_s
            +(p_r+p_s)_mu bar u_r Gamma_nu u_s]/4,
T0(x)=Tdiag+C exp(i Q.x)+C* exp(-i Q.x),
C=conj(c_1)c_2 T_12/V,     Q=p_2-p_1=(0,-1,1,0).                (6)
```

The notation `T0` denotes the **complete zeroth-order stress**, not only its diagonal part. The integrated flat-box energy is `E0`, independent of relative phase. Local stress changes with phase; common rephasing leaves it unchanged. These equal-energy modes have a stationary interference pattern, so time averaging alone does not remove it. Orthogonal internal mass eigenchannels have no such cross term in an identity kinetic comparison; the selected interference is between momentum modes of the same eigenchannel.

**Conservation proof.** Equal mass shells imply `Q.(p_1+p_2)=0`. The two spinor equations imply `bar u_1 (Gamma.Q)u_2=0`. Contracting (6) therefore gives `Q^mu C_mu_nu=0`; the constant diagonal term is conserved independently. The trace of the whole stress is exactly `-barPsi0 M Psi0`.

For these selected populations, the elementary overlap estimate gives a lower bound valid for every position/relative phase:

```text
barPsi0 M Psi0 >= mu/V [sum_r |c_r|^2 u_r^dagger beta u_r
                       -2 |c_1 c_2 u_1^dagger beta u_2|]
                  = 0.003506136125259117 > 0.                    (7)
```

Thus the need for nonzero scalar curvature in this family cannot be removed by tuning only the relative phase. This bound concerns (4)--(5), not arbitrary Dirac states or native coefficients.

## 4. A Metric for the Complete Source, Including Its Positive Ground Part

Write `g=eta+epsilon h1+O(epsilon^2)`. Here `h1_mu_nu` is a metric tensor perturbation, not the scalar HC amplitude used earlier. In Lorenz/harmonic gauge, `bar_h1=h1-eta Tr_eta(h1)/2` obeys

```text
Box bar_h1=-2 T0,     partial^mu bar_h1_mu_nu=0.                  (8)
```

The oscillatory part has `Box T_osc=-Q^2 T_osc`, `Q^2=2`, so `bar_h1,osc=2 T_osc/Q^2`. Unlike the earlier difference-only construction, retain the positive constant source `Tdiag` as well. Put `x2=x.eta.x`, `X_mu=eta_mu_nu x^nu`, `tau=Tr_eta Tdiag`. A local polynomial particular solution is

```text
bar_h1,diag,mu nu= -Tdiag,mu nu x2/4
                  +eta_mu_nu (x.Tdiag.x)/4
                  +tau X_mu X_nu/36
                  -5 tau eta_mu_nu x2/72.                       (9)
```

**Verification.** In four dimensions, `Box x2=8`, `Box(x.Tdiag.x)=2 tau`, and `Box(X_mu X_nu)=2 eta_mu_nu`. The last three terms of (9) cancel in its wave operator, leaving `-2 Tdiag`. Its divergence cancels in two groups: `-(Tdiag.x)_nu/2+(Tdiag.x)_nu/2=0`, and `5 tau X_nu/36-5 tau X_nu/36=0`. Thus the sum of (9) and the oscillatory solution solves every component of (8), including the nonzero trace.

This is a local nonperiodic particular solution. A positive constant source cannot be solved by a periodic static flat-box perturbation with its zero mode discarded. The polynomial grows outside the small local weak-field patch; no isolated object, asymptotically flat boundary condition or global gravitational state is supplied. Homogeneous gravitational radiation/gauge data can be added only with their own initial/boundary choice.

## 5. The Probe Reaction Is Computed, Not Frozen

For the symmetric tetrad choice `E=I+epsilon eta h1/2`, expand the same operator as `D_E=D0+epsilon D1[h1]+O(epsilon^2)`, where `D0=i Gamma.partial-M`. The explicitly derived variations are

```text
delta Gamma^mu=-eta^{mu rho} h1_rho a Gamma^a/2,
omega1_mu,ab=(partial_b h1_a mu-partial_a h1_mu b)/2,
S1_mu=-omega1_mu,ab Gamma^a Gamma^b/4,
D1[h1]Psi0=i delta Gamma^mu partial_mu Psi0+i Gamma^mu S1_mu Psi0.
```

Set `Psi=Psi0+epsilon Psi1+O(epsilon^2)`. The required equation is

```text
D0 Psi1=-D1[h1]Psi0.                                           (10)
```

The right side is nonzero. In particular, the new construction does not repeat the scalar-parent trick of obtaining a zero multiplier reaction while keeping fixed-reference matter outside the effective stress.

For (5)--(9), (10) has a closed, finite Fourier/polynomial representation: the spatial wavevectors are `k_1,k_2,2k_1-k_2,2k_2-k_1`, the homogeneous spatial polynomials have degree at most two, and the explicit time polynomial has degree at most two. The constant internal matrix is diagonalized only to reduce this example to its chosen eigenchannel; the resulting solution is lifted back to all three components using `v`.

After factoring out `exp(-i E0 t)`, each Fourier block obeys

```text
i dot z=A_k z+b_0+b_1 t+b_2 t^2,
A_k=alpha.k+beta mu-E0-i alpha.partial_polynomial.                (11)
```

Spatial differentiation lowers polynomial degree, so this space is closed. Augmenting `z` by the clock `(1,t,t^2)` converts (11) into a constant matrix ODE. The implementation uses the already installed `mpmath.expm` at 25-digit working precision, not a hand-written integrator or a fit. The chosen correction data are `Psi1(0,x)=0`. Independent finite differences check both spatial derivatives and time derivatives from separate matrix exponentials, and direct substitution verifies (10) away from the report point.

This gives a constructive local first-order common solution. The metric is sourced by the complete `T[Psi0]`; `T[Psi1]` first contributes to Einstein's equation at second gravitational order because the matter source is multiplied by `epsilon`. Both the spinor and adjoint equations are retained. A classical/amplitude comparison is not by itself a fully normalized interacting quantum state on the curved background.

## 6. Order Check in the Full Equations

The independent nonlinear check uses the actual real coframe `E=I+epsilon eta h1/2`, not just an artificially linearized curvature. Its metric includes the induced second-order term, and its Levi--Civita and spin connections are recomputed from the full coframe jets. The corrected spinor is inserted into the same curved Dirac equation and stress (including the off-shell volume term).

At `(t,x,y,z)=(0.08,0.2,-0.3,0.1)`, `delta=0.4`:

```text
||G^(1)[h1]-T[Psi0]||            = 2.31e-17
||D0 Psi1+D1[h1]Psi0||           = 4.86e-19
||Psi1||                         = 1.17e-4

epsilon       ||G-epsilon T||        ||D_E Psi||
0.04          6.3765e-7               5.1698e-9
0.02          1.5945e-7               1.2925e-9
0.01          3.9866e-8               3.2311e-10
```

Halving the coupling divides both nonlinear residuals by approximately four, as required for a first-order solution with second-order remainders. This is an order check, not an exact nonlinear solution or an error bound for physical observations. The curved current also satisfies the off-shell identity `nabla_mu j^mu=2 Im(barPsi D_E Psi)`; conservation is not imposed by discarding its residual.

## 7. The Native Boundary Has Not Disappeared

For these zeroth-order modes the original fixed-weight real bilinear coframe is `C^a_mu=Re(Psi0^dagger K^a partial_mu Psi0)=partial_mu j^a/2`. Their equal energy gives `C^a_0=0`, and the current depends only on `Q.x`; hence `rank C<=1` (rank one at the report point). It is not the invertible background tetrad `I` of this weak metric.

Smooth first-order corrections cannot turn this into the required zeroth-order equality `E=C`. The earlier same-frame trace identity also still excludes imposing that unchanged equality together with the same ordered Dirac equation and real mass bilinear. The present result therefore does not repair the native coframe by adding a spin connection. It deliberately tests an **independent-metric**, common-action comparison instead.

Further obligations remain:

- Derive the allowed native metric/readout map and explain how it differs from, or coarse-grains, the excluded same-field definition.
- Evaluate the actual C7/M16/HC/Yukawa and gauge/projector operators and reactions, rather than identifying the finite matrix (4) with them.
- Specify which probe modes are retained. The native conditional Einstein action already describes integrating internal modes out; adding those same modes again as explicit matter would double-count them without a matching prescription.
- Derive physical scales, a quantum state and its renormalized vacuum/stress, and control stress fluctuations. A one-particle mean-source example does not certify semiclassical gravity, and the bosonic coherent-shift argument must not be applied unchanged to fermions.
- Extend to higher orders or an exact nonlinear solution, with global boundary conditions, normalization, admissibility and stability checked separately.

## 8. Source and Reproduction

The subsequent [stress-to-metric pullback](HC_Stress_Metric_Pullback.md) makes the weak sourced metric a nonlocal probe functional once gauge, Green operator and gravitational data are specified. Eliminating the complete quadratic gravitational action gives the correct Dirac reaction; a matter-only substitution doubles it. A computed free-wave counterexample keeps the same zeroth-order source but changes physical curvature and the corresponding probe correction. The continuation also diagnoses naive retarded-action symmetrization and checks a causal doubled-history prescription. It does not identify this response with the native local bilinear coframe or derive the assumed Einstein kernel.

The native source anchors are `thm:master-field-equation`, `thm:variational-form`, and `prop:bilinear-einstein-reconstruction` in the retained `sources/research/parts/v470/10_sphaera_and_physics.tex`. Its Einstein statement assumes an effective action after coarse-graining; it does not determine the quantum stress or the numerical finite matrix used here. These are source definitions and conditional claims, not executable instructions or completed consistency certificates.

For the external common-metric framework, see [Miguel Alcubierre, *The Dirac equation in General Relativity and the 3+1 formalism*, Sections V and VII](https://arxiv.org/html/2503.03918v2#S7): tetrad/spin compatibility, the real symmetric action, stress and its mass trace. The signs and index order here are explicitly declared and checked, not copied between conventions. Equations (4)--(11) are the present worked finite comparison. No claim of discovering the standard Einstein--Dirac coupling is made.

`python -B analysis/HC_Dirac_State_Gravity.py --output analysis/HC_Dirac_State_Gravity.json` reproduces the report. Thirty-five focused tests check Clifford/adjoint conventions, triadic and positive-energy mode equations, fermionic Fock covariance, stress/trace and action variation, common spin compatibility, the old-background failure, complete-source metric jets, the homogeneous source and Lorenz condition, the closed forcing and matrix-exponential correction, nonlinear second-order remainders, current balance and the native coframe negative control.

The implementation uses the existing NumPy and mpmath installations; no SciPy or other package was installed. These are local algebraic proofs and finite numerical regressions, not empirical evidence, a proof-assistant certificate or a new main-paper theorem.
