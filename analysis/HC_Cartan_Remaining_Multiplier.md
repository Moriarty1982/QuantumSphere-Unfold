# Six Remaining Normal Multiplier Directions

Date: 2026-10-18. Scope: **the explicitly added neutral odd-cross Einstein-Cartan comparison model only**, at the existing regular point E=I, dE=0. This is a normal-kernel quotient and response calculation, not six new physical modes, six extra gauge symmetries, native HC physics, constraint closure or a Cauchy solution. No main TeX/PDF, release, index or shared input is changed.

Inputs are the existing [regular gravitational completion](HC_Cartan_Regular_Gravity.md) and [spatial propagation calculation](HC_Cartan_Spatial_Propagation.md). Their saved point and higher jets are retained without refitting. M, Q, c=1, u=0 and the multiplier value, including its temporal column (.01,.02,-.03,.04), remain unchanged. The JSON records both input fingerprints and every entry of the new 56-by-6 basis. Normal variations of E2 and d lambda below are explicit diagnostics around that point, not silent changes of its prepared data.

## 1. A Reproducible Quotient

Let N be the prior 68-by-56 normal matrix, with unknowns ordered as

\[
 x=(\delta E_{,00},\ \delta\Psi_{,0},\ \delta\lambda_{,0}).
\]

It includes all 56 original point equations and twelve mixed temporal/spatial coframe-constraint curls. Its numerical rank is 40, and its kernel dimension is 16. The ten previously exhibited leading coordinate/Lorentz directions form G. The quotient considered here is precisely ker(N)/im(G), not a quotient by all possible or conjectured symmetries.

The regular 28-by-28 temporal probe/constraint block fixes

\[
 \delta\Psi_{,0}=0,\qquad \delta\lambda_a{}^0{}_{,0}=0.
\]

Choose the Euclidean complement to G by setting the temporal row and column of h=delta E_,00 to zero and taking its spatial 3-by-3 block symmetric. This is a convention in the declared normal frame, not a Lorentz-invariant norm or a complete gauge-fixing theorem. It leaves a spatial multiplier velocity B_a^i=delta lambda_a^i_,0 and symmetric h_ij to determine.

Define the Q-weighted axial vector, its lowered vector and spatial part by

\[
 a=A_Q=\bar\Psi Q\Gamma^a\Gamma_5\Psi=(a^0,s),\quad
 u=\eta a,\quad n=|s|,\quad \hat s=s/n,\quad
 P_u=I-\frac{u u^T}{u^Tu}.
\]

For this point a is approximately (9.64432558,5.98188857,2.67049551,7.35332315), with a^T eta a=3.97288269 and n=9.84814188. In particular a^0 and n are nonzero. The parametrization does not cover branches where either vanishes.

Here is a closed six-coordinate parametrization, with w,v in R^3 and [v]_cross z=v cross z:

\[
 \begin{split}
 \delta\Psi_{,0}&=0,\qquad B_a{}^0=0,\\
 h_{ij}(v)&=\hat s_i v_j+v_i\hat s_j,\\
 B(w,v)_{a}{}^i
   &=\frac{u_a}{|u|}w_i+
      \left[P_u\begin{pmatrix}0_{1\times3}\\(4/n)[v]_{\times}\end{pmatrix}\right]_{ai}.
 \end{split}                                                     \tag{1}
\]

The first three basis vectors use w=e_i,v=0; the last three use w=0,v=e_i. Projecting with P_u removes the already exhibited axial-column nulls from the second family and makes this representative unique. It is not an equation imposed on the physical model.

At the existing point, the 21-by-12 spatial-connection/orthogonality compensation map has full column rank 12. Direct substitution of (1) gives compensation residual 2.97e-16, ||N basis||=8.61e-15 and exact G^T basis=0. The six-column spatial multiplier projection has rank six. Together G and this basis have rank 16; their span misses the independently computed full normal kernel by only 1.29e-13. These rank statements are numerical, with all singular values saved, not interval-certified global rank statements.

## 2. Axial Source Nulls Versus Coframe Compensation

At E=I the Clifford response in the existing conventions is

\[
 L_{(a,\mu),(\nu,bc)}
   =\tfrac12\delta_{\mu\nu}\epsilon^{abcd}u_d,
 \qquad \epsilon^{0123}=+1,\qquad b<c.                            \tag{2}
\]

