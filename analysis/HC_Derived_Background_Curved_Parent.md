# A Curved Joint Branch With a Probe-Derived Background

Date: 2026-10-16. Status: full variation and an exact local branch of a declared neutral derived-readout parent; a separate fixed-axis obstruction to identifying its deformation with the native HC current. This is not a solution of the full native action or an adopted main-paper correction.

## Result and Scope

The [derived ART/QFT reference coordinates](HC_Background_Coframe_Origin.md) and the [curved neutral HC profile](HC_Two_Frame_Action_Bridge.md) can be joined in one explicit action. The background and null potential are varied rather than frozen. The coupled massive reference-Dirac probe, independent metric/coframe equation, both scalar equations and both constraints have a common local solution.

The additional axis-potential equation is the crucial check. On the transverse null branch it vanishes by a divergence identity, even though a freely varied independent axis would have a nonzero reaction. The latter equation is not silently discarded: the model declares an exact scalar-derived axis `n=du` and includes its full allowed variations.

**This remains a comparison model.** Its probe kinetic action uses a fixed microscopic reference metric, not the effective gravitational metric. The probe's mass energy therefore does not source that effective Einstein equation in this action. The neutral scalar deformation is an added constitutive choice, not an evaluated native HC matrix. The native charged gauge, projector, Yukawa and matching sectors are not present. The result is neither universal gravitational coupling nor a solution of the original paper.

Trying the unchanged native HC bilinear then reaches a definite boundary: for the previous probe family on a generic sample patch, the required fixed null direction is outside even the linear span of its Hermitian internal current readouts. Positivity gives a particularly simple exclusion bound. More coefficient fitting in that fixed direction cannot solve this identification; the probe, axis or readout must change.

## 1. Keep the Background and Axis Equations

Use the exact three-channel reference-Dirac solution of the background audit, with Hermitian internal mass/coupling matrix and fixed spin weights. Define the prepared symmetric cross-readout coordinates

```text
Y^a[Psi]=Re(Psi_ART^dagger K^a Psi_QFT)/2,
Theta^a_mu=partial_mu Y^a,
U[Psi]=n_a Y^a,
n_a=(-1,0,0,1),       l^a=eta^{ab}n_b=(1,0,0,1).         (1)
```

Restrict to a patch where `Theta` is invertible. The ART current coordinates can also be tested, but are a different declared readout. Neither is identified with the original full-field coframe, which remains subject to the earlier trace obstruction.

Take independent fields `Psi,E,h,u,lambda,zeta`, with real nonsingular coframe `E`, real scalars `h,u`, real multiplier density `lambda_a^mu` and real scalar density `zeta`. The common parent is

```text
S = S_D,reference[Psi]
  + integral d^4x sqrt|g(E)| [R(g)/(2 kappa_eff)-F_mu_nu F^mu_nu/4]
  + integral d^4x lambda_a^mu(E^a_mu-Theta^a_mu[Psi]-kappa h l^a partial_mu u)
  + integral d^4x zeta(u-U[Psi]),

g=E^T eta E,       F=kappa dh wedge du.                  (2)
```

`S_D,reference` is the real symmetric massive triadic action already solved in the fixed microscopic Cartesian reference chart. It is not silently changed into an induced-frame Dirac action. The geometric sector is evaluated on that same spacetime through the functional map `Y[Psi]`; simply keeping old gammas after a coordinate substitution is not the argument.

The scalar two-form in (2) is neutral and parameterized by two scalar potentials. It is not an independently varied matrix gauge connection. `kappa_eff`, the null update and the choice of cross-readout remain explicit inputs. Compactly supported variations in the nondegenerate patch are assumed; no boundary term at infinity or global solution is asserted.

## 2. Vary Before Substituting the Null Profile

Let `pi_E=delta S_geom/delta E`. With the convention `EL=partial L/partial field-partial_mu(partial L/partial field_mu)`, all independent equations are

```text
pi_E+lambda=0,
E-Theta-kappa h l du=0,
u-U[Psi]=0,

EL_h,F-kappa lambda_a^mu l^a partial_mu u=0,
EL_u,F+kappa partial_mu(h lambda_a^mu l^a)+zeta=0,

EL_D+(DY)^* W=0,
W_a=partial_mu lambda_a^mu-zeta n_a.                    (3)
```

The last equation includes the real/complex variational derivative of the readout. Its sign follows by integrating `-lambda_a^mu partial_mu delta Y^a` by parts. For the symmetric cross-readout its Wirtinger sources are

