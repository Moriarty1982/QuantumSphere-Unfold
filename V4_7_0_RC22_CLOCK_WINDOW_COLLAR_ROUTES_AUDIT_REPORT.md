# v4.7.0-RC22 Clock-Window Calibration and Non-Collar Route Audit

RC22 carries two layers: r87, which executes branch Q3 of the r48 queue (photon-clock
selector-window calibration), and r88, which examines question (b) of the r86 C5 split.
It supersedes RC21 (r86), which is retained unchanged as provenance.

Neither layer produces a new mathematical result in the sense of a new closure. Both make
inherited structure explicit and eliminate candidate routes. No guard is spent.

## r87 --- photon-clock window calibration

The r15 window family was recorded as a table of three computed values without the rules
behind it. r87 extracts them.

**Window-existence criterion.** A chart has a nonempty zero-clock phase window exactly when

```
16 / G_avail  <=  S_V  <  16
```

The upper end is the direct/assisted boundary, the lower end the assisted/blocked boundary.
All three inherited windows (V3, V5, V8) lie in the band. Their half-widths were recomputed
from the r15 formula in exact rational ratios 3/5, 2/5, 7/9 and agree with the inherited
values to six decimals.

**Single-packet lift formula.** Adding one admissible packet at fixed kappa changes the
overlap flux by `Delta S = 1 + 2 kappa N`. The r16 shadow-basin lift of V6 is the instance
`N: 3 -> 4` at `kappa = 3/4`, giving `Delta S = 11/2` and `S: 15/2 -> 13`.

**Blocked-chart ranking is measure-dependent.** r15 ranks by gain ratio and finds V6 nearest.
By missing overlap flux the order differs:

| chart | S_V | G_avail | G_req/G_avail | missing S |
|---|---:|---:|---:|---:|
| V0 | 4 | 1 | 4 | 12 |
| V6 (pre-r16) | 15/2 | 3/2 | 64/45 ~ 1.422 | 19/6 ~ 3.167 |
| V9 | 3 | 3 | 16/9 ~ 1.778 | 7/3 ~ 2.333 |

By gain ratio: V6 < V9 < V0. By missing flux: V9 < V6 < V0. The two measures correspond to
two lift mechanisms; since r16 in fact lifted through S, the additive column is the relevant
one, and there V9 is the nearer target.

**Last blocked edge reduced to one datum.** The edge V8 -> V9 needs `Delta S >= 7/3`, less
than the `11/2` actually delivered at V6. Whether one packet suffices depends only on the
decomposition of `S_9 = 3`, of which exactly two are admissible:

| (N_9, kappa_9) | Delta S | S_9' | G_9 S_9' | crosses 16? |
|---|---:|---:|---:|---|
| (2, 1/2) | 3 | 6 | 18 | yes |
| (3, 0) | 1 | 4 | 12 | no |

That packet count is not recorded in the present source.

**Provenance gap, recorded as open.** The stated aim of Q3 was to sharpen the provenance of
the bound `Delta_gamma < 1/5`. That bound appears in this source only inside summary and
guard layers, never with a derivation; it enters through the compressed r55--r80 chain where
the detailed r65 step was replaced by the chain invariant. r87 records negatively that the
r15/r16 window layer does not yield it: that layer produces 3/5, 2/5, 7/9, 8/5, 16/9, 32/15,
16/3 and the constant 16, none of which gives 1/5, and its half-widths are measured in units
of sigma_V rather than as a bound on a frequency spread. Q3 is therefore discharged in its
calibration part and left open in its provenance part: `R_cal^r87 = (0,0,0,1)`.

## r88 --- non-collar routes to finite C5 discharge

r86 listed three candidate shapes for question (b) without examining them. r88 examines them
and closes two.

**Shape (i), constant subtraction.** The recursion `Phi^(n+1) = q Phi^(n) - c` has closed form
`Phi^(n) = q^n (Phi^0 + c/(1-q)) - c/(1-q)` and attains zero at an integer stage N if and only
if `c = c*(N) = (1-q) q^N Phi^0 / (1 - q^N)`. For `q = 3/4`, `Phi^0 = 1` this gives
`3/4, 9/28, 27/148, 81/700, 243/3124` for N = 1..5, each verified in exact rational
arithmetic. For generic c the orbit does not meet zero at all but passes from positive to
negative between consecutive stages; sample runs with `c = 1/10, 1/5, 1/4, 3/10` cross at
stages 5, 3, 3, 3 without ever taking the value zero. Exact discharge therefore requires the
channel strength tuned to the target stage, a measure-zero condition.

**The admissibility obstruction.** Tuning is not the decisive objection. With `c = c*(N)` we
get `Phi^(N+1) = -c < 0`, and the orbit stays negative thereafter. It leaves the bounded
collar domain `D_5^bd` at the stage immediately after discharge, and admissibility of
`U_5^bd` was established in r09 precisely through preservation of positivity.

**Shapes (i) and (ii) are one shape, already excluded.** To stay inside the domain, a
subtractive channel needs a stopping rule at stage N. That is a truncation, which is shape
(ii), forbidden by the bounded-collar limit guard `LG_5^bd` of r11. The most natural way
around that guard collapses back into it.

