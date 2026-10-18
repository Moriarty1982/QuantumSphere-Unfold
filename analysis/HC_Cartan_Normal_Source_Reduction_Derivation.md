# Finite-Point Normal Source Reduction

Date: 2026-10-18. Scope: the added neutral odd-cross Einstein-Cartan comparison model, at the saved regular normal point. The action parameters M and Q, gravitational coefficient and vacuum term, multiplier value, and all retained lower/spatial data are fixed. This note derives a finite-dimensional inverse statement; it does not assert regional constraint closure or hyperbolicity.

## The actual affine normal system

Use `HC_Cartan_Joint_Neighborhood.load_data()` for the current prepared data, point, joint higher jets, extras, and provenance report. The normal matrix itself is constructed by `HC_Cartan_Spatial_Propagation.normal_curl_system(prepared, point)` and needs only the prepared data and point.

In that function the 56 real unknowns are absolute entries, ordered as

\[
x=(E_{,00}\ [16],\ \operatorname{realify}\Psi_{,0}\ [24],\
       \lambda_{,0}\ [16])\in\mathbb R^{56}.
\]

The function replaces exactly these entries in copies of the saved point. It retains every other second coframe entry, spatial spinor derivative, spatial multiplier derivative, and the multiplier value. The normal frame is E=I, dE=0. The residual is affine in x:

\[
\mathcal R(x)=b+Nx\in\mathbb R^{68},\qquad
b=\mathcal R(0),\qquad N_{:j}=\mathcal R(e_j)-b.
\]

The first 56 rows are the original point equations after algebraic elimination of the same Cartan connection: 16 constitutive constraints, 24 real probe Euler components, and 16 coframe Euler components. The final 12 rows are the mixed (0,i) constitutive curls, i=1,2,3, with four coframe components each. The code takes the first three antisymmetric coordinate pairs in its declared pair ordering.

Thus the unforced system is Nx=r with r=-b. For an explicitly specified residual target t, the algebraic right-hand side is r=t-b. Allowing arbitrary r in the theorem below is linear algebra; it does not authorize changing the physical action or inserting arbitrary forcing into its Euler equations. A perturbation delta x about a saved x_* instead satisfies N delta x=t-\mathcal R(x_*). Do not confuse this increment convention with the function's absolute-entry convention.

Writing F=C_Q-E for the constitutive residual, the appended curls are

\[
\partial_0F_{ai}-\partial_iF_{a0}=0.
\]

They follow from F=0 on a sufficiently differentiable field. Symmetric second spinor derivatives cancel in this antisymmetrization. At the normal point dE=0, the explicit first-coframe terms vanish, as reflected in `curl_constraints`. These are necessary differential consequences, not twelve independent new action laws. They need not follow from F=0 at a single isolated point: imposing them restricts which point jets can extend to a field satisfying F=0. Neither their inclusion nor their satisfaction proves propagation of all constraints.

## Orthonormal kernel split

Let G0 be `HC_Cartan_Regular_Gravity.coframe_normal_gauge_basis()`, a 56-by-10 matrix. Its four coordinate columns and six Lorentz columns have support only in the coframe acceleration block. They are the exhibited leading normal gauge directions. Orthonormalize their span to obtain G with G^T G=I_10. This Euclidean orthonormalization is a coordinate convention, not a Lorentzian inner product or a complete gauge-fixing theorem.

Let C be the 56-by-6 `basis` returned by `HC_Cartan_Remaining_Multiplier.canonical_basis(prepared)`. Its first three columns are axial-source-null spatial multiplier velocities. Its last three combine longitudinal symmetric spatial coframe accelerations with compensating multiplier velocities. This construction requires the weighted axial temporal component and spatial norm to be nonzero; the module explicitly guards these conditions.

Define

\[
\widetilde C=(I-GG^T)C,\qquad
U=\operatorname{orth}(\widetilde C).
\]

Here orth means any full-rank thin QR or SVD orthonormalization. At this point G0^T C=0 already, but projection makes the definition robust to a different canonical representative. The requirements are

\[
NG=0,\quad NU=0,\quad G^TU=0,\quad U^TU=I_6,
\qquad \ker N=\operatorname{im}G\oplus\operatorname{im}U.
\]

U spans the complement represented by C; its columns need not equal the canonical columns or retain their normalization and ordering. In particular, a coefficient vector q in U coordinates is not automatically the canonical pair (w,v). With T=U^T C, one has C=UT at the saved orthogonal representative and q=T(w,v). In general the equality is (I-GG^T)C=UT, with any removed G component absorbed into g. T is invertible when the projected canonical basis has rank six.

## Finite-point theorem and proof

Assume N has rank 40 and the kernel split just stated. Let L have 28 orthonormal columns spanning ker(N^T), and let N^+ be the Moore-Penrose pseudoinverse in the declared real Euclidean coordinates. For each fixed r in R^68,

\[
\begin{split}
\{x:Nx=r\}&=\varnothing &&\text{if }L^Tr\ne0,\\
\{x:Nx=r\}&=\{N^+r+Gg+Uq:
             g\in\mathbb R^{10},q\in\mathbb R^6\}
             &&\text{if }L^Tr=0.
\end{split}
\]

Equivalently, solvability holds if and only if the 28 left compatibility conditions L^T r=0 hold; conditional on them, every solution has the displayed form with unique g and q. The statement does not claim that the displayed expression solves incompatible data.

