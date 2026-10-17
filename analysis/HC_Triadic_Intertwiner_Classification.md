# What the Triadic Links Determine About Gauge Representations

Date: 2026-10-17. Status: conditional finite-dimensional representation theorems, explicit maximal-commutant calculations and simultaneous local-frame transport of the preceding coherent branch. No native channel charges, C7 embedding, Standard Model gauge group or physical frame shift is derived. Main TeX/PDF unchanged.

This continues [triadic gauge factorization](HC_Triadic_Gauge_Factorization.md). The preceding solution assumed equivalent channel representations. Here the question is when fixed equivariant links **force** that equivalence, and which further assumptions are needed to select the common gauge algebra.

## 1. Native Data: What Is and Is Not Specified

The probe block `prop:triadic-two-probe` in `sources/research/parts/v470/10_sphaera_and_physics.tex` names `g_Y T_12` and `chi T_i_perp`, but does not evaluate these operators or assign gauge generators to ART/QFT/orthogonal probe channels. The same passage's three channels must still be distinguished from color and generation indices.

`prop:structural-matter-gauge-mass` in `16_master_model.tex` reads effective gauge symmetry as invariance of closure-compatible transport. This motivates testing the admissible intertwiners; it does not specify all their matrix entries or their maximal commutant.

There is a further important gap: `sec:theorem7` in `12_structural_core.tex` uses general readout maps `R_f:K->O_f`. They are **not** supplied as fixed orthogonal channel projectors. Conditions that require a gauge transformation to preserve each channel label separately are therefore additional hypotheses, not consequences of the readout-map notation or of C7 closure. Channel-label projectors below are not the native C7 projector.

## 2. Relative Representations Can Be Forced Without Fixing a Charge

Let H_i and H_0 carry finite-dimensional irreducible complex unitary representations of the same group. Suppose a nonzero fixed link `K_i:H_0->H_i` intertwines them. Infinitesimally, for a connected group,

\[
 T_i^aK_i=K_iT_0^a\quad\text{for all generators }a.       \tag{1}
\]

**Proposition.** The representations are equivalent and `K_i=s_i U_i`, where `s_i>0` and U_i is unitary. Along a connected graph of such links all channel representations are equivalent. The matrices need not be identical in separately chosen channel bases.

**Proof.** The kernel of K_i and its image are invariant subspaces. Irreducibility and nonzero K_i make the link injective and surjective. Taking adjoints of (1) shows that `K_i^dagger K_i` commutes with every Hermitian generator. Each eigenspace of this positive Hermitian matrix is invariant; irreducibility makes it `s_i^2 I`. Thus `U_i=K_i/s_i` is unitary and (1) gives `T_i^a=U_i T_0^a U_i^dagger`. Propagate this along connected edges. The group version follows from the same argument for its unitary representation matrices. No assertion about disconnected-group representations follows from Lie-algebra data alone.

For one-dimensional U(1) representations, nonzero constant links therefore require equal charges. But their common value q is unconstrained: `q=-3.2,0,1,12` all satisfy the same finite intertwiner equations. Group global form, charge quantization, normalization, chiral assignments and anomaly constraints have not been determined. A link between inequivalent representations needs additional transforming coupling data or must vanish.

If the representations are reducible, a nonzero link may couple only shared subrepresentations. Its kernel can retain independent transformations. One must not extend the irreducible conclusion to every direction of an operator-valued channel merely because one matrix element is nonzero.

## 3. Invertible Links Give a Computable Root Test

On three equal-size carriers, take a Hermitian resonance with scalar diagonal blocks and links

\[
 \Omega=\begin{pmatrix}
 mI&K_{12}&K_1\\K_{12}^\dagger&mI&K_2\\
 K_1^\dagger&K_2^\dagger&mI
 \end{pmatrix}.
\]

Assume **fixed channel labels**, so a Hermitian symmetry generator is `T=diag(T_1,T_2,T_0)`. If K_1,K_2 are invertible, (1) gives

\[
 T_i=K_iT_0K_i^{-1}.                                      \tag{2}
\]

Hermiticity of T_i is equivalent to

\[
 [T_0,K_1^\dagger K_1]=[T_0,K_2^\dagger K_2]=0.            \tag{3}
\]

