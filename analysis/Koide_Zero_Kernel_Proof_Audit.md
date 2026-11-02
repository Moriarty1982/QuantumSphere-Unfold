# Koide and Local Zero-Kernel Proof Audit

Date: 2026-10-15. Scope: the unreleased full-source v4.8.0-r01 working copy, not a new release or an external institutional evaluation.

## What Was Actually Added

The main entry `sources/research/v480-companion.tex` now includes `parts/koide-and-kernel.tex` before the inherited physical core. The new section contains eight propositions with explicit proofs, counterexamples and a positive finite kernel instance. The original full v4.7 fragments remain unchanged and auditable. Their preservation does not certify their claims; the new qualifications govern the identified inherited Koide argument.

Neither the proposed `activateZeroKernel` display macro nor a replacement of the first Koide derivation by a `GRCite` token was adopted. Printing an implication is not an activation, and a reference token is not a proof.

The subsequent [HC-to-lepton identification audit](HC_Lepton_Readout_Identification.md) now tests the conditional HC construction against the retained native definitions. Its five additional propositions rule out specified direct routes and give a precise descent interface; they do not construct the missing physical generation coupling. The local/global kernel distinction below is unchanged.

## Koide: The Missing Condition Is Now Exact

For nonnegative principal mass roots `x_i = sqrt(m_i)`, let `A = sum(x_i)/3 > 0`, `u = A(1,1,1)` and `d = x-u`. Orthogonality gives

```text
K = sum(x_i^2)/sum(x_i)^2 = 1/3 + ||d||^2/(9 A^2).
K = 2/3  iff  ||d||^2 = ||u||^2 = 3 A^2.
```

Cyclic symmetry preserves these components but does not set their norm ratio. Cauchy--Schwarz only yields the lower bound `K >= 1/3`. The cyclic orbit of `(1,2,3)` has `K = 7/18`; equal positive roots give `K = 1/3`. These are explicit counterexamples to the inherited sufficiency claim, not counterexamples to Koide as a separate empirical relation.

### A Conditional HC Route

In a declared real three-root representation, take `e = (1,1,1)/sqrt(3)`, an orthogonal involution `J_m`, and `C_m = (I+J_m)/2`. If `x = alpha C_m e` is nonzero and componentwise nonnegative, `alpha > 0`, then

```text
h = <e, J_m e>,    K = 2 / [3(1+h)].
Koide holds iff h = 0.
```

The proof uses `||C_m e||^2 = <e,C_m e> = (1+h)/2`. A realizable sufficient construction exchanges `e` and `v = (2,-1,-1)/sqrt(6)` and fixes their orthogonal complement. It gives `C_m e = (e+v)/2`, with equal symmetric and asymmetric norms. In contrast, `J_m = I` is an admissible orthogonal involution with `K = 1/3`.

This is not yet the paper's native HC derivation. One must independently construct the native representation on mass roots, establish positivity and prove `h = 0`. Choosing the representation to fit Koide would simply insert the missing condition. The direction in the zero-sum plane, hence the phase, is still free. A cyclic-equivariant linear operator cannot generate a nondegenerate hierarchy from a symmetric input; an asymmetric input, symmetry-breaking selection or non-equivariant coupling must be identified.

### Radius, Phase and a Limiting-Case Error

Every admitted root triple has `x_k = A[1+r cos(theta+2 pi k/3)]`, with `r >= 0` and nonnegative brackets. Then `K = 1/3+r^2/6`; Koide fixes `r = sqrt(2)`, not the phase or scale.

At `beta = 0`, the inherited ansatz `theta = pi-sqrt(2) asin(beta)` at fixed Koide radius gives mass ratios `(3-2 sqrt(2), 3/2+sqrt(2), 3/2+sqrt(2))`, not complete mass degeneracy. Its first signed-root bracket is negative. Taking squared masses then requires absolute values for principal roots and invalidates the signed-root denominator identity. Equal nonzero masses instead require `r = 0` and have `K = 1/3`.

### Fixed Historical-Input Diagnostic

These are calculations using only values already quoted in the paper, not updated experimental inputs or a new fit:

| Quantity | Value |
| --- | ---: |
| Mass inputs in MeV | 0.51100, 105.658, 1776.86 |
| Root mean `A` | 17.7155558664 |
| `K` | 0.666660818717 |
| Root-plane phase, ordered as quoted | 132.7327925517 degrees |
| Phase ansatz at `beta = 0.5493` | 132.8798136631 degrees |
| Predicted masses at that fixed `A`, in MeV | 0.4455944783, 106.9229844721, 1775.6769389820 |
| Relative mass errors | -12.7995%, +1.19724%, -0.0665816% |

