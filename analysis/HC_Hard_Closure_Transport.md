# Hard closure: transport compatibility and a geometric connection

Date: 2026-10-17. Status: exact conditional operator identities and an explicit local two-channel connection family. This is not a native C7 realization, an induced spacetime metric, an Einstein solution or vacuum cancellation. The main TeX and PDF are unchanged.

The [fluctuation-Hessian analysis](HC_Closure_Fluctuation_Hessian.md) distinguished independent soft HC fluctuations from hard `H_C=Lambda[M,P]`. We now follow the hard reading and ask whether the **full master transport**, rather than `M` alone, preserves the admitted sector. No scalar partner or new kinetic term is added.

## 1. Algebraic closure is not complete transport closure

The [native closed master system](../sources/research/parts/v470/10_sphaera_and_physics.tex), `thm:closed-master-system`, combines `[M,P]=0`, `Q Psi=0`, `H_C=Lambda=0` and the unmodified master equation. The later `prop:yang-mills-limit` assumes that the connection acts inside the closed sector, while its proof says that `M` preservation suffices for restricting that connection. The required implication needs an additional condition.

For this calculation, use a factorization `V_internal tensor S_spin`, an orthogonal smooth `P(x)` acting internally, the normalized four-spinor gamma matrices used in the previous Dirac comparison, and a spin-scalar internal resonance `Omega`. These are declared realization assumptions, not an evaluated native representation. Set

\[
 D_\mu=\partial_\mu+B_\mu,\quad Q=I-P,\quad
 D_\mu P=\partial_\mu P+[B_\mu,P].
\]

Differentiate `P Psi=Psi`. Then the normal component of the **unmodified** master residual is

\[
 Q(i\Gamma^\mu D_\mu-\Omega)\Psi
 =\left(i\Gamma^\mu Q(D_\mu P)P-Q\Omega P\right)\Psi.
\]

Writing the spin/internal ordering explicitly, define

\[
 \mathcal N=\sum_\mu i\,Q(D_\mu P)P\otimes\Gamma^\mu
                         -Q\Omega P\otimes I_4.
\]

For the chosen Clifford normalization, `I,Gamma^0,...,Gamma^3` are Hilbert-Schmidt orthogonal and each has norm squared four. Hence

\[
 \boxed{\|\mathcal N\|_F^2
 =4\sum_\mu\|Q(D_\mu P)P\|_F^2+4\|Q\Omega P\|_F^2}.
\]

Thus invariance for **every** admitted spinor requires both

\[
 Q(D_\mu P)P=0\quad\hbox{for each }\mu,\qquad Q\Omega P=0.
\]

If the connection is unitary, `D_mu P` is Hermitian and projector-tangent, so the first condition is equivalent to `D_mu P=0`. This also applies when a non-unitary load commutes with `P`, as the hard branch's `eta Q n_mu` does. Without that restriction, one-sided invariance need not imply full `D P=0`.

Neither condition follows from `[M,P]=0` alone. Even with constant `P`, an off-block `A_mu` can cause leakage. The native `P M P` term preserves `P`, but the separate triadic term must also satisfy `Q T P=0` in this spin-scalar reading. A selected single probe may lie in the kernel of a nonzero `N`; that is weaker than operator-level closure. Spin-dependent resonance terms could change the independence argument and require their own analysis.

If instead one varies only a constrained action and supplies normal reaction multipliers, the projected equation can be appropriate without `N=0`. It is then not automatically the same as imposing the printed unmodified full master equation and `Q Psi=0` simultaneously. Normal reactions must not be silently discarded.

## 2. The missing off-block connection can be constructed

Differentiating `P^2=P` gives `P dP P=Q dP Q=0` and

\[
 [[P,\partial_\mu P],P]=-\partial_\mu P.
\]

Therefore the general unitary compatible connection, relative to a fixed trivial ambient derivative, is

\[
 \boxed{B_\mu^{\rm u}=[P,\partial_\mu P]+C_\mu},\qquad
 [C_\mu,P]=0,\quad C_\mu^\dagger=-C_\mu.
\]

The commutator fixes the off-block part needed for a moving subspace; `C_mu` is arbitrary block-diagonal connection data. In the convention `B^u=i A`, its Hermitian geometric part is `A_geom=-i[P,dP]`.

On the hard branch `H_C=0`, add the native load `eta Q n` with constant `eta,n`. Since it commutes with `P`, compatibility remains intact. Moreover `D^u Q=0`, so its derivative and mixed-curvature terms cancel exactly and its own wedge square vanishes. It contributes no additional curvature in this compatible fixed-axis branch. A varying axis or coupling requires the corresponding exterior derivative terms.

