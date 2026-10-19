# First compatibility attribution: prescribed jets and known identities

## Question and scope

The general first-source gate stays injective in the tested samples, yet a
source correction alone leaves a projected first-prolongation residual near
0.00406. This calculation asks which part comes from fixing higher tangential
data and whether the remainder has a known structural origin.

Only the added neutral commuting-spinor odd-cross Einstein--Cartan comparison
is involved. Couplings, lower field data and the six sources are not re-solved.
Main TeX/PDF and the published payload are unchanged. No regional solution,
native HC/C7 identification or uniform rank certificate is claimed.

## Release higher prescribed data, not lower equations

The 272-vector H consists of the four first derivatives of the primary 68
equations. At fixed lower data it is affine in the local psi2, lambda2 and E3
jets. There are 720 real coordinates: 224 previously allowed normal coordinates
and 496 additional prescribed coordinates. Third spinor derivatives cancel.

The full higher response A has numerical rank 220 at the origin and two displaced
points, versus rank 160 with normal higher changes alone. Thus releasing the
prescribed data adds 60 image directions. This does not prescribe 60 physical
modes; it is a rank statement about this coordinate jet map.

## The 52 known compatibility rows

The entire sampled left kernel of A is spanned by three explicit row families:

1. **24 constitutive curl rows.** For all six pairs r<s and four frame indices,
   H(C_{as,r})-H(C_{ar,s}) equals the constitutive curl J_{rs,a} computed from
   lower fields and the eliminated Cartan connection. Symmetric psi2 cancels.
   The 12 temporal-spatial curls are already in the primary equations; the other
   12 are spatial curls.
2. **24 differentiated Lorentz rows.** If L_alpha F0=0 is the established
   off-shell Lorentz identity, then
   L_alpha partial_r F0=-(partial_r L_alpha) F0.
   The right side must be retained when the lower residuals are nonzero.
3. **Four coordinate Ward rows.** The derivative terms satisfy

\[
 \sum_{a,\mu} E^a_\nu\partial_\mu F_{E,a}^{\mu}
 +\lambda_a^{\mu}(\partial_\mu C^a_\nu-\partial_\nu C^a_\mu)
 =-F_{E,a}^{\mu}(\partial_\mu E^a_\nu-\partial_\nu E^a_\mu)
  -C^a_\nu\partial_\mu\lambda_a^{\mu}
  +2\operatorname{Re}[(\partial_\nu\psi)^\dagger R].
\]

Write these relations as K H=h, with K of size 52-by-272. At each sample,
rank K=52, K A is numerically zero, and its row-space projector agrees with the
full left-kernel projector of A. The sampled projector discrepancy is at most
1.02e-10. Consequently the incompatible component is reconstructed as

\[
 P_{\ker A^\top}H=K^+h
\]

to about 2.4e-10. This is a complete numerical attribution of this first-stage
left space at these points, not an exhaustive higher-order propagation theorem.
The three row families are not orthogonal; their raw right-hand-side norms must
not be added as independent residual contributions.

## Controls and results

The displacement scale is r=1/16384, a diagnostic Taylor-coordinate scale,
not a certified source-gate radius or a physical length.

| Sample | Normal-only compatibility | All-higher compatibility | Direct corrected H |
| --- | ---: | ---: | ---: |
| origin | 1.81e-10 | 1.05e-10 | 5.83e-10 |
| (r,0,0,0) | 0.005230 | 5.80e-7 | 5.80e-7 |
| (0,r,0,0) | 0.004190 | 3.06e-7 | 3.06e-7 |

The comparison here keeps sources fixed; the previous value near 0.00406 was
after fitting sources with prescribed higher data fixed. The two controls should
not be confused.

A minimum-norm higher correction has total coordinate norm 0.04583 and 0.03629
at the displaced points, including changes 0.02618 and 0.01882 in the prescribed
coordinates. Re-evaluation of the actual, unprojected first derivatives agrees
with the affine higher prediction to at most 6.7e-10. No new lower solution is
obtained: primary residuals remain about 6.03e-7 and 3.36e-7.

Both directional derivative steps, 1e-4 and 5e-5, verify K H=h to below 1e-9.
An additional deliberately non-solution lower jet checks that Lorentz and Ward
source terms cannot be dropped. These float checks are not interval certificates.

## Consequence for a derivation

On the sampled rank branch, if F0=0 and all constitutive curls vanish, then all
52 right-hand sides vanish, removing this first higher-jet compatibility
obstruction. This follows conditionally from the identities plus the observed
complete left-space span; no general exact-rank theorem is asserted.

Of the curls, the mixed 12 are in F0. The spatial 12 follow on an initial surface
if C vanishes there as a differentiable spatial field, not merely at one point.
The Lorentz and Ward rows are identities with residual sources, not 28 extra
independent physical constraints.

Thus the earlier 0.004-scale remainder is predominantly caused by the chosen
higher prescribed continuation. Its smaller irreducible part is accounted for
by lower residuals and constitutive curls, rather than an unidentified new
first-stage equation. The next task is to repair these lower/spatial conditions
consistently, then recheck all higher orders.

Pointwise higher corrections at separate coordinates need not be derivatives of
one common field. No integrability, regional constraint propagation, or renewed
1114-row completion is proved by this first-stage calculation.

## Reproduce

Run `python -B analysis/HC_Cartan_First_Compatibility_Attribution.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_first_compatibility_attribution`.
The adjacent JSON records fingerprints and diagnostics. New prescribed-response
matrices are fingerprint-cached; two local workers evaluate independent points.
