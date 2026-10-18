# Conditional Gravitational Constraint Propagation

Date: 2026-10-18. Independent analytic derivation for the explicitly added
neutral Cartan comparison. This note assumes the Ward identity specified
below; its derivation from the parent action is separate work. No numerical
jet is promoted to an open-set solution.

## 1. Hypotheses and Exact Density Convention

On an open spacetime region assume an invertible real coframe, the exact
sourced Cartan equation (with its algebraic elimination performed exactly),
the complete real probe equation R=0, and ALL constitutive equations
F=C-E=0. These are open-set hypotheses, not just pointwise jet conditions.
Assume the Lorentz and coordinate identities then give

\[
 S^{\mu\nu}=\mathfrak F_{E,a}{}^\mu\eta^{ab}
                     (E^{-1})^\nu{}_b=S^{\nu\mu},\qquad
 \partial_\mu S^{\mu\nu}
       +\Gamma^{\nu}_{\mathrm{LC}\,\mu\rho}S^{\mu\rho}=0.       \tag{1}
\]

Here eta=diag(-1,1,1,1), g=E^T eta E, and the coframe residual is the
Euler density with the sign in HC_Cross_Cartan_Parent.md, equation (2).
In particular no Einstein-equation normalization or extra minus sign is
silently inserted. Set

\[
 v=|\det E|=\sqrt{-\det g}>0,\qquad T^{\mu\nu}=S^{\mu\nu}/v.
                                                               \tag{2}
\]

Thus S is a contravariant weight-one tensor density and T is a tensor.
Since partial_mu v=v Gamma^rho_{LC rho mu}, (1) is exactly
nabla^LC_mu T^{mu nu}=0. The two contracted connection terms in the
covariant derivative of the density cancel; adding another volume-connection
term to (1) would be incorrect. All derivatives below use LC, not the
eliminated connection with torsion. Invertibility of E makes S=0 equivalent
to the complete coframe Euler equation. A fixed nonzero rescaling of the
Euler residual rescales every constraint below and changes no propagation
conclusion.

## 2. Slicing, Projections, and the Six Evolution Equations

Use a chart whose time covector is timelike, g^{00}<0. Its level surfaces
are spacelike. Write

\[
 g=-N^2dt^2+h_{ij}(dx^i+\beta^i dt)(dx^j+\beta^j dt),\quad
 N=(-g^{00})^{-1/2}>0,\quad \beta^i=-g^{0i}/g^{00},
\]
\[
 n_\mu=(-N,0,0,0),\quad n^\mu=N^{-1}(1,-\beta^i),\quad
 h^\mu{}_\nu=\delta^\mu{}_\nu+n^\mu n_\nu,\quad v=N\sqrt h.
                                                               \tag{3}
\]

Here h=det(h_ij); D is its spatial connection. A timelike time *covector*
is the requirement; the coordinate vector partial_t need not be timelike.
Define, with spatial vectors understood as tangent to a slice,

\[
 H=T^{\mu\nu}n_\mu n_\nu,\quad
 M^\mu=-h^\mu{}_\alpha T^{\alpha\nu}n_\nu,\quad
 P^{\mu\nu}=h^\mu{}_\alpha h^\nu{}_\beta T^{\alpha\beta}.
\]
\[
 T^{\mu\nu}=Hn^\mu n^\nu+n^\mu M^\nu+M^\mu n^\nu+P^{\mu\nu},
 \quad M^0=P^{0\mu}=0,\quad M_i=h_{ij}M^j.                    \tag{4}
\]

The required evolution choice is the six equations

\[
 h^\mu{}_\alpha h^\nu{}_\beta Q^{\alpha\beta}=0,\qquad
 Q^{\mu\nu}=T^{\mu\nu}-\tfrac12 g^{\mu\nu}
                                      g_{\rho\sigma}T^{\rho\sigma}.
                                                               \tag{5}
\]

Because tr_g T=-H+tr_h P and the spatial dimension is three, (5) implies
tr_h P=3H and hence

