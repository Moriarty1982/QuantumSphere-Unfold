# v4.7.0-RC24 Q4 Executed Audit

RC24 carries r91, which executes branch Q4 of the r48 queue. It supersedes RC23, retained
unchanged as provenance. With r91 the queue is fully worked through: Q1 and Q2 executed,
Q3 calibrated, Q5 consolidated, Q4 negatively settled. **No guard has been spent.**

## r91 --- Q4 executed, beta_4 shown not spendable

Q4 had been carried as *inadmissible* since r54 with the reason "beta_4 = 1/256 remains
unspent". That reads as a policy: a guard held back by choice. It is not.

**C4 is no longer a commutator problem.** The r07 split test decomposes

```
S_4^comm  ->  S_4,-^comm (routed_comm)  +  S_4,+^comm (zero_2s)
```

and neither component carries active leakage afterwards. The antisymmetric mixed-transport
part is not contracted away; it is read through a declared commutator comparison channel, and
the source states explicitly that this does not mean a global commutator vanishing theorem.
The active support reduces to `Supp_4^r07 = { S_4,out^collar }`, the component crossing the
bounded--exterior interface. What remains of C4 is a boundary-crossing seam, not a commutator
remainder.

Anyone approaching Q4 from its queue description --- "C4 mixed-kernel localization" --- would
have worked on the wrong object.

**Absorbability was already settled.** r13 tests the residual kernel and finds it not
absorbable by the declared bounded, comparison-routed or selector-routed channels. An
absorption would require a new comparison tensor, a new selector, or an identification with
bounded C5 contraction debt; the first two are absent and the third is forbidden.

**The threshold identity.** The bound does not occur once. r13 states by definition

```
Theta_v := beta_4^r12 = 1/256
```

making the residual C4 bound and the local ridge-front relay threshold the same quantity ---
the threshold on which the whole window and relay-chain theory rests. The detector chain
carries the same value as `theta_det = 1/256`, and r81 types it explicitly alongside
`eps_M^len = l_P / L_ref`, with the sentence: *"These are terminal scales, not exact
all-readout zeros."*

Two readings are distinguished in the layer. Either 1/256 is one terminal scale in three
roles, or three quantities sharing a dyadic value. The source settles the first two by
definition; for the third it supplies equality of value and of role but no explicit
identification. The argument needs only the first two plus the r81 typing.

**Theoremlet r91.** Spending beta_4 --- declaring the residual seam absorbed --- requires
treating a residual at the terminal scale as an exact zero. Under the matter-frame typing:

```
Phi <= eps_M  =>  0_M^eps  =>  0_termdata      but      0_M^eps  =/=>  0_all
```

Q4 is therefore not blocked by a missing tensor or an unbuilt selector. It is blocked by the
same typing that blocks C5 = 0, and no refinement of the localization can remove that block.

**Status reclassification.** Using the r86 vocabulary:

```
Q4:   inadmissible_policy  ->  Excluded_typed
```

The practical difference matters for planning. Under the old reading Q4 was a branch one
might open later, once a suitable comparison tensor had been built. Under the corrected
reading, building that tensor would not help: the obstruction is the typing of the scale at
which the residual sits. A future C4 closure, if one exists, must come from a route that does
not pass through a terminal-scale bound --- structurally the same requirement r88 placed on
shape (iii) for C5.

**Physical reading, recorded as interpretation and not as claim.** The commutator component
was routed rather than eliminated: an antisymmetric transport remainder is not something a
change of chart removes, which is the expected behaviour of a noncommutative structure. What
survives is a seam at the bounded--exterior interface, bounded by the terminal resolution. A
residual sitting at the resolution scale of the readout cannot be declared absent by that
same readout; below the terminal scale the frame records a zero, and that record is a
statement about the frame, not about the object. No claim is made that beta_4 equals a
physical constant, that 1/256 has dimensional meaning, or that the seam corresponds to a
measurable quantity.

Ledger: `R_Q4^r91 = (0,0,1)` for (commutator component already routed, absorbability already
settled, spending shown unavailable). The third component is 1 because a negative result
closes the branch, not the obstruction: C4 remains open in the exact/global ledger.

