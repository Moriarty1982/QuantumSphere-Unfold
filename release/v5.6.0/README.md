# Quantum Sphaera Companion v5.6.0 — DOI RESERVED (draft unpublished)

**Reserved on 28 November 2026 with the author's approval:** Zenodo draft 24632437, version DOI 10.5281/zenodo.24632437 (workflow "Zenodo Release", run 46166760238, new version of 24563811). From now on use `deposition_id=24632437`, never `new_version_of`. Nothing uploaded; upload and publication need the author's approval. DOI stamped in `qam/editions/v5_release.json`, the metadata description, `.zenodo.json`, `CITATION.cff`, `working-preamble.tex`, `DOI_ROLES` in `tools/qs.py` and `AGENTS.md`. The German preprint 0.5.0 references this version (author decision of 28 November 2026), so v5.6.0 is published before or together with it.

Status (28 November 2026): release files prepared on branch and PR. No Zenodo step has been taken. Reservation, upload and
publication each need the author's explicit approval (`AGENTS.md`), and so does the decision that this version appears.

- Target version: v5.6.0 (full Companion and physics paper, one package).
- Version DOI: to be reserved (use `new_version_of=24563811` only for the reservation, afterwards `deposition_id`).
- Concept DOI: https://doi.org/10.5281/zenodo.19210728
- Predecessor: v5.5.0, DOI 10.5281/zenodo.24563811, record https://zenodo.org/records/24563811 (published 26 November 2026).
- Metadata draft: `release/zenodo/metadata_v5_6_0.json` (publication date provisional, 2026-11-28).
- Prepared together with the German preprint 0.5.0 (`release/preprint-de-v0.5.0/README.md`).

## What is new

- Full Companion: research layers v4.10.0-r69 to r75.
  - r69: naming convention for frames and lepton sectors (author decision of 26 November 2026).
  - r70: port weights against amplitudes, the compensator on the state sphere, correction to r69.4 (exploration k382); r71:
    Friedman coincidence scan (diagnostic tool, k419).
  - r72: restatement of the photon-clock guard.
  - r73: the common lepton offset is an angle φ; scale-free branch choice, sign set by the author; φ = 0.0395773 stays measured;
    lepton mass balance (H213–H227).
  - r74 (new): H228–H236 and exploration k449; every further route to φ refuted or without a hit; H236 clarifies a double
    counting (φ carries the offset, q only the sign; no verdict changes; H227 predictions unaffected); author decision of
    28 November 2026: φ stays open, the strand rests.
  - r75 (new): dated register of the model state and its predictions for v5.6.0 (as of 28 November 2026), with derived / set /
    measured / post hoc for every entry, and the author's version rule.
- Physics paper: new subsection "The lepton phase: an angle, a branch and one measured number" (masses part, r69–r74) and new
  section "Predictions of this version (as of 28 November 2026)" (limits part, r75); one sentence in the main limits text.
- Research catalogue: eight entries appended to `qam/editions/v5_research_notes.json` (69 in total).
- `AGENTS.md`: standing rule of the author of 28 November 2026 "Vorhersagen je Version".

## Predictions of this version (summary of r75)

| Quantity | Prediction | Source | Rests on |
|---|---|---|---|
| mass ordering | normal | H227, H213 | φ measured; branch sign and Brannen form set |
| Σm_ν | 59.30 ± 0.24 meV | H227 | φ measured, μ_ν fitted; K = 2/3 postulate |
| m₁, m₂, m₃ | 0.379 / 8.81 / 50.11 meV | H227 | as Σm_ν |
| m_β | 8.87 ± 0.04 meV | H227 | as Σm_ν; mixing data measured |
| m_ββ | 1.3 to 4.0 meV | H227 | as m_β; Majorana phases free |
| R = Δm²₂₁/Δm²₃₁ | 0.030839 (not blind) | H99, H100 | φ measured; H99 set |
| sin²θ₁₂ | 0.3086 (H9, post hoc) / 0.3019 (H176) / 0.318–0.3195 (H206–H208) | exclusive readings | JUNO decides |
| θ₁₂–CP correlation | sin²θ₁₂ ≳ 0.315 with \|sin δ\| ≈ 1, or ≈ 0.304 with \|sin δ\| ≈ 0.65 | H208 (post hoc) | JUNO + DUNE |
| sin²θ₂₃, sin²θ₁₃, δ_CP | 0.4954, 0.0223, ±77.7° with sin δ < 0 | H176, H207, H125 | β_sym from the postulate; readouts set |
| Ω_m | β_sym² = 0.30185 | H96 | postulate; identification post hoc |
| m_W | 80.3615 ± 0.0018 GeV | H15 | γ_L from the postulate; identification post hoc |
| m_τ | 1776.969 MeV (Koide) vs 1777.134 MeV (H102) | r63, H227, H102 | K = 2/3 postulate |

Inputs: φ = 0.0395773 measured; branch sign a setting; β_sym = 0.5494056410 from the counting postulate (r67), not derived;
K = 2/3 under the postulate of equal standing of the frames; Brannen form and H99 set; scales μ_e, μ_ν fitted; q → 0⁻ (H236).
The binding table is layer r75; this summary does not replace it.

## Validation done in the preparation

Only what was actually run, in the cloud container (no pdflatex available).

- `python -m pytest qam/store/test_editions.py -q`: 3 passed (after replacing four commands in the prediction table of the
  physics edition that the edition scrubber did not know).
- Research catalogue: 69 notes registered by `configure_v5_editions` (subagent run); every excerpt occurs exactly once.
- `python tools/qs.py guards` on the new layers r74 and r75: 0 candidates.
- Reservation dry run (`tools/zenodo_publish.py ... --new-version-of 24563811 --reserve-only --dry-run`): metadata validated, no
  Zenodo API call.
- Not done: LaTeX build (runs as check "paired-documents" on the PR), `tools/qs.py doi`, any Zenodo step, DOI stamping
  (`qam/editions/v5_release.json`, `.zenodo.json`, `CITATION.cff`, `working-preamble.tex`, `DOI_ROLES`), no visual check of PDFs.

## Scope

This minor version changes content, not the status of the open physical questions. OP1 to OP5, C5 and C6/T2 remain open. The
counting rule and the equal standing of the frames are postulates. φ is a measured input, the branch sign a setting. No prediction
is decided by data. No guard is closed by the release.

## Next steps needing the author's approval

1. Merge of this preparation (standing rule: merge when CI is green).
2. Reservation of the version DOI (draft as new version of 24563811).
3. DOI stamping as in `.github/ISSUE_TEMPLATE/release-4-doi.yml`, rebuild, `tools/qs.py doi` on both PDFs.
4. Paired build, upload with `replace_files=true` and `default_preview` set to the full PDF; check of the draft and its preview.
5. Publication (`publish=true`, `confirm_publish=true`) with the final date; preview check afterwards (`zenodo-fix-preview.yml`).
6. Tag `v5.6.0` and GitHub release by the author on the local machine; afterwards issues, wiki and DOI discipline in `AGENTS.md`.
