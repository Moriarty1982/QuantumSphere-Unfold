# v4.7.0-RC20 Citation Repair Audit

RC20 carries the r85 source repairs: two misdirected citation targets and one scope
separation inside the central unity theorem. No mathematical content is added and no
claim scope is widened. Both repairs narrow what is asserted.

## Repairs

| Item | Before | After |
|---|---|---|
| Proof of Theorem "Unity of the Sphaera" | `brendecke2026rh`, Theorem 3.2 | Lemma 13.2, Step 3 |
| GUE universality argument | `brendecke2026rh`, Theorem 3.2 | Proposition 13.1 and Lemma 13.2, Step 3 |
| Unity theorem item (vi), gauge group | inside the unitary-equivalence list | separate consequence, equivalence not asserted |

Theorem 3.2 of the cited source is the functional equation. The adelic Stone--von Neumann
application is Step 3 in the proof of Lemma 13.2, resting on Proposition 13.1. The numbering
is confirmed internally: three passages of the Companion cite Theorem 3.3 for the
Guinand--Weil explicit formula, the entry immediately following Theorem 3.2.

A full cross-reference sweep of all `brendecke2026rh` and `brendecke2026main` citations
carrying a number found no further mismatch: 9 numbered references resolve to the correct
type and number, 7 further references are symbolic (T1+T3, T4+T5, T6) and resolve to
Theorem 9.2, Theorem 10.1 and Theorem 14.1 respectively.

## DOI records

- Version DOI: `10.5281/zenodo.20232911`
- Concept DOI: `10.5281/zenodo.19210728`
- Previous/baseline DOI: `10.5281/zenodo.20117361`
- Expired prior reserved DOI: `10.5281/zenodo.20181842` (absent from the PDF)

No new DOI is requested by RC20. The reserved v4.7.0 Version DOI is unchanged.

## Compile audit

Toolchain: MiKTeX 25.12, pdfLaTeX, three passes.

| Check | RC19 | RC20 | Result |
|---|---:|---:|---|
| PDF pages | 1014 | 1016 | +2 (r85 section) |
| LaTeX passes | 3 | 3 | equal |
| LaTeX errors | 0 | 0 | ok |
| Undefined refs / citations | 0 / 0 | 0 / 0 | ok |
| Duplicate-label warnings | 0 | 0 | ok |
| Rerun warnings | 0 | 0 | ok |
| Labels total | 3290 | 3296 | +6 (the six r85 labels) |
| Overfull hbox warnings | 58 | 58 | unchanged |
| Title-page visible Version DOI lines | 1 | 1 | ok |
| Title-page visible Concept DOI lines | 1 | 1 | ok |
| PDF Version DOI hits | 4 | 5 | +1 (r85 source-only clause) |
| PDF Concept DOI hits | 9 | 9 | unchanged |
| PDF previous/baseline DOI hits | 14 | 15 | +1 (r85 source-only clause) |
| Expired DOI hits in PDF | 0 | 0 | ok |

The RC19 column was produced by rebuilding the frozen RC19 snapshot with the same
toolchain, not copied from the RC19 report. Rebuilt that way, RC19 reproduces its
documented page count (1014) and label count (3290) exactly.

**Overfull count caveat.** The original RC19 report records 45 overfull hbox warnings.
The same source rebuilt under MiKTeX 25.12 yields 58. The difference is a toolchain effect,
not a regression: RC19 and RC20 both yield 58 under the present toolchain, so the r85
changes introduce no new overfull box. The overfull count is therefore not a portable
baseline value and must be compared within one toolchain only.

## Guard state

Unchanged by RC20:

```
R_glob^(r85,+)   = (0,1,1,1,1)
Gamma_guard^r85  = (1,1,1,1,1)
R_eff/local^r85  = (0,0,0,0,0)
R_exact/global^r85 = (1,1,1,1,1)
```

The release scope is unchanged: guarded effective/local and frame-typed closures, not exact
global closure. RC20 does not claim exact finite C5 zero closure, exact all-readout
terminality, C6/T2 closure, a global photon-clock/RH theorem, or global all-readout closure.

## Divergence note

The unity theorem also appears in the main paper `brendecke2026main`
(DOI `10.5281/zenodo.19210213`), where item (vi) is not modified. The two documents differ
in that scope sentence until the main paper is revised. The Companion carries the narrower
and correct scope.

## Release status

Public upload/release was not performed and is not authorized by RC20. The PDF is named
`Quantum_Sphaera_Companion_v4_7_0_r85.pdf`; on an actual release it would be renamed to the
release filename. The RC19 artefacts are retained unchanged as provenance.
