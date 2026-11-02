# Regional Scope of the Ward Gates

Date: 2026-10-18. Added neutral Cartan comparison only. No main TeX/PDF,
action coefficient, native frame or physical scale is changed.

## Result and Essential Scope Distinction

The previous [second coordinate gate](HC_Cartan_Second_Coordinate_Ward_Gates.md)
is an exact CONDITIONAL point implication. Its homogeneous version assumes
vanishing second constitutive sources. This audit keeps those sources and
tests whether the necessary Ward residual equations alone propagate F=C-E.

They do not, even when the displayed multiplier gate is uniformly invertible
on a region. An explicit smooth residual-level example satisfies all coordinate
and Lorentz Ward identities, has zero initial F and all its initial jets,
yet develops nonzero F later. This is a counterexample ONLY to uniqueness
for the standalone necessary Ward residual system.

It is NOT a solution of the parent fields, a parent nonuniqueness example,
an obstruction to every parent reduction, or a replacement physical model.
F is prescribed independently instead of being evaluated from spinors and a
coframe. R and FE are declared zero residual arrays, not evaluated field Euler
expressions. The multiplier background also differs from the saved parent's
spatial multiplier jets. These differences are deliberate and retained in
the numerical report and tests.

A separate [second Lorentz gate](HC_Cartan_Second_Lorentz_Transport_Gates.md)
uses the ACTUAL saved lower data and strengthens the point implication without
assuming full F2=0. Its map is injective at that point, but its source-free
simplification does not hold unchanged on a surrounding region. The two
calculations address different backgrounds and must not be conflated.

## Exact Smooth Necessary-System Example

Retain only the saved temporal multiplier value ell_0 and the three spatial
gradients L_j of its temporal column. Let x=(x1,x2,x3) and set

    ell(x) = ell_0 + sum_j xj L_j,
    lambda_a^mu = ell_a(x) delta_0^mu.

All spatial multiplier columns are identically zero and ell is time
independent. Therefore div(lambda_a)=sum_mu partial_mu lambda_a^mu=0,
despite the nonzero spatial derivatives of lambda_a^0. This is NOT the full
saved multiplier background, whose spatial-column gradients are nonzero.

Choose a fixed q=(1,0,0,0) and w=(1,0.3,-0.2), and define

    v(x) = q - ell(x) * (ell(x).q)/(ell(x).ell(x)),
    F^a_0(t,x) = 0,
    F^a_i(t,x) = b(t) v^a(x) w_i.

The ordinary contraction ell.v is exactly zero; no extra eta is involved.
For formal R=FE=0, the complete coordinate Ward identity reduces to

    nu=0: 0,
    nu=i: ell_a partial_t F^a_i = b'(t) ell.v w_i = 0.

The Lorentz identity reduces to F:(J.T lambda)=0, because J.T lambda has
only a temporal column and F has zero temporal column. These equations hold
as functions, so their differentiated identities also hold. Their satisfaction
does not construct a spinor/coframe realization of the prescribed residuals.

Two profiles serve distinct controls:

- b(t)=t: F vanishes on the entire initial spatial domain but its time
  derivative is nonzero. This directly tests the missing F2 source.
- b(t)=exp(-tau^2/t^2) for t>0, and b(t)=0 for t<=0, with tau=1/4:
  F and ALL finite initial derivatives vanish, while F is nonzero later.

The second profile is smooth at zero: each one-sided derivative is a finite
sum of powers of 1/t times exp(-tau^2/t^2), all tending to zero. Multiplying
by the smooth rational vector v preserves this for all mixed derivatives.
The numerical implementation evaluates only the first two derivatives;
its small-time branch returns their double-precision underflow values.
The all-orders statement is the analytic argument, not a finite test claim.

## Uniformly Invertible Gate Does Not Remove Its Sources

Let M(0) have rows ell_0 and L_1,L_2,L_3, as in the previous gate. Then

    M(x) = T(x) M(0),
    T(x) = I + e0 (0,x1,x2,x3),
    T(x)^-1 = I - e0 (0,x1,x2,x3).

