# Version 5 release preparation, 12 November 2026

The author requested commit, merge and push of the research state, followed
by a v5 Zenodo edition retaining the open string-relaxation question.
Research PR #100 was merged as e3a3d7e6b7fb44d3719c45abfa0b9802d5f89fa1.
The paired main build 43163957197 and Wiki Sync succeeded.

Zenodo reservation run 43164056602 created draft 24152615, version DOI
10.5281/zenodo.24152615. It is NOT published. The predecessor record
24108818 was checked through the public API and is v4.11.0 under concept
DOI 10.5281/zenodo.19210728. Reuse deposition_id=24152615 for every later
action; do not create another new version.

Both English documents now record the analytical comparison of fixed
outer length, optional de Sitter identification, tensile relaxation,
dissipation and remaining physical obligations. No scientific guard,
proof status or open problem is promoted by the release preparation.
The new source section is additional; historical rounds are unchanged.

The final payload must come from a successful clean paired build after
these edits, with the exact commit recorded. The candidate workflow
retrieves only that successful paired-build artifact, checks its commit,
checksums, edition bindings and database integrity, and packages the two
English PDFs and sources before invoking the existing Zenodo helper.
The full Companion is explicitly selected as preview. Publication remains
a separate final action after inspection of the concrete uploaded draft.

The earlier English-only source archive choice is retained. The separate
German reader edition is not in the payload. Public citation stays at
v4.11.0 until Zenodo confirms publication. Build flags recording incomplete
argument review are retained; technical validity does not certify physics.

## Concrete candidate validation

Source commit 539b75bfce29ce20bb9aa7e59c251727b49faa45 was built successfully
in paired run 43197984602. Full edition: 1402 pages; physics edition: 28.
All four log findings are zero in both documents. 113 input checksums,
88 archive entries and SQLite integrity checked. Local complete Zenodo
helper dry run passed. Both titles contain the version and concept DOI
exactly once and no predecessor DOI. Visual inspection of full pages
1,170,171 and physics pages 1,25,26 found no clipping or overlap; this is
not a new visual review of all historical pages. Exact hashes are in
RELEASE_VALIDATION_2026_11_12.json. The four PR checks (Lean, TeX, Linux,
Windows) passed on the candidate source commit.

Later changes to the upload workflow and this report do not alter that
frozen manuscript or its package. The upload uses the exact source build,
not an unverified recompiled or renamed draft PDF.
