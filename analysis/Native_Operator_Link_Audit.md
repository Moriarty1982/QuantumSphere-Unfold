# Native Projector, Clock and Generation Link

Date: 2026-10-15. Scope: the unreleased full-source research working copy. The original operator names have been traced, but native numerical matrix elements and a physical lepton spectrum have not been recovered.

## Source Findings

| Required input | Original source in `sources/research/parts/v470/` | Actual information |
| --- | --- | --- |
| Generation embedding `T` | `10_sphaera_and_physics.tex:1077`, `thm:three-generations` | Proposed octonionic slot dictionary; no common metric, normalized seed mode or joint closure/clock action |
| Closure projector `P` | Same fragment, lines 2062-2071 and 2140-2155 | Trace condition modulo HC and idempotence; not the evaluated generation projector or an orthogonality proof |
| Pacer `R_beta` | Same fragment, `thm:dirac-probe`, line 2077 | `exp(i*pi*beta) R_GUE`; no evaluated eigenvectors relative to `P,T` |
| First-order mass operator `Omega` | Same fragment, `thm:master-field-equation`, lines 2174-2196 | Symbolic sum with direct, projected Millennium, triadic and compensator terms; no generation matrix or gap |
| Paired triadic channels | Same fragment, `prop:triadic-two-probe`, lines 2260-2295 | Operator-valued couplings; no identification of probe-channel indices with generations, adjoint relations, units or ranks |
| Defect penalty and exact closure | Same fragment, lines 2353-2449, including `prop:equivalent-closure-criteria` | Explicit quadratic penalty and `[M16,P]=0`; no equation identifying the clock with `M16` |
| Refined physical field operator | `16_master_model.tex`, `thm:minimal-mmhc-field-equation` | Retains the symbolic direct/projected/triadic/compensator split |
| Spectral-to-mass realization | `17_open_question_genealogy.tex`, `prop:spectral-to-mass-realization-map` | Declares a structural interface without evaluating this mass law |
| HS carrier coding | `32_atlas_and_op_promotion.tex`, HS(4) meta-septum and HS(6) Dixon-coding layer | Connects carrier sizes and coordinate encodings, not the missing joint operator matrix elements |

The new main section `sources/research/parts/native-operator-link.tex` follows the generation-coupling section and contains seven propositions with proofs. It keeps the previous bounded/finite, positive-metric, orthogonal-projector assumptions. All inherited fragments remain unchanged. The distinctions between the HC projector `C`, Meta-Septum projector `P` and minimal penalty `H_C` are retained.

## 1. A Native Algebraic Link That Can Be Evaluated

For an orthogonal `P`, decompose a bounded matrix as `M = [[A,F],[G,D]]`. Its closure commutator and symmetric residue are

```text
K = [M,P] = [[0,-F],[G,0]],
E = (I-P)MP + PM(I-P) = [[0,F],[G,0]].
K* K = E* E = diag(G*G,F*F).
```

Consequently the two terms of the inherited minimal penalty coincide in this realization:

```text
H = rho K* K + sigma E* E = (rho+sigma) K* K,
[H,P] = 0,
S* H S = (rho+sigma) r_ref^2 Q_M,
Q_M = [(I-P) M S/r_ref]* [(I-P) M S/r_ref].
```

Self-adjointness of `M` is unnecessary. Orthogonality of `P` in the adjoint metric is essential; idempotence alone does not suffice. The coefficients need compatible units. The identity does not identify the native clock with `M`. If one separately supplies `R_beta = exp(i phi) M`, its Gram matrix is `Q_M`; this is an extra bridge, not a recovered source equation.

The penalty is block-diagonal even when the defect is nonzero. Using that penalty itself as the off-sector pacer therefore produces zero transition. A deeper independently postulated compensator generator is outside this statement.

## 2. Exact Closure Can Eliminate the Proposed Route

If `[M,P]=0`, then `P` also commutes with `M*`, every star polynomial in `M`, and its norm limits. A clock from that unital operator algebra has no off-sector block, so `Q=0`. In particular, a bounded normal functional-calculus clock of the exactly closed Millennium matrix cannot generate masses through this defect readout.

Conversely, exact closure of `M` alone says nothing about an independent clock. The explicit witness `M=I`, `P=diag(I,0)`, `R=[[0,I],[I,0]]` has exact Millennium closure and `Q=I`. Internal masses in `P Omega P` are not excluded by either result.

## 3. Why the Riemann Spectrum and a Common Frame Shift Are Insufficient

For a fixed projector and seeds, rotate a diagonal self-adjoint clock between each selected/complementary coordinate pair. Its full spectrum stays fixed, even when simple and positive, but

