# Are the Probe Equations Outdated? A Source and Variational Audit

Date: 2026-10-17. Status: active-source comparison, an explicitly derived real-action equation with variable kinetic weights, and a curved same-coframe construction kept off shell. No native equation is replaced. Main TeX/PDF unchanged.

This continues the [sourced Cauchy/coframe calculation](HC_Sourced_Cauchy_Coframe.md). That calculation solves a declared flat-reference Maxwell--Dirac comparison locally, but its full-rank real coframe is holonomic. Here the reference spin connection is no longer frozen: an explicit curved construction uses the Levi--Civita connection of the same reconstructed coframe. Its failure is then tested against the actual probe law and a more general phase-current identity.

## 1. Which Source Equation Is Still Active?

The active `sources/research/v480-companion.tex` includes both the newer HC qualifications and the inherited field chapters. The saved audit records file hashes and source-anchor lines for these blocks; this is a provenance check, not a machine proof of their mathematical claims.

| Source block | What it currently says | Consequence for this calculation |
| --- | --- | --- |
| Chapter 10, `thm:dirac-probe` and `prop:dirac-limit` | Free effective Dirac law after the stated reductions | A limit, not the full coupled transport law |
| Chapter 10, `thm:master-field-equation` and `prop:triadic-two-probe` | `(i Gamma^mu D_mu-Omega)Psi=0`, with connection, HC, closure and triadic terms | This ordered equation has not been withdrawn |
| Chapter 12, `thm:hc-spectral-projector` and `rem:hc-shadow-vs-core` | The structural compensator C is identified with a spectral projector, distinguished from its visible defect | A represented local C/adjoint/readout map is still needed to infer a physical transport coefficient |
| Chapter 13, `thm:theorem-level-shadow-fluid-type-readout` | The same ordered probe/resonance system remains the kernel; fluid laws would be coarse-grained readouts | Fluid language is not a later replacement equation |
| Chapter 13, `hyp:frame-dependent-defect-readout` | A deeper HC generator could survive a vanishing visible defect | Minimal visible `H=0` is not a theorem of extinction of all deeper HC structure; the generator/readout map remains uncomputed |
| Chapter 16, `thm:minimal-mmhc-field-equation` | Again the same first-order operator structure | The displayed `beta T` versus chapter 10's `beta g_Y T` can be a coefficient convention if the operator/carrier is the same; no new differential term is supplied |
| New HC section, `v480:hc-dynamics-geometry` | Real-action alternatives and the conditional same-frame obstruction are explicitly distinguished from the ordered law | The original variational claim cannot be used without fixing action, adjoint and allowed variations |

**Answer to the version question:** no evaluated superseding native probe equation was found in these relevant active blocks. Their legacy status does not mean that a new curved or coarse-grained equation has already replaced them. The latest flat-reference calculation is a deliberately reduced comparison, not a computation of every native term. Its limitations were scope restrictions, not evidence of having accidentally read an obsolete free-Dirac equation.

There is nevertheless a real modernization obligation: a curved effective calculation must derive its probe variation with its measure, weights, spin connection and composite-field reactions. It must not reuse a fixed-background equation without checking those terms. The original chapter 10 action has no explicit curved-volume/spinor-variation completion that settles this identification.

## 2. Derive the Fixed-Background Real Probe Equation

Let `psi` be a commuting complex finite vector. Set `K^mu=(K^mu)^dagger`, `W=W^dagger`, real positive volume density `v`, and `D_mu=partial_mu+B_mu`. All background quantities are initially held fixed during the probe variation. The real symmetric action is

\[
 S_D=\int d^4x\,v\left[
 \frac i2\{\psi^\dagger K^\mu D_\mu\psi
                 -(D_\mu\psi)^\dagger K^\mu\psi\}
 -\psi^\dagger W\psi\right].                            \tag{1}
\]

Independent variation of `psi^dagger` and integration by parts give

\[
 R_{\rm sym}=iK^\mu\partial_\mu\psi
 +\frac{i}{2v}\partial_\mu(vK^\mu)\psi
 +\frac i2(K^\mu B_\mu-B_\mu^\dagger K^\mu)\psi-W\psi=0.
                                                               \tag{2}
\]

Equivalently define the Hermitian compatibility defect

\[
 Z=v^{-1}\partial_\mu(vK^\mu)
      -B_\mu^\dagger K^\mu-K^\mu B_\mu,
\]
\[
 R_{\rm sym}=R_{\rm ord}+\frac i2Z\psi,\qquad
 R_{\rm ord}=iK^\mu D_\mu\psi-W\psi.                    \tag{3}
\]

