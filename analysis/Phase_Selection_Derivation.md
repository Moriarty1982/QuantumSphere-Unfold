# Phase Selection and the Explicit Minimal HC Functional

Date: 2026-10-15. Status: explicit native substitution now shows why the minimal HC matching penalty alone does not select the phase. The earlier selection equation remains conditional, not a consequence of that substitution. No numerical native phase, Koide radius, generation embedding, gap or absolute mass scale is predicted. This is a separate analysis note; the main TeX document is unchanged.

## Result

The source supplies the minimal functional, not just a placeholder. On a positive carrier with orthogonal `P`, direct block multiplication gives

```text
M = [[A,F],[G,D]],
Lambda[M,P] = (rho+sigma) diag(G*G,F*F).
```

Consequently, on the displayed source condition `H_C=Lambda`, the matching residual `R=H_C-Lambda` and its penalty vanish for every admissible phase. This zero is independent of the particular positive comparison used for the residual. With exact closure, both mixed blocks and `Lambda=H_C` vanish as well.

This restricts the earlier proposed mechanism: the minimal matching penalty is not by itself a phase-selecting potential. Section 8 derives its actual phase dependence and the probe/curvature forces that could change the result. It also shows why freezing a field that is subsequently allowed to relax can give spurious phase stability.

For a separately justified, nonzero reduced residual, the earlier conditional selection formula is still

```text
cos(Phi) = -Re(R1* G R0)/(R1* G R1).
```

Here the independently evaluated residual must have the form `R(Phi)=R0+cos(Phi) R1`, the comparison `G` must be constant and positive, and other contributions to the phase force must vanish. Direct substitution into the minimal native functional does not establish these conditions: its matrix dependence differs from this ansatz, and on `H_C=Lambda` there is no nonzero matching residual to minimize.

The calculation now identifies the exact obstruction and the surviving source-dependent route. Selecting the right side from the historical masses would still be another fit, not the missing derivation.

## 1. What Can Be Varied in the Existing Action?

The retained source `sources/research/parts/v470/10_sphaera_and_physics.tex`, at `thm:variational-form`, contains

```text
S = integral [bar(Psi) i Gamma^mu D_mu Psi - bar(Psi) Omega Psi
              - Tr(F_mu_nu F^mu_nu)/4 - U_C7 - U_HC],
U_HC = lambda_H ||H_C-Lambda[M,P]||^2.
```

The triadic tensor enters `Omega` through a coupling `c_T T`. The displayed field content does not give a separately evaluated equation defining `T` as a function of the other carrier/field data, nor a specified kinetic/potential functional for an independently varied `T`. This is the relevant missing definition, not a failure of the numerical diagonalization. The source's designation of its variational form as a theorem is not a proof that all dependent field equations have already been derived correctly.

There are three distinct cases:

1. If `T` is a fixed operator, it is input to the probe equation, not a variable whose value follows from that equation.
2. If an independent tensor is introduced into the displayed linear probe coupling without further tensor dependence, variation produces a probe bilinear constraint, schematically `delta S/delta T_ij = -c_T bar(Psi_i) Psi_j`, not an equation solving for `T_ij`. Hermitian/allowed-component variations select the corresponding real bilinear constraints. No general conclusion that every spinor must vanish is drawn from that schematic expression.
3. If `T=T[M,P,H_C,g,...]` is derived from existing fields, its variation is determined by that map. Such a map could close the problem without a new independent field, but it has not been evaluated here.

For a phase-only parametrization of the coupling, a specified probe background contributes `-integral bar(Psi) partial_Phi(Omega) Psi` to the action derivative. This can be nonzero and state dependent. It is not a universal phase-selection law until the state, other fields and boundary conditions are supplied. At fixed other fields and `Psi=0`, the explicit probe term is zero for every tensor phase. That statement concerns the displayed probe action, not a proof that the complete quantum vacuum is phase flat: fluctuations or an evaluated implicit field dependence could generate an effective potential.

## 2. Exact HC Stationarity, Including an Active Comparison Tensor

Assume a licensed positive phase-energy reduction and put

```text
R(Phi) = H_C-Lambda[M,P],
U_HC(Phi) = lambda_H R(Phi)* G(Phi) R(Phi),       lambda_H > 0.
```

The coefficient is held constant in this differentiation. `G` is the positive Hermitian comparison on the actual residual space. It is not automatically the generation kinetic matrix or a Lorentzian spacetime metric. The displayed source norm must first be identified with this comparison; the tensor grammar does not supply its entries by itself.

