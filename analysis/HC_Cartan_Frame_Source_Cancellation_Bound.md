# Frame-source cancellation in the Cartan comparison

## Scope

This sidecar concerns only the added neutral commuting-spinor odd-cross
Einstein-Cartan comparison. It does not identify the native HC/C7 sector.
The existing field polynomial, equations and nonzero low-order defects are
preserved. Main TeX and PDF are unchanged.

## Structural derivation

Write E for the coframe matrix, A=E^-1 and v for its positive volume.
The preceding sidecar checks every quadratic coefficient in

    H(A,v) = v (A^T tensor I6)^T H0 (A^T tensor I6).

The source has an additional exact coefficient identity. With p=(mu,l),
l=0,...,5, all 16 coordinate blocks satisfy

    F_(mu,l),a,m,i,j = delta_(m,mu) Fflat_l,a,i,j.

The check is equality of every stored coefficient, not a sampled or
tolerance-based fit. Define real bilinears

    T_l,a = Re sum_u,i,j conjugate(psi_u,i) Fflat_l,a,i,j psi_u,j,
    U_l,a = Re sum_u,i,j conjugate(psi_u,i) Fflat_l,a,i,j (Q psi)_u,j.

Then the original right side, including its multiplier response, is

    f_(mu,l) = -v sum_a A_mu,a T_l,a - sum_a lambda_a,mu U_l,a.

Multiplying by E tensor I6 before taking norms gives

    [(E tensor I6) f]_r,l
      = -v T_l,r - sum_a (lambda E^T)_a,r U_l,a,

because sum_mu E_r,mu A_mu,a=delta_r,a. Consequently

    k = -(E^T tensor I6) H0^-1
        vec[T^T + v^-1 (lambda E^T)^T U^T].

Vectorization is coordinate-major with six Lorentz channels per coordinate.
The minus sign includes both the original source and the response sign.
The first term has no inverse coframe or volume left inside the source.
The external coframe factor remains variable, as do all factors of the
multiplier term. This is an off-shell algebraic identity on invertible
coframes with positive volume, not a new field equation or approximation.

## Derivatives and controls

The regrouped expression is evaluated as a value model with four separately
controlled physical derivative models. No derivative of an unknown value
tail is taken. Variable coframe, spinor, volume and multiplier contributions,
including all cross terms and discarded higher-degree products, remain.

For an identically zero multiplier jet the Cartan correction is independent
of volume at fixed coframe and spinor. A zero multiplier *value* does not
remove its nonzero derivatives: the differentiated multiplier channel still
contains 1/v. Tests distinguish these cases. The positive-volume domain
guard is retained even when the multiplier jet is zero.

Controls compare arbitrary off-shell sources and all four derivatives to
the previous unreduced source formula, uncertain inputs to perturbed direct
evaluations, and the complete connection to the original independent
connection evaluator. Saved sample checks cover axes, corners and an
interior point; those samples are not the proof of the support identity.

## Recomputed enclosures

| Whole-cube estimate | r=1/16384 | r=1/32768 |
|---|---:|---:|
| Previous combined 80 rows | 0.001772711744 | 0.00005484954722 |
| Source-cancelled combined | 0.001064593063 | 0.00003293248451 |
| Constraint tail | 0.00002293896912 | See saved JSON |
| Probe tail | 0.00005193832923 | See saved JSON |
| Coframe tail | 0.0003943999256 | 0.00001226850596 |
| Curl tail | 0.0009872088613 | 0.00003051048163 |

Combined upper estimates improve by about 40 percent at both radii.
Connection value-tail bounds approximately halve, while derivative-tail
bounds decrease by factors about 3.2 to 3.5. Retained 80-row coefficient
arrays differ from the parent only by about 6.8e-15 in Frobenius norm from
floating-point regrouping. Nonzero degree-three/four defects remain.

These binary64 majorants are still much larger than the sampled residuals.
The exact coefficient support check and inherited fixed-Hessian certificate
do not make the surrounding nonlinear computation outward-rounded. No
exact low-order closure, regional compatibility, convergent PDE solution,
distance-to-solution bound or physical identification follows.

## Reproduction

Run `python -B analysis/HC_Cartan_Frame_Source_Cancellation_Bound.py`, then
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_frame_source_cancellation_bound`.
The JSON records predecessor/source fingerprints, complete retained
coefficients, diagnostics, and original-equation sample controls. The two
radius calculations use at most two local workers with separate caches.
