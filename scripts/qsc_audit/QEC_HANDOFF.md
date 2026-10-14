# QAM framework interface: handoff for Trent Slade / QEC

This change provides an executable concept interface for the QAM/MML/MMA structure in Marc Brendecke's Quantum Sphaera Companion. It is offered for review as a possible QEC adapter or integration reference.

## What is available

- `framework_interface.py`: a versioned QAM context containing objects, declared relations, guards, source provenance and residual witnesses; fixed MML `EXPORT` / `SCRUB` requests; MMA `continue` / `guard` / `reject` results.
- `tensor_grammar_check.py`: a local role/index checker for ordinary upper–lower pairings, explicitly mediated same-variance comparisons, same-kind primitive tensor formation, finite Boolean masks and guarded mixed readouts.
- Five JSON examples: direct positive and negative controls, a framework context, a framework export request and a framework tensor-audit request.
- 43 unit tests covering syntax, assumption propagation, residual preservation, representation integrity, replay and SHA-512 migration boundaries.

All fingerprints use SHA-512: 512 bits / 128 lowercase hexadecimal characters. Both report types explicitly record `hash_algorithm: "sha512"`. The schemas are `qam-role-audit/2` and `qsc-framework-interface/2`.

## Why the concept boundary matters

`QClEq`, `QAdmTransport`, `QRead` and `QTensorAdm` are recorded as separate declared mathematical relationships. A representation hash does not create an equivalence relation or prove admissibility. Tensor-admissibility declarations are bound to the particular pair being checked. An unrelated request guard cannot supply a missing tensor-admissibility declaration.

An open residual remains open even when a grammar check succeeds. The interface records declarations and checks supported structural syntax; `closure_proved` and `mathematical_relations_proved` remain false. No numerical tensor calculus, automatic LaTeX parser, transport engine or theorem prover is included.

## Quick evaluation

Run from the QuantumSphere-Unfold repository root with Python 3.10+; no extra packages are required:

```text
python -B -m unittest discover -s scripts/qsc_audit/tests -v
python -B scripts/qsc_audit/framework_interface.py scripts/qsc_audit/examples/framework_context.json scripts/qsc_audit/examples/framework_tensor_request.json --output build/audit/framework_tensor.report.json
python -B scripts/qsc_audit/framework_interface.py scripts/qsc_audit/examples/framework_context.json scripts/qsc_audit/examples/framework_tensor_request.json --verify build/audit/framework_tensor.report.json
```

The positive framework example returns `continue` with seven accepted local operations, while preserving an open residual and an unresolved `QClEq` declaration. The direct negative example returns three rejections and one unresolved tensor-admissibility obligation.

## Integration notes

1. Start with a read-only adapter that accepts an explicit context and request and returns the receipt. Payloads and context should remain unchanged.
2. Retain QAM guards, declared relationships, scope and residual witnesses when mapping QEC objects into the context. Declared evidence text is not independently verified.
3. Keep the versioned SHA-512 interface identities distinct from QEC's existing SHA-256 receipt identities. Existing QEC proof chains would need an explicit compatibility/migration design before any replacement.
4. The current tools fingerprint source-rule files at repository-relative paths. Adoption elsewhere requires an explicit source-bundle layout or reviewed source resolver; the rules must not disappear during packaging.
5. The current implementation and source texts remain in Marc's repository. Attribution, licensing and any upstream incorporation should be agreed before redistribution or merging into QEC.

The implementation was written for this repository; no QEC source code was copied. QEC's reproducible-receipt and replay approach motivated the engineering pattern. The grammar and concept boundaries are grounded in the Companion's existing QAM, store/readout and tensor-admissibility source blocks.

Further documentation: [framework interface](FRAMEWORK_INTERFACE.md), [tensor role checker](TENSOR_GRAMMAR.md).
