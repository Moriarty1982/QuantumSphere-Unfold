"""Next finite Cartan completion with prescribed tangential jets.

Fixed comparison action and lower source point. No regional PDE claim.
"""
import argparse
from dataclasses import dataclass
import hashlib
import importlib.util
import json
import os
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "next_cauchy_sources", Path(__file__).with_name("HC_Cartan_Normal_Source_Compatibility.py"))
source = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(source)
joint = source.neighborhood.joint
regular = source.regular
CACHE_SPEC = importlib.util.spec_from_file_location(
    "next_cauchy_cache", Path(__file__).with_name("Numerical_Matrix_Cache.py"))
cache = importlib.util.module_from_spec(CACHE_SPEC)
CACHE_SPEC.loader.exec_module(cache)
DEPENDENCIES_SPEC = importlib.util.spec_from_file_location(
    "next_cauchy_dependencies", Path(__file__).with_name("Numerical_Dependencies.py"))
dependencies = importlib.util.module_from_spec(DEPENDENCIES_SPEC)
DEPENDENCIES_SPEC.loader.exec_module(dependencies)


def create_container(cache_root=None, *, cache_enabled=None, matrix_cache=None, svd_backend=None):
    """Compose one explicit numerical scope at the application boundary."""
    if matrix_cache is not None and (cache_root is not None or cache_enabled is not None):
        raise ValueError("Configure either an injected cache or cache construction options")
    if matrix_cache is None:
        root = (Path(cache_root) if cache_root is not None else
                Path(__file__).resolve().parents[1] / "build/numerical-cache")
        enabled = os.environ.get("QSC_MATRIX_CACHE", "1") != "0" if cache_enabled is None else cache_enabled
        cache_factory = lambda: cache.MatrixCache(root, enabled=enabled)
    else:
        cache_factory = lambda: matrix_cache
    backend_factory = dependencies.NumPySVDBackend if svd_backend is None else lambda: svd_backend
    return dependencies.NumericalContainer(cache_factory, backend_factory)


def _resolve_services(services):
    if services is not None:
        return services
    # Preserve legacy helper callers; the CLI composes and injects an explicit scope.
    matrix_cache = cache.CACHE
    if os.environ.get("QSC_MATRIX_CACHE", "1") == "0":
        matrix_cache = cache.MatrixCache(matrix_cache.root, enabled=False)
    return create_container(matrix_cache=matrix_cache).services()


OLD_EQUATION_COUNT = 394
EARLIER_COORDINATE_COUNT = 1200
FIXED_SPINOR_COORDINATE_COUNT = 240
CONNECTION_COORDINATE_COUNT = 880
HIGHEST_COORDINATE_COUNT = 1720
COLUMN_STEP = 64.0


@dataclass(frozen=True, slots=True)
class AffineSystem:
    """One response matrix with explicit earlier/highest coordinate ownership."""
    matrix: np.ndarray
    base: np.ndarray
    older: tuple
    highest: tuple

    def __post_init__(self):
        if self.matrix.ndim != 2 or self.base.shape != (self.matrix.shape[0],):
            raise ValueError("Affine matrix and residual dimensions do not match")
        if self.matrix.shape[1] != len(self.older)+len(self.highest):
            raise ValueError("Affine coordinate ownership does not match its columns")
        if not np.all(np.isfinite(self.matrix)) or not np.all(np.isfinite(self.base)):
            raise ValueError("Affine system must contain finite numeric values")
        for indices, limit in ((self.older, EARLIER_COORDINATE_COUNT),
                               (self.highest, HIGHEST_COORDINATE_COUNT)):
            if (len(set(indices)) != len(indices)
                    or any(not isinstance(i, (int, np.integer)) or isinstance(i, (bool, np.bool_))
                           or not 0 <= i < limit for i in indices)):
                raise ValueError("Affine coordinate indices must be unique integers in range")

    @property
    def older_count(self):
        return len(self.older)

    def to_arrays(self):
        return {"matrix": self.matrix, "base": self.base,
                "older": np.asarray(self.older, dtype=np.int64),
                "highest": np.asarray(self.highest, dtype=np.int64)}

    @classmethod
    def from_arrays(cls, arrays):
        return cls(arrays["matrix"], arrays["base"],
                   tuple(arrays["older"].tolist()), tuple(arrays["highest"].tolist()))

    def apply(self, coordinates, highest, delta):
        delta = source.normal.cartan.checks._real(delta, (self.matrix.shape[1],), "affine increment")
        coordinates = source.normal.cartan.checks._real(
            coordinates, (EARLIER_COORDINATE_COUNT,), "earlier coordinates").copy()
        highest = source.normal.cartan.checks._real(
            highest, (HIGHEST_COORDINATE_COUNT,), "highest coordinates").copy()
        coordinates[list(self.older)] += delta[:self.older_count]
        highest[list(self.highest)] += delta[self.older_count:]
        return coordinates, highest


