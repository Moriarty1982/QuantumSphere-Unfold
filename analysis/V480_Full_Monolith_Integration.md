# Full-Monolith Reading Route and v4.8.0 Integration

Date: 2026-10-15. Status: unreleased v4.8.0-r01 research working copy; no new version DOI and no public upload.

## Correct Baseline

The origin is the complete `release/v4.7.0/Quantum_Sphaera_Companion_v4_7_0_source (2).tex`, not the older modular `sources/active-core.tex`. The corresponding published PDF has 1,014 pages. A separate, unchanged-source rebuild also produces exactly 1,014 pages after the contents, references and long tables settle.

The new entry is `sources/research/v480-companion.tex`. The published TeX/PDF, prior releases, older modular pilot and separate Historical Witness remain distinct artifacts. No numerical difference between those unrelated version scopes is treated as a missing portion of the full paper.

## Full Length Comparison

| Portion | Full v4.7 baseline | v4.8 working route | Change |
| --- | ---: | ---: | ---: |
| Main text, title/frontmatter and contents | 523 pages | 135 pages | -388 (-74.19%) |
| Complete support, appendices and bibliography | 491 pages | 884 pages | +393 |
| Entire document | 1,014 pages | 1,019 pages | +5 (+0.49%) |

The baseline split is before `app:mm-tools` on page 524. The working split is before `v480:appendix-start` on page 136. Both totals include the whole respective document, not only the conceptual reading route. The earlier 655-to-656 comparison is a different modular scope and is not reused here.

The earlier editorial milestone had 1,008 pages (124 main/frontmatter plus 884 support/bibliography). Its net six-page saving was principally a navigation change: the printed contents shows section-level entries instead of the full subsection hierarchy. The Koide/local-kernel proof section added four net pages, giving 1,012. The HC-to-lepton identification test added three, giving 1,015; the subsequent generation/closure-coupling construction adds four more, giving 1,019. All subsection records and inherited body text remain. This is not a claim that the inherited mathematical prose itself was shortened; new qualifications and proofs now outweigh the navigation saving by five pages. Paper size, font sizes and page margins remain those of the full v4.7 baseline.

## Complete Coverage, Not a Short Substitute

`sources/research/v480-source-map.json` partitions the origin into 38 disjoint fragments and records their byte offsets, first source lines and SHA-256 values. All 3,403,614 original bytes are retained. Concatenating the fragments in origin order reproduces the frozen source byte for byte. The reading order includes every fragment exactly once, including the later shift, OP selector/atlas work, C4/C5 development, post-r54 solve-chain summary and frame-typed endpoint through r84.

The captured local source has Windows CRLF line endings. The map additionally records canonical LF offsets and hashes for Git/Linux checkouts (3,340,412 canonical bytes). The portable audit permits only this explicit line-ending conversion; all mathematical and prose content must still match. A regression test simulates an LF checkout. The local measurement confirms a byte-identical reconstruction without normalization as well.

All 3,290 original label occurrences survive, with no newly duplicated labels. The new reader/premise/integration modules are separate from the inherited fragments. The later macro-defining chains preserve their mutual order, and the bibliography follows the complete retained development.

Preserving text is not certifying its mathematics. Some inherited claims are overstrong or unresolved. Their source remains auditable; the main premise audit states known limitations rather than treating a successful build or a stored assertion as a proof.

## What Is Integrated Now

| Component | Present working integration | Remaining condition |
| --- | --- | --- |
| Full v4.7 source | Complete mapped baseline, main/support split and current scope summary | Not a scientific validation of every inherited argument |
| QAM/MML/MMA | Complete infrastructure retained; later shifted normal form/backtranslation governs new objects | No rollback to the older pre-v4 pilot; coding/typing remains proof-neutral |
| MM/HC premises | Visible conditional eigenprojection criterion and counterexamples | Native operator, domains, scalar support and complement exclusion must be supplied; dependent inherited uses need audit |
| Koide | Proved equal-norm criterion, radius/phase decomposition and conditional HC-shaped projection formula; counterexamples to cyclic sufficiency and the fixed-radius degeneracy claim | Native mass-root representation, positivity, HC orthogonality condition and phase/scale law are not derived |
| HC-to-lepton identification | Proved norm-controlled descent and direct-route obstructions; sector/generation triples distinguished; residual-coupling ansatz has explicit positivity, dual and isotropic-limit tests | No native root map or evaluated generation coupling is supplied; the physical interaction and its Koide law remain unestablished |
| Generation/closure coupling | Conditional closed odd seeds and a positive transition Gram matrix; slot/eigenmass distinction; cyclic harmonic spectrum, positivity chambers and small-root law; global/relative phase tests | Native common-carrier projector/pacer/seed action, physical mass law, radius/phase selection and absolute scale remain unestablished; no parameter-free spectrum |
| Zero-kernel | Choice-free set quotient, finite least-code normal forms, precise partial-readout factorization and routed descent criterion; explicit positive finite model | Native admissibility/aspects/recursive filters, all actual readouts/aggregators and full-surface normal forms remain open; no global activation |
| OP1 exponent | Inverse-identity warning and proved uniqueness for the independently fixed exponent-five ansatz | Exponent, prefactor and lattice origin are not derived |
| OP5/C5 | Full-sum/regularization obligations separated from detector evidence and the fit dictionary | Native boundary/exterior/mixed residual functions, fixed norms and evaluated guards are still needed |
| Planck readout | Typed candidate scale `ell_eff(R) = ell_P * lambda_R`, units and orientation/signature separation | No automatic identification between a dimensionless detector threshold and a length scale |
| Metric/field equations | A positive conformal metric is labelled as an additional ansatz; zero-factor degeneracy and the separate null construction are explicit | Actual readout-to-geometry map, dynamics, conservation and approximation/stability proofs remain open |

