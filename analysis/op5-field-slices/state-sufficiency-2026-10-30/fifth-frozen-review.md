# Independent bounded review: frozen lower germ in fifth-order control

30 October 2026. Read-only code/result review and saved-coefficient/rank inspection; no optimization or linear solve rerun. Reviewed fifth_frozen_lower.py, fifth-frozen-lower-result.json and the current raw_coeff warm-seed code in recursive_calibrator.py. No shared source, older result or repository file was modified.

## Scope and affine structure

The comparison fixes the successful fourth-order candidate through spinor coefficient degree3. Degree4 coefficients are free; degree5 coefficients are eliminated and recovered through the complete highest-operator left gate. The retained lower residual is F degree3 (20 multiindices x24=480 rows); the projected degree4 source contributes 105 rows. There are 35x24=840 real fourth-coefficient variables.

This objective is structurally affine in the free degree4 coefficients. A degree4 spinor coefficient first enters its first derivative at degree3. Its first occurrence in any covariant jet or coframe is therefore at degree3 (or degree4 in undifferentiated appearances). Two variable contributions multiply only at degree at least6, beyond the residual truncation degree4. The coframe constant term and its inverse stay fixed, so the finite inverse series does not introduce a hidden denominator depending on the free coefficients. Remaining products with fixed degree0/1 data give linear contributions. Projection through the fixed highest-operator left kernel preserves affinity.

Consequently a one-shot least-squares solution is the appropriate global numerical test for this particular affine variable window. It is not merely a nonlinear optimizer failing from one starting point. The midpoint check supports the implementation but is not the sole justification of affinity.

## Actual script and result

The script's slicing matches the declared frozen/free window. Its full wide-matrix SVD gives a complete left gate. Both lower F-degree3 equations and projected F-degree4 equations enter the same least-squares objective. Recovery of fifth coefficients is followed by full unprojected residual evaluation. No blocking packing, degree or linearity error was found.

An independent inspection compared every saved coefficient of degree0..3 against the fourth-order seed and found exactly zero difference at all three points. The saved repair singular values show:

| point | projected residual | smallest retained sigma (528th) | largest discarded sigma (529th) | affine midpoint error |
|---|---:|---:|---:|---:|
| 0 | 1.3870396191 | 2.4415e-4 | 1.2051e-13 | below 4.5e-12 |
| 1 | 1.3707012411 | 6.3880e-4 | 1.2269e-13 | below 4.5e-12 |
| 2 | 1.3615010857 | 2.5621e-4 | 1.1963e-13 | below 4.5e-12 |

All three 585x840 repair matrices have numerical rank528 at the recorded relative cutoff1e-9. The clearly separated listed singular values support stability of that numerical rank at cutoffs1e-8 through1e-11; this reviewer inspected the spectrum rather than rerunning the solves. It is not a symbolic or interval-certified rank.

The returned compromise vector has actual F-degree3 residual norms approximately 5.51,5.44,5.39 and F-degree4 norms 13.67,14.57,13.03. It is therefore NOT a repaired successful fifth jet. These are residuals after trading the two nonzero blocks in a coefficient-norm least-squares objective. F degrees0..2 remain at their prior small levels because they cannot depend on the free degree4/5 coefficients.

## Interpretation

The data support numerical incompatibility of the particular frozen degree0..3 germ with a fifth-order completion using only degree4 changes and free degree5. This is stronger than failure with degree4 also frozen, but weaker than any universal no-go result. The successful unrestricted fifth-order calibration is a different finite jet, because it changed some earlier coefficients.

At least some earlier coefficient below degree4 must change to find the known successful fifth-order comparison. This control does not identify whether releasing only degree3 would suffice, whether degree2 must change, or whether a different fourth-order candidate could already admit a fixed-lower prolongation. It establishes neither nonexistence of the comparison model nor a physical obstruction. The substantial earlier-coefficient movement remains a genuine open issue for constructing a compatible infinite sequence.

## Provenance caution

The control's inputs_sha256 records its script, generic module and fourth-order seed, but the generic constructor/raw_coeff also reads the original model source, lower-data file and joint-fit sidecars; the coordinate point is taken from the third-joint-fit sidecar. The complete fourth seed overwrites coefficient values, but these other files remain operational dependencies. Include their hashes in the enclosing evidence record when archiving this control. This observation does not identify a numerical discrepancy in the results reviewed here.

## Verdict

Bounded implementation/design review passed with the stated provenance caution. Saved evidence supports a cutoff-stable numerical incompatibility in this fixed affine variable window. No exact no-go theorem, regional nonexistence statement, convergence conclusion or OP5 closure is asserted.
