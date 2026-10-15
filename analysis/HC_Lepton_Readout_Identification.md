# HC-to-Lepton Readout Identification Test

Date: 2026-10-15. Scope: the full-source, unreleased v4.8.0-r01 research working copy. This is a mathematical identification test, not a recovered physical interaction or an external evaluation.

## Result

The existing definitions do not establish that the native HC is the three-root operator in the preceding conditional Koide construction. Two direct routes are excluded under explicit assumptions. A residual-state readout with an independently supplied generation coupling is compatible with the refined mass language, but that coupling and its generation states are not yet supplied by the paper.

The new main section `sources/research/parts/hc-mass-identification.tex` contains five propositions with proofs. It is included immediately after `koide-and-kernel.tex` and before the inherited physical core. All original full-source fragments are unchanged.

The subsequent [generation-coupling construction](Generation_Closure_Coupling.md) now supplies conditional seed and coupling formulas from the named closure projector and pacer. It distinguishes slot and eigenstate mass laws, identifies a cyclic harmonic spectrum and a possible small-root boundary, and tests the inherited overall phase. It still does not supply the native evaluated operator action or derive the Koide radius.

## Existing Objects Actually Found

| Existing object | Source location in the retained fragment | What it supplies, and what it does not |
| --- | --- | --- |
| `C=(I+J)/2`, `P_-=(I-J)/2` | `10_sphaera_and_physics.tex`, central decomposition and `sec:stringlqg` | A compensated/fixed part and an odd part; no three-generation mass-root map |
| Three generations in octonionic slots | Same fragment, `thm:three-generations` | A proposed generation dictionary; not an identification with the matter/tachyon/photon sector triple |
| Koide/Brannen law | Same fragment, `thm:koide-triolic` | The disputed ratio and phase claims; does not construct the native HC action on root coordinates |
| Undeveloped Yukawa mechanism | Same fragment, remark titled "Mass spectrum beyond Koide" | An explicit acknowledgment of a missing mass-spectrum mechanism |
| Residual localization as massive readout | `16_master_model.tex`, `subsec:mass-null-axis` | A qualitative distinction from the photon fix-sector; no evaluated lepton mass functional |
| Higgs mediation | Same fragment, `def:higgs-mediation` | A named interface for residual localization; no specified generation coupling |
| Effective field operator `Omega` | Same fragment, `thm:minimal-mmhc-field-equation` | A symbolic operator sum, not its numerical generation matrix elements or an assigned lepton spectrum |
| Spectral-to-mass realization `R_m` | `17_open_question_genealogy.tex`, `prop:spectral-to-mass-realization-map` | A named map and domain/codomain, without an executable functional rule or a proof of the Koide norm law |
| Common frame quadratic term | `10_sphaera_and_physics.tex`, `def:lagrangian` | `beta^2 <f,f>`; this alone does not distinguish equally normalized generation states |

The inherited unitary-equivalence argument calls `J` unitary, whereas the gauge-invariance proof calls it anti-unitary. Those conventions must not be silently interchanged. An anti-unitary involution can be treated as an orthogonal involution on the realified Hilbert space, but its average with the identity is not generally complex-linear. The new identification test explicitly works on a real Hilbert realization; it does not resolve every inherited complex-linearity claim.

## 1. What a Valid Linear Identification Would Require

Let `B:H -> R^3` be a bounded coisometry, `B B* = I`, on a real Hilbert realization of the carrier. If `ker(B)` is invariant under the orthogonal involution `J`, then

```text
J_m = B J B*,    J_m^2 = I,    J_m* = J_m,
B J = J_m B,    B C = C_m B,    C_m = (I+J_m)/2.
```

Conversely, intertwining implies invariance of `ker(B)`. The coisometry assumption is a sufficient way to retain the ordinary Euclidean root metric. An arbitrary similarity transformation can preserve the involution identity while destroying orthogonality; arbitrary compression can fail even to be an involution.

For a separately justified seed with `B f_0 = e = (1,1,1)/sqrt(3)`, one must still prove that physical principal roots are `x = alpha B C f_0`, with positivity and nonzero output. Only then is the prior criterion applicable:

```text
K = 2 / [3(1+h)],
h = <e,J_m e> = <B*e, J B*e>.
Koide requires h = 0.
```

Neither `B`, this seed/readout law, nor this native orthogonality condition is constructed by the inherited definitions. The route is sufficient, not a claim that all mass readouts must be linear. Nonnegative roots cannot be represented by a nonzero linear map on an entire vector space: the map must be restricted to admitted states or replaced by a nonlinear law.

## 2. Direct Routes That Fail

### Pure HC on an Odd Fermionic Input

