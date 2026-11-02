# Constitutive Taylor model with a whole-cube tail

## Purpose and scope

The preceding natural tensor-ball enclosure lost low-order cancellations and
gave a constraint-block bound about 2362 at radius r = 1/16384. This audit
preserves the multivariate polynomial through degree four before taking norms,
and bounds the remaining terms separately.

This first application covers only the 16 constitutive equations. It does not
yet replace the other 64 rows of the 80-equation audit. All field coefficients,
source values and couplings are unchanged; no residual coefficients are fitted
or forced to zero. The added neutral commuting-spinor odd-cross Einstein--Cartan
comparison remains distinct from a native HC/C7 identification. The main
TeX/PDF are unchanged.

## Taylor tensor and tail algebra

Set y = x/L for the chosen coordinate radius L. Represent a tensor expression
as

    A(y) = sum_{|alpha| <= 4} A_alpha y^alpha + R_A(y),
    sup_{|y_i| <= 1} ||R_A(y)||_F <= t_A.

There are 70 retained multiindices in four variables. The coefficient norm
bound is p_A = sum_alpha ||A_alpha||_F. Polynomial addition and all retained
contractions are performed on their actual coefficients before taking norms.
Thus exact polynomial cancellation is retained in real arithmetic, unlike
subtraction of independent value balls. Existing nonzero input tails remain
uncertain and are added, not canceled by assuming that two tails coincide.

For a bilinear contraction with Frobenius bound factor K, the new tail includes

    K [sum_{|alpha|+|beta| > 4} ||A_alpha|| ||B_beta||
       + t_A (p_B+t_B) + p_A t_B].

The omitted polynomial products are explicitly included. A lone summed tensor
index contributes the necessary square-root dimension factor; contractions
with repeated indices inside a single operand are rejected. Multilinear
expressions are reduced to successive binary contractions, retaining every
index still needed by later operands. Complex conjugation is coefficientwise
because the coordinates y are real.

The calculation is on the full four-cube |x_i| <= L, which also covers the
Euclidean ball ||x|| <= L. The previous natural bound and this new cube bound
can therefore be compared as upper estimates on that common Euclidean ball;
the new bound is not restricted to the few sampled directions.

## Matrix inverses and the actual constraint expression

For A = A0 + delta A, form Z = -A0^-1 delta A and a whole-cube estimate

    q >= sup ||Z||_F,    q < 1.

The inverse uses the first five Neumann terms, with each product truncated by
the same tail algebra. The additional geometric tail is bounded by

    q^5 ||A0^-1||_F / (1-q).

The constant part of Z is zero in the mathematical construction. Frobenius
submultiplicativity supplies a valid, possibly loose bound on the higher matrix
powers. An unresolved q >= 1 is rejected rather than silently inverted as a
uniform model. This procedure is used for both the coframe and Cartan Hessian.
The determinant is evaluated as a polynomial; positivity follows from the
positive center orientation and the resolved Neumann path from that center.

The base quartic germ is assembled from its symmetric derivative tensors with
the correct multiindex factorials. All previous corrections, including the
fourth-spinor reprepare and degree-six coframe/degree-five spinor and multiplier
extension, are included. High polynomial field terms enter the tail; their
derivatives can contribute retained coefficients and are not discarded early.

The model then follows the same algebraic Cartan elimination, Levi-Civita
connection, spin lift and covariant readout as the original equations. In
particular it evaluates the actual constraint

    C = Im <psi, Q D psi> - E,

with all its field correlations retained in the degree-four polynomial.

## Results

| Quantity | L = r | L = r/2 |
| --- | ---: | ---: |
| Constant coefficient norm | 5.25e-15 | 5.25e-15 |
| Sum of degree-one coefficient norms | 4.26e-16 | 2.13e-16 |
| Sum of degree-two coefficient norms | 2.94e-19 | 7.35e-20 |
| Sum of degree-three coefficient norms | 7.08e-20 | 8.85e-21 |
| Sum of degree-four coefficient norms | 5.35e-11 | 3.34e-12 |
| Whole-cube tail estimate | 2.70219e-2 | 8.38376e-4 |
| Whole-cube total residual estimate | 2.70219e-2 | 8.38376e-4 |
| Coframe Neumann ratio | 1.48e-8 | 2.92e-9 |
| Cartan-Hessian Neumann ratio | 5.35e-8 | 1.05e-8 |

The first constraint-block bound improves from about 2362 to about 0.027,
an improvement exceeding 80000-fold on the common ball. The recomputed tail
decreases by a factor about 32.23 when the radius is halved, consistent with
retaining terms through degree four. This observed two-radius ratio is not
itself a certified scaling law on all intermediate radii.

At r the tested actual constraint norms are about 6.96e-10, 3.74e-9 and
4.48e-11. Their discrepancies from the retained polynomial are safely below
the new tail, but the bound remains millions of times larger than these sample
values. Preserving low-order cancellation is a substantial improvement, not a
sharp residual certificate or a completed regional solution.

The degree-four coefficient bound is nonzero and is consistent with the
previous finite extraction accuracy; it is not replaced by the fitted target
zero. The lower-degree numerical values and all coefficients are likewise
stored, not erased. Their tiny size does not certify exact vanishing.

## Numerical and proof boundaries

All coefficients, inverse centers and norm bounds are evaluated in binary64.
The formulas enclose the mathematical operations in real arithmetic, but no
outward rounding covers floating-point errors. Zero-radius constant models
match independent original constraint evaluations within ordinary evaluation
accuracy, including a deliberately perturbed off-shell point. The inherited
exact retained-origin kernel representation remains authoritative for that
separate check; these neighborhood models do not replace its precision audit.

This result provides a cancellation-preserving polynomial plus a conservative
whole-cube tail for one block. It does not bound distance to an exact solution,
prove convergence of successive corrections, or supply regional compatibility
and propagation for the remaining equations. Extending the calculation to the
probe, coframe and curl blocks and controlling rounding remain necessary before
claiming a uniform certificate for the full system.

## Reproduce and tests

Run `python -B analysis/HC_Cartan_Constitutive_Taylor_Bound.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_constitutive_taylor_bound`.
Two bounded local workers evaluate the two radii. The adjacent JSON stores
fingerprints, all 70 tensor coefficients at each radius, low-order norms,
inverse ratios, tail bounds and independent point controls.

Tests cover retained and discarded products, exact polynomial cancellation,
complex multilinear contractions, trace factors, scalar geometric and
noncommuting matrix inverses, unresolved-inverse rejection, derivative packing,
field reconstruction, off-shell constraint evaluation and saved coefficients.
