# QAM tensor role checker

This first executable checker validates **explicit role data** derived from the Companion's two-sided notation. It does not parse TeX or compute numerical tensors. It is a research/audit tool around the paper.

It can also be called as the first adapter of the [QAM/MML/MMA framework interface](FRAMEWORK_INTERFACE.md), which retains the shared object, relation, guard and residual context around each audit request.

## Purpose and source rules

The rules come from these existing Companion blocks:

- `02_store_array_and_pre_v4_readouts.tex`: two-sided structural tensor interface; admissible contractions and comparisons; guarded mixed readouts; binary mask registry.
- `03_two_sided_tensor_masks_and_freeze.tex`: role-erasure normal form; Boolean selector grammar; mask-filter conservativity.
- `05_qam_tensor_admissibility_translation.tex`: same-kind tensor formation and the separate structural admissibility obligation.

The report records SHA-512 fingerprints of these files and of the checker. No QEC source was copied. The useful engineering patterns adopted are reproducible representation, a chained audit record and recomputation of saved reports.

## Inputs

The versioned JSON schema is `qam-role-audit/2`. Start from `examples/tensor_roles_valid.json`.

Version 2 uses SHA-512 throughout (512 bits, 128 lowercase hexadecimal characters), with `hash_algorithm: "sha512"` recorded in reports. Version-1 inputs and reports are not silently migrated; update the schema and recompute the report.

- `spaces`: named index spaces with positive integer dimensions. A name identifies a space; two spaces of equal dimension are not silently identified.
- `objects`: named objects with `kind`, JSON `payload`, and an `indices` map. Index slots declare `label`, `space`, `side`, `variance`, and `role`.
- Front roles: `readout`, `frame`, `observer`, `language`, `address`. Back roles: `structure`, `action`, `field`, `transport`, `operator`.
- `comparison` and `selector` object kinds are auxiliary declarations for this input format, not new primitive QAM kinds.
- `guards`: named assumptions with `status` (`true`, `false`, or `null`) and textual `evidence`. Evidence is a recorded declaration, not a machine-checked proof. The positive example deliberately uses illustrative assumptions.
- `mask_universes`: ordered lists of readout-kind names. Entry `j` receives bit `2**j`. Their order is semantically significant.
- `operations`: ordered local checks, each with a unique `id`, a `type` and a list of declared `guards`.

Operation forms:

| Type | Fields beyond `id`, `type`, `guards` | Checked behavior |
|---|---|---|
| `contract` | `left`, `right`, each `{object,index}` | Opposite variance, matching space and dummy label; no pairing a slot with itself. |
| `compare` | `left`, `right`, `comparison`, `comparison_slots` | Same-variance operands; a declared binary comparison with opposite-variance slots and matching spaces/labels. Front/back role tags remain explicit. |
| `tensor_product` | `left`, `right` object names | Same-kind formation for states, layers, operators, readouts, branches or shells. Structural admissibility needs separate declared guards. |
| `mask` | `universe`, `operator`, `left`, and `right` for binary operations | `union`, `intersection`, `xor`, finite-universe `complement`. Zero activates no kind; bits outside the universe are rejected. |
| `mixed_readout` | `universe`, `mask`, `components`, `aggregation` | Components are `{object,readout_kind}`. The mask selects declared readouts without rewriting payloads; aggregation is named, not evaluated. Compatibility needs separate declared guards. |

Each contraction is a local pairing check. The two sandwich checks in the example describe the two pairings in `A_mu T^mu_nu B^nu`; they do not execute the sandwich or derive an output tensor. Full expression parsing, dummy-index multiplicity across an entire expression, coordinate transformations, tensor transport and numerical aggregation are outside this first version.

## Outputs and safety limits

The checker reports `accepted`, `rejected`, or `unresolved` for each operation. `accepted` means the supported role grammar and supplied guard declarations pass; it does **not** establish mathematical tensor admissibility or closure. Both proof flags remain false in every report. Missing admissibility guards and unknown guards remain visible as unresolved obligations.

Reports contain the input fingerprint, rule-source fingerprints, normalized role data or selector results, guard declarations, an ordered receipt chain and a final report fingerprint. Hashes establish representation integrity, not QAM closure equivalence. Changing an input, assumption, source rule file or checker invalidates replay against the old report. Object-map key order does not affect identity; operation and mask-universe order do.

The tool does not rewrite source TeX, modify component payloads, access a network, evaluate arbitrary expressions or execute user-supplied code. Unknown operation fields are rejected. The CLI refuses to overwrite its input with the output report.

## Run and review

From the repository root, using Python 3.10 or later and no extra dependencies:

```powershell
python -B scripts/qsc_audit/tensor_grammar_check.py scripts/qsc_audit/examples/tensor_roles_valid.json --output build/audit/tensor_roles_valid.report.json
python -B scripts/qsc_audit/tensor_grammar_check.py scripts/qsc_audit/examples/tensor_roles_valid.json --verify build/audit/tensor_roles_valid.report.json
python -B scripts/qsc_audit/tensor_grammar_check.py scripts/qsc_audit/examples/tensor_roles_rejected.json --output build/audit/tensor_roles_rejected.report.json
python -B -m unittest discover -s scripts/qsc_audit/tests -v
```

Expected report location: `build/audit/` (ignored generated output). Omitting `--output` prints the complete report. The negative example deliberately returns exit code 1 with three rejections and one unresolved admissibility obligation.

Exit codes: 0 = all supported checks accepted (or saved report matches recomputation); 1 = rejected/unresolved checks (or replay mismatch); 2 = malformed input or file error. A successfully verified negative report remains a negative mathematical/grammar result: verification checks the saved report's integrity, not whether its operations were accepted.

## Validation

The unit tests exercise raw same-variance rejection, dual comparison, mismatched spaces and labels, invalid role sides, mixed-kind tensors, unresolved and failed guards, finite mask operations, unchanged payloads, unsupported fields, duplicate input identities and tampering even after recalculating the stored hashes.
