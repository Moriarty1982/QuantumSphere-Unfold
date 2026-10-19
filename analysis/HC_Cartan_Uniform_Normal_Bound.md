# A Uniform Majorant for the Augmented Normal Chart

Date: 2026-10-19. Local, uncommitted follow-up after committed/pushed
baseline 176427e. The OP register and issue 16 were read, not updated.
Added neutral commuting-spinor odd-cross comparison only. Main TeX/PDF
and published payloads unchanged.

## From Samples to a Coefficient Estimate

The [general normal chart](HC_Cartan_General_Normal_Chart.md) had favorable
ranks at thirteen points, but its sampled maximum matrix change was not
a uniform bound. This calculation constructs the normal coefficient
matrix directly and propagates analytic norm bounds for every input
through its tensor contractions. Its radius selection uses that majorant,
not a maximum over samples.

The result is a real-arithmetic sufficient inequality, evaluated with
floating-point norms and arithmetic. It is not an outward-rounded
interval certificate or a machine-verified exact proof.

## Direct Coefficients Rather Than Subtraction of Uncertain Equations

For the same 56 normal unknowns, write a variation as delta E_,00,
P=delta psi_,0 and L=delta lambda_,0. Field values E, dE, psi and lambda
are fixed in forming each coefficient matrix. Consequently delta omega
at order zero is zero. Only the derivative of the connection changes.

For the Cartan contribution, with H k=-s+R.T lambda,

    delta (partial_0 k)
       = H^-1(-delta (partial_0 s)
               +delta (partial_0 R).T lambda + R.T L).

Here delta (partial_0 H)=0 since the coframe first jet is not a normal
unknown. The source and response derivatives are the bilinear functions
of psi and P from the general evaluator. The LC contribution is the
linear response of partial omega to delta E_,00 at the actual E. These
give delta curvature and the coefficients of all 68 equations directly.

The matrix depends on E, dE, psi, lambda and the spatial first spinor
derivatives. It does not depend on the chosen normal values themselves;
nor on unrelated second coframe derivatives or first multiplier
derivatives as independent background coefficients. Those derivatives
still enter the Taylor bounds for E, dE and lambda as functions of x.

The direct formula matches the earlier affine-column matrix at the
origin to 2.45e-14 and is independently tested at a non-origin point.
This avoids subtracting two large uncertain residuals when estimating
the coefficient perturbation.

## Tensor-Ball Calculus

A tensor ball (A0,rho) means ||A-A0||_F<=rho. Addition uses the triangle
inequality. Transposition, reshape, conjugation, real/imaginary projection
and nonduplicating coordinate restriction do not increase rho. Stacking
blocks uses the square root of the sum of squared block error bounds.
Complex probe realification is an isometry.

For each implemented multilinear contraction C, a Frobenius contraction
bound gives

    ||C(A1,...,Ak)-C(A10,...,Ak0)||_F
      <= M [product_j (||Aj0||_F+rho_j) - product_j ||Aj0||_F].

The difference is accumulated without subtracting nearly equal large
products. M includes sqrt(dimension) for a lone summed index. Repeated
indices within one operand, ellipses and duplicating advanced slices
are rejected by this restricted implementation. The coefficient formula
uses only supported contractions. Reusing the same uncertain tensor in
several places is safely overestimated by treating those occurrences
independently; correlations are not claimed to tighten the estimate.

This calculus is conservative. Its unit tests check complex contractions,
dimension factors, contractive operations and block composition, alongside
direct field/operator comparisons. Such tests do not replace the stated
norm inequalities or make floating arithmetic interval-certified.

## Uniform Input Envelopes

All envelopes use the changed compatible jet and full symmetric tensor
norms. For ||x||<=r, define d and p as in the
[coefficient-domain estimate](HC_Cartan_Compatible_Lift_Regularity.md),
and additionally bound

    ||dE||_F <= ||E2|| r + ||E3|| r^2/2 + ||E4|| r^3/6,
    ||spatial dpsi-spatial dpsi0||_F
       <= ||psi2|| r + ||psi3|| r^2/2 + ||psi4|| r^3/6,
    ||lambda-lambda0||_F
       <= ||lambda1|| r + ||lambda2|| r^2/2 + ||lambda3|| r^3/6.

The last bound uses all multiplier columns, not only the temporal column.
The temporal first spinor entry is set to zero in this coefficient
representation because it is one of the unknowns, not a coefficient.

