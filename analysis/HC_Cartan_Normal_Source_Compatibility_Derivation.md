# Finite Higher-Jet Compatibility of the Six Normal Sources

Date: 2026-10-18. Independent bounded derivation for the added neutral Cartan
comparison. The parent owns the actual 384-by-1200 matrix A, 384-by-6 response
B, their numerical ranks, and all solves. This sidecar derives the finite
linear algebra and checks its affine hypothesis by reading the implemented
equations. No matrix assembly, large solve, test suite, or new saved-data
validation was performed here.

## Data and Coordinate Convention

Use one matching tuple `(prepared, point, jets, extras, report)` returned by
`HC_Cartan_Joint_Neighborhood.load_data()`, and construct the six columns U
with `HC_Cartan_Normal_Source_Reduction.build_reduction(prepared, point)`.
The loader reads `HC_Cartan_Next_Joint_Completion.json`, checks its source
fingerprints and scalar-completion fingerprint, and checks exact retention
of the saved spinor Hessian. It reconstructs the matching psi2, lambda2, E3,
psi3 and extras E4, lambda3, psi4. These are the latest saved joint data,
not a newly fitted point. This statement describes the loader's checks;
this sidecar has not executed them. The parent's calculation should retain
the matching input fingerprints with its numerical results.

Do not substitute `Remaining_Multiplier.load_data()` or
`Regular_Gravity.load_data()`: they load older completions. Using the
remaining-multiplier module's `normal_point` and `canonical_basis` helpers
does not require invoking its old loader. Do not mix the current point
with old higher coefficients or extras.

Fix prepared data, psi0, psi1, lambda0, E=I, dE=0, all spatial lower data,
the ten selected leading gauge coordinates, and the normal-equation target.
Here the latter two increments are zero. Let q be a real six-vector and set

    point(q) = normal_point(point, U q).

In this chart U changes only E2[0,0,a,mu] and lambda1[0,a,i] with i=1,2,3.
It leaves psi1 and lambda1[0,a,0] unchanged. The canonical columns have this
support; projecting off the displayed gauge span preserves it: that span
has only E2 components, so cannot introduce spinor or multiplier entries.
All other lower entries remain fixed. This is the restricted variation used
below, not an arbitrary displacement of the 56 normal coordinates.

Write z in the real unique-symmetric coordinate convention of
`Regular_Gravity.unpack`:

| Block | Real coordinates | Slice |
| --- | ---: | --- |
| psi2 increment | 240 | 0:240 |
| lambda2 increment | 160 | 240:400 |
| E3 increment | 320 | 400:720 |
| psi3 increment | 480 | 720:1200 |

Set `jets(z) = jets + unpack(z)` blockwise. These are increments about the
loaded jets, not absolute replacement coefficients. Symmetry and complex
realification follow the existing unpackers. The coordinate Euclidean norm
used below is not the full-tensor Frobenius norm with permutation weights.
Allowing all 1200 coordinates is a new completion problem: psi2 is allowed
to change here, although the saved later joint fit retained it.

Define the actual residual

    H(q,z) = Regular_Gravity.equations(prepared, point(q), jets(z))["vector"].

Its rows are C1 (64), realified R1 (96), FE1 (64), and the ten symmetric
C2 pairs (160), totaling 384. This is not the later 1114-row residual;
extras do not enter this evaluator. Keep the computed origin h0=H(0,0),
including its floating-point residual, rather than silently setting it to zero.

## Why This Residual Is Jointly Affine

Read `Regular_Gravity.connection_second` and `equations`, together with
`Spatial_Propagation.connection_first` and `first_probe`. At the fixed
lower point their dependency structure is as follows. All assertions of
affinity are over real coordinates, including real/imaginary spinor parts.

1. omega0 and its spin lift b0 depend on fixed psi0 and lambda0. They do
   not depend on q or z. `connection_first` makes omega1 a fixed term plus
   a linear map of E2 and lambda1. Thus omega1 depends affinely on q and
   is independent of z. Recompute it for each changed point; passing the
   saved `first_connection` would freeze a required part of the response.
2. In `connection_second`, source_second is linear in psi2 and E2 plus
   the fixed psi1-pair term. response_first is fixed; response_second is
   linear in psi2 plus a fixed psi1-pair term. hessian_second is linear
   in E2. Its product with k0 uses fixed k0. The remaining terms are
   response_second times fixed lambda0, fixed response_first times lambda1,
   and lambda2 times fixed prepared response. Multiplication by the fixed
   inverse Hessian and addition of the linear E3 Levi-Civita term yield
   omega2 affine jointly in (q,z). There is no E2*psi2, lambda1*psi2,
   E2*lambda2, or omega1*omega1 term in this formula.
3. cov0 is fixed. cov1 is psi2 + b1*psi0 + b0*psi1. cov2 is psi3 +
   b2*psi0 + b1*psi1 in each differentiated slot + b0*psi2. Every variable
   factor is paired with a fixed factor. Consequently C1 and C2 are affine;
   in particular C2 pairs psi2 with fixed cov0 and psi1 with cov1, and
   subtracts E2 linearly.
4. curvature0 is affine in omega1 because omega0 is fixed. The implemented
   curvature1 polarization subtracts the quadratic pure-omega1 term:
   `curvature_upper(omega0+w) - curvature_upper(omega0)`
   `- curvature_upper(w) + curvature_upper(0,dw)`.
   Its surviving terms are bilinear in fixed omega0 and w=omega1, and
   linear in dw=omega2. Thus curvature1 is jointly affine. FE1 combines
   this with x1, fixed mass/psi1 terms, and linear lambda1; it introduces
   no product of two varying factors.
