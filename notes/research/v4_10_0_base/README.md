# 4.10 base: revised main body and layers v4.9.0-r20 to r25 (source-only)

This folder records how the research candidate became the base for 4.10. It is **not** a release.

- Public baseline: v4.9.0, Version DOI `10.5281/zenodo.23534954`, Concept DOI `10.5281/zenodo.19210728`. No 4.10
  Version DOI is reserved; the title page shows the latest published Version DOI until one is.
- `\workingversion` is `4.10.0-draft` (`sources/research/parts/working-preamble.tex`).
- Guard and residual vectors are unchanged in every layer: `R_glob = (0,1,1,1,1)`, `Gamma_guard = (1,1,1,1,1)`,
  `beta_4 = 1/256` unspent. No layer claims C5 = 0, C6/T2, a global photon-clock/RH theorem or global all-readout
  closure.

## What changed

1. **The parts in `sources/research/parts/v470/` are no longer frozen.** The author decided on 2026-10-22 that the
   revision of the main body (layer v4.9.0-r25) becomes the base for 4.10, instead of being carried as
   qualifications in `premise-audit.tex`. The frozen state remains available under the tag `v4.9.0`;
   `v480-source-map.json` and its hashes describe that state.
2. **Revision rule** (layer v4.9.0-r25): a statement that later layers refuted, excluded or withdrew is moved word for
   word to the new appendix `parts/v4100-archive.tex` (`sec:v490-archive`); at its place the same environment keeps
   its number and label, with a short statement of what survives and a pointer. Known errors are corrected in place
   with a framed status note (`\qsstatus`) that gives the earlier wording. Reinterpreted or open statements keep their
   text and receive a status note. Layers, pre-registration notes and test results are never archived.
3. Applied to four parts: `10_sphaera_and_physics`, `18_op1_op2_mathematics`, `20_frame_and_teichmueller`,
   `23_physical_readouts` (55 edits, 15 archived statements). The edits are the same as in the local full monolith;
   `llm/revision_spec_v490.py` holds them, `llm/aufraeumen_v410_github.py` applies them to the parts.
4. The layers v4.9.0-r20 to r25 are appended verbatim to `parts/v490-post-release-layers.tex`.

## Contents

| Path | Content |
|---|---|
| `rounds/v490_r20_round.tex` … `v490_r25_round.tex` | each layer as a separate append-only block |
| `llm/` | check scripts `k59`–`k63`, the revision scripts and specification, core map (`Kernkarte`, v8.3) |

Source of the carried layer block: `Quantum_Sphaera_Companion_v4_8_0_source.tex` after layer v4.9.0-r25,
SHA256 `ccd6d223a02f40785ae3b7cda5a32df8c108367d61a85bc084016dae7c854fba`, lines 70747–71625; content SHA256 of the
block `1b9f34ed3e20053216bee7cae13e0d667e61ef6c92b1745361bde3438fa1490e`. The state of the local monolith before the
revision is tagged `vor-aufraeumen-v490-r24` on the local-history branch.

Build of the candidate under MiKTeX 25.12, three pdfLaTeX passes: 1204 pages, 3752 labels, 0 undefined references or
citations, 0 duplicate labels, no rerun warning, 58 overfull boxes (unchanged). Title page: one Version DOI line, one
Concept DOI line.

## Layers

| Layer | Title | Result |
|---|---|---|
| r20 | A provenance hypothesis for `Delta_gamma < 1/5` | photon-frame clock gain at the Hopf point; chart V3 and clock seed are Hopf data |
| r21 | The clock bound frame by frame, and a derivation of 1/5 | 1/5 is the unique frame-consistent bound; measured matter frame 0.1925 |
| r22 | The frame rule as a standing convention | Convention F (matter, tachyon as `J_B` image, photon as degenerate fixed point); required frame subsection |
| r23 | Convention F applied to the main body | 113 frame-dependent statements classified |
| r24 | Correction of the three discrepancies of r23 as single-frame artefacts | sign = orientation code; main-body tachyon = real projection; main-body photon frame = reference frame R |
| r25 | Revision of the main body | 15 dead ends archived, known errors corrected, status notes |
