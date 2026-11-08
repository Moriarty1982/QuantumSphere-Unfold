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

## Exact inverse search for spin readouts

From the repository root, run the OP1 example with Python's standard library:

```sh
python -m qam.tools.spin_readout_search --max-twice-spin 3
```

Supply custom counting weights to `sector_effects(weights)` and
`axis_effect(weights)` from `qam.tools.spin_readout_search`. Keys are
nonnegative integer labels `2j`, with one copy of each listed irrep.
Values are integers or fractions. The solver reports effects forced by
trace zero or full dimension and the unique rotation-invariant scalar
effect on each listed sector, assuming the effect preserves spin sectors.

The single-axis search assumes a shared function of `2m` alone. Within
each parity, the magnetic label sets are nested. The required trace
increment must lie between zero and the number of newly admitted labels.
This condition is also sufficient: the solver distributes the increment
evenly among those new labels. It returns an exact rational witness or
the first conflicting pair. Omitted sectors impose no constraints.
These checks establish representability in the selected access model.
A native QAM transition or measurement instrument requires its own
dynamical justification.

## Local QAM index and readout cache

From the repository root:

```sh
python -m qam.tools.readout_db index
python -m qam.tools.readout_db find einstein
python -m qam.tools.spin_readout_search --cache build/qam.sqlite3
```

The generated database is local to the workspace. The index reads existing
QAM exports in `qam/`, `notes/research/`, and `build/qam-records/`.
Pass explicit directories after `index` to replace that scope. Indexing
rebuilds the claim table and preserves the cache. The index verifies claim
and record hashes and checks available source files, allowing an exact LF
hash match for CRLF checkouts. This is a provenance check. Semantic checks
remain with the QAM checkers.

The spin example stores structured results with exact rational strings.
The key includes the readout ID, frame, counting inputs, method and solver
source digest. A repeated request reuses the stored result. Other callers
can use `cached_readout` and supply all dependencies in the request key,
including formula and premise hashes when their computation uses those
records. The spin example currently uses a Python recipe. Indexed TeX
statements are searchable provenance records and require an explicit
executable recipe to become callable readouts.

### MML requests and MMA receipts

The database CLI reuses the existing framework interpreter for supported
MML requests. From the repository root:

```powershell
python -m qam.tools.readout_db mma scripts/qsc_audit/examples/framework_context.json scripts/qsc_audit/examples/framework_export_request.json
python -m qam.tools.readout_db mma-status
```

The interpreter evaluates the declared context and guards. SQLite stores
the request and the complete MMA receipt, including context hash and
source fingerprints. An insert trigger counts distinct receipts by
`continue`, `guard`, or `reject`. Repeating the same receipt does not
increase the count. Rebuilding the formula index preserves both the
receipts and the calculation cache.

SQLite has no stored procedure language. The Python adapter runs MML
explicitly, and the trigger only updates the receipt counters. The
supported MML instructions and their guard semantics are those of the
existing framework interface. The numerical spin readout continues to use
its separate cache recipe.

The database adapter also accepts the bounded MML instruction `READOUT`:

```powershell
python -m qam.tools.readout_db mma scripts/qsc_audit/examples/framework_context.json qam/examples/spin_readout_mml.json
```

The allowlisted recipe `op1.spin-counting-effects` takes frame M or T and
an integer maximum `2j` from 1 to 200. The existing interpreter checks
the request envelope and guards before the adapter uses the cache or
runs the solver. The receipt includes the structured result and cache
identity, including the context hash and implementation versions.
`continue` means the recipe executed successfully, including when it
returns a mathematical obstruction in the selected access model.
The standalone framework interpreter retains its original instruction set.

## LaTeX display of MMA readouts

Load `qam-readout` and use `\qamreadout{path/to/result.tex}` to include a
generated MMA receipt fragment. Generate the fragment before compilation
from the repository root:

```powershell
python -m qam.tools.readout_db mma scripts/qsc_audit/examples/framework_context.json qam/examples/spin_readout_mml.json --tex-output build/qam-records/spin-readout-result.tex
$env:TEXINPUTS = 'qam/tex;'
pdflatex -output-directory=build/qam-records qam/examples/spin_readout_mml.tex
```