Product differentiation gives

```text
dU_HC/dPhi = lambda_H [2 Re(R' * G R) + R* G' R].
```

The `G'` term is indispensable if the active comparison itself depends on the physical phase. A passive chart change must transport residuals, metric and their derivatives consistently; it cannot act as a physical phase force.

For the full reduced system, stationarity is instead

```text
0 = dE_probe/dPhi + dU_HC/dPhi + dE_other/dPhi.
```

Kinetic/gradient terms require their corresponding Euler-Lagrange derivatives when a spatially varying phase field is being solved. Minimizing the HC penalty alone is legitimate only after the other phase forces have been shown absent or consistently incorporated. Neither a positive residual norm nor a local admissibility flag proves that condition.

## 3. A Closed Selection Formula Under Explicit Reduction Assumptions

Suppose a specified residual channel admits

```text
R(Phi) = R0 + x R1,       x=cos(Phi),
```

with `R0,R1` independent of `Phi`, constant positive `G`, and no remaining phase forces. Define

```text
A = Re(R1* G R0),       B = R1* G R1 > 0.
```

Then

```text
U_HC/lambda_H = R0* G R0 + 2 A x + B x^2,
dU_HC/dPhi = -2 lambda_H sin(Phi) [A+B cos(Phi)].
```

For a nontrivial interior phase, `sin(Phi) != 0`, hence

```text
x_star = -A/B = -Re(R1* G R0)/(R1* G R1).
```

At that point,

```text
d^2U_HC/dPhi^2 = 2 lambda_H B sin(Phi)^2 > 0.
```

This proves a strict local phase minimum, with conjugate phase partners. It does not by itself establish radial, dynamical, full-field or global stability. If `R1=0`, the channel is phase blind and no preferred phase follows. If the unconstrained `x_star` lies outside the allowed positive-root range, the constrained minimum is a boundary, not the claimed interior hierarchy.

The formula is covariant under a constant nonunitary chart transformation `R_i'=D^-1 R_i`, `G'=D* G D`. Its numerator and denominator are both unchanged. This checks explicitly that the selection depends on actual residual/comparison data rather than a namespace shift or untransported coordinate norm.

One illustrative, chosen residual, not a mass calibration, is `R0=(-0.8,0.2)`, `R1=(1,0)`, `G=I`. It selects `cos(Phi)=0.8`, `Phi=0.6435011088...` and the local branch `theta=(2pi+Phi)/3=2.3088954720...`. This verifies the mechanism; those residual entries are not native data or a parameter-free prediction.

## 4. Which Tensor Invariant Can Supply This Phase Dependence?

Retain the earlier conditional Hermitian cyclic family

```text
B = a I + z U + conjugate(z) U*,       z=r exp(i theta),
a=1/sqrt(6),       r=1/sqrt(12),       Phi=3 theta modulo 2pi.
```

This radius remains the imposed Koide-shaped input. Fourier diagonalization gives real roots `ell_k=a+2r cos(theta+2pi k/3)`. Their first two invariants are phase independent:

```text
Tr B = 3a,
Tr B^2 = 3a^2+6r^2=1.
```

The first spectral phase invariant appears at cubic order:

```text
det B = a^3-3ar^2+2r^3 cos(Phi),
Tr B^3 = 3a^3+18ar^2+6r^3 cos(Phi).
```

This is precisely closed-cycle dependence. An independently justified projection onto such a cubic loop invariant could produce `R0+cos(Phi) R1`; squaring that residual would then produce the needed second harmonic. This is a possible additional reduction, not the result of the explicit minimal native `Lambda`: the latter is quadratic in the mixed Millennium blocks, as evaluated in section 8. The source does not identify it with a fitted function of this generation tensor.

For this fixed-radius family the positive-root chamber is `|Phi| <= pi/4`, up to the cycle convention. Equivalently `cos(Phi) >= 1/sqrt(2)`. At `|Phi|=pi/4` a root vanishes; at `Phi=0` two roots coincide. A stable, nondegenerate three-positive-root phase needs

```text
1/sqrt(2) < x_star < 1.
```

### Why Low-Order Spectral Polynomials Do Not Select the Needed Interior Phase

The restriction here is a real, unitary-conjugation-invariant polynomial of the single Hermitian `B`, with no additional fixed generation tensors and fixed `a,r`. Such a polynomial is a symmetric polynomial in its three eigenvalues. Its generators are `e1=Tr B`, `e2=((Tr B)^2-Tr B^2)/2` and `e3=det B`, of degrees one, two and three.