```text
R_ART,readout=(W_a K^a Psi_QFT)/4,
R_QFT,readout=(W_a K^a Psi_ART)/4,
R_perp,readout=0.                                       (4)
```

These sources need not vanish off shell. Periodic parent-action variations and independent probe variations verify their signs and factors. The auxiliary potential constraint in (3) retains the entire reaction of the probe-dependent null axis; it is not equivalent to prescribing `n` externally.

Put `p_mu=partial_mu h`, `q_mu=partial_mu u`. Varying the scalar action gives

```text
EL_h,F=kappa div_mu(F^{mu nu}q_nu),
EL_u,F=kappa div_nu(F^{mu nu}p_mu).                      (5)
```

**Proof.** In the `h` variation, `delta F_mu_nu=kappa[(partial_mu delta h)q_nu-q_mu(partial_nu delta h)]`. Antisymmetry gives `delta L=-kappa F^{mu nu}q_nu partial_mu delta h`; integration by parts proves the first equation. The `u` variation instead gives `delta L=-kappa F^{mu nu}p_mu partial_nu delta u`, proving the second. Both divergences include the metric volume and raised-index derivatives.

For comparison, if an arbitrary covector `q` were independently varied in `F=kappa dh wedge q`, its algebraic reaction would be

```text
J_q^nu=-kappa F^{mu nu}p_mu.                            (6)
```

The actual scalar-potential equation is `EL_u=-div J_q`, not `J_q=0`. Changing the allowed axis field space changes the theory. Both scalar equations have been checked against independent off-null periodic variations with a varying metric density, so their vanishing below is a property of the branch rather than an identity accidentally built into the test.

## 3. The Common Local Branch

Choose any nondegenerate patch of the exact coupled reference probe from the previous audit and set

```text
u=n_a Y^a[Psi],
h=log(F0+b_1 Y^1+b_2 Y^2)/a,
a=kappa_eff kappa != 0,       F0+b_1 Y^1+b_2 Y^2>0,

E=(I+kappa h l n^T)Theta,
lambda=0,       zeta=0.                                 (7)
```

For the displayed numerical example `kappa=0.4`, `kappa_eff=1`, `F0=2`, `b=(0.1,0)`. These are dimensionless test inputs, not native physical scales. Positivity of `h` can be required on a smaller patch. The underlying probe has real bare mass `0.6` and Hermitian mediator couplings `4` and `0.7`; it is no longer the constant massless probe of the earlier neutral example.

**Constraints.** Since `du=n_a dY^a`, both constraints in (3) hold identically. In `Y` coordinates,

```text
g_Y=eta+2 kappa h n n^T,
g_x=Theta^T g_Y Theta,
det E=det Theta != 0.                                   (8)
```

This is an exact pullback, not the addition of metric components in incompatible frames. The auxiliary field `u` remains independently varied in (3); (7) is substituted only afterward.

**Independent metric/coframe equation.** In the `Y` chart the old null-geometry calculation gives

```text
G_ab=-kappa Delta_perp h n_a n_b,
T_ab=kappa^2 |grad_perp h|^2 n_a n_b.
```

The logarithm of a positive affine harmonic function obeys `Delta_perp h+kappa_eff kappa |grad_perp h|^2=0`, hence `G=kappa_eff T`. Pullback preserves the full tensor equation. Therefore `pi_E=0`, and the coframe equation holds with `lambda=0`. This is stronger than a null contraction or a restricted-action equation.

**Both scalar equations.** The covector `q=du` is null and parallel in this transverse null metric; `q.p=0` and `q.partial h=0`. Thus

```text
kappa F^{mu nu}q_nu=0,
kappa F^{mu nu}p_mu=kappa^2 p^2 q^nu,
div_nu(p^2 q^nu)=0.                                    (9)
```

The first identity solves the `h` equation. The last identity, using transverse `p^2` and parallel `q`, solves the additional `u` equation. Crucially the middle expression is generally **not zero**. The axis reaction was retained and has vanishing divergence on this branch; it was not set to zero by ignoring a field variation.

**Probe equations.** Equations (7) and (9) permit `lambda=zeta=0`, so `W=0` and the additional sources (4) vanish. The exact reference-Dirac probe therefore remains on shell. This is a branch-specific absence of the computed backreaction, not a general assertion that probes never react to the new geometry.

**Current.** `Y[Psi]` is invariant under a common local phase applied to all three probes. So are `Theta` and `U`. These couplings supply no extra common-phase current; the conserved total current is the original reference current. Channel exchange remains balanced as in the background audit. No induced-frame probability current is substituted for it.

