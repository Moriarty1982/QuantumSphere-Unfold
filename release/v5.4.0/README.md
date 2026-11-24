# Quantum Sphaera Companion v5.4.0

Published on Zenodo on 24 November 2026.

- Version DOI: https://doi.org/10.5281/zenodo.24500009
- Record and deposited files: https://zenodo.org/records/24500009
- Reservation run: 45392337901 (dry run 45386101739; two earlier attempts, 45386155010 and 45387496233, were refused by
  Zenodo with HTTP 403 "unusual traffic" before anything was created).
- Concept DOI: https://doi.org/10.5281/zenodo.19210728
- Predecessor: v5.3.0, DOI 10.5281/zenodo.24434403.
- Frozen source commit and tag target: 122eb34315a7870106a3e7a8d8fcbf74c438449d.

## What is new

- Full Companion: research layers v4.10.0-r31 to r59. Most of them are explorations, not blind tests; the pre-registered
  tests are recorded as such and marked as not blind where their outcome was foreseeable. Topics: the orientation of the
  octant step as a time orientation and the Holst term (r31); a worked OP5 case with an assumed, not derived source
  identification (r32 to r35); candidate mediators of the directed channel and an audit of that chain (r36 to r45); frame,
  axis and time orientation as readout data (r46 to r51, r54); the frame map JB on the area operator (r52); counting rules as
  a dimension formula (r53); how the open problems hang together (r55); Lambda as an input within a named class of
  constructions of the record (r56); a feedback cascade compared with DESI DR2 BAO, not excluded but worse than LambdaCDM
  (r57); a temporally ordered octant readout (r58); the handedness series and the Hilbert-shift tower, collecting k245 to k274
  and H125/H126 (r59).
- Physics paper: the worked OP5 case in the geometry part; additions to the limits section from r52 to r58; one paragraph on
  the handedness series (r59) in the masses part.
- Research catalogue: four new entries in `qam/editions/v5_research_notes.json`.
- Layout only: two over-wide display lines in r38 and r46 were broken; their content is unchanged.

## Validation

- Local paired build (TeX Live, container): full Companion 1537 pages, physics edition 36 pages; zero undefined references,
  multiply defined labels, rerun requests and overfull boxes. `tools/qs.py doi` on both PDFs: compact title page rule and
  DOI separation hold.
- The first candidate run (45393309870) stopped at the package check because the full edition had two overfull boxes; fixed
  in commit 122eb343.
- GitHub paired build 45393851967 of commit 122eb343.
- Package dry run 45394201291 against draft 24500009: metadata validated, no Zenodo mutation.
- Upload 45394362273 into draft 24500009, with verification: unpublished draft, DOI and version correct, files with MD5
  equal to the package, default preview `Quantum_Sphaera_Companion_v5_4_0_full.pdf`.
- Publication run 45394967543 on the author's approval ("wenn es dann klappt, darfst du sofort selbst veröffentlichen").
- After publication the record showed `build-manifest.json` as preview: the publication run uploads the files again, which
  cleared the preview set in the draft. Fixed on the author's approval by a metadata-only edit (run 45397571661,
  `zenodo-fix-preview.yml`): `default_preview` is now `Quantum_Sphaera_Companion_v5_4_0_full.pdf`; files, DOI and version
  unchanged. Since PR #288 `tools/zenodo_publish.py` sets the preview after every upload.
- GitHub release: `preprint-de-v0.3.0` was created by `github-release.yml`; `v5.4.0` was refused for the Actions token
  ("Resource not accessible by integration") and is created by the author.

## Scope

This minor version changes content, not the status of the open physical questions. OP1 to OP5, C5 and C6/T2 remain open; the
orientation of the octant step, the counting rule per frame and the source identification of the OP5 case are not derived.
No guard is closed by the release. Database records and hashes do not prove physical interpretation.
