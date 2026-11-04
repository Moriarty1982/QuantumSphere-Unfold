# QAM paper — outline (draft, 4 Nov 2026)

**Working title:** *A typed bookkeeping language for verifiable research with language models: design, Lean verification, and a case study*

**Type:** methods paper. **Publication:** Zenodo (no arXiv). Subject keywords for the Zenodo record instead of arXiv categories:
logic in computer science, formal verification, Lean 4, programming-language semantics, AI-assisted research, reproducibility,
research integrity. A journal submission (e.g. a venue for research software or AI-for-science) is possible later; it does not require arXiv.

**Length target:** 12–18 pages.

## 1. Introduction (≈ 2 pp.)
- Problem: long research projects carried out with language models accumulate three kinds of error that are hard to see in prose:
  quantities from different frames compared as if they were the same, values put in but later read as derived, and statements
  promoted beyond what was shown.
- Idea: a small typed language on top of ordinary set theory that makes these errors ill-formed, plus a store machine whose
  ledger records every step; the language is formalized in Lean.
- Contributions: (i) the language (QAM) and its instruction layer (MML/MMA); (ii) Lean proofs of its invariants (preservation,
  progress, atomicity, ledger completeness, no false certificate); (iii) a case study of a months-long project with about 90 audit
  rounds and 58 pre-registered tests; (iv) an honest account of what the discipline caught and what it did not.

## 2. The language (≈ 3 pp.)
- Eight tagged tuples over ZF (state, layer, operator, readout, branch, shell, witness, tensor); recognition predicates, not axioms.
- Relations: admissible transport, closure-class equivalence, readout; closure-compatible readouts.
- Two-sided display: front indices = frame/readout side, back indices = structure side; only upper–lower contraction, all other
  comparisons through declared comparison or selector tensors.
- Status tags (proved / computed / conditional / reading / open / withdrawn) and frame tags.
- Hilbert-shift reindexing and back-translation.

## 3. Syntax and semantics of the store machine (≈ 3 pp.)
- Store = content (objects at addresses, relations), guard register, snapshots, ledger.
- Instructions (MML): store, link, snapshot, rollback, scrub, export.
- Transition semantics (MMA): raw effect, guard check, status cont / reject / guard, ledger entry.
- Certificates: a certificate for P contains a proof of P; machine candidates are only labels.

## 4. What is proved in Lean (≈ 3 pp.)
Lean 4 (v4.35.0), core only for these modules, built in CI without `sorry`.
- `QSFormal.QAM`: tag disjointness (`not_state_and_op`, `qState_iff_tag`, `tag_lt_eight`); shift/back-translation bijection
  (`back_shift`, `shift_back`, `back_toShifted`, `toShifted_back`); transport principles and chains (`first_transport_principle`,
  `first_op_transport`, `chain_clEq`, `chain_readout`).
- `QSFormal.Store`: guard fidelity (`exec_cont_admissible`), **preservation** (`exec_preserves`, `run_preserves`), lineage
  (`exec_logs`), rollback (`rollback_restores`), no false certificate (`no_false_certificate`).
- `QSFormal.StoreProgress` (new, 4 Nov 2026): **no stuck states** (`exec_ne_halt`), exact status characterization
  (`exec_cont_iff`, `exec_reject_iff`), **atomicity** (`exec_atomic`), **progress** for snapshot, scrub and export
  (`snapshot_progress`, `scrub_progress`, `export_progress`), **ledger completeness** (`exec_ledger_length`, `run_ledger_length`).
- `QSFormal.Route`: admissibility and closure-class preservation along route paths.
- What is *not* proved: anything about the content that is written in the language. The language secures form, not truth.
- Simplifications against the full specification: natural-number addresses, no pointer conditions, no clone/merge.

## 5. Case study (≈ 4 pp.)
- Setting: one author with a starting conjecture, language models used from the beginning (Claude; ChatGPT/Codex), a 1300-page
  research text, a public repository.
- Process: numbered append-only rounds; pre-registration notes committed before computation; guard linter; independent recomputation
  (including cross-checks between models); a parallel computation workflow; an internal referee step.
- Numbers (to be finalized from the repository): about 90 audit rounds since v4.8.0; 58 registered tests, of which the wiki table
  lists 15 refuted, 6 confirmed, 6 invalid by their own criterion, the rest compatible, structural or pending; four predictions open.
- Error classes and how they were caught, with examples:
  - frame mixing (comparison across frames; caught by the two-sided display) — e.g. the audit of the open problems;
  - put-in values read as derived — the frame offset and its counting reading;
  - over-promotion — the cosmological-constant chain, the six early predictions;
  - external dependence — a claimed proof of the Riemann hypothesis, caught not by the language but by an audit round;
  - numerical artefacts — a precision-conversion error withdrawn before entering a round.
- Translation table: key statements in standard and QAM notation (from `paper/short/extras/appendix_qam.tex`).

## 6. Discussion and limits (≈ 2 pp.)
- What the typing prevents and what it cannot prevent (wrong premises, wrong literature readings, flawed physics).
- Cost: overhead of the bookkeeping; length of the record (85 % protocol in the research text).
- Relation to existing practice: proof assistants, provenance and lab-notebook systems, pre-registration in empirical science,
  workflow languages; to be researched.
- Next steps: progress for store/link/rollback under stated guard conditions; clone/merge; a checker that reads the research text.

## 7. Conclusion

## Appendix
- Lean module list and how to build.
- Disclosure of language-model use (same wording as the physics paper).

## Open tasks
- Literature research for Section 6 (related work).
- Final numbers for Section 5 from the repository (rounds, tests, retractions).
- Decide the title.
