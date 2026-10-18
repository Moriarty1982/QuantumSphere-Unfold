# Conditional Constitutive Transport in a Fixed Coordinate Frame

Date: 2026-10-18. Independent bounded derivation for the neutral Cartan
comparison. This is an exact coordinate identity and a conditional transport
statement along already given fields, not a full parent PDE existence theorem.

## 1. Definitions and Regularity

Work in one coordinate chart and one fixed spinor/readout trivialization.
Stack the three spinor channels into a column psi in C^12. Let A_a be the
constant Hermitian readout matrices used by the comparison (the matrices
`A = prolong.Q_WEIGHTS` in `HC_Cartan_Cauchy_Rank.py`). The label a takes
four values; its placement in A_a does not introduce an eta contraction.
Define, componentwise,

\[
 D_\mu\psi=\partial_\mu\psi+B_\mu\psi,\qquad
 C^a{}_\mu=\operatorname{Im}(\psi^\dagger A_aD_\mu\psi),\qquad
 F^a{}_\mu=C^a{}_\mu-E^a{}_\mu.                         \tag{1}
\]

Here B_mu acts on the stacked column; in the supplied implementation it is
the spin connection tensored with the identity on the three channels.
No anti-Hermiticity of B_mu with respect to A_a is assumed. For the following
classical identities, psi of class C^2 and B and E of class C^1 suffice.
If B has been eliminated algebraically in terms of other fields and their
jets, these assumptions concern the resulting B; its derivatives must
include that dependence by the chain rule.

For any such component one-form V, fix the unnormalized coordinate curl

\[
 (dV)^a{}_{\mu\nu}:=\partial_\mu V^a{}_\nu
                         -\partial_\nu V^a{}_\mu.       \tag{2}
\]

Thus there is no factor of two ambiguity from bracket notation. In
particular dE here is the ordinary exterior derivative in this fixed
trivialization, not Cartan torsion dE + omega wedge E.

## 2. Exact Product Rule and Cancellation

With a fixed a and constant A_a, direct differentiation gives

\[
 \partial_\mu C^a{}_\nu=\operatorname{Im}\left[
 (\partial_\mu\psi)^\dagger A_a(\partial_\nu\psi+B_\nu\psi)
 +\psi^\dagger A_a\left(
 \partial_\mu\partial_\nu\psi
 +(\partial_\mu B_\nu)\psi+B_\nu\partial_\mu\psi\right)
 \right].                                                   \tag{3}
\]

Antisymmetrizing and commuting the coordinate partial derivatives yields

\[
\begin{aligned}
 (dC)^a{}_{\mu\nu}=\operatorname{Im}\big[&
 (\partial_\mu\psi)^\dagger A_aD_\nu\psi
 -(\partial_\nu\psi)^\dagger A_aD_\mu\psi\\
 &+\psi^\dagger A_a\{(\partial_\mu B_\nu-\partial_\nu B_\mu)\psi
              +B_\nu\partial_\mu\psi-B_\mu\partial_\nu\psi\}\big].
                                                               \tag{4}
\end{aligned}
\]

The canceled term is exactly
Im[psi^dagger A_a (partial_mu partial_nu - partial_nu partial_mu)psi].
Hermiticity further gives the equivalent expanded form

\[
\begin{aligned}
 (dC)^a{}_{\mu\nu}
 ={}&2\operatorname{Im}[(\partial_\mu\psi)^\dagger A_a\partial_\nu\psi]\\
 &+\operatorname{Im}\big[
 (\partial_\mu\psi)^\dagger A_aB_\nu\psi
 -(\partial_\nu\psi)^\dagger A_aB_\mu\psi\\
 &\hspace{16mm}+\psi^\dagger A_a(B_\nu\partial_\mu\psi-B_\mu\partial_\nu\psi)
 +\psi^\dagger A_a(\partial_\mu B_\nu-\partial_\nu B_\mu)\psi\big].
                                                               \tag{5}
\end{aligned}
\]