The additional direct link requires

\[
 [T_0,L]=0,\qquad L=K_1^{-1}K_{12}K_2.                    \tag{4}
\]

Equations (3)--(4), with T_0 Hermitian, are necessary and sufficient for the full fixed-label generator to commute with this Omega. **Proof:** (2) solves the two tree edges; taking its adjoint yields (3). Substitution into `T_1 K_12=K_12 T_2` yields (4). Lower-edge conditions are adjoints. The scalar diagonal blocks impose no further condition. Noncentral diagonal Omega_i would impose additional commutators and cannot be dropped in a native application.

The corresponding slots already exist in the native block: `K_i=chi T_i_perp` and `K_12=g_Y T_12`. Hermitian paired blocks and the finite positive adjoint used here are comparison hypotheses, not evaluated native adjoint relations. No new interaction is proposed by naming the existing direct-link slot.

The polar decomposition also clarifies (2): since T_0 commutes with the positive polar factor of K_i, T_i is unitarily, not just nonunitarily, equivalent to T_0 on this residual algebra. Assuming arbitrary Hermitian T_0 before checking (3) fails for anisotropic links.

L is a relative-path endomorphism on the anchor channel. It is **not** a derived spacetime Wilson loop, gauge curvature or physical holonomy. It may be nonunitary and dimensionful; only its commutant is used here. Under channel basis changes it transforms as `L->U_0 L U_0^dagger`.

## 4. Explicit Maximal Compatible Algebras

Use `m=.6`, auxiliary channel dimension d=2, `K_1=4I`, `K_2=.7I`. These are the prepared finite comparison links, not evaluated native T_i_perp. A real-linear system on Hermitian matrices computes the joint commutant of Omega and the three fixed channel-label projectors. The numerical rank threshold is displayed in the calculation; the following dimensions also have direct algebraic explanations.

| Fixed data | Real Hermitian dimension | Reason |
|---|---:|---|
| Scalar tree links, channel labels fixed | 4 | T_1=T_2=T_0; maximal common u(2) |
| Same Omega, no fixed channel-label condition | 12 | Three distinct resonance eigenvalues, each with multiplicity two |
| K_1=diag(4,2), K_2=.7I | 2 | T_0 must commute with diag(16,4) |
| Two links with noncommuting simple Gram matrices | 1 | Only a common scalar generator remains |
| Extra direct link `.2 exp(.3i) I` | 4 | L is scalar |
| Extra direct link `.2 diag(exp(.3i),exp(-.3i))` | 2 | T_0 must also commute with a noncentral simple loop map |
| K_1=diag(4,0), K_2=.7I | 3 | A disconnected direction in channel 1 retains its own charge |
| K_1=0, K_2=.7I | 8 | One free u(2) channel plus the connected common u(2) |

These are **maximal algebras compatible with specified fixed data**, not a determination of the actual gauge algebra, its global group or a dynamical symmetry-breaking process. The physical gauge algebra could be a proper subalgebra. The first result explains the preceding common factor if fixed labels and scalar full-rank links are justified. The second proves that Omega alone does **not** force that factorization. Invariance of C7 alone does not add the missing fixed-label conditions either.

Unequal scalar link strengths and scalar phases leave the first common algebra unchanged as long as the links remain nonzero. Thus the numbers 4 and .7 cannot be read as different gauge charges by themselves. Noncentral Gram or loop data can reduce the maximal compatible algebra. Whether the native tensor activation supplies such data remains an unevaluated operator question.

## 5. Scalar Phase: Same Algebra Does Not Mean Same Spectrum

The extra direct link is absent from the earlier solved star reference; this paragraph is a **separate finite control**, not a new solved field branch. With `K_12=.2 exp(i phi) I`, changing phi leaves the common u(2) algebra intact but can change the resonance spectrum.

For scalar links a=4, b=.7, c=.2 and channel dimension d=2, the closed triangle contributes

\[
 \operatorname{Tr}\Omega^3
 =d\{3m^3+6m(a^2+b^2+c^2)+6abc\cos\phi\}.
\]

