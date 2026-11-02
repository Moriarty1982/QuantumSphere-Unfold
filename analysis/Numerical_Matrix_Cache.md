# Persistent Numerical Matrix Cache

Local performance infrastructure, not a new mathematical result. Initial
integration is deliberately limited to `HC_Cartan_Cauchy_Next_Completion.py`;
historical calculation modules are not rewritten.

## Identity and Collision Handling

`Numerical_Matrix_Cache.MatrixCache` uses SHA-256 to select a bucket. A
bucket can hold several entries with the same fingerprint. A hit requires
an exact comparison of the entire typed canonical input record, including
every input array's bytes, dtype and shape, not a second hash comparison.
Tests deliberately force different inputs to the same fingerprint.

Python dictionary key collisions and scientific fingerprint collisions
are separate issues. A second dictionary alone would not establish that
two numerical inputs are equal. This cache stores collision groups both
in memory and as independent files under each fingerprint directory.

Structured input identity distinguishes lists from tuples, numeric scalar
types, signed zeros and metadata. Dictionary insertion order and array
memory layout do not affect identity: keys are sorted and numeric arrays
are represented in C order. Object arrays, strings as arrays, unsupported
objects and nonfinite numeric inputs/results are rejected. Cache input
mutation during a calculation prevents publishing that result.

The caller must include every dependency of the calculation. The Cartan
integration includes actual prepared/lower data, coordinates, highest
coefficients, mask-defining source fingerprints and NumPy version. SVD
entries include the full matrix, full/economy mode, NumPy version and
cache implementation fingerprint. Rank cutoffs and right-hand sides are
not cached as SVD results: the solver recomputes its rank, inverse action
and unprojected residual for each current problem.

## Storage and Safety

Default storage is `build/numerical-cache/`, already excluded by the
repository's build ignore rule. No cache file belongs in a paper/release.
Entries are compressed NPZ with numeric arrays and JSON metadata;
`allow_pickle=False` is mandatory. Saved dtype, shape and SHA-256 checksums
detect damaged numeric payloads. These checks are integrity checks, not
authentication of data supplied by an adversary; use the local cache as
generated workspace data, not as a downloaded trusted result certificate.

Writes use a temporary file followed by atomic replacement with a unique
entry name. Concurrent processes may compute duplicate entries, but do not
replace one another's collision-group index. Broken entries are skipped
and recomputed. Write permission failures leave the numerical calculation
usable without persistence. A bounded 128 MiB memory cache avoids repeated
disk reads; callers receive copies so mutation cannot poison stored data.
There is no automatic disk eviction in this first implementation.

## Initial Integration

The current next-Cauchy calculation caches its 720-by-1720 highest response,
the 1114-by-1168 re-preparation system, and the SVDs used in unrestricted,
masked, combined and old-first solves. It still evaluates the actual field
equations after each solve. A cache hit is never a compatibility proof.

Normal execution uses the cache automatically. To force fresh computation:

```powershell
python -B analysis/HC_Cartan_Cauchy_Next_Completion.py --no-cache
```

Alternatively set `QSC_MATRIX_CACHE=0` for a process. Add `--cache-stats`
to show hits/misses. The existing scientific JSON report contains neither
machine-specific cache paths nor timing-dependent hit counts.

The targeted tests cover collisions, persistence across instances, output
isolation, corruption recovery, nonfinite/object rejection and concurrent
writers. Verification timings are recorded below after actual execution.

## Measured Verification (2026-10-18)

Final implementation, two separate Python processes on the local machine:

| Complete next-Cauchy script | Wall-clock time | Cache events |
| --- | ---: | --- |
| Cold, populate current implementation entries | 70.227 seconds | 7 misses, no hits |
| Warm, read current entries from disk | 3.985 seconds | 7 disk hits, no misses |

The generated scientific JSON reports are byte-identical. This is about
17.6 times faster for the measured unchanged repeat, not a prediction for
new matrices, every research task, or the entire test suite. Actual field
residual checks still run. First-time writes and changed inputs still
require computation; changed implementation fingerprints deliberately
invalidate earlier entries.

Verification uses targeted tests rather than another whole audit run:
24 cache/adversarial/integration tests, 14 current-Cartan numerical tests
and 34 full-monolith tests (72 distinct checks). The 14 numerical tests
also pass with `QSC_MATRIX_CACHE=0`. Cache tests pass with ResourceWarning
treated as an error. The full origin-preservation and whitespace checks
pass. No main TeX/PDF, native model, release, commit or push is changed.

## Clean-Code Refactor

The cache now separates exact lookup, computation/input validation, and
publication into focused methods. `_MemoryEntry` replaces positional
in-memory tuples with named fields. Statistics updates are protected by
the same lock; builders still run outside it. The public cache API, typed
canonical encoding and schema-one NPZ format are unchanged. Regression
tests cover archives written before this refactor and dynamic imports
without module registration.

The current Cartan script uses two explicit data containers:

- `AffineSystem` binds the response matrix and residual to their earlier
  and highest coordinate masks. It validates dimensions, ownership,
  finiteness and indices and applies increments without altering inputs.
- `SVDReduction` owns a read-only copy of its coefficient matrix and
  centralizes rank, cutoff, inverse and kernel logic. A requested complete
  kernel includes the missing right-null directions for wide matrices.
  A zero-rank report no longer invents a retained singular value.

This is a scoped maintainability refactor of the two current modules,
not a migration of historical calculations or a change of field equations.
The containers have frozen field bindings; arbitrary NumPy payloads are
not generally claimed deeply immutable. The cache retains defensive-copy
semantics. No Docker runtime or additional package is required.

Refactor verification: 28 cache/compatibility/structure tests, 9 new
solver-container tests, 14 actual Cartan numerical tests and 34 full-monolith
tests passed (85 distinct checks). Cache tests treat ResourceWarning as
an error. No full audit-suite rerun was needed for this scoped refactor.
The original pre-refactor scientific JSON was saved locally before edits;
all its contents remain equal after excluding the deliberately refreshed
input-fingerprint record. The final cold/warm reports are byte-identical.

The measured refactor run took 73.531 seconds cold and 4.270 seconds warm
in a separate process, with seven disk hits and zero misses on the repeat.
These measurements show the cache remains effective, not an additional
speedup from clean-code structure. The earlier timing table records the
pre-refactor measurement. Full-origin preservation and whitespace checks
pass; the main paper/PDF remain unchanged and nothing was committed/pushed.

The subsequent [dependency-injection integration](Numerical_Dependency_Injection.md)
adds a real provider composition root, distinct from those data containers.
The current CLI constructs and injects scoped cache/backend services and
does not modify the environment to disable caching. Existing standalone
cache calls keep their compatibility behavior. Scientific values remain
unchanged; the latest targeted verification has 103 passing checks.