\[
                         P^{ij}=Hh^{ij}.                       \tag{6}
\]

These statements also hold with S and its density-valued trace reversal
in (5). In coordinates adapted to the foliation the precise contravariant
form is

\[
 Q^{ij}+\beta^i Q^{0j}+\beta^j Q^{i0}
                  +\beta^i\beta^j Q^{00}=0.                    \tag{7}
\]

Equivalently, lower BOTH spacetime indices on Q and impose Q_ij=0,
since partial_i are slice tangent. Merely imposing contravariant Q^{ij}=0
is not (5) for general shift. This is a choice of gravitational residual
evolution equations, not a proof that these equations form a well-posed
evolution system for the parent fields.

The four constraints H=M_i=0 are exactly the four coordinate density
constraints S^{0nu}=0, with explicit conversion

\[
 S^{00}=\frac{v}{N^2}H,\quad
 S^{0i}=v\left(\frac{M^i}{N}-\frac{\beta^i H}{N^2}\right),\quad
 H=\frac{N^2}{v}S^{00},\quad
 M_i=\frac{N}{v}h_{ij}(S^{0j}+\beta^j S^{00}).                \tag{8}
\]

Thus H here is the normal projection of the Euler tensor, not twice that
projection and not an ADM scalar constraint with an implicit conventional
factor. Equations (6) and (8) fix all signs and density normalizations.

## 3. Negative Control: Naive Spatial Residual Evolution

At a frozen normal point g=eta, N=1, beta=0, v=1, the naive choice
S^{ij}=0 gives the principal subsystem, for V=(S^{00},S^{01},S^{02},S^{03}),

\[
 \partial_t V+A^k_{\rm naive}\partial_k V=0,\qquad
 A_{\rm naive}(\xi)=
 \begin{pmatrix}
 0&\xi_1&\xi_2&\xi_3\\
 0&0&0&0\\0&0&0&0\\0&0&0&0
 \end{pmatrix}.                                               \tag{9}
\]

The notation A(xi) denotes the spatial Fourier/principal contraction;
equivalently the equations are partial_t S^{00}+partial_i S^{0i}=0,
partial_t S^{0j}=0. For xi nonzero, A_naive has rank one, its square is
zero, and it has a nontrivial Jordan block. It is not diagonalizable and
admits no positive definite symmetrizer: a matrix symmetric in a positive
inner product must be diagonalizable. Explicitly, S^{0i}(t)=S^{0i}(0)
and S^{00}(t)=S^{00}(0)-t partial_i S^{0i}(0); high spatial frequencies
give derivative loss. Zero-data uniqueness in a suitably smooth class is
not ruled out by this example, but a uniform same-order symmetric
hyperbolic energy estimate is. The naive choice fails the requested
positive-symbol test already at the normal point.

## 4. Exact Conditional Propagation Equations

Fix the extrinsic-curvature sign and acceleration by

\[
 K_{ij}=-h_i{}^\mu h_j{}^\nu\nabla_\mu n_\nu
        =-\frac{1}{2N}(\partial_t-\mathcal L_\beta)h_{ij},\quad
 K=h^{ij}K_{ij},\quad a_i=D_i\log N.                           \tag{10}
\]

Then nabla_mu n^mu=-K. For clarity, the two divergence projections BEFORE
imposing (6) are

\[
 n_\nu\nabla_\mu T^{\mu\nu}
 =-n(H)+KH+K_{ij}P^{ij}-D_iM^i-2a_iM^i,
\]
\[
 h_i{}^\nu\nabla_\mu T^\mu{}_\nu
 =h_i{}^\nu n^\mu\nabla_\mu M_\nu-KM_i-K_i{}^jM_j
        +Ha_i+D_jP^j{}_i+a_jP^j{}_i.                          \tag{11}
\]

For a spatial covector,
h_i{}^nu n^mu nabla_mu M_nu =
N^{-1}(partial_t-L_beta)M_i+K_i{}^j M_j.
Substitute (6) into (11), and set both projections to zero using (1):

