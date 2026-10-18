# Parallel Follow-Up of the Regular Cartan Jet

Date: 2026-10-18. Status: parallel follow-up reviewed and integrated, with combined verification complete. This records independent work streams and their integration gates, not a new field-theory result. All tasks concern the explicitly added neutral odd-cross Cartan comparison. No main TeX/PDF change or Git operation is requested for this round.

## Common Baseline

The [regular gravitational prolongation](HC_Cartan_Regular_Gravity.md) supplies a 384-equation finite-jet completion with evaluated rank 332. Fifty-two derived row identities explain its numerical compatibility. The 68-by-56 normal system has a sixteen-dimensional kernel; ten leading coordinate/Lorentz gauge directions have been exhibited, but the six-dimensional remaining quotient has not been classified. The fields remain off shell away from the prepared point.

Baseline input SHA-256 values before dispatch:

| Input | SHA-256 |
| --- | --- |
| `HC_Cartan_Cauchy_Rank.json` | `7ee98a63c60dbe71a4bee535b2b73bca518e7ed7165e17889a894f912d52590f` |
| `HC_Cartan_Spatial_Propagation.json` | `1ca98d6b4658d279867469948cfdafe68442fa04456320ab4267d0df5befb75b` |
| `HC_Cartan_Regular_Gravity.json` | `9719ef580419e7a1d4c49a7aec2f41987832d806215defacd74d8db8c09f4cdc` |
| `HC_Cartan_Regular_Gravity.py` | `89cf5597fc935d463eed604f9c9eb247cda17b576ae294dbfad6e45dacbc063f` |
| `HC_Cartan_Spatial_Propagation.py` | `1eaa40763d84f28dfb0846032a96da28dd18ab8080cdc2a400c82827eb21feaf` |

The last completed working-checkout baseline suite had 1,825 audit tests and 34 separate OP5 tests, including six unrelated metadata-hygiene tests outside this research change set. The research baseline alone was therefore 1,819 audit tests plus 34 OP5 tests. This historical baseline does not assert that newly written follow-up tests have already passed.

## Independent Work Streams

| Stream | Question | Exclusive output files |
| --- | --- | --- |
| Remaining multipliers | What do the six remaining normal directions do to the sourced connection, curvature and constraints? Which effects are zero and which are compensated? | `HC_Cartan_Remaining_Multiplier.{py,json,md}` and its focused test module |
| Next scalar compatibility | Does the full nonzero-lambda scalar Hessian vanish on the saved jet? Can a failed gate be repaired while keeping all 384 prior equations? | `HC_Cartan_Next_Scalar_Compatibility.{py,json,md}` and its focused test module |
| Independent review | Are the existing action variations, identities, leading gauge directions and curvature claims correct and appropriately qualified? Preserve the independent checks as regression tests. | `HC_Cartan_Independent_Review.md` and `test_hc_cartan_independent_covariance.py` |
| Parent integration | Derive a temporal regularity neighborhood, check input consistency, review returned changes, resolve concrete findings, run one combined verification, and update shared indexes. | This note, `HC_Cartan_Regular_Neighborhood.{py,json,md}` and focused tests, shared research indexes, and any explicitly justified integration repairs |

Each worker may read the common baseline but must not overwrite it, another stream's outputs, the main paper or release metadata. No worker commits or pushes. The next-scalar stream is deliberately bounded to a necessary gate; it is not a request for an unchecked full C3/R2/FE2 solver.

## Integration Gates

1. Match every result to the same unchanged input point and model. Re-preparing free higher jets must not be described as evolving the old data.
2. Check action-level or algebraic derivations independently of a fitted numerical solution. A large test count alone is not evidence for physical identification.
3. Retain failed frozen-data controls and full unprojected residuals. A successful projected equation is insufficient.
4. Distinguish actual algebraic null directions, compensation by other fields, leading gauge freedom and physical degrees of freedom.
5. Re-run focused tests after integrating any repair, then run the complete audit and separate OP5 suite once. Verify unchanged main-paper reconstruction.
6. Keep local compatibility, formal integrability, Cauchy propagation/existence and native physics as separate claims.

