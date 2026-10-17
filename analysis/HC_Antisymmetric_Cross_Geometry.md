# Exchange-Odd Cross Geometry and Its Conserved Parent Current

Date: 2026-10-17. Status: an additional constitutive candidate built from existing cross-readout ingredients; a curved diagnostic of an exact reference probe; and independently checked parent-action variation. Not an adopted native coframe, a new native probe equation, or a common induced/gauge/Einstein solution. Main TeX/PDF unchanged.

This follows the [probe-law revision audit](HC_Probe_Law_Revision_Audit.md). Its HC-free, compatible **full real self-bilinear** forced a homothetic current of divergence eight, whereas the closed real action required zero. The present candidate changes that observable rather than inserting a compensating imaginary mass or omitting a conservation equation.

## 1. Existing Ingredients, Additional Choice

Chapter 12, `sources/research/parts/v470/12_structural_core.tex`, explicitly supplies the cross-bilinear `Re(bar Psi_ART Gamma^a D_mu Psi_QFT)` **and the expression with the probes exchanged**. It also discusses relative phase lag and an earlier focusing readout before compression into a metric; its focusing functional is heuristic. It does not select the following exchange-odd combination as the physical coframe.

For a common specified carrier, ordinary adjoint and compatible reference transport, write

\[
 B_{12}^a{}_{\mu}=\bar\Psi_1\Gamma^aD_\mu\Psi_2,\quad
 B_{21}^a{}_{\mu}=\bar\Psi_2\Gamma^aD_\mu\Psi_1,
\]
\[
 C_\pm^a{}_{\mu}=\frac12\operatorname{Re}(B_{12}^a{}_{\mu}\pm B_{21}^a{}_{\mu}).
                                                               \tag{1}
\]

For constant internal selectors and unitary internal transport commuting with them, or covariantly transported selectors, the even combination has the familiar identity

\[
 C_+^a{}_{\mu}=\frac12(D^\omega_\mu\operatorname{Re}
                       (\bar\Psi_1\Gamma^a\Psi_2)).
\]

The relevant derivative includes the selector reaction if it is not covariantly constant. In the flat reference with constant selectors this is an exact gradient, so an invertible even coframe is locally flat. This cross current is not automatically the total Dirac phase current; their conservation laws must not be identified.

The odd combination is generally **not** that gradient. On three internal probe channels define

\[
 R_-=(|1\rangle\langle2|-|2\rangle\langle1|)/2,\quad
 Q=iR_-=Q^\dagger.
\]

Then `C_minus=Re(Psi^dagger R_minus K^a D_mu Psi)=Im(Psi^dagger Q K^a D_mu Psi)`. Its eigenvalues in channel space are `(-1/2,0,1/2)`. Channel labels are not generations, colors or an evaluated matter/tachyon assignment.

Using (1) as `E=C_minus`, with `g=E^T eta E`, is an **additional physical dictionary**. It is not algebraically equivalent to chapter 10's full self-bilinear reconstruction. Its normalization and physical units remain uncalibrated.

## 2. What the Already Solved Probe Branches Give

On the [fully sourced stationary spectral branch](HC_Spectral_Gauge_Completion.md), evaluate both cross readouts with its actual internal and spin connections. At the previous reference point the odd singular values are approximately

\[
 (.0073554364,\;1.5756289\cdot10^{-6},\;0,\;0).
\]

The angular columns vanish. The new combination gives rank two there, not a full four-dimensional geometry. Thus merely changing the observable does not complete that same polarized branch.

A separate positive control uses the **already prepared exact affine-spatial massive reference-Dirac solution** from [background provenance](HC_Background_Coframe_Origin.md), retaining its real three-channel matrix with diagonal `.6` and mediator links `4,.7`. This is a neutral fixed-reference comparison; no charged Gauss, metric or closure-field variation is present in that solution. No new free point jets are fitted here.

At `(t,x,y,z)=(.1,.02,-.03,.01)`, the odd coframe has singular values

\[
 (.228882875,\;.008833526,\;.008816261,\;.008799532).
\]

Its determinant is `-1.5685248e-7`, and its metric has one negative and three positive eigenvalues. It reverses coframe orientation relative to this reference; a native orientation/spin convention has not been assigned. Analytic derivatives through third order of the same reference solution give a nonzero Riemann tensor and curvature scalar about `721993.9814` in the arbitrary dimensionless normalization. This is not a physically calibrated curvature prediction. Independent finite differences check the analytic jets and curvature.

