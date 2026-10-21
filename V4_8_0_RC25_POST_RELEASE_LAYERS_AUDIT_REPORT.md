# v4.8.0-RC25 Post-Release Layers Audit

RC25 is a release candidate on the state after layer v4.8.0-r20. It carries the published v4.8.0 monolith
(Version DOI `10.5281/zenodo.23365244`, which contains r85–r94 and v4.8.0-r01, r02) together with the eighteen
source-only layers v4.8.0-r03 through r20 recorded since that release. The v4.8.0 release is retained unchanged as
provenance. RC25 does not request a new DOI and does not authorize a public release.

Unlike the v4.7.0 candidates RC19–RC24, RC25 carries no snapshot source file: the git tag `RC25` fixes the source.

## Character of the layers since v4.8.0

The eighteen layers are predominantly audits, corrections and tests. Their joint outcome, recorded in the register
of v4.8.0-r09 and extended in r17–r20, is that **no prediction of the Companion's falsifiability corollary stands as
confirmed**, while several structural results carry. Earlier layers are not rewritten; every status change is a new
register entry.

| layer | content |
|---|---|
| r03 | dimensional and numerical audit of the physical-constant layer; F11: both inputs of the frame factor are values of the same Barbero–Immirzi parameter, one from a superseded counting |
| r04 | decoupling from the Riemann source, which is no longer a proof source; standalone Heisenberg compensator and cascade; repaired triole hierarchy |
| r05 | corrected explicit formula; Θ-sum conjecture refuted; GUE statistics empirical only |
| r06 | signature (1,6) of the biquaternion kernel; Reading B (ℂ³ under SO(3,ℂ), Riemann–Silberstein form) adopted as working reading; triole lemma; null cone = S₀ |
| r07 | sector assignment s > 0 matter, s < 0 tachyon, s = 0 photon; duality angle |
| r08 | prediction P1 (photon-frame unfolding) not confirmed |
| r09 | P2 excluded by data, P3 a coincidence; register of all predictions and main results |
| r10 | Koide form as triole; Reading B supplies kinematics, not dynamics |
| r11 | first pre-registered test: δ = K/3 refuted |
| r12 | pre-registered neutrino and mixing tests H2–H8; octonionic flavour group; PMNS claim reclassified |
| r13 | JUNO 2026 re-check; H9 fixed for future JUNO data; associator of the generation triple |
| r14 | colour and generation separated |
| r15 | octonionic Hopf fibration as carrier of the triality slots |
| r16 | pre-registered test H11: masses from invariants on the triple space refuted up to degree four |
| r17 | time direction of the cosmological fractions: Ω_Λ = 1 − β_sym² at all epochs is incompatible with the drift of β_sym assumed in the saturation model (sign reversed, Ω_Λ(z=1100) too large by 5.8·10⁸) |
| r18 | three-frame typing of the frame offset by rapidity cross terms; the frame factor γ_L is the matter–tachyon term but is used for matter–photon conversion; the observer position 0.422 is a halving in the wrong variable; r17 narrowed to the saturation model |
| r19 | readout cubes linked by transition maps add only a holonomy; Reading B has no Lorentz transformation between the sectors; ℤ₂ holonomy of the duality circle around the photon; the earlier reading as a photon-centred view |
| r20 | tachyon frame: same holonomy and principal spinors as matter; superluminal rapidity artanh(1/v) + iπ/2 with imaginary part equal to the duality angle, relating both readings; cross terms with the tachyon imaginary; holonomy test H13 refuted |

## Pre-registered tests

All tests were fixed in committed notes (`llm/Vorab_Notiz_H*.md`) before computation.

