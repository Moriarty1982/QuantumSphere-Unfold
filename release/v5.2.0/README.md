# Quantum Sphaera Companion v5.2.0

Published on Zenodo on 17 November 2026.

- Version DOI: https://doi.org/10.5281/zenodo.24294648
- Record and eight deposited files: https://zenodo.org/records/24294648
- Concept DOI: https://doi.org/10.5281/zenodo.19210728
- Predecessor: v5.1.0, DOI 10.5281/zenodo.24237112.
- Frozen source commit and tag target: 8fb6e9378f6e6789697c60d3ba8b748cc2b56de6.
- Paired document build: 43978954178; upload: 43981330807; reservation: 43978639426.

The two English editions share one source snapshot. The full Companion has 1457 pages; the physics edition has 30.

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

## Validation

- Paired document build 43978954178 of commit 8fb6e93: full Companion 1457 pages, physics edition 30 pages; both with
  zero undefined references, multiply defined labels, rerun requests and overfull boxes; no tracked changes.
- Both title pages carry the version DOI 10.5281/zenodo.24294648 and the concept DOI exactly once and no predecessor
  DOI (`tools/qs.py doi`). Pages inspected visually: full page 1, physics page 18 (new subsection 5.8).
- Edition tests (`qam.store.test_editions`) passed locally; guard linter on round r28: 0 candidates.
- Zenodo dry run 43978552171 and reservation 43978639426.
- The upload run verified the unpublished draft, the DOI, the version and all eight checksums; its preview check
  failed because the helper does not set the preview explicitly. The author set the preview on Zenodo and published
  the record. After publication the public record was checked: eight files with MD5 equal to the uploaded package,
  both PDFs equal to the paired build, default preview `Quantum_Sphaera_Companion_v5_2_0_full.pdf`, version v5.2.0,
  date 2026-11-17, relation "is new version of" v5.1.0.

## Scope

This minor version changes content, not the status of the open physical questions. The Koide overlap, the size of
the core and the counting rule per frame remain open. No guard or open problem is closed by the release. Database
records and hashes do not prove physical interpretation.
