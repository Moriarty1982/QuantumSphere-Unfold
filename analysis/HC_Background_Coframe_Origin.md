# Can the Background Coframe Be Obtained From the Paper?

Date: 2026-10-16. Status: source-backed conditional constructions, an exact background expansion and a coupled reference-Dirac existence example. This does not establish the native background state, adopt a new geometric readout or solve the full native Einstein/gauge/closure system.

## Result

**There is a better-supported candidate than an unexplained external identity matrix:** the paper already contains distinct ART/QFT probe readouts, a third intrinsic coupling channel, and cross-bilinear geometry. Their evaluation on a reference solution can supply a local background coframe. A concrete Hermitian three-channel example below has a nondegenerate ART coframe and, on a later local patch, nondegenerate ART/QFT cross-coframes.

There is also an exact way for a background term to arise from the existing bilinear: expand the same field around a nonzero reference state. However, the expansion contains linear cross terms and connection variations. It is not generally just `theta+C[phi]`, and changing the expansion point does not remove the full-field trace obstruction.

The distinction is decisive. A channel or cross-readout background is supported by the paper's **hypothesis-grade two-probe geometry**, not already identified with its full closed-triadic coframe. In the explicit example the full coframe is actually degenerate at the origin. This is an existence comparison for the proposed readout interface, not a repaired native Einstein theorem.

## 1. What Is Actually Prepared in the Source?

| Source | Existing object | What it supplies, and what it does not |
| --- | --- | --- |
| `10_sphaera_and_physics.tex`, `def:biquaternion` | Displayed time/spatial quadratic expression | A kinematic comparison after a real spacetime slice and coordinate map are declared; no evaluated rank-four coframe field |
| Same file, `prop:bilinear-einstein-reconstruction` | `E=Re(bar(Psi_triangle) Gamma D Psi_triangle)` | The total triadic reconstruction with maximal rank assumed; no explicit additive background |
| `12_structural_core.tex`, `hyp:bidirectional-probe-lensing` and its trace observables | ART/QFT probes, an intrinsic `Psi_perp` channel, relative phase and both cross-bilinears | The strongest prepared route to a regime-relative reference geometry; its universal lensing law remains hypothetical |
| `16_master_model.tex`, `eq:toe_master_semiconcrete` | Inter-sector couplings `Lambda_ab` | Named coupling slots, not numerical matrix elements or a selected background solution |
| `36_frame_typed_endpoint.tex`, `subsec:r81-photon-frame-null-note` | Photon/clock candidate null object | A typed boundary readout, not a rank-four spacetime reference or an exact all-readout zero |

All are retained native sources, not instructions to execute or theorem certificates. The example below uses their conditional Dirac/coupling pattern; its finite carrier and numerical data have not been extracted from the native C7/M16 operators.

## 2. The Exact Background Expansion

For a fixed adjoint and frame weights write

```text
C[Psi,D]^a_mu=s Re(bar(Psi) Gamma^a D_mu Psi),
Psi=Psi0+phi,       D=D0+delta B,
theta=C[Psi0,D0].
```

Direct expansion gives the identity

```text
E=theta
  +s Re[bar(Psi0) Gamma D0 phi+bar(phi) Gamma D0 Psi0]
  +C[phi,D0]
  +s Re[(bar(Psi0)+bar(phi)) Gamma delta B (Psi0+phi)].    (1)
```

**Proof.** Distribute the linear operator `D0` and the connection variation through the sum, then distribute both occurrences of the field in the bilinear. Taking the real part is real-linear. No dynamical equation or approximation is used.

Thus a background is not necessarily a new independent geometric object: it can be an existing bilinear evaluated at a reference state. But the correction in the exact affine expression `E=theta+delta E` is the **whole remainder in (1)**, not the old quadratic formula applied to `phi` alone. In the report's unfitted sample, ignoring the linear cross term gives an error norm about `0.14004`, while the complete expansion agrees within `2.6e-16`.

At fixed connection an average of `phi` and `-phi` cancels the linear cross term exactly. Correlated sign-changing connection fluctuations need not cancel: terms with both `delta B` and `phi` are even under that change. A genuine coarse-graining needs its correlation rules and common comparison, not just a zero-mean label. Varying adjoints, gamma matrices or projector data introduces their further variations; (1) does not silently freeze them in a native claim.