Consequently L^T(u tensor w)=0 column by column, by antisymmetry. This explains the first three directions: their normal source, contorsion derivative and coframe acceleration variations vanish. It is an actual algebraic kernel of the **Cartan spin-source response**, not of the full parent action.

For the v family, first omit P_u in (1). Projection changes the source by zero because of (2). Substituting the unprojected B into H delta k=L^T B gives

\[
 \begin{array}{ll}
 \delta k_{i,0j}=h_{ij}, & \delta k_{i,jk}=0,\\
 \delta k_{0,0j}=-2a^0v_j/n,&
 \delta k_{0,ij}=(s_i v_j-v_i s_j)/n,
 \end{array}                                                       \tag{3}
\]

with lowered Lorentz indices antisymmetric. For h in (1), the normal LC contribution obeys

\[
 \delta\omega^{LC}_{i,0j,0}=-h_{ij},\qquad
 \delta\omega^{LC}_{0,ab,0}=0.                                   \tag{4}
\]

Thus the spatial columns of delta omega_,0 cancel between (3) and (4). The temporal column generally does not vanish.

Equations (2)-(4) are more than a fit of an SVD basis. The implementation checks (2) entrywise against the gamma-matrix response and on independent spinors. For (3), after multiplying by n, both sides are bilinear in the four components of a and three components of v. All twelve basis coefficients of H delta k-L^T B are checked: every coefficient is exactly zero with this normal integer H and half-integer Clifford coefficients. Normal-frame dyadic arithmetic is exact for these coefficient comparisons. The code separately checks the connection formula against the original Cartan elimination.

The distinction is measurable. L^T B has rank three on the v family; it does not vanish. If h is suppressed, N applied to these three B directions has rank three and norm 7.77772, so they are no longer normal nulls. More generally, keeping all E2 fixed gives a 68-by-12 spatial multiplier block of rank nine, leaving only the three axial source nulls. The extra three are genuinely **compensated coframe/contorsion directions**, not an algebraically absent multiplier coupling.

## 3. Why Independent Cartan Curvature Is Unchanged

After the temporal block has fixed delta Psi_,0 and delta lambda^0_,0, only omega_,0 changes, because all lower values and spatial jets are fixed. Let W_i,ab=delta omega_i,ab_,0. Then only delta R_0i can be nonzero. The point gravitational equations and mixed curls constrain W through a 28-by-18 real map.

Its gravitational part has rank 12; its curl part has rank nine; their stack has full rank 18 at this point. Structurally, split W into its boost matrix P_ij=W_i,0j and rotation matrix V_ik=epsilon_kjl W_i,jl/2. The independent coframe Euler equation forces P=0 and V symmetric. Once P=0, the spatial rows of the Clifford curl response contain the nonzero factor a^0 multiplying each row of V. Hence the curls force V=0. This explains why the remaining normal kernel has W=0 rather than undetected spatial Cartan curvature.

For the canonical v representatives, (3)-(4) leave only

\[
 \delta\omega_{0,ab,0}\ne0,\qquad
 \delta\omega_{i,ab,0}=0\ (i=1,2,3),\qquad
 \delta\omega_{\mu,ab,r}=0\ (r\ne0).                            \tag{5}
\]

Curvature antisymmetrizes its coordinate derivative indices, so the remaining 00 derivative drops out. The connection value itself is unchanged. **All six directions leave the entire independent Cartan curvature tensor at the point unchanged**, not just its Ricci projection. The computed full tensor response norm is below 1e-14.

That does not mean all geometry is unchanged. For the compensated three, the independent E metric's LC curvature response has rank three, and the first torsion derivative response has rank three. The LC curvature change is canceled by the contorsion reaction in the independent Cartan curvature. The connection first-jet response also has rank three, with only the 00 coordinate slot surviving. Neither rank is a physical mode count.

## 4. Relation to the Schur Nullspace

For the same prepared spinor, rank(L)=12 and rank(S)=9 for S=L H^-1 L^T, as in the earlier spacelike axial calculation. On the present six-dimensional multiplier image,

\[
 \operatorname{rank}(L^TB)=3,\qquad \operatorname{rank}(SB)=2.
\]

The v parallel to s direction gives SB=0 while L^T B is nonzero and h is nonzero. Thus the six split, with respect to these two maps, into:

- Three axial source-null directions, already in ker(L^T).
- One further Schur-null direction that still changes contorsion and requires h.
- Two further directions with nonzero Schur response, compensated by h.

