# Probe Sources, Backreaction and Positive-Constrained HC Selection

Date: 2026-10-16. Status: a conditional source calculation, conservation obstruction and constructive fixed-radius positive-cone phase minimum, now tested against released shape/scale directions. Those tests find shape descent and a zero-scale endpoint unless additional native constraints or forces are supplied. This is not a native phase or mass prediction, a solution of OP5/C5, or a modification of the main TeX document.

## Result and Model Boundary

The previous [minimal-functional audit](Phase_Selection_Derivation.md) showed that the matching penalty is identically zero on the source condition `H_C=Lambda`. That conclusion remains unchanged. This follow-up takes two further steps:

1. It derives the generation-resolved probe source and shows why the written scalar currents do not specify its cycle coherence. In the simplest self-consistent, unitary cyclic reduction, that coherence is conserved, not generated automatically by the HC feedback.
2. It solves the previously excluded case in which the unconstrained compensator minimizer violates positivity. If `H_C` is instead an independent positive field, a symmetric source and the positivity boundary can select a strict interior phase. There is a proved interval of the source/penalty ratio with such a minimum.

The second result is a **different dynamical completion**: it replaces exact matching by a constrained variational condition. It cannot be imposed simultaneously with `H_C=Lambda` for the nonzero source in this example. It also retains the assumed generation embedding, cyclic radius and off-closure Millennium bridge. The ratio selecting the phase remains unevaluated native input.

The follow-through in sections 7--10 makes the stability boundary concrete. The same energy does not select the assumed Koide radius: a trace-preserving cyclic change of shape lowers the energy from the fixed-radius phase minimum. If the overall coupling scale is also variable with no supporting force, it runs to zero in this energy. The inherited deeper-compensator hypothesis allows a distinction between a core and its visible defect but does not supply the missing readout, root constraint or numerical source/penalty ratio.

## 1. The Probe Contribution to J Can Be Written Explicitly

The retained source `sources/research/parts/v470/10_sphaera_and_physics.tex`, at `thm:variational-form`, inserts `H=H_C` into both

```text
D_mu = partial_mu+i A_mu+kappa H n_mu+eta P_perp n_mu,
Omega = ...+gamma H.
```

Holding the other fields fixed gives

```text
delta_H S_probe = integral bar(Psi) (i kappa Gamma.n-gamma) delta H Psi.
```

Assume a specified finite factorization `V_gen tensor S_spin`, with internal operators commuting with the spin matrices, and a specified Dirac adjoint `bar(Psi)=Psi* (I_gen tensor eta_D)`. These are required representation data, not consequences of merely labelling a channel a frame. Put

```text
C = eta_D (i kappa Gamma.n-gamma),
R_Psi = |Psi><Psi|,
J_Psi = Herm Tr_spin[(I_gen tensor C) R_Psi].
```

Then the real variation is exactly `Re delta_H S_probe = integral Tr(J_Psi delta H)` for Hermitian `delta H`. Equivalently, arrange amplitudes as a matrix `W` with generation rows and spin columns:

```text
J_Psi = Herm(W C^transpose W*).
```

The transpose here is not an adjoint: it follows from the declared row convention. Direct contraction verifies the formula for arbitrary complex spin weights. Weighted incoherent sums of probe amplitudes add their corresponding sources. A Dirac-weighted source need not itself be positive; a later positive modal density is an additional reduction.

The curvature contribution is the Hermitian representative of

```text
kappa n_nu Tr[(D_mu^ad F^{mu nu}) delta H],
```

with the trace and boundary assumptions already stated in the earlier audit. The full `J_S` is a generation matrix, not just a scalar current. The source fields, their spin representation and their joint background have not yet been evaluated on the generation carrier.

### Why the Displayed Scalar Currents Do Not Determine This Matrix

The source defines `J_nu^(Psi)=bar(Psi) Gamma_nu Psi`, and the other two currents by derivatives of traces. No generation/gauge generator is inserted in those displayed current definitions.

Take a fixed spinor `u` and a normalized generation vector `v`, with `Psi=v tensor u`. Every fully generation-contracted spin bilinear is