Most importantly, if this is merely a decomposition of the same full native coframe and the same induced-frame ordered equation, the [previous trace identity](HC_Bilinear_Geometry_Bridge.md) still applies to the total field. Writing its terms differently cannot evade it.

## 3. A Channel Can Exchange Charge Without an Imaginary Total Mass

In a declared factorization let `P` be a constant internal Hermitian projector commuting with the spin weights, not automatically the native closure projector. For a reference-frame on-shell equation define

```text
theta_P^a_mu=s Re(bar(Psi) P Gamma^a D_mu Psi),
w_P=bar(Psi) P Omega Psi,
Gamma_ref^mu=(theta_ref^(-1))^mu_a Gamma^a.
```

The projected trace and current identities are

```text
Tr(theta_P theta_ref^(-1))/s=Im w_P,
partial_mu j_P^mu=2 Im w_P,       j_P^mu=bar(Psi)P Gamma_ref^mu Psi.      (2)
```

Here the current formula assumes the fixed constant kinetic weights and ordinary reference connection of the example. Moving projectors, frame weights or other connection terms need their own derivatives and reactions.

Even if the full mass bilinear is real, a channel bilinear need not be. With a Hermitian internal `Omega` and the declared spin adjoint,

```text
Im w_P=bar(Psi)[P,Omega]Psi/(2i).                         (3)
```

**Proof.** The conjugate of `bar(Psi)P Omega Psi` is `bar(Psi)Omega P Psi` under these weighted-adjoint and commutation assumptions. Subtraction proves (3). Multiplication of the on-shell reference equation by `bar(Psi)P`, followed by its imaginary part, proves the first line of (2); differentiating the Hermitian current proves the second.

This is an ordinary Hermitian channel-exchange mechanism, not an invented imaginary eigenmass. Summing over a complete set of internal channel projectors gives zero net exchange because their sum commutes with `Omega`. If `[P,Omega]=0`, the exchange vanishes. Zero trace alone need not make a reference-frame coframe degenerate; it only prevents the unchanged identity-like trace under that fixed comparison.

The ART subprojector must not be identified with `P_C7`. An interacting regime channel and the full closure-stable carrier have different roles. Neither (2) nor (3) proves the native C7 embedding or its exact closure.

## 4. An Exact Coupled Background, Not Just a First Jet

Use the same declared four-spinor matrices as the preceding audits:

```text
beta=diag(1,1,-1,-1),       K^a=(I,alpha_i),
Gamma^a=beta K^a,          {Gamma^a,Gamma^b}=-2 eta^{ab}I.
```

Take three internal modes ordered as `(ART,QFT,perp)` and a constant real Hermitian mass/coupling matrix

```text
Omega = [[m, 0, g_A],
         [0, m, g_Q],
         [g_A, g_Q, m]],
m=0.6,       g_A=4,       g_Q=0.7.                       (4)
```

There is no direct ART/QFT matrix entry: their interaction uses the already prepared orthogonal channel. The chosen numbers are dimensionless existence-test inputs, not native predictions, calibrated particle masses or derived physical coupling strengths.

The reference equations are

```text
(i Gamma^mu partial_mu-Omega)Psi=0,
partial_t Psi=-alpha_i partial_i Psi-i H Psi,
H=Omega tensor beta.                                    (5)
```

`H` is Hermitian in the positive reference time norm. These equations follow from the common real free coupled-probe action in this finite realization. They are a conditional probe subsystem, not the entire native action with gauge, projector and gravity equations.

Choose affine-spatial initial data `Psi(0,x)=A0+sum_i B_i0 x_i`. With `e1=(1,0,0,0)` and

```text
A0_ART=e1,        A0_QFT=0,        A0_perp=i e1,
(B_x0,B_y0,B_z0)_ART=((0,0,0,1),(0,0,0,i),(0,0,1,0)),
B_i0,QFT=0,       B_i0,perp=-i B_i0,ART.                 (6)
```

An exact solution exists in this polynomial class. Let `Alpha_i=I3 tensor alpha_i`,

