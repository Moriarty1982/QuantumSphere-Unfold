# Constitutive Transport: the Missing Closure Condition

Date: 2026-10-18. Added neutral commuting-spinor odd-cross Cartan comparison
only. No native action, frame identification, scale or main TeX/PDF change.

## Exact Identity

The [independent derivation](HC_Cartan_Constitutive_Transport_Derivation.md)
uses the complete algebraically eliminated connection and defines F=C-E.
In a fixed coordinate/readout trivialization its exact transport identity is

    partial_t F^a_i = partial_i F^a_0 + J^a_0i,
    J = dC-dE = dF.

The explicit formula for J contains first spinor derivatives and derivatives
of the connection, but no freely chosen symmetric spinor Hessian. The latter
cancels by commutation of coordinate derivatives. Connection derivatives still
contain derivatives of their underlying fields. A curvature-only rewriting
that omits the readout compatibility terms is generally wrong; a negative
control checks this explicitly. Ordinary dE is not Cartan torsion.

If F_0 and J_0i vanish AS FUNCTIONS on a coordinate product region, initial
F_i=0 is retained along each vertical time segment. This conditional fact does
not prove J_0i=0 from the remaining parent equations. In particular, it cannot
remove the open-set R=F=0 assumption of the gravitational subsidiary theorem.

## New Explicit Point-Jet Control

The numerical control starts from the latest saved joint 1114-component
completion, not the older frozen incompatible preparation. It keeps Q, M,
the action coefficients, psi at the point, lambda at the point, all first
coframe derivatives, and all non-temporal entries of the 56 normal unknowns
fixed. A unit direction in the original normal kernel varies only E_,00,
psi_,0 and lambda_,0. This is not a parameter refit or an extra gauge claim.

The original normal block has numerical rank 34. Appending twelve mixed curls
raises it to 40; their restriction to the original kernel has rank six.
The maximum-response singular vector supplies a reproducible witness, with
its sign fixed by the largest component. A symmetric spinor Hessian correction
then cancels all first spatial F derivatives and all derivatives of F_0 at
the point. The antisymmetric mixed defect cannot be removed in this way.

For normal amplitude 0.01, direct unprojected recomputation gives:

- All 56 original point equations: norm 1.08e-14.
- All first spatial constitutive derivatives: norm 1.61e-13.
- All derivatives of the temporal constitutive column: norm 1.31e-13.
- Time derivatives of the spatial constitutive columns: norm 0.3820506011.
- Mixed curl defect: norm 0.3820506011.
- Independent product-rule/transport checks: errors below 2e-13.

Opposite amplitude reverses the drift and doubled amplitude doubles it, to
floating precision. At zero amplitude the original joint jet is recovered
up to the tiny Hessian correction, with vanishing drift to about 1e-13.
The size is in comparison-model coordinates, NOT a measured physical rate.

The adjusted Hessian is intentionally NOT asserted to retain the 1114-component
completion. Indeed the frozen-higher-data first probe derivative has norm
0.0829222897 for the perturbed witness, versus about 7e-12 at zero amplitude.
This explicit failed prolongation control prevents confusing the witness with
a solution of the full field equations on a neighborhood. First spatial
constraints at one point are likewise not data on an entire Cauchy surface.

## What This Resolves and Leaves Open

The result establishes a precise non-implication: the unprolonged normal point
equations and vanishing first spatial constitutive jets do not force mixed
constitutive transport. It does NOT disprove that a complete reduced parent
system, including its differential consequences, can propagate constraints.
It does NOT establish impossibility, instability or extra physical modes.

The next closure calculation must incorporate the six effective mixed-curl
conditions and six affine compatibility combinations into the coupled probe,
multiplier and gravitational reduction. Those regional equations must be
derived as differential consequences or justified as an equivalent constrained
reduction, rather than simply imposed as a new physical law. Their own
compatibility and the remaining multiplier directions still need control.

The saved [report](HC_Cartan_Constitutive_Transport.json) pins LF-normalized
source fingerprints and the authoritative joint data. Twelve focused tests
cover the general coordinate product rule, actual-field differences,
curvature-rewriting omission controls, Hessian symmetry, numerical ranks,
fixed inputs, signed amplitude response and failed first-probe prolongation.
All calculations use floating arithmetic, not interval or exact rank proofs.

Verification: all 2,068 audit tests and 34 separate OP5 checks passed (2,102
total), including twelve new transport checks. The full-monolith preservation
and whitespace checks passed. No commit, push or PDF build was performed.
