# Completed tableau and projection-gate review

30 October 2026. Bounded review at the declared completed system R=(F24,G4,dg4), with the scalar g0 condition imposed on the fixed field values. This review checks the implementation and a local vertical tangent projection at point0; it does not independently derive the physical meaning or all-order completeness of G.

## Packing, symmetric prolongation and flags

Reviewed completed_tableau_check.py against its underlying Taylor model. Its q packing is psi24, then four first-jet blocks of24 (real12,imaginary12 per coordinate), then position4. This matches the current m.pack/m.unpack convention. The J blocks used in A2 and A3 therefore align correctly.

Symmetric second derivatives use ten unordered coordinate pairs with24 real entries each. An off-diagonal variable contributes J_nu to derivative equation mu and J_mu to derivative equation nu, with no factor2. Symmetric third derivatives use twenty unordered triples; for each second-derivative equation pair, each coordinate lambda contributes the appropriate J_lambda block to that triple. These are actual derivative values, not polynomial coefficients, so the lack of permutation multiplicities is correct.

The first flag calculation contracts the four first-symbol coordinate blocks with flag columns, stacks evaluations and takes successive rank increments. The prolonged flag calculation contracts the symmetric second-symbol tensors similarly; using shared pair entries, without a factor2, is the correct contraction. Full wide-matrix SVDs supply complete nullspaces. No packing or contraction error was found.

The recorded numerical counts g1=65, g2=127 and first characters(23,22,19,1) give the bound128. The prolonged characters(65,42,19,1) give bound210, whereas g3=209. Thus sampled flag equality fails by one at both stages. Four agreeing sampled flags are evidence for a generic numerical pattern, not a proof of delta-regularity, constant rank on a neighborhood, analytic involutivity or failure of every further completion. The character comparison alone is not a physical no-go theorem.

## Actual lower-germ repair and gate definition

completed_review_projection_gate.py reuses the authoritative R definitions without changing the source. It reads actual Hessian values from fifth-window-result.json, correctly restoring multiindex factorials. At point0 it obtains J rank31, a65-dimensional vertical first-jet tangent N=ker J, and symmetric A2 of shape128x240 with rank113 and a15-dimensional complete left kernel L.

The saved Hessian already gives total derivative residual norm2.98e-13. A closest least-squares correction of norm3.53e-13 reduces that residual to2.95e-14. R itself has norm7.82e-14. The subsequent gate keeps this repaired Hessian fixed, varies only first jets along all65 N directions, and evaluates

Gate = L^T d_jets[(D R)(q) tangent(q,H_fixed)] N.

The differentiated tangent includes the changing spinor derivative J_mu in its psi rows; omitting this would be an incorrect test. The coordinate and field values are fixed. At a compatible base H, holding the complete left kernel at its base value is valid for this tangent test: derivatives of L multiply the already-zero prolonged residual. Variations of A2 acting on fixed H are included by differentiating the full prolonged expression, not by freezing its coefficient matrix.

This is only the vertical projection test with psi and position fixed. It does not check all tangents of the full first-jet equation manifold that also vary psi or position.

## Finite differences and AD discrimination

All65 tangent columns were tested at central steps1e-4 and1e-5. The resulting gate norms are2.53e-9 and6.19e-9, while the matrix difference between steps is6.65e-9. Nominal relative-only ranks would incorrectly assign rank to numerical noise. An empirical cutoff based on ten times the step difference detects no stable nonzero singular value.

completed_review_ad_gate.py then differentiates the same total derivative expression by Torch AD, with no finite-difference quotient. The full unprojected derivative norm is165.71, but its projected gate norm is5.27e-14 and largest singular value3.28e-14. Its differences from the two finite-difference matrices are2.53e-9 and6.19e-9. Thus the finite-difference signal is consistent with numerical differentiation error, not a detected hidden lower constraint.

The position/background polynomial in the authoritative R contains exact background coefficients through second order, sufficient here: the gate differentiates in first-jet directions at fixed position. No unrepresented third position derivative is needed for this calculation.

## Verdict and remaining boundary

The completed-tableau code passes this bounded packing/flag review. At the tested point, no additional vertical first-jet constraint is detected by the R2-to-R1 projection gate: all65 tested tangent directions have projected defect at AD roundoff. This numerical result supports infinitesimal compatibility in this restricted vertical test. It does not establish analytic surjectivity of the full projection, formal integrability, eventual involutivity, propagation of all constraints, regional existence, or OP5 closure.

In particular the sampled Cartan equality gap and the vanishing vertical source gate address different questions and are not contradictory. A tableau can fail the sampled involutivity test without the present source projection exposing a new lower equation at that point. Further prolongation, regularity and nonvertical projection questions remain open.

Artifacts: completed_review_projection_gate.py/result.json and completed_review_ad_gate.py/result.json. Reproduce the two Python scripts from the repository working directory; they do not optimize scalar data or modify the authoritative model, prior results or repository files. The scripts reuse the declared R evaluator, so this is an independent diagnostic path/code review, not an independent derivation of R from physics.
