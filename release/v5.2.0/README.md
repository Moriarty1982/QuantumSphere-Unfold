# Quantum Sphaera Companion v5.2.0

In preparation (17 November 2026). Not yet published.

- Version DOI: 10.5281/zenodo.24294648 (reserved 17 November 2026, draft 24294648, unpublished).
- Reservation run: 43978639426.
- Concept DOI: https://doi.org/10.5281/zenodo.19210728
- Predecessor: v5.1.0, DOI 10.5281/zenodo.24237112.

## What is new

- Full Companion: research layers v4.10.0-r15 to r28. They record a correction of the frame reading of v4.9.0-r38;
  status notes on the helicity axis, the invariant doublet, the clock functional, the commutant of one generation and
  prior literature (r15–r19); a candidate witness and a per-frame restatement of C5 (r20, r21); the typing of the
  collapse state and of the cascade (r22, r23); the backward check of the counting statistics per frame (r24); two and
  four Dixon copies, the duplication rule for the shift tower and its correction (r25–r27); and the status of the
  residual bend and of the horizon counting rule after the refuted tests H106–H111 and the explorations of 16 and 17
  November 2026 (r28).
- Physics paper: a development subsection on where the missing number of the bent-octant reading comes from (rigidity
  of symmetric carrier constructions, the core as the only escape, its size given only by the weight-two counting
  rule, dependence of the tau-mass test on counting rule and area spectrum), and one sentence in the outlook.

## Validation (before upload)

- Paired document build 43978954178 of commit 8fb6e93: full Companion 1457 pages, physics edition 30 pages; both with
  zero undefined references, multiply defined labels, rerun requests and overfull boxes; no tracked changes.
- Both title pages carry the version DOI 10.5281/zenodo.24294648 and the concept DOI exactly once and no predecessor
  DOI (`tools/qs.py doi`). Pages inspected visually: full page 1, physics page 18 (new subsection 5.8).
- Edition tests (`qam.store.test_editions`) passed locally; guard linter on round r28: 0 candidates.
- Zenodo dry run 43978552171 and reservation 43978639426.

## Scope

This minor version changes content, not the status of the open physical questions. The Koide overlap, the size of
the core and the counting rule per frame remain open. No guard or open problem is closed by the release. Database
records and hashes do not prove physical interpretation.
