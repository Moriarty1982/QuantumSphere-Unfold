# v4.8.0 Release Audit

v4.8.0 carries the full v4.7.0 monolith, the source-only layers recorded after the v4.7.0
release (v4.7.0-r85 through r94), the opening layer of the v4.8.0 line (v4.8.0-r01,
Planck-Readout Metric Layer) and the release integration layer v4.8.0-r02. Earlier layers are
not rewritten. **No guard has been spent.**

## DOIs

| Role | DOI |
|---|---|
| Version DOI (v4.8.0) | `10.5281/zenodo.23365244`, reserved in Zenodo draft deposition 23365244 |
| Concept DOI | `10.5281/zenodo.19210728` |
| Previous version DOI (v4.7.0) | `10.5281/zenodo.20232911`, provenance only |
| Previous/baseline DOI (v4.6.0) | `10.5281/zenodo.20117361`, provenance only |
| Expired, must not appear | `10.5281/zenodo.20181842` |

The draft was created through `actions/newversion` from deposition 20232911, so it sits under
the existing Concept DOI. It is not published.

## Source changes since v4.7.0

| Layer | Content |
|---|---|
| r85 | citation repair, unity-theorem scope separation |
| r86 | C5 collar bookkeeping, finite-zero exclusion for any multiplicative recursion with q > 0 |
| r87, r89 | photon-clock selector-window calibration and its correction |
| r88 | non-collar routes: subtractive channel and truncation excluded, shape (iii) open |
| r90, r92 | Delta_gamma < 1/5 reconstructed exactly as min over the primary relay chain, attained at V3 |
| r91 | Q4 executed: beta_4 cannot be spent under matter-frame typing |
| r93 | two-sided typing read as a routing grammar |
| r94 | provenance of the C5 factor 3/4: declared ledger value, detector stage fixes q only to (0.7469, 0.7579] |
| v4.8.0-r01 | readout-calibrated Planck scale; photon-frame Planck length as instance; orientation code separated from r82 signature |
| v4.8.0-r02 | release integration and scope refresh |

Front matter: title page carries the v4.8.0 Version DOI line and the Concept DOI line;
`\docversion` = 4.8.0; a "v4.8.0 Release Scope and Provenance Notice" precedes the inherited
v4.7.0 notice. The working source was renamed from `Quantum_Sphaera_Companion_v4_7_0_source.tex`
to `Quantum_Sphaera_Companion_v4_8_0_source.tex` (git rename, history preserved).

## Compile audit

Toolchain: TeX Live 2022, pdfTeX 1.40.22, three pdfLaTeX passes, built outside the project
folder. RC19–RC24 were built with MiKTeX 25.12, which reports 58 overfull boxes for RC19 where
this toolchain reports 45; the overfull count is therefore not comparable across the two
toolchains.

| Check | Value |
|---|---:|
| PDF pages | 1045 |
| Undefined references / citations | 0 / 0 |
| Duplicate label warnings | 0 |
| Rerun warnings | 0 |
| Labels total | 3369 |
| Overfull hbox warnings | 45 (none in r94, v4.8.0-r01, r02 or the front notice) |
| Title page: Version DOI lines (v4.8.0) | 1 |
| Title page: Concept DOI lines | 1 |
| Title page: previous DOI lines | 0 |
| PDF hits: v4.8.0 / Concept / v4.7.0 / v4.6.0 DOI | 3 / 12 / 9 / 17 |
| PDF hits: expired DOI | 0 |

## Guard check

`qs.py guards` over r94, v4.8.0-r01, r02 and the front notice: 0 candidates.

```
Gamma_guard = (1,1,1,1,1)
R_glob      = (0,1,1,1,1)
beta_4      = 1/256, unspent
```

Open items carried into v4.8.0, none an obstruction to a guarded claim: r88 shape (iii);
independent derivation of the C5 factor 3/4 (r94); uniform use of the two-sided notation
(r93); MM/HC field-equation refactor (v4.8.0-r01).

The release does not claim exact finite C5 zero closure, exact all-readout terminality, C6/T2
closure, a global photon-clock/RH theorem, global all-readout closure, or a negative physical
length.

## Tool changes

- `qs.py doi`: role table updated to v4.8.0; previous-version DOIs on the title page are now
  flagged.
- `qs.py outline/ledger` do not yet recognise round headings of the form `v4.8.0-rNN`; labels
  and references for those layers were checked directly.
- `tools/zenodo_publish.py` (GitHub): new-version drafts, DOI reservation, replacement of
  inherited draft files.