```text
Psi* (I_gen tensor C) Psi = u* C u,
```

independent of `v`. But the matrix source is proportional to `|v><v|`. For the cyclic shift `U`, the two choices

```text
v_local=(1,0,0),       v_uniform=(1,1,1)/sqrt(3)
```

have respectively `Tr(|v><v| U)=0` and `1`. Thus even all such scalar spin currents do not recover the matrix element needed by the phase equation. This is an information-loss witness for the current readout, not a claim that both choices solve the complete coupled native field system.

If the printed resonance equation is read literally as `D_mu F^{mu nu}=j^nu I_gen`, its curvature source is central and has zero contraction with `U`. An intended non-Abelian interpretation instead needs the explicit generator-resolved current and representation. Its normalization and the native connection's reality/metric conditions must be derived from the action, not supplied by this scalar reading.

The inherited cross-bilinear geometry channel, in `12_structural_core.tex` near `prop:expected-probe-lensing-behaviour`, offers a place to retain coupled-probe information. It does not give the generation-resolved amplitudes or evaluate `Tr(J U)`; its focusing functional is explicitly heuristic. It is not already the missing source value.

## 2. Self-Consistent Cyclic Feedback Does Not Generate the Needed Coherence

To test more than an arbitrarily frozen source, assume a licensed canonical, Hermitian modal reduction with one common real spin coupling `g`, a positive number-density matrix `rho`, and no other generation torque. The finite energy is

```text
E(H,rho,Phi) = lambda_H ||H-Lambda(Phi)||_F^2+g Tr(rho H),
Lambda=t Q(Phi),       Q=B*B,       t>0.
```

Here `rho` is a modal population matrix, not the earlier closure coefficient also denoted rho. This reduction is not the unproved assertion that the native resonance operator is already a self-adjoint time Hamiltonian. Any direct `B` dependence of the remaining probe energy must be retained in a fuller model.

First allow unconstrained Hermitian `H`, as in the previous analysis. Exact elimination gives

```text
H_star = Lambda-g rho/(2 lambda_H),
E_eff = g Tr(rho Lambda)-g^2 Tr(rho^2)/(4 lambda_H),
h_rho = delta E_eff/delta rho = g Lambda-g^2 rho/(2 lambda_H).
```

With unitary modal evolution `i rho_dot=[h_rho,rho]`, the self term commutes with its own density:

```text
i rho_dot = g[Lambda,rho].
```

For the cyclic candidate `Lambda=t B^2`, `B=aI+zU+conjugate(z)U*`, all `Lambda(Phi)` commute with the fixed `U`, even when `Phi` changes with time. Consequently

```text
j = Tr(rho U),
j_dot = i g Tr(rho[Lambda,U]) = 0.
```

This is stronger than merely noting that equal occupations are phase blind. A localized probe can develop off-diagonal density entries while retaining `j=0`; arbitrary local coherence is not the particular cycle coherence required by the force. The feedback term does not supply a missing initial `j` by itself. A nonzero initial mode imbalance is possible, but is then state data, not a universal phase prediction.

A noncirculant interaction `h_extra` can change this:

```text
j_dot = i Tr(rho[h_extra,U]).
```

The formula gives an explicit test for the native triadic/gauge coupling. It does not rule out such a coupling: its matrix elements relative to the generation cycle remain unknown. Dissipation, a bath, changing occupations, spin-dependent correlations or a varying carrier require their own evolution equations and are not covered by this closed unitary test.

## 3. Solving the Positive-Compensator Case Instead

The previous elimination explicitly excluded a minimizer that violates an imposed positive cone. That case can be solved without adding a fitted phase potential. Consider the different model

```text
E(H,Phi) = lambda_H ||H-Lambda(Phi)||_F^2+<J,H>,
H>=0,       lambda_H>0,       J=J*.
```

Complete the square and minimize the distance to the positive-semidefinite cone:

```text
X = Lambda-J/(2 lambda_H),
E = lambda_H ||H-X||_F^2+<J,Lambda>-||J||_F^2/(4 lambda_H),
H_star = X_+.
```