Changing phi from 0 to pi/2 changes this trace by `2*6*4*.7*.2=6.72` and the sorted eigenvalue vector by norm about `.11739`. No simultaneous unitary conjugation can do that. A genuine relative scalar cycle phase can therefore affect this finite resonance even though it does not reduce the allowed gauge algebra. This is not a physical mass identification, nor is every scalar frame phase in the paper identified with this cycle phase.

## 6. Different Local Channel Bases Preserve the Existing Solution

Return to the preceding **star** comparison and its coherent curved-product solution. In the gauge-major ordering define

\[
 S(x)=\sum_{i=1,2,0}U_i(x)\otimes|i\rangle\langle i|,
\]

using `U_1=exp(.4 i t sigma_1)`, `U_2=exp(.7 i z sigma_3)`, `U_0=I`. The coordinate rates are arbitrary comparison inputs. Transform all internal data together:

\[
 \Psi'=S\Psi,\quad P'=SPS^\dagger,\quad
 \Omega'=S\Omega S^\dagger,\quad
 B'_\mu=SB_\mu S^\dagger-(\partial_\mu S)S^\dagger.         \tag{5}
\]

Then direct differentiation gives

\[
 D'_\mu\Psi'=SD_\mu\Psi,\quad
 F'_{\mu\nu}=SF_{\mu\nu}S^\dagger,\quad
 D'_\mu P'=S(D_\mu P)S^\dagger.
\]

The gauge embedding must transform too: `T_a'=S(T_a tensor I3)S^dagger`. Its source projection is

\[
 \Pi'_g(X)=S\Pi_g(S^\dagger X S)S^\dagger.
\]

These are simultaneous local changes of internal basis, **not** three additional physical gauge symmetries in the original fixed common embedding. The transformed connection space contains the fixed inhomogeneous term in (5); it is not obtained merely by declaring a larger freely variable connection. The external metric, spin connection and gamma matrices are unchanged. No Lorentz-frame or native matter/tachyon/photon shift is identified with S.

At `(.4,.9,.4,.02)`, direct matrix jets and independently differentiated full curvature give residual norms about `3.0e-16` for the Dirac equation, `1.2e-10` for the correctly projected connection equation, and `5.0e-16` for curvature covariance. Mass-operator eigenvalues are unchanged. Omitting the connection term in (5) leaves Dirac residual `.20554`; transforming the probe/connection but freezing Omega leaves `.32957`. Independent channel bases are harmless only when the coupled data are transported consistently.

The full unprojected equation remains outside the comparison's gauge field space, as in the previous note. H_C is still eliminated on the hard-dependent comparison domain, not also varied independently. The C7 embedding, source/action dictionary, native bilinear metric, global boundary data and backreaction are not supplied by this basis change.

## Outcome and Reproduction

The relative-representation assumption can now be replaced by a precise conditional test: evaluate the native fixed equivariant links, their kernels/Gram matrices, any relative-path maps, the diagonal blocks, and the actual gauge/readout invariants. Nonzero links between irreducible channels force equivalence; scalar full-rank links with fixed labels force a maximal common factor. Neither statement fixes an absolute charge, proves those native hypotheses or equates readout maps with fixed projectors.

- [Calculation](HC_Triadic_Intertwiner_Classification.py) and [saved results](HC_Triadic_Intertwiner_Classification.json).
- Run `python -B analysis/HC_Triadic_Intertwiner_Classification.py --output analysis/HC_Triadic_Intertwiner_Classification.json`.
- Run `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_triadic_intertwiner_classification.py`.

Thirty focused checks cover the Hermitian linear constraints, root reduction, irreducible/equivalent-basis witnesses, kernels, missing readout locks, scalar versus matrix cycle phases, spectrum changes, full local-frame jets and projected curved equations, plus omitted-connection/mass controls. The written finite proofs, not the SVD rank tests alone, support the conditional claims. No main-TeX edit, PDF rebuild, release activation or Git operation is introduced.

The following [cross-readout/spectral gauge calculation](HC_Spectral_Gauge_Completion.md) replaces assumed channel locks by a precise conditional invariance test for the paper's existing ART/QFT cross-bilinear. If that readout transforms covariantly instead, the larger resonance commutant remains possible; the source does not remove its extra directions. An explicit local completion supplies their distinct field responses and checks why the previous common connection is not a generic consistent truncation of that larger theory. The actual native observable/gauge contract remains unproved.