Every field equation of the declared parent has now been checked. No native Gauss/projector/HC-matrix equation has thereby been added or solved.

## 4. Independent Numerical Checks in the Original Coordinates

The code differentiates the exact probe analytically through third order, applies the full product rule to `Y[Psi]`, and builds the metric's first and second `x` derivatives. It computes the Levi--Civita curvature from those jets independently of the tensor pullback. Scalar equations include derivatives of the inverse metric, density and **both** scalar gradients.

At the nondegenerate cross-readout sample `(t,x,y,z)=(0.01,0.02,-0.03,0.01)`:

```text
Y=(0.00346628412144,0.00014303861126,-0.00020902420873,0.00007024229605)
h                                      = 1.7328858311623325
reference probe residual norm          = 1.38e-15
coframe constraint norm                = 0
h Euler residual                       = -2.98e-16
u Euler residual                       = 0
independent-axis reaction norm         = 0.34970098783011605
direct Einstein component residual     = 1.05e-11
coframe Euler density residual norm    = 4.95e-15
direct/pullback stress difference       = 8.85e-22
```

The exact identities prove the local branch; these numbers check its implementation. The larger direct-curvature residual matches the independent Levi--Civita versus pullback error. The cross-coordinate frame is near its initially degenerate slice, so connection/metric-jet arithmetic contains amplified cancellations. These are dimensionless coordinate diagnostics, not invariant errors, measured energies or native residual norms. The ART-readout variant has direct Einstein residual about `9.16e-13`. Both have nonzero Riemann curvature.

## 5. Attempting the Original Positive HC Identification

The parent assumes the constitutive update `kappa h l du`. To identify this with the original factorized HC coframe term requires an actual positive internal operator such that

```text
v_H^a=Psi^dagger K^a H_C Psi=h l^a,
H_C >= 0,       l=(1,0,0,1).                            (10)
```

This is a separate equation, not a consequence of varying the scalar comparison model.

For the exact probe family, every row lies in the spin space spanned by

```text
e=(1,0,0,0),       f=(0,0,z,x+i y)/r,
r=sqrt(x^2+y^2+z^2).                                   (11)
```

The time evolution preserves this form: the mass Hamiltonian acts internally and by `beta`, while the derivative source contributes only to the upper `e` component. On a generic patch the active row space has dimension two.

On this orthonormal space the Hermitian matrix `K^0-K^3` restricts to

```text
[[1,-z/r],[-z/r,1]],
delta=1-|z|/r.                                         (12)
```

For every positive internal `H_C`, positivity and the restricted operator bound imply

```text
v_H^0-v_H^3 >= delta v_H^0.                             (13)
```

**Proof.** Factor the probe matrix by its singular-value decomposition. Both quadratic forms reduce to positive internal weights on the active spin-row space; the smallest eigenvalue of the matrix in (12) bounds one form by `delta` times its identity/time form. Taking the positive weighted trace proves (13). The code tests independent positive matrices, not just a diagonal HC ansatz.

At the sample `delta=0.7327387580875757`. The desired vector `h l` instead has `v_H^0=h>0` and `v_H^0-v_H^3=0`. It cannot satisfy (13). Thus no positive internal HC matrix can produce this unchanged fixed-axis deformation for these probes on that patch.

There is an even stronger linear obstruction. For every Hermitian internal current weight, including indefinite ones, the available spatial currents obey

```text
z(x v^1+y v^2)-(x^2+y^2)v^3=0.                         (14)
```

**Proof.** The spin space (11) has no diagonal spatial currents. Its off-diagonal matrix element is determined by the single complex product of the two spin coefficients. Its real and imaginary parts span the vectors `(x,y,z)` and `(-y,x,0)`; both obey (14). All real Hermitian internal combinations therefore obey it as well. The target positive `z` null vector does not when `x^2+y^2>0`.

The current-map range has rank three at the sample, and the least-squares residual for the unit target `(1,0,0,1)` is about `0.9636241` even without positivity. This is an exact range restriction, not a failed numerical optimization.

**Boundary of the exclusion.** A different radial spatial axis has zero positivity gap for the same probe row space; a collinear sample can also have zero gap. Changing the probe, spin representation, axis or readout can therefore change the result. A varying axis must have its integrability, curvature profile and all variations recomputed; the plane-null logarithmic solution cannot simply be retained. This is not a no-go theorem for the paper, nonfactorized HC operators or all possible backgrounds.

There is a second, independent frame-compatibility test. The pulled-back covector is null for the effective metric, but at the sample its norm in the fixed microscopic reference metric is `-0.1124202677974469`, not zero. With the declared Clifford convention,