@dataclass(frozen=True, slots=True)
class SVDReduction:
    """Shared numerical rank decision and inverse for a fixed matrix."""
    matrix: np.ndarray
    singular: np.ndarray
    right_vectors: np.ndarray
    inverse: np.ndarray
    rank: int
    cutoff: float

    @classmethod
    def from_matrix(cls, matrix, *, retain_kernel=False, services=None):
        matrix = np.array(matrix, copy=True)
        if matrix.ndim != 2 or min(matrix.shape) == 0:
            raise ValueError("SVD reduction requires a nonempty matrix")
        full = retain_kernel and matrix.shape[0] < matrix.shape[1]
        left, singular, right = _resolve_services(services).svd(matrix, full_matrices=full)
        cutoff = max(1e-9, singular[0]*1e-10)
        rank = int(np.sum(singular > cutoff))
        inverse = (right[:rank].T/singular[:rank]) @ left[:, :rank].T
        matrix.setflags(write=False)
        return cls(matrix, singular, right, inverse, rank, cutoff)

    @property
    def kernel(self):
        if self.right_vectors.shape[0] != self.inverse.shape[0]:
            raise ValueError("A full right basis is required for the complete kernel")
        return self.right_vectors[self.rank:].T

    def solve(self, base):
        base = source.normal.cartan.checks._real(base, (self.matrix.shape[0],), "affine residual")
        solution = -self.inverse @ base
        return {"solution": solution, "inverse": self.inverse, "rank": self.rank,
                "singular": self.singular, "cutoff": self.cutoff,
                "remainder": base+self.matrix @ solution}