The reference Dirac residual is `1.35e-15`. Replacing the reference gammas and spin transport by the candidate metric's own ones gives residual norm about `525.837` and changes the odd coframe by norm `.00196618`. The construction is therefore a **curved observable of an on-shell reference probe**, not a self-consistent induced-frame field solution. Those component norms are diagnostics, not invariant physical error magnitudes.

## 3. The Odd Readout Is Not Locally Phase-Blind

At fixed connection, let every probe acquire the same local phase alpha. Then

\[
 D_\mu\Psi\longmapsto e^{i\alpha}(D_\mu\Psi+i\partial_\mu\alpha\,\Psi),
\]
\[
 C_-^a{}_{\mu}\longmapsto C_-^a{}_{\mu}
                +q^a\partial_\mu\alpha,\qquad
 q^a=\Psi^\dagger QK^a\Psi=-\operatorname{Im}(\bar\Psi_1\Gamma^a\Psi_2).
                                                               \tag{2}
\]

The even readout is phase-blind in this test. Equation (2) is not failure of gauge covariance: a simultaneous common gauge-connection transformation cancels the added derivative. Under general internal transformations the selector must also transform covariantly, or its fixed invariance contract restricts the group. The [earlier fixed/covariant readout audit](HC_Gauge_Invariant_Geometry_Readouts.md) still applies. Merely squaring a fixed bare cross coframe does not ensure a gauge-invariant metric.

## 4. Derive the Current From One Parent Action

Declare independent E, probes, a real multiplier **density** `lambda_a^mu`, the chosen connection/readout data and a real geometric action. A possible parent is

\[
 S=S_D[E,\Psi]+S_{\rm geom}[E]+\int d^4x\,
       \lambda_a{}^\mu(E^a{}_{\mu}-C_-^a{}_{\mu}[E,\Psi,D]).
                                                               \tag{3}
\]

This is a new specified variational comparison, not the inherited action. Which connection is independent, reference or induced must be declared and varied consistently. The following probe/phase variation holds with E and the other independent fields fixed; their own Euler equations remain necessary.

The real Dirac term varies under local rephasing as `-integral v J_D^mu partial_mu alpha`. By (2), the constraint term adds `-integral lambda_a^mu q^a partial_mu alpha`. Hence the full on-shell phase identity is

\[
 \partial_\mu\left(vJ_D^\mu+\lambda_a{}^\mu q^a\right)=0,
 \qquad v=\sqrt{|g|}.                                    \tag{4}
\]

The extra current is a variational consequence, not a subtraction of eight by hand. There is no reason to impose the unchanged probe equation and its separate conserved current **as well as** this altered parent equation. Conversely, (4) alone does not determine lambda or prove that the old divergence is canceled on a solution.

Because Q and the spin weights commute, the constraint changes the Hermitian kinetic **density weights** to

\[
 \mathbb K^\mu=vK^\mu_{\rm coordinate}
                     +\lambda_a{}^\mu(Q\otimes K^a_{\rm frame}).
                                                               \tag{5}
\]

With the mass weight `v W`, their probe equation follows from the general variable-weight real-action formula in the preceding audit. Derivatives of lambda, frame and selector, and the connection's adjoint contribution must be retained. This is a kinetic change, not simply a shifted mass or an unchanged geodesic equation.

The script independently varies the direct real Dirac-plus-constraint density on a periodic off-shell test and compares with (5)'s Euler derivative. The density actions agree to `3e-14`, the probe variation to about `2.4e-9`, and the off-shell phase Ward identity to `1e-14`. The test also retains a connection not commuting with Q. It is a probe-variation check, not a solution of the coframe, multiplier, gauge and geometry equations. A covariant externally prescribed selector has its own reaction in the gauge Ward identity; adopting an actual dynamical selector requires its equation too.

## 5. A Nonempty Positive Temporal Domain

In the declared flat reference with `K^0=I`, use (5) at a point. Let `ell_0=lambda_0^0` and `ell_vec=(lambda_1^0,lambda_2^0,lambda_3^0)`. The alpha matrices give eigenvalues `ell_0 +/- |ell_vec|`; Q contributes `0,+/-1/2`. Therefore

\[
 \lambda_{\min}(\mathbb K^0)
 =v-\tfrac12(|\ell_0|+|\boldsymbol\ell|).
\]

Strict positivity holds precisely when

