# v4.9.0 Research Candidate

Date: 2026-10-18. Unreleased draft, not a publication or DOI assignment.
Public citation metadata and release/v4.7.0 and release/v4.8.0 are unchanged.

## Adopted Main-Text Changes

The existing `sources/research/v480-companion.tex` entry now includes
`parts/cartan-normal-source.tex`, after the real-action/geometry section
and before inherited field claims. Its historical filename is retained so
the full-origin audit and build route remain valid. Working title/PDF
metadata identify 4.9.0-draft; inherited docversion remains 4.7.0.

The new section includes:

- The explicitly assumed neutral odd-cross Cartan action, independent
  fields, declared comparison matrices and residual/density conventions.
- Coordinate and Lorentz identities with their full probe and
  constitutive residual sources after compatible Cartan elimination.
- A conditional gravitational constraint-propagation proposition and
  energy argument, requiring the full probe/constitutive equations on an
  open region, trace-reversed spatial evolution and boundary assumptions.
- The finite rank-40 normal inverse, with 28 left compatibility rows and
  the exhibited 10+6 kernel split; exact linear-algebra proof conditional
  on its rank/span hypotheses, distinguished from numerical evidence.
- The conditional source law for compatible prescribed tangential jets,
  its proof, explicit 464/736 mask and pointwise numerical gate evidence.
- Actual-field residual controls, the failed frozen-highest next-order
  control, provenance and the unresolved higher/spatial/regional duties.

This adopts a bounded synthesis, not all intervening analysis notes.
No native Einstein emergence, physical coupling/scale, frame assignment,
full gauge classification, regional existence or OP5 closure is asserted.
No theorem is replaced by a parser token or by a test count.

## Source Evidence

The numerical inputs and scripts remain at commit 8215320, with matching
fingerprints. Primary working notes are
`HC_Cross_Cartan_Parent.md`,
`HC_Cartan_Diffeomorphism_Residual_Identity.md`,
`HC_Cartan_Lorentz_Residual_Identity.md`,
`HC_Cartan_Gravitational_Subsidiary.md`,
`HC_Cartan_Normal_Source_Reduction.md`,
`HC_Cartan_Normal_Source_Compatibility.md` and their derivations, plus
`HC_Cartan_Source_Cauchy_Jet_Mask.md` and
`HC_Cartan_Next_Joint_Completion.md` for the later control.

The older `HC_Probe_Law_Revision_Audit.json` has only its entrypoint
provenance hash and shifted anchor line numbers refreshed for the added
include. Its inherited source records, numerical controls and historical
claim status are unchanged. The corresponding 51 focused tests pass.
The dependent fingerprint of that report in
`HC_Cartan_Joint_Cartan_Regularity.json` was also refreshed, without changing
any coefficient, numerical estimate or regularity claim.

## Release Boundary

The candidate still requires a deliberate release decision, final payload
and metadata preparation before publication. CITATION.cff continues to
identify the published v4.8.0. No upload, tag, DOI reservation or release
directory is created by this integration. A rebuilt local PDF is a preview,
not a published version.

## Build and Length Audit

The main PDF was rebuilt in place at
`build/v480-reading-audit/v480-companion.pdf`; its title and PDF metadata
identify v4.9.0-draft. The existing entry filename is intentionally unchanged.
The built-in compiler was attempted, but its XeTeX backend rejects the
inherited pdfTeX-specific `pdfcompresslevel`. The local MiKTeX pdfLaTeX build
then completed with package installation and shell escape disabled. A final
run exited successfully with settled references and no undefined citations,
undefined references, duplicate destinations or remaining TeX errors.

| Scope | Previous working PDF | New research candidate | Change |
| --- | ---: | ---: | ---: |
| Main text and frontmatter | 153 | 160 | +7 |
| Appendices and bibliography | 884 | 884 | 0 |
| Total | 1037 | 1044 | +7 |

This is a comparison of the successive full-source research working PDFs,
not of the published v4.8.0 release PDF. The independently rebuilt origin
still matches the published v4.7.0 count of 1014 pages. Machine-readable
current metrics are in `V490_Full_Monolith_Metrics.json`; the previous
`V480_Full_Monolith_Metrics.json` is retained as the earlier measurement.

All 38 inherited fragments and 3,403,614 original bytes remain preserved;
all 3290 inherited label occurrences remain present, with no new duplicates.
There are now 53 uniquely included source files. The 58 inherited overfull
boxes remain; no new overfull box occurs in the added section. This is not
a warning-free retypesetting of all 1044 pages. The title and added-section
pages 43--47 were rendered and visually reviewed for layout and legibility.

## Test Record

Eight new integration checks pass, as do all 34 full-monolith tests.
Two complete 2161-test runs were executed. The first found the outdated
entrypoint provenance record; the second passed 2160 tests and found only
its dependent saved fingerprint in the Cartan regularity report. After
refreshing that fingerprint, all 101 targeted tests passed: 8 regularity,
51 probe-law/provenance, 8 new integration and 34 full-monolith checks.
The subsequent complete run after both repairs passed all 2161 tests in
278.176 seconds. All 34 separate OP5 checks also passed (2195 total).
Preservation, settled page metrics and whitespace checks pass. The final
version review confirms unchanged release payloads, CITATION.cff and
.zenodo.json, and current PDF/source page metrics. These checks do not establish
the open mathematical obligations stated in the main text.

Changes are saved locally; this integration has not been committed or pushed.

## Acceptance Status

| Item | Current status |
| --- | --- |
| Main-text adoption | Section 9 included once, before inherited field claims |
| Mathematical claim scope | Three conditional propositions with proofs; finite ranks explicitly numerical |
| Working version | 4.9.0-draft in title and PDF metadata; historical entry filename retained |
| Source preservation | 38 origin fragments and all 3290 inherited labels retained |
| PDF and length | Current settled 1044-page preview; +7 versus previous working PDF |
| Layout | New pages and title visually reviewed; 58 inherited overfull boxes remain |
| Public baseline | Release payloads, CITATION.cff and .zenodo.json unchanged |
| Publication | Not performed; final release payload, metadata and explicit release decision pending |
| Commit and push | Not performed for this integration |

The outstanding surface compatibility, higher-order re-preparation, coupled
PDE existence and native/physical identification are research obligations,
not hidden results of this editorial pass. A publication restricted to the
stated conditional comparison results does not require claiming these
questions solved. It must keep these limits visible and must not describe
this candidate as a completed OP5 or unified-field proof.
