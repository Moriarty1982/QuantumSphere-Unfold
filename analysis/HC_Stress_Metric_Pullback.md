# Stress-to-Metric Reconstruction, Action Pullback and Causal Data

Date: 2026-10-16. Status: conditional first-order stress-to-metric map, a checked reduced-action reaction, an explicit free-radiation nonuniqueness example and a causal doubled-history construction. This assumes the Einstein response of the previous comparison; it does not derive that response, its Newton coefficient or the native HC/coframe dictionary from QAM. No main-TeX change is adopted.

## Result

The [common-metric Dirac calculation](HC_Dirac_State_Gravity.md) no longer needs a separately guessed sourced weak metric: once a Green operator, gauge and gravitational boundary/initial data are declared, it gives a functional of the complete probe stress. This is a **nonlocal differential bilinear** in the effective probes, not the original pointwise real bilinear coframe. The distinction is a change in physical dictionary, not an equivalent rewriting of the native definition.

Three checks make this statement precise:

1. Eliminating a metric from its quadratic action gives one quarter of its source pairing. The induced probe variation agrees with the earlier common-metric Dirac reaction. Substituting only into the matter action doubles that reaction.
2. The same zeroth-order probe stress admits different curved weak metrics if independent incoming/free gravitational radiation is allowed. This is not merely a coordinate ambiguity: an explicit transverse-traceless wave has zero Einstein tensor but nonzero linear Riemann tensor. Its extra Dirac reaction can also be solved.
3. A single-history real action with a naively inserted retarded kernel varies into retarded **plus advanced** response. A doubled-history initial-value construction gives the intended retarded response, provided the histories are identified only after variation.

These are conditional reductions of an assumed Einstein--Dirac comparison, not a microscopic emergence theorem, an exact nonlinear solution or quantum-gravity validation.

## 1. What the Reconstruction Actually Determines

In the flat reference and first gravitational order, let `T=T_flat[Psi]` be the stress of the retained triadic Dirac amplitudes. In harmonic gauge the sourced equation reads

```text
Box bar_h_mu_nu=-2 kappa T_mu_nu,
P A=A-eta Tr_eta(A)/2,     P^2=I,
h[Psi;B]=kappa R_B T[Psi]+h_free[B],
R_B=-2 P Box_B^{-1}.                                           (1)
```

Here `h` is the actual leading metric perturbation in `g=eta+h+O(kappa^2)`; it is not the old scalar HC amplitude. The free wave is taken at the same weak order. `P` is trace reversal in four dimensions, **not** the native closure projector. The symbol `B` records the Green-function prescription, comparison/gauge choice, domain and gravitational data.

With retarded data, (1) depends on the source in the past light cone, plus the independent homogeneous gravitational solution. It is not a rule assigning a metric from the probe value at the same point. Likewise a fixed finite internal matrix such as the Millennium matrix does not automatically define this spacetime Green operator without an actual represented differential/domain map.

Equation (1) is valid as an Einstein solution when its source and data satisfy the harmonic constraints. A conserved zeroth-order on-shell Dirac stress supplies the source condition. For off-shell variations one must instead use an explicit gauge-fixed quadratic inverse; one may not require the arbitrary varied stress to remain conserved and then claim to have varied every probe component.

Most importantly, solving (1) is **not a derivation of Einstein's equation**. It uses the Einstein--Hilbert leading response already assumed in the common-action comparison. The native conditional effective action also assumes its geometric derivative expansion. Its coefficient, coarse-graining and operator matching remain open.

## 2. Reduced Action and the Factor of Two

Use the real Lorentzian tensor pairing `<<A,B>>=integral A^{mu nu} B_mu_nu`, with both indices raised by the fixed reference metric. The boundary conditions and integrations by parts must be chosen so that the gauge-fixed linear Einstein operator `E_gf` and its inverse `R_B` are self-adjoint in this pairing. Fixed homogeneous data are treated separately.

The quadratic gravitational-plus-source action is

```text
S_lin[Psi,h]=S_D0[Psi]-<<h,E_gf h>>/(4 kappa)+<<h,T[Psi]>>/2,
E_gf h=-Box P h/2,
E_gf h=kappa T,     h=kappa R_B T.                              (2)
```

At its metric stationary point, direct substitution into **both** terms gives

```text
S_reduced[Psi]=S_D0[Psi]+S_ind[Psi],
S_ind=kappa <<T,R_B T>>/4=<<h,T>>/4,
delta S_ind=kappa <<delta T,R_B T>>/2=<<h,delta T>>/2.             (3)
```

**Proof.** The gravitational term becomes `-<<h,T>>/4`, while the matter coupling is `+<<h,T>>/2`. Their sum is the first identity. Varying the two source slots in the symmetric quadratic form gives the displayed derivative. Equivalently the metric-chain reaction vanishes by its own stationary equation: this is the variational envelope identity, not permission to discard an unsolved metric equation.

