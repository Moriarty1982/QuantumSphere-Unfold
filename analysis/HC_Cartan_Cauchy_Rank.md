# Temporal Constraint Rank and the Limits of Jet Propagation

Date: 2026-10-18. Status: structural Cauchy-rank audit of the same **added neutral odd-cross Cartan parent**, plus a newly prepared regular point. Not a proof of constraint propagation, Cauchy existence, stability, native gravity or a physical scale. Main TeX/PDF unchanged.

This follows [joint Cartan prolongation](HC_Cartan_Prolongation.md). Instead of accepting another successful finite jet as evidence of evolution, inspect the coefficient matrix that would have to determine time derivatives. Two results matter: the old lambda=0 point lies on a rank-degenerate temporal branch; and its frozen higher jet violates the next scalar consequence. A suitable nonzero multiplier can regularize the probe/temporal-constraint block while retaining positive probe weights. The full constrained gravitational evolution still needs reduction and propagation equations.

## 1. Positive Probe Weights Are Not Enough

Retain the previous E, Psi, independent Lorentz connection, real multiplier density lambda, fixed Q=i(E12-E21)/2, the prepared Hermitian M, c=1 and u=0. These are comparison assumptions, not an evaluated native HC/C7 action. The Cartan connection is eliminated from its own equation including the multiplier source.

At a normal point with E=I and first E jet zero, put `ell_a=lambda_a^0`, `a_b=partial_0 lambda_b^0`, and

\[
 A_a=Q\otimes K^a,\qquad
 \mathbb K^0=I_{12}+\ell_a A_a.
\]

For positive K0, the real probe equation determines its time derivative in the form

\[
 \dot\Psi=\dot\Psi_* -\tfrac12(\mathbb K^0)^{-1}A_b\Psi\,a_b.           \tag{1}
\]

All known spatial, mass, spin, density and connection-adjoint terms are included in the starred source. Substituting (1) into the four **temporal-column** constraints `C^a_0-E^a_0=0` gives

\[
 f_a+T_{ab}a_b=0,\qquad
 T_{ab}=-\tfrac12\operatorname{Im}
            \bigl(\Psi^\dagger A_a(\mathbb K^0)^{-1}A_b\Psi\bigr).       \tag{2}
\]

Because the A matrices and inverse temporal weight are Hermitian, T is real antisymmetric. This is a derived response matrix, not a new force or coupling. Positivity of K0 does **not** imply invertibility of T. The combined real 28-by-28 probe/temporal-constraint matrix has rank `24+rank(T)`.

## 2. The Previous Zero-Multiplier Branch Has Two Null Conditions

Write alpha_i=K^i and Sigma_k=-i alpha_i alpha_j for cyclic i,j,k. In the Q eigenbasis define the real spin-polarization vectors

\[
 s_\pm^k=\xi_\pm^\dagger\Sigma_k\xi_\pm,\qquad
 w=\Psi^\dagger(Q^2\otimes\boldsymbol\Sigma)\Psi=(s_++s_-)/4.
\]

At lambda=0, K0=I. Pauli multiplication gives the exact block

\[
 T=\frac12\begin{pmatrix}
 0&0&0&0\\
 0&0&-w_3&w_2\\
 0&w_3&0&-w_1\\
 0&-w_2&w_1&0
 \end{pmatrix}.                                                       \tag{3}
\]

For nonzero w it has rank two and null vectors `(1,0,0,0)` and `(0,w)`. Thus (2) requires

\[
 f_0=0,\qquad w\cdot f_{spatial}=0,                                   \tag{4}
\]

and does not determine all four a components. When the spatial coframe constraints already hold, the first of (4) is the preceding weighted-mass scalar compatibility condition. The other is a spin-aligned temporal compatibility condition. If w=0, T instead vanishes and the degeneration is stronger; rank two is not universal.

On the previous prepared state the two nonzero singular values are `1.28919938`; the combined probe block has rank 26, even though **every temporal probe eigenvalue is exactly one**. The positive temporal estimates in the earlier notes remain correct but never supplied an invertible full evolution system.

