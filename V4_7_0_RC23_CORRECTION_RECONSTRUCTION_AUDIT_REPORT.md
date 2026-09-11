# v4.7.0-RC23 Correction and Reconstruction Audit

RC23 carries two layers: r89, which corrects two false factual assertions in r87, and r90,
which attempts a reconstruction of the bound `Delta_gamma < 1/5`. It supersedes RC22, which
is retained unchanged as provenance and which carries the erroneous r87 text.

## r89 --- correction of r87

r87 asserted that the decomposition of the V9 overlap flux was not recorded in this source
and that `V8 -> V9` was the last blocked relay edge. Both were false.

| r87 assertion | status | actual location |
|---|---|---|
| `(N_9, kappa_9)` not recorded | false | r14 chart ledger: `(2, 1/2, 3)` |
| `V8 -> V9` is the only blocked edge | false | r17 stitched it |
| no claim which case holds | moot | decided in r17 |

The r14 finite valley-front chart scan tabulates all ten charts with packet count, coherence
parameter and available gain. The r17 guarded micro-lift performed
`(2, 1/2, 3) -> (3, 1/2, 3)`, obtaining `H_9' = 18 > 16` with margin 2, and stitched the
chain to `V1 ... V9`.

**The defect was in the source survey, not in the calculation.** The r87 single-packet lift
formula `Delta S = 1 + 2 kappa N` applied to the r14 parameters gives `Delta S = 3`,
`S_9' = 6`, `G_9 S_9' = 18` --- precisely the values r17 reports. What r87 presented as an
open alternative was a correct prediction of a step already taken. The corrected r87 text
records this as a verification.

Rule r89, now also in the project documentation: a claim that a datum is missing concerns
the whole monolith and must be checked against the rounds adjacent to the one being read.
The solve chain habitually tabulates in one round and consumes in another.

## r90 --- reconstruction attempt for `Delta_gamma < 1/5`

r87 recorded that this bound has no derivation in the source: it enters through the
compressed r55--r80 chain, and the detailed r65 text is not part of the packet. Three
searches have now confirmed its absence rather than merely failing to find it: the project
directory, an archive of 841 tex files spanning v0.1 to v3.35, and nine v4 release packets.
A git pickaxe over the reconstructed history shows the notation `Delta_gamma` and `W_clk`
first appearing in RC19 --- that is, they were introduced during the v4.7.0 rounds r01--r84,
of which no intermediate state is archived.

**This layer reconstructs a bound of the right size from what is present. It is not a
recovery of the original argument.**

The r15 clock model fixes three ingredients: the probe
`C_gamma(tau) = 1 + eta |sum w_m exp(i gamma_m tau)|^2 / (sum |w_m|)^2`, its local normalized
form `G_V(tau) = 1 + (G_avail - 1) cos^2((tau - tau_V)/sigma_V)` giving
`eta = G_avail - 1`, and window membership `C_gamma >= G_req`.

Expanding the coherence factor to first order in the phase spread yields
`1 - Var(phi)`, so the selector survives exactly while

```
Var(phi) <= 1 - (G_req - 1)/(G_avail - 1) = 1 - rho_V
```

where `rho_V` is the ratio already tabulated in the r15 half-width formula. Over the three
charts that carry windows:

| chart | rho_V | 1 - rho_V |
|---|---|---|
| V3 | 3/5 | 0.4000 |
| V5 | 2/5 | 0.6000 |
| V8 | 7/9 | 0.2222 |

The family-wide bound is the minimum, `2/9 = 0.2222`, attained at the narrowest window V8.
The recorded bound `1/5 = 0.2` sits just below it with a margin of exactly ten percent.
Rounding `2/9` down to the nearest simple fraction gives `1/5`, and that matches the rounding
discipline used elsewhere, where thresholds are carried as `1/256` and `1/64`.

**Rejected alternative.** The same table contains `rho_V3 - rho_V5 = 3/5 - 2/5 = 1/5`, which
reproduces the constant exactly rather than approximately. It is rejected: a difference of
two window ratios is not a spread of clock frequencies, does not depend on gamma at all, and
nothing in the grammar would make such a difference a preservation threshold.

**Limits, stated rather than papered over.** `Delta_gamma` is nowhere defined in this source,
so whether it denotes a variance, a standard deviation or a maximal deviation is not
recorded; the expansion is first order and holds only for small spread; and the ten-percent
margin is plausible but not derived. Under a standard-deviation reading the comparison would
be against `sqrt(2/9) = 0.471` and `1/5` would be far more conservative than necessary --- which
is evidence for the variance reading, not proof.