With `e1,e2` fixed, any such polynomial of total degree at most five is at most affine in `e3`, hence at most `constant+c cos(Phi)`. It is phase blind when `c=0`; otherwise it cannot have a strict interior minimum in the positive-root chamber. The constrained minima lie at the doubly degenerate or zero-root boundary.

A nonlinear dependence on `e3` first appears at degree six, for example `e3^2` or `Tr B^6`. Explicit expansion gives

```text
Tr B^6 = 3a^6+90a^4r^2+270a^2r^4+60r^6
         +(120a^3r^3+180ar^5) cos(Phi)
         +6r^6 cos(2Phi).
```

The last coefficient is `0.0034722222...` in the declared normalization. Numerical Fourier checks independently reproduce the absence of the second harmonic below degree six and its presence at degree six.

This is not a universal requirement for a sixth-degree fundamental interaction. Additional generation tensors, explicit background dependence, non-polynomial effective actions or unheld radial data change the hypotheses. In particular, a squared HC residual could supply a sixth-degree **effective** phase dependence if its unsquared residual contains the cubic invariant. That conditional possibility must not be confused with the actual quadratic minimal `Lambda` or its zero on-shell matching residual. The result does not require adding an independently invented sextic term to the paper.

## 5. Equivalent Two-Harmonic Equation and the Target Condition

The conditional residual penalty can be written, up to a constant, as

```text
V_sel(Phi) = lambda1 cos(Phi)+lambda2 cos(2Phi),
lambda1=2 lambda_H A,       lambda2=lambda_H B/2 > 0.
```

Its stationary interior phase obeys

```text
cos(Phi)=-lambda1/(4 lambda2),
V_sel''(Phi)=4 lambda2 sin(Phi)^2 > 0.
```

The strict positive-root chamber requires `-4 < lambda1/lambda2 < -2sqrt(2)`. The coefficient ratio is not an additional fitted parameter if `A,B` have genuinely been computed from the native residual. Treating the two harmonics as an independent new potential without deriving their coefficients would instead be an extra model completion, not a source result.

For clarity, the historical benchmark gives only the following diagnostic requirement:

| Quantity | Original assumed phase | Historical inversion target |
| --- | ---: | ---: |
| `Phi` | `0.674385466392` | `0.666687459003` |
| Equivalent `lambda1/lambda2` | `-3.124363296374` | `-3.143497613016` |
| Required residual projection `-A/B` | `0.781090824093` | `0.785874403254` |

The equivalent harmonic ratio changes by about `0.6124%`. This quantifies a possible residual-force change that could select the previously calibrated phase; it is not a prediction that the tensor activation makes that change. Reconstructing `R0` or `R1` from the last column would hide a mass fit in the selection rule.

For independently computed coefficients, their first-order response would satisfy

```text
delta Phi = [delta lambda1 - (lambda1/lambda2) delta lambda2]
            /(4 lambda2 sin(Phi)).
```

This converts an evaluated background/residual perturbation into a phase perturbation. If the comparison metric depends on `Phi`, or other forces remain, the full equation in section 2 must be used instead.

## 6. The Simplest Probe-Energy Minimization Also Does Not Fix the Target

For a scalar Hermitian three-probe matrix with fixed diagonal entries and nonzero fixed link magnitudes, the characteristic polynomial has the form

```text
P(E,Phi)=P0(E)-2p cos(Phi),       p=|c w1 w2|>0.
```

At a simple eigenvalue,

```text
dE_i/dPhi = -2p sin(Phi)/product_(j!=i)(E_i-E_j).
```

For the lowest level the denominator is positive. Thus its energy decreases on `0<Phi<pi` and is minimized at `Phi=pi`, not at a generic intermediate phase. The declared toy trimer verifies this derivative against direct matrix differentiation. This is a one-excitation, fixed-modulus test, not the vacuum selection of a relativistic field theory; different occupations, tensor blocks, backreaction or a regulated quantum effective action require their own calculation.

It prevents calling the desired intermediate angle a consequence of simple energy minimization when no such calculation has been given.

## 7. What Is and Is Not Derived

Derived here are the exact HC phase-force term with a comparison derivative, the conditional residual-projection selection rule and its local stability, its two-harmonic form, the low-degree spectral obstruction and the simple trimer energy-selection test. Section 8 adds the explicit minimal native substitution, the vanishing relaxed penalty, the frozen isotropic quartic obstruction and the surviving source-dependent force.