`X_+` retains the positive eigenvalues of `X` and replaces the negative ones by zero. To see why it is the global minimizer, diagonalize `X`: in that chart every off-diagonal entry of `H` adds a nonnegative square, and each allowed diagonal entry separately minimizes `(h_i-x_i)^2` over `h_i>=0`. This also proves uniqueness for fixed `Lambda,J` because the quadratic is strictly convex.

The equivalent constrained equations are

```text
2 lambda_H(H-Lambda)+J-S=0,
H>=0,       S>=0,       H S=0.
```

`S` is the constraint reaction, not another freely chosen source or a new fitted coupling. These are variational inequalities/complementarity conditions. They are not the source's exact matching equation `H=Lambda`.

### A Symmetric, Self-Consistent Population Test

Take three equally populated modes, `rho=I_3`, and a common positive coupling, `J=g I_3`, `g>0`. This is a populated finite sector, not the empty quantum vacuum. Its density commutes with any instantaneous modal Hamiltonian, so it is a stationary density in this simplified closed model; a process preparing it has not been derived.

With `Lambda=t Q`, define the dimensionless input ratio

```text
k = g/(2 lambda_H t).
```

The full matrix minimizer is then

```text
H_star=t(Q-kI)_+,
S=2 lambda_H t(kI-Q)_+.
```

The reduced energy is an explicit non-polynomial spectral function:

```text
E_eff/(lambda_H t^2) = sum_i f_k(q_i),
f_k(q) = q^2                 when q<=k,
         2kq-k^2             when q>=k.
```

Without the positive constraint the energy would be `g t Tr Q-3g^2/(4 lambda_H)`, phase independent since `Tr Q=1`. Positivity changes that result when modes reach the boundary. The envelope derivative, or direct differentiation of the piecewise energy, gives

```text
E_eff'=-2 lambda_H <H_star-Lambda,Lambda'>
       =<J-S,Lambda'>=-<S,Lambda'>.
```

The last equality uses `J=gI` and `Tr Lambda'=0`. The constraint reaction supplies a generation-resolved spectral filter even though the imposed population is symmetric. This does not contradict section 2: it is a different constrained model, and no nonzero probe cycle coherence has been generated. Nor does it contradict the low-degree polynomial obstruction: spectral clipping is not a polynomial of degree at most five.

## 4. Exact Interior-Phase Law and Stability

Retain the earlier assumed fixed-radius family

```text
a=1/sqrt(6),       r=1/sqrt(12),       u=Phi/3,
0<=Phi<=pi/4,
q_small=(a+2r cos(2pi/3+u))^2,
q_middle=(a+2r cos(4pi/3+u))^2,
q_large=(a+2r cos u)^2.
```

On the open chamber, `q_small` decreases, `q_middle` increases and `q_large` decreases. All three are positive; their sum is one. The positive-root condition on `B`, rather than squaring arbitrary negative roots, fixes this interval.

For the branch with two modes clamped, `q_small,q_middle<k<q_large`,

```text
F=E_eff/(lambda_H t^2)
 = Tr Q^2-(q_large-k)^2,
Tr Q^2=17/24+(sqrt(2)/6)cos(Phi).
```

For `Phi>0`, differentiating gives

```text
F'=2 q_large' [k-K(Phi)],
K(Phi)=q_large-(Tr Q^2)'/(2 q_large'),
q_large'=-(4r/3)(a+2r cos u)sin u.
```

The apparent `0/0` at `Phi=0` is removable. With `x=cos(Phi/3)`, direct simplification gives the explicit law

```text
K(Phi)=(1+sqrt(2)x)^2/6 - 3(4x^2-1)/(4(1+sqrt(2)x)).
```

Its endpoints are exact:

```text
K(0)    =(33-23sqrt(2))/12 = 0.0394240054516...,
K(pi/4)=(2-sqrt(3))/4     = 0.0669872981078....
```

For completeness, its derivative with respect to `x` is

```text
dK/dx = 2[x^3-(3sqrt(2)/4)x^2-3x-5sqrt(2)/16]
        /[3(x+sqrt(2)/2)^2] < 0
```