def input_fingerprints():
    result = source.input_fingerprints()
    for name in (Path(__file__).name, "Numerical_Matrix_Cache.py", "Numerical_Dependencies.py",
                 "HC_Cartan_Normal_Source_Compatibility.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def highest_mask():
    quads = joint.third.diagnostic.QUADS
    triples = joint.third.TRIPLES
    e4 = [16*i+j for i, q in enumerate(quads) if q.count(0) >= 2 for j in range(16)]
    l3 = [560+16*i+j for i, q in enumerate(triples) if 0 in q for j in range(16)]
    # psi4 is packed by quartet, each with its own 12 real + 12 imaginary entries.
    p4 = [880+24*i+j for i, q in enumerate(quads) if 0 in q for j in range(24)]
    return {"e4": e4, "l3": l3, "p4": p4}


def highest_matrix(prepared, *, services=None):
    return _resolve_services(services).cached("Cartan.highest-matrix/v1",
                        {"prepared": prepared, "sources": input_fingerprints(), "numpy": np.__version__},
                        lambda: {"matrix": _highest_matrix(prepared)})["matrix"]


def _highest_matrix(prepared):
    maps = joint.highest_maps(prepared)
    principal = source.spatial.constraint_principal_map(prepared["data"]["psi"])
    spinor = maps["symmetric"] @ np.kron(np.eye(35), principal)
    connection = np.vstack((maps["joint"][394:794], maps["connection"]))
    return np.column_stack((connection, np.vstack((np.zeros((400, 840)), spinor))))


def evaluate_fields(prepared, point, coordinates, highest, lc):
    highest = source.normal.cartan.checks._real(
        highest, (HIGHEST_COORDINATE_COUNT,), "E4/lambda3/psi4 coordinates")
    return joint.full_residual(prepared, point, coordinates, highest[:880],
                               highest[880:].reshape(35, 24), lc)


def solve_affine(matrix, base, *, services=None):
    matrix = np.asarray(matrix)
    return SVDReduction.from_matrix(matrix, services=services).solve(base)


def norm_report(result):
    return {"all_1114_norm": float(np.linalg.norm(result["vector"])),
            "old_394_norm": float(np.linalg.norm(result["old"])),
            "R2_norm": float(np.linalg.norm(result["probe"])),
            "FE2_norm": float(np.linalg.norm(result["gravity"])),
            "C3_norm": float(np.linalg.norm(result["constraint"]))}


def solve_report(solved):
    rank = solved["rank"]
    s = solved["singular"]
    return {"rank": rank, "rank_cutoff": solved["cutoff"],
            "smallest_retained_singular": float(s[rank-1]) if rank else None,
            "largest_discarded_singular": float(s[rank]) if rank < len(s) else None,
            "linear_minimum_residual_norm": float(np.linalg.norm(solved["remainder"])),
            "increment_norm": float(np.linalg.norm(solved["solution"]))}


def reprepare_matrix(prepared, point, coordinates, highest, lc, higher, *, services=None):
    def build():
        return _reprepare_matrix(prepared, point, coordinates, highest, lc, higher).to_arrays()
    result = _resolve_services(services).cached("Cartan.reprepare-matrix/v1", {
        "prepared": prepared, "point": point, "coordinates": coordinates,
        "highest": highest, "lc": lc, "higher": higher,
        "sources": input_fingerprints(), "numpy": np.__version__}, build)
    return AffineSystem.from_arrays(result)


def _reprepare_matrix(prepared, point, coordinates, highest, lc, higher):
    allowed = sum(source.allowed_cauchy_coordinates().values(), [])
    older = [i for i in allowed if i >= FIXED_SPINOR_COORDINATE_COUNT]
    base = evaluate_fields(prepared, point, coordinates, highest, lc)["vector"]
    columns = []
    # With psi2 fixed, all retained equations are affine in lambda2/E3/psi3.
    for i in older:
        changed = coordinates.copy()
        changed[i] += COLUMN_STEP
        columns.append((evaluate_fields(prepared, point, changed, highest, lc)["vector"]-base)/COLUMN_STEP)
    high_allowed = sum(highest_mask().values(), [])
    padded = np.vstack((np.zeros((OLD_EQUATION_COUNT, HIGHEST_COORDINATE_COUNT)), higher))
    matrix = np.column_stack((np.column_stack(columns), padded[:, high_allowed]))
    return AffineSystem(matrix, base, tuple(older), tuple(high_allowed))


def apply_increment(coordinates, highest, assembled, delta):
    return assembled.apply(coordinates, highest, delta)


def preserve_old_first(assembled, *, services=None):
    """Lexicographic solve; never trade old equations against new rows."""
    count = assembled.older_count
    matrix, base = assembled.matrix, assembled.base
    old = matrix[:OLD_EQUATION_COUNT, :count]
    reduction = SVDReduction.from_matrix(old, retain_kernel=True, services=services)
    particular = -reduction.inverse @ base[:OLD_EQUATION_COUNT]
    kernel = reduction.kernel
    tail = np.column_stack((matrix[OLD_EQUATION_COUNT:, :count] @ kernel,
                            matrix[OLD_EQUATION_COUNT:, count:]))
    tail_base = base[OLD_EQUATION_COUNT:]+matrix[OLD_EQUATION_COUNT:, :count] @ particular
    solved = solve_affine(tail, tail_base, services=services)
    size = kernel.shape[1]
    delta = np.concatenate((particular+kernel @ solved["solution"][:size], solved["solution"][size:]))
    return {"old_rank": reduction.rank, "old_kernel_dimension": size,
            "old_minimum_residual_norm": float(np.linalg.norm(base[:OLD_EQUATION_COUNT]+old @ particular)),
            "tail_solve": solved, "solution": delta}


def evaluate(*, services=None):
    services = _resolve_services(services)
    fingerprints = input_fingerprints()
    prepared, point, jets, _, saved = source.neighborhood.load_data()
    prior_path = Path(__file__).with_name("HC_Cartan_Normal_Source_Compatibility.json")
    prior_report = json.loads(prior_path.read_text(encoding="utf-8"))
    if prior_report["input_sha256"] != source.input_fingerprints():
        raise ValueError("Source witness report has stale inputs")
    reduction = source.normal.build_reduction(prepared, point)
    q = np.asarray(prior_report["example_source_values"])
    z = np.asarray(prior_report["example_higher_increment"])
    changed, _ = source.changed_fields(point, jets, reduction["sources"], q, z)
    coordinates = np.asarray(saved["jet_coordinates"])+z
    highest = np.concatenate((saved["connection_coordinates"],
                              np.asarray(saved["fourth_spinor_real"]).reshape(-1)))
    lc = joint.third.lc_cubic(prepared, changed)
    frozen = evaluate_fields(prepared, changed, coordinates, highest, lc)
    high = highest_matrix(prepared, services=services)
    high_allowed = sum(highest_mask().values(), [])
    highest_controls = {}
    for name, allowed in (("unrestricted_highest", list(range(1720))),
                          ("tangential_highest_fixed", high_allowed)):
        solved = solve_affine(high[:, allowed], frozen["vector"][394:], services=services)
        h = highest.copy()
        h[allowed] += solved["solution"]
        actual = evaluate_fields(prepared, changed, coordinates, h, lc)
        highest_controls[name] = dict(solve_report(solved), **norm_report(actual),
                                     allowed_highest_coordinates=len(allowed),
                                     affine_error=float(np.linalg.norm(actual["vector"][394:]
                                                                       -solved["remainder"])))
    assembled = reprepare_matrix(prepared, changed, coordinates, highest, lc, high, services=services)
    solved = solve_affine(assembled.matrix, assembled.base, services=services)
    fitted_c, fitted_h = apply_increment(coordinates, highest, assembled, solved["solution"])
    fitted = evaluate_fields(prepared, changed, fitted_c, fitted_h, lc)
    preserved_old = preserve_old_first(assembled, services=services)
    ordered_c, ordered_h = apply_increment(coordinates, highest, assembled, preserved_old["solution"])
    ordered = evaluate_fields(prepared, changed, ordered_c, ordered_h, lc)
    rng = np.random.default_rng(18101114)
    trial = rng.normal(size=assembled.matrix.shape[1])*.003
    trial_c, trial_h = apply_increment(coordinates, highest, assembled, trial)
    affine_error = float(np.linalg.norm(evaluate_fields(prepared, changed, trial_c, trial_h, lc)["vector"]
                                         -assembled.base-assembled.matrix @ trial))
    preserved = np.setdiff1d(np.arange(EARLIER_COORDINATE_COUNT), assembled.older)
    high_preserved = np.setdiff1d(np.arange(HIGHEST_COORDINATE_COUNT), assembled.highest)
    if fingerprints != input_fingerprints():
        raise RuntimeError("Next Cauchy completion inputs changed")
    return {"scope": "Fixed-source, fixed-psi2 finite next Cartan completion with prescribed tangential jets",
            "input_sha256": fingerprints, "source_values": q.tolist(),
            "highest_layout": "E4 560; lambda3 320; psi4 35 quartets x (12 real then 12 imaginary)",
            "highest_mask_counts": {k: len(v) for k, v in highest_mask().items()},
            "frozen_control": norm_report(frozen), "highest_only_controls": highest_controls,
            "reprepared": dict(solve_report(solved), **norm_report(fitted),
                               matrix_shape=list(assembled.matrix.shape),
                               earlier_allowed_count=assembled.older_count,
                               highest_allowed_count=len(assembled.highest),
                               simultaneous_affine_error=affine_error,
                               actual_linear_remainder_error=float(np.linalg.norm(fitted["vector"]-solved["remainder"])),
                               preserved_older_error=float(np.linalg.norm(fitted_c[preserved]-coordinates[preserved])),
                               preserved_highest_error=float(np.linalg.norm(fitted_h[high_preserved]-highest[high_preserved]))),
            "starting_coordinates": coordinates.tolist(), "starting_highest": highest.tolist(),
            "fitted_coordinates": fitted_c.tolist(), "fitted_highest": fitted_h.tolist(),
            "old_first": dict(solve_report(preserved_old["tail_solve"]), **norm_report(ordered),
                              old_response_rank=preserved_old["old_rank"],
                              old_kernel_dimension=preserved_old["old_kernel_dimension"],
                              old_minimum_residual_norm=preserved_old["old_minimum_residual_norm"]),
            "old_first_coordinates": ordered_c.tolist(), "old_first_highest": ordered_h.tolist(),
            "not_full_earlier_normal_jet_repreparation": True,
            "not_general_nonexistence_or_regional_evolution": True,
            "main_TeX_PDF_changed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--no-cache", action="store_true")
    parser.add_argument("--cache-stats", action="store_true")
    args = parser.parse_args()
    container = create_container(cache_enabled=False if args.no_cache else None)
    services = container.services()
    result = evaluate(services=services)
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("highest_mask_counts", "frozen_control",
                                                  "highest_only_controls", "reprepared", "old_first")}))
    if args.cache_stats:
        print(json.dumps({"matrix_cache": services.matrix_cache.stats,
                          "enabled": services.matrix_cache.enabled}))


if __name__ == "__main__":
    main()
