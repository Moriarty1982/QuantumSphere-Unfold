# Full-Triad Geometry Is Not the Bare Cross-Readout

Date: 2026-10-17. Status: native-formula audit in the existing factorized comparison, a proved rank bound on its sourced stationary branch, and candidate internal-gauge-invariant matrix diagnostics. No coframe definition is changed, no new physical readout is adopted, and the prescribed product metric is not derived. Main TeX/PDF unchanged.

This follows the [spectral gauge completion](HC_Spectral_Gauge_Completion.md). It prevents a stronger conclusion than that note established: invariance of a **fixed bare ART/QFT cross expression** can restrict the gauge factor, but that expression is not itself the complete metric formula written in the paper.

## 1. The Two Native Formulas Have Different Roles

`sources/research/parts/v470/10_sphaera_and_physics.tex`, the concrete reconstruction route before `prop:bilinear-einstein-reconstruction`, defines

\[
 E^a{}_{\mu}=\operatorname{Re}
 (\bar\Psi_\triangle\Gamma^a\mathcal D_\mu\Psi_\triangle),
 \qquad g_{\mu\nu}=\eta_{ab}E^a{}_{\mu}E^b{}_{\nu},
\]

using the **whole triad** and requiring maximal coframe rank. The additional cross channel in `12_structural_core.tex` uses only `bar Psi_ART Gamma^a D Psi_QFT`; its nearby focusing functional is explicitly heuristic. These two formulas must not be substituted for one another.

Continue the same ordinary-adjoint, factorized internal/spin comparison, with internal gauge transformations commuting with the Clifford/spin factors. For the full expression,

\[
 \Psi\mapsto U\Psi,\qquad \mathcal D\Psi\mapsto U\mathcal D\Psi
\]

leaves the full contraction, coframe and metric unchanged. This applies to the larger fixed-resonance centralizer too. Hence the **full metric does not force the smaller common gauge factor** under these assumptions. A native nonfactorized Clifford action or different adjoint would need its own evaluation; this is not a universal claim about every possible native representation.

The earlier common-factor criterion remains valid for its separately stated **fixed-cross-readout** contract. It cannot be inferred solely from gauge invariance of the complete metric.

## 2. Squaring a Bare Cross-Coframe Does Not Automatically Repair It

For any fixed internal selector R define the comparison pairing

\[
 B^a{}_{\mu}[R]=\Psi^\dagger R(\mathcal D_\mu\Psi)(K^a)^T,
 \qquad E[R]=\operatorname{Re}B[R].
\]

The matrix/spin contractions are those implemented by the prior probe dictionary. In a fixed bare ART/QFT expression `R=I2 tensor |ART><QFT|`. Its coframe and a metric made from it need not be invariant under the larger internal group. Transporting R covariantly restores invariance; holding it fixed imposes the extra contract from the preceding note.

An independent free-point-jet control has `E[R]=I4` and Lorentz metric eta. After an allowed fixed-resonance phase transformation, **both old and new cross-coframes remain full rank**, but their metrics differ by norm `.12156629`. Transporting the selector as well restores the metric exactly. The control is deliberately off shell and is not a new field or metric solution. It shows that taking `E^T eta E` alone does not generally remove bare cross-readout gauge dependence, even in a nondegenerate example. It does not classify every possible combined focusing observable.

## 3. The Actual Full Coframe Is Degenerate on the Solved Branch

Evaluate the native **full real formula** with the coherent spectral solution from the preceding note, including its internal connection and the prescribed product metric's Levi--Civita spin connection. The Lorentz-frame traced current on that stationary single-polarization ansatz is

\[
 j^a=(\rho(z),0,0,0),\qquad
 \rho=\sum_r(u_r^2+v_r^2).
\]

The internal anti-Hermitian connection cancels out of the real contraction. The closed `eta Qn` load annihilates the probe. For the product spin connection only spatial rotations occur, and their real contributions vanish on this current. Differentiating the ordinary bilinear therefore gives, **on this ansatz**,

\[
 E^a{}_{\mu}=\tfrac12\delta^a_0\delta^z_\mu\rho'(z),
 \qquad \rho'=4\sum_r m_ru_rv_r.                           \tag{1}
\]

This proves rank at most one, independently of choosing a common potential or independent spectral potentials. It is not just a small determinant at one numerical point. Wherever rho' is nonzero, the reconstructed metric is