The naive matter-only substitution instead gives `<<h[Psi],T[Psi]>>/2`, twice the induced term. Differentiating it gives twice the correct source reaction. The gravitational action cancels the extra chain contribution. If fixed free gravitational data are present, their external linear coupling contributes `<<h_free,T>>/2`, with appropriate boundary terms and constants accounted for separately.

The inverse and homogeneous boundary data are held fixed during (3). A probe-dependent domain, coarse-graining, gauge map or boundary prescription adds its own variations. A merely pointwise right inverse, without matched boundary terms, is not automatically an admissible reduced-action kernel.

Since the leading stress is quadratic in effective amplitudes and `R_B` is linear, the induced functional is quartic. This is the familiar weak gravitational self-interaction structure of the comparison, not a new native phase potential, a positive-definite energy theorem or a fundamental nonlinear quantum law.

## 3. Check Against the Actual Dirac Reaction

The full common-metric Dirac action has the first-order metric coupling `L1=h_mu_nu T_off^{mu nu}/2`, where the **off-shell** stress retains the reference `eta_mu_nu L_D0` term. Its spinor Euler derivative is

```text
EL_barPsi(L1)=D1[h]Psi+Tr_eta(h) D0 Psi/2.                       (4)
```

This follows independently by expanding `sqrt|g| D_E Psi`, where `D_E=D0+D1[h]+...` and `sqrt|g|=1+Tr_eta(h)/2+...`. The varying gamma matrices and spin connection are those of the same symmetric tetrad as in the previous Dirac note. On a zeroth-order solution, `D0 Psi0=0`, so (4) reduces to the previously computed `D1[h]Psi0`.

The numerical action test does not vary only the relative phase or normalized mode populations. It varies arbitrary four-component spinor Fourier amplitudes and their derivatives off shell. The fields and variations share one harmonic temporal frequency in this static regression sector; this is not a general four-dimensional time-grid simulation. The finite-difference derivative of (3) agrees with the independently reconstructed common-metric operator. A separate deliberately off-shell baseline retains the measure-times-`D0` term in (4); omitting that term fails the check.

For a reproducible stationary test use a two-dimensional static periodic grid and a nonzero-mode Fourier inverse

```text
R(k)=2 P/|k|^2 for k!=0,     R(0)=0.                            (5)
```

This is a self-adjoint, gauge-fixed **nonzero-mode** regression sector. The code records the removed constant source explicitly. It is not a full-source periodic Einstein solution or a retarded history. At the selected triadic modes and `kappa=0.2`:

```text
induced action                      = 2.6986927021510858e-6
eliminated-parent/action difference = 4.24e-22
source-direction variation error    = 3.75e-17
spinor variation/Dirac-reaction error= 1.73e-16
omitted constant-source norm        = 0.019796337989986635
```

The earlier local polynomial solution still supplies an Einstein particular solution for that positive constant source on a nonperiodic weak patch. Its source-dependent polynomial boundary values have **not** been proved to define a self-adjoint or retarded action inverse, and are not quietly used as one in (3). A complete causal/domain-specific reduction must supply the corresponding data and boundary terms.

The Fourier test also separates local and integrated phase dependence: changing the relative phase moves the local sourced metric, but the integrated induced action of these translationally related two-mode patterns is unchanged. Global common rephasing changes neither source nor metric. No universal phase-selection potential follows from this example.

## 4. Same Probe Source, Different Physical Curvature

In a fixed harmonic gauge, add the free wave

```text
h_TT=A cos(omega(t-z)) diag(0,1,-1,0),
G^(1)[h_TT]=0,
R^(1)_0x0x=+A omega^2 cos(omega(t-z))/2.                         (6)
```

It is trace-free, transverse and solves the homogeneous wave equation. The nonzero linearized Riemann component proves that this is not a removable infinitesimal coordinate gauge wave. Adding it leaves the first-order Einstein source unchanged, while changing actual tidal curvature.

The matter reaction is not ignored. Solve

```text
D0 Psi1,TT=-D1[h_TT]Psi0,     Psi1,TT(0,x)=0.                    (7)
```

The additional forcing has four Fourier modes, each with one harmonic clock. A constant five-dimensional augmented matrix and the installed `mpmath.expm` give its explicit solution. Adding (7) to the prior first-order spinor correction yields a second weak Einstein--Dirac family. Both share the same zeroth-order probe source and the chosen zero correction data at the initial slice; their gravitational data differ. They are not claimed to have identical exact quantum states or stresses at higher orders.

At `(0.08,0.2,-0.3,0.1)`, `A=0.03`, `omega=1.1`, the free Einstein residual is zero and the linear tidal component is about `0.0181456`. These are dimensionless first-order coefficients, not measured curvature. The extra probe correction is nonzero, about `7.07e-5`, with its linear Dirac residual about `1.12e-19`. After adding this wave and reaction, the full Einstein/Dirac residuals again fall by approximately four when the gravitational strength is halved.