Not derived are the numerical native residual channels, the underlying tensor field relation, a state-independent vacuum, or the full phase-dependent effective action. The older finite HC menu/lock scores and zero-clock timing windows are not these quantities: `def:hc-lock-score` and `prop:v470-r15-finite-zero-clock-window-extraction` define local routing/timing tests. No identification of their phase/time variables with this internal generation loop has been supplied. Their numbers cannot simply be substituted into the formula above.

The remaining route is specific:

1. Derive `T` on a generation-resolved carrier from existing fields, or specify its independent dynamics.
2. Evaluate the non-penalty probe/curvature forces on that phase family. The minimal matching residual alone is zero on `H_C=Lambda`; the affine-cosine selection formula cannot be applied there as a nontrivial selector.
3. Include probe, connection, other phase forces and any comparison variation in one stationary background solution.
4. Establish radial/kinetic normalization, the complementary gap and the products setting `mu`. A mass reference does not fix those dimensionless data; phase selection alone does not close the absolute scale problem.

Until those inputs are evaluated, it would be incorrect to say the physical phase has been derived numerically. There is a conditional selection equation and an explicit obstruction to deriving its nonzero coefficients from the minimal matching penalty alone.

## 8. Substitution of the Actual Minimal Native Functional

### 8.1 What the Existing Definition Actually Gives

The same retained source, at `Explicit closure functional` following `sec:closure-field-system`, specifies

```text
Lambda = rho [M,P]*[M,P] + sigma R_C*R_C,
R_C = (I-P)MP+PM(I-P),                   rho,sigma >= 0.
```

In the orthogonal splitting defined by `P`, write `M=[[A,F],[G,D]]`. Then

```text
[M,P] = [[0,-F],[G,0]],       R_C = [[0,F],[G,0]],
[M,P]*[M,P] = R_C*R_C = diag(G*G,F*F).
```

This recovers the Gram identity already proved in `v480:native-penalty-identity`. The new step is to substitute it into the proposed selection mechanism rather than leave the native functional abstract.

If the source condition `H_C=Lambda` is imposed, then identically

```text
R = H_C-Lambda = 0,
U_HC = lambda_H ||R||^2 = 0,
dU_HC/dPhi = d^2U_HC/dPhi^2 = 0.
```

These statements hold along any differentiable admissible phase family satisfying that condition, including when the comparison depends on phase. In the formula of section 3, representing this zero family nontrivially as `R0+cos(Phi)R1` on an interval is impossible: both coefficients would be zero and the selection ratio would be `0/0`, not the historical target.

`thm:closed-master-system` additionally imposes `R_C=0`. That is stronger than matching the compensator. It requires `F=G=0` and hence `Lambda=H_C=0`. The nonzero mixed-block family used below is therefore an off-closure diagnostic, not a solution of that exactly closed system. This does not exclude a phase or masses in another internal operator such as `T`.

### 8.2 Conditional Cyclic Bridge: the Residual Is Not Affine in the Loop Cosine

To give the previous generation candidate its most direct test, assume additionally

```text
F=s_M B*,       G=s_M B,       s_M>0,
t=(rho+sigma)s_M^2,
Lambda=t diag(Q,Q),            Q=B*B=B^2.
```

The bridge is not supplied by the source. `s_M` has the units of the Millennium block and is not identified with the mass-dimension coupling `mu` in the separate field operator `Omega`. For the Hermitian cyclic candidate and `U^3=I`, multiplication gives

```text
Q = (a^2+2r^2) I + c(theta) U + conjugate(c(theta)) U*,
c(theta) = 2ar exp(i theta)+r^2 exp(-2i theta),
theta=(2pi+Phi)/3 on the chosen local branch.
```

In a fixed generation chart these are first and second harmonics of `theta`, not a constant matrix plus `cos(Phi)` times a constant matrix. For example, `Q(Phi)` and `Q(-Phi)` are generally different matrices although their spectra agree. Thus even freezing `H_C` does not justify the matrix-residual ansatz in section 3. A further projection must be explicitly supplied and evaluated.

The Frobenius norm nevertheless reduces to a scalar spectral invariant:

```text
Tr B^4 = 3a^4+36a^2r^2+18r^4+24ar^3 cos(Phi)
       = 17/24+(sqrt(2)/6) cos(Phi)
```