Ledger: `R_rec^r90 = (0, 0, 1)` for (coherence bound derived, numerical match established,
r65 provenance still missing). The third component stays open; only the original text can
close it. The provenance component of `R_cal^r87` is likewise unchanged.

## DOI records

- Version DOI: `10.5281/zenodo.20232911`
- Concept DOI: `10.5281/zenodo.19210728`
- Previous/baseline DOI: `10.5281/zenodo.20117361`
- Expired prior reserved DOI: `10.5281/zenodo.20181842` (absent from the PDF)

No new DOI is requested by RC23.

## Compile audit

Toolchain: MiKTeX 25.12, pdfLaTeX, three passes. The RC19 column was produced by rebuilding
the frozen RC19 snapshot with the same toolchain.

| Check | RC19 | RC21 | RC22 | RC23 | Result |
|---|---:|---:|---:|---:|---|
| PDF pages | 1014 | 1019 | 1025 | 1030 | +5 over RC22 (r89, r90) |
| LaTeX errors | 0 | 0 | 0 | 0 | ok |
| Undefined refs / citations | 0/0 | 0/0 | 0/0 | 0/0 | ok |
| Duplicate-label warnings | 0 | 0 | 0 | 0 | ok |
| Rerun warnings | 0 | 0 | 0 | 0 | ok |
| Labels total | 3290 | 3305 | 3322 | 3335 | +13 (6 from r89, 7 from r90) |
| Overfull hbox warnings | 58 | 58 | 58 | 58 | unchanged |
| Title-page Version DOI lines | 1 | 1 | 1 | 1 | ok |
| Title-page Concept DOI lines | 1 | 1 | 1 | 1 | ok |
| PDF Version DOI hits | 4 | 6 | 6 | 6 | unchanged |
| PDF Concept DOI hits | 9 | 9 | 9 | 9 | unchanged |
| Expired DOI hits in PDF | 0 | 0 | 0 | 0 | ok |

**Overfull count caveat.** The original RC19 report records 45; the same source under
MiKTeX 25.12 yields 58. Toolchain effect, not a regression: RC19 through RC23 all yield 58
here, so no layer since RC19 introduces a new overfull box.

## Guard state

Unchanged by RC23:

```
R_glob^(r90,+)  = (0,1,1,1,1)
Gamma_guard^r90 = (1,1,1,1,1)
```

Neither r89 nor r90 spends a guard. r90 makes no spectral identification between Riemann
zeros and photon ticks; all its statements are local and chart-bound. `W_clk^loc` continues
to be carried as a conditional local statement under its inherited bound, whose status as an
inherited constant is unchanged.

The release scope is unchanged: guarded effective/local and frame-typed closures, not exact
global closure.

## Version control

From RC23 onward the document is under git. The history runs from v0.6.0 (1238 lines) through
v1.0.0, v2.9.0, v3.0.0, v4.0.0, v4.4, v4.6.0 and RC19 to the present state, reconstructed
from the archived release states. Tags mark the major transitions and every RC.

Dates before v4.0.0 are archiving dates, not authoring dates: the source files come from a
download folder in which whole version blocks share a timestamp. The ordering is correct
because it derives from the version numbers; the days are not. From v4.0.0 the dates come
from the release archives and are reliable.

Snapshot files are no longer required for future RCs --- a tag carries the same information.
The existing `..._RC19..._RC23_*_source.tex` files remain because the manifests hash them.

## Queue state

| branch | content | status |
|---|---|---|
| Q1 | local field-interface elaboration | done (r49--r54) |
| Q2 | theoremlet-to-lemma packaging | done (r55--r80) |
| Q3 | photon-clock selector-window calibration | calibrated (r87); provenance reconstructed but not recovered (r90) |
| Q4 | C4 mixed-kernel localization | inadmissible while `beta_4 = 1/256` stays unspent |
| Q5 | C5 asymptotic-collar bookkeeping | done (r86) |

The finite relay chain runs `V1 ... V9`; only `V0` remains outside it, needing `Delta S = 12`
against the largest executed lift of `11/2`.

## Release status

Public upload/release was not performed and is not authorized by RC23. The PDF is named
`Quantum_Sphaera_Companion_v4_7_0_r90.pdf`; on an actual release it would be renamed to the
release filename. The RC19 through RC22 artefacts are retained unchanged as provenance.
