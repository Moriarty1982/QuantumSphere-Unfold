# Quantum Sphaera Companion v5.5.0 — DOI RESERVED, NOT UPLOADED, NOT PUBLISHED

Status on 26 November 2026: the version DOI is reserved (approved by the author on 26 November 2026). Zenodo draft 24563811
is a new version of record 24500009; it is unpublished and holds no files. Nothing is uploaded or published, and no tag
exists. The DOI resolves only after publication. For every later run use `deposition_id=24563811`, never `new_version_of`
again. Runs of the workflow "Zenodo Release": dry run 45842058182, reservation 45842937765.

- Target version: v5.5.0 (full Companion and physics paper, one package).
- Version DOI: https://doi.org/10.5281/zenodo.24563811 (reserved, unpublished).
- Concept DOI: https://doi.org/10.5281/zenodo.19210728
- Predecessor: v5.4.0, DOI 10.5281/zenodo.24500009, record https://zenodo.org/records/24500009.
- Metadata draft: `release/zenodo/metadata_v5_5_0.json` (publication date provisional).
- Source state of the checks below: working tree on top of commit c0657a6afe231e2877531430cc199f4c283b14d0, with uncommitted
  changes. The frozen source commit is fixed only after the release branch is committed.

## What is new

- Full Companion: research layers v4.10.0-r60 to r68. Most of them are explorations or tests marked as not blind in whole
  or in part; refuted tests are recorded as refuted. Topics: the family SO(3) on the Albert algebra, its breaking to A4 by
  the charge as a spin-3 tensor, a no-go for quark mixing under exact A4, H127 (r60); corrections of two formula slips in
  r56.4 and r07.4, no number or status changes (r61); octonion copies in the sedenions and the remainder generation, H138 to
  H147 (r62); the Koide point as fixed point of the frame exchange and the postulate of equal standing of the matter and
  the tachyon frame, with the phase 2/9 still a fit, H148 to H156 (r63); a record of the tests H105 and H128 to H136 and
  precisions from the audit of the stand-alone physics article (r64); charge axis and charge type on the sedenion carrier,
  with the relative CP sign depending on one named setting, H162 (r65); beta_sym as the overlap of the Hopf state with the
  antipode under one named reading, H164 (r66); the counting rule adopted by the author on 26 November 2026 as a postulate,
  beta_sym = 0.5494056410 and gamma_L = 1.8646997646 as reference values, and the refuted test H165 (r67); a recalculation of all numbers that depend on beta_sym at the reference value, an
  exploration that changes no recorded verdict (r68).
- Physics paper: a new development section "Family symmetry, octonion copies and the Koide point on the tower" in the masses
  part (r60 to r65); additions to "One number and several translations" in the limits part on the recursive field equation
  (r64), the two-readout reading (r66), the counting postulate with its reference value and H165 (r67), and one sentence
  on the recalculation k358 (an exploration, recorded as layer r68); one sentence in the main
  text of the limits section on the postulate.
- Layout only: three tables and one display in r60, r62 and r67 were reset to fit the page; their content is unchanged.
- Research catalogue: eleven new entries appended to `qam/editions/v5_research_notes.json` (H149 to H156, H162, the
  decision note of r67, and the recalculation k358); 61 entries in total.

## Validation done in the preparation

Only what was actually run, locally in a container (TeX Live 2023, pdflatex), on the working tree named above.

- `python -m pytest qam/store/test_editions.py -q`: 3 passed, before and after the changes.
- `python -m qam.tools.configure_v5_editions` into a new database: 7 physics sections, 2468 full statements (the number
  the test expects), 61 research notes registered, each with a verbatim excerpt that occurs exactly once in its note.
- `python -m qam.tools.build_v5_documents` (after adding r68 and the layout fix): status `candidate-built`,
  `build_complete` true. Full Companion 1572 pages, physics edition 38 pages. Both: zero undefined references, zero
  multiply defined labels, zero rerun requests, zero overfull boxes. The PDFs of this build carry the v5.4.0 title data
  and are not release files. A first build had four overfull boxes in the full Companion (frames table of r60, table of
  r62.1, display of r67.1, frames table of r67); they were removed by a layout-only change (column widths, one display
  split in two), content unchanged.
- Reservation dry run from section 1 of `notes/anleitungen/zenodo-release.md` (`--reserve-only --dry-run`): metadata
  validated, no Zenodo API call that changes anything.
- `guard_linter.py` (`notes/research/v4_8_0_r03_r12/llm/training/`) on the metadata and on the three changed edition
  texts: 0 hits.

The check "paired-documents" runs on the PR of this preparation. Not done: `tools/qs.py doi` on the PDFs (needs the reserved DOI), any Zenodo step, `CITATION.cff`, `.zenodo.json`, the DOI section of `AGENTS.md`, `DOI_ROLES` in `tools/qs.py`. The schema
of the assertion database was not changed; no migration was needed for the checks above. No visual check of the PDFs.

## DOI stamping (26 November 2026)

Entered: `qam/editions/v5_release.json` (version 5.5.0, date, version DOI), the metadata description, `.zenodo.json` (copy of
the metadata file), `CITATION.cff`, `DOI_ROLES` in `tools/qs.py`, the DOI section of `AGENTS.md` (as reserved and
unpublished), `sources/research/parts/working-preamble.tex` (version, date, DOI, PDF title). The publication date
2026-11-26 in these files is provisional and is set to the actual date before publication. Rebuild after stamping (local container, `python -m qam.tools.build_v5_documents`): status `candidate-built`,
`build_complete` true; full Companion 1572 pages, physics edition 38 pages; `pytest qam/store/test_editions.py`: 3 passed.
`python tools/qs.py doi` on both PDFs: the version DOI 10.5281/zenodo.24563811 occurs exactly once, on the title page; no
previous DOI on a title page; the expired DOI does not occur. The release files themselves come from the paired build on
GitHub, not from this local build.

## Scope

This minor version changes content, not the status of the open physical questions. OP1 to OP5, C5 and C6/T2 remain open.
The counting rule is a postulate, not derived, and so is the equal standing of the matter and the tachyon frame; OP1 now
reads "derive the counting postulate". Refuted, among others: H138a, H138b, H142b, H144c (r62); H128a, H131b, H132, H135,
H136 (r64); H165 (r67). The number of generations, the charge axis, the Brannen phase, the orientation of the octant step
and the source identification of the OP5 case are not derived. No guard is closed by the release. Database records and
hashes do not prove physical interpretation.

## Next steps needing the author's approval

1. Commit, PR and merge of this preparation (content changes go through branch and PR).
2. Paired build on GitHub (check "paired-documents" on the PR).
3. Done on 26 November 2026: reservation of the version DOI (draft 24563811).
4. Done on 26 November 2026 (see "DOI stamping" below): DOI stamping as in `.github/ISSUE_TEMPLATE/release-4-doi.yml`: `qam/editions/v5_release.json`, metadata description,
   `CITATION.cff`, `.zenodo.json`, this note, `DOI_ROLES` in `tools/qs.py`, DOI section of `AGENTS.md`; rebuild and
   `tools/qs.py doi` on both PDFs.
5. Upload into the draft with `replace_files=true` and `default_preview` set to the full PDF; check of the draft and its
   preview by the author.
6. Publication (`publish=true` and `confirm_publish=true`), with the final publication date in the metadata.
7. Preview check after the publication run (`zenodo-fix-preview.yml` with `apply=false`, correction only if needed).
8. Tag `v5.5.0` and GitHub release by the author; afterwards issues, wiki and the DOI discipline in `AGENTS.md`.
