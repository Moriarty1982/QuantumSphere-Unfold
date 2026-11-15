# Quantum Sphaera Companion v5.1.0

Published on Zenodo on 15 November 2026.

- Version DOI: https://doi.org/10.5281/zenodo.24237112
- Record and eight deposited files: https://zenodo.org/records/24237112
- Concept DOI: https://doi.org/10.5281/zenodo.19210728
- Predecessor: v5.0.0, DOI 10.5281/zenodo.24152615.
- Frozen source commit and tag target: dfdb41387264e728a13a9a51a8636fd532011ff2.
- Paired document build: 43662217359; upload: 43663052541; reservation: 43661985497.

The two English editions share one source snapshot. The full Companion has 1412 pages; the physics edition has 29.

## What is new

- Full Companion: research layers v4.10.0-r12 to r14 and the counterterm registry. Layer r14 records the explorations of
  14 and 15 November 2026: the slot Fourier construction and its limits, the search for a source of the balanced
  Koide reference, a colour- and charge-preserving map between the sedenion and the Dixon carriers, the bent-octant
  reading of the charged-lepton phase and the flux-free guarded core, with two corrections made during the work.
- Physics paper: a short paragraph and a development subsection (5.7) on the bent octant. For three states with
  pairwise overlap one half the Koide value holds for every Bargmann phase, and det G = (√2 cos φ − 1)/2 separates
  the flat octant from three positive masses. The geometric reading as a flux-free core is stated with its status;
  the borrowed term "reflector" (from the Enigma cipher machine) is explained. A remark in the outlook notes the
  conditional tau-mass value of H102 and its placeholder basis. One sentence in section 4 notes that colour and
  charge alone do not separate generation and spin.
- Tooling: the v5 build, package and Zenodo candidate workflow read version, DOI and file names from
  `qam/editions/v5_release.json` instead of fixed v5.0.0 values.

## Validation

- Paired build of commit dfdb413: both documents with zero undefined references, multiply defined labels, rerun
  requests and overfull boxes; build manifest without tracked changes.
- Both title pages carry the version DOI 10.5281/zenodo.24237112 and the concept DOI exactly once and no predecessor
  DOI (`tools/qs.py doi`). New pages inspected visually: physics pages 1, 13, 17, 18, 23; full pages 1, 1405, 1406.
- Edition tests (`qam.store.test_editions`) passed locally.
- The upload run verified the unpublished draft, the DOI, the version and all eight checksums; its preview check
  failed because the helper does not set the preview explicitly. The author set the preview on Zenodo and published
  the record. After publication the public record was checked: eight files with MD5 equal to the uploaded package,
  default preview `Quantum_Sphaera_Companion_v5_1_0_full.pdf`, version v5.1.0, date 2026-11-15, relation
  "is new version of" v5.0.0.

## Scope

This minor version changes content, not the status of the open physical questions. The Koide overlap, the size of
the core and the counting rule per frame remain open. No guard or open problem is closed by the release. Database
records and hashes do not prove physical interpretation.