```text
U(t)=exp(-i H t),       J(t)=integral_0^t exp(-2i H s) ds,
B_i(t)=U(t)B_i0,
A(t)=U(t)[A0-sum_i Alpha_i J(t)B_i0],
Psi(t,x)=A(t)+sum_i B_i(t)x_i.                           (7)
```

**Proof.** Since `{H,Alpha_i}=0`, one has `U^(-1)Alpha_i U=Alpha_i exp(-2iHt)`. Differentiating (7) gives `Bdot_i=-i H B_i` and `Adot=-i H A-sum_i Alpha_i B_i`, exactly the constant and spatial coefficients of (5). The spectral formula for `J` uses `t exp(-i lambda t) sinc(lambda t/pi)` on each eigenvalue and is regular also for zero modes. Finite-difference tests independently verify all four coordinate derivatives.

This solves the reference equation on a neighborhood, not just at a chosen point. The spatial polynomial is not a normalizable whole-space ground state, and the native theory has not selected these initial data. It is used as a local classical background witness.

At the origin the channel coframes and current divergences are

```text
theta_ART=I4,       E_QFT=0,       E_perp=-I4,
Im(w_ART,w_QFT,w_perp)=(4,0,-4),
div(j_ART,j_QFT,j_perp)=(8,0,-8),       div j_total=0.     (8)
```

The reference residual norm is about `9.8e-16`. Nearby at `(x,y,z)=(0.02,-0.03,0.01)`, the ART determinants at times `(-0.01,0,0.01)` are approximately `(0.9782772,0.9986,0.9755920)`. Thus a continuous open patch has a genuine rank-four ART coframe. It was evaluated from a field solving a massive, Hermitian coupled equation, not inserted externally.

For fixed frame weights and zero HC transport,

```text
theta_ART^a_mu=partial_mu j_ART^a/2.
```

Consequently `Y_ART^a=j_ART^a/2` are local coordinates wherever this coframe is invertible; its metric is locally flat. This supplies a reference-background candidate, not new gravitational curvature. Its nonconserved channel current has an explicit compensating mediator exchange. It is not the conserved current of an isolated ART theory.

The phase dependence is explicit. Replacing the initial mediator phase by `exp(i phi)` gives at the origin

```text
Tr theta_ART=g_A sin(phi),
(theta_ART)^0_0=g_A sin(phi)-3.                          (9)
```

The `3` counts the specifically chosen spatial initial gradients. This is not a universal numerical threshold or a prediction for the paper's physical frame offset. It demonstrates how an allowed relative phase can change the background readout through a real coupling. The bare real mass changes the evolution but not this instantaneous exchange.

## 5. The Already Written ART/QFT Cross-Bilinear Also Works Locally

The native lensing section explicitly introduces both orientations

```text
E_AQ^a_mu=Re(bar(Psi_ART)Gamma^a partial_mu Psi_QFT),
E_QA^a_mu=Re(bar(Psi_QFT)Gamma^a partial_mu Psi_ART).
```

Using the same exact solution (7), at `(t,x,y,z)=(0.01,0.02,-0.03,0.01)` gives

```text
rank E_AQ                 = 4
det E_AQ                  = 2.2444615514533138e-7
rank [(E_AQ+E_QA)/2]      = 4
det [(E_AQ+E_QA)/2]       = 1.1833827329851391e-7.         (10)
```

These determinants are coordinate/normalization diagnostics, not invariant gravitational strengths. Nonzero determinants prove nondegeneracy on some open neighborhood of that sample. At the origin these cross-readouts are instead degenerate; rank must not be asserted globally. Switching off the QFT/mediator coupling in these initial data makes both cross-readouts disappear.

The bidirectionally symmetric candidate has an exact background-coordinate interpretation:

```text
theta_cross=(E_AQ+E_QA)/2
            =partial_mu Re(Psi_ART^dagger K^a Psi_QFT)/2. (11)
```

**Proof.** Differentiate the real cross bilinear. Hermiticity of `K^a` turns the derivative acting on `Psi_ART^dagger` into the exchanged orientation. The two terms are precisely `E_QA` and `E_AQ`.

When nondegenerate, (11) is another locally flat reference coframe obtained from the already proposed cross-readout. Symmetrizing it is a stated candidate choice, not a unique native prescription. The ordered cross-readout need not be exact in this way; its curvature and action are not computed here.

