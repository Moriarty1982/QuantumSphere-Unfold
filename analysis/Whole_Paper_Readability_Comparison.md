# Modular Active-Core Reading Route and Length Comparison

Date: 2026-10-15. Entry point: `sources/active-core.tex`.

## Scope Correction

The user's intended complete paper is the v4.7.0 full monolith. Its repository PDF, `release/v4.7.0/Quantum_Sphaera_Companion_v4_7_0 (5).pdf`, has 1,014 pages, verified with PDF metadata. The restructuring below was applied only to the older modular `sources/` tree, which retains the v3.35.0 synchronization baseline with later working edits. Calling this a completed whole-paper pass was incorrect. It does not fulfill the requested restructuring and length comparison for the complete v4.7.0 paper.

The separate archived modular test PDFs have 638 pages (Active Core) and 249 pages (Historical Witness). They are different document/version scopes, not an additive reconstruction of the v4.7.0 monolith. Consequently, neither subtracting 655 from 1,014 nor adding the historical witness to 656 measures the unprocessed part of v4.7.0. The missing follow-up is now separately implemented as `sources/research/v480-companion.tex`, with full-origin coverage and its own 1,014-page baseline audit. See `analysis/V480_Full_Monolith_Integration.md` and its metrics JSON; this report remains only the historical modular comparison. Frozen release files remain unchanged.

## Baseline and Scope

The baseline is the local working state immediately before this whole-paper pass, including the earlier QAM/proof-detail pilot. It is not a comparison against a published release. The active document includes its frontmatter, contents, technical appendices and bibliography; the separate Historical Witness and frozen release sources are not modified or counted here.

The pass separates the mathematical/physical main line from supporting protocols throughout the modular active include tree only. This is an editorial reorganization, not a line-by-line scientific validation, a full-v4.7.0 revision or a new release.

## Measured Length

| Portion | Before | After | Change |
| --- | ---: | ---: | ---: |
| Main text, frontmatter and contents | 453 pages | 125 pages | -328 pages (-72.41%) |
| Technical appendices and bibliography | 202 pages | 531 pages | +329 pages |
| Complete active document | 655 pages | 656 pages | +1 page (+0.15%) |

The first appendix, labelled `app:mm-tools`, starts on page 454 before and page 126 after. The split counts all pages before that first appendix as main/frontmatter and all remaining pages as appendix/bibliography.

These are layout page counts from settled pdfLaTeX draft-mode runs, read from the AUX file. No replacement PDF was produced and no editor tab was replaced. Font size, paper size and page margins are unchanged. The contents' number columns were widened to accommodate the longer appendix identifiers.

The complete document is **not shorter**. Its main line is substantially shorter because full technical material was relocated, not discarded. Reduced frontmatter repetition is offset by new navigation, visible scope qualifications and pagination. A further reduction in total length would require a separate, substantive deduplication/selection pass within the retained appendices.

For an additional source-level check, the comment-stripped expanded TeX has 34,248 lines / 2,296,234 characters before and 34,384 lines / 2,299,412 characters after. These include commands and whitespace and are not prose word counts.

## What Changed

- The core Sphaera/physics construction, structural/spectral hypotheses, master model, mathematical OP statements, physical readouts and live burdens remain in the main line.
- Historical pre-closure tools, earlier synthesis, local crystal/HC repair, status genealogy, Phase IV detail, local OP-entry protocols and the full OP transport unfolding now have named appendix destinations.
- Complete handoff/grouped-layer modules, split/refold register memory and the computational/decoder specification are reused once in the appendices, without duplicate includes.
- The abstract and reader orientation no longer repeat the full release-by-release infrastructure history. Conditions and open status remain visible, including the distinction between transport invariance and numerical OP closure.
- The single appendix switch is now in the appendix wrapper, independent of where a computational module is included.

## Preservation and Checks

Seven extracted fragments, totalling 498,832 bytes, were moved by exact byte slicing. Other complete modules were rerouted through includes. The local relocation manifest is `build/reading-length-audit/relocations.json`.

The before/after audit preserves all 1,876 baseline label occurrences and all 4,574 protected statement, proof, table and display-formula blocks, modulo whitespace for the block hashes. There are no missing baseline labels, no missing protected blocks and no newly duplicated labels. Eleven navigation labels were added. All 48 files in the resulting literal include tree occur once.

The 75 audit/regression tests and 34 OP5 relay tests pass (109 total). The final layout run has no unresolved references or rerun request. Layout work remains: 79 overfull-box reports and four pre-existing duplicate float-anchor warnings are present. Successful compilation is not a claim of warning-free typography or mathematical correctness.

The preservation audit follows literal inputs and hashes selected environments and standalone displays. It is not a full TeX interpreter and does not prove that an inherited argument is correct. Inherited stronger status wording is retained for reconstruction, subject to the visible present-day qualifications; this pass does not resolve those scientific issues.

## Rechecking

The audit tool is `scripts/qsc_audit/reading_length_audit.py`. Local full manifests are `build/reading-length-audit/before.json` and `build/reading-length-audit/after.json`; build artifacts are intentionally ignored by Git. It rejects page measurements if an active TeX source is newer than the AUX file.

Before expanded-source SHA-256: `464327f41ea325356fc3c739beabe99e71bf5ca12346c177185684d9020fbfba`.

After expanded-source SHA-256: `7f092953c4ea7141f73344bab46c1e1c4bcafec91ffc9e3a1f448fbd269a9bfa`.
