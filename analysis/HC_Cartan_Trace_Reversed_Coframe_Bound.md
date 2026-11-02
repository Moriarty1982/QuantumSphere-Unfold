# Trace-reversed coframe bound with centered operators

## Same coframe equation, different enclosure

Following the Hermitian curl regrouping, the 16 coframe Euler rows were the
largest block in the whole-cube estimate. This audit factors that equation
before taking norms. It retains the same field, sources, couplings and the
other 64 rows. No equation coefficients are fitted or forced to zero.

Scope remains the added neutral commuting-spinor odd-cross Einstein--Cartan
comparison, not a native HC/C7 identification. Main TeX/PDF are unchanged.

## Off-shell factorization

Write A=E^-1, v=|det E|, and define the unweighted matter readout and mass term

    X_a,mu = Im[psi^dagger (I tensor W_a) D_mu psi],
    m = Re[psi^dagger (M tensor beta) psi].

In the existing index conventions, set

    Y_ac = sum_mu A_mu,a X_c,mu,
    K_ac = sum_mu,nu,b A_mu,a A_nu,b R_mu,nu^(c,b).

Then the independent coframe Euler equation is exactly

    F_E = v [Y - (tr Y + m) I + (1/2)(tr K) I - K] A^T + lambda.

The two inverse-variation curvature terms in the original equation coincide
after using antisymmetry in both curvature index pairs. The scalar curvature
contraction is tr K. These facts yield the displayed gravitational term.
The matter term follows by factoring the rightmost A^T from
v(A X A)^T - v[tr(A X)+m]A^T. No field equation or Ricci symmetry is required.

The pair antisymmetries follow from the real lower Lorentz connection in this
comparison; no pair-exchange symmetry, first Bianchi identity or torsion-free
Ricci symmetry is imposed. Arbitrary curvature tensors antisymmetric in their
two pairs are used in an independent off-shell test, with demonstrably
nonsymmetric K. The factorization must not be applied to unconstrained
curvature tensors without those pair antisymmetries.

The readout X is also regrouped with the already-checked Hermitian spin response:
its partial-derivative term is retained and its connection term is one half
the imaginary expectation of W S - S^dagger W. This step is unweighted in
channel space, unlike the Q-weighted constitutive curl.

## Why the trace maps have sharper constants

For any complex 4-by-4 matrix, decompose K=k I+K0, with tr K0=0. The trace and
traceless components are orthogonal in the Frobenius inner product. Therefore

    (1/2)(tr K) I - K = k I - K0

has exactly the same Frobenius norm as K. Its operator norm on this tensor
space is one, without assuming K symmetric. Similarly,

    Y - (tr Y) I = -3 y I + Y0

has Frobenius operator norm three. These maps act on the retained coefficients
before taking norms, and their tail bounds use those exact constants.
Rational symbolic tests verify G^T G=I for the full 16-component gravity map
and the eigenvalues 1 (multiplicity 15), 9 (multiplicity 1) of the squared
matter map.

## Fixed-center operators instead of repeated Frobenius factors

The ordinary contraction estimate overcounts even multiplication by I, whose
Frobenius norm is two but spectral operator norm is one. The new matrix-product
bound separates the fixed centers A0,B0, retained nonconstant coefficient norms
pA+,pB+, and tails tA,tB. Its tail includes all discarded polynomial products
and

    tA (||B0||_2 + pB+) + tB (||A0||_2 + pA+) + tA tB.

Nothing is discarded from the variable matrices. The final multiplication by
the inverse coframe uses this bound.

The Ricci pullback likewise combines its two constant inverse factors into a
single linear map on curvature, then retains every term with one or two inverse
deviations. At the present center A0=I, that fixed map is

    L(R)_ac = sum_b R_abcb.

On the full 256-component curvature space, L L^T=4 I, so its norm is exactly
two. Applying two separate Frobenius norms of I would instead give four.
This norm does not need pair antisymmetry; the antisymmetry assumption is used
only in the coframe factorization itself. For other constant centers the code
constructs the same linear map explicitly and evaluates its spectral norm.

## Results on the same cubes

Let r=1/16384. Estimates cover |x_i|<=L and hence ||x||<=L.

| Quantity | L=r | L=r/2 |
| --- | ---: | ---: |
| Previous coframe tail | 2.16745 | 0.0674980 |
| New coframe tail | 0.320179 | 0.00997588 |
| Previous combined 80-row estimate | 2.33530 | 0.0727342 |
| New combined 80-row estimate | 0.926433 | 0.0288757 |

At r the new frame-level matter tail is about 0.03972, the Ricci/gravity tail
about 0.28046. The trace-reversed gravity tail equals the Ricci tail because
the trace map is an isometry. After the final inverse/volume factors, the
coframe tail is about 0.32018. The unchanged improved curl tail, about 0.86760,
again exceeds that block. These are statements about conservative enclosure
constants, not an attribution of physical error or a new obstruction.

The coefficient arrays differ from the original coframe polynomial in norm by
about 1.29e-14, consistent with reordered arithmetic. Independent actual-point
evaluations agree to about 8e-15--2.1e-14, including cube corners. The saved
degree-three/four coframe coefficient bounds at r remain about 8.71e-11 and
1.62e-10; they are not set to zero. Actual tested coframe residuals are still
far below the tail bounds.

The fact that the combined estimate is now below one has no special existence
or physical-accuracy significance. These component norms have not been turned
into a distance-to-solution bound or a contraction theorem for a regional PDE.

## Verification and remaining boundary

Tests cover exact trace-map constants, the exact identity-center pullback norm,
nonconstant matrix products with discarded terms and uncertain tails, and the
full independent coframe Euler formula with nonsymmetric Ricci data. A perturbed
multiplier produces a clearly nonzero coframe equation that the new expression
preserves. Other 64 stored coefficient rows remain bitwise unchanged.

The production calculation still evaluates real-arithmetic majorant formulas
in binary64, without outward-rounded error enclosures. It does not establish
exact low-order vanishing, constraint propagation, a regional solution,
all-order convergence, native coupling identification or physical length scales.
The separate rational retained-origin kernel certificate remains authoritative
for its precision-sensitive update.

Run `python -B analysis/HC_Cartan_Trace_Reversed_Coframe_Bound.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_trace_reversed_coframe_bound`.
Two bounded local workers evaluate independent radii. The JSON stores source
fingerprints, unchanged/modified coefficient arrays, operator norms, tail
diagnostics and actual-equation controls. Historical artifacts are not rewritten.