on `cos(pi/12)<=x<=1`: `x^3-3x<0` and both remaining terms are negative. Since `dx/dPhi<0` for `Phi>0`, `K'(Phi)>0`. There is therefore exactly one positive interior solution `k=K(Phi_star)` whenever

```text
0.0394240054516... < g/(2 lambda_H t) < 0.0669872981078....
```

It has the conjugate partner `-Phi_star`. At the solution,

```text
F''(Phi_star)=-2 q_large'(Phi_star) K'(Phi_star)>0.
```

### Checking the Active Set and the Global Chamber Minimum

The stationary branch really has two clamped modes. `K<q_large` follows because `(Tr Q^2)'` and `q_large'` are both negative. At `k=q_middle`, direct differentiation gives

```text
F'=2(q_small-q_middle)q_small'>0.
```

Comparing this with `2q_large'(q_middle-K)` proves `q_middle<K` on the open chamber. Thus the stationary solution stays in the assumed active set.

For a fixed `k` strictly between the endpoint values, `q_small<k<q_large` throughout the chamber. Wherever `q_middle<k`, strict monotonicity of `K` makes `F'` negative before the stationary point and positive after it. If `q_middle` later crosses above `k`, the formula becomes

```text
F=q_small^2+2k(1-q_small)-2k^2,
F'=2(q_small-k)q_small'>0.
```

There is no lower minimum after that crossing. The interior solution is therefore a global minimum on this fixed-radius phase chamber, not only a stationary point. Strict convexity in `H` and this reduced minimum give a minimum jointly in `H` and `Phi` with `a,r,t` fixed. Sections 8--9 show why this is not a minimum against released shape and scale directions; spatial, gauge, population and other native variations remain separate obligations.

## 5. Numerical Example, Not a Calibrated Prediction

Use the illustrative round input `k=0.05`, not a value inferred from the historical phase or lepton masses. Bisection of the monotone exact law gives

| Quantity | Conditional result |
| --- | ---: |
| Positive phase `Phi_star` | `0.487058671539 rad` |
| Local root coefficient phase `theta` | `2.256747992906 rad` |
| `q_small` | `0.001810419273` |
| `q_middle` | `0.041693402214` |
| `q_large` | `0.956496178513` |
| `H_star/t` eigenvalues | `(0,0,0.906496178513)` |
| `E_eff/(lambda_H t^2)` | `0.0948912352574` |
| Phase curvature in the same energy units | `0.00529273379816` |

The exact threshold law and its derivative are checked symbolically and independently against matrix minimization and finite differences. Computed eigenvalues of exact zero modes can be negative at about `1e-16`; the report retains those roundoff values and states a `1e-12` numerical tolerance. They are not negative physical modes.

Changing the input ratio moves the phase continuously through the entire interior interval. This is therefore a mechanism, not a parameter-free value. Matching a desired angle by inverting `K` would merely calibrate this ratio.

There is also an important readout cost: `Q` has three positive eigenvalues, but the selected compensator has **rank one**, not three positive eigenvalues. It cannot itself be declared the three charged-lepton masses. A separate physical coupling/Schur readout could still involve `Q`, but that identification, its chirality, canonical kinetic terms and scale remain unproved.

## 6. What Must Change Before This Can Enter the Main Theory

The native source currently defines positive `H_C` by `H_C=Lambda` and additionally sets the mixed closure residue to zero in the exactly closed system. In this example `H_star!=Lambda`; the earlier mixed-block realization also has nonzero closure residue. Thus it is **not** a solution of those native equations.

To use the constructive branch, one would have to justify replacing exact matching by the positive-field variational inequality, reconcile strict versus dressed/off-closure sectors, and establish the positive static modal reduction from the real full action. The source's connection and spin representation do not automatically provide those conditions. Its other direct tensor/probe/curvature phase forces cannot be discarded in a purported full solution.

The existing source now provides a precise research choice, not a numerical answer: retain `H_C=Lambda` and calculate phase selection solely from the substituted remaining action, or justify an independently varied positive compensator with its complete source and constraints. In the second case the additional ratio `g/(2 lambda_H t)` must be calculated from the actual population and native coefficients, independently of any target masses.

