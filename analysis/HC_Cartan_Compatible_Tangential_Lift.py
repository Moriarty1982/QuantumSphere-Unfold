"""Search new compatible higher data with the lower source point fixed.

All higher jets may change; no regional Cauchy solution is claimed.
"""
import argparse
from concurrent.futures import ProcessPoolExecutor
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "compatible_lift_quadratic", Path(__file__).with_name("HC_Cartan_Complete_Quadratic_Gate.py"))
quadratic = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(quadratic)
prior = quadratic.prior
WORKER_FIELDS = None


def input_fingerprints():
    result = quadratic.input_fingerprints()
    result[Path(__file__).name] = hashlib.sha256(
        Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


def _initialize_worker(prepared, point, coordinates, highest, lc, base):
    global WORKER_FIELDS
    WORKER_FIELDS = prepared, point, coordinates, highest, lc, base


def _column(task):
    kind, index = task
    prepared, point, coordinates, highest, lc, base = WORKER_FIELDS
    changed = coordinates.copy()
    if kind == "older":
        changed[index] += 64.
        value = (prior.evaluate_fields(prepared, point, changed, highest, lc)["vector"]-base)/64.
    else:
        changed[index] += .25
        plus = prior.evaluate_fields(prepared, point, changed, highest, lc)["vector"]
        changed[index] -= .5
        minus = prior.evaluate_fields(prepared, point, changed, highest, lc)["vector"]
        value = (plus-minus)/.5
    return kind, index, value


def higher_response(prepared, point, coordinates, highest, lc, masked, high, *, services, workers):
    def build():
        base = prior.evaluate_fields(prepared, point, coordinates, highest, lc)["vector"]
        older = np.zeros((1114, 960))
        older[:, np.array(masked.older)-240] = masked.matrix[:, :masked.older_count]
        missing = sorted(set(range(240, 1200))-set(masked.older))
        tasks = [("older", i) for i in missing]+[("psi2", i) for i in range(240)]
        jacobian = np.zeros((1114, 240))
        args = (prepared, point, coordinates, highest, lc, base)
        print(f"Building {len(missing)} additional earlier columns and 240 spinor columns with {workers} workers", flush=True)
        if workers == 1:
            _initialize_worker(*args)
            results = map(_column, tasks)
            for kind, index, value in results:
                (older if kind == "older" else jacobian)[:, index-240 if kind == "older" else index] = value
        else:
            with ProcessPoolExecutor(max_workers=workers, initializer=_initialize_worker, initargs=args) as pool:
                for kind, index, value in pool.map(_column, tasks, chunksize=8):
                    (older if kind == "older" else jacobian)[:, index-240 if kind == "older" else index] = value
        full_high = np.vstack((np.zeros((394, 1720)), high))
        return {"matrix": np.column_stack((older, full_high)), "jacobian": jacobian, "base": base}
    return services.cached("Cartan.compatible-tangential-response/v1", {
        "sources": input_fingerprints(), "numpy": np.__version__,
        "prepared": prepared, "point": point, "coordinates": coordinates, "highest": highest}, build)


def spinor_basis():
    return np.array([prior.regular.unpack(v)["p2"] for v in np.eye(1200)[:240]])


def spinor_quadratic(p, basis, selector, weights):
    tensor = np.einsum("p,prsuq->rsuq", p, basis)
    values = []
    for r, s, t in prior.joint.third.TRIPLES:
        value = np.zeros((4, 4), dtype=complex)
        for i, j, k in ((r, s, t), (s, r, t), (t, r, s)):
            value += np.einsum("uv,uw,mwk,avk->am", tensor[j, k].conj(), selector,
                               tensor[i], weights, optimize=True)
        values.append(value.imag)
    return np.asarray(values).reshape(320)


def spinor_quadratic_jacobian(p, basis, selector, weights):
    tensor = np.einsum("p,prsuq->rsuq", p, basis)
    rows = []
    for r, s, t in prior.joint.third.TRIPLES:
        value = np.zeros((4, 4, len(basis)), dtype=complex)
        for i, j, k in ((r, s, t), (s, r, t), (t, r, s)):
            value += np.einsum("duv,uw,mwk,avk->amd", basis[:, j, k].conj(),
                               selector, tensor[i], weights, optimize=True)
            value += np.einsum("uv,uw,dmwk,avk->amd", tensor[j, k].conj(),
                               selector, basis[:, i], weights, optimize=True)
        rows.append(value.imag)
    return np.asarray(rows).reshape(320, len(basis))


def apply_increment(coordinates, highest, p, w):
    c, h = coordinates.copy(), highest.copy()
    c[:240] += p
    c[240:] += w[:960]
    h += w[960:]
    return c, h


def evaluate(*, services=None, workers=2, iterations=8):
    services = prior._resolve_services(services)
    fingerprints = input_fingerprints()
    prepared, masked, _ = quadratic.load_problem(services)
    before = json.loads(Path(__file__).with_name("HC_Cartan_Cauchy_Next_Completion.json").read_text(encoding="utf-8"))
    _, point, _, _, saved = prior.source.neighborhood.load_data()
    source_values = np.array(before["source_values"])
    sources = prior.source.normal.build_reduction(prepared, point)["sources"]
    changed = prior.source.normal.remaining.normal_point(point, sources @ source_values)
    coordinates = np.array(saved["jet_coordinates"])
    highest = np.concatenate((saved["connection_coordinates"], np.asarray(saved["fourth_spinor_real"]).reshape(-1)))
    lc = prior.joint.third.lc_cubic(prepared, changed)
    high = prior.highest_matrix(prepared, services=services)
    response = higher_response(prepared, changed, coordinates, highest, lc, masked, high,
                               services=services, workers=workers)
    matrix, jacobian, base = (response[k] for k in ("matrix", "jacobian", "base"))
    left, singular, right = services.svd(matrix, full_matrices=False)
    cutoff = max(1e-9, singular[0]*1e-10)
    rank = int(np.sum(singular > cutoff))
    inverse = (right[:rank].T/singular[:rank]) @ left[:, :rank].T
    gate = left[:, rank:]
    scalar = prior.joint.third.scalar
    basis = spinor_basis()
    selector, weights = scalar.Q, np.asarray(scalar.odd.readouts.dirac.WEIGHTS)

    def polynomial(p):
        value = base+jacobian @ p
        value[794:] += spinor_quadratic(p, basis, selector, weights)
        return value

    def direct(p, w):
        c, h = apply_increment(coordinates, highest, p, w)
        return prior.evaluate_fields(prepared, changed, c, h, lc)

    rng = np.random.default_rng(19102920)
    control_p = rng.normal(size=240)*.03
    control_w = rng.normal(size=2680)*.03
    polynomial_error = np.linalg.norm(direct(control_p, control_w)["vector"]
                                     -polynomial(control_p)-matrix @ control_w)
    if polynomial_error > 1e-7:
        raise ValueError("Expanded polynomial does not match the full evaluator")
    p = np.zeros(240)
    history = []
    for _ in range(iterations):
        remainder = gate.T @ polynomial(p)
        derivative = jacobian.copy()
        derivative[794:] += spinor_quadratic_jacobian(p, basis, selector, weights)
        solved = prior.solve_affine(gate.T @ derivative, remainder, services=services)
        history.append(dict(prior.solve_report(solved), gate_norm=float(np.linalg.norm(remainder))))
        if np.linalg.norm(remainder) < 1e-8 or np.linalg.norm(solved["solution"]) < 1e-10:
            break
        accepted = False
        for scale in (1., .5, .25, .125, .0625, .03125):
            trial = p+scale*solved["solution"]
            if np.linalg.norm(trial) > 1e4:
                continue
            if np.linalg.norm(gate.T @ polynomial(trial)) < np.linalg.norm(remainder):
                p = trial
                history[-1]["accepted_scale"] = scale
                accepted = True
                break
        if not accepted:
            history[-1]["accepted_scale"] = None
            break
    w = -inverse @ polynomial(p)
    refinement = []
    for _ in range(3):
        actual = direct(p, w)
        refinement.append(float(np.linalg.norm(actual["vector"])))
        if refinement[-1] < 1e-8:
            break
        correction = -inverse @ actual["vector"]
        if np.linalg.norm(correction) < 1e-10:
            break
        w += correction
    actual = direct(p, w)
    c, h = apply_increment(coordinates, highest, p, w)
    old_free = sum(prior.source.allowed_cauchy_coordinates().values(), [])
    old_fixed = np.setdiff1d(np.arange(1200), old_free)
    high_fixed = np.setdiff1d(np.arange(1720), sum(prior.highest_mask().values(), []))
    spatial = [794+16*t+4*a+mu for t, triple in enumerate(prior.joint.third.TRIPLES)
               if 0 not in triple for a in range(4) for mu in (1, 2, 3)]
    lower_norm = float(np.linalg.norm(prior.source.normal.normal_equations(prepared, changed)))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Compatible-data inputs changed")
    return {"scope": "New higher tangential data at fixed six-source lower point, finite comparison only",
        "input_sha256": fingerprints, "source_values": source_values.tolist(),
        "matrix_shape": list(matrix.shape), "matrix_rank": rank, "left_gate_dimension": gate.shape[1],
        "free_psi2_count": 240, "free_other_earlier_count": 960, "free_highest_count": 1720,
        "polynomial_control_error": float(polynomial_error), "history": history,
        "refinement_history": refinement, "final": prior.norm_report(actual),
        "all_68_lower_norm": lower_norm, "all_384_norm": float(np.linalg.norm(actual["old"][:384])),
        "spatial_C3_norm": float(np.linalg.norm(actual["vector"][spatial])),
        "numerically_completed": bool(np.linalg.norm(actual["vector"]) < 1e-7 and lower_norm < 1e-7),
        "earlier_tangential_change_from_original": float(np.linalg.norm((c-coordinates)[old_fixed])),
        "highest_tangential_change_from_original": float(np.linalg.norm((h-highest)[high_fixed])),
        "earlier_tangential_change_from_rejected_witness": float(np.linalg.norm(
            (c-np.array(before["starting_coordinates"]))[old_fixed])),
        "psi2_increment_norm": float(np.linalg.norm(p)), "other_increment_norm": float(np.linalg.norm(w)),
        "fitted_coordinates": c.tolist(), "fitted_highest": h.tolist(),
        "lower_point_changed_during_fit": False, "tangential_data_changed": True,
        "not_preservation_of_previous_prescribed_germ": True,
        "not_regional_existence_native_action_or_scale_identification": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--workers", type=int, choices=(1, 2), default=2)
    parser.add_argument("--iterations", type=int, default=8)
    args = parser.parse_args()
    if args.iterations < 1:
        parser.error("--iterations must be positive")
    result = evaluate(services=prior.create_container().services(), workers=args.workers, iterations=args.iterations)
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k not in ("input_sha256", "fitted_coordinates", "fitted_highest")}))


if __name__ == "__main__":
    main()
