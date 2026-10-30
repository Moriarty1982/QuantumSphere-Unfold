# OP5 field compatibility and precision checkpoint

30 October 2026. Research comparisons, not an OP5 closure certificate.

## Read first

- `OP5_Boundary_Fair_Result.md`: implementation correction. Earlier extra edge samples were evaluated but did not enter the optimization residual. Corrected comparisons are preserved; old interpretations must not be used as positive edge-weighting evidence.
- `OP5_Temporal_Coframe_Gauge_Result.md`: four pointwise shear directions and a transverse temporal-coframe fixation. No global gauge symmetry or well-posed evolution established.
- `OP5_Temporal_Compatibility_Identity_Result.md`: explicit four left compatibility rows; one combination is the known scalar state condition, three further combinations remain.
- `OP5_Direct_Compatibility_Result.md`: direct local repairs achieve roundoff-scale full residuals but still fail the second-jet continuation checks. Pointwise closure is not a regional solution.
- `OP5_High_Precision_Example_Result.md`: pointwise residual follows 30/50/80-digit arithmetic after the necessary state normalization is reconstructed. Frozen rounded inputs retain a roughly 3e-15 floor. This does not remove the larger field-continuation residuals.

## Reproduction

Run from `analysis/op5-field-slices/`. Python with NumPy, SymPy, PyTorch is required for the field comparisons; the high-precision example requires mpmath and SymPy. Scripts reuse documented neighboring artifacts and `../OP5_Counterflow_Full_Residual_Check.py`. Most scripts write a same-name JSON sidecar, so use a separate copy to preserve historical results. Research artifacts retain the conventions and restricted assumptions stated in their individual reports.

Portable-copy check at this checkpoint: 43 Python files parsed, 42 JSON files parsed; the six high-precision cases were rerun from a separate copy of the repository files and reproduced the recorded residual values. This was not a rerun of all expensive field optimizations. Existing paper figure remains the original affine comparison field, not the newer candidates.

## Next discriminating work

1. Select first jets with both direct compatibility and derivatives of the scalar state condition, then eliminate symmetric second jets before attributing the remaining source gate. This is a finite-order diagnostic, not yet a regional existence proof.
2. Audit which conditions originate in the native action and which belong only to the comparison readout and zero-spin-connection assumptions. Do not promote the comparison branch into a physical derivation by numerical fit.
3. Only after propagation is understood, formulate a reduced regional initial-value problem with justified coordinate/readout data and monitored independent errors. Lower numerical norms alone are insufficient.

Historical notes saying locally saved/not committed describe their original stage. This checkpoint archives the sequence together; it does not retroactively modify a Zenodo release or establish a new physical constant.
