# Review of next completed projection: scalar Omega gate

30 October 2026. Bounded code review and direct directional differentiation of the declared R=(F24,G4,dg4). This does not derive a physical Omega equation or prove an analytic rank theorem.

## Conventions and implementation

Reviewed completion_omega_probe.py. The order3 symbol uses ten derivative multiindices and twenty spinor multiindices; the order4 symbol uses twenty and thirty-five respectively. The factors alpha_mu+1 match normalized coefficients partial^alpha/alpha!, and the per-coefficient real12/imaginary12 packing matches the reused field evaluator. The reported ranks271 and528 give a209-dimensional third-jet tangent and112-dimensional fourth-source left gate. Complete SVD bases are retained.

All lower coefficients0..2 are fixed. Third coefficients vary in ker A3. Since the completed R is first order in psi, these directions preserve its degree2 equations to linear order; at fixed lower jets the dependence on the third jet is affine, so they should preserve that degree exactly in exact arithmetic. They do not preserve every higher compatibility equation automatically.

The completed coefficient evaluator computes the coframe and its inverse series with the correct noncommutative Neumann ordering. Am is the real representation of psi†Q, K is its convolution with the inverse-coframe barred Clifford symbol, and the K/dF contraction uses the same index order as the direct declared pointwise R. Scalar g is formed before differentiating. Keeping F through degree4 is sufficient for completed R through degree3; the synthetic zero derivative slot at degree4 is not used by those retained rows. Spinor degrees4 and5 are set to zero only to define the higher-source representative; free fourth derivatives are subsequently eliminated through A4.

## Direct crosscheck independent of coefficient differentiation

omega_review_direct.py constructs the SAME truncated cubic spinor as an explicit one-variable polynomial along a coordinate direction. It obtains its first derivatives by differentiating that polynomial, packs q(lambda), and differentiates the declared original pointwise R(q(lambda)) directly. The background Taylor is rebuilt through degree4: R includes first background derivatives, so degree3 differentiation requires fourth background derivatives. Monomials use multiplication rather than a problematic zero exponent in AD.

For the time-axis direction, direct automatic derivatives divided by ordinary degree factorials agree with the normalized completed series at degrees0..3 with errors2.72e-14,1.24e-13,7.21e-14,3.06e-12. The degree3 coefficient norm is272.57. A mixed direction(1,0.2,-0.3,0.4) gives errors2.72e-14,1.40e-13,1.99e-13,2.47e-12, with degree3 coefficient norm191.66. This corroborates the K-series/source implementation and factorial translation in an independent evaluation path. The reviewer does not infer exhaustive correctness of every coefficient from these two directions.

## Recorded Omega evidence

The parent probe records a projected source derivative of shape112x209 with first singular value0.5494780051 and second singular value2.93e-12. Thus its rank-one pattern is widely separated from the observed arithmetic error; the value0.549 is coordinate/norm dependent, not a physical constant. Sampled A4 coefficient columns agree to below4e-12.

The recorded finite perturbations along the dominant third-jet tangent have sizes1e-3 and1e-2. They leave the retained lower completed coefficients changed by only about1e-12 but produce best fourth-source residuals0.0005494772 and0.0054947792, matching the dominant-gate prediction. Removing the scalar projection brings those residuals back to about9.6e-10. The baseline higher-source compatibility residual is about1.28e-9, so these are numerical finite witnesses with a large separation of scales, not exact certified counterexamples.

These finite controls support the interpretation that one new source condition is visible in this next projection, unlike the earlier R2-to-R1 test. The earlier zero gate and this later nonzero gate address different derivative orders and are not contradictory.

## Boundary

The evidence does not establish exact rank one in an analytic neighborhood, a complete intrinsic formula for Omega, all subsequent propagation identities, a regional existence/no-go theorem or OP5 closure. A useful next step is to derive the scalar gate in coordinate-independent or explicitly declared coordinate form, append its actual lower-order condition, and revisit the completed system. A bounded nonlinear failure after appending it would still not by itself prove impossibility.

Reviewer writes only omega_review_direct.py/result.json and this omega_review.md. No fitting, old-result edits, shared-model changes or repository writes are performed.