## DOI records

- Version DOI: `10.5281/zenodo.20232911`
- Concept DOI: `10.5281/zenodo.19210728`
- Previous/baseline DOI: `10.5281/zenodo.20117361`
- Expired prior reserved DOI: `10.5281/zenodo.20181842` (absent from the PDF)

No new DOI is requested by RC24.

## Compile audit

Toolchain: MiKTeX 25.12, pdfLaTeX, three passes. The RC19 column was produced by rebuilding
the frozen RC19 snapshot with the same toolchain.

| Check | RC19 | RC22 | RC23 | RC24 | Result |
|---|---:|---:|---:|---:|---|
| PDF pages | 1014 | 1025 | 1030 | 1033 | +3 over RC23 (r91) |
| LaTeX errors | 0 | 0 | 0 | 0 | ok |
| Undefined refs / citations | 0/0 | 0/0 | 0/0 | 0/0 | ok |
| Duplicate-label warnings | 0 | 0 | 0 | 0 | ok |
| Rerun warnings | 0 | 0 | 0 | 0 | ok |
| Labels total | 3290 | 3322 | 3335 | 3343 | +8 (the eight r91 labels) |
| Overfull hbox warnings | 58 | 58 | 58 | 58 | unchanged |
| Title-page Version DOI lines | 1 | 1 | 1 | 1 | ok |
| Title-page Concept DOI lines | 1 | 1 | 1 | 1 | ok |
| PDF Version DOI hits | 4 | 6 | 6 | 6 | unchanged |
| PDF Concept DOI hits | 9 | 9 | 9 | 9 | unchanged |
| Expired DOI hits in PDF | 0 | 0 | 0 | 0 | ok |

The three cross-references from r91 into the r07 and r13 layers all resolve.

**Overfull count caveat.** The original RC19 report records 45; the same source under
MiKTeX 25.12 yields 58. Toolchain effect, not a regression: RC19 through RC24 all yield 58
here, so no layer since RC19 introduces a new overfull box.

## Guard state

Unchanged by RC24, and pointedly so:

```
R_glob^(r91,+)  = (0,1,1,1,1)
Gamma_guard^r91 = (1,1,1,1,1)
beta_4 = 1/256 unspent
```

beta_4 remains unspent not as a reserve held back, but because the spending operation is not
available in the declared typing. RC24 does not claim exact finite C5 zero closure, exact
all-readout terminality, C6/T2 closure, a global photon-clock/RH theorem, or global
all-readout closure.

## Queue state after r91

| branch | content | status |
|---|---|---|
| Q1 | local field-interface elaboration | done (r49--r54) |
| Q2 | theoremlet-to-lemma packaging | done (r55--r80) |
| Q3 | photon-clock selector-window calibration | calibrated (r87); provenance reconstructed, not recovered (r90) |
| Q4 | C4 mixed-kernel localization | executed and negatively settled (r91), `Excluded_typed` |
| Q5 | C5 asymptotic-collar bookkeeping | done (r86) |

The r48 queue is fully worked through. What remains open is now precisely named rather than
diffuse:

1. a C5 witness outside the collar iteration, meeting the four requirements of r88 shape (iii)
2. a C4 route that does not pass through a terminal-scale bound (r91)
3. chart `V0`, outside the finite relay chain, needing `Delta S = 12` against the largest
   executed lift of `11/2`
4. the uncompressed r65 text carrying the derivation of `Delta_gamma < 1/5`

## Version control

The document is under git. The history runs from v0.6.0 through v1.0.0, v2.9.0, v3.0.0,
v4.0.0, v4.4, v4.6.0 and RC19 to the present state, reconstructed from the archived release
states, with tags on the major transitions and every RC. Dates before v4.0.0 are archiving
dates, not authoring dates.

## Release status

Public upload/release was not performed and is not authorized by RC24. The PDF is named
`Quantum_Sphaera_Companion_v4_7_0_r91.pdf`; on an actual release it would be renamed to the
release filename. The RC19 through RC23 artefacts are retained unchanged as provenance.