## Results

The parent [temporal-neighborhood estimate](HC_Cartan_Regular_Neighborhood.md) gives a conservative baseline coordinate radius 1/8192 with positive probe weights and invertible T throughout the Taylor-field ball, using analytic norm inequalities evaluated with floating-point input constants. Its 22 focused tests pass. It is not full normal-rank control, an interval certificate or an on-shell neighborhood.

The [independent review](HC_Cartan_Independent_Review.md) found no concrete sign/index/variation defect in its targeted scope. Direct parent-action covariance and complete accompanying gauge-jet changes support the previous identities more independently than a solved residual alone. Its eight independent covariance/companion-jet regression tests are saved and pass both the worker run and parent recheck.

An important retained boundary is that **the matched curvature is metric Levi-Civita curvature, not the sourced Cartan curvature**. At the saved point the review finds nonzero torsion and a clear Cartan/LC curvature difference. Their component norms are chart-dependent diagnostics, not new physical scales. The reconstructed algebraic Cartan residual checks the solve, not its action derivation by itself.

The [next scalar gate](HC_Cartan_Next_Scalar_Compatibility.md) is complete. It derives the exact nonzero-multiplier off-shell scalar identity, finds a failed Hessian on the frozen earlier jet and then jointly solves the ten new conditions with all 384 prior equations. The 394-by-1200 rank is 342, and the directly evaluated full residual norm is about 7.04e-11. The lower point/couplings are unchanged; the higher preparation is new, not an evolution of the previous vector. Its 34 tests and 80 earlier focused regressions pass in the worker run.

Parent [cross-result integration](HC_Cartan_Parallel_Neighborhood.json) checks the exact retained arrays/couplings and common input fingerprints, re-evaluates all 394 equations without refitting, and recomputes the regular temporal estimate on the new higher data. All eight integration tests pass. The selected radius happens to remain 1/8192, with newly evaluated margins, rather than an inherited constant.

The [remaining-multiplier calculation](HC_Cartan_Remaining_Multiplier.md) constructs a full explicit six-coordinate complement to the ten known leading gauge directions. Three are axial spin-source nulls of L^T; three require symmetric coframe-acceleration/contorsion compensation. All six preserve the point Cartan curvature, but the compensated three change metric LC curvature and torsion derivatives. The frozen higher probe equations detect all six, so neither source-nullness nor point-curvature blindness establishes an extra action symmetry. The worker's 38 new tests and 80 prior focused regressions pass.

The two mathematical workers and reviewer have finished. Parent review found no mathematical integration repair necessary. Before committing, source-only fingerprinting was made insensitive to CRLF/LF checkout conversion, with an added check inside the existing fingerprint regression; mathematical data and stored input digests remain unchanged. The common baseline inputs and retained lower data remain unchanged. There are 110 new tests in this parallel round: 38 multiplier, 34 scalar-gate, eight independent covariance, 22 temporal-neighborhood and eight cross-result integration checks. The parent combined working-checkout run passes all 1,935 audit tests; the separate OP5 run passes 34, for 1,969 total. Six audit tests belong to unrelated, separately maintained metadata changes not included in this research commit: the committed research suite therefore contains 1,929 passing audit tests plus 34 OP5 tests, or 1,963 total. Test discovery independently confirms that partition; it is not a second full test run. Main-paper reconstruction retains the same expanded hash, 38 inherited fragments and all original labels. The worker reports are not substituted for the combined run. The personal skill packaging validation also passes separately and is not included in the mathematical test count.

## Reusable Workflow

At the user's request, this bounded delegation pattern is also installed as the personal `parallel-computation` skill outside the repository. It defaults to independent substantial calculations and checks, not parallelizing every small Python command. Disjoint writes, a locally owned critical path, fixed-input validation, a small worker budget and one parent integration run are retained. Resource-limit failures should not trigger repeated replacement agents. The skill's packaging validator passes; that is not a mathematical validation of this paper.