at the imposed `a=1/sqrt(6)`, `r=1/sqrt(12)`. For a fixed, generation-isotropic reference `H_0=h_P I_3 direct-sum h_perp I_3`, the actual matching penalty is

```text
||H_0-Lambda||_F^2
 = 3(h_P^2+h_perp^2)-2t(h_P+h_perp)+2t^2 Tr B^4.
```

Its only phase term is `48 t^2 a r^3 cos(Phi)`. For positive `lambda_H,t,a,r`, minimizing this on the positive-root chamber selects `|Phi|=pi/4`, where one root vanishes, not a strict interior phase. If `t=0`, it is phase blind. An anisotropic reference/comparison can change this conclusion, but then it is additional generation-resolved data, not the invariant minimal result. These quartic formulas use an explicitly declared Hilbert-Schmidt comparison; the zero on `H_C=Lambda` does not require this particular norm.

### 8.3 Why Freezing the Compensator Can Invent Phase Stability

Suppose instead `H` is an independent field being minimized. For the penalty alone,

```text
E(H,Phi)=lambda_H ||H-Lambda(Phi)||_F^2,
partial_H E=2 lambda_H (H-Lambda)=0,
H_star(Phi)=Lambda(Phi),       E_eff(Phi)=0.
```

Holding `H` at its matched value for just one phase `Phi_0` would give the positive frozen-field curvature `2 lambda_H ||Lambda'(Phi_0)||_F^2`. That is not the curvature after field relaxation. At a matching point the Hessian blocks are

```text
E_PhiPhi = 2 lambda_H ||Lambda'||_F^2,
E_HH = 2 lambda_H I,       E_HPhi = -2 lambda_H Lambda'.
```

Eliminating `H` subtracts `E_PhiH (E_HH)^(-1) E_HPhi`, exactly the same positive number. The relaxed curvature is zero. The numerical check at the illustrative `Phi_0=0.5`, `t=lambda_H=1` gives `0.0383571613144-0.0383571613144=0`. This explains why a nonzero off-shell norm does not establish on-shell phase selection.

### 8.4 The Full Source Action Has Other Compensator Forces

The source also inserts `H` into `D_mu` and `Omega`, so varying only `U_HC` is not varying the complete action. Hold `M,P,T,n_mu,Gamma^mu` and the couplings fixed for this partial variation; use a constant Hilbert-Schmidt comparison and admissible Hermitian `delta H`. Then

```text
delta_H D_mu = kappa n_mu delta H,       delta_H Omega = gamma delta H,
delta_H F_mu_nu
 = D_mu^ad(kappa n_nu delta H)-D_nu^ad(kappa n_mu delta H).
```

Here `D_mu^ad X = partial_mu X+[connection_mu,X]`. Trace cyclicity and integration by parts with vanishing boundary variation give the formal first variation

```text
delta_H S = integral {
    bar(Psi) (i kappa Gamma.n-gamma) delta H Psi
  + kappa n_nu Tr[(D_mu^ad F^{mu nu}) delta H]
  - 2 lambda_H Re Tr[(H-Lambda)* delta H]
}.
```

For a real action on Hermitian fields, take the real functional and its Hermitian projection. The displayed derivative does not assume that the unusual native connection is already a unitary Lorentzian field theory or that its static energy is positive. If `T` is later made a function of `H`, or the comparison varies with `H`, its chain-rule terms must also be retained.

Define `J_S` as the Hermitian Riesz representative of the first two terms on this finite real variation space. Stationarity requires

```text
2 lambda_H (H-Lambda) = J_S.
```

Therefore `H=Lambda` can be a full stationary field only when those other forces cancel, `J_S=0`, or an independently justified constraint removes these variations. The inherited assertion that the displayed action has *exactly* the stated closure equation is too strong without this check. This is a specific variational gap, not merely a missing numerical coefficient. If `H=Lambda` is a definition imposed before variation instead, the penalty is zero identically and the remaining action must be varied with that substitution; it is not a separate phase potential.

There is a nonempty class with no such force: constant `M,P,H`, `Psi=0`, `A_mu=0` and constant `n_mu` give connection matrices `n_mu (kappa H+eta P_perp)`, all proportional to the same matrix. Their curvature vanishes. All three displayed source currents vanish as well. Within the displayed local action this leaves no compensator phase potential. It is a restricted classical configuration, not a claim about fluctuations, boundary holonomy, or every possible native background; exact closure additionally requires the vanishing mixed blocks noted above.

### 8.5 An Explicit Remaining Source-Dependent Equation

