# Preparation checks — 11 November 2026

The existing local helper was run with draft metadata and the two actual
PDFs from successful container run 43078619869. It completed successfully
in `--dry-run` mode. This is local validation, not acceptance by Zenodo's
server and not validation of a complete final release payload.

```powershell
python tools/zenodo_publish.py --metadata release/zenodo/metadata_v5_0_0_draft.json --files build/v5-layout-ci-43078619869/qsc-v5-paired-documents-3/Quantum_Sphaera_Companion_v5_0_0_draft_full.pdf build/v5-layout-ci-43078619869/qsc-v5-paired-documents-3/Quantum_Sphaera_Companion_v5_0_0_draft_physics.pdf --environment production --new-version-of 24108818 --default-preview Quantum_Sphaera_Companion_v5_0_0_draft_full.pdf --dry-run
```

| Input | Size (bytes) | SHA-256 |
|---|---:|---|
| Full draft PDF | 19837278 | b845f482050c06039e493402f7e0a7aaa25a9e32114014b7ebd5e456e092d540 |
| Physics draft PDF | 375711 | 6244e02c21c0ce05cfc5c07fc819afd56296740da83a0cfbc90e6d5130136510 |

Both PDFs were found; the full draft was explicitly selected as preview.
No token, DOI reservation, draft creation, file upload or publication was
needed. The final source archive, final document version, actual date and
reserved DOI are not present in this check. It must not be reused as a
final payload acceptance result. `CITATION.cff` and published release files
remain unchanged.