\[
 |\ell_0|+|\boldsymbol\ell|<2v.                          \tag{6}
\]

The independently varied parent test lies within that region; its smallest temporal eigenvalue is about `.85463`. Thus the required kinetic modification need not immediately make this temporal form indefinite. Equation (6) is not a derived multiplier solution, a generic curved-frame bound, or a well-posedness/stability theorem for the full constrained system. At the boundary the temporal form degenerates.

## 6. The Quadrature Limit Has a Cosmological-Term Trap

If one imposes `Psi_2=exp(i delta) Psi_1` with **constant** delta and the same derivative, direct substitution gives

\[
 C_-=-\sin\delta\,\operatorname{Im}(\bar\Psi_1\Gamma^aD_\mu\Psi_1),
 \qquad C_+=\cos\delta\,\operatorname{Re}(\bar\Psi_1\Gamma^aD_\mu\Psi_1).
\]

In particular `delta=pi/2` makes the odd readout a kinetic self-bilinear. This is an algebraic control, not the paper's computed phase shift. The given real triadic mixing does not generally preserve that quadrature relation: with the third channel initially empty it already breaks at second time order through that mediator.

There is a further restriction if one replaces the full dictionary by `E=-s Im(bar Psi Gamma^a D Psi)` and uses its inverse in the same kinetic contraction. Then

\[
 -\operatorname{Im}(\bar\Psi\Gamma^\mu D_\mu\Psi)=4/s.
\]

Thus the kinetic action on that composite dictionary has a volume-term form, not an unconstrained generic matter kinetic density. In the standard independent-metric symmetric Dirac stress formula, using the **same** derivative in both places gives `T_mu,nu=(L_D-1/s)g_mu,nu`. If the unchanged real Dirac equation also holds, `L_D=0` and `T_ab=-eta_ab/s`: a vacuum-type equation of state, not generic matter. This conditional algebra is checked off shell; it is not a solved induced field system, a physical vacuum-energy calculation or a permission to set a native mass to a fitted value.

A closely related methodological warning exists in the primary literature. [Diakonov, *Towards lattice-regularized Quantum Gravity*, section IV, eq. (11), and section V, eq. (12)](https://arxiv.org/pdf/1109.0091) defines a derivative-antisymmetrized composite tetrad and shows that the corresponding same-fermion Dirac action becomes four times a volume term. His construction uses Euclidean anticommuting fields and an independent spin connection; it is **not** identical to this Lorentzian commuting-probe comparison or a validation of the Sphaera model. It does reinforce why the action must change consistently with a new composite tetrad.

## Outcome and Remaining Work

The exchange-odd cross candidate has a concrete advantage over the full real self-bilinear: it can carry non-holonomic, curved reference readout data, and its common parent supplies a new phase-current contribution with a nonempty positive temporal domain. Its ingredients occur in the paper, but their selection and normalization as a metric law remain new assumptions.

No common induced-frame or gravitational solution has yet been found. The sourced stationary branch remains rank two; the positive curved reference example fails when its own spin connection is substituted. The next task is to solve the parent coframe/multiplier/probe/gauge equations together, retaining the readout's transformation/reaction and all normal equations. A special quadrature identification must not silently collapse the proposed matter readout into the kinetic/volume case above.

## Reproduction

Follow-through: the [independent Cartan/coframe parent analysis](HC_Cross_Cartan_Parent.md) now derives all four Euler equations and the distinct LC chain reaction. Its 40 checks find an exact rank-nine connection/constraint compatibility criterion, violated by this unchanged curved reference jet even after allowing torsion or changing the Einstein coefficient. This does not exclude a different branch or the correctly varied LC-restricted action; neither has been solved.

- [Calculation](HC_Antisymmetric_Cross_Geometry.py) and [saved results](HC_Antisymmetric_Cross_Geometry.json).
- Run `python -B analysis/HC_Antisymmetric_Cross_Geometry.py --output analysis/HC_Antisymmetric_Cross_Geometry.json`.
- Run `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_antisymmetric_cross_geometry.py`.

Thirty-eight focused checks cover exchange/phase/gauge identities, analytic probe/coframe jets and independent curvature differences, reference versus induced equations, kinetic/current parent variation, the exact temporal positivity domain, quadrature non-preservation and the kinetic-volume/stress trap. No package installation, main-TeX change, PDF rebuild, publication or Git operation is introduced. These tests check the stated identities and conditional comparisons, not empirical gravity, native closure or proof-assistant certification.