Here `W=eta_D Omega` when that mass weight is Hermitian. This is the adjoint-weighted equation; multiplication by the invertible adjoint returns the corresponding Gamma form. A non-Hermitian W would itself need a different reality prescription. The formula does not assume that B commutes with K.

The density/weight derivative and the connection's adjoint contribution are equally necessary. With the correctly matched torsion-free spin connection, curved coordinate weights and `v=sqrt|g|`, geometric compatibility gives **Z=0**. Adding the density derivative on top of an already compatible ordered Dirac operator would double-count part of the spin transport; it is not a missing free parameter.

For fixed flat Hermitian weights and internal `B=iA+kappa H n`, factorized internal Hermitian H gives instead `Z=-2 kappa K^mu n_mu H`. Equation (3) then cancels the real action's ordered HC transport, as the current main section already states. For noncommuting H, the remaining Hermitian interaction is `i kappa[K^mu n_mu,H]/2`, not the old ordered product. This genuinely changes the equation and must be declared.

The source/action distinction also appears in the primary literature: [Adak, Bagci, Pala and Sert, *The Generalized Dirac Equation in the Metric Affine Spacetime*, section 3](https://arxiv.org/html/2506.23609v1#S3) compare direct covariantization and variation of a real spinor action. Their extra metric-affine couplings are **not** adopted here. Equations (1)--(3) above follow by the displayed direct variation and are tested independently by a periodic action variation.

## 3. A Field-Density Rewrite Does Not Fix the Obstruction

For fixed background volume put `q=sqrt(v) psi`. The flat-density variable has

\[
 B'_\mu=B_\mu-\tfrac12\partial_\mu\log v\,I,
 \qquad D'_\mu q=\sqrt v\,D_\mu\psi.                     \tag{4}
\]

The physical full coframe must then be transported as

\[
 E^a{}_{\mu}=v^{-1}\operatorname{Re}(q^\dagger K^aD'_\mu q).
\]

Keeping q but leaving the old connection and old coframe dictionary unchanged adds a real current-gradient term. That is a change of reconstruction, not merely a newer notation for the same probe. The explicit example below verifies that (4) preserves both the probe residual and the coframe, including the original nonzero trace diagnostic. This fixed-background invertible redefinition is not an off-shell elimination of a probe-dependent composite volume.

## 4. A Curved Coframe With Its Own Spin Connection

Take dimensionless `tau>0`, coordinates `(tau,x,y,z)`, and

\[
 E^a{}_{\mu}=\operatorname{diag}(1,\tau,\tau,\tau),\qquad
 ds^2=-d\tau^2+\tau^2(dx^2+dy^2+dz^2).                  \tag{5}
\]

In the previous spin representation `K^a=(I,alpha_i)`, beta=diag(1,1,-1,-1), use the ordinary-adjoint probe and its **same induced** torsion-free spin connection:

\[
 \psi=\sqrt{2\tau}\,(1,0,0,0)^T,\quad
 S_\tau=0,\quad S_i=\alpha_i/2,\quad
 \Gamma^\tau=\beta,\quad\Gamma^i=\beta\alpha_i/\tau.
\]

There is no HC, internal gauge potential or affine background term in this coframe. Direct contraction gives

\[
 \operatorname{Re}(\psi^\dagger K^a D_\mu\psi)
 =\operatorname{diag}(1,\tau,\tau,\tau)=E^a{}_{\mu}.      \tag{6}
\]

In particular the spatial columns come from geometric spin transport, not from manually assigned spatial probe derivatives. The full current is `j^a=(2 tau,0,0,0)`. The metric has

\[
 R_{\tau\tau}=0,\quad R_{ij}=2\delta_{ij},\quad R=6/\tau^2\ne0.
\]

This escapes the preceding **flat-reference** gradient identity without changing the real bilinear coframe functional. It is a kinematically consistent curved coframe/probe/spin triple, not a solution of the probe equation or a sourced gauge/Einstein system. A one-channel restriction suffices to test the geometric obstruction; no native generation, C7 carrier or triadic mass identification is inferred.

At `tau=1.2`, `m=0.6`, the calculation gives curvature scalar `4.1666666667`, coframe reconstruction error below `4e-16`, and Z norm zero. The same compatible real/ordered probe residual is nevertheless

\[
 R_\Gamma=(2i/\tau-m)\psi,\qquad
 \operatorname{Im}(\bar\psi R_\Gamma)=4.
\]

The half-density rewrite has `q=sqrt(2) tau^2(1,0,0,0)^T` and `B'_tau=-3/(2 tau) I`. It leaves the normalized imaginary contraction equal to four. Naively keeping the old connection changes the volume-normalized coframe's time component from one to four. This is a concrete false-repair control.

The compatible Dirac equation on this prescribed cone is not itself insoluble or obsolete. The homogeneous spinor `psi_D=tau^(-3/2) exp(-i m tau)(1,0,0,0)^T` solves it and has conserved current. Its real bilinear coframe is instead `tau^(-3) diag(-3/(2 tau),1/2,1/2,1/2)`, not (5). At the reference point its probe residual is below `6e-17` but its coframe-definition error is `2.33621`. Solving the background probe equation and satisfying the same reconstructed geometry are separate requirements.

## 5. A Stronger Geometric Test Before Choosing a New Probe Law

Assume the same fixed Clifford frame, ordinary Hermitian frame weights, a compatible Lorentz spin connection of E, and purely internal unitary transport. Suppress HC and the closure load on the closed probe. Lorentz compatibility gives the covariant bilinear identity

\[
 E^a{}_{\mu}=\tfrac12(D^\omega_\mu j)^a
 =\tfrac12(\partial_\mu j^a+\omega_\mu{}^a{}_b j^b).
\]

Set `J^nu=(E^-1)^nu_a j^a`. The tetrad postulate then implies, purely from the coframe definition,

\[
 \nabla_\mu J^\nu=2\delta_\mu^\nu,\qquad
 \nabla_\mu J^\mu=8.                                   \tag{7}
\]

This does not yet use a Dirac equation. Differentiating once more with torsion zero gives

\[
 R^\rho{}_{\sigma\mu\nu}J^\sigma=0.
\]

It does not require the entire Riemann tensor to vanish. The cone (5) has nonzero spatial curvature and obeys this annihilation condition. On a timelike-current patch, (7) also makes J a gradient homothetic vector: `J_mu=partial_mu(j_a j^a)/4`. With `tau=sqrt(-j_a j^a)/2`, its local metric has cone form `-d tau^2+tau^2 h_ij(x)dx^i dx^j`. Thus the compatible same-coframe dictionary is a strong geometric restriction, not a parametrization of generic curved metrics. These are local statements, not a cosmological identification.

On the other hand, (1)--(3) with Hermitian W obey the off-shell identity

\[
 v^{-1}\partial_\mu(vj^\mu)=2\operatorname{Im}(\psi^\dagger R_{\rm sym}),
 \qquad j^\mu=\psi^\dagger K^\mu\psi.                    \tag{8}
\]

Hence an on-shell closed real probe has divergence zero, not eight. The cone's computed divergence is exactly eight. A finite real normalization `s` multiplying the coframe changes this to `8/s`, not zero. The values refer to dimensionless comparison normalization, not physical particle-creation rates.

## 6. Does Composite-Action Backreaction Remove This Conflict?

A changed equation must be derived from the whole action, including measure, inverse coframe and spin-connection dependencies. The earlier [parent-action bridge](HC_Two_Frame_Action_Bridge.md) already gives the differential chain-rule reactions. Merely adding (3) is not that full composite variation.

There is a useful conclusion even before evaluating all those higher-derivative terms. At fixed E and connection, a local phase changes `D_mu psi` by `i(partial_mu alpha)psi`. Since j^a is real, its extra contribution to **Re**`(bar psi Gamma^a D_mu psi)` vanishes. The coframe constraint is therefore locally phase-blind, not merely invariant under a constant phase.

Consider a parent with independent `E,psi` and real multiplier density `lambda_a^mu(E^a_mu-C^a_mu[E,psi])`, the real Dirac action (1), and bosonic terms depending on E or other locally phase-blind quantities. Under a local probe rephasing, the constraint and these bosonic terms contribute no phase-gradient term. The Dirac action alone varies as `-integral v J^mu partial_mu alpha`. Thus the full probe Euler equation still requires the same conservation law (8). An allowed implicit elimination of the auxiliary fields preserves that identity; it does not generate a new central phase current.

At fixed E the explicit multiplier probe weight is already instructive:

\[
 V_\lambda=\frac12\left(\partial_\mu\lambda_b{}^\mu
              -\lambda_a{}^\mu\omega_\mu{}^a{}_b\right)K^b.
\]

All coefficients are real, so `V_lambda` is Hermitian and `Im(psi^dagger V_lambda psi)=0`. The reaction cannot cancel four by being relabeled an imaginary mass. The calculation checks the full local-phase constraint invariance and this Hermitian reaction.

**Conditional conclusion:** even an updated composite probe equation cannot make this HC-free, compatible, same-real-coframe branch stationary if its only phase current is the standard Dirac current. This extends the previous ordered-equation test to the stated class of real composite actions. It is not a no-go theorem for all native adjoints, nonunitary HC transport, nonlocal readouts, phase-sensitive collective couplings, torsion/nonmetricity, or operator/quantum coarse-graining.

## 7. Can the Surviving Deeper Projector Supply the Missing Term?

Chapter 12 identifies a structural spectral projector C; chapter 13 explicitly leaves the generating equation and its frame readout deferred. These symbols are not automatically the field `H_C(x)`, the closure projector `P_C7`, or a nonunitary connection coefficient. In particular the source does not yet identify C with a smooth **orthogonal** projector in the ordinary positive adjoint used by the finite comparisons.

Test one natural additional realization: a smooth internal orthogonal projector `P=V V^dagger`, `V^dagger V=I`, and unitary ambient transport `B_mu^dagger=-B_mu`. Its compressed connection is

\[
 b_\mu=V^\dagger\partial_\mu V+V^\dagger B_\mu V,
 \qquad b_\mu+b_\mu^\dagger=0.                           \tag{9}
\]

The identity follows by differentiating `V^dagger V=I`. If V acts internally and commutes with the spin weights, the full real coframe of `Psi=V chi` becomes the coframe of chi with b included. But the anti-Hermitian internal b contributes zero to its real contraction. A Berry-type connection can have nonzero internal curvature without supplying a real HC transport load or an extra traced phase current.

This is tested using the **already prepared** isometric texture and compatible connection `B=[P,dP]` from the [hard-closure analysis](HC_Hard_Closure_Transport.md). Lift the same curved-cone spinor through its two-dimensional internal line bundle. For a finite comparison take `M=m P+(m+0.6)(I-P)`. Then P is a spectral projector of this comparison M, `D P=0`, `[M,P]=0`, and the minimal positive visible defect vanishes while P remains nonzero. This is not the native M16 or its C7 representation.

The calculation gives projector norm one, visible-defect norm below `3e-32`, reduced internal-curvature norm `.1697056275`, and an unchanged full real coframe within `2e-16`. The full/reduced probe residual lift agrees within `4e-16`, and its imaginary contraction is still four. A second compatible connection with the same P can even remove that internal curvature; the projector alone does not select the connection.

Thus the most direct orthogonal/unitary realization of a surviving core does **not** repair this branch. Nonisometric comparisons, spin/internal mixing, nonunitary transport or nonlocal elimination can change the hypotheses, but require an actual represented readout and its currents. No native gauged source equation has been solved by this projector test. The deferred meta-field generating equation cannot be inferred from the existence of its spectral symbol.

## Outcome and Next Native Obligation

The probe equations are not simply obsolete: the relevant later source still retains them. Their migration to a curved/composite description is incomplete, and its assumptions must be made explicit. Correct spin transport can produce curved, full-rank coframes, but updating density terms or restoring locally phase-blind geometric reactions cannot by itself cure (7)--(8).

The next defensible step is to choose and derive a genuinely different microscopic-to-effective identification, rather than fitting a compensating constant. Possibilities to investigate include the actual deeper-HC/readout map of chapter 13, a different effective coframe observable, or a reference/effective split with its full action and extra data. None is supplied by the existing symbols alone. In particular, a surviving deeper HC kernel does not automatically become a nonzero connection term when its specified visible readout is zero.

## Reproduction

The subsequent [exchange-odd cross-geometry analysis](HC_Antisymmetric_Cross_Geometry.md) tests an explicitly different observable formed from both existing cross-readout directions. It gives a curved rank-four diagnostic of an exact reference probe, remains rank two on the sourced stationary branch, and derives the changed parent phase current and a positive temporal kinetic domain. Replacing the reference connection by the candidate's own spin connection still fails; the full joint field problem is not solved and the native coframe is not replaced.

- [Calculation](HC_Probe_Law_Revision_Audit.py) and [saved audit/results](HC_Probe_Law_Revision_Audit.json).
- Run `python -B analysis/HC_Probe_Law_Revision_Audit.py --output analysis/HC_Probe_Law_Revision_Audit.json`.
- Run `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_probe_law_revision_audit.py`.

Fifty-one focused checks cover the source-version/HC-role distinction, general real action and Ward identity, noncommuting HC terms, independently varied periodic action, curved same-coframe geometry, half-density transport, conserved-background negative control, locally phase-blind multiplier reactions and the surviving spectral-projector comparison. These are finite numerical/action regressions and source provenance guards, not proof-assistant certification or physical validation. No package installation, main-TeX correction, compiler invocation or release activation is part of this analysis.