```text
Q_theta = diag((d_i^+ - d_i^-)^2 sin(2 theta_i)^2)/(4 r_ref^2).
```

The transition eigenvalues and their ratios change. Thus knowledge of clock eigenvalues alone, even beyond spacing statistics, does not determine the required cross matrix elements. This finite witness is not a proposed native zero-sequence clock; it isolates the missing relative eigenspace orientation.

Likewise, simultaneous unitary transport of `P,R,T`, a common phase and a scalar normalization yield only

```text
Q_f = s^2 V* Q_0 V.
```

They preserve spectral mass ratios. The proof includes projected-seed normalization, not only a change of a preselected basis. It is not a statement that physical Lorentz boosts act unitarily in this positive carrier metric. A scalar Planck-readout calibration does not supply a generation-splitting law. Relative channel or frame motion needs an independently specified operator relation.

## 4. Probe Channels Are Not Generation Indices

`rank(B*B)=rank(B)`. Three positive masses in this candidate require three independent output amplitudes. A single scalar complementary channel has rank at most one and leaves two zero candidate eigenmasses. A single operator-valued channel can have a larger output space; the source's symbol `Psi_perp` is not a proof of a one-dimensional native complement. The three probe blocks must not be relabelled as three generations without an embedding.

## 5. A Conditional Origin of the Quadratic Mass Law

Freeze the background and supply a Hermitian mass-dimension truncation with canonical kinetic normalization, in units `hbar=c=1`:

```text
Omega_tr = [[A,V*],[V,H_perp]],
H_perp >= Delta I > 0.
```

Other closed modes must either be absent from this invariant truncation or consistently included/eliminated. The paired triadic operators need adjoint relations and compatible units. These are not established by the original symbolic block equation.

Eliminating the complementary coordinate of a light eigenstate gives the exact Schur equation

```text
[A - V* (H_perp-lambda I)^(-1) V] x = lambda x,
y = -(H_perp-lambda I)^(-1) V x.
```

For `|lambda| < Delta`, the zero-energy approximation has the operator-norm error bound `||V||^2 |lambda|/[Delta(Delta-|lambda|)]`. A flat positive gap `H_perp=Delta I`, vanishing direct block `A=0`, and separately established coupling `V=mu B` give exact light signed eigenvalues `-m_i`, with

```text
m_i = (sqrt(Delta^2+4 mu^2 q_i)-Delta)/2,
m_i = (mu^2/Delta) q_i + O(mu^4 q_i^2/Delta^3).
```

This justifies a leading positive mass-magnitude law `kappa Q` under the additional canonical Dirac-type interpretation, with `kappa=mu^2/Delta`. The signed effective operator is negative. A non-flat gap gives a weighted Gram matrix, and a direct block changes the result. Finite-gap corrections do not preserve Koide automatically. No native gap, coupling scale or physical interaction has been derived here.

For a normalized exact light eigenstate, the complementary weight is `m_i/(Delta+2m_i)`. It is nonzero for positive `m_i`. Strict original closure `P psi=psi` instead forces `V x=0`; with `A=0` it cannot produce those positive masses. A dressed light spectral projector can be invariant, but it differs from `P`. Approximate closure, exact Millennium closure, and exact invariance under the full field operator are different claims.

## Concrete Remaining Input

The next native calculation is `(I-P) R_beta S` and its relation, if any, to `(I-P) Omega S`, with represented domains, metric, units, grading, generation action and sufficient rank. A physical choice between strict `P` closure, a controlled approximate sector, a dressed projector or a different internal mass readout must be explicit. The existing text does not yet choose or evaluate these data. The Koide radius, relative phase selection and absolute scale remain unproved.

The subsequent [coupling/scale determination attempt](Coupling_Scale_Determination.md) evaluates a normalized three-channel candidate using the inherited phase/radius hypotheses. It separates the explicit matrix from a native identification and proves that no positive flat-gap scale choice repairs this candidate's middle/largest mass ratio. The physical scales remain undetermined; the numerical examples distinguish external references, illustrative choices and one-mass calibrations.

## Verification

The generation-coupling regression file now has 49 finite numerical tests, including 18 new checks for the penalty identity and its metric scope, closure-transfer counterexamples, fixed simple clock spectra, normalized frame covariance, rank, exact Schur reduction and its error bound, flat/non-flat gap masses, complementary weights, finite-gap Koide drift and dressed versus original projectors. One new integration regression keeps this section and its qualifications before the inherited claims. These examples supplement the written algebra; they do not recover native operators or certify a physical theory.
