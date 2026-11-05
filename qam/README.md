# QAM — bookkeeping checks for research records

QAM is a small typed bookkeeping discipline for long research records, written with or without language models.
It is independent of the Quantum Sphaera project, which only serves as its first case study.

It catches three kinds of error:

| error | rule | TeX (`qam.sty`) | Lean (`QAM.Provenance`, `QAM.QamFile`) |
|---|---|---|---|
| **promotion**: a conditional or computed statement treated as proved | a conclusion has at most the status of its weakest premise | error on `\qamderive` / `\qamconvert` | `no_promotion`, `checked_no_promotion_record`, `checked_proved_record` |
| **input read as result**: a value put in by hand later cited as derived | every claim carries the inputs it rests on; none is lost or invented | error on `\qamindependent` | `independent_iff`, `checked_inputs_record`, `checked_independent_record`, `checked_inputs_sourced` |
| **frame mixing**: quantities of different frames compared or combined | combine and compare only within a frame; change frame only through a declared map | error on `\qamderive` / `\qamcompare` / `\qamconvert` | `frames_declared`, `no_maps_same_frame` |

In addition the TeX package refuses keys, frames and maps that are used before they are declared or declared twice (the record is
append-only). The frame `*` is convention-free (a number or theorem valid in every convention fits every frame), and
`\qamcompose{K}{G}{H}` declares the composite of two maps. Spaces in premise lists are ignored (`{a, b}` = `{a,b}`).

**Division of labour.** `qam.sty` applies the rules while compiling; `qamcheck` (Lean, verified checker, unverified parser) applies the
same rules again to the exported file and checks the hash links; `qamhash.py` recomputes the hashes. Lean does not compute MD5.

**Limits.** Only what is declared is checked. A claim declared `proved` without premises is accepted as such. A fitted value declared
again under a new name is not recognised. Frames are names; several convention axes need frames of their own with maps between them.

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

## Generated QAM notation

The declarations contain everything the QAM notation needs, so the package writes it. The optional first argument is the symbol:

```latex
\qammap[G]{G}{M}{T}
\qaminput[\gamma]{gamma}{M}{computed}
\qamclaim[\kappa]{counting}{M}{proved}
\qamderive[\beta]{beta}{computed}{gamma,counting}
\qamconvert[\beta']{betaT}{conditional}{G}{beta}

\qam{gamma}   % ^M γ := R(w_γ), w_γ = ⟨6, γ⟩ [computed]
\qam{beta}    % ^M β ⇐ ^M γ, ^M κ, W = {w_γ} [computed]
\qam{betaT}   % ^T β' = ^T_M G ^M β, W = {w_γ} [conditional]
\qam*{beta}   % without status tag
\qamledger    % table of all claims in declaration order
```

With `\usepackage[export]{qam}` every claim is also written to `\jobname.qam`, one line per claim, e.g.
`beta := derive(gamma,counting); frame M; status computed; inputs {gamma}`.

## Checking the exported record in Lean

`qam/lean/QAM/QamFile.lean` reads a `.qam` file and checks every line against the record before it; Lean proves what a
successful check means (`derive_sound`, `convert_sound`, `indep_sound`, `compare_sound`, `checked_no_promotion`, `checked_indep`).
Run it with

```
cd qam/lean && lake build && lake exe qamcheck ../examples/example.qam
```

Examples in `qam/examples/`: `example.tex`/`.qam` must pass; `bad_*.qam` must be rejected. Four of them come from documents compiled
with `mode=warning`, one (`bad_inputs.qam`, an input deleted by hand) cannot be produced by TeX at all. Only the checker is verified,
not the parser that reads the text lines.

## Hash chain from the starting thesis

`\qamthesis[\tau]{thesis}{M}{conditional}{statement}` declares the thesis a paper starts from. Every claim gets a hash: MD5 of
`kind;key;frame;status;inputs;sources;statement`, where *sources* are the hashes of its premises. A derived claim therefore names the exact
versions of what it was derived from; change one word of the thesis and every hash below it changes, while independent claims keep theirs
(example: `qam/examples/thesis.tex`). `\qamhash{k}` prints a short hash, `\qamledger` shows a hash column and the record hash.

Checked independently of TeX:
- `python3 qam/tools/qamhash.py verify FILE.qam` recomputes every hash and the record hash (and the MD5 of the source, if present);
- `qamcheck` (Lean) verifies the links: sources are exactly the recorded hashes of the premises, no hash twice
  (`link_derive_sound`, `link_convert_sound`, `link_leaf_sound`);
- `qamhash.py manifest FILE.qam OUT.json FILES...` writes SHA-256 sums of source, PDF and record for a release.

Equal hashes mean equal records, not true ones. MD5 guards against accidental change; the SHA-256 manifest is the check for a release.

The checks run in a single pass because every claim must be declared before it is used. Tests: `sh qam/tex/tests/run_tests.sh`
(workflow `qam-tex.yml`). Requires LaTeX 2022-06 or later.

## Lean

`qam/lean/` is a standalone Lake package that uses the Lean core only (no Mathlib, builds in seconds):
`QAM/Provenance.lean` states the rules for derivation trees; `QAM/QamFile.lean` is the checker for exported records. Its record-level
theorems hold for every record the checker accepts, at any distance along the premises: `checked_good` (an invariant of the whole
record), `checked_no_promotion_record`, `checked_proved_record`, `checked_inputs_record`, `checked_independent_record`,
`checked_inputs_sourced`. Workflow: `qam-lean.yml`.
The older modules `QSFormal.QAM`, `Store`, `StoreProgress`, `Route` and `Models` formalize the object kinds and the store machine;
see the methods paper in `paper/qam/`.

License: CC BY 4.0.
