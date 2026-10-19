# Refreshed Probe And Constraint Bounds

## Scope

This calculation updates the first 40 equations of the existing neutral
commuting-spinor odd-cross Einstein-Cartan comparison with the
[improved connection enclosure](HC_Cartan_Implicit_Connection_Bound.md).
It changes no fields, fixed parameters, equation contractions or fitted
coefficients. Main TeX/PDF and published payloads remain unchanged. This is not
a native HC/C7 identification.

The preceding combined 80-row estimate still inherited the original constraint
and probe tails, about 0.02702 and 0.04805 at radius 1/16384. Those bounds remain
valid, but do not yet exploit the smaller uncertainty in the connection value.
Here they are recomputed rather than reused.

## Same Primary Equations

The construction retains the original spin connection S, covariant spinor jet
D psi, and weight matrices W. Schematically the unchanged primary equations are

```text
C = Im(psi^dagger Q [frame weights] D psi) - e,
P = i W^mu D_mu psi - v [mass weight] psi + (i/2) A psi,
A = partial_mu W^mu - (S_mu)^dagger W^mu - W^mu S_mu.
```

The actual contractions, index ordering, channel ordering, signs and factors
are identical to the earlier full Taylor evaluator. Kinetic, mass and balance
terms remain separately bounded. The probe's twelve complex components are
packed as twelve real followed by twelve imaginary components. This real-linear
packing is isometric, so its tail is retained without an extra factor.

Neither primary equation needs derivatives of the connection itself: only its
value enters S. Thus the gain in this calculation comes from the preceding
improvement in the connection value, not from reusing its smaller first
derivative tails as an additional gain. The physical derivatives of W remain
essential. They are rebuilt from the known derivatives of the coframe, inverse,
volume and multiplier, including dA_inv=-A_inv (de) A_inv. No unknown value
remainder is differentiated.

## Recomputed Results

| Quantity | Radius 1/16384 | Radius 1/32768 |
| --- | ---: | ---: |
| Previous constraint tail | 0.027021901 | 0.000838376 |
| New constraint tail | 0.005886709 | 0.000182719 |
| Previous probe tail | 0.048045665 | 0.001490818 |
| New probe tail | 0.010468426 | 0.000324966 |
| Unchanged coframe tail | 0.003432194 | 0.000106443 |
| Unchanged curl tail | 0.007877813 | 0.000243714 |
| Previous combined 80-row upper estimate | 0.055788969 | 0.001730936 |
| New combined 80-row upper estimate | 0.014767572 | 0.000457947 |

All stored 80-row coefficient arrays are bitwise unchanged in this evaluation.
The last 40 coefficient rows and their enclosures are inherited unchanged. The
new first-40 bounds are combined with those existing coframe/curl bounds by a
root sum of squares, since these are disjoint output components.

At the larger radius, the probe tail consists of about 0.003829076 kinetic,
0.000000296 mass and 0.006639053 balance uncertainty. The weight-divergence tail
is about 0.000002710 and remains present. Probe uncertainty still dominates,
with most of it in the balance term. This diagnostic suggests inspecting the
joint spin/weight contractions next, not interpreting the improved bound as
smaller actual equation errors.

## Verification And Limits

Eight focused tests check complex/real packing and its full tail; invalid shape
rejection; nonzero off-shell agreement with the original equations; the
multiplier derivative's effect on the probe; explicit independence from
connection derivative inputs; input fingerprints; bitwise coefficient
preservation; unchanged last-40 enclosures; all retained probe terms; nonzero
low-order defects; and original-equation sample controls at two radii. The two
radius cases are recomputed with two local workers.

The retained degree-three/four coefficient defects are not fitted again or set
to zero. The combined estimate is still much larger than sampled residuals and
remains a binary64 majorant without full outward rounding. Samples do not prove
a whole-region estimate. Exact low-order closure, regional PDE compatibility,
convergence, native identification and distance to an exact solution remain
unproved. Crossing one or any other arbitrary numerical threshold is not an
existence criterion.

The executable and saved JSON report share this note's filename stem.