\[
 (\partial_t-\beta^j\partial_j)H+N D_iM^i
              =2NKH-2M^iD_iN,                                \tag{12}
\]
\[
 (\partial_t-\mathcal L_\beta)M_i+N D_iH
              =NKM_i-2H D_iN.                                \tag{13}
\]

Here (L_beta M)_i=beta^j partial_j M_i+M_j partial_i beta^j.
Thus the shift-gradient term on the right when (13) is written with the
transport derivative is +M_j partial_i beta^j. All terms on the right and
all spatial-connection terms are linear homogeneous in (H,M). No source
independent of the constraints remains under the stated open-set hypotheses.

As an immediate flat check, the positive choice is P^{ij}=H delta^{ij}
and gives partial_t H+partial_i M_i=0,
partial_t M_i+partial_i H=0, including the plus signs in both spatial
couplings. These signs produce real characteristic speeds.

## 5. Explicit Symbol and Uniform Positive Symmetrizer

For U=(H,M_1,M_2,M_3)^T, (12)-(13) have the form
partial_t U+A^k partial_k U=B U. Their 4-by-4 principal symbol is

\[
 A(\xi)=-\beta^k\xi_k I_4+N
 \begin{pmatrix}
 0&h^{1k}\xi_k&h^{2k}\xi_k&h^{3k}\xi_k\\
 \xi_1&0&0&0\\
 \xi_2&0&0&0\\
 \xi_3&0&0&0
 \end{pmatrix},\qquad
 W=\begin{pmatrix}1&0\\0&(h^{ij})\end{pmatrix}>0.              \tag{14}
\]

W A(xi) is symmetric, with off-diagonal entries N h^{ik}xi_k.
The characteristic speeds are

\[
 -\beta^i\xi_i+N|\xi|_h,\quad
 -\beta^i\xi_i-N|\xi|_h,\quad
 -\beta^i\xi_i\ \text{(twice)},\qquad
 |\xi|_h^2=h^{ij}\xi_i\xi_j.                                 \tag{15}
\]

The two transport modes have xi_i M^i=0. At a normal point W=I_4 and
A(xi) has symmetric off-diagonal blocks xi^T and xi. There is no Jordan
degeneracy of the negative control. Multiplication by W gives a symmetric
hyperbolic system with positive time matrix W, regardless of shift size.

To connect quantitatively to HC_Cartan_Joint_Neighborhood.md, suppose the
metric on the region obeys its analytic coframe bound ||E-I||_2<=d and put

\[
 q=d(2+d),\quad a=1-q>0,\quad b=1+q,\quad
 z=\frac{d(2-d)}{(1-d)^2}<1.
\]

The joint estimates imply

\[
 aI\le(h_{ij})\le bI,\qquad
 (1+z)^{-1/2}\le N\le(1-z)^{-1/2},\qquad
 |\beta|\le\frac{z}{1-z},
\]
\[
 \min(1,b^{-1})I_4\le W\le\max(1,a^{-1})I_4,\qquad
 a^{3/2}\le\sqrt h\le b^{3/2}.                                \tag{16}
\]

Indeed ||g-eta||<=q bounds the spatial block on both sides, while
||g^{-1}-eta||<=z bounds g^{00} and the vector g^{0i}. These inequalities
give a uniform symmetrizer and uniformly bounded characteristic speeds
throughout such a metric ball, not just at the origin. The saved joint
ball has radius 1/16384 and reported d approximately 2.989405570e-9,
z approximately 5.978811166e-9. Its numerical margins are floating-point
evaluations, not interval-certified bounds; (16) is the analytic statement.

The numerical bounds refer to the comparison chart. An arbitrary different
spacelike slicing uses (3)-(15) with its own lapse, shift, and positive
spatial metric. On a compact regular slab they again give uniform constants
provided the slicing stays quantitatively spacelike and the chart stays
regular. The original chart's tiny numerical margins do not transfer to
uncontrolled coordinate changes or slicings approaching null. No normal-
cone estimate for the probe/constitutive block is needed for this residual
subsystem.

