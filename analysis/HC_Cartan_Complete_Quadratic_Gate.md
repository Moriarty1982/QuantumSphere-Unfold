# Complete Quadratic Gate and a Separating Equation Combination

Date: 2026-10-19. Local, uncommitted work after baseline 5eb266f.
The OP register and issue 16 were read; no public issue was changed.
This is the added neutral commuting-spinor odd-cross comparison, not
native HC/C7 or a regional existence construction. Main TeX/PDF unchanged.

## Fixed Problem

Continue the [normal-Hessian calculation](HC_Cartan_Normal_Hessian_Completion.md).
Freeze the same six source values, lower point, couplings, and prescribed
tangential jets. The free increments are p in R^96 (normal psi2) and
w in R^1168 (368 earlier and 800 highest allowed coordinates). No
tangential datum is silently adjusted to make the system solvable.

The [source-reading derivation](HC_Cartan_Normal_Hessian_Gate_Derivation.md)
gives, in exact arithmetic for the analytic evaluator,

    F(p,w) = b + J p + (0_794 ; C m(p)) + A w,

where m(p) lists all p_i*p_j with i<=j. A is independent of p. This
follow-up constructs every column of C analytically from the pairing,
instead of sampling a few directions of a nonlinear fit.

## Complete Coefficients

Let V_i be the inserted symmetric complex psi2 tensor for real coordinate
i. For each triple (r,s,t), form the Hessian coefficient from

    Im sum_(a,b,c) [pair((V_i)_bc, (V_j)_a, Q)
                   + pair((V_j)_bc, (V_i)_a, Q)],

with placements (r,s,t), (s,r,t), and (t,r,s). Off-diagonal entries are
the coefficient of p_i*p_j; diagonal entries are divided by two.
The first 794 residual rows have no quadratic terms. Complex basis
vectors are interpreted over the reals: there are 96 real directions,
not 96 independent complex directions.

This yields C of shape 320 by 4656. If L spans ker(A.T), the complete
projected quadratic coefficient matrix is L_C3.T C, not a directional
test. The measured values are:

| Quantity | Value |
| --- | ---: |
| Numerical rank A | 568 |
| Left-gate dimension | 546 |
| Norm of all raw quadratic coefficients | 29.39387691 |
| Norm of all projected coefficients | 4.41e-12 |
| Largest projected column norm | 4.02e-13 |
| Rank of projected 96-column J | 96 |
| Remaining affine gate norm | 31.94761833 |

All 4656 columns are therefore numerically absorbed by the older/highest
response. This is stronger than the previous three-direction evidence,
but a floating-point nullspace is still not an exact symbolic certificate.

## Separating Combination

Let B=L.T J, g=L.T b, and r=g-B B^+g. The implementation chooses

    y = L r / ||r||.

Its full 1114 coefficients are saved in the JSON report. Numerically:

| Control | Value |
| --- | ---: |
| Norm y | 1 |
| y.T b | 31.94761833 |
| Norm y.T A | 1.54e-15 |
| Norm y.T J | 1.45e-14 |
| Norm y_C3.T C | 2.25e-15 |

The exact conditional argument is short: if y annihilates A, J and C
exactly, then y.T F(p,w)=y.T b for every p,w. If y.T b is nonzero,
no p,w solves these equations for the frozen data. Equivalently,
y.T b=0 is a necessary compatibility condition for this finite problem.
No new force, damping parameter or physical coupling has been introduced.

The norm of y's C3 block is 0.99835; the other blocks participate too.
This locates the dominant numerical obstruction in the third constraint
within the current coordinate and residual normalization. Neither this
block norm nor the value 31.95 is a physical observable or an invariant
size independent of equation rescaling.

## Evidence Versus Proof

Three direct full-residual evaluations at distinct amplitudes agree with
the reconstructed polynomial within 3.0e-10 to 2.5e-9. Their y.T F stays
at 31.94761833, including arbitrary allowed w corrections. Focused tests
also compare C against a separate direct pairing loop and actual second
differences, then replay every projected coefficient and the saved y.

This is a numerical separating witness, not a certified global
nonexistence theorem. The analytic polynomial structure is established
by source inspection, but A and J are numerically assembled, and L and
y come from numerical SVDs. Tiny coefficient errors cannot simply be
declared zero for unbounded p,w. A rigorous bounded exclusion requires
certified error bounds, and an unbounded exact exclusion requires exact
annihilation identities. In particular, a failed optimizer alone would
not justify this conclusion.

Update: the [spatial-trace follow-up](HC_Cartan_Spatial_Trace_Obstruction.md)
finds a simpler exact dependency obstruction in 120 individual spatial
C3 equations, with a rationally evaluated nonzero component for the
saved data. This avoids having to certify this particular numerical y.

The original next proof task was to reconstruct or otherwise certify a separating
row using the original analytic coefficients. Separately, to construct
a continuation rather than exclude these data, derive and impose the
next-order compatibility on the tangential germ, while retaining the
earlier 384-row source law. Changing that germ is a new problem and must
be recorded explicitly. No compatible replacement data are constructed here.

The original unshifted solution and conditional source law remain intact.
No claim about all source values, all tangential data, regional PDE
existence, native frames, mass, Planck scales, or publication follows.

## Reproduction and Handoff

Run `python -B analysis/HC_Cartan_Complete_Quadratic_Gate.py --output
analysis/HC_Cartan_Complete_Quadratic_Gate.json` from the repository root.
The existing dependency-injection services cache the full coefficients
and central Jacobian under fingerprints of all inherited inputs.

Verification: 29 focused tests passed (8 complete-quadratic, 7 prior
normal-Hessian, 14 previous Cauchy-completion tests). Initial new-test
failures were test-harness issues: a closure was bound as an instance
method, and a real basis was incorrectly rank-tested over the complex
field. Both were corrected; the scientific evaluator was unchanged.
The full repository suite was not rerun for this isolated follow-up.
No additional agent was spawned after the prior usage-limit failure;
the complete calculation and independent-formula checks ran locally.
