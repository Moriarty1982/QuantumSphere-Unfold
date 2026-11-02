# Off-Shell Lorentz Residual Identity After Cartan Elimination

Scope: the explicitly added neutral odd-cross Einstein-Cartan comparison with
commuting spinors, fixed declared M and Q, c=1 and u=0. This is a finite numerical
off-shell audit, not a symbolic or interval certificate, a Cauchy solution, a
native-action identification, or a physical scale determination.

## Identity and Elimination

The independent parent density and Euler conventions are those in
`HC_Cross_Cartan_Parent.py`; the full complex probe Euler density is the
`symmetric` result of `HC_Probe_Law_Revision_Audit.py:real_operator`.
For each of the six elementary Lorentz generators,

```text
J.T eta + eta J = 0,
S_J = -(eta J)_ab Gamma^a Gamma^b / 4,
delta E = J E, delta psi = S_J psi, delta lambda = -J.T lambda,
F = C[Q]-E, F_lambda = -F,
FE:(J E) + 2 Re[(S_J psi)^dagger R] + F:(J.T lambda) = 0.
```

The plus sign in the last term follows from the two minus signs in
`F_lambda` and `delta lambda`. The probe contraction uses all real and imaginary
components, including the weight-divergence and connection-adjoint correction.
No point constraint F=0, probe equation R=0, or coframe equation FE=0 is imposed.
These are undifferentiated residuals, not the previous conditional differentiated
rows evaluated on a solution.

Local Lorentz invariance of the independent parent also involves the connection
Euler expression and its derivative. Substitution of the exact algebraic Cartan
solution makes that expression identically zero as a field expression, so its
derivatives vanish as well. The chain-rule contributions to the remaining
reduced Euler expressions therefore vanish. This explains why the parent FE,
R and F evaluated on the compatible eliminated connection obey the displayed
identity. Merely setting the point value of the connection Euler expression to
zero while choosing an unrelated connection derivative does not suffice.

## Unfitted Compatible Data

Seeds 74181, 74182 and 74183 generate unrelated complex psi and p1, a nonzero
multiplier with all columns present, arbitrary l1, symmetric E2 and independent
higher Taylor coefficients. Only the algebraic 24-component connection equation
is solved; no matter, coframe, constraint, continuation, rank or fitting solve is
performed. The full-current `regular.connection_second` path calls
`spatial.connection_first` and retains the nonzero-lambda reactions.

The initial chart has E=I and dE=0. A nonlinear coordinate map
`y^r=A^r_m x^m+B^r_mn x^m x^n/2`, with B symmetric in m,n,
produces E=A and `d_s E^a_m=B^a_ms`. The multiplier transforms as the vector
density `lambda'=abs(det A) lambda A^(-T)`; its derivative includes the Jacobian
and density derivatives. Omega and its first derivative are pulled back as
connection one-form jets. Thus curvature is computed from an actual compatible
first jet, including the LC(E,dE) part, rather than drawn independently.

The pullback tests independently recompute the full probe residual and verify
`R'=abs(det A) R`, `FE'=abs(det A) FE A^(-T)`, `F'=F A`, and the two-form
curvature transformation. Raw-parent finite differences additionally rebuild
LC, spin maps and the Hessian at displaced polynomial field values, bypassing
the optimized source forms and connection-jet routines. They check all four
first derivative directions in both charts and one mixed second derivative.
The latter is a focused check of the full-current second helper, not an
exhaustive second-jet certificate. Second connection derivatives are not needed
in the undifferentiated residual identity itself.

## Results

The largest absolute identity residual across all 18 sample/generator pairs is
2.45e-15. The fixed regression tolerance is 2e-11.

| Seed | norm F | norm R | norm FE | norm connection Euler | norm dE |
| --- | ---: | ---: | ---: | ---: | ---: |
| 74181 | 1.91832 | 6.07554 | 5.20649 | 4.61e-16 | 1.31780 |
| 74182 | 2.61040 | 6.82378 | 5.35273 | 6.25e-16 | 1.41158 |
| 74183 | 2.60655 | 13.53253 | 31.44914 | 8.41e-16 | 1.18583 |

These are chart-dependent Euclidean component norms. The JSON retains the
actual zeroth constraint residual F0=C[Q]-E, the full complex R, FE, E, dE,
psi, multiplier, and each generator's three signed contractions. Here F0 means
the value of F at the sampled point, not a zero-multiplier source.

For the first seed, halving the raw-parent difference step from 4e-4 to 2e-4
reduces the normal first-connection error from 5.70e-7 to 1.43e-7, the pulled
first-connection error from 8.37e-7 to 2.10e-7, and the mixed second error from
4.10e-7 to 1.01e-7. This is consistent with centered-difference convergence.

Every generator in every sample detects reversing or omitting each of the
three terms. The smallest absolute failed residual for the retained probe-sign
and multiplier-sign reversals is 0.0661. Further controls discard either the real
or imaginary probe residual, or replace it with the ordered operator; all fail.
A separate control changes d omega, hence curvature, while keeping omega and
the pointwise algebraic Cartan residual unchanged; the Lorentz identity fails.
This directly exercises the distinction between pointwise elimination and its
compatible differential consequences highlighted in the independent review.

## Reproduction

```text
python -B analysis/HC_Cartan_Lorentz_Residual_Identity.py
python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_cartan_lorentz_residual_identity.py -v
```

Eight focused tests pass, including the parent-added normalized source
fingerprint check. The JSON pins the local transitive Python dependencies with
LF-normalized SHA256 values and rejects input changes during evaluation.
Only this sidecar's .py/.json/.md files and
`scripts/qsc_audit/tests/test_hc_cartan_lorentz_residual_identity.py` were created.
No shared source or saved input was edited; no full suite, Git operation or new
chat was used. The optional Schur-obstruction recast is outside this audit.