In particular it would be incorrect to identify the whole six-dimensional quotient with ker(S), or to identify a Schur null with zero connection response. Their relationship follows from the full source and compensation formulas, not from the count seven of the earlier full 16-component Schur kernel.

## 5. Higher Equations Detect the Directions

For this diagnostic, hold the saved Psi2, lambda2, E3 and Psi3 of the regular gravitational completion fixed. The baseline full 384-component residual is 5.69e-11. Vary the six lower normal directions of (1) without projecting any equation or re-solving a higher coefficient. The resulting response ranks are:

| Quantity | Axial source-null three | Compensated three | All six |
|---|---:|---:|---:|
| Original 56 point equations | 0 | 0 | 0 |
| Independent connection value | 0 | 0 | 0 |
| Independent connection first derivative | 0 | 3 | 3 |
| Independent Cartan curvature at the point | 0 | 0 | 0 |
| Independent E metric LC curvature | 0 | 3 | 3 |
| First torsion derivative | 0 | 3 | 3 |
| First coframe constraints, frozen Psi2 | 0 | 2 | 2 |
| First probe equations, frozen higher jets | 3 | 3 | 6 |
| First coframe Euler equations, frozen higher jets | 3 | 3 | 6 |
| Second coframe constraints, frozen higher jets | 3 | 3 | 6 |
| First kinetic-density derivative | 3 | 3 | 6 |

All first-constraint changes are in F^a_0,0. They do not contradict the unchanged mixed curls. Because the spinor-to-coframe principal map is surjective, they can be canceled by changing only the symmetric Psi_,00 entry; this narrow repair is tested, but does not repair the other higher equations automatically.

The first-probe response has singular values approximately (6.20101,4.28694,3.74535,1.48303,1.14671,.540375): it detects all six coordinates on the fixed higher completion. The full frozen 384-component response has rank six and norm 141.95293. Its norm is retained as a failed frozen-completion control, not projected away. Affinity checks have norm 6.63e-12. These are **not** six new independent consistency obstructions: higher jets can compensate some of these changes, and their simultaneous continuation is a separate task.

Even the axial source-null family is not an algebraic parent redundancy. In a separate deliberately off-shell independent-connection control, shift lambda's **value** by its axial null while holding omega,d omega fixed. The Cartan source is unchanged, but the independent coframe Euler expression changes by that multiplier shift itself, with rank three. Normal velocity source-nullness must not be promoted to invariance of the action.

Independent central differences of the actual Taylor fields, at step 2e-5, check the connection, torsion, constraint and probe first-derivative responses with maximum errors about 5.80e-8, 6.59e-8, 1.63e-7 and 2.51e-7 respectively. These are truncation/roundoff checks, not certified bounds. The unchanged K0 and T remain the existing positive and invertible point blocks; no neighborhood or full-PDE-rank estimate is claimed here.

## 6. Outcome and Limits

The six remaining normal directions have a concrete reproducible explanation: **three axial spin-source nulls plus three coframe/contorsion compensations**. Pointwise independent Cartan curvature is blind to all six, whereas higher probe and gravitational equations on the frozen completion are not. The three compensated directions also change the LC metric curvature, so absence from the Cartan curvature cannot be described as absence from all geometry.

This identifies the quotient after the ten exhibited leading gauge directions. It neither proves nor excludes an additional coupled gauge structure with appropriate higher variations. A Noether identity or action symmetry would be needed before claiming another gauge freedom. Likewise, re-solving a finite hierarchy would not itself prove surface-data propagation, constant rank, convergence or Cauchy existence. Nothing here identifies this added comparison with the native paper, introduces a physical scale, or proves six particles or instabilities.

## Reproduction

- [Calculation](HC_Cartan_Remaining_Multiplier.py), [saved basis and audit](HC_Cartan_Remaining_Multiplier.json), [38 focused tests](../scripts/qsc_audit/tests/test_hc_cartan_remaining_multiplier.py).
- `python -B analysis/HC_Cartan_Remaining_Multiplier.py --output analysis/HC_Cartan_Remaining_Multiplier.json`
- `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_cartan_remaining_multiplier.py`

Only these four task-owned files are created. Shared basis files, the parallel regular-neighborhood task, main TeX/PDF, release files, repository indices and Git history are not edited.

Verification: 38 new focused tests, 42 existing regular-gravity tests and 38 existing spatial-propagation tests pass, 118 tests in these three targeted runs. The full repository suite was not rerun in this independent subtask.