A small phase discrepancy is not a uniformly small mass error. The electron readout is particularly sensitive here. The inherited `thm:koide-triolic` and dependent phase-prediction wording are not established physical derivations by these calculations.

## Kernel: Constructive Local Results

Fix a supplied nonempty set-sized fragment `A_F` and a supplied closure equivalence `E_F`. The relation's native meaning is an input obligation, not inferred from state tags.

- Tagged payload extraction `p_t(<t,a>) = a` is total on the declared tagged surface and reconstructs its raw syntax.
- The semantic quotient `q_F(a) = [a]` exists in ZF without selecting representatives, and reflects exactly the supplied equivalence.
- Every total class-constant closure-relevant readout factors uniquely through that quotient.
- On a finite fragment with injective integer codes, the least-coded class member gives a total idempotent normal form `N_F`, reflecting exactly `E_F`.
- A partial readout `f:D -> Y` factors on observed classes precisely when it is constant on the normal-form fibres inside `D`. Equality of partial functions additionally requires `D = N_F^-1(N_F(D))`: the domain must be a union of fibres.
- A supplied state aggregator descends when it respects componentwise equivalence. Congruence plus preservation of the class on diagonal inputs suffices to preserve a common input class. Weight normalization alone proves neither property.
- The declared payload-preserving tag shift commutes with payload extraction and quotient/normal-form comparisons. This proves an encoding compatibility, not arbitrary physical frame invariance.

Class compression does not reconstruct every original payload. A quotient class is not automatically a native kernel payload, and finite representative selection does not supply a canonical representative on an arbitrary proper class.

### Counterexamples to Weaker Claims

1. For `p(<0,a>) = a`, every candidate `N` satisfies the reviewer's displayed identity `N(p(<0,a>)) = N(a)`. On two distinct closure classes a constant `N` still satisfies it but loses the compatible identity readout. The macro's statement is therefore insufficient.
2. A readout defined at only one of two equivalent states is compatible where defined, yet composition with its quotient factor also becomes defined at the other state. Pairwise value agreement does not establish equality of partial readouts.
3. With classes `{0,1}` and `{2,3}` and normalized weights `(1/2,1/2)`, the constant aggregator `G(a,b) = 2` is congruent but sends inputs `0,1` to the wrong class.

### Positive Finite Instance

Use `A_F = {0,1,2,3}` and classes `{0,1}`, `{2,3}`. Then `N_F = (0,0,2,2)`. The readout `(7,7,11,11)` factors through `{0,2}`. With `c(a) = floor(a/2)`, declare the aspect tuple `("state", c(a), ("class", c(a)))`, constant on each class. Let transport swap `0,1` and `2,3`, and let `G(a,b) = a`. All stated local gates hold, including the payload-preserving tag shift. This is a consistent supplied local model, not a recovered native QAM witness or a symmetric physical averaging law.

## Original Activation Package: Current Status

| Obligation | What is established here | What remains native/model-specific |
| --- | --- | --- |
| Payload extraction | Explicit total tagged projection and syntactic reconstruction on the declared fragment | Identification of the admitted native domain |
| Native kernel admissibility | A consistent finite carrier with chosen invariant aspects can be supplied | Membership, required type/class/signature preservation and recursive-filter compatibility for the paper's actual objects |
| Closure reflection | Set quotient and finite least-code normal forms reflect the supplied `E_F` exactly | Native closure equivalence and its interpretation; a suitable normal form beyond the local fragment |
| Readout factorization | Total class-constant post-class-map values factor; exact partial factorization has the additional domain-saturation criterion | All actual required readouts, their post-class maps, domains and aspect invariance |
| Routed descent | Congruence plus the diagonal class property is a proved sufficient condition; a finite positive table exists | The actual admitted native state aggregator and these properties for all intended routes |

The later shifted normal form is retained. The full global activation package is still unproved. No external `WARN_022`/`WARN_081` clearance, MEALS outcome or institutional certification is claimed.

## Reproducible Checks

`scripts/qsc_audit/kernel_fragment_audit.py` validates a supplied finite equivalence without silently completing it. It constructs least-code normal forms and checks readout fibres, partial domains, transport edges and complete aggregation tables. The table audit is exhaustive and exponential, not a new efficient solver. Readout values are already post-class-map values; the checker does not infer those maps or the native equivalence.

`scripts/qsc_audit/tests/test_koide_and_kernel.py` has 35 tests covering the algebraic identities, HC-shaped projection formula, counterexamples, fixed paper inputs, finite construction and positive instance. These regression tests supplement the written proofs; they are not a formal proof-assistant certificate. The full audit suite also checks that the proof section is visibly included before the inherited claims and that all original fragments/labels survive. Build/page measurements and overall test totals are recorded in `analysis/V480_Full_Monolith_Integration.md` and `analysis/V480_Full_Monolith_Metrics.json`.
