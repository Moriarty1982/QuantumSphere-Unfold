# Implicit Connection Bound

## Scope And Diagnosis

This calculation concerns only the existing neutral commuting-spinor odd-cross
Einstein-Cartan comparison, not native HC/C7 identification. The fields, fixed
couplings and equations remain unchanged. No new fit is performed. Main
TeX/PDF and published payloads remain unchanged.

The [isometric curvature enclosure](HC_Cartan_Isometric_Curvature_Bound.md)
leaves curl uncertainty dominant. Instrumenting the existing connection
construction attributes almost all connection derivative uncertainty to the
algebraic Cartan term, not the Levi-Civita term. At radius 1/16384 the latter's
derivative tails are about 3.2e-9 to 3.6e-9, compared with total connection
derivative tails about 0.00775 to 0.00800.

Two separately recorded controls improve the Cartan part: its fixed basis
embedding and the derivative of its implicit linear system.

## Fixed Basis Embedding

Let B be the existing 64-by-24 matrix mapping the Cartan coefficients k into
the lower-index connection. Its stored entries are integers. Exact arithmetic
gives

```text
B^T B = 2 I_24,
||B||_2 = sqrt(2).
```

Every nonzero input attains that ratio of positive Euclidean component norms.
The previous generic contraction used the Frobenius factor sqrt(48). Applying
B jointly therefore replaces that factor by sqrt(2) for both connection values
and each separately controlled physical derivative. The dyadic upper constant
1.4142135623730951 has exact rational square at least two. The map's dimension
or rank does not identify physical source sectors.

## Implicit Physical Derivative

The existing algebraic connection solve is H k=f, with H the Cartan Hessian
and f the unchanged source/multiplier right side. The old product-rule path
computes

```text
dk = -(H^-1 dH H^-1) f + H^-1 df.
```

The new path evaluates the equivalent identity

```text
H dk = df - (dH) k,
dk = H^-1 [df - (dH) k].
```

This is an algebraic derivative identity, not an additional field equation.
It combines terms before the final inverse multiplication and avoids separately
bounding a differentiated inverse matrix times the source. It does not omit
the dH term or freeze the Hessian. The inverse value, all product tails and
discarded high-degree coefficients remain enclosed by the existing Taylor
arithmetic. Physical dH and df models are built from the field polynomial and
controlled derivative identities, not by differentiating an unknown remainder.

The previous product-rule evaluation is retained as a control. A second control
changes only the basis embedding, so the two improvements are not conflated.
The independently implemented original connection/first-derivative evaluator
also checks the new path off shell and at shared neighborhood points.

## Recomputed Results

At radius 1/16384 the four connection derivative tails change as follows:

| Coordinate | Old | Basis Only | Basis And Implicit Derivative |
| --- | ---: | ---: | ---: |
| 0 | 0.007997838 | 0.001632555 | 0.000368352 |
| 1 | 0.007746753 | 0.001581302 | 0.000317103 |
| 2 | 0.007909775 | 0.001614579 | 0.000350374 |
| 3 | 0.007996058 | 0.001632191 | 0.000367993 |

The connection value tail decreases from 0.000106275 to 0.000023133. The
retained value coefficients agree exactly; the derivative coefficient arrays
change by about 4.31e-16 in Frobenius norm from regrouping roundoff.

The latest isometric-curvature, restricted-Ricci and joint-exterior-curl
evaluators are then recomputed with this same connection:

| Quantity | Radius 1/16384 | Radius 1/32768 |
| --- | ---: | ---: |
| Previous coframe tail | 0.046274514 | 0.001442014 |
| New coframe tail | 0.003432194 | 0.000106443 |
| Previous curl tail | 0.138006485 | 0.004299086 |
| New curl tail | 0.007877813 | 0.000243714 |
| Previous combined 80-row upper estimate | 0.155646041 | 0.004846335 |
| New combined 80-row upper estimate | 0.055788969 | 0.001730936 |

Constraint and probe rows deliberately retain their earlier coefficient arrays
and enclosures; they describe the same mathematical fields and connection.
Their tails at the larger radius are about 0.02702 and 0.04805. The inherited
probe enclosure now dominates. Thus improvements to curl/coframe alone cannot
remove the remaining combined bound. The new 80-row coefficient difference is
about 1.20e-15, and nonzero degree-three/four defects remain explicit.

## Verification And Remaining Gap

Eight focused tests cover the exact embedding Gram matrix and saturation;
implicit/product-rule polynomial agreement; uncertain inverse, source and
physical derivative inputs; invalid/unresolved inverse rejection; off-shell
connection and first-derivative agreement with the independent original
evaluator; input fingerprints; unchanged first 40 rows; the two separate
improvement controls; and original-equation sample checks. Samples include an
axis, two cube corners and an interior point, and separately compare connection
value and derivative errors with their tails. The two radius cases use two
local workers.

Exact certificates apply only to fixed linear constants. The nonlinear
enclosure remains binary64 without full outward rounding. Sample agreement
does not prove a whole-region estimate, and all retained low-order errors remain
nonzero. Neither exact low-order closure, regional PDE compatibility,
convergence nor distance to an exact solution follows from these numbers.

The executable and JSON report share this note's filename stem.
