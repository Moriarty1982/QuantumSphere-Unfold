# Full-Source v4.8.0-r01 Research Working Copy

Entry point: `v480-companion.tex`. This is the full-monolith-derived working line, not the older `sources/active-core.tex` modular synchronization baseline. It is unreleased and has no assigned v4.8 DOI.

## Origin and Preservation

- Origin: `release/v4.7.0/Quantum_Sphaera_Companion_v4_7_0_source (2).tex`.
- Published baseline PDF: 1,014 pages; the local rebuilt baseline must match before a page comparison is accepted.
- All 3,403,614 original source bytes are partitioned into 38 fragments in `parts/v470/`. Every fragment is included once. Reassembling them in manifest order recovers the original byte for byte.
- `v480-source-map.json` records origin hash, byte offsets, first source lines and fragment hashes. Do not regenerate it over existing work or silently edit inherited fragments.
- Captured CRLF byte offsets/hashes and canonical LF offsets/hashes are both recorded. The local reconstruction is byte-identical; portable checks permit only Git's CRLF/LF checkout conversion, not changes to prose, formulas or guards.
- The main entry and `parts/support-route.tex` define the reading order. The later macro-defining v4 chains keep their mutual order. The bibliography is placed after the complete retained development.
- New prose, premise qualifications and research integration are outside the preserved fragments. `docversion` stays 4.7.0 for inherited records; working metadata separately identifies 4.8.0-r01.

## What This Candidate Does

The main line keeps the core construction, operator/closure hypotheses, master model and physical readouts, with an early qualification of known MM/HC, inverse-exponent and OP5 issues. It adds a compact current-v4 synthesis and a proposed Planck-readout/MM-HC integration interface. Supporting infrastructure, all later v4 material and provenance remain compiled in the appendices.

The new main section `parts/koide-and-kernel.tex` proves the additional equal-norm condition for Koide, gives a conditional HC-shaped realization, and constructs a quotient/finite local kernel with precise readout and aggregation conditions. This does not derive the native mass-root representation or activate the global native kernel. See [the proof audit](../../analysis/Koide_Zero_Kernel_Proof_Audit.md) for the proofs' scope, counterexamples and remaining activation obligations.

The following section `parts/hc-mass-identification.tex` tests that HC-to-mass identification against the actual inherited definitions. It proves a norm-controlled descent criterion and obstructions to the pure odd-input HC route and the common-norm closed-triole mass law. A residual-coupling readout is explicitly an additional ansatz, not a recovered interaction. See [the identification audit](../../analysis/HC_Lepton_Readout_Identification.md) for the source map, proved limitations and next generation-resolved coupling obligation.

The subsequent `parts/generation-coupling.tex` constructs conditional closed odd generation states and a closure-defect coupling from the named pacer/projector. It separates fixed-slot norms from candidate mass eigenvalues, derives a cyclic Brannen-type spectrum and a small-root phase boundary, and proves that the inherited overall phase alone cancels. Native matrix elements, the physical mass law and the Koide radius remain unestablished. See [the generation-coupling audit](../../analysis/Generation_Closure_Coupling.md).

The following `parts/native-operator-link.tex` tests the original projector, clock and triadic field definitions. It derives an exact Gram compression of the minimal defect penalty, proves the conditional closure-transfer obstruction and isospectral/frame underdetermination, and gives a gapped-block mass-magnitude law with an explicit exact-closure limitation. These are conditional operator results, not evaluated native matrix elements. See [the native-link audit](../../analysis/Native_Operator_Link_Audit.md).

The subsequent `parts/coupling-scale-candidate.tex` evaluates a normalized cyclic matrix from the inherited, still unproved radius and phase hypotheses. It proves a two-harmonic Koide obstruction and shows why no positive flat-gap scale choice repairs this candidate's muon/tau ratio. Planck/electroweak reference choices and one-mass calibrations remain explicitly separate from native predictions. Reproduce the numerical report with `python -B analysis/Coupling_Scale_Candidate.py`; see [the scale determination audit](../../analysis/Coupling_Scale_Determination.md).

The same section now diagnoses the discrepancy through root-phase/radius inversion and analytic sensitivity, without replacing the candidate by a fitted phase. An independent SI check confirms the Planck reference conversion. Non-flat-gap fits and a direct-mass-block bound distinguish the rejected flat-Planck-gap induced-mass test from a general exclusion of Planck-order sectors; all fitted quantities remain labelled as such.

The following `parts/tensor-shift-coupling.tex` makes the earlier identity-metric assumption explicit and extends the test to declared positive comparison/kinetic tensors. Five propositions establish the generalized spectrum, covariance even under nonunitary charts, comparison-metric fit freedom, absolute metric scale bounds and identity-tensor-extension invariance. The current QAM tag migration is retained, not interpreted as a numerical phase or mass shift. An added physical comparison can change ratios; its benchmark-fitted weights are not extracted from the source. The same numerical report includes the tensor audit, with 18 additional finite regression checks and a source-integration guard.