Neither branch here identifies a gravitational operator, a wormhole, a native C5 residual, the Koide radius or the absolute mass scale. No change to the main TeX or publication scope was made.

## 7. Can the Deeper Compensator Keep Exact Closure Intact?

The retained `13_hc_hypotheses.tex` already distinguishes the visible positive defect field from a deeper generator. In `hyp:frame-dependent-defect-readout` it proposes

```text
H_def^(f) = D_read^(f)(H_core;M,P),
```

explicitly at hypothesis grade, without evaluating `D_read`. This is a relevant structural opening, not a new discovery or a constructed bridge. The source's spectral projector `C`, the effective field `H_def` and the hypothesized generator `H_core` must not be silently identified. The working premise audit also qualifies the inherited spectral-projector claims.

Two possible readouts have very different consequences:

1. If the positive field's visible readout is an isometric compression `S* H_core S`, zero readout implies `H_core S=0`. Indeed `||H_core^(1/2) S v||^2=0` for every `v`. The generator may survive on the hidden complement, but cannot have a nonzero direct or cross action on those visible seeds. This is a finite positive-carrier statement, not a claim about an indefinite metric or an unspecified nonlinear readout.
2. If the visible readout instead measures mismatch, for example `[H_core,P]*[H_core,P]`, zero only forces block preservation. A nonzero internal block `P H_core P` can remain. This supplies a concrete algebraic distinction between a surviving core and a vanishing defect, but is not an identification of `M`, `C` or the actual native `H_core`.

In the written probe action, the field multiplying `gamma` and entering the connection is still the effective `H_def`. A surviving deeper object does not automatically appear there when `H_def=0`. Its action on probes would require a specified additional readout/coupling or an evaluated dependence of the triadic tensor on that core.

Therefore renaming the positive variable of section 3 as a deeper compensator does not reconcile its nonzero matching residual with the old equation. The map, target functional and source action must be supplied. Hypothesis 7.5 provides the distinction, not the numerical dynamics needed to complete it.

## 8. Releasing the Assumed Koide Radius Lowers the Energy

Keep `t,g,lambda_H` fixed and retain the same positive-field energy, `Q>=0`, `Tr Q=1` and cyclic symmetry, but do not impose the unproved radius `r/a=1/sqrt(2)`. The reduced spectral function satisfies the exact identity

```text
f_k(q) = 2kq-k^2+(k-q)_+^2,
F(Q) = E_eff/(lambda_H t^2)
     = 2k-3k^2+sum_i (k-q_i)_+^2.
```

For `0<k<1/3`, the unrestricted fixed-trace global minimum is therefore

```text
F_min=2k-3k^2,
argmin F = {Q>=kI : Tr Q=1}.
```

There are many such matrices, including unequal positive spectra, not a uniquely selected hierarchy or phase. `Q=I/3` demonstrates nonemptiness. At or above `k=1/3`, the unique global minimum is `Q=I/3` with `F=1/3`. One direct proof sets `d_i=(k-q_i)_+`: `sum d_i>=3k-1`, and `sum d_i^2>=(sum d_i)^2/3`. Inserting the bound gives `F>=1/3`; equality at these thresholds forces equal modes.

### An Admissible Cyclic Descent From the Previous Phase Minimum

For any interior phase solution of section 4, both small eigenvalues satisfy `q_i<k<1/3`. Define

```text
Q_e=(1-e)Q+e I/3,       0<=e<=1,
B_e=sqrt(Q_e).
```

The path preserves positivity, `Tr Q_e=1` and commutation with the fixed cycle `U`. Its principal root remains Hermitian and cyclic. Since a three-cycle has simple spectrum, every such commuting three-dimensional matrix is circulant, so `B_e=a_e I+z_e U+conjugate(z_e)U*` with `Tr B_e^2=1`. No change of carrier, cycle or norm is required. The root radius and generally its phase are now allowed to respond.

The exact one-sided initial energy derivative is

```text
dF(Q_e)/de at e=0
 = -2 sum_(q_i<k) (k-q_i)(1/3-q_i) < 0.
```