**The free-parameter trap.** Weakening to a stage-dependent channel `c_n` does produce a
finite zero, but a family with unconstrained `(c_n)` realizes any orbit whatsoever, including
orbits violating every other guard. It records the desired answer rather than deriving it. An
admissible variant would have to fix `(c_n)` by an independent structural rule, and that rule
would be the mathematical content. None is declared in the grammar.

**What remains.** Shape (iii), a witness unrelated to the collar iteration, is not supplied.
r88 states its burden: it must exhibit the vanishing of the C5 obstruction itself rather than
smallness of the score; be independent of `U_5^bd`; stay compatible with `C5_det/eff` at
`theta = 1/256, n = 20`; and not import the all-readout slot. The first requirement is the
substantive one: any statement about C5 obtained through the score is a statement about the
limit, which is exactly what the standing guard separates from finite discharge.

Ledger: `D_(b)^r88 = (excluded, excluded, open)`, `R_(b)^r88 = (0,0,1)`. Question (b) remains
`Open_undecided` with a narrower search space.

## DOI records

- Version DOI: `10.5281/zenodo.20232911`
- Concept DOI: `10.5281/zenodo.19210728`
- Previous/baseline DOI: `10.5281/zenodo.20117361`
- Expired prior reserved DOI: `10.5281/zenodo.20181842` (absent from the PDF)

No new DOI is requested by RC22.

## Compile audit

Toolchain: MiKTeX 25.12, pdfLaTeX, three passes. The RC19 column was produced by rebuilding
the frozen RC19 snapshot with the same toolchain.

| Check | RC19 | RC20 | RC21 | RC22 | Result |
|---|---:|---:|---:|---:|---|
| PDF pages | 1014 | 1016 | 1019 | 1025 | +6 over RC21 (r87, r88) |
| LaTeX passes | 3 | 3 | 3 | 3 | equal |
| LaTeX errors | 0 | 0 | 0 | 0 | ok |
| Undefined refs / citations | 0/0 | 0/0 | 0/0 | 0/0 | ok |
| Duplicate-label warnings | 0 | 0 | 0 | 0 | ok |
| Rerun warnings | 0 | 0 | 0 | 0 | ok |
| Labels total | 3290 | 3296 | 3305 | 3322 | +17 (10 from r87, 7 from r88) |
| Overfull hbox warnings | 58 | 58 | 58 | 58 | unchanged |
| Title-page Version DOI lines | 1 | 1 | 1 | 1 | ok |
| Title-page Concept DOI lines | 1 | 1 | 1 | 1 | ok |
| PDF Version DOI hits | 4 | 5 | 6 | 6 | unchanged |
| PDF Concept DOI hits | 9 | 9 | 9 | 9 | unchanged |
| Expired DOI hits in PDF | 0 | 0 | 0 | 0 | ok |

The cross-references from r87 into the r15/r16 relay layers and from r88 into the r09/r11
collar layers all resolve.

**Overfull count caveat.** The original RC19 report records 45; the same source under
MiKTeX 25.12 yields 58. Toolchain effect, not a regression: RC19 through RC22 all yield 58
here, so no layer since RC19 introduces a new overfull box. The count is not a portable
baseline value and must be compared within one toolchain only.

## Guard state

Unchanged by RC22:

```
R_glob^(r88,+)     = (0,1,1,1,1)
Gamma_guard^r88    = (1,1,1,1,1)
R_eff/local^r87    = (0,0,0,0,0)
R_exact/global^r88 = (1,1,1,1,1)
```

The release scope is unchanged: guarded effective/local and frame-typed closures, not exact
global closure. RC22 does not claim exact finite C5 zero closure, exact all-readout
terminality, C6/T2 closure, a global photon-clock/RH theorem, or global all-readout closure.
r87 makes no spectral identification between Riemann zeros and photon ticks; its relay chains
remain finite, the longest certified one being the length-six chain of r16.

## Queue state after r88

| branch | content | status |
|---|---|---|
| Q1 | local field-interface elaboration | done (r49--r54) |
| Q2 | theoremlet-to-lemma packaging | done (r55--r80) |
| Q3 | photon-clock selector-window calibration | calibrated (r87); `Delta_gamma` provenance open |
| Q4 | C4 mixed-kernel localization | inadmissible while `beta_4 = 1/256` stays unspent |
| Q5 | C5 asymptotic-collar bookkeeping | done (r86) |

Two concrete data gaps block further progress, neither requiring a guard: the packet count
`N_9` of the sparse reentry front, and the uncompressed r65 text carrying the derivation of
`Delta_gamma < 1/5`. Both live in the RC16 source packet
(`RC14_uncompressed_reference_source.tex`), which is not part of this working directory.

## Divergence note

The unity theorem also appears in the main paper `brendecke2026main`
(DOI `10.5281/zenodo.19210213`), where item (vi) is not modified. The two documents differ in
that scope sentence until the main paper is revised. Inherited from r85, unchanged since.

## Release status

Public upload/release was not performed and is not authorized by RC22. The PDF is named
`Quantum_Sphaera_Companion_v4_7_0_r88.pdf`; on an actual release it would be renamed to the
release filename. The RC19, RC20 and RC21 artefacts are retained unchanged as provenance.