The subsequent [physical-origin diagnosis](../../analysis/Coupling_Physical_Origin_Diagnosis.md) is deliberately a separate analysis note, not an additional main-text section. It distinguishes inverse-gap susceptibility, tiny Planck-induced norm dressing, coherent triadic phases and ordinary QED matching, with 20 further finite tests. None of these tests supplies the missing native coefficients or determines a physical cause from the mass benchmark alone.

The next [triadic-propagator analysis](../../analysis/Triadic_Propagator_Identification.md), also outside the main TeX, connects the OP5 note's prepared relay to the newer generation-coupling candidate. It supplies the propagator reduction, mandatory diagonal/norm corrections, invariant cycle phase, scalar fixed-exchange restriction and an explicit internal-generation tensor witness preserving that exchange. Thirty-four further tests also check ordered background/pole derivatives and a conditional connection/holonomy route. The interaction coefficients, native generation embedding and transport paths remain unspecified input; preserving the declared exchange does not establish strict visible/C7 closure.

The following [phase-selection derivation](../../analysis/Phase_Selection_Derivation.md) remains a separate analysis note. Its explicit minimal-native substitution now shows that the HC matching penalty vanishes for every admissible phase on `H_C=Lambda`; it does not derive the earlier affine-cosine residual ansatz. Even a frozen generation-isotropic reference gives only a first-harmonic quartic penalty, not a strict interior minimum. The note derives the other probe/curvature terms in the compensator variation and a conditional source-dependent phase equation. The earlier weighted-projection selection rule and low-degree spectral obstruction retain their stated assumptions. Forty-eight tests check these results; no native background/current or physical phase value has been determined, and the target-mass inversion remains only a diagnostic condition.

The separate [source/backreaction analysis](../../analysis/HC_Source_Backreaction.md) derives the spin partial-trace source and shows that scalar currents do not determine its generation coherence. A self-consistent cyclic unitary reduction conserves that coherence. A different completion, varying an independent positive compensator instead of imposing `H_C=Lambda`, has a proved fixed-radius, fixed-scale interior phase minimum for an explicit interval of the input source/penalty ratio. This uses a populated sector, not an empty vacuum; its selected compensator has rank one and is not three positive masses. Releasing the assumed radius gives a cyclic positive descent to a lower-energy shape plateau; a free amplitude goes to zero in this energy. The inherited deeper-compensator hypothesis does not provide the missing readout or independent shape/scale support. Fifty-eight checks now cover these results, including the new radial/scale and core/readout tests. The main TeX and native closure claims are not changed by this conditional construction.

The printed contents list shows section-level navigation only. Subsections and their contents records are retained; their individual entries are not printed in the short contents list. This is a navigation reduction, not removal of mathematical text.

This is not a mathematical validation of every inherited claim. Historical overstrong wording remains auditable and is not licensed by its preservation. The premise qualifications are not a completed repair of all dependent arguments. See `analysis/V480_Full_Monolith_Integration.md` for the integration map, measurements and remaining gates.

## Checks and Build

Run `python -B scripts/qsc_audit/full_monolith_reading.py check` from the repository root. The script rejects a changed origin, changed/missing/duplicated fragments, coverage gaps and newly duplicated labels; the declared CRLF/LF conversion is the sole content-hash normalization. Unit tests are under `scripts/qsc_audit/tests/`.

The numerical examples in `test_generation_coupling.py` require NumPy, as does the separate OP5 relay check. The origin-preservation command itself remains standard-library-only. Passing finite numerical tests does not establish the native coupling or replace the written proofs.

Build `v480-companion.tex` with this directory as the working directory and an output directory under `build/`. Multiple pdfLaTeX runs are required for the contents, references and tables. Use `-no-shell-escape` and `--disable-installer` locally. The existing manual QSC LaTeX build workflow can select `sources/research` with historical-witness building disabled; there is only one TeX entry point directly in this directory.

The `measure` subcommand takes `--before-aux`, `--after-aux` and `--output`; it checks freshness and settled reference/table logs. Page counts include frontmatter, contents, all support and bibliography. This cannot be substituted with the older 655-page modular comparison.

## Integration Discipline

Keep edits in new working modules until a deliberate mathematical repair replaces an inherited statement with its full dependency audit. Do not use a preservation hash to defend an incorrect claim. Do not merge the old modular pre-v4 metadata over the later shifted normal form. Do not modify the published payload, invent a DOI, activate publication or promote detector terminality to all-readout zero.