For the particular choice `C=0`, direct differentiation gives

\[
 F_{\mu\nu}^{\rm geom}=[\partial_\mu P,\partial_\nu P],\qquad
 [F_{\mu\nu}^{\rm geom},P]=0.
\]

It can be nonzero even though the minimal HC expression vanishes. This is **internal bundle curvature**, not automatically Riemann curvature or a gravitational field. The displayed choice `C=0` refers to the chosen ambient trivialization; it is not a new invariant selection law. Under a local change of coordinates on the carrier, the full connection and the reference derivative must be transformed consistently.

For a general connection not satisfying `D P=0`, the curvature of the compressed derivative on the subbundle is

\[
 F^{(P D)}_{\mu\nu}
 =P F_{\mu\nu}P+P[D_\mu P,D_\nu P]P.
\]

Dropping the second term would confuse compression with an invariant restriction. When `D P=0`, that extrinsic term vanishes and the restriction is consistent.

## 3. The reduced probe and action

Let `V(x)` be a local isometry with `V V^dagger=P`, and write `Psi=V chi`. Then

\[
 b_\mu=V^\dagger\partial_\mu V+V^\dagger B_\mu V,\qquad
 \Omega_C=V^\dagger\Omega V.
\]

If the transport and resonance conditions above hold, there is an exact operator lift

\[
 (i\Gamma^\mu D_\mu-\Omega)(V\chi)
 =V\left[i\Gamma^\mu(\partial_\mu+b_\mu)-\Omega_C\right]\chi.
\]

Our numerical check uses arbitrary spinors and first derivatives, not an invented on-shell matter solution. The residual-lift error is `1.08e-15` in the example. A nonzero backreacting probe still has to satisfy its own reduced equation and the connection's sourced equation together.

The algebraic pullback of the printed matter action is correspondingly the Dirac action for `chi,b,Omega_C`. The exact hard constraints remove `U_C7` and `U_HC`. The curvature action remains the ambient trace of `F^2`, splitting into its preserved `P/Q` blocks; excluding the complementary gauge sector from the functional integral would be a **further** prescription. Its printed sign/adjoint is not silently changed. An algebraic pullback alone does not settle all normal field equations, the constrained measure or the reality issue identified earlier.