For d<1, use ||E^-1-I||_F<=d/(1-d), volume lower bound v_min=(1-d)^4,
and volume change bound dv=4d+6d^2+4d^3+d^4. Cartan congruence gives

    H(E)^-1 = (E.T tensor I6) H(I)^-1 (E tensor I6) / |det E|,

and hence the Frobenius inverse-Hessian change bound

    ||H(E)^-1-H(I)^-1||_F
      <= ||H(I)^-1||_F (2d+d^2+dv)/v_min.

Thus no uncertain matrix inversion is assumed inside the tensor-ball
calculation. The established coframe/Cartan identities provide explicit
input envelopes instead.

## Uniform Chart Inequality and Result

Let N(x) be 68 by 56 and retain the fixed sixteen coordinate rows W from
the earlier chart. Set T(x)=(N(x);W), of shape 84 by 56. The propagated
matrix ball gives

    ||T(x)-T(0)||_2 <= ||N(x)-N(0)||_F <= epsilon(r).

If sigma0=sigma_min(T(0)) and epsilon<sigma0, then, in exact arithmetic,

    sigma_min(T(x)) >= sigma0-epsilon > 0,
    ||T(x)^+||_2 <= 1/(sigma0-epsilon).

The analogous bound on sigma_40(N(x)) establishes rank at least 40,
not an exact upper rank of 40. The latter requires additional kernel
identities; no such conclusion is inferred from small perturbations.

Starting from r=1/16384, the algorithm halves the radius until both
singular margins retain at least half their origin values. The reported
float evaluation selects:

| Quantity | Value |
| --- | ---: |
| Radius r | 2^-32 = 2.3283064365e-10 |
| Origin augmented singular margin | 0.10594420 |
| Matrix-change majorant epsilon(r) | 0.04934813 |
| Augmented singular lower estimate | 0.05659606 |
| Augmented left-inverse norm upper estimate | 17.66907 |
| 40th normal singular lower estimate | 0.05659606 |

The mixed-curl block contributes most of the majorant (about 0.04918),
followed by the coframe block (about 0.00411). These block bounds combine
quadratically. Constraint and probe coefficient changes are much smaller.

This is deliberately not a sharp radius. The first majorant at the old
common radius is about 12993, while actual operator samples there had
changes around 0.038. At the newly selected radius the largest sampled
change is only 1.46e-7, far below the 0.04935 majorant. The small selected
radius reflects loose norm products, not evidence of a physical cutoff
or of a singularity outside it. The bound has no identified length unit.

## What Is Still Open

The inverse estimate is for the augmented mixed-order matrix T, not an
unrestricted inverse of the rank-deficient N. The fixed coordinate rows
are not a proven transported gauge/source classification. Arbitrary
84-component forcing is still subject to 28 left compatibility
conditions, and this estimate does not propagate them.

No claim of exact rank 40 everywhere, full PDE hyperbolicity, compatible
surface evolution, regional solution, native HC/C7, physical frames or
scale identification follows. The existing off-origin compatibility
defects are not removed by bounding the operator.

Further work can tighten the mixed-curl majorant and provide outward
rounding if a certified numerical radius is needed. The more substantive
dynamical task remains the left compatibility/subsidiary system and its
propagation. The [compatibility split](HC_Cartan_Normal_Compatibility_Split.md)
now identifies the twelve spatial constitutive rows, four gravitational
rows, six Lorentz identities and six remaining mixed-curl gates. It also
retains the forcing term in the exact projector-transport identity; no
closed full propagation theorem follows yet. These sidecars change no
field equations or couplings.

## Reproduction and Verification

Run `python -B analysis/HC_Cartan_Uniform_Normal_Bound.py --output
analysis/HC_Cartan_Uniform_Normal_Bound.json` from the repository root.
The existing DI/cache services are reused for independent matrix checks.
The small bound recursion is local and sequential; no additional agent
was spawned after the earlier usage-limit failure.

31 focused tests passed: 11 tensor-ball/uniform-bound tests, 10 general
normal-chart tests and 10 compatible-lift regularity tests. They include
the direct coefficient formula at nonzero coframe/gradient, input
enclosures at both the old and new radii, monotonicity, and the explicit
scope guards. The full repository suite was not rerun for this isolated
analysis addition. Work after commit 176427e remains local and uncommitted.
