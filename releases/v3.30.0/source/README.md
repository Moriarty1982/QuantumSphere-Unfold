# Audited v3.30.0 source layout

This source directory is the repository-friendly assembly target for the audited **v3.30.0** release.

## Intended structure

- `Quantum_Sphaera_Companion_v3_30_0_release_final_wrapper.tex` — compilable wrapper
- `assemble_audited_release.tex` — body assembly file
- `parts/part_01.tex` ... `parts/part_19.tex` — sequential splits of the audited release body

## Current repo status

The wrapper and release metadata are present in the repository.
The full audited body is prepared locally in a split 19-part form and should be mirrored here as the next repository synchronization step.

This split layout is preferred for future repository sync work over oversized monolithic TeX uploads.
