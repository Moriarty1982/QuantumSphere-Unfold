"""Complete polynomial coefficient audit of the fixed-data normal Hessian gate."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "complete_quadratic_hessian", Path(__file__).with_name("HC_Cartan_Normal_Hessian_Completion.py"))
hessian = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(hessian)
prior = hessian.prior


def input_fingerprints():
    result = hessian.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Normal_Hessian_Completion.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def normal_basis():
    indices = prior.source.allowed_cauchy_coordinates()["psi2"]
    return np.array([prior.regular.unpack(v)["p2"] for v in np.eye(1200)[indices]])


def quadratic_coefficients(basis, selector, weights, triples):
    """C3 coefficients for monomials p_i*p_j, i<=j, not divided differences."""
    rows = []
    for r, s, t in triples:
        value = np.zeros((4, 4, len(basis), len(basis)), dtype=complex)
        for i, j, k in ((r, s, t), (s, r, t), (t, r, s)):
            if not np.any(basis[:, j, k]) or not np.any(basis[:, i]):
                continue
            value += np.einsum("puv,uw,qmwk,avk->ampq", basis[:, j, k].conj(),
                               selector, basis[:, i], weights, optimize=True)
        rows.append((value+value.swapaxes(-1, -2)).imag)
    tensor = np.asarray(rows).reshape(320, len(basis), len(basis))
    first, second = np.triu_indices(len(basis))
    coefficients = tensor[:, first, second].copy()
    coefficients[:, first == second] *= .5
    return coefficients


def monomials(point):
    first, second = np.triu_indices(len(point))
    return point[first]*point[second]


def load_problem(services):
    report = json.loads(Path(__file__).with_name(
        "HC_Cartan_Cauchy_Next_Completion.json").read_text(encoding="utf-8"))
    saved_hessian = json.loads(Path(__file__).with_name(
        "HC_Cartan_Normal_Hessian_Completion.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Stale next-completion report")
    if saved_hessian["input_sha256"] != hessian.input_fingerprints():
        raise ValueError("Stale normal-Hessian report")
    prepared, point, _, _, _ = prior.source.neighborhood.load_data()
    sources = prior.source.normal.build_reduction(prepared, point)["sources"]
    changed = prior.source.normal.remaining.normal_point(point, sources @ np.array(report["source_values"]))
    coordinates = np.array(report["starting_coordinates"])
    highest = np.array(report["starting_highest"])
    lc = prior.joint.third.lc_cubic(prepared, changed)
    high = prior.highest_matrix(prepared, services=services)
    assembled = prior.reprepare_matrix(
        prepared, changed, coordinates, highest, lc, high, services=services)
    indices = prior.source.allowed_cauchy_coordinates()["psi2"]

    def residual(p, w=None):
        c = coordinates.copy()
        c[indices] += p
        h = highest
        if w is not None:
            c, h = assembled.apply(c, h, w)
        return prior.evaluate_fields(prepared, changed, c, h, lc)["vector"]

    return prepared, assembled, residual


def evaluate(*, services=None):
    services = prior._resolve_services(services)
    fingerprints = input_fingerprints()
    prepared, assembled, residual = load_problem(services)
    scalar = prior.joint.third.scalar
    coefficients = services.cached("Cartan.complete-normal-quadratic/v1", {
        "sources": fingerprints, "numpy": np.__version__}, lambda: {
            "coefficients": quadratic_coefficients(normal_basis(), scalar.Q,
                np.asarray(scalar.odd.readouts.dirac.WEIGHTS), prior.joint.third.TRIPLES)})["coefficients"]
    jacobian = services.cached("Cartan.complete-normal-jacobian/v1", {
        "sources": fingerprints, "numpy": np.__version__}, lambda: {
            "jacobian": hessian.central_jacobian(residual, np.zeros(96))})["jacobian"]
    left, singular, _ = services.svd(assembled.matrix, full_matrices=False)
    rank = int(np.sum(singular > max(1e-9, singular[0]*1e-10)))
    gate = left[:, rank:]
    projected = gate[794:].T @ coefficients
    base = residual(np.zeros(96))
    reduced_jacobian = gate.T @ jacobian
    solved = prior.solve_affine(reduced_jacobian, gate.T @ base, services=services)
    remainder = solved["remainder"]
    witness = gate @ remainder/np.linalg.norm(remainder)
    rng = np.random.default_rng(19104656)
    controls = []
    for amplitude in (.03, .3, 1.):
        p = rng.normal(size=96)*amplitude
        w = rng.normal(size=1168)*.01
        quadratic = coefficients @ monomials(p)
        prediction = base+jacobian @ p+assembled.matrix @ w
        prediction[794:] += quadratic
        actual = residual(p, w)
        controls.append({"p_norm": float(np.linalg.norm(p)),
            "full_polynomial_error": float(np.linalg.norm(actual-prediction)),
            "witness_value": float(witness @ actual),
            "quadratic_witness_value": float(witness[794:] @ quadratic)})
    blocks = {"C1": (0, 64), "R1": (64, 160), "FE1": (160, 224),
              "C2": (224, 384), "scalar_Hessian": (384, 394),
              "R2": (394, 634), "FE2": (634, 794), "C3": (794, 1114)}
    if fingerprints != input_fingerprints():
        raise RuntimeError("Polynomial audit inputs changed")
    return {"scope": "Complete finite coefficient audit, fixed-source prescribed-tangential comparison only",
        "input_sha256": fingerprints, "quadratic_coefficient_shape": list(coefficients.shape),
        "quadratic_coefficient_norm": float(np.linalg.norm(coefficients)),
        "projected_coefficient_shape": list(projected.shape),
        "projected_coefficient_norm": float(np.linalg.norm(projected)),
        "maximum_projected_column_norm": float(np.linalg.norm(projected, axis=0).max()),
        "A_rank": rank, "gate_jacobian": prior.solve_report(solved),
        "witness_norm": float(np.linalg.norm(witness)),
        "witness_base_value": float(witness @ base),
        "witness_A_error": float(np.linalg.norm(witness @ assembled.matrix)),
        "witness_J_error": float(np.linalg.norm(witness @ jacobian)),
        "witness_quadratic_coefficient_error": float(np.linalg.norm(witness[794:] @ coefficients)),
        "witness_block_norms": {key: float(np.linalg.norm(witness[a:b])) for key, (a, b) in blocks.items()},
        "witness": witness.tolist(), "controls": controls,
        "exact_statement": "If yA=0, yJ=0, yQ_coeff=0 and yb!=0 exactly, F(p,w)=0 is impossible for these fixed data",
        "floating_point_evidence_not_exact_or_interval_certificate": True,
        "not_regional_existence_or_general_nonexistence": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    services = prior.create_container().services()
    result = evaluate(services=services)
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k not in ("input_sha256", "witness")}))


if __name__ == "__main__":
    main()