| test | content | outcome |
|---|---|---|
| H1 | Koide phase δ = K/3 | refuted |
| H2 | neutrinos as light-like triole | compatible; normal ordering supported by JUNO 2026 |
| H3 | triole sign as Majorana CP parity | compatible, not testable at present |
| H4 | TM1 against TM2 | TM1 preferred over TM2; TM1 itself disfavoured by JUNO 2026 |
| H5 | Hopf angle as mixing angle | failed |
| H6 | criteria for selecting the TM1 lift | main criterion (S₃ with the triole) speaks against TM1 |
| H7, H10 | Heisenberg compensator, associator as selection criteria | no selection reason found |
| H8 | Cayley–Dickson involution as CP | disfavoured by JUNO 2026 |
| H9 | sin²θ₁₂ = β_sym²/cos²θ₁₃ = 0.30862 | open; decided by the next JUNO release with σ ≤ 0.004 |
| H11 | masses from invariants on the triple space | refuted |
| H12 | assignment of measured values to rapidity cross terms | not separable from H9 by the fixed criterion; no test |
| H13 | readout factor as Wigner holonomy of a triole boost loop | refuted (z = −7.9) |

A post-hoc observation attached to H13 (cos²(δ/2) instead of cos δ) is recorded in r20 as not registered and not
counting.

## DOI records

- Version DOI (v4.8.0, unchanged on the title page): `10.5281/zenodo.23365244`
- Concept DOI: `10.5281/zenodo.19210728`
- Previous version DOI (v4.7.0): `10.5281/zenodo.20232911`
- Previous/baseline DOI (v4.6.0): `10.5281/zenodo.20117361`
- Expired prior reserved DOI: `10.5281/zenodo.20181842` (absent from the PDF)

No new DOI is requested by RC25. A public release of this state would require a new version number and a new
Version DOI.

## Compile audit

Toolchain: MiKTeX 25.12, pdfLaTeX, three passes. The v4.8.0 column was produced by rebuilding the source of tag
`v4.8.0` (SHA256 `83f90d3e…`, identical to the v4.8.0 manifest) under the same toolchain; the published v4.8.0 PDF
was built under TeX Live 2022.

| check | v4.8.0 (rebuilt) | RC25 | result |
|---|---:|---:|---|
| PDF pages | 1045 | 1096 | +51 (eighteen layers) |
| LaTeX errors | 0 | 0 | ok |
| undefined refs / citations | 0 / 0 | 0 / 0 | ok |
| duplicate-label warnings | 0 | 0 | ok |
| rerun warnings | 0 | 0 | ok |
| raw `??` markers, source / PDF | 0 / 0 | 0 / 0 | ok |
| labels total | 3369 | 3474 | +105 |
| overfull hbox warnings | 58 | 58 | unchanged |
| PDF bookmarks | 0 | 986 | bookmarks re-enabled after v4.8.0 |
| title-page Version DOI lines | 1 | 1 | ok |
| title-page Concept DOI lines | 1 | 1 | ok |
| PDF Version DOI hits | 3 | 21 | +18, one source-only clause per layer |
| PDF Concept DOI hits | 12 | 30 | +18, same clauses |
| PDF previous version DOI hits | 9 | 9 | unchanged |
| PDF previous/baseline DOI hits | 17 | 17 | unchanged |
| expired DOI hits in PDF | 0 | 0 | ok |

**Overfull count.** The published v4.8.0 report records 45 under TeX Live; the same source yields 58 under MiKTeX
25.12, the toolchain effect already documented for RC19. No layer since v4.8.0 adds an overfull box.

**Bookmarks.** The r25/r27 workaround `bookmarks=false` was removed after the v4.8.0 release and had been tested only
under TeX Live. RC25 is the first build of the bookmarked source under MiKTeX: 986 bookmarks, no change in pages,
labels or hard audit values against the layer-by-layer builds.

## Guard state

Unchanged across all twenty v4.8.0 layers:

```
R_glob      = (0,1,1,1,1)
Gamma_guard = (1,1,1,1,1)
beta_4 = 1/256 unspent
```

The guard linter (`llm/training/guard_linter.py`) reports no hit from v4.8.0-r03 to the end. The heuristic scan
`qs.py guards` reports the same two candidates as in the v4.8.0 source, both in negated context in r84. RC25 does not
claim exact finite C5 zero closure, exact all-readout terminality, C6/T2 closure, a global photon-clock/RH theorem, or
global all-readout closure.

## Release status

Public upload/release was not performed and is not authorized by RC25. The PDF is named
`Quantum_Sphaera_Companion_v4_8_0_r20.pdf`; on an actual release it would be renamed to the release filename. The
v4.8.0 release artefacts and RC19–RC24 are retained unchanged as provenance.