Proof: the fundamental orthogonality relation gives im(N)=ker(N^T)^perp, so L^T r=0 is necessary and sufficient. In that case NN^+r=r. Subtracting N^+r from any solution gives an element of ker N, and the orthonormal 10+6 split gives its unique coordinates. Conversely N annihilates both added terms. Also N^+r is perpendicular to ker N, hence g=G^T x and q=U^T x. It is the unique minimum-norm particular solution. This proves the assertion.

Useful equivalent identities are

\[
NN^+=I_{68}-LL^T,\qquad
N^+N=I_{56}-GG^T-UU^T.
\]

For incompatible data the same expression has residual Nx-r=-LL^T r, independent of g and q. A pseudoinverse must therefore be accompanied by a compatibility check; a least-squares return value alone is not a solution certificate. The 28 conditions are independent as linear conditions on arbitrary r. Their expressions in the frozen physical data can have additional identities or restrictions and need not be 28 new independent field laws. The six-dimensional left obstruction computed for curls induced on the original kernel in `normal_curl_system` is not the full 28-dimensional left kernel of N.

## What six arbitrary source functions mean

At one fixed admissible point q is an arbitrary six-vector selecting the normal-kernel component after the ten leading gauge coefficients g are specified. One may call q six prescribed source functions when writing a candidate local normal reduction. This means that the algebraic normal equations leave these six coefficients undetermined. They are not six arbitrary components of r, six additional action couplings, or six proved freely evolving physical degrees of freedom.

Over varying data such a formula is conditional on constant rank, a regular canonical chart, and suitably smooth choices of G and U. A raw QR/SVD basis can change signs or rotate under parameter variation, so its numerical coefficients do not automatically define smooth scalar functions. Even with a smooth local frame and compatible r at every point, arbitrary smooth q need not be realizable by derivatives of one common field: spatial equations, equality of mixed derivatives, differentiated compatibility, and higher completion conditions can restrict q and its derivatives.

Nor is the six-dimensional complement proved gauge. A principal normal kernel tests only this truncated normal response. Gauge symmetry requires an appropriate transformation of full fields preserving the action/equations, with the corresponding identities and compatibility at higher orders. In the canonical construction, three directions annihilate the Cartan source response; the other three require coframe/contorsion compensation. Neither property alone establishes action invariance. Even a zero higher response in a particular frozen test would not establish such invariance.

This inverse is consequently a finite-point normal rank inverse. It provides no full regional PDE principal-symbol analysis, symmetrizer, uniform evolution estimate, subsidiary-system closure, or Cauchy existence/uniqueness theorem. Probe positivity or other previously bounded subblocks do not supply these missing steps for the full coupled system.

## Bounded numerical check

A fresh check used the current fingerprint-checked joint loader and built only the 68-by-56 normal system and its small bases. No higher completion solve, full test suite, or higher response calculation was run. Absolute rank cutoff: 1e-9 for the reported basis/matrix ranks.

| Quantity | Result |
| --- | ---: |
| Shape of N | 68 by 56 |
| Rank of original 56 rows | 34 |
| Curl rank induced on original kernel | 6 |
| Rank of N | 40 |
| Ranks of G0, C, [G0,C] | 10, 6, 16 |
| Rank of (I-GG^T)C | 6 |
| Smallest retained singular value of N | 0.105944195691534 |
| Largest discarded singular value of N | 3.47e-15 |
| Norm of NG | 3.54e-16 |
| Norm of NC | 8.61e-15 |
| Norm of NU | 7.50e-15 |
| Norm of G0^T C | 0 (computed) |
| Norm of [G,U]^T[G,U]-I | 7.31e-16 |
| Full SVD kernel missed by span([G0,C]) | 1.29e-13 |
| Norm of L^T b | 2.23e-14 |
| Affine solver residual norm | 1.13e-13 |

The annihilation, independence, and dimension count check that the canonical quotient spans the entire remaining kernel at this point, to floating-point accuracy. The exact theorem above is conditional on its exact rank/kernel hypotheses; these diagnostics are not interval-certified proofs of rank throughout a neighborhood. The affine solver residual refers to its returned particular solution, not a separately recomputed saved-point residual.

## Higher-response provenance and logical pitfalls

`HC_Cartan_Remaining_Multiplier.load_data()` reads the older `HC_Cartan_Regular_Gravity.json` joint completion. Do not use that loader for a claim about the latest joint higher response. Obtain `(prepared, point, jets, extras, report)` together from `HC_Cartan_Joint_Neighborhood.load_data()`. It checks source fingerprints and the scalar-completion fingerprint and checks that the retained spinor Hessian equals the saved one. It unpacks current p2, l2, e3, p3 and the additional e4, l3, p4 from the matching joint report. Do not combine current lower jets with old l2/e3/p3 or old extras.

Passing the current jets to `gravity.equations` evaluates only that function's 384-component first-constraint/first-probe/first-gravity/second-constraint vector. It does not evaluate the entire later joint completion or its fourth-order field data. Claims at that later order must use the matching evaluators and extras.

If a normal entry changes while current higher jets are frozen, explicitly label the result a frozen-higher-jet residual difference. The changed point generally no longer satisfies the saved higher equations. A nonzero difference shows that the saved higher completion is not unchanged along that finite displacement; it does not prove that no new higher completion exists. No completion solve is performed here.

Also distinguish a derivative at the saved point from a unit finite difference. Higher residuals contain products of lower jets, so affinity in higher unknowns does not imply affinity in the normal variables being varied. A secant response or a two-step affinity diagnostic is not automatically an exact linearized response. The saved joint jets are finite Taylor data, not a regional exact solution; their provenance and finite completion properties cannot turn this normal inverse into a regional theorem.