This is a rank degeneration of a coefficient map in the selected field model and time chart. It is not a spacetime curvature singularity, measured instability or universal exclusion of a native theory.

## 3. Exact Regularity Criterion With a Nonzero Multiplier

Still at E=I, the temporal probe form is positive precisely when

\[
 |\ell_0|+|\boldsymbol\ell|<2.                                         \tag{5}
\]

Use Q's eigenvalues `(-1/2,0,+1/2)` and the inverse identity
`(a I+b.alpha)^(-1)=(a I-b.alpha)/(a^2-|b|^2)`. The q=0 channel does not contribute to T. Define

\[
 D_\pm=(1\pm\ell_0/2)^2-|\boldsymbol\ell|^2/4.
\]

Direct spectral/Pauli reduction of (2) gives

\[
 \operatorname{pf}(T)=
 \frac{\boldsymbol\ell\cdot(s_+\times s_-)}{64D_+D_-},\qquad
 \det T=\operatorname{pf}(T)^2.                                      \tag{6}
\]

One way to obtain (6) is to split the antisymmetric matrix into temporal and spatial three-vectors. Terms parallel to ell drop from their scalar product; the remaining opposite-channel cross terms yield the displayed triple product. The implementation checks the full identity against matrix inversion for generic positive temporal columns.

Within (5), T is invertible exactly when the triple product in (6) is nonzero. A nonzero ell0 alone is insufficient. Parallel channel spin polarizations or a spatial ell orthogonal to their cross product remain singular. Scalar phase changes of the two spectral spinors do not change this instantaneous criterion. This is not a gauge-symmetry claim about M, which does not commute with Q, and these channel polarizations are not identified with physical matter/tachyon frames.

For the unchanged spinor value, set ell=`epsilon*(.1,.2,-.3,.4)`. At epsilon=.1:

- ell=`(.01,.02,-.03,.04)`.
- Smallest temporal probe eigenvalue: `.96807418`.
- Singular values of T: `(1.2835991,1.2835991,.0339230,.0339230)`.
- Pfaffian: `-.0435435843`; the combined probe block has full rank 28.

As epsilon tends to zero, the two small T singular values vanish linearly while the probe form tends to I. The inverse T norm grows from about `29.48` at epsilon=.1 to `29651` at epsilon=.0001. Thus probe positivity cannot provide a uniform inverse bound near the old branch.

## 4. The Full Normal System Is Still Constrained

Fix spatial derivatives and initial first E jet. The original point equations after the same Cartan elimination are affine in these highest normal derivatives:

- 16 components of E_,00.
- 24 real components of Psi_,0.
- 16 components of lambda_,0.

The 56 equations consist of 16 coframe constraints, 24 real probe equations and 16 independent coframe Euler components. The evaluated 56-by-56 matrix has rank 32 on the previous lambda=0 point and rank 34 at the regular temporal control.

The twelve spatial-column constitutive rows have no such highest normal derivatives. The coframe-acceleration block has rank six, with ten null directions in that block. At the regular point the whole normal kernel has dimension 22 and projects with rank twelve onto the velocities of the **spatial multiplier columns**. Thus even an invertible 28-by-28 probe block does not finish the Cauchy reduction. Spatial-constraint propagation, the remaining multiplier equations and gauge treatment are essential. Kernel directions are not declared physical modes or instabilities.

Simply changing lambda while freezing the earlier spatial data is not a solution: the best full normal residual of that off-shell control is about `1.79983`. The rank calculation alone must not be promoted to compatible initial data.

## 5. Reprepare a Regular Point, Without Claiming a Surface

To distinguish a coefficient example from a point satisfying the equations, retain the same spinor **value**, M, Q, c and u, but allow its four first derivatives, the symmetric second E jet and first lambda jet to change. Set E=I, first E jet zero and lambda's value to the regular ell above, with its other coordinate columns zero.

All four original point equations are then affine in 320 real coordinates. The 56-by-320 matrix has evaluated rank 50. Its unprojected residual norm is `1.87e-13`; the Cartan equation is retained through its own eliminated source, not imposed as torsion-free. The regular probe/temporal block uniquely recovers the point's probe time derivative and four a components. The full normal system still has rank 34, now with a compatible right-hand side.