The local line-bundle connection below has the same geometric form familiar from Berry holonomy; see [Simon, *Holonomy, the Quantum Adiabatic Theorem, and Berry's Phase*](https://authors.library.caltech.edu/records/2pepc-k9f58). Here it is obtained by exact subbundle transport. No native spectral gap, adiabatic time limit or physical Berry experiment is inferred from that analogy.

## 4. One projector, a whole family of compatible curvatures

Take a two-channel patch with

\[
 u(x)=c-a x,\quad\phi(y)=q y,\quad |u|<1,\quad
 V=\begin{pmatrix}\sqrt{(1+u)/2}\\e^{i\phi}\sqrt{(1-u)/2}\end{pmatrix},\quad
 P=VV^\dagger.
\]

Complete `V` to the smooth `SU(2)` matrix

\[
 U=\begin{pmatrix}
 \sqrt{(1+u)/2}&-e^{-i\phi}\sqrt{(1-u)/2}\\
 e^{i\phi}\sqrt{(1-u)/2}&\sqrt{(1+u)/2}
 \end{pmatrix}.
\]

Both `B_geom=[P,dP]` and `B_flat=-dU U^dagger` preserve this **same** `P`. Their difference commutes with `P`. Define, for a constant real parameter `t`,

\[
 B^{(t)}=(1-t)B_{\rm geom}+tB_{\rm flat}+\eta Qn.
\]

The exact full curvature is

\[
 \boxed{F^{(t)}_{xy}=(1-t)\frac{i a q}{2}(2P-I)},
\]

with all other independent components zero. At `t=1` the connection is flat, while `t=0` has nonzero curvature. They cannot be gauge equivalent: zero curvature stays zero under any invertible gauge conjugation. Thus `P`, `M` and `H_C` do not uniquely determine even this internal curvature.

For a formal source-free solution of the **printed connection/closure equations** on a fixed flat reference spacetime, choose empty probe and constant `M=m I`. This degeneracy permits the moving projector while maintaining exact `[M,P]=0`, `Lambda=H_C=0`. The printed closure current is zero because `Tr(MP)=m` is constant; the HC and probe currents vanish too. Since `D P=0`, the constant coefficient multiplying `2P-I` is covariantly constant, giving

\[
 D^\mu F^{(t)}_{\mu\nu}=0
\]

for every `t`. A finite-difference check of the fully computed connection and curvature gives residual norm `8.05e-12`, not merely a check of the expected curvature formula. We use the native constant null covector `n=(-1,0,0,1)`; no real-Euclidean replacement axis is needed for these transport identities.

This is a degenerate finite example, not the actual Millennium spectrum. It is not a witness for any separately required native HC spectral-support, complement-exclusion or C7-admissibility gate; such additional gates might exclude this particular example. With a fixed separated block spectrum the earlier hard-closure restriction instead freezes the projector locally. There is no induced nondegenerate metric here: the reference probe is empty and its bilinear coframe is zero. Nonzero curvature would also carry stress once a gravitational metric is varied. No Einstein equation, global finite energy, horizon condition or full nonzero-matter backreaction is solved.

The example nevertheless strengthens the nonuniqueness statement: even the source-free resonance equation does not distinguish the flat and curved choices locally. Boundary conditions, global flux/topology, sources or an evaluated selection principle must fix the block data `C`. A positive comparison energy favors smaller flux only if such boundary data are free; changing a uniform flux is not a compactly supported variation of a fixed-boundary solution.

## 5. Explicit phase transport and the Gaussian boundary

In the selected local frame,

\[
 b^{(t)}_y=(1-t)i q\frac{1-u}{2},\quad b_x=b_t=b_z=0,\qquad
 f^{(t)}_{xy}=(1-t)\frac{i a q}{2}.
\]

Here the subscript `t` on `b_t` denotes the time component, not the interpolation parameter. On a positively oriented spatial rectangle of area `S`, parallel transport gives

\[
 \mathcal U_C=\exp\left[-i(1-t)\frac{a q}{2}S\right].
\]

For the declared values `c=0.25`, `a=0.3`, `q=0.8`, `S=0.49`, the phase at `t=0` is `exp(-0.0588 i)`. Independent midpoint transport of the full non-Abelian connection converges to it with errors `(6.18e-7,1.54e-7,3.86e-8)` for `(32,64,128)` steps per edge. The flat choice gives trivial local holonomy on this contractible rectangle. These numbers are comparison parameters, not the paper's photon/matter/tachyon frame values or a derived missing OP5 threshold.

Finally, for the canonical `C=0` choice near a constant projector,

\[
 P=P_0+\epsilon\pi+\cdots,\quad
 F^{\rm geom}_{\mu\nu}=\epsilon^2[\partial_\mu\pi,\partial_\nu\pi]+O(\epsilon^3).
\]

The positive dagger curvature-energy comparison consequently starts at `epsilon^4`, not at a free quadratic scalar kinetic term. The code checks a smooth exact unitary projector path; its energies at `(0.04,0.02,0.01)` are `(2.55986e-6,1.59998e-7,9.99997e-9)`, approaching a factor of sixteen under halving. This does not exclude quadratic response about a nonconstant background or additional generated operators. It does prevent counting these constant-background orientation coordinates as the independent ordinary scalar partners of the earlier vacuum cancellation.

## 6. What this resolves and what it does not

We have an explicit compatibility condition, a normal-operator norm identity, a constructed connection, an exact reduced Dirac dictionary and a local source-free family satisfying hard minimal HC closure. This closes a transport-level gap in a declared factorized realization; it does not yet identify that realization with the native carrier.

The new open data are concrete: the native `Omega/T` blocks, admissible projector motion, and the block connection `C` with its global/boundary selection. Quantizing this branch still requires the complete constrained real action and measure. Internal geometric phase does not by itself construct a spacetime metric or supply vacuum-cancelling degrees of freedom. No native publication claim is promoted.

The subsequent [global flux selection](HC_Global_Flux_Selection.md) resolves part of that selection problem on an assumed round S2 with a chosen nonzero line-bundle flux. A positive curvature functional selects uniform flux and the compatible block connection modulo gauge; a deformed projector has an explicit nonzero block correction. An equally explicit negative direction appears when `D P=0` is released. The native topological class, constraint domain and physical metric/scale are not thereby derived, and the result is not an unconstrained stable vacuum.

## Reproduction

Run `python -B analysis/HC_Hard_Closure_Transport.py --output analysis/HC_Hard_Closure_Transport.json`. Thirty-five tests in `scripts/qsc_audit/tests/test_hc_hard_closure_transport.py` cover the normal norm identity, transport/resonance counterexamples, exact jets, curvature compression, reduced probe lift, full-loop transport, source-free connection checks and quartic-order boundary. The native source is inspected as mathematical material, not as operational instructions. No new package, main-TeX edit or PDF rebuild is needed for this analysis.