```text
(Gamma_ref^mu q_mu)^2=-(q_mu eta_ref^{mu nu}q_nu)I.
```

The reference slash is invertible, with minimum singular value about `0.3284058`. Consequently the original ordered HC transport cannot annihilate a nonzero `H_C Psi` on this unchanged background/axis: its norm is at least that singular value times `||H_C Psi||`. If `H_C Psi=0`, the original HC current also vanishes. The old transport-dark null-spinor mechanism therefore cannot be imported merely because the **effective** metric calls this axis null. This identifies a missing common gamma/null-cone dictionary; it does not exclude a different, consistently reconstructed microscopic operator or axis.

Rotating only the background-null update axis cannot repair that mismatch at this cross-readout sample. Normalize any such covector as `n=(-1,b)`, `|b|=1`, and pull it back as `q=Theta^T n`. The triangle inequalities give

```text
|q_0| >= t_minus=max(0,|Theta^0_0|-||Theta^{1:3}_0||),
||q_spatial|| <= s_plus=||Theta^0_{1:3}||+||Theta^{1:3}_{1:3}||_op,
q_ref^2 <= -t_minus^2+s_plus^2.                         (15)
```

Here `t_minus=0.3160611602764769` and `s_plus=0.007291408119375868`, so `q_ref^2 <= -0.09984149240294952 < 0` for **every** normalized background-null update direction. This strict bound persists on a sufficiently small neighborhood by continuity. It obstructs importing a reference-null dark-spinor mechanism merely by rotating this update; it does not exclude solving new probe equations with nonzero transport. Its scope is the background-null axes of the rank-one construction, not every null covector of the already deformed effective metric. The identity-coframe negative control has bound zero and no strict separation.

## 6. What Has and Has Not Been Reached

Established in the stated comparison:

- A nonconstant, probe-derived background and a nonzero curved neutral scalar geometry share one local parent-action solution.
- Massive Hermitian triadic probe dynamics and conserved total reference current are retained.
- The background and axis-potential reactions were varied and checked. The actual field space matters: a freely varied covector axis would add an unsatisfied equation.
- The native fixed-axis positive internal HC identification is excluded for the unchanged probe family; even its Hermitian current span misses the target.
- The geometric null axis is not microscopic-reference-null in this example, so the unchanged native ordered transport has no nonzero dark spinor along it. The uniform bound also rules out repairing this mechanism by rotating only the background-null update direction on the selected cross-readout patch.

Not established:

- The native coframe/readout selection, HC transport and Yukawa law, gauge Gauss sources, projector reactions or exact minimal closure. Nonzero scalar `h` is not automatically native `H_C=Lambda`.
- Gravitational coupling of the reference probe's mass energy. `S_D,reference` has no effective-metric variation by definition; calling it ordinary matter minimally coupled to `g(E)` would be a different action and different equations.
- A derived Einstein coupling, equivalence principle, normalizable vacuum, global boundary conditions, stability or well-posedness of the higher-derivative composite theory.
- The old same-frame full-bilinear equation. The selected background dictionary, fixed microscopic reference and added null constitutive update remain explicit changes under investigation.

The next native calculation should therefore establish the common gamma/null-cone and HC/probe/axis dictionaries rather than just fit the scalar coefficient. If the native transport, mass and gauge terms are restored, the probe and geometry must be solved together again. The present exact joint branch is a controlled comparison for that task, not its completion.

## 7. Reproduction

The subsequent [quantum-state source analysis](HC_Quantum_State_Gravity.md) adds an explicitly distinct, metric-coupled scalar carrier. It derives a sourced Helmholtz profile and solves the enlarged neutral parent, while separately constructing a massive one-particle stress difference and its first-order gravitational response. It does not make the existing reference probes gravitate through the effective metric, identify the native HC matrix or preserve the exact null scalar branch after restoring a mass term.

`python -B analysis/HC_Derived_Background_Curved_Parent.py --output analysis/HC_Derived_Background_Curved_Parent.json` reproduces the report. Forty-six focused tests check analytic jets against independent differences, full tensor pullback against Levi--Civita curvature, off-null scalar action variations with a varying density, parent multiplier signs and complex probe factors, every declared branch equation, current conservation, the native HC cone/range obstructions and the microscopic/effective null-cone mismatch, including the uniform background-null-axis bound and negative controls. NumPy is already installed. The written proofs are not replaced by finite tests, and no proof-assistant or empirical certificate is claimed. The main TeX/PDF and frozen v4.7 fragments remain unchanged by this continuation.