Equations (4)-(5) agree with `explicit_curl` in
`HC_Cartan_Spatial_Propagation.py`: its first jet index differentiates the
connection component indexed by the second, and its pairs are
(0,1), (0,2), (0,3), (1,2), (1,3), (2,3).
The cancellation removes the explicit freely prescribed symmetric spinor
Hessian. It does not remove derivatives of an eliminated connection; those
can themselves contain higher derivatives of its underlying fields.

## 3. Curvature Rewriting and Its Frame Limitation

An algebraically useful rewriting, still in this same trivialization, is

\[
 K_{\mu\nu}=\partial_\mu B_\nu-\partial_\nu B_\mu+[B_\mu,B_\nu],
 \qquad H_{a\mu}=B_\mu^\dagger A_a+A_aB_\mu,
\]
\[
\begin{aligned}
 (dC)^a{}_{\mu\nu}=\operatorname{Im}\big[&
 (D_\mu\psi)^\dagger A_aD_\nu\psi
 -(D_\nu\psi)^\dagger A_aD_\mu\psi
 +\psi^\dagger A_aK_{\mu\nu}\psi\\
 &-\psi^\dagger H_{a\mu}D_\nu\psi
 +\psi^\dagger H_{a\nu}D_\mu\psi\big].                    \tag{6}
\end{aligned}
\]

This follows by substituting partial_mu psi = D_mu psi - B_mu psi into
(3). Dropping the H terms requires an additional compatibility condition;
Hermiticity of A_a alone does not supply it. Nor does the presence of K
make (6) a Lorentz-covariant exterior derivative of the a-indexed readout.

For precision, under psi' = S psi and
B'_mu = S B_mu S^{-1} - (partial_mu S) S^{-1}, a desired readout law
C'^a_mu = Lambda^a_b C^b_mu is ensured by

\[
 A'_a=(S^{-1})^\dagger\Lambda^a{}_b A_b S^{-1}.             \tag{7}
\]

Keeping the same constant matrices in both frames therefore requires the
specific intertwining identity S^dagger A_a S = Lambda^a_b A_b. This is
an extra property to establish for the chosen representation and readout.
If A_a varies, (4) acquires the additional terms

\[
 \operatorname{Im}[\psi^\dagger(\partial_\mu A_a)D_\nu\psi
                  -\psi^\dagger(\partial_\nu A_a)D_\mu\psi]. \tag{8}
\]

Also dC' = Lambda dC + dLambda wedge C for a varying Lambda. A frame
connection on the a index is required to turn this into a covariant curl.
No such covariant identity is asserted here. Equations (1)-(6) use the
fixed comparison frame, which is sufficient for the coordinate conclusion.

## 4. The Defect Is the Transport Source

Define the curl defect

\[
 J^a{}_{\mu\nu}:=(dC)^a{}_{\mu\nu}-(dE)^a{}_{\mu\nu}.
 \qquad dF=J.                                               \tag{9}
\]

Writing x^0 = t gives the exact identity, without any field equation,

\[
 \boxed{\quad
 \partial_t F^a{}_i=\partial_i F^a{}_0
 +(dC)^a{}_{0i}-(dE)^a{}_{0i}
 =\partial_i F^a{}_0+J^a{}_{0i}.\quad}                      \tag{10}
\]

Consequently imposing the temporal constitutive equations F^a_0 = 0 on
a region reduces (10) to partial_t F^a_i = J^a_0i. Their spatial
derivatives vanish because F^a_0 vanishes as a function there, not because
its value vanishes at one point. Homogeneous transport requires the mixed
defect to vanish, or an independently proved homogeneous closure in the
residuals; the product rule alone supplies neither closure nor a probe
evolution equation.

In particular, R(p) = 0 and mathfrak F_E(p) = 0, where mathfrak F_E is the
coframe Euler residual, do not set J(p) to zero. Even adding F(p) = 0 and
the exact algebraic Cartan equation does not set derivatives of F to zero.
The values of a function and of selected field equations at one point do
not imply their first differential consequences. The gravitational
propagation note assumes all F = 0 on a region and explicitly proves no
propagation of F; its conditional Ward argument cannot supply that missing
assumption without a separate constitutive argument.

