# Independent design review: simultaneous first/second-jet feasibility

30 October 2026. Separate review of the existing raw model and packing. No optimization run was executed by this reviewer. Reviewed OP5_Joint_Compatibility_Second_Jet_Check.py, OP5_Temporal_Compatibility_Identity_Result.md, OP5_Joint_Compatibility_Lower_Data.json and OP5_Counterflow_Full_Residual_Check.py. This is an implementation-design review, not an independent mathematical proof or a regional-existence certificate.

## Contract

Fixed: coordinate point, twelve complex spinor values, original background G/h/spin and their coordinate dependence, chosen time-coframe value. Variables: 96 real first derivatives and 240 real symmetric second derivatives. Retain the original regular chart det E != 0 and spacelike time slices; do not adjust model couplings to hide residuals.

It is meaningful to solve F=0 (24 real equations), all four total derivatives d_mu F=0 (96 real equations), and the four value-only time-coframe fixing equations jointly. This is finite second-jet feasibility. It does not establish evolution, constraint propagation at every order, or existence of a field on a neighborhood. The original frozen-first-jet failure should remain a control.

## Packing and chain rule

First-jet packing in the existing code is all 48 real entries in (mu,spinor) order followed by all 48 imaginary entries. Symmetric second-jet columns use pairs (i,j), i<=j, then 24 real/imaginary spinor components. For i!=j, one shared Hessian variable contributes J_j to derivative equation i and J_i to derivative equation j. There is no factor of two. Diagonal variables contribute once.

The total derivative is F_pos_mu + F_psi partial_mu psi + sum_nu F_J_nu partial_mu partial_nu psi. F_pos must include derivatives of the original G, h and azimuthal spin background while holding psi and jets fixed. The inverse coframe must differentiate through its dependence on the same jets. A linear Taylor model of the background at the evaluation point suffices for this first prolongation, but its first derivatives must be exact/verified there.

Fixing E0 at one point does not mean fixing its spatial derivatives to zero. Adding d_mu E0=0 would silently narrow the problem. Conversely, if E0 is intended as a prescribed regional function, its derivative data must be explicitly declared; a pointwise fixing is not automatically a global gauge symmetry.

## Cheapest independent acceptance checks

1. Recompute F and E using the original NumPy evaluator, independently of the optimizer.
2. Build a common second-order Taylor field. At pos +/- h e_mu, use psi +/- h J_mu + h^2 H_mumu/2 and jets_nu +/- h H_munu. Central differences of the original F must agree with the optimized prolonged residual at h=1e-4,1e-5,1e-6. Exact mixed symmetry is imposed by construction.
3. Report F norm, prolonged norm, E0 error, det E, g^{00}, Hessian norm and changes to first jets separately. A small weighted total loss does not imply all blocks are small. Report scale choices.
4. Independently check the scalar identity g=4-h psi^dagger Z beta psi/2 and dg=0. At exact F=dF=0 these should be consequences; finite residual disagreement diagnoses chain-rule or packing error.
5. Re-evaluate the linear symmetric completion matrix at fitted first jets and eliminate all symmetric second jets with an explicit singular-value cutoff. This tests that the compatibility source was actually reduced, rather than traded against solver truncation.

An underdetermined optimizer can move far or inflate Hessians. Penalizing movement is acceptable for step selection, but final feasibility must be assessed without the penalty. If using elimination/variable projection, the matrix depends on first jets; a frozen left projector or frozen pseudoinverse is not the full residual. Rank changes near the numerical cutoff need separate inspection.

## Verdict

Design is conditionally sound under the stated pointwise fixing, packing and chain rule. The smallest remaining implementation obligation is independent full-evaluator validation of the prolonged residual at the fitted jets. A numerical success would be new finite-jet evidence only; a failed fit would not prove incompatibility of the whole model.

## Review of actual joint_fit.py and saved results

Subsequently inspected the actual implementation and joint-fit-result.json without rerunning the optimizer. First jets are correctly unpacked as 48 real then 48 imaginary entries. The symmetric Hessian picker constructs H[mu,nu,component]. Its permute(1,2,0) packing gives rows (nu,component) and derivative columns mu, matching the Jacobian chain rule. The first 24 tangent rows give the spinor derivative, the next 96 give first-jet derivatives and the final four are coordinate identity. The background Taylor term uses its exact symbolic coordinate Jacobian; therefore its derivative at the central point is the original background derivative. The nonlinear inverse coframe is differentiated automatically. Time-coframe fixing is value-only.

The NumPy/Taylor control re-evaluates the exact background at displaced coordinates and a common quadratic Taylor spinor with its corresponding affine first derivatives. Its central derivative is thus a valid independent check of the first prolongation, although NumPy and Torch share the algebraic model convention. No packing or chain-rule bug was found on inspection. Residual reduction approximately quadratic with central step from 1e-4 to 1e-5 supports consistency; the smaller step approaches floating cancellation.

An additional reviewer calculation used only saved psi/first jets and the original symbolic h and its derivatives, with Zbeta=diag(1,-1,0) tensor beta. It independently evaluated q=psi†Zbeta psi, g=4-hq/2, dq_mu=2 Re(psi†Zbeta J_mu), and dg_mu=-(dh_mu)q/2-h dq_mu/2. Results at points 0/1/2:

| quantity | point 0 | point 1 | point 2 |
|---|---:|---:|---:|
| g | 1.33e-15 | -8.88e-16 | 4.44e-16 |
| norm dg | 3.29e-14 | 2.62e-15 | 3.47e-15 |

This corroborates the scalar constraint and its first derivatives, without rerunning optimization. It is floating numerical evidence, not an exact certificate. First-jet changes are 0.00166, 0.0437, 0.0170 in the declared packed Euclidean norm; Hessian norms are approximately 7.08, 6.90, 7.18. No explosion is visible in these norms, but no physical norm interpretation is supplied.

Updated verdict: actual implementation passes this bounded design/packing self-contained review with no blocking issue found. The saved results support numerical feasibility of F=0 and its first prolongation with symmetric second jets at three independent points, after changing first jets jointly. They supersede only the previous frozen-first-jet obstruction at this order. They do not establish third-jet compatibility, regional existence, a shared solution through all three points, native QSC/GR identification, or OP5 closure.
