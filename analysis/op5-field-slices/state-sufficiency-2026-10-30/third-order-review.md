# Third-order design and independent scalar gate

30 October 2026. Independent bounded review; no third-jet optimizer or full completion SVD run by reviewer.

## Chain rule

Let q=(packed psi24, packed first jets96, coordinates4), with F(q) real24. Along coordinate mu the tangent is v_mu=(pack J_mu, pack H_mu, e_mu). Then

dd_mu_nu F = HessF[v_mu,v_nu] + DF_psi pack H_munu + DF_jets pack T_munu_dot.

Thus the proposed source is HessF[v_mu,v_nu]+DF_psi pack H_munu; third jets enter linearly. The Hessian must include the original background's second coordinate derivatives. Coordinate accelerations vanish. Ten symmetric derivative-pair blocks have 24 rows each (240 total); twenty symmetric triple blocks have 24 real variables each (480 total). For each equation pair (mu,nu), the third-jet variable with unordered multiset (mu,nu,lambda) contributes through the first-jet Jacobian block lambda. There is no multiplicity factor when using actual derivative values rather than polynomial coefficients.

Independent control: evaluate original F on a common cubic Taylor spinor, its quadratic first derivatives, and exact position-dependent background. Pure second differences use F(+h)-2F(0)+F(-h), divided by h²; mixed differences use four corners divided by 4h². Compare against AD source/operator at multiple h. To test just the source, use zero third jets and quadratic spinor/affine first derivatives.

## Necessary scalar gate: evaluated independently

The original identity is ell(psi)F = g = 4-h q_scalar/2, q_scalar=psi† Zbeta psi, Zbeta=diag(1,-1,0) tensor beta. Since the current F and dF are numerical zero, ddF=0 would imply ddg=0 up to the corresponding small lower-residual terms. At fixed psi, first jets and Hessian, ddg is independent of all third derivatives:

dq_mu=2 Re(psi†Zbeta J_mu)

ddq_munu=2 Re(J_mu†Zbeta J_nu + psi†Zbeta H_munu)

ddg_munu=-[(ddh_munu)q_scalar+(dh_mu)dq_nu+(dh_nu)dq_mu+h ddq_munu]/2.

Using original symbolic h, its gradient and Hessian, and the saved joint-fit first/second jets, the reviewer obtained symmetric-packed norms ||ddg|| = 40.8986925051, 41.8305982008, 40.4456152746 at points 0,1,2. Raw matrices are in third-order-scalar-gate.json. These are far above lower-order roundoff residuals. This is independent contraction code, not the parent's DD-F Hessian implementation.

Therefore frozen fitted second jets already fail a necessary third-order completion gate. Free third derivatives alone cannot repair this scalar defect. This does not retract the earlier finite second-jet feasibility: it is precisely a new constraint on those second jets arising one derivative order later. Next meaningful joint fit must allow second jets to change while retaining all lower equations and adding ddg or the full second prolongation. No universal nonexistence, physical interpretation or OP5 closure follows.

## Actual implementation and quantitative attribution

Reviewed third_check.py: second background Taylor term has the correct 1/2 coefficient; mixed entries are symmetrically filled. HessF contraction and the DF_psi H term implement the chain rule above. Third-jet columns use sorted triples and contribute the lambda first-jet block once to each derivative-pair row, matching actual derivative values. The independent cubic Taylor control has the correct 1/6 field and 1/2 first-derivative coefficients. No blocking indexing issue was found.

The reviewer persisted and executed third_gate_review.py, which does not import the parent's AD Hessian or rerun optimization. Raw output is third-gate-review-result.json. For ell=(-Im((S tensor I)psi), Re((S tensor I)psi)), each derivative-pair scalar row annihilates every third-jet contribution because ell DF_jets=0. Up to lower residual terms, K b=packed ddg for K=I_10 tensor ell. Since the ten block rows are orthogonal with common norm ||ell||, every completion has lower bound ||ddg||/||ell||.

| point | scalar lower bound | unrestricted residual in parent result | bound² / symmetric residual² |
|---|---:|---:|---:|
| 0 | 28.9353281932008 | 28.9353281932008 | 0.9701863 |
| 1 | 29.6301538102438 | 29.6301538102438 | 0.9711852 |
| 2 | 28.6022482924994 | 28.6022482924994 | 0.9696190 |

The norm equality holds within 4.7e-14 in the saved floating results. Independent NumPy central differences give ||ell DF_jets|| between 3.0e-10 and 3.5e-10. Contracting the source obtained from a quadratic Taylor field gives ||ell b-ddg|| about 2.2e-5 at step 3e-4 and 2.4e-6 at step 1e-4, consistent with second-order differencing error.

Interpretation: the scalar Hessian gate accounts numerically for the entire unrestricted-third-jet residual. It supplies approximately 97% of the squared fully symmetric residual in this particular unweighted Euclidean packing. The extra symmetric remainder is nonzero and is not explained by this one gate. These percentages are numerical norm attribution, not physical fractions or universal constants.