## 5. What the Saved Normal Ranks Establish

The normal system is the 56-by-56 affine system implemented by
`normal_matrix` in `HC_Cartan_Cauchy_Rank.py` (called the normal system
here). Its 56 equations are 16 constitutive equations, 24 real probe
equations, and 16 coframe Euler equations, with the same Cartan connection
already eliminated. Its unknowns are E_,00 (16 real components), psi_,0
(24), and lambda_,0 (16); all other jets are frozen.

The saved reprepared regular point has reported normal rank 34 and a
consistent original affine system to floating-point precision. In
`normal_curl_system`, adding the twelve mixed curls gives a 68-by-56
matrix of reported rank 40. At the normal comparison point E = I,
partial E = 0, these curls of C equal the mixed defects J. In general
they must instead be compared with dE.

Let M be the original matrix, N the twelve added rows, and Z a matrix
whose columns span ker M. Then

\[
 \operatorname{rank}\begin{pmatrix}M\\N\end{pmatrix}
 =\operatorname{rank}M+\operatorname{rank}(NZ)=34+6=40.       \tag{11}
\]

Thus six linear combinations of the added conditions constrain directions
left free by the original equations: the mixed curls are not consequences
of those pointwise normal equations at this jet. The remaining six
left-null combinations of NZ impose affine compatibility on the frozen
data. If M x_* + b = 0 and the added equations are N x + c = 0, their
solvability requires L^T(N x_* + c) = 0 for every column of L in
ker((NZ)^T). For the HISTORICAL frozen preparation in
`HC_Cartan_Spatial_Propagation.json`, the saved projection norm is about
25.44 and the augmented least-squares residual norm about 2.837, so that
frozen preparation fails the augmented affine system. This failure is not
attributed to the later joint 1114-component completion, whose mixed curls
do vanish at the origin. These norms refer to different projections and
need not coincide.

These are recorded numerical ranks and residuals, not an exact symbolic
rank certification or an assertion about every jet. They do demonstrate
the gap in promoting that pointwise preparation to homogeneous propagation.
Symmetric spinor second derivatives cannot fix its antisymmetric defect:
their contributions to (3) cancel in (4). The script's full re-preparation
can change other jets to meet additional finite-order conditions, but a
finite-order completion is still not a regional evolution theorem.

## 6. Limited Conditional Theorem

Let sufficiently regular fields as in Section 1 be given on a coordinate
product region I times Omega, with t_0 in I. Assume throughout that region

\[
 F^a{}_0=0,\qquad J^a{}_{0i}=0.                              \tag{12}
\]

If F^a_i(t_0,x) = 0 for every x in Omega, then F^a_mu = 0 throughout the
region. Indeed, (10) gives partial_t F^a_i = 0 at each fixed spatial x,
so integration gives F^a_i(t,x) = F^a_i(t_0,x). No spatial boundary data
are required for this coordinate ordinary differential equation, provided
each vertical segment used lies within the region. More generally the
exact sourced formula is

\[
 F^a{}_i(t,x)=F^a{}_i(t_0,x)+\int_{t_0}^{t}
       [\partial_iF^a{}_0+J^a{}_{0i}](s,x)\,ds.              \tag{13}
\]

Requiring the full curl defect J = 0 on the region is a sufficient stronger
hypothesis for (12). Only its mixed components enter transport. The spatial
identity J^a_ij = partial_i F^a_j - partial_j F^a_i also shows that full
J = 0 forces spatial closedness; closedness alone is weaker than F_i = 0.
Although dJ = 0 follows identically from J = dF, it does not force the
mixed components J_0i to vanish from pointwise parent equations.

This theorem is conditional on the regional mixed curl equations and the
regional temporal constitutive equations. It does not derive them from
R = mathfrak F_E = 0, establish a homogeneous subsidiary system for J,
prove propagation of the probe residual, or construct any parent solution.
In particular it establishes no full PDE existence, hyperbolicity, gauge
closure, or native-field identification. It supplies the exact constitutive
transport identity and the additional regional hypothesis under which
initial spatial constitutive constraints propagate.
