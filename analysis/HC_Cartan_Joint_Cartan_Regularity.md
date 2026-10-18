# Joint1114 Cartan Regularity

This sidecar proves a uniform algebraic estimate for the eliminated 24 by 24
Cartan Hessian on the saved joint1114 quartic Taylor fields. Input norms and
singular values are evaluated in finite floating point, without interval
certification. The estimate does not establish PDE existence, propagation,
hyperbolicity of the full system, or a physical length scale.

## Uniform Estimate

The existing curvature-Hessian representation is

`H(E)[p,q] = |det E| sum inverse(E)[m,a] inverse(E)[n,b] C[p,q,m,n,a,b]/2`.

Here C is `prepared['curvature_hessian']`, obtained by polarization of the
quadratic connection curvature. The connection basis orders its coordinate
index first, then the six lower Lorentz pairs. Consequently, with
`A = inverse(E).T tensor I_6`, coordinate-to-frame conversion of each connection
factor gives the exact congruence

`H(E) = |det E| A.T H(I) A`.

This identity holds for an indefinite H(I); positive definiteness is not
assumed. It follows directly from substituting the frame connection into the
quadratic curvature action. Tests also compare it to C contraction and the
original `contorsion_hessian` polarization on nonsymmetric real coframes.

Let `||E-I||_2 <= d < 1`, `s0 = sigma_min(H(I)) > 0`, and
`h0 = ||H(I)||_2`. All singular values of E lie in `[1-d,1+d]`.
Thus `|det E| >= (1-d)^4` and `sigma_min(A) >= 1/(1+d)`.
Using the least singular value product inequality twice gives, uniformly,

`sigma_min(H(E)) >= s0 (1-d)^4/(1+d)^2 > 0`,

`||inverse(H(E))||_2 <= (1+d)^2/[s0 (1-d)^4]`.

There is also a direct perturbation estimate. Write `t=d/(1-d)` and
`v=4d+6d^2+4d^3+d^4`. Since `||A-I||_2 <= t`, `||A||_2 <= 1/(1-d)`,
and `||det E|-1| <= v`, splitting the congruence at unit volume gives

`||H(E)-H(I)||_2 <= h0 [v/(1-d)^2 + 2t + t^2] = B(d)`.

Therefore `s0-B(d)` is a second, possibly negative, singular margin.
A negative perturbation margin means only that this second estimate fails;
the congruence estimate remains positive for every d less than one.
Radius selection conservatively requires `s0-B(d) >= s0/2`.

## Saved Joint Fields

The lower point comes from
`HC_Cartan_Next_Joint_Completion.third.diagnostic.load_data()`.
The older jets are unpacked from the joint report's `jet_coordinates`, not
from a previous completion. The first 560 connection coordinates are the 35
unique E4 matrices; the remaining 320 are the 20 unique lambda3 matrices.
The 35 by 24 real psi4 array is converted rowwise with `prior.complexify`.
Q and M remain unchanged, with Einstein coefficient 1 and vacuum 0.
The loader verifies the saved joint provenance and the retained psi2.

This independent loader retains *unique* arrays in its extras dictionary,
unlike the parent neighborhood loader's full symmetric arrays. Its `fields`
routine applies the existing unique-coordinate homogeneous Taylor evaluator
to E4, psi4 and lambda3, then solves the exact Cartan equation afresh.
Its coefficients use the Frobenius norm of the *expanded full symmetric*
derivative tensors, so Cauchy-Schwarz yields, for `||x||_2 <= r`,

`||E(x)-I||_2 <= ||E2||_F r^2/2 + ||E3||_F r^3/6 + ||E4||_F r^4/24`.

The saved norms are approximately 1.17010697, 21371.62485 and 35772.44462.
The unweighted unique E4 norm, 12464.61156, must not replace its full norm.
The base Hessian has `s0 = 0.9999999999999997` and
`h0 = 2.0000000000000004` in floating point.

| Coordinate Ball | Coframe Distance Bound | Cartan Singular Lower Bound | Inverse Norm Upper Bound |
| --- | --- | --- | --- |
| Cartan-only selected r = 1/64 | 0.01381939030 | 0.9202475082 | 1.086664176 |
| Parent temporal r = 1/16384 | 2.989405570e-9 | 0.9999999821 | 1.00000001794 |

The Cartan-only selected ball has perturbation margin 0.8275016743.
Its larger radius does not extend the parent's temporal-block estimates.
The parent report is read only to evaluate the same Cartan bound at its
selected radius; neither parent code nor report is edited.

## Validation And Countercontrols

Seventeen checks at the origin and axis/random boundary points evaluate the
full new quartic fields. They record actual Hessian changes, least singular
values, inverse norms, exact Cartan residuals, and comparisons against both
the original polarized Hessian and the congruence. These samples validate
the implementation; the inequalities above supply the uniform argument.
The maximum polarization discrepancy is zero and the maximum congruence
discrepancy is about 3.85e-16 on these checks.

E4 norm factors 1, 16 and 4096 worsen the fixed-radius estimate. Factor 4096
makes the perturbation margin negative at 1/64 and forces selection of
1/128, where the perturbation margin is 0.6849222526. The congruence bound
still resolves the larger ball. Focused tests additionally scale the actual
E4 field, verify full permutation multiplicities and the pure-quartic
sixteenfold-norm/half-radius identity, exercise coframe distances up to .95,
and reject invalid distances or a zero base singular margin.

The JSON records LF-normalized SHA256 fingerprints for the implementation,
local transitive dependency modules and their available saved reports,
including the joint completion and the parent neighborhood report.
Before/after fingerprint comparison detects input changes during evaluation.

Reproduce with `python -B analysis/HC_Cartan_Joint_Cartan_Regularity.py --output
analysis/HC_Cartan_Joint_Cartan_Regularity.json`, then run only
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_joint_cartan_regularity`.
