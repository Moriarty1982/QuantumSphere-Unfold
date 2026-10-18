"""Finite normal-spinor Hessian gate; comparison action only, not PDE existence."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "normal_hessian_prior", Path(__file__).with_name("HC_Cartan_Cauchy_Next_Completion.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)


def input_fingerprints():
    result = prior.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Cauchy_Next_Completion.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def central_jacobian(function, point, step=0.25):
    point = np.asarray(point, dtype=float)
    columns = []
    for i in range(point.size):
        direction = np.zeros_like(point)
        direction[i] = step
        columns.append((function(point+direction)-function(point-direction))/(2*step))
    return np.column_stack(columns)


def evaluate(*, services=None, iterations=4):
    services = prior._resolve_services(services)
    fingerprints = input_fingerprints()
    report = json.loads(Path(__file__).with_name(
        "HC_Cartan_Cauchy_Next_Completion.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Next-completion report has stale inputs")
    prepared, point, _, _, _ = prior.source.neighborhood.load_data()
    reduction = prior.source.normal.build_reduction(prepared, point)
    changed = prior.source.normal.remaining.normal_point(
        point, reduction["sources"] @ np.asarray(report["source_values"]))
    coordinates = np.asarray(report["starting_coordinates"])
    highest = np.asarray(report["starting_highest"])
    lc = prior.joint.third.lc_cubic(prepared, changed)
    high = prior.highest_matrix(prepared, services=services)
    assembled = prior.reprepare_matrix(
        prepared, changed, coordinates, highest, lc, high, services=services)
    indices = prior.source.allowed_cauchy_coordinates()["psi2"]

    def fields(p, w=None):
        c = coordinates.copy()
        c[indices] += p
        h = highest
        if w is not None:
            c, h = assembled.apply(c, h, w)
        return prior.evaluate_fields(prepared, changed, c, h, lc)

    def residual(p):
        return fields(p)["vector"]

    matrix = assembled.matrix
    left, singular, right = services.svd(matrix, full_matrices=False)
    cutoff = max(1e-9, singular[0]*1e-10)
    rank = int(np.sum(singular > cutoff))
    inverse = (right[:rank].T/singular[:rank]) @ left[:, :rank].T
    gate = left[:, rank:]
    rng = np.random.default_rng(181096)
    p_trial = rng.normal(size=len(indices))*.03
    w_trial = rng.normal(size=matrix.shape[1])*.03
    mixed_error = np.linalg.norm(fields(p_trial, w_trial)["vector"]
                                 -residual(p_trial)-matrix @ w_trial)
    f0 = residual(np.zeros(len(indices)))
    # A cubic central difference vanishes on every line for a quadratic map.
    third_difference = residual(3*p_trial)-3*residual(2*p_trial)+3*residual(p_trial)-f0
    quadratic_controls = []
    for scale in (.03, .3, 1.):
        direction = rng.normal(size=len(indices))*scale
        second = (residual(direction)+residual(-direction)-2*f0)/2
        quadratic_controls.append({"direction_norm": float(np.linalg.norm(direction)),
            "quadratic_norm": float(np.linalg.norm(second)),
            "old_and_euler_quadratic_norm": float(np.linalg.norm(second[:794])),
            "projected_quadratic_norm": float(np.linalg.norm(gate.T @ second))})
    if mixed_error > 1e-7:
        raise ValueError("Normal Hessian changes the older response: fixed-matrix elimination invalid")
    p = np.zeros(len(indices))
    history = []
    for _ in range(iterations):
        base = residual(p)
        reduced = gate.T @ base
        jac = central_jacobian(residual, p)
        solve = prior.solve_affine(gate.T @ jac, reduced, services=services)
        history.append(dict(prior.solve_report(solve), gate_norm=float(np.linalg.norm(reduced))))
        if np.linalg.norm(reduced) < 1e-8:
            break
        step = solve["solution"]
        if np.linalg.norm(step) < 1e-9:
            history[-1]["stopped_small_step"] = True
            break
        accepted = False
        for scale in (1., .5, .25, .125, .0625):
            candidate = p+scale*step
            if np.linalg.norm(candidate) > 1e4:
                continue
            if np.linalg.norm(gate.T @ residual(candidate)) < np.linalg.norm(reduced):
                p = candidate
                history[-1]["accepted_scale"] = scale
                accepted = True
                break
        if not accepted:
            history[-1]["accepted_scale"] = None
            break
    w = -inverse @ residual(p)
    actual = fields(p, w)
    c = coordinates.copy()
    c[indices] += p
    c, h = assembled.apply(c, highest, w)
    fixed_c = np.setdiff1d(np.arange(1200), list(assembled.older)+indices)
    fixed_h = np.setdiff1d(np.arange(1720), assembled.highest)
    if fingerprints != input_fingerprints():
        raise RuntimeError("Normal Hessian inputs changed during computation")
    return {"scope": "Fixed-source finite normal-psi2 gate, neutral commuting-spinor comparison only",
            "input_sha256": fingerprints, "normal_psi2_count": len(indices),
            "affine_response_shape": list(matrix.shape), "affine_response_rank": rank,
            "left_gate_dimension": gate.shape[1], "mixed_response_error": float(mixed_error),
            "third_difference_norm": float(np.linalg.norm(third_difference)),
            "quadratic_controls": quadratic_controls,
            "initial_gate_norm": float(np.linalg.norm(gate.T @ f0)),
            "history": history, "final": prior.norm_report(actual),
            "final_gate_norm": float(np.linalg.norm(gate.T @ residual(p))),
            "elimination_error": float(np.linalg.norm(actual["vector"]-residual(p)-matrix @ w)),
            "preserved_earlier_error": float(np.linalg.norm(c[fixed_c]-coordinates[fixed_c])),
            "preserved_highest_error": float(np.linalg.norm(h[fixed_h]-highest[fixed_h])),
            "normal_increment": p.tolist(), "linear_increment": w.tolist(),
            "fitted_coordinates": c.tolist(), "fitted_highest": h.tolist(),
            "not_general_nonexistence_or_regional_evolution": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--iterations", type=int, default=4)
    args = parser.parse_args()
    if args.iterations < 1:
        parser.error("--iterations must be positive")
    services = prior.create_container().services()
    result = evaluate(services=services, iterations=args.iterations)
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k not in (
        "input_sha256", "normal_increment", "linear_increment", "fitted_coordinates", "fitted_highest")}))


if __name__ == "__main__":
    main()