All 320 coordinates are saved separately. This control establishes **a regular compatible point in the same assumed model**, not first differentiated coframe constraints, curvature matching on this new branch, Cauchy data on a surface or a local solution. It does not inherit the old singular-branch jet's higher-order achievements. The original metric/readout dictionary and physical normalization remain additional comparison assumptions.

## 6. A Concrete Failure of Automatic Frozen-Jet Extension

The preceding exact scalar consequence was

\[
 \mathcal A=v(4+b_Q)+\lambda:C[Q^2]=0.
\]

At the earlier normal point, its second derivative is

\[
 \mathcal A_{,rs}=b_{Q,rs}+\lambda_{,rs}:C[Q^2]
                 +\lambda_{,r}:C[Q^2]_{,s}
                 +\lambda_{,s}:C[Q^2]_{,r}.                           \tag{7}
\]

The volume terms vanish there because first E derivatives vanish and `4+b_Q=0`; lambda itself is zero. Equation (7) depends on E/Psi second jets and lambda's first/second jets, **not** on third E/Psi jets or new higher derivatives.

For the saved prolongation data, (7) has component norm `204.1562` and time-time component `-68.7331`. An independent difference of the actual scalar density on those Taylor fields agrees with the analytic Hessian to about `1.98e-5`. Meanwhile their earlier 404-equation residual remains below `1e-8`: both facts hold simultaneously.

Therefore that **entire frozen numerical jet** cannot also meet the next differentiated scalar consequence, without re-solving its free lower data. If the point coframe constraint and probe equation hold through the required orders, (7) must vanish; arbitrarily adding fourth jets cannot fix it. This is a robust numerical diagnostic of failure to extend these particular data, not an interval-certified exclusion of all nearby jets. The condition is a differential consequence of the existing full equations, not a new physical law or an additional independent axiom.

The result answers the propagation question at the level actually tested: the successful finite truncation did not automatically supply its next necessary condition. It does **not** prove that the full correctly reduced evolution violates its constraints; that evolution has not yet been constructed.

## Outcome and Next Gate

The old positive lambda=0 branch is temporally rank-degenerate, and the frozen saved jet fails a next scalar gate. A suitable nonzero multiplier and noncollinear spectral spin polarizations provide a regular probe block with positive weights, and re-prepared data satisfy all point equations there. This gives a concrete reason to study a constant-rank branch before relying on further zero-multiplier jet fits.

Next construct the spatial constitutive/gravitational constraints and their propagation on that branch, and reduce the remaining multiplier/gauge system. A singular-branch crossing would instead require its own compatibility analysis. Neither route is yet a full Cauchy or native-gravity proof. No coupling scale, physical frame identification, quantum ground state or new main-paper result is asserted.

The following [spatial-integrability audit](HC_Cartan_Spatial_Propagation.md) derives a 24-component curl criterion that cannot be repaired by higher spinor derivatives alone. The saved regular point fails it. Re-solving first spinor/geometric/multiplier data on the same regular temporal block completes all point equations and first constraint/probe derivatives. Six additional normal restrictions and six lower-data compatibility projections appear, but a sixteen-dimensional normal kernel remains; this is not full gravitational propagation or a Cauchy solution.

## Reproduction

- [Calculation](HC_Cartan_Cauchy_Rank.py), [saved rank audit and regular point](HC_Cartan_Cauchy_Rank.json), [38 focused tests](../scripts/qsc_audit/tests/test_hc_cartan_cauchy_rank.py).
- `python -B analysis/HC_Cartan_Cauchy_Rank.py --output analysis/HC_Cartan_Cauchy_Rank.json`
- `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_cartan_cauchy_rank.py`

Tests include the exact Pfaffian and exceptional polarizations, both singular compatibility projections, positive-weight rank changes, original normal-equation coefficients, regular-point preparation/reproduction, independent scalar differences and the preservation of the earlier finite-order checks. No package installation, TeX/PDF rebuild, release modification or Git operation is introduced.
