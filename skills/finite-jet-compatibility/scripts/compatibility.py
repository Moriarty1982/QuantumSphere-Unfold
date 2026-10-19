"""Finite-dimensional compatibility diagnostics; numerical ranks are not proofs."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np


def _matrix(value, name, *, rows=None, allow_empty=False):
    result = np.asarray(value)
    if result.ndim != 2 or result.dtype.kind not in "fciub":
        raise ValueError(f"{name} must be a numeric matrix")
    if (rows is not None and result.shape[0] != rows
            or result.shape[0] == 0 or (result.shape[1] == 0 and not allow_empty)):
        raise ValueError(f"{name} has incompatible or empty dimensions")
    if not np.all(np.isfinite(result)):
        raise ValueError(f"{name} must be finite")
    return result.astype(np.complex128 if np.iscomplexobj(result) else np.float64)


def _vector(value, size, name):
    result = np.asarray(value)
    if result.shape != (size,) or result.dtype.kind not in "fciub" or not np.all(np.isfinite(result)):
        raise ValueError(f"{name} must be a finite numeric vector of length {size}")
    return result.astype(np.complex128 if np.iscomplexobj(result) else np.float64)


def _tolerance(value):
    if not np.isscalar(value) or not np.isreal(value) or not np.isfinite(value) or value < 0:
        raise ValueError("Tolerances must be finite nonnegative real scalars")
    return float(value)


def _svd(matrix, services=None):
    # Economy U is already complete for wide matrices, but not for tall ones.
    full = matrix.shape[0] > matrix.shape[1]
    if services is not None:
        return services.svd(matrix, full_matrices=full)
    return np.linalg.svd(matrix, full_matrices=full)


def _decompose(matrix, absolute, relative, services=None):
    left, singular, right = _svd(matrix, services)
    cutoff = max(_tolerance(absolute), _tolerance(relative)*(singular[0] if singular.size else 0))
    rank = int(np.sum(singular > cutoff))
    inverse = (right[:rank].conj().T/singular[:rank]) @ left[:, :rank].conj().T
    return {"rank": rank, "cutoff": cutoff, "singular": singular,
            "inverse": inverse, "left_null": left[:, rank:]}


def eliminate(matrix, source=None, *, absolute=1e-9, relative=1e-10,
              source_absolute=1e-8, source_relative=1e-10, services=None):
    """For A z + B q + b=0, eliminate z before assessing source coordinates q.

    Optional services provides svd(matrix, full_matrices=...), matching the
    repository's injected numerical services. No global container is resolved.
    """
    matrix = _matrix(matrix, "matrix")
    source = (np.zeros((matrix.shape[0], 0)) if source is None else
              _matrix(source, "source", rows=matrix.shape[0], allow_empty=True))
    result = _decompose(matrix, absolute, relative, services)
    gate = result["left_null"].conj().T @ source
    if min(gate.shape) == 0:
        source_rank, source_singular = 0, np.empty(0)
        source_inverse = np.zeros((source.shape[1], gate.shape[0]), dtype=gate.dtype)
        source_cutoff = _tolerance(source_absolute)
        _tolerance(source_relative)
    else:
        reduced = _decompose(gate, source_absolute, source_relative, services)
        source_rank, source_singular = reduced["rank"], reduced["singular"]
        source_inverse, source_cutoff = reduced["inverse"], reduced["cutoff"]
    return dict(result, matrix=matrix, source=source, source_gate=gate,
                source_rank=source_rank, source_singular=source_singular,
                source_inverse=source_inverse, source_cutoff=source_cutoff)


def fit_sources(system, target, *, tolerance=1e-8, require_unique=False,
                require_compatible=False):
    """Return a least-squares diagnostic, never silently certify a bad fit."""
    target = _vector(target, system["matrix"].shape[0], "target")
    tolerance = _tolerance(tolerance)
    unique = system["source_rank"] == system["source"].shape[1]
    if require_unique and not unique:
        raise ValueError("The eliminated source gate is not injective")
    projected = system["left_null"].conj().T @ target
    q = -system["source_inverse"] @ projected
    higher = -system["inverse"] @ (target+system["source"] @ q)
    residual = target+system["matrix"] @ higher+system["source"] @ q
    norm = float(np.linalg.norm(residual))
    limit = tolerance*(1+float(np.linalg.norm(target)))
    compatible = norm <= limit
    if require_compatible and not compatible:
        raise ValueError(f"Remaining full compatibility residual {norm:.6g} exceeds {limit:.6g}")
    return {"sources": q, "higher_increment": higher, "residual": residual,
            "residual_norm": norm, "compatibility_limit": limit,
            "compatible": compatible, "unique_sources": unique}


def attribute_left_space(system, known_rows, known_rhs, target, *,
                         absolute=1e-9, relative=1e-10, services=None):
    """Diagnose K A=0 and K b=h, retaining h rather than assuming it vanishes.

    Redundant known rows are allowed. A matching dimension alone is insufficient:
    span, annihilation, identity and reconstruction errors are all returned.
    """
    matrix = system["matrix"]
    known_rows = _matrix(known_rows, "known_rows")
    if known_rows.shape[1] != matrix.shape[0]:
        raise ValueError("known_rows must act on the equation space")
    rhs = _vector(known_rhs, known_rows.shape[0], "known_rhs")
    target = _vector(target, matrix.shape[0], "target")
    known = _decompose(known_rows, absolute, relative, services)
    projector = system["left_null"] @ system["left_null"].conj().T
    known_projector = known["inverse"] @ known_rows
    incompatible = projector @ target
    predicted = known["inverse"] @ rhs
    return {"known_rank": known["rank"], "left_nullity": system["left_null"].shape[1],
            "annihilation_error": float(np.linalg.norm(known_rows @ matrix)),
            "span_error": float(np.linalg.norm(known_projector-projector)),
            "identity_error": float(np.linalg.norm(known_rows @ target-rhs)),
            "reconstruction_error": float(np.linalg.norm(predicted-incompatible)),
            "incompatible_norm": float(np.linalg.norm(incompatible))}


def _json_vector(value):
    if np.iscomplexobj(value):
        return {"real": value.real.tolist(), "imag": value.imag.tolist()}
    return value.tolist()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="NPZ with matrix, target and optional source/known_rows/known_rhs")
    parser.add_argument("--output", type=Path, help="JSON report; otherwise stdout")
    parser.add_argument("--absolute", type=float, default=1e-9)
    parser.add_argument("--relative", type=float, default=1e-10)
    parser.add_argument("--source-absolute", type=float, default=1e-8)
    parser.add_argument("--tolerance", type=float, default=1e-8)
    parser.add_argument("--require-compatible", action="store_true")
    parser.add_argument("--require-unique-source", action="store_true")
    args = parser.parse_args(argv)
    try:
        with np.load(args.input, allow_pickle=False) as data:
            system = eliminate(data["matrix"], data["source"] if "source" in data else None,
                               absolute=args.absolute, relative=args.relative, source_absolute=args.source_absolute)
            fitted = fit_sources(system, data["target"], tolerance=args.tolerance)
            report = {"scope": "finite-dimensional numeric compatibility, not a regional or physical proof",
                "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
                "implementation_sha256": hashlib.sha256(Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest(),
                "numpy_version": np.__version__, "shape": list(system["matrix"].shape),
                "higher_rank": system["rank"], "rank_cutoff": system["cutoff"],
                "higher_singular_values": system["singular"].tolist(),
                "left_nullity": system["left_null"].shape[1], "source_rank": system["source_rank"],
                "source_rank_cutoff": system["source_cutoff"],
                "source_singular_values": system["source_singular"].tolist(),
                "compatible": fitted["compatible"], "unique_sources": fitted["unique_sources"],
                "full_residual_norm": fitted["residual_norm"], "compatibility_limit": fitted["compatibility_limit"],
                "source_values": _json_vector(fitted["sources"]),
                "higher_increment_norm": float(np.linalg.norm(fitted["higher_increment"]))}
            if ("known_rows" in data) != ("known_rhs" in data):
                raise ValueError("known_rows and known_rhs must be supplied together")
            if "known_rows" in data:
                report["attribution"] = attribute_left_space(system, data["known_rows"], data["known_rhs"],
                    data["target"], absolute=args.absolute, relative=args.relative)
        output = json.dumps(report, indent=2, allow_nan=False)+"\n"
        if args.output:
            if args.output.resolve() == args.input.resolve():
                raise ValueError("Output must not overwrite the input dataset")
            args.output.write_text(output, encoding="utf-8")
        else:
            print(output, end="")
        return 2 if ((args.require_compatible and not fitted["compatible"])
                     or (args.require_unique_source and not fitted["unique_sources"])) else 0
    except (ValueError, KeyError, OSError, np.linalg.LinAlgError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    raise SystemExit(main())
