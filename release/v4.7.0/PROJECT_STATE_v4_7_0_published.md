# Quantum Sphaera Companion v4.7.0 — published state

Status: published/public on Zenodo.

## Public record

- Zenodo record: https://zenodo.org/records/20232911
- Version: v4.7.0
- Version DOI: 10.5281/zenodo.20232911
- Concept DOI: 10.5281/zenodo.19210728
- Previous/baseline DOI: 10.5281/zenodo.20117361
- Expired prior reserved DOI: 10.5281/zenodo.20181842 — do not use as final DOI
- Published date: 2026-05-17
- Title: Quantum Sphaera Companion: A Structure-First Mathematical Unfolding
- Author: Marc Brendecke

## Authoritative candidate/source

The authoritative release candidate/source for the published v4.7.0 record is:

```text
v4.7.0-RC19 concept DOI restore
```

RC19 restored the Concept DOI on the title page and metadata while retaining the Version DOI and guarded claim scope.

## Published file set visible on Zenodo

```text
Quantum_Sphaera_Companion_v4_7_0 (4).pdf
Quantum_Sphaera_Companion_v4_7_0_RC19_concept_doi_restore_packet.zip
Quantum_Sphaera_Companion_v4_7_0_source (1).tex
```

## Scope guard

Allowed claims are guarded local/restricted/effective only, including:

- local/restricted downstream chain;
- conservative C4 relative-seam neutralization;
- C5 detector-threshold terminality at theta = 1/256 after n = 20;
- local photon-clock selector preservation under Delta_gamma < 1/5;
- local typed mixed-comparison control;
- terminal-data bridge and restricted terminal-data naturality;
- matter-frame epsilon terminality and tachyon-frame signed-scale separation;
- terminal blocker freeze distinguishing terminal-data zero from exact all-readout zero.

Forbidden claims remain:

- exact finite C5 zero closure;
- exact all-readout terminality;
- C6/T2 closure;
- global photon-clock/RH theorem;
- global all-readout closure.

## GitHub release workflow status

The repository contains a manual Zenodo workflow:

```text
.github/workflows/zenodo_release.yml
```

and CLI helper:

```text
tools/zenodo_publish.py
```

The production secret name is:

```text
ZENODO_TOKEN
```

Optional sandbox secret:

```text
ZENODO_SANDBOX_TOKEN
```

The workflow is manual-only via workflow_dispatch and should not publish on push.

## Repository file staging note

Large release files are not automatically committed by this state checkpoint. If needed for workflow upload tests, place final upload files in:

```text
release/v4.7.0/
```

Expected names:

```text
Quantum_Sphaera_Companion_v4_7_0.pdf
Quantum_Sphaera_Companion_v4_7_0_source.tex
Quantum_Sphaera_Companion_v4_7_0_RC19_concept_doi_restore_packet.zip
```

