# Fixed spin-response operator norm

## Same field and same Taylor coefficients

This follow-up sharpens the fixed response used in the Hermitian curl and
trace-reversed coframe enclosures. It changes neither the fields nor their
couplings, sources or equations. The complete 70-by-80 retained coefficient
arrays remain bitwise identical to the preceding saved coframe report in this
evaluation. Only the tail bounds change.

Scope remains the added neutral commuting-spinor odd-cross Einstein--Cartan
comparison. Main TeX/PDF are unchanged. This continuation is separate from the
research snapshot committed and pushed before starting the new calculation.

## Exact operator constant

For the frozen matrices, the response of the previous Hermitian identity is

    R_a,bc = W_a L_bc - L_bc^dagger W_a,
    L_bc = -gamma_b gamma_c / 4.

Flatten b,c as 16 input coordinates and a,i,j as 64 output coordinates. Denote
the resulting complex matrix by A. Its coefficient-tensor Frobenius norm is
sqrt(24), about 4.899. However, the bound needed for applying this fixed linear
map to an uncertain connection tensor is its induced operator norm.

Let T transpose the input matrix and let P_minus=(I-T)/2 be the orthogonal
antisymmetric projector. Exact Gaussian-rational evaluation of the frozen
entries gives

    A^dagger A = 2(I-T) = 4 P_minus.

The squared singular values are 4 on the six-dimensional antisymmetric
subspace and 0 on the ten-dimensional symmetric subspace. Therefore

    ||A||_2 = 2.

A unit antisymmetric input attains output norm two. The constant cannot be
replaced by one. No projection or zeroing of the input field is performed;
the complete map is applied to all stored input coefficients. The rank six
here belongs only to this fixed Lorentz spin-response map. It is not an
identification with the six source coordinates or a new compatibility gate.

For leading tensor indices, the same map acts independently on each block.
The Frobenius norm of the joint output is thus bounded by twice the joint
input Frobenius norm, without an additional square-root batch-count factor.
The implementation applies the retained coefficients directly and multiplies
the tail by two instead of sqrt(24).

## Use in the two equation blocks

The optimized response acts on the value connection in the Hermitian curl
terms and on its separately controlled physical derivatives. It also acts on
the unweighted matter readout in the coframe equation. The previously derived
trace maps and centered Ricci/inverse operators remain unchanged. Constraint
and probe rows retain their previous bounds.

| Quantity | L=r | L=r/2 |
| --- | ---: | ---: |
| Previous Hermitian curl tail | 0.867598 | 0.0270437 |
| New curl tail | 0.354565 | 0.0110520 |
| Previous coframe tail | 0.320179 | 0.00997588 |
| New coframe tail | 0.296727 | 0.00924819 |
| Previous combined 80-row estimate | 0.926433 | 0.0288757 |
| New combined 80-row estimate | 0.465620 | 0.0145121 |

Here r=1/16384. Bounds cover the cubes |x_i|<=L, hence the common Euclidean
balls. The combined estimate includes the unchanged nonzero low-order
coefficient norms; it is not just the tail. The frame-level matter tail at r
decreases from about 0.03972 to 0.01627. The frame-level Ricci/gravity tail,
about 0.28046, is unchanged by this spin-response improvement.

All sampled original-equation residuals remain unchanged, including cube
corners, and below the conservative estimates. The bounds still greatly exceed
those sampled errors. No statement about distance to an exact solution follows
from the numerical size of these estimates.

## Controls and boundary

Tests prove the frozen Gram/projector relation exactly, exhibit saturation,
compare arbitrary batched complex input models with direct response
contractions, and check that the tail constant does not grow with the batch
count. Perturbed off-shell curl and coframe values match the original evaluator;
nonzero residuals are not erased. All retained coefficients match the preceding
report, including degree-three/four defects.

The exact constant of this one linear map does not make the surrounding
production calculation an interval certificate. Polynomial coefficients,
inverse centers, nonlinear tails and arithmetic operations still use binary64
without outward rounding. Regional PDE compatibility, exact low-order closure,
all-order convergence, native HC/C7 identification and physical length scales
are not established. The separate rational origin-kernel certificate retains
its own authority.

Run `python -B analysis/HC_Cartan_Spin_Response_Operator_Bound.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_spin_response_operator_bound`.
Two bounded local workers evaluate independent radii. The adjacent JSON stores
fingerprints, unchanged coefficient arrays, exact-map diagnostics, previous/new
tail estimates and actual-equation controls.