Thus the previous minimum is not stationary on this larger allowed shape space. This does **not** refute its constrained minimum if a genuine native fixed-radius law forbids the path. It shows precisely why that law is necessary rather than optional.

There is even a pure radius descent while holding the original phase fixed. Use

```text
B(s,Phi)=[I+s exp(i theta)U+s exp(-i theta)U*]/sqrt(3+6s^2),
s=r/a,       theta=(2pi+Phi)/3.
```

At the illustrative `k=0.05` phase minimum, direct differentiation gives `partial F/partial s=0.007425933377...` at `s=1/sqrt(2)`. Slightly decreasing `s` remains in the positive-root chamber and lowers the energy. The explicit matrix derivative, not only a finite-difference observation, is retained in the executable check.

For the same unfitted test example:

| Quantity | Value |
| --- | ---: |
| Previous fixed-radius energy `F` | `0.0948912352574` |
| Released-radius fixed-trace minimum | `0.0925` |
| Exact mixing descent derivative | `-0.0367969716722` |
| First mixing fraction reaching the global minimum | `0.145358220151` |
| Energy at mixing fraction `0.2` | `0.0925` |
| Resulting `r/a` | `0.419840799569` |
| Resulting principal-root Koide ratio | `0.450844197988` |

These are structural counterexamples in the reduced model, not alternative measured lepton masses. They show that this energy can improve by leaving the imposed `K=2/3` circle. The resulting lower-energy plateau need not select equal masses, so the conclusion is loss of shape selection, not universal mass degeneracy.

## 9. Releasing the Overall Scale Drives This Energy to Zero

Suppose additionally that the Millennium transition amplitude determining `t` is allowed to vary. Keep the physical source `g` and penalty coefficient `lambda_H` fixed; one must **not** hold `k=g/(2 lambda_H t)` fixed in this variation. Direct constrained-envelope differentiation gives

```text
dE_eff/dt
 = -2 lambda_H <H_star-tQ,Q>
 = 2 lambda_H sum_i q_i min(t q_i,g/(2 lambda_H)) > 0
```

for `t>0`, `g>0`, `Tr Q=1`. This part of the energy has no stationary nonzero scale. Its endpoint is

```text
t=0,       H_star=0,       E_eff=0.
```

At that endpoint the normalized phase/shape is not selected by this energy. In the conditional mixed-Millennium bridge, `t=(rho_cl+sigma_cl)s_M^2` with a fixed positive coefficient sum, zero `t` removes the mixed block and coincides with the algebraic exact-closure limit. It is not thereby a complete solution of the native gauge/probe field equations or their nonzero source constraints.

The important qualification is that the displayed native field tuple does not itself list `M` or its mixed amplitude as an independent field variable. If those are fixed background data, this scale variation is not licensed and cannot be used to assert physical decay of the coupling. In that case their scale is input, not a value derived by minimizing this action. If they are dynamical, their other forces or constraints must be supplied before claiming a nonzero equilibrium or time evolution.

At the illustrative point `t=lambda_H=1`, `g=0.1`, the scale derivative is `0.099132852664...` in the declared energy/field units. No Planck or electroweak scale is extracted from it.

## 10. What the Existing Equations Do and Do Not Fix

### Exact Matching Cannot Be Recovered While Keeping This Interior Mechanism

At every interior phase minimum of section 4 the largest compensator mode is active and differs from its target by `t k`. Therefore

```text
||H_star-Lambda||_F / ||Lambda||_F
 >= k/||Q||_F >= k > (33-23sqrt(2))/12.
```

Here `||Q||_F<=Tr Q=1` because `Q>=0`. In the analyzed three-mode block there is at least a `3.94%` relative mismatch in this comparison, not an arbitrarily small approach to exact matching. The illustrative point has about `6.80%`. Adding matched spectator blocks changes the full-matrix Frobenius denominator, so this is not a universal percentage for the whole native carrier. This operator mismatch must not be identified with the earlier angular shift; they are different quantities.

