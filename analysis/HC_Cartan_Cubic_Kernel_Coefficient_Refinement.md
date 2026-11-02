# Cubic kernel-coordinate refinement and quartic refresh

## Scope

This sidecar continues the direct quartic coefficient refinement for the added
neutral commuting-spinor odd-cross Einstein-Cartan comparison. It constructs
a new working candidate without replacing any authoritative parent polynomial,
historical report, main TeX/PDF or published payload. Numerical low-order
improvement is not exact closure, regional existence or native HC/C7 physics.

## Allowed cubic corrections

The unknowns are homogeneous coframe degree-five, spinor degree-four and
multiplier degree-four corrections. With amplitudes r^2, r and r, their
leading residual contribution is degree three. All coefficients below degree
three remain fixed.

The spinor correction is not allowed to move arbitrarily in its 840 real
coordinates. Each of the 35 monomials uses the existing exact 4-by-24 origin
readout kernel: 20 free coordinates and four dependent pivots. The readout
is checked against the actual frozen origin spinor, selector and weights.
The 24-by-20 basis satisfies A B=0 using rational arithmetic.

There are 896 coframe, 700 free spinor and 560 multiplier coordinates, or
2156 unknowns. The system has 20 monomials times 80 residual and 16 fixed
coordinate rows, giving shape 1920 by 2156. It is assembled directly from
monomial derivatives and the inherited frozen origin Jacobian, not directional
finite-difference extraction of the residual target. The Jacobian itself is
still binary64, so the numerical rank is not exact-rank certification.

## Exact representation and rounded representative

After solving, each free-coordinate increment is interpreted as its exact
binary64 rational and added to the old rational free value. Dependent pivots
are then reconstructed rationally. Both the incremental and total origin
readout updates vanish exactly, including all 320 retained C3 update rows.
No residual coefficient is manually set to zero.

For the neighborhood calculations, the resulting total monomial coefficients
are converted to binary64. That rounded polynomial is a different numerical
representative, not the exact parametric object. The saved raw 1114-row origin
controls make this distinction explicit:

| Origin diagnostic | Norm |
|---|---:|
| Inherited binary64 anchor before kernel updates | 4.87114e-10 |
| Raw rounded representative before this refinement | 1.28080e-7 |
| Raw rounded representative after refinement | 1.39723e-7 |

These failed rounded controls are retained, not replaced by an anchored zero.
There is no fresh high-precision nonlinear evaluation or solve of all 1114
origin rows here. Exact frozen-origin preservation and rounded-neighborhood
enclosures cannot be combined into one certified field solution.

## Cubic fit and necessary quartic refresh

The cubic system has numerical rank 1296 at cutoff 2.51457e-8, with retained
condition estimate about 2.08e6. The increment norm is 4.95699e-9, and the full
linear residual norm is 8.82299e-20. Using relative cutoffs 1e-10 and 1e-12,
with absolute floor 1e-9, gives the same retained rank and increment.

The actual recomputed cubic coefficient norm becomes 2.70741e-19. This is
about 3.84e8 times smaller than 1.03832e-10 before refinement, but remains
nonzero and is comparable to its 2.70266e-19 response-prediction discrepancy.
Those small values are numerical cancellation diagnostics, not exact zeros.

Changing cubic data also changes quartic sources. The quartic coefficient
norm initially grows from 2.70317e-15 to 3.38678e-10. The old quartic fit and
its bounds therefore cannot simply be reused. A fresh right side is formed
from this intermediate candidate and the constrained quartic system is
solved again. Its numerical rank remains 2454, and the new quartic increment
norm is 7.51104e-9.

| Complete 80-row coefficient norm | Before | After cubic plus quartic refresh |
|---|---:|---:|
| Degree three, r=1/16384 | 1.03832e-10 | 2.70741e-19 |
| Degree four, r=1/16384 | 2.70317e-15 | 5.69095e-19 |
| Degree three, half radius | 1.29790e-11 | 3.38426e-20 |
| Degree four, half radius | 1.68948e-16 | 3.55684e-20 |

All lower coefficient arrays are bitwise unchanged in the saved evaluation.
The normal-coordinate increment norms are 2.79981e-23 (cubic) and 6.84360e-23
(quartic). Lower origin field and used higher-jet values are unchanged. The
changed fourth spinor jet is handled separately by its exact kernel identity.

## Negative neighborhood controls and refreshed bounds

Small low-order coefficients do not imply a smaller full neighborhood error.
At the larger radius, all four recorded full residual samples become slightly
larger. For example, y=(1,0,0,0) changes from 9.60920e-8 to 9.61010e-8, and
y=(-1,1,-1,1) from 8.89382e-6 to 8.89461e-6. Higher-order terms dominate.

The whole-cube majorant is recomputed for the rounded candidate. It is about
0.00102076215, slightly worse than 0.00102066985 for the preceding quartic-only
candidate. At half radius it is about 0.0000315720847. The tiny third/fourth
coefficients do not reduce the much larger tail bound. Constant, linear and
quadratic residual coefficients also remain nonzero.

No interval or outward-rounded nonlinear certificate, convergent expansion,
regional compatibility or physical identification follows. The next substantial
gap includes reconciling exact kernel coordinates with stable neighborhood
evaluation and controlling the higher-order tail, not declaring low-order
closure from small binary64 coefficient norms.

## Reproduction and controls

Run `python -B analysis/HC_Cartan_Cubic_Kernel_Coefficient_Refinement.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_cubic_kernel_coefficient_refinement`.
The JSON stores both numerical fits, all updated coefficients, the new exact
free/pivot certificate, independent original-equation samples, refreshed bounds
and the failed rounded-origin controls. Independent radius checks use two local
workers; the cubic and quartic solves are sequential and use compact cached
results. Tests verify rational kernel integrity, deliberately corrupted pivots,
free-coordinate addition before rounding, independent old node response maps,
fixed lower coefficients and actual shared-field witness reproduction.