Thus the probe source alone does not select the entire metric, even after a gauge is fixed. One must also specify gravitational initial/incoming data. Choosing no incoming radiation can define a particular retarded prescription; it is an additional condition, not a consequence of a local probe bilinear.

## 5. Why a Naive Retarded Action Fails

A real single-history source functional of the same form as (3), but with a nonsymmetric retarded response, has the variation

```text
S_naive=kappa <<T,R_ret T>>/4,
delta S_naive=kappa <<delta T,(R_ret+R_ret^dagger)T>>/4.          (8)
```

For a self-adjoint wave operator the transposed retarded kernel is the advanced kernel, with its corresponding boundary prescription. A source at a later time therefore contributes to the naive earlier variational gradient. Writing `retarded` in the kernel does not prevent this symmetrization.

The implementation checks (8) independently using the elementary retarded oscillator kernel `theta(t-t') sin(omega(t-t'))/omega`. Trapezoidal weights are retained, including on a nonuniform time grid; the adjoint is the weighted one. A terminal-time source produces zero actual retarded response at all earlier sample times, but a nonzero earlier gradient from the ordinary single-history action. The kernel test verifies the variational issue; it is not a measured gravitational response or noise spectrum. Independent comparison to a forced-oscillator solution checks quadrature convergence.

No conclusion about irreversibility or viscosity follows just from choosing retarded data. The full Einstein--Dirac comparison remains conservative; eliminating a sector can introduce memory and initial-data dependence in a reduced description.

## 6. A Causal Doubled-History Construction

Introduce two histories of the **same** source and define

```text
T_c=(T_1+T_2)/2,     T_d=T_1-T_2,
S_ind,CTP=kappa <<T_d,R_ret T_c>>/2.                             (9)
```

Vary first. Then take the physical limit `T_1=T_2=T`. In a left-history variation, `delta T_d=delta T_1`, while every term multiplying unvaried `T_d` vanishes. Therefore

```text
delta_1 S_ind,CTP|physical=kappa <<delta T_1,R_ret T>>/2.          (10)
```

This is exactly the required retarded source reaction from a metric `h=kappa R_ret T`. There is no advanced term at the physical limit. Both the average and difference contributions are kept away from that limit and checked against independent finite variations. Although (9) is zero on coincident histories, its physical variational derivative is not: setting the histories equal **before** variation would delete the equation.

This is the classical doubled-history/closed-time-path response structure. Appropriate initial and final matching conditions are required for a full variational initial-value problem. A quantum influence functional additionally needs its state, renormalization, fluctuations and noise terms; none is supplied by (9) alone. This construction must not be identified merely by notation with the paper's two-sided tensor tags, ART/QFT probes, matter/tachyon frames or a wormhole. Those are different objects unless an actual map and state prescription are derived.

For the underlying variational distinction and doubled-variable formulation, see [Chad R. Galley, *The classical mechanics of non-conservative systems*, the integrated-oscillator example and doubled-history construction](https://arxiv.org/html/1210.2745v2). The reduced-action prefactors, Dirac-source checks and free-gravitational-wave example above are explicitly worked out here; the general retarded-action issue is established literature, not a claimed discovery.

## 7. Native Interpretation and Next Obligation

At the declared weak scope one may now write an effective sourced coframe candidate

```text
E_eff[Psi;B]=I+eta h[Psi;B]/2+O(kappa^2).                        (11)
```

It is background-supported and nonlocal through (1). This differs from the native local real `Re(barPsi Gamma D Psi)` definition and does not evade the previously proved same-frame trace obstruction while preserving that definition. The older rank-one example remains a negative control.

Equation (11) supplies a conditional **effective dictionary**, not a proof of its microscopic origin. Its immediate native obligations are to justify this nonlocal/coarse-grained readout from the actual represented operators; identify which probe modes are retained versus integrated out; select gravitational data and a causal variational prescription; and derive the scale/couplings. Simply solving the assumed Einstein operator would otherwise be circular as a proposed derivation of gravity.

This continuation establishes neither exact nonlinear closure nor universal quantum-gravity validity. It does specify how a consistent probe-only weak action could be formed and why both boundary data and complete variation are indispensable.

## 8. Reproduction

`python -B analysis/HC_Stress_Metric_Pullback.py --output analysis/HC_Stress_Metric_Pullback.json` reproduces the report. Thirty-five focused tests cover self-adjoint response and source projection, gauge-fixed versus physical equations, full-parent and reduced variations, the factor-of-two negative control, actual on/off-shell spinor reactions, phase/scaling behavior, free tidal curvature and its computed matter reaction, full-equation order checks, retarded adjoints and doubled-history causality.

The code uses the existing NumPy and mpmath installations. These are written conditional identities and finite numerical regressions, not physical measurements, proof-assistant certificates or an adopted native theorem. The main TeX/PDF and inherited source remain unchanged by this analysis.