Increasing `lambda_H` at fixed `g,t` gives `k->0`, leaves the interior-selection interval and recovers phase-blind matching in any fixed strict-positive-root region. Alternatively holding `k` in the interval by scaling `g` as well changes the physical source, not just enforcement of the same constraint.

### Neither Normalization Nor a Shift Fixes the Ratio

A search of the retained source finds `lambda_H` in its compensator-current definition and the action penalty, without a numerical determination equation. The probe mass coefficient `gamma` and the closure coefficients `rho_cl,sigma_cl` are called effective coefficients; the state determining the common modal source `g` is not evaluated. This search does not prove that a future full background solution could never determine them. It means the current displayed definitions do not evaluate `g/(2 lambda_H t)`.

Changing field units cannot repair this. Under

```text
H'=cH,       t'=ct,       lambda_H'=lambda_H/c^2,       g'=g/c,
```

the energy and `k` are unchanged. A QAM tag migration likewise does not create the missing numerical input. Changing `g` independently is a physical/source change; choosing it to reproduce an angle is calibration.

### The Exact Additional Shape Obligation

For a positive principal root with `Tr B^2=1`, Koide would require

```text
Tr B=sqrt(3/2).
```

In the cyclic parametrization this fixes `a=1/sqrt(6)` and `r=1/sqrt(12)`, hence protects precisely the circle used in section 4. The existing propositions `v480:koide-equal-norm` and `v480:koide-hc-mixing` give equivalent/sufficient conditions, including orthogonality of the represented HC image to the symmetric root direction. They do not establish that the native HC/seed map meets that condition. Cyclic symmetry, projector idempotence and the deeper-generator hypothesis alone do not do so.

If this root trace is imposed as a hard constraint, the shape descent in section 8 is forbidden and the phase-only theorem is valid on that constrained surface. Calling the imposed trace a derivation of Koide would be circular. A soft stabilizing force would instead have to balance the nonzero radial derivative and pass the coupled radius/phase stability test; a potential merely centered at the old radius with zero first derivative does not keep that exact radius after the new force is added.

The next native requirement is therefore concrete: derive the independent equal-norm/root-trace law and nonzero scale support from represented operators or the full background equations, while retaining the separate source/phase problem. The present cone energy supplies none of these by itself. No arbitrary radial potential, selected multiplier or numerical ratio was added to make the example fit.

The following [HC/root-readout audit](HC_Root_Readout.md) tests this requirement with an explicit nonlinear candidate. A quadratic residual map can protect the radius only with an independently justified metric-isometric transfer; its relative coefficient remains exposed. A further sharp positivity bound rules out that isometric choice on the full two-mode input cone: this candidate then needs a physically selected and preserved restricted background domain, or replacement by another readout. Fixed-simple-clock countermodels satisfy strong HC channel balance without the Koide root balance. These results do not derive the missing native metric, domain dynamics or scale support.

The subsequent [root-phase dynamics analysis](HC_Root_Phase_Dynamics.md) proves the exact normalized dictionary with this static phase energy. It distinguishes an added chamber-preserving gradient law, finite-barrier inertial trapping and a different canonical complex-mode evolution. In the last extension the old radial descent becomes an accessible transverse mode even at fixed pure-mode norm; the angular minimum is a hyperbolic saddle. This does not apply if a native constraint excludes that extension, but the actual projected evolution and preparation must then be derived. No damping or kinetic law is inferred merely from static minimization.

## Reproduction

`python -B analysis/HC_Source_Backreaction.py --output analysis/HC_Source_Backreaction.json` reproduces the separate machine-readable report. The 58 checks in `scripts/qsc_audit/tests/test_hc_source_backreaction.py` cover the original 34 source/conservation/cone checks and 24 additional radius/closure checks. The additions verify normalized cyclic shape paths, pure radial and mixing descent, the unrestricted trace minimum and plateau, exact Koide-constraint loss, the fixed-source scale derivative, the zero-scale endpoint, field-unit covariance, the stiff-matching limit and relative mismatch bound, distinct positive-compression/mismatch readouts, the hypothesis-grade source boundary and invalid inputs. NumPy was already installed; no new package is required by the executable checks. None of these finite regressions certify the uncomputed native model.
