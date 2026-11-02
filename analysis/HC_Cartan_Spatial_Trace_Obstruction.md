# Spatial Trace Compatibility: A Direct Obstruction

Date: 2026-10-19. Local, uncommitted work after baseline 5eb266f.
Issue 16 and the OP register were read; no public issue was changed.
Added neutral commuting-spinor odd-cross comparison only. No main TeX,
PDF or published payload was changed.

## What Was Missing

The [complete quadratic audit](HC_Cartan_Complete_Quadratic_Gate.md)
identified a numerical separating combination. A simpler obstruction
can now be read directly from individual equations: 120 spatial C3
components are unaffected by every allowed correction. Their residual
is already about 31.89492 for the chosen witness.

This clarifies the problem's provenance. The arbitrary higher-jet lift
at the earlier 384-row order supplied tangential coefficients that need
not satisfy the later spatial C3 equations. Freezing those coefficients
before attempting the 1114-row completion froze in a nonzero constraint.
The calculations did not establish a fundamental obstruction to nonzero
sources or a physical failure of the comparison model.

## Exact Structural Statement

Use derivative index 0 as the distinguished normal direction. Fix the
lower point and the represented tangential germs of E, E_t, psi and
lambda. Allow precisely the masks from the previous Cauchy calculation:

| Variable | Allowed increments |
| --- | --- |
| psi2 | At least one normal derivative |
| lambda2 | At least one normal derivative |
| E3 | At least two normal derivatives |
| psi3 | At least one normal derivative |
| E4 | At least two normal derivatives |
| lambda3, psi4 | At least one normal derivative |

Let G collect C3_ijk,a,mu for i,j,k,mu in {1,2,3}, with i<=j<=k and
a in {0,1,2,3}. Then G has 10*4*3=120 components and is independent of
all the allowed increments p,w. Consequently

    G(data)=0

is a necessary compatibility condition on these prescribed tangential
data, and in the implemented unweighted residual coordinates

    ||F(p,w)|| >= ||G(data)||.

Proof by the actual evaluator's dependencies:

1. C3 uses psi_ijk and psi_ijkmu. With spatial i,j,k,mu these are fixed
   tangential psi3/psi4 values. Its psi2 factors have only spatial
   derivative indices and are fixed as well.
2. The algebraic Cartan connection differentiated in spatial directions
   uses the corresponding spatial lambda and spinor jets. Its source
   and response derivatives contain no normal psi2 increments. Its
   lower geometric inputs and LC cubic are fixed by the lower point.
3. The LC contribution to omega2_ij uses E3_ijrho. With spatial i,j,
   rho can add at most one normal derivative; every such entry is
   frozen. The corresponding omega3_ijk contribution uses E4_ijkrho,
   again with at most one normal derivative, and is frozen. The
   lambda3_ijk contribution is tangential and frozen.
4. Pairing these fixed jets in `constraint_third`, adding the highest
   connection/principal images, and subtracting E3_ijk cannot introduce
   any allowed increment. This proves the independence without ranks,
   SVD, finite differences, or a small-parameter approximation.

It is important that the tangential germ of E_t is fixed too: E3 and
E4 entries with exactly one normal derivative are part of that germ.
This statement need not hold under a different Cauchy mask. The frame
label a=0 is an internal coframe index, not an extra normal derivative.

## Exact Rational Scalar Check

The selected component is C3_(333),0,2, global zero-based residual row
1100. The code separately implements its repeated-spatial derivative
formula with exact SymPy rational arithmetic. Saved binary input values
are interpreted as exact rationals, not rounded decimal approximations.
No numerical nullspace or numerical rank enters this scalar evaluation.

Two variants are retained:

| Exact evaluation | Approximate display only |
| --- | ---: |
| Freeze the prepared numerical coefficients as rationals | 15.77688059111224403781 |
| Rebuild spin-dependent source/response from rational psi | 15.77688059111016057274 |

The second variant verifies each component form directly against the
rational Clifford matrices, rebuilds source, response and source-component
maps, and checks the frozen Cartan inverse by the exact identity H H^-1=I.
It then recomputes connection derivatives through order three and the
selected C3 component using the same analytic normal-point formulas.
Full exact numerators and positive denominators are saved in the JSON.
In both cases the integer comparison numerator > 15*denominator holds.
Thus the component is strictly larger than 15 in these explicitly
specified rational finite-data models.

Combined with the structural independence, this rules out any allowed
p,w completing this exact saved witness in either rational convention.
This is a direct fixed-data obstruction, not just optimizer failure.
It does not prove nonexistence for nearby or altered tangential data,
and does not certify a full unrounded covariant action or regional PDE.
The older original solution was numerical; its tiny nonzero residuals
are not being promoted to exact rational identities.

## Numerical Cross-Checks and Provenance

| Control | Result |
| --- | ---: |
| All 120 spatial rows at the selected shifted witness | 31.89492155 norm |
| Their allowed 1168-column response | Exactly zero in the assembled array |
| Changes under three simultaneous normal p,w variations | Exactly zero in evaluator output |
| Same rows at the original saved completion | 2.73e-10 norm |
| Same rows with source shift alone, old higher jets | 2.73e-10 norm |
| Difference caused by that source shift alone | Exactly zero in evaluator output |
| Floating value of the selected component | 15.77688059111824 |
| Difference between floating and frozen rational value | 6.0e-12 |

The source basis changes only E2_00 and selected lambda1_0 entries.
These do not enter the purely spatial trace above. The large trace
defect therefore arises with the chosen higher tangential lift, not
from this source shift acting on an otherwise unchanged spatial germ.
The reported norms depend on the chosen residual scaling; they are not
physical observables.

## Next Construction

The next compatible-data problem must impose the spatial C3 equations
while selecting the tangential higher jets, instead of choosing them
from only the earlier 384 equations and then freezing them. Preserve
the earlier conditional source law, or recompute its gate explicitly
if those data change. Satisfying these 120 necessary conditions alone
would still not solve the remaining 994 equations or establish regional
evolution. The subsequent [expanded higher-data construction](HC_Cartan_Compatible_Tangential_Lift.md)
now supplies a numerical replacement at the same lower source point,
by changing the previously prescribed higher tangential data. This does
not remove the obstruction for the old frozen data.

## Reproduction and Verification

Run `python -B analysis/HC_Cartan_Spatial_Trace_Obstruction.py --output
analysis/HC_Cartan_Spatial_Trace_Obstruction.json` from the repository root.
The inherited response matrix uses the existing DI/cache services; the
small exact scalar computation runs directly and needs no new package.

39 focused tests passed: 10 spatial-trace, 8 complete-quadratic, 7
normal-Hessian and 14 previous next-Cauchy tests. They replay the exact
rebuilt rational value, verify invariance after changing every allowed
coordinate, and provide a positive control: changing a forbidden
tangential psi4 entry does change the selected component. The full
repository suite was not rerun for this isolated analysis. No further
agent was spawned after the earlier usage-limit failure.
