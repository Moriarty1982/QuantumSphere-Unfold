# English-only publication candidate

Author instruction: only the English texts are to be uploaded. The German
reader edition and German narrative review notes are excluded. The database
is retained as machine-readable evidence, not as another reader edition.

## Exact source

- Main revision: `802c7af9e672f138461ffb112b0fcd43b7b79c58`.
- GitHub paired build: 43087358029, successful. Lean, TeX, Linux/Windows
  batch checks and Wiki Sync on the same revision also succeeded.
- Shared snapshot: `63250fead33996bf0ad45483d8d5856c71648df6d202431fcab201c7bbf1e212`.
- English full PDF: 1401 pages; English physics PDF: 27 pages.

The authentic bundle was downloaded and all 111 original checksums checked.
Both document logs have zero undefined references, duplicate labels,
rerun requests and overfull boxes. Both still retain open argument review.

## Candidate files

The local candidate is `build/v5-english-upload-verified/`:

- `Quantum_Sphaera_Companion_v5_0_0_draft_full.pdf`
- `Quantum_Sphaera_Companion_v5_0_0_draft_physics.pdf`
- `Quantum_Sphaera_v5_0_0_draft_english_sources.zip`
- `qam.sqlite3`
- `build-manifest.json`, `package-manifest.json`, `README.md`, `SHA256SUMS.txt`

The source ZIP has 86 entries. It includes both exported LaTeX entrypoints,
their resources, assembly records, retained machine evidence and selected
provenance code. German Markdown reports, German translation templates,
the German reader PDF and compiler logs are not selected. Assembly records
can retain the identities of omitted historical source reports. Consult
the original repository revision for those reports and for the complete
application code required to regenerate the database, rather than merely
compile the exported documents. The English archive README explains this
boundary; this is not a whole-repository archive.

## Reproduction

```powershell
gh run download 43087358029 --dir build/v5-main-43087358029
python -m qam.tools.package_v5_documents --bundle build/v5-main-43087358029/qsc-v5-paired-documents-6 --out build/v5-english-upload-verified --expected-commit 802c7af9e672f138461ffb112b0fcd43b7b79c58
python tools/zenodo_publish.py --metadata release/zenodo/metadata_v5_0_0_draft.json --files "build/v5-english-upload-verified/*" --environment production --new-version-of 24108818 --default-preview Quantum_Sphaera_Companion_v5_0_0_draft_full.pdf --dry-run
```

Use new output directories: the packaging tool refuses overwriting an
existing target. The helper dry run is local; it does not establish
server-side acceptance of metadata or files.

## Checks actually performed

- Exact input file coverage and checksums, clean source commit, document
  findings, per-edition source bindings and common snapshot checked.
- Database opened read-only; SQLite integrity check passed and both
  edition hashes point to the declared snapshot in the stored table.
- ZIP CRC and byte identity of every selected source checked; German
  translation paths and narrative Markdown notes excluded.
- Both documents compiled successfully directly from the extracted ZIP
  using the local LaTeX system. All four log findings are zero for both.
  This validates source completeness, not byte-identical cross-platform PDFs.
- A deliberately altered checksummed file was rejected before any output
  directory was created. No altered test artifact entered the payload.
- Repeated package creation produced the same source ZIP checksum.
- The two title pages and physics pages 12,14–16 of the exact container PDFs
  were rendered and inspected. No clipping or overlap observed. Earlier
  bounded layout reviews remain applicable to unchanged source regions;
  this is not a fresh visual review of all 1401 Companion pages.
- Complete eight-file candidate passed the local upload-helper dry run,
  with the full English PDF explicitly selected as preview.

The retained machine-readable inventory and checks are in
`ENGLISH_PAYLOAD_VALIDATION.json`. No DOI was reserved and no Zenodo files
were uploaded or published by this preparation. The candidate still says
draft: after DOI reservation and release title-page updates, regenerate
the final PDFs, source archive, manifests and dry run. Never relabel this
draft package silently as final. Public citation remains v4.11.0.
