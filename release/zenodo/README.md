# Zenodo release workflow

This repository uses a manual GitHub Actions workflow for Zenodo deposits:

- Workflow: `.github/workflows/zenodo_release.yml`
- CLI helper: `tools/zenodo_publish.py`
- Metadata: `release/zenodo/metadata_v4_7_0.json`

## Secret

The production Zenodo token must be stored as a repository secret named:

```text
ZENODO_TOKEN
```

For sandbox tests, optionally store:

```text
ZENODO_SANDBOX_TOKEN
```

Tokens must never be committed to the repository.

## Running the workflow

Open GitHub Actions and run `Zenodo Release` manually.

Recommended first run:

```text
environment: sandbox
dry_run: true
publish: false
confirm_publish: false
metadata: release/zenodo/metadata_v4_7_0.json
files_glob: release/v4.7.0/*
```

Production draft upload without publishing:

```text
environment: production
dry_run: false
publish: false
confirm_publish: false
```

Production publish requires both:

```text
publish: true
confirm_publish: true
```

## File layout

Place final upload files in:

```text
release/v4.7.0/
```

Expected files for v4.7.0:

```text
Quantum_Sphaera_Companion_v4_7_0.pdf
Quantum_Sphaera_Companion_v4_7_0_source.tex
Quantum_Sphaera_Companion_v4_7_0_RC19_concept_doi_restore_packet.zip
```

The workflow does not build the PDF. It only validates metadata/files and performs the Zenodo API actions.

## Release policy

Work may happen directly on `main`. Published releases should be frozen with annotated Git tags, e.g.

```bash
git tag -a v4.7.0 -m "Quantum Sphaera Companion v4.7.0 public release"
git push origin v4.7.0
```