For `J f = -f`, the defining formula gives `C f = 0`. Thus `B C f` vanishes, as does any readout of `C f` that sends zero to zero. This is incompatible with positive lepton masses on that input lane. It does not exclude using the residual state, coupled inputs or an alternative nonlinear realization.

A fixed seed gives the opposite trivial result: when `J f_0 = f_0` and `B f_0 = e`, the descended `J_m e = e`, so the projected root triple is constant and `K = 1/3`.

The quaternion-sector statement that the compensated output is orthogonal to both inputs cannot supply the root correlation condition in the same Hilbert metric: an orthogonal projector satisfies `<C f,f> = ||C f||^2`. A nonzero projected output is not orthogonal to its own input there.

### Symmetric Input With Equivariant Readout

For a cyclic generation action `U` and root-coordinate cycle `P`, suppose `F(U f) = P F(f)`. If `U f_0 = f_0`, then `P F(f_0) = F(f_0)`. Thus the roots are equal (or all zero). This holds even for nonlinear `F`. A common frame parameter cannot evade it while both input symmetry and equivariance remain intact.

The generation action `U` is not the same datum as the matter/tachyon involution `J`. An asymmetric input, symmetry-breaking selection or non-equivariant generation coupling must be exhibited; merely counting three sectors does not supply one.

### Norms of a Closed Triole

If `z_0+z_1+z_2 = 0` in a normed vector space and one proposes `m_i = kappa ||z_i||^2` with the same positive scale for all generations, set `r_i = ||z_i||`, `s = sum(r_i)`. The triangle inequality gives `r_i <= s/2`, hence

```text
1/3 <= sum(r_i^2)/s^2 <= 1/2.
```

This candidate cannot produce `K = 2/3`. The result concerns a positive norm and the stated common-scale mass law, not an indefinite quadratic form or every nonlinear generation map. Unequal couplings change the assumptions and must be derived separately.

### Fitting the HC Shape Is Not Identification

Every nonzero nonnegative target root vector can be reproduced by choosing `C_x = x x^T / ||x||^2`, `J_x = 2 C_x-I` and a positive scale. Thus existence of a freely selected HC-shaped operator is consistent with every mass triple, including ones violating Koide. The operator and readout must be fixed independently of the target masses for the criterion to predict anything.

## 3. A Concrete Residual-Coupling Target

The refined mass language motivates the following additional effective ansatz, with dimensionless admitted generation states, a dimensionless bounded coupling `D_beta:H_- -> V` on `H_- = ker(J+I)`, and a positive mass scale `kappa`:

```text
u_i = P_- psi_i,
m_i(beta) = kappa ||D_beta u_i||^2,
x_i = sqrt(kappa) ||D_beta u_i||.
```

This is a declared test interface, not a derived Yukawa theory. It has useful structural properties: nonnegative masses, zero mass on fully fixed inputs, potentially nonzero mass on odd inputs, and equality for `J`-dual inputs under the same coupling. Different dual-sector masses would require a frame-labelled change of coupling/readout.

For `q_i = ||D_beta u_i||^2`, Koide still independently requires `sum(q_i) = (2/3) [sum(sqrt(q_i))]^2`. Positivity and the HC decomposition do not imply this equation.

For equally normalized residual states, the isotropic choice `D_beta* D_beta = beta^2 I` gives equal masses `kappa beta^2`, hence `K = 1/3` at nonzero `beta`. At zero all masses vanish and the ratio is undefined. More generally, a common positive scale changes no mass ratios. The already written isotropic frame term is therefore insufficient by itself for this readout.

Conversely, an unrestricted diagonal coupling can fit any chosen masses on an orthonormal generation basis. Its availability is not a prediction. The next model-specific task is to determine both the admitted generation states and the coupling (or an explicit alternative readout) from independently specified carrier/field data, then test the Koide condition, phase and scale. The inherited historical-OP3-closed and P2-confirmed wording cannot serve as that construction.

## Verification Scope

`scripts/qsc_audit/tests/test_hc_mass_identification.py` contains 18 checks: exact rational operator examples, loss of orthogonality under arbitrary similarity, failed descent with non-invariant kernel, real versus complex linearity, the odd/fixed input obstructions, cyclic equivariance, the triangle bound and its scope, fitting freedom, and positive/dual-invariant/isotropic residual examples. It constructs no native physical coupling. One additional route regression keeps this section visible before the inherited claims.

Overall build measurements and test totals are recorded in `analysis/V480_Full_Monolith_Integration.md` and `analysis/V480_Full_Monolith_Metrics.json`. The quotient/local-kernel proof scope in `analysis/Koide_Zero_Kernel_Proof_Audit.md` is unchanged; no global kernel activation is inferred from the HC-to-mass analysis.
