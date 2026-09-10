# v4.7.0-RC21 C5 Collar Consolidation Audit

RC21 carries the r86 layer, which executes branch Q5 of the r48 queue: consolidation of the
C5 asymptotic-collar bookkeeping. It supersedes RC20 (r85 citation repair), which is retained
unchanged as provenance.

## Content of r86

r86 produces no new mathematical result. It collects the C5 collar data spread over r04--r13
and the compressed r55--r80 chain, writes down the threshold function whose single value was
already recorded, and corrects a classification.

**Threshold function.** The detector stage was recorded only at the point `theta = 1/256`,
`n = 20`. The underlying function is

```
n_min(theta) = ceil( log_{4/3}(1/theta) )
```

verified in exact rational arithmetic against brute-force search over 40 thresholds, with no
deviation. For `theta = 1/256` it yields 20, matching the inherited r63--r64 detector stage:
`(3/4)^19 = 0.004228... > 1/256` while `(3/4)^20 = 0.003171... <= 1/256`. Each halving of the
threshold costs `log_{4/3}(2) = 2.4094...` further stages.

**Finite-zero exclusion.** For any purely multiplicative collar recursion
`Phi^(n+1) = q Phi^(n)` with `q` in (0,1) and `Phi^(0) > 0`, no finite `N` has
`Phi^(N) = 0`, because a product of finitely many strictly positive factors is strictly
positive. The conclusion turns on `q > 0` alone and is independent of the value 3/4, so no
refinement of the contraction factor can produce a finite discharge.

**Status refinement.** The r83 table lists `C5_zero` as `Open_exact/global` with the reason
"no finite N with Phi_5^(N) = 0". That reason reads as "not yet found" but is in fact a
proof. The entry conflates two questions, which r86 separates:

| | Question | Status |
|---|---|---|
| (a) | Does `U_5^bd` reach zero at a finite stage? | `Excluded_rec` (provably not) |
| (b) | Is there a route to `C5 = 0` outside the multiplicative collar? | `Open_undecided` |

Searching for a finite collar stage that discharges C5 is therefore a provably empty search.
Only (b) is genuinely open, and it was previously hidden inside (a).

**Search direction.** Because the exclusion follows from multiplicativity plus positivity,
any candidate mechanism must leave that form: a declared subtractive channel, a truncation
rule (forbidden by the r11 limit guard), or an object unrelated to the collar iteration.
r86 states this search space and does not enter it.

## DOI records

- Version DOI: `10.5281/zenodo.20232911`
- Concept DOI: `10.5281/zenodo.19210728`
- Previous/baseline DOI: `10.5281/zenodo.20117361`
- Expired prior reserved DOI: `10.5281/zenodo.20181842` (absent from the PDF)

No new DOI is requested by RC21.

## Compile audit

Toolchain: MiKTeX 25.12, pdfLaTeX, three passes. The RC19 column was produced by rebuilding
the frozen RC19 snapshot with the same toolchain.

| Check | RC19 | RC20 | RC21 | Result |
|---|---:|---:|---:|---|
| PDF pages | 1014 | 1016 | 1019 | +3 over RC20 (r86 section) |
| LaTeX passes | 3 | 3 | 3 | equal |
| LaTeX errors | 0 | 0 | 0 | ok |
| Undefined refs / citations | 0 / 0 | 0 / 0 | 0 / 0 | ok |
| Duplicate-label warnings | 0 | 0 | 0 | ok |
| Rerun warnings | 0 | 0 | 0 | ok |
| Labels total | 3290 | 3296 | 3305 | +9 over RC20 (the nine r86 labels) |
| Overfull hbox warnings | 58 | 58 | 58 | unchanged |
| Title-page visible Version DOI lines | 1 | 1 | 1 | ok |
| Title-page visible Concept DOI lines | 1 | 1 | 1 | ok |
| PDF Version DOI hits | 4 | 5 | 6 | +1 (r86 source-only clause) |
| PDF Concept DOI hits | 9 | 9 | 9 | unchanged |
| PDF previous/baseline DOI hits | 14 | 15 | 15 | unchanged |
| Expired DOI hits in PDF | 0 | 0 | 0 | ok |

The seven cross-references from r86 into the r09 and r11 collar layers all resolve
(`undefined_refs = 0`).

**Overfull count caveat.** The original RC19 report records 45 overfull hbox warnings; the
same source under MiKTeX 25.12 yields 58. This is a toolchain effect, not a regression. RC19,
RC20 and RC21 all yield 58 under the present toolchain, so neither r85 nor r86 introduces a
new overfull box. The overfull count is not a portable baseline value and must be compared
within one toolchain only.

## Guard state

Unchanged by RC21:

```
R_glob^(r86,+)     = (0,1,1,1,1)
Gamma_guard^r86    = (1,1,1,1,1)
R_eff/local^r86    = (0,0,0,0,0)
R_exact/global^r86 = (1,1,1,1,1)
```

r86 spends no guard. It strengthens the justification of the standing C5 guard rather than
consuming it: the first component of the exact/global ledger keeps the value 1, now for the
sharper reason that no finite closure exists inside the declared recursion and no route
outside it has been declared.

The release scope is unchanged: guarded effective/local and frame-typed closures, not exact
global closure. RC21 does not claim exact finite C5 zero closure, exact all-readout
terminality, C6/T2 closure, a global photon-clock/RH theorem, or global all-readout closure.
The detector-threshold result `C5_det/eff` is unaffected and remains `Closed_eff/local` at
`theta = 1/256`, `n = 20`.

## Queue state

Branch Q5 of the r48 queue is discharged. Remaining: Q3 (photon-clock selector-window
calibration, guard-neutral, open) and Q4 (C4 mixed-kernel localization, inadmissible while
`beta_4 = 1/256` stays unspent).

## Divergence note

The unity theorem also appears in the main paper `brendecke2026main`
(DOI `10.5281/zenodo.19210213`), where item (vi) is not modified. The two documents differ in
that scope sentence until the main paper is revised. The Companion carries the narrower and
correct scope. This is inherited from r85 and unchanged by r86.

## Release status

Public upload/release was not performed and is not authorized by RC21. The PDF is named
`Quantum_Sphaera_Companion_v4_7_0_r86.pdf`; on an actual release it would be renamed to the
release filename. The RC19 and RC20 artefacts are retained unchanged as provenance.
