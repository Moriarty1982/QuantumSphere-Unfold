# QAM — bookkeeping checks for research records

QAM is a small typed bookkeeping discipline for long research records, written with or without language models.
It is independent of the Quantum Sphaera project, which only serves as its first case study.

It catches three kinds of error:

| error | rule | TeX (`qam.sty`) | Lean (`QSFormal.Provenance`) |
|---|---|---|---|
| **promotion**: a conditional or computed statement treated as proved | a conclusion has at most the status of its weakest premise | error on `\qamderive` / `\qamconvert` | `no_promotion`, `proved_only_from_proved` |
| **input read as result**: a value put in by hand later cited as derived | every claim carries the inputs it rests on; none is lost or invented | error on `\qamindependent` | `inputs_tracked`, `inputs_sourced`, `independent_iff` |
| **frame mixing**: quantities of different frames compared or combined | combine and compare only within a frame; change frame only through a declared map | error on `\qamderive` / `\qamcompare` / `\qamconvert` | `frames_declared`, `no_maps_same_frame` |

In addition the TeX package refuses keys that are used before they are declared or declared twice (the record is append-only).

Status order: `open < reading < conditional < computed < proved`.

## TeX package

```latex
\usepackage{qam}                 % errors stop the compiler
% \usepackage[mode=warning]{qam} % warnings only

\qamframe{M} \qamframe{T}
\qammap{G}{M}{T}                         % declared comparison map from M to T
\qaminput{gamma}{M}{computed}            % a value put in by hand
\qamclaim{thm}{M}{proved}                % a premise without inputs
\qamderive{beta}{computed}{gamma,thm}    % ok; \qamderive{beta}{proved}{...} would stop
\qamconvert{betaT}{conditional}{G}{beta} % into frame T
\qamcompare{betaT}{obs}                  % only within one frame
\qamindependent{lemma}                   % stops if lemma rests on an input
\qamshow{beta}                           % prints [computed | frame M | inputs: gamma]
```

Example error:

```
! Package qam Error: Promotion: `beta' is declared `proved', but its weakest
(qam)                premise `gamma' is only `conditional'.
```

The checks run in a single pass because every claim must be declared before it is used. Tests: `sh qam/tex/tests/run_tests.sh`
(workflow `qam-tex.yml`). Requires LaTeX 2022-06 or later.

## Lean

`formal/QSFormal/Provenance.lean` (Lean core only) states the same rules for derivation trees and proves the theorems in the table.
The older modules `QSFormal.QAM`, `Store`, `StoreProgress`, `Route` and `Models` formalize the object kinds and the store machine;
see the methods paper in `paper/qam/`.

License: CC BY 4.0.