The Python step checks guards and runs the allowlisted recipe or loads
its cached result. The fragment shows the outcome, the result or reasons
for blocking it, and the SHA-512 receipt identifier. A missing fragment
produces a LaTeX warning and a visible placeholder. Regenerate the fragment
after changing the context or request. LaTeX reads the generated fragment
without invoking Python or SQLite. Use fragments generated by the adapter
or from a trusted source.

To retrieve the original MML request and MMA receipt from the hash printed
in the document, use:

```powershell
python -m qam.tools.readout_db receipt <SHA-512> --tex-output build/qam-records/spin-readout-restored.tex
```

The command accepts the hash as one string or in the printed groups.
It checks the stored receipt and request hashes before returning them.
The optional fragment export is available for READOUT receipts and uses
the recorded result without rerunning the recipe. Hash verification
checks the stored records, while recomputation checks the current model.

New MMA runs also store a deduplicated context snapshot. To rerun a stored
request against that exact context with the current implementation, use
`python -m qam.tools.readout_db receipt HASH --replay`. Replay bypasses the
result cache and reports separately whether the receipt and its result
match. A changed implementation hash may change the receipt even when
the result is identical. Older receipts without a saved context can still
be retrieved. They need a context snapshot before they can be replayed.

### Trace an argument from an MMA receipt

A READOUT request may include a top-level `premises` array of QAM claim
hashes. Build the index before executing such a request. MMA follows
the recorded source hashes recursively and snapshots the claims in
dependency order in the receipt. Each entry keeps its statement, status,
frame and source location. A missing premise returns `guard` and prevents
recipe execution. The hashes also enter the calculation cache identity.

```powershell
python -m qam.tools.readout_db index
python -m qam.tools.readout_db mma scripts/qsc_audit/examples/framework_context.json qam/examples/spin_readout_mml.json
python -m qam.tools.readout_db receipt HASH --trace --replay
```

The trace is bound to the receipt hash and remains available after
reindexing. Replay uses the saved premise snapshot. The trace contains
declared dependencies and preserves their status. For example, the
OP1 request links the counting rule with status `reading`. The recorded
relationship does not turn that assumption into a proof.

### Bounded route search

```powershell
python -m qam.tools.readout_db mma scripts/qsc_audit/examples/framework_context.json qam/examples/spin_route_mml.json
```

`SEARCH_ROUTE` explores a fixed OP1 operation catalogue up to the requested
step and spin limits. It records excluded paths and their reasons alongside
candidate routes and their missing guards. Its receipt identifies the
operation catalogue and exact axis solver by their implementation hashes.
The example returns `guard` (exit code 1) because no route passes without an
open native assumption. The stored receipt can be retrieved and replayed
as above. The catalogue is a finite model; declared true guards do not
establish a physical operation.

`SEARCH_ROUTE` also accepts top-level `premises`. Run the index command
before using the OP1 example with its linked counting rule. A missing
premise blocks the search. The saved premise snapshot is available through
`receipt HASH --trace` and is reused for replay even if the index changes.

With `rotation_angles`, SEARCH_ROUTE can generate new routes from
declared spin rotations. Supported angles are 90, 180 and 360 degrees.
The construction takes the coherent axis mean, computes its normalized
SU(2) character exactly on each admitted spin and tests whether the target
character is unique. Successful candidates add a rotation, mean and
spectral-filter step. Failed candidates retain their colliding spins.
The OP1 example uses a three-step limit and tests all three angles.
Native access to the gravitational rotation, the coherent mean and the
spectral filter are three separate guards.

Generated rotation routes report a sufficient finite axis quadrature for
the spin cutoff: equally spaced azimuths and Gauss-Legendre heights.
The OP1 example needs 18 weighted rotations. This describes the exact
operator average on the declared carrier. Coherent execution remains a guard.

When both 90 and 360 degrees are declared, the OP1 example also generates
a four-step route through the half-integer sector. The preliminary
parity step has its own coherent-control guard. The route appears when
the reduced spectrum has no target collision and the prefilter removes
at least one distinct competing eigenvalue.
