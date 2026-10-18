# Numerical Dependency Injection

The current next-Cauchy computation now has an explicit composition root,
not merely data-container classes. `Numerical_Dependencies.py` defines a
small dependency-injection container without a new framework dependency.

## Providers and Lifetimes

`NumericalContainer` accepts a cache factory and an SVD-backend factory.
Its `services()` method constructs each dependency once and supplies one
`NumericalServices` object per container scope. Concurrent resolution is
protected by a lock; computations do not run under that container lock.
Independent containers can own independent caches and backends.

The supplied cache implements the `NumericCache` protocol; the backend
implements `SVDBackend`. The default is `NumPySVDBackend`. A replacement
backend supplies `svd(matrix, full_matrices=...)` and an explicit identity
with `backend` and `version` fields. Its identity enters the cache key,
so changing a backend does not silently reuse another implementation's
decomposition. Backend identity must describe its actual configuration.

The numerical functions receive `NumericalServices` explicitly, rather
than resolving arbitrary services from a container or modifying globals.
The container is the composition root, not a service locator inside the
mathematical model.

## Current Wiring

`HC_Cartan_Cauchy_Next_Completion.create_container()` configures the two
providers. The CLI resolves services once and injects them into `evaluate`,
matrix preparation, SVD reduction and both ordinary and old-first solves.
Cache statistics come from this injected cache instance. `--no-cache`
configures the scope; it no longer modifies `os.environ`.

```python
from pathlib import Path
from analysis.HC_Cartan_Cauchy_Next_Completion import create_container, evaluate

container = create_container(
    cache_root=Path("build/my-numerical-cache"),
    cache_enabled=True,
)
report = evaluate(services=container.services())
```

Tests or callers can supply `matrix_cache=...` and `svd_backend=...`.
Supplying an existing cache together with cache-construction options is
rejected as ambiguous. Explicitly injected services do not consult the
module-global cache or re-read the environment at each numerical step.

Calls to existing standalone helpers without explicit services retain a
compatibility adapter for their previous global-cache/environment behavior.
The older standalone cache API is also retained. This does not claim that
every inherited scientific module has been migrated: their internal
NumPy calculations and actual field-law implementation remain unchanged.
The injected backend controls the current layer's SVD reductions.

## Scope

The earlier `AffineSystem`, `SVDReduction` and `_MemoryEntry` classes remain
data containers; they were not dependency injection by themselves. The
new provider composition and explicit service propagation address that
separate requirement. There is no Docker runtime, installation, public
upload, main-TeX/PDF change or new mathematical conclusion.

## Verification

Eighteen DI-specific tests pass, including provider lifetime, concurrent
resolution, independent scopes, explicit cache disablement, backend-key
isolation, analytic fake-backend injection and protection against use of
a poisoned global cache. The two complete numerical runs additionally
exercise the CLI composition and service propagation with the actual
field residuals, beyond the focused static orchestration checks.

All 103 targeted checks pass: 18 DI, 28 cache, 9 data-container, 14 actual
Cartan and 34 full-monolith tests. There was no full audit-suite rerun.
The cold run took 72.611 seconds; a separate warm process took 4.350
seconds with seven disk hits. Cold/warm reports are byte-identical.
All scientific report values match the pre-DI baseline after removing
the expected refreshed input-fingerprint record. Main-source preservation
and whitespace checks pass. Nothing was committed, pushed or published.