5. In `first_probe`, w0 is fixed; w1 is linear in lambda1; w2 is linear
   in E2 and lambda2. z0 uses w1 and fixed b0,w0. z1 uses b1*w0,
   b0*w1, w1*b0, w0*b1, and the trace of w2. The probe then uses
   w1*cov0, w0*cov1, z1*psi0, and z0*psi1, with the indicated fixed
   factors. Neither w1*cov1 nor b1*w1 occurs at this order.

Hence there are constant real matrices, in these fixed coordinates,

    H(q,z) = h0 + B q + A z,
    A : R^1200 -> R^384,    B : R^6 -> R^384.

There are no q*z, q^2, or z^2 terms in this evaluator under these hypotheses.
This follows from the displayed formulas, not merely from separate affinity
tests with z=0 or q=0. Equivalently, A's columns are H(0,e_j)-h0 and B's
columns are H(e_i,0)-h0; these unit differences equal derivatives exactly
in exact arithmetic. The parent's finite-difference assembly is subject to
roundoff. Its A must represent increments about these same latest jets.

## Necessary and Sufficient Compatibility

Let r=rank(A), and let L have 384-r orthonormal columns spanning ker(A.T).
This L belongs to A, not to the earlier 68-row normal system. Finite real
linear algebra gives

    range(A) = ker(A.T)^perp,
    A A^+ = I - L L.T.

For any prescribed q, a higher increment z exists with H(q,z)=0 if and
only if

    L.T (h0 + B q) = 0.

Necessity follows by left multiplication of the residual equation by L.T.
For sufficiency the condition puts -(h0+Bq) in range(A), where A A^+
is the identity. Define

    J = L.T B,    c = -L.T h0.

The exact source gate is therefore J q = c. It accounts for changes in
the higher jets rather than demanding that the frozen higher residual vanish.
Replacing L by any other orthonormal frame changes neither compatibility
nor rank(J).

There is at least one admissible q precisely when c belongs to range(J).
Equivalently, K.T c=0 for a basis K of ker(J.T). If this holds, all sources are

    q = J^+ c + V v,

where the columns of V span ker(J), and v is arbitrary in R^(6-rank(J)).
Thus the admissible set is an affine subspace of dimension 6-rank(J),
provided it is nonempty. In particular:

- rank(J)=6 gives one admissible q only if the gate is consistent.
- rank(J)=0 gives every q if c=0, and no q otherwise.
- If h0 is exactly zero, c=0 and the admissible set is ker(J).

In general

    rank(J) = rank([A B]) - rank(A) <= rank(B) <= 6.

The previously reported frozen-higher rank(B)=6 says the six columns produce
independent residual changes when z=0. It does not say rank(J)=6: some or
all of those changes can lie in range(A) and be absorbed by a higher lift.
Even B of full column rank is compatible with J=0. The parent must compute
J and its gate before drawing a conclusion about admissible q; this sidecar
supplies no numerical rank for A or J.

## Minimum Higher Lift and Its Gate

For a compatible q write d=h0+Bq and choose a matrix Z whose columns span
ker(A). Every exact higher lift, and only such a lift, is

    z = -A^+ d + Z w,    w in R^(1200-r).

Indeed A(-A^+d)=-d under the gate; differences between two solutions lie
in ker(A). The particular lift z_min=-A^+d lies in range(A.T), perpendicular
to ker(A), so uniquely minimizes the declared Euclidean increment norm.
It minimizes z for that prescribed q, not jointly over both q and z.
Its minimality is coordinate-dependent and carries no physical selection rule.

Do not apply the inverse without checking compatibility. For an incompatible
q the same formula is only a least-squares correction and leaves

    H(q,-A^+d) = (I-A A^+)d = L L.T d,
    ||H(q,-A^+d)||_2 = ||L.T d||_2.

An arbitrary Z w cannot remove this obstruction. Numerical compatibility
requires a declared rank cutoff and residual tolerance, a retained/discarded
singular-value gap, and direct recomputation in the actual equations.
Acceptance within tolerance is not exact solvability certification. A tiny
saved h0 may create a tiny nonzero c; report it rather than assuming that
the saved point is an exact solution or that q=0 automatically passes.

## Limits at the Next Order

This affinity statement is specific to C1/R1/FE1/C2 with the fixed lower
data above. At the next order, differentiated expressions can contain
omega1*omega1, b1*psi2, w1*cov1, and terms coupling E2 to higher coefficients.
For FE2, the second curvature derivative already permits products of first
connection derivatives. Such terms can produce q^2 or q*z; if lower jets
are also allowed to vary more generally, additional products appear.
Cancellations along these particular source columns require a fresh proof.
The later joint completion's affinity in its own variables at a frozen point
does not establish joint affinity when that point varies with q.

Changing psi2/lambda2/E3/psi3 can invalidate later equations and any estimates
tied to their saved values. The 384-row gate is necessary and sufficient
only for this stated finite completion problem. It does not preserve the
later 1114-row completion automatically and does not classify the remaining
kernel as gauge or as physical modes. It neither permits arbitrary regional
source functions nor proves mixed-derivative integrability, propagation,
hyperbolicity, regional existence, or native-model identification.