This is the strongest source-based answer to the background question so far: the required four one-forms can be constructed from the prepared coupled probe observables. It still needs a physical selection rule for this background state, normalization and readout, and a common action for its gravitational use.

## 6. Why This Does Not Silently Solve the Original Reconstruction

The full inherited coframe remains the sum of the channel coframes. In (8),

```text
E_total=theta_ART+E_QFT+E_perp=0.
```

Thus the full native reconstruction is degenerate at the origin even though the selected background is nondegenerate. The distinction is demonstrated rather than assumed away. Moreover the reference gamma matrices in (5) are not identified with the inverse selected coframe throughout the patch. The [same-frame obstruction](HC_Bilinear_Geometry_Bridge.md) is unchanged.

If the full field is expanded around this background, all of (1) must be retained. If geometry is instead defined by a regime/cross-readout, that is an explicit development of the paper's hypothesis-grade two-probe route, not a proof that the old full-field coframe has acquired an additive identity term.

Nor can the locally flat coframe simply be changed to `I` by using `Y` coordinates while leaving the old microscopic kinetic operator unchanged. Coordinate changes also transport the reference gamma matrices, derivatives, volume and background/current data. The separate neutral HC metric family from the [two-frame action bridge](HC_Two_Frame_Action_Bridge.md) therefore cannot be glued to this interacting background without redoing their common variation.

If `theta=theta[Psi0]` is used in a multiplier parent, `Psi0` must be varied or explicitly justified as frozen. For example its background equation gains the variational reaction `-(D_Psi0 theta)^*lambda`, together with the derivatives of the fluctuation remainder. Deriving a background from fields creates these equations; it does not eliminate them. Gauge Gauss sources, the native closure projector, the represented triadic operator, stability and the scale transfer remain unsolved here.

## 7. Why the Other Anchors Are Weaker

The displayed kernel expression uses three complex spatial coefficients. If treated as independent, its polarized real quadratic form has one negative and six positive directions. A declared three-real-dimensional spatial slice, such as `z_i=exp(i alpha_i)X_i` with fixed phases, gives the desired `(1,3)` comparison. The source still needs the slice/readout map and its rank; this calculation does not validate the inherited quaternion conjugation or automatic Lorentz-group claims. It is not a derivation of the affine term from the algebra alone.

Likewise an internal Hopf `S3` provides potential spatial forms only after an explicit map to physical spacetime. Adding a clock form, independence, scale and a metric/dynamical interpretation is further input. A single photon-clock one-form or null axis has rank at most one and cannot by itself supply four independent coframe forms. The later photon-clock/non-promotion guards remain in force.

## 8. Verification and Next Native Obligation

`python -B analysis/HC_Background_Coframe_Origin.py --output analysis/HC_Background_Coframe_Origin.json` reproduces the report. The 44 focused tests check source anchors, exact background expansion and correlations, Hermitian mediator dynamics and all reference Dirac components, finite-difference derivatives, channel/global balances, projector covariance, local ranks, cross-readout activation and gradient coordinates, plus negative controls for the full original coframe and the kinematic/clock candidates. These are written algebraic proofs and finite numerical regressions, not a proof-assistant or empirical certificate.

The next native obligation is now more specific: choose whether the geometric reference is a background evaluation of the full field or a regime/cross-readout; represent its actual C7/triadic couplings; select a background state; and vary that choice with the remaining fields in one common action. The present calculation supplies a source-backed existence construction, not that selection or the full native solution. The main TeX/PDF remain unchanged by this analysis.

The subsequent [derived-background curved parent](HC_Derived_Background_Curved_Parent.md) performs that common variation in an explicit neutral comparison. An auxiliary scalar potential retains the probe-dependent axis equation; its divergence vanishes on the pulled-back null branch without discarding a nonzero independent-axis reaction. The exact coupled reference probe and curved scalar geometry solve all equations of that declared parent. Separate positive-HC/current-span and microscopic/effective null-cone tests then obstruct its unchanged native fixed-axis/current/transport identification; a uniform bound shows that rotating only the background-null update axis cannot restore the reference-null dark mechanism on the selected cross-readout patch. The reference probe does not gravitate through the effective metric in this comparison action; native gauge/closure/universal coupling remain unresolved. Forty-six tests cover this step without adopting it into the main paper.
