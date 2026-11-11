# Version 5 publication preparation

This directory contains reviewable publication text, not a release payload.
No v5 DOI, publication date, tag, reservation or upload has been created.
Public citation remains v4.11.0. `CITATION.cff` is intentionally unchanged.

## Record and document plan

One new version of the existing Companion record is planned. It will
contain both the full Companion and the English physics paper, generated
from the same frozen snapshot. They are complementary editions of the
same release package. The record's version DOI will identify the package;
citations should additionally name the chosen document and its section.
The concept DOI remains 10.5281/zenodo.19210728. A separate independent
physics-paper record and DOI are not part of this plan.

This follows Zenodo's record model: a record can contain multiple files
and receives a DOI. Replacing files requires a new record version.
Official references, checked 11 November 2026:
[About records](https://help.zenodo.org/docs/deposit/about-records/),
[Manage versions](https://help.zenodo.org/docs/deposit/manage-versions/).

The main record title retains the Companion name and identifies the two
editions. The physics PDF retains its own article title. The German
reader edition is an additional reading aid and is not automatically
included in this two-document plan.

## Metadata and package preparation

`../zenodo/metadata_v5_0_0_draft.json` is locally valid draft metadata.
Its version and preparation paragraph deliberately mark it as unfinished.
Before a real upload, create final metadata with version v5.0.0, the actual
publication date, and the reserved version DOI in the appropriate fields.
Replace the preparation paragraph with the final package description;
retain the scientific scope and review limitations.

Planned final package contents, still to be assembled and checked:

- Full Companion PDF, selected English physics PDF.
- Source archive with both entrypoints, all required resources and assembly
  records, together with the documented database snapshot and evidence.
- A package README explaining the two entrypoints, source snapshot,
  assumptions, unresolved guards and reproducibility commands.
- A checksum manifest of the actual final files, not the preparation text.

The current builder already produces a shared draft bundle; no draft PDF
is relabelled as final here. Final filenames and the default preview must
be fixed before the real upload. Use the full Companion as the proposed
preview, matching the record title. The upload helper must receive that
exact PDF filename through `--default-preview`.

## Remaining sequence

1. Obtain merge approval for the open CI, layout and review/preparation PRs;
   merge in dependency order and recheck each retargeted diff.
2. The self-review's local precision notes have been addressed in both languages
   and locally rebuilt; see the dated precision follow-up in notes/research.
   Open research claims must remain qualified; they need not become solved
   merely to publish an honestly scoped preprint.
3. Freeze the selected release revision. Reserve a DOI only after explicit
   authorization, update both title pages and final metadata, then build
   and check the concrete two-document release payload.
4. Run the helper's local dry run with exactly that payload and preview.
5. Upload only after explicit authorization; inspect the actual draft files,
   metadata and preview. Publish only after explicit final authorization.
6. Update public citation, release notes and repository baseline only in
   accordance with the completed release stage.

See `../../notes/anleitungen/zenodo-release.md` and the scoped self-review
under `../../notes/research/referee/v5-physics-2026-11-11-pass1/`.
