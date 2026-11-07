# QAM — frame interfaces and checks for research records

## Frame-local physics and ordinary notation

`qam/tex/qam-physics.sty` implements declared physics profiles and scoped default
contexts on top of the existing QAM record. A profile assigns an interpretation
to ordinary mathematical formulas in one declared frame. It does not derive
that physics from QAM or silently extend it to other frames.

```latex
\usepackage{amsmath}
\usepackage[export]{qam}
\usepackage{qam-physics}

\qamframe{ART}\qamframe{QM}
\qamprofile{gr}{ART}{L_{\rm ART}}{conditional}
  {Classical GR with Lorentz metric and Levi-Civita connection, SI units}
\qamprofile{qm}{QM}{L_{\rm QM}}{conditional}
  {Schrodinger QM with a specified Hilbert space and Hamiltonian}

\begin{qamcontext}{gr}
\[
\qamformula{einstein}{conditional}
  {G_{\mu\nu}+\Lambda g_{\mu\nu}=\frac{8\pi G_{\rm N}}{c^4}T_{\mu\nu}}
\]
\begin{qamcontext}{qm}
\[
\qamformula{schrodinger}{conditional}
  {i\hbar\frac{\partial}{\partial t}|\psi(t)\rangle=\hat H|\psi(t)\rangle}
\]
\end{qamcontext} % the ART default is restored
\end{qamcontext}
```

The equations print in their ordinary notation inside their exact profile.
`\qamphys{einstein}` reuses a stored formula. Outside its profile it automatically
shows both left roles, `ART` and the declared language `L_ART`, around the ordinary
formula. `\qamphys*{einstein}` always shows them, including inside the default
context. Nesting restores the outer context; it never relabels old records.

| Command | Meaning |
|---|---|
| `\qamprofile{key}{frame}{language}{status}{interpretation}` | Declare one immutable interpretation profile; the frame must already exist and cannot be `*`. |
| `\begin{qamcontext}{profile} ... \end{qamcontext}` | Choose a scoped default profile for ordinary-looking formulas. |
| `\qamformula[premises]{key}{status}{ordinary TeX}` | Register and display a formula in that context, with the profile and any extra premises retained as dependencies. |
| `\qamphys{key}` / `\qamphys*{key}` | Display an existing formula with automatic / always explicit left roles. |
| `\qamphysconvert{key}{status}{map}{source}{target-profile}{target-formula}` | Explicitly transport through a declared map and provide the target interpretation. This always prints explicit roles. |

No GR-to-QM transition is supplied by the example. A transition must have the
declared source and target frames; its target formula must be explicitly supplied.
The new record depends on both the transported source and the target profile.
Profiles within the same named frame are still distinct: the formula API refuses
an implicit mixture of their premises. Use an explicit declared self-frame map
and target interpretation if such a comparison is intended.

Formula/profile identifiers start with an ASCII letter and use letters, digits,
hyphens or underscores. `qphys-profile-...` and `qphys-transfer-...` are internal
record keys and must not be redeclared. Interpretation text and formulas cannot
contain literal semicolons, which delimit the existing `.qam` record format.
Ordinary TeX math commands such as `\;` are not literal semicolon tokens.

**Export and status.** With `export`, the unchanged `.qam` format contains an
explicit frame, language/profile in the statement, and the original formula TeX.
The profile is a hashed premise, so changing the interpretation or formula changes
the record hash. Extra inputs remain tracked. `conditional` in the example marks
an imported model/profile assumption, not a claim that QAM has disproved established
physics. Authors assign the appropriate status to each statement; translation never
raises it. Formula registration records an interpretation and declared dependencies,
not a machine-verified mathematical derivation of its contents.

**Actual checking scope.** The new package checks context, profile identity, source/
target frames, duplicate declarations and inherited status/provenance. Its commands
do not commit invalid records even in `mode=warning`. The ordinary formula is an
unexpanded TeX payload, not an executable CAS expression: Einstein tensors, units,
operator domains, physical laws and the truth of a transition are not automatically
verified. Existing low-level `\qamclaim`/`\qamderive` remain available with their
original frame-level checking; they do not gain a profile checker by being loaded
alongside this package. The existing Lean checker validates the resulting record
dependencies and frame links; it does not interpret the physical formula/profile.

Complete example: [`examples/physics.tex`](examples/physics.tex). It exercises ART,
QM, nested defaults, explicit notation and standalone reuse. The test suite also
checks an explicit transition with a different target formula; this is an
illustrative declared map, not a GR/QM theory.

```sh
python3 qam/tex/tests/run_tests.py
# Retain compiler logs, PDFs and exported records for inspection:
python3 qam/tex/tests/run_tests.py --output-dir build/qam-tests
```

The runner is cross-platform and uses the installed `pdflatex`. If `pdftotext` is
available, it also checks the rendered implicit/explicit roles and nested context
restoration. CI installs it. These are software tests, not physical hypothesis tests.

## Existing record checks

The base QAM package implements typed bookkeeping checks for long research records, written with or without language models.
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

## Optional Qiskit simulation

From the repository root:

```sh
python -m pip install -r qam/simulation/requirements.txt
python -m qam.examples.area_qiskit
```

Use `qam.simulation.Basis(frame, labels)` to declare the QAM interpretation
of the computational basis. Labels must be unique and hashable. Use a
power-of-two basis size and model any padding states explicitly.
`basis.prepare(label)` prepares one basis state. Apply a Qiskit circuit with
`state.evolve(circuit)`. For a frame transition, declare the output basis
with `state.evolve(circuit, target=target_basis)` and supply the circuit
implementing the proposed map.

Use `state.readout(frame, observable)` to obtain probabilities grouped by the
output of a diagonal observable. For a mixed readout, the observable
function implements the model's selector and aggregation on each basis label.
A rotated measurement can be represented by applying its basis-change
circuit before readout. The simulator checks frame labels and dimensions.
The model author supplies the interpretation and justification of the circuit.