The working title and PDF metadata identify v4.8.0-r01 as unreleased. The inherited `docversion` remains 4.7.0 so old release statements are not relabelled as new v4.8 results. The v4.7 version DOI is provenance only; no v4.8 DOI is invented.

The new main section `parts/koide-and-kernel.tex` contains eight propositions with proofs, beginning on page 12 and ending with the activation boundary and positive instance on page 16. See [the proof audit](Koide_Zero_Kernel_Proof_Audit.md) for the exact results, counterexamples, fixed historical-input diagnostic and the five native activation obligations. No reviewer-supplied warning or predicted institutional score is declared resolved.

The following `parts/hc-mass-identification.tex` spans pages 16--19 and contains five further proved propositions. It shows why pure compensation of an odd input, symmetric readout of a fixed input and a common-norm closed-triole mass law do not establish the claimed hierarchy. It states the actual linear descent conditions and a separately labelled residual-coupling ansatz. The [identification audit](HC_Lepton_Readout_Identification.md) maps these results to the inherited definitions and isolates the missing generation states/coupling. Historical OP3-closed/P2-confirmed wording does not discharge that obligation.

The subsequent `parts/generation-coupling.tex` spans pages 19--23 and contains eight further propositions. It constructs `S = P T (T* P T)^(-1/2)` and `D_beta = (I-P) R_tilde_beta P` under explicitly stated realization assumptions. It derives a cyclic Brannen-type eigenvalue spectrum and a phase-boundary mechanism for one quadratically small candidate mass, but not the native radius/phase or physical mass law. The written overall pacer phase cancels from this norm readout and the absolute commutator expectation. The [generation-coupling audit](Generation_Closure_Coupling.md) also records the zero expectation on exactly closed inputs, the slot/eigenbasis distinction, the OP2 grading qualification and the unitary-dilation underdetermination example.

## Path to a Release

1. **Source gate:** keep the full-source identity check and current shifted normal form; do not merge the older v3.35-based tree over the later full monolith.
2. **Correction gate:** replace known incorrect theorem formulations deliberately and audit all dependent uses. The new premise section qualifies them but is not a completed correction of every inherited proof.
3. **Scale gate:** declare readout, reference length, units, calibration and sign/orientation data. Distinguish the new dimensionless scale coefficient from the native dimensionful tachyon-scale symbol.
4. **Operator/residual gate:** supply actual domains, represented MM/HC operators and the native C5 residual dictionary. The OP5 working note and relay helper can contribute conditional criteria/regression examples, not substitute synthetic vectors for native data.
5. **Dynamical gate:** construct the proposed evolution/action and prove the claimed conservation, limiting and stability properties. Fluid or gravitational interpretations are not derived dynamics until that map exists. A null trajectory is not a zero metric tensor.
6. **Release gate:** reconcile the resulting statements with the effective/local/global ledger, audit the complete source and render, then make a deliberate version/DOI/publication decision. No upload workflow was activated.

The existing manual QSC LaTeX workflow can target `sources/research` with historical building disabled. The current default modular entry points and frozen release remain unchanged; promoting this working entry to a release/default build is a separate reviewed step.

## Verification and Artifacts

- `scripts/qsc_audit/full_monolith_reading.py check` verifies exact origin coverage, unchanged inherited fragments, unique inclusion and label preservation. The `measure` command rejects stale or unsettled page data and a baseline that fails to reproduce 1,014 pages.
- The complete audit suite has 181 passing tests, including 35 Koide/local-kernel checks, 18 HC/mass identification checks, 31 numerical generation/closure-coupling checks and three proof-section integration regressions; the separate OP5 relay suite has 34 passing tests (215 total). The generation-coupling examples use the already installed NumPy routines; no package was installed for this work. These are structural, algebraic and finite-model checks, not proofs of native physical closure or a formal proof-assistant certificate.
- Machine-readable measurements are in `analysis/V480_Full_Monolith_Metrics.json`. Baseline/research build files are under `build/full-v470-baseline/` and `build/v480-reading-audit/`.
- The local preview is `build/v480-reading-audit/v480-companion.pdf`. The final layout run has no unresolved references, undefined citations, duplicate destinations or outstanding rerun request. Both the baseline and the working route report 58 overfull boxes. Both also retain one inherited, tolerated `Infinite glue shrinkage` split-box diagnostic. This is not a warning-free typesetting claim or a visual audit of all 1,019 pages.
- Newly authored frontmatter, premise/integration pages and representative main/support/late-v4 transitions were rendered for visual checks. The Koide/local-kernel section was inspected on pages 12--16; the HC/mass identification section and its transition on pages 16--20; and the new generation-coupling section/transition on pages 19--24. The updated orientation on page 2 was inspected again. Sample images are under `build/v480-reading-audit/visual-check/`; these build artifacts are intentionally not committed as source.

Frozen source SHA-256: `0b74890e4f5d8ebbfd4820a4ff7bb44a621c61655720a9021e3c42d6d115e803`.

Canonical LF source SHA-256: `019e7a35adb3e299b1eed7e5310397d922d18575fe8a5122c3b448cf1a383329`.