\[
 g[E]=-(\rho'/2)^2\,dz^2,
\]

of rank one, not a nondegenerate four-dimensional Lorentz metric. At the reference point `(.4,.9,.4,.02)`, `E^0_z=.2279789642`; the other singular values are numerical zero. The previously prescribed product metric has rank four. It remains a background used to solve the comparison Dirac/gauge equations, **not the metric induced by their same probe**.

Internal unitary basis changes leave this full coframe invariant and cannot repair its rank. Simply evaluating the imaginary pairing instead gives rank two here, but it is a different coframe functional and is not adopted. Further internal field responses on the unchanged stationary polarization are not a geometric completion.

Equation (1) is a rank bound for this branch, not an exclusion of every native probe. More angular/spin/current structure is needed to leave this rank deficiency, but would not by itself settle the earlier [same-induced-frame trace obstruction](HC_Bilinear_Geometry_Bridge.md). That obstruction still applies if the same induced inverse frame, the same ordered real-bilinear probe equation and its other hypotheses are imposed. Rank is necessary, not the whole identification problem.

## 4. Which Fixed Bilinear Readouts Remain Internally Invariant?

Let `E_r=I2 tensor q_r` be the fixed resonance spectral projectors. Invariance of a fixed internal bilinear selector under the maximal spectral `U(2)^3` requires

\[
 R=\sum_r c_rE_r.                                         \tag{2}
\]

**Proof.** Independent central phases in each block kill off-diagonal blocks of R. Independent U(2) rotations then force each diagonal block to be scalar. Hermitian selectors have three real parameters. For only the common U(2) factor the fixed selectors instead have the form `I2 tensor R_channel`, giving nine Hermitian parameters. The calculation checks both dimensions.

Thus a **fixed bilinear** inter-mode selector is not invariant under the larger group. This statement concerns resonance eigenmodes, not physical generations or observer frames. It does not prohibit covariant readout references or nonlinear invariant combinations.

## 5. Intrinsic Pair and Loop Diagnostics

The already computed full matrix current transforms as `J^mu->U J^mu U^dagger`. The spectral projectors commute with the declared maximal gauge group. Consequently

\[
 C_{rs}^{\mu\nu}=\operatorname{Tr}(E_rJ^\mu E_sJ^\nu),
\]
\[
 L^{\mu\nu\lambda}
 =\operatorname{Tr}(E_1J^\mu E_2J^\nu E_3J^\lambda)          \tag{3}
\]

are internal-gauge invariant by cancellation and trace cyclicity. A simultaneous change of representation must also transport the spectral projectors. Hermitian currents give `(C_rs^{mu nu})*=C_rs^{nu mu}`; the real pair tensor is symmetric in its spacetime indices. Its fixed-time component is

\[
 C_{rs}^{00}=\|E_rJ^0E_s\|_{\rm HS}^2\geq0.
\]

These expressions do not require a new independent compensating field. They are nonetheless **new candidate readout functionals**, not the paper's original quadratic coframe. They scale quartically and sextically in the classical probe amplitudes, respectively; the native coframe scales quadratically. Normalization, dimensions, variation and interpretation cannot be imported unchanged.

In the fixed time chart of the sourced reference solution, the off-diagonal pair components are nonzero, for example `C_12^{00}=.0009370289` and `C_13^{00}=.0162020272`. The time-loop value is `.00012702575` with zero imaginary part within numerical precision. The existing real polarization therefore does not demonstrate a nontrivial cyclic phase. A separate **off-shell algebraic control** gives loop `(1-i)/4`, with phase `-pi/4`, and verifies that such a complex loop can be internally invariant. It is not an on-shell phase-selection result.

Internal invariance is not observer independence: C and L are spacetime tensors, and their `00`/`000` components are not Lorentz scalars. Contractions using the already assumed metric are possible diagnostics, not a derivation of that metric. Quantum operator versions additionally need ordering and expectation-value prescriptions: a product of classical mean currents is not automatically the expectation of a current product or a quantum-coherence/entanglement certificate.

The present solution has `J^theta=J^phi=0`. Every pair tensor in (3), and any combination with only internal scalar coefficients, therefore has zero angular rows and columns and rank at most two. These readouts do not supply a full-rank metric on this branch. Inserting an external metric or other independent spacetime tensors can change that rank, but is not an intrinsic current-only reconstruction. No general exclusion of curvature-based or derivative-based geometry is claimed.

## Outcome and Reproduction

The next [sourced Cauchy/coframe construction](HC_Sourced_Cauchy_Coframe.md) escapes this branch's rank-one defect using spatial spin/current structure in an explicitly different flat-reference common-U(1) comparison. Analytic self-sourced Cauchy data give full rank locally, but the real coframe is exactly `d(j/2)` and its induced metric is locally flat. The same-induced-frame Dirac/current obstruction remains; the Hopf flux sector is not continued by that construction.

The complete metric formula does not decide between the two gauge/readout contracts in this comparison. The fixed bare cross expression needs a stronger invariance condition, while intrinsic nonlinear matrix invariants offer another possible readout route. None repairs the full coframe's rank-one defect on the solved stationary branch. The next substantive requirements are an explicit native observable law, sufficient spatial/spin structure, and a consistent reference-versus-induced geometry/action relation, not merely another internal basis or scalar phase.

- [Calculation](HC_Gauge_Invariant_Geometry_Readouts.py) and [saved results](HC_Gauge_Invariant_Geometry_Readouts.json).
- Run `python -B analysis/HC_Gauge_Invariant_Geometry_Readouts.py --output analysis/HC_Gauge_Invariant_Geometry_Readouts.json`.
- Run `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_gauge_invariant_geometry_readouts.py`.

Twenty-seven checks cover the native formula distinction, full and cross-metric covariance, nondegenerate off-shell controls, rank/current identities, selector commutants, non-Abelian pair/loop invariance, spacetime tensor transformations, amplitude scaling and the missing angular directions. No main-TeX edit, PDF rebuild, package installation or release activation is introduced. This follow-up was made after the separately requested research commit/push.
