# v4.8.0-r01 Research Notes

Working title:

**Planck-Readout Metric Layer and MM/HC Field-Equation Refactor**

## Status

Internal research branch only. This directory is not a mutation of the published `v4.7.0` TeX/PDF payload.

## Baseline

- Public baseline: `v4.7.0`
- Version DOI: `10.5281/zenodo.20232911`
- Concept DOI: `10.5281/zenodo.19210728`

## Purpose

This branch begins the post-v4.7.0 research line by separating physical readout scales from lower interface/transport scales.

The local working expression is:

```tex
\ell_{\mathrm{eff}}(R)=\ell_P\lambda_R
```

where `R` is an admissible readout/interface mode and `\lambda_R` is its MM/HC/QAM calibration factor or pullback norm.

## Scope guard

Allowed here:

- effective/readout-dependent Planck scale;
- local frame-dependent length calibration;
- information-layer metric pullback;
- signed or orientation-coded readout effects;
- two-sided structural tensor notation as conservative grammar.

Blocked here:

- negative physical length as direct observable;
- exact through-collapse length theorem;
- global T2 closure;
- global all-readout terminality;
- RH/global photon-clock theorem.

## Files

- `planck_readout_metric_layer_candidate.tex` — first guarded LaTeX insertion candidate for later integration into the active core.
