# Numerical Helper Contract

The helper is self-contained apart from NumPy. Its functions can be imported by
path without project modules. Pass an existing `services` object when using the
repository's injected SVD/cache implementation; no global container is resolved.

## CLI

```powershell
python -B <skill-folder>/scripts/compatibility.py case.npz --output result.json
```

The NPZ must contain finite numeric arrays:

- `matrix`: A, shape (m,n), m,n positive.
- `target`: b, shape (m,).
- `source`: optional B, shape (m,s), including s=0.
- `known_rows` and `known_rhs`: optional paired K (k,m), h (k,).

The sign convention is A z+B q+b=0. Attribution is applied to the original higher
matrix A and target b, not to an implicitly source-augmented matrix. Supply a
different explicit matrix if that is the desired question.

`--absolute`, `--relative`, `--source-absolute` and `--tolerance` expose numerical
thresholds. Compare scaling and singular gaps before interpreting ranks. The
compatibility criterion is norm(full residual) <= tolerance*(1+norm(b)).

Without enforcement flags the tool returns diagnostics even for incompatible or
nonunique systems. `--require-compatible` and `--require-unique-source` produce
exit code 2 when the corresponding check fails, while retaining the report.
Invalid inputs also fail rather than being coerced to a plausible result. NPZ
object arrays are forbidden. Output cannot overwrite the input dataset.

The JSON records input/implementation hashes, NumPy version, full singular values,
cutoffs, source values and residual diagnostics. Complex source values are encoded
as separate `real` and `imag` lists. No field theory, units, packing or derivative
order can be inferred from an unlabelled matrix: retain those in the calling audit.

## Python

```python
system = eliminate(A, B, services=services)
fit = fit_sources(system, b, require_unique=True, require_compatible=True)
attribution = attribute_left_space(system, K, h, b)
```

Omit `services` outside an existing dependency-injection setup. `fit` includes
the full residual and a higher correction as arrays. The attribution helper
returns errors, not an unconditional success/proof flag. It tolerates redundant
known rows but reports whether they actually span the full left kernel.