## 6. Energy Estimate and Conditional Zero Propagation

Assume coefficients are sufficiently regular for (12)-(13) and energy
integration, for example C^1 lapse, shift and spatial metric with bounded
first derivatives on a compact slab, N bounded away from zero, and the
uniform spatial-metric bounds above. Smooth parent fields and the regularity
needed to form their Euler residuals are a sufficient setting. The metric
ball alone supplies no bounds on arbitrary solution derivatives; those are
additional regularity assumptions in the energy estimate.

Set

\[
 e=\tfrac12(H^2+h^{ij}M_iM_j),\qquad
 \mathcal E(t)=\int_{\Omega_t} e\sqrt h\,d^3x.                 \tag{17}
\]

For a fixed coordinate spatial domain the exact balance law is

\[
 \partial_t(\sqrt h\,e)
 +\partial_i\{\sqrt h\,(NHM^i-\beta^i e)\}
 =\sqrt h\left[
   \tfrac32 NK H^2+\tfrac12 NK |M|_h^2
   +N K_{ij}M^iM^j-3H M^iD_iN\right].                        \tag{18}
\]

To check the lower-order coefficients, use
(partial_t-L_beta)h^{ij}=2N K^{ij},
partial_t sqrt(h)=sqrt(h)(-NK+D_i beta^i),
and the product divergence of N H M^i. In particular the two acceleration
couplings in (12)-(13) contribute -4 H M^i D_iN before this last product
divergence contributes +H M^i D_iN. This accounts for the -3 in (18).

The absolute value of the right side is at most C(t) sqrt(h) e. One
explicit adequate choice, taking spatial suprema, is

\[
 C(t)=\sup_{\Omega_t}\left(
       3N|K|+2N|K_{ij}|_{h,\mathrm{op}}+3|DN|_h\right).        \tag{19}
\]

Take C integrable in time. For periodic slices, compact slices without
boundary, compact support with no boundary flux, or a domain with
nonnegative outward energy flux / homogeneous incoming constraint data,
integration and Gronwall give

\[
 \mathcal E(t)\le\mathcal E(0)
                 \exp\left(\int_0^t C(s)\,ds\right).          \tag{20}
\]

For an artificial timelike boundary, zero initial data alone are insufficient:
incoming constraint modes must be excluded. Locally one can instead use
a shrinking domain whose boundary moves inward faster than the largest
coordinate characteristic speed. On a Euclidean unit spatial covector
that speed is bounded by |beta|+N/sqrt(a). The moving-boundary energy
term then makes the outward flux nonnegative, giving (20) in the resulting
local domain of dependence. A small interior cylinder/cone fitting inside
the open region and the joint ball suffices; the Euclidean four-ball is
not itself being asserted to be a global time slab.

Consequently H=M_i=0 initially implies H=M_i=0 throughout that domain.
With (6), this gives T=0, hence S=0 and the complete coframe Euler
equation. The uniform positivity in (16) makes the energy coercive in
the four constraint components, so this is a same-order energy argument,
unlike the naive normal-point control.

## 7. Exact Scope of the Conclusion

Conditional theorem: along any sufficiently regular fields satisfying the
exact eliminated Cartan equation, R=0 and all F=0 on an open region, the
assumed Ward identity (1), and the six gravitational evolution equations
(5), vanishing initial gravitational constraints propagate on a spacelike
foliation subject to the domain/boundary conditions above.

This establishes a symmetric hyperbolic subsystem for the four gravitational
Euler residuals. It does not establish hyperbolicity, solvability, gauge
closure, or existence for the full parent field equations. It proves no
propagation of R or F and cannot justify assuming them from initial values
alone. If those residuals are nonzero, their Ward-identity source terms
must be retained and the homogeneous proof does not apply. The joint
Taylor fields have nonzero R/F away from the origin, so their coefficient
regularity makes (16) available but does not satisfy the hypotheses of
this conditional theorem. Deriving/verifying (1) for the parent remains
separate from this independent constraint calculation.
