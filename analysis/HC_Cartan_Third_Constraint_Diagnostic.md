# Third Constraint Gate and Frozen-Jet Failure

This continues only the explicitly added neutral odd-cross Cartan comparison.
It neither changes the main TeX paper nor identifies its native gravity,
couplings, frames or physical scales. No superconducting interpretation is used.

## Fixed Inputs

The input is the strongest saved 1200-coordinate jet in
`HC_Cartan_Next_Scalar_Compatibility.json:joint_394_system.jet_coordinates`.
The lower point, Q, Hermitian M, Einstein coefficient 1 and vacuum 0 are kept.
The earlier 394-component residual is about 7.04e-11. No earlier derivative is
refitted here. Input-source hashes of that report are checked before evaluation.

The new unknowns are fourth spinor derivatives (840 real coordinates), fourth
coframe derivatives (560), and third multiplier derivatives (320). There are
320 third-constraint components in unique sorted derivative-triple coordinates.

## Exact Spinor Block

Let L be the surjective real 4-by-24 spinor pairing map at the fixed psi.
For F=C[Q]-E, the highest-spinor part of its third derivative is

    (P psi4)^a_(ijk;mu) = L^a(psi4_(ijkmu)).

Its image is fully symmetric in all four coordinate slots, not just i,j,k.
Consequently its rank is 4*35=140, its kernel dimension is 840-140=700, and
its cokernel dimension is 320-140=180. These counts follow analytically from
surjectivity and symmetry; they are not a floating-point rank guess.

For every unique quartet, equality of its rows gives independent compatibility
conditions. There are 180 such scalar equalities. Listing every differentiated
curl instead would produce 240 rows with 60 dependencies. The implementation
uses the independent equalities and an orthogonal projection in the explicitly
declared, unweighted unique-triple component norm.

## Do Coframe and Multiplier Derivatives Remove the Rest?

With all lower jets fixed, the third constraint is affine:

    C3 = b + P psi4 + B_E E4 + B_lambda lambda3.

For the new highest connection derivatives only,

    delta omega3 = LC_LINEAR(E4) + unpack(H^-1 L_response^T lambda3).

The algebraic Cartan source and H derivatives do not acquire third-order terms
from E4 or psi4; those fields begin at degree four. Their nonzero lower-order
contributions, including the nonzero multiplier value, remain in b. The new
connection contribution to C3 is the full Q-weighted spinor pairing with
`spin_lift(delta omega3) psi`. Thus it is not valid to drop connection terms
when projecting the differentiated curls.

After projecting out the 140-dimensional spinor image, the numerical ranks are:

| New connection variables | Projected rank |
| --- | ---: |
| E4 only | 95 |
| lambda3 only | 125 |
| E4 and lambda3 together | 135 |

The combined smallest retained singular value is about 4.60 and the next is
about 1.46e-13. This is a clear numerical gap, not an exact arithmetic rank
certificate. The full C3 map consequently has numerical rank 275 and leaves
45 compatibility directions beyond all three new jets.

## Frozen Source and Controls

The source b is evaluated on the saved cubic coframe/spinor and quadratic
multiplier Taylor fields. At each displaced sample the actual algebraic Cartan
connection is recomputed. Central third differences use h=1e-3, 5e-4, 2.5e-4,
with Richardson extrapolation. Repeated and mixed derivative indices are both
included. Successive central changes have norms 18.7585 and 4.68937, a ratio
near four. The last two extrapolations differ by about 0.00246831; their
projected difference is about 0.00169989. These are stability indicators, NOT
certified error bounds.

| Quantity | Unweighted component norm |
| --- | ---: |
| Frozen C3 source | 260390.585 |
| Residual after best psi4 alone | 235125.066 |
| Residual after all new psi4, E4, lambda3 | 26799.511 |

The final residual is recomputed in all 320 components, not merely in the
projected or selected rows. The saved JSON retains the source, new jet
coordinates, full residual and singular values. The minimum-norm fit is a
diagnostic of failure, not a successful continuation or a new authoritative jet.

An independent control adds random quartic coframe/spinor and cubic multiplier
fields to the actual Taylor evaluator, resolves Cartan at each sample, and
compares the third derivative of the changed constraint against the analytic
highest-jet map. For response norm about 390.614, the coarse and fine errors
are about 0.07560 and 0.01890; the extrapolated error is about 0.000349.
The control includes Taylor factorials and repeated indices independently.

The companion `HC_Cartan_Second_Probe_Diagnostic.md` also finds a nonzero frozen
full second probe derivative, norm about 10453.163. A solved scalar Hessian does
not imply that full vector equation. That probe diagnostic alone does not test
whether new multiplier derivatives could repair it.

## Consequence and Next Calculation

Numerically, the particular saved 394-completion cannot be extended by only
appending the new jets: even C3 alone has a large unreachable residual. A joint
R2/FE2/C3 extension with those lower jets frozen cannot repair that failed
necessary condition. This is strong controlled numerical evidence, not a
symbolic nonexistence theorem or an obstruction for every possible lower jet.

The appropriate next calculation is to expose the 45 left-null compatibility
conditions and reprepare the earlier psi2/lambda2/E3/psi3 data subject to the
old 394 conditions and the new constraints. Such reoptimization need not remain
affine. R2 also depends on the already chosen psi3 and E3, so adding only still
higher spinor derivatives cannot fix that equation. The full FE2 equation was
not assembled here because the frozen C3 necessary condition already fails.

No formal integrability, PDE propagation, convergent solution or local-existence
claim follows. The component norms and coordinate steps are not physical units.

## Reproduction

```text
python -B analysis/HC_Cartan_Third_Constraint_Diagnostic.py --output analysis/HC_Cartan_Third_Constraint_Diagnostic.json
python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_cartan_third_constraint_diagnostic.py
```

Independent parallel review confirmed the spinor rank/cokernel derivation and
the need to retain E4/lambda3 connection responses. The parent implemented and
cross-checked those response maps; the other worker independently implemented
the frozen R2 diagnostic. All prior input artifacts remain unchanged.

Verification: 18 focused C3 tests and seven R2 tests pass within the complete
1,960-test audit checkout, plus 34 separate OP5 checks. Six of the checkout's
audit tests are pre-existing unrelated uncommitted metadata-hygiene work.
The unchanged main-document preservation check also passes.