One can go further without inventing `R0,R1`. In a licensed static positive reduction, let the rest of the energy be linear in `H` with a fixed Hermitian source `J`:

```text
E(H,Phi)=lambda_H ||H-Lambda(Phi)||_F^2+<J,H>,
<X,Y>=Re Tr(X*Y).
```

`J` is the derivative of the *energy*, not a sign-identification with the Lorentzian action source `J_S`. This reduction is conditional: connection curvature may generate nonlinear/derivative dependence, and a state solved simultaneously with `H` need not give a fixed `J`. For unconstrained Hermitian variations, or an interior minimum of an imposed positive cone, completing the square gives exactly

```text
H_star=Lambda-J/(2 lambda_H),
R_star=-J/(2 lambda_H),
E_eff(Phi)=<J,Lambda(Phi)>-||J||_F^2/(4 lambda_H).
```

If `H_star` violates an additional positivity constraint, this unconstrained formula is not that constrained solution. No indefinite test field is promoted to a physical state.

For the conditional cyclic bridge, set `J_sum=J_11+J_22` from the two diagonal three-generation blocks, and `j=Tr(J_sum U)`. Direct substitution now yields a concrete phase force:

```text
E_eff = constant+2t Re[j (2ar exp(i theta)+r^2 exp(-2i theta))],
dE_eff/dPhi = -(4t/3) Im[j (ar exp(i theta)-r^2 exp(-2i theta))].
```

Thus, when these are the only forces, the equation to solve is

```text
Im[j (ar exp(i theta)-r^2 exp(-2i theta))] = 0.
```

This is not another fitted harmonic coefficient: it exposes the particular matrix element of the probe/curvature source that must be evaluated. With generation-isotropic blocks, `j=0` and no phase is selected. Even a diagonal but generation-dependent `J_sum` gives `j=0` in this cyclic chart; an off-diagonal source coherence relative to the cycle is needed for this term. If `J` depends on phase, its derivatives and the rest of the energy must be restored.

An additional fixed generation tensor also fixes relative orientation. The expression is on the declared local `theta` branch, not a function of an isolated loop phase on the whole circle with all backgrounds forgotten. Simultaneous transport of `J` and `Lambda` preserves their trace pairing. This does not contradict the spectral-polynomial obstruction for a single tensor without a generation background.

The native probe state/current and its allowed variation are still unevaluated. Consequently this derivation does not determine the angle, the radial normalization or the absolute mass scales. It does identify precisely why the minimal HC penalty cannot supply them alone and which existing non-penalty fields could contribute without fitting a new potential to the masses.

The subsequent [source/backreaction follow-up](HC_Source_Backreaction.md) evaluates the spin partial-trace source and a self-consistent cyclic conservation test. It also solves the previously excluded positive-cone case: an independently varied positive compensator can have a fixed-radius phase-selecting constraint reaction even with a symmetric population. That is a different completion, not an exception to the zero on `H_C=Lambda` or to the unconstrained isotropic-source calculation above. Its selected compensator is rank one, and its source/penalty ratio remains an input. Releasing the radius gives an explicit energy descent; releasing the amplitude at fixed source gives a zero-scale endpoint unless other native forces or constraints support it. The deeper-compensator hypothesis does not supply that support or the missing readout by itself.

## Reproduction and Tests

Run `python -B analysis/Phase_Selection_Derivation.py --output analysis/Phase_Selection_Derivation.json`. This report is separate from the earlier coupling-candidate report and labels the illustrative residual, source assumptions and historical target condition separately.

The 48 tests in `scripts/qsc_audit/tests/test_phase_selection_derivation.py` cover spectral invariants/chambers, trace harmonics, conditional minimization and curvature, phase-blind and boundary cases, comparison covariance and derivatives, coefficient/dimension guards, absence of historical-mass inputs from the selection functions, the trimer derivative, fixed-background probe examples and saved-report reproduction. Twenty-two added checks evaluate the native functional on general non-Hermitian blocks, exact closure and the conditional cyclic bridge; distinguish matrix from spectral harmonics; verify frozen/isotropic and relaxed behavior, Hessian cancellation, source elimination, joint unitary covariance and its explicit phase force; and reject incompatible carrier/source inputs. A finite constant-connection check also verifies the curvature contribution to the first variation; it does not establish the native Lorentzian dynamics. These are finite checks supporting the arguments, not a native physical prediction or a formal proof-assistant certificate. No package was installed, and no LaTeX source was changed for this follow-up.
