# Direct quartic coefficient refinement

## Scope and preserved data

This sidecar constructs a new candidate in the neutral commuting-spinor
odd-cross Einstein-Cartan comparison. It refines the existing homogeneous
coframe degree-six, spinor degree-five and multiplier degree-five coefficients.
It does not replace the authoritative parent polynomial or published payload.
Main TeX/PDF remain unchanged.

All lower field data and the earlier rational fourth-spinor kernel
representation remain fixed. Degree counting preserves the retained origin
jet and every residual coefficient below degree four. Direct evaluations
confirm zero origin field/higher-jet change and bitwise unchanged lower
residual coefficient arrays. The inherited failed rounded-origin recheck is
not repaired, overwritten or hidden by this higher-order correction.

## Coefficient-space system

The previous quartic fit used directional finite differences and a degree-four
Vandermonde conversion. Here the right side is the actual degree-four Taylor
coefficient array of the current 80-row residual. Each of the 35 monomials
contributes 80 equation rows and 16 fixed-coordinate rows, giving a 3360-by-3584
system. Coordinate *increments* are constrained to zero; those rows are not
released to improve the fit.

The response is assembled directly by differentiating the correction
monomials: two coframe derivatives, one spinor derivative and one multiplier
derivative. With the existing amplitudes r^2, r and r, the radius factors
cancel from these leading coefficient maps. Coefficients are integer falling
factorials multiplying the frozen origin field Jacobian. Independent node
response builders agree to about 2.23e-15 at the tested directions.

The inherited Jacobian is still a binary64 calculation, not an exact symbolic
or interval-certified matrix. The compact SVD fit stores increments, singular
values and the full incompatible residual, without caching large full inverse
or singular-vector arrays. Cache identity includes the full matrix, target,
backend/version and cutoff policy. Two cutoffs share one decomposition.

## Results at r=1/16384

| Quantity | Value |
|---|---:|
| Numerical rank | 2454 |
| Primary singular-value cutoff | 2.92620e-8 |
| Retained condition estimate | 8.24034e7 |
| Previous quartic coefficient Frobenius norm | 1.29032e-10 |
| Fitted full augmented residual norm | 2.70317e-15 |
| Independently recomputed quartic residual norm | 2.70317e-15 |
| Coefficient-response prediction error | 6.09028e-19 |
| Coordinate-increment norm | 6.69284e-22 |
| Field coefficient increment norm | 7.45876e-8 |
| Previous quartic field coefficient norm | 7.59911e-5 |

The quartic residual decreases by about 47,700 times, with an increment about
0.098 percent of the previous quartic coefficient norm. The retained condition
estimate is about 22 times smaller than in the previous directional system,
but remains large. Reducing the relative cutoff from 1e-10 to 1e-12 (with
absolute cutoff 1e-9) retains the same rank and increment in this evaluation.
That single sensitivity check is not an exact-rank or conditioning certificate.

The new block coefficient norms are approximately 2.08124e-15 (constitutive),
1.07857e-15 (probe), 1.34620e-15 (coframe), and 6.05805e-19 (curl).

## Attribution of the remaining constitutive source

The preceding exterior audit gives F3=(1/r)d_y C4. An allowed quartic
correction cannot change F3 when all lower orders are fixed. Thus it cannot
freely remove the nonclosed part of C4.

Let D be the 120-by-140 coefficient differential on one homogeneous
degree-four one-form. Its numerical rank is 84. For the four constitutive
components, D C4 has norm 5.96586e-15 before correction, and changes only by
3.84306e-20. The minimum Euclidean coefficient solution for that fixed source,
D^+ D C4, has norm 2.08122e-15. The actual remaining C4 norm is 2.08124e-15;
their coefficient-vector difference has norm 8.10116e-18.

The remaining constitutive defect is therefore numerically almost the
known lower-order compatibility source, rather than merely an arbitrary fit
failure. This attributes only that known identity family, not the entire
left kernel or the probe/coframe remainders. The source floor is conditional
on frozen floating data, not an exact physical obstruction or nonexistence
proof. Further repair must revisit the cubic data and preserve their origin
kernel constraints; adding still higher orders cannot remove this source.

## Full-equation and bound controls

At four directions and two radii, the shared corrected field is evaluated in
the original 80-row equations. The quartic improvement does not imply a
uniform pointwise improvement: at y=(0,1,0,0), the sampled norm changes from
6.61853e-8 to 6.61860e-8, a slight increase. At y=(-1,1,-1,1) it decreases
from 8.90204e-6 to 8.89382e-6. Higher-order terms still dominate these samples.
Both effects are retained in the saved report.

The enclosure is recomputed for the changed polynomial. Its combined
whole-cube estimate is 0.00102066985, versus 0.00102092622 before; at half
radius it is 0.0000315692705. These remain non-outward-rounded majorants,
not exact residual zeros or distance-to-solution estimates. Cubic defects
remain unchanged, as do the unresolved regional compatibility, convergence,
and native HC/C7 identification questions.

## Reproduction

Run `python -B analysis/HC_Cartan_Quartic_Coefficient_Refinement.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_quartic_coefficient_refinement`.
The JSON records input fingerprints, singular values, the full candidate
coefficient vector, retained residual coefficients, source attribution,
cutoff sensitivity and negative pointwise controls. Independent radius
evaluations use two local workers; the single coupled solve is sequential.
Historical inputs and reports remain unchanged.