Thus det M(x)=det M(0), and on |x|<=r,

    sigma_min(M(x)) >= sigma_min(M(0))/(1+r).

At r=0.01 the floating-input lower bound is about 0.00857495944. The bound
on |ell(x)| is positive too, making v smooth throughout that spatial ball.
These are analytic inequalities evaluated with stored floating inputs, not
an interval certificate for a parent solution or its coefficient domain.

At t=0 with b(t)=t, spatial F1=0, but

    X_ai = partial_t F^a_i = v^a w_i,
    F2[j,0,a,i] = (partial_j v^a) w_i,
    L_ja X_ai + ell_a F2[j,0,a,i] = 0.

This is precisely the second-constitutive source omitted by a homogeneous
gate. At x=0 its norm is about 0.539633924; the two opposite terms cancel
to about 1e-16. The actual time drift has norm about 1.04514752. Setting
the F2 contraction to zero would change the problem, not prove uniqueness.
The sourced matrix equation reconstructs this nonzero drift correctly.
For the flat profile, F at t=1/4 has norm greater than 0.3 while all initial
jets vanish. None of these coordinate norms is a physical rate or scale.

## Separate Actual-Point Lorentz Improvement

The independent derivation differentiates the full Lorentz identity twice
before specializing. Assume a regional temporal equation F_0=0, lower point
F=R=FE=0, R1=FE1=0, all spatial F1=0, and mixed R2[0,j]=FE2[0,j]=0.
At the actual point lambda has only its temporal column. Consequently the
F2[0,j]:(J.T lambda) term uses only temporal-column F2 and vanishes, without
requiring the spatial columns of F2 to vanish. What remains is

    X:(J.T partial_j lambda) = 0, for every generator J and j=1,2,3.

The resulting 18-by-12 matrix G has numerical rank 12, smallest singular
value about 0.0857465382. On the original six-dimensional normal-curl image
it has rank six, so it excludes all such point responses under its exact
hypotheses. The saved baseline residuals and ranks remain floating evidence,
not a proof that an exact nearby field solution exists.

Two scope controls are essential:

- F_0=0 merely AT A POINT does not imply temporal-column F2=0. For example
  F_0=t*x1*y has zero initial value and first point jet but nonzero mixed
  temporal/spatial second derivative, which restores a Lorentz source.
- At the saved point the spatial multiplier values vanish but their spatial
  gradients have norm about 2.56938. They cannot vanish identically in a
  neighborhood with those same jets. Away from the point the spatial-column
  F2:(J.T lambda) source therefore returns. If spatial multiplier columns
  instead vanish identically as in the formal example, this Lorentz2 gate
  has zero coefficients, not the injective actual-point map.

The injective point map is therefore an improved necessary compatibility
condition, not a homogeneous regional subsidiary system.

## Consequence for the Next Reduction

The Ward identities, temporal multiplier-gate invertibility and initial
constraints used in the formal example do not justify a GENERAL propagation
theorem: that example satisfies the identities and all their derivatives.
This does not rule out closure using additional verified properties of the
actual coefficient background; the example does not share all its jets.
The next parent proof must justify that extra structure, rather than promote
the displayed point gates to regional uniqueness. The concrete route remains
an Euler-based reduced evolution with the constitutive readout, all sources
retained, controlled multiplier directions and a closed subsidiary estimate
from zero initial constraints. No such reduction or estimate is claimed
here, and the native identification remains untouched.

The [pinned report](HC_Cartan_Ward_Regional_Nonclosure.json) records both
backgrounds explicitly. Sixteen focused tests cover exact identity
cancellation, independent field differences, uniform gate bounds, the
nonzero F2 source, zero initial jets, the actual-point Lorentz matrix and
the source terms restored when its hypotheses are relaxed.

Verification: 2,124 audit tests and 34 separate OP5 checks passed (2,158
total), including sixteen new regional-scope/Lorentz-gate tests. The
full-monolith preservation and whitespace checks passed. No commit,
push or PDF build was performed.
