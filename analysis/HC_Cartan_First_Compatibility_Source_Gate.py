"""Test source identification using only first derivatives of the primary 68 rows.

Finite-jet comparison only; no regional propagation or physical identification.
"""
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "first_gate_lift", Path(__file__).with_name("HC_Cartan_Compatible_Tangential_Lift.py"))
lift = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(lift)
prior, source = lift.prior, lift.prior.source


def input_fingerprints():
    result = lift.input_fingerprints()
    for filename in (Path(__file__).name, "HC_Cartan_Compatible_Tangential_Lift.json"):
        result[filename] = hashlib.sha256(
            Path(__file__).with_name(filename).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


def extraction_matrix():
    """Pack d_r(C, Re R, Im R, FE, J_0i) from C1/R1/FE1/C2."""
    matrix = np.zeros((272, 384))
    pairs = list(source.prior.PAIR2)
    for r in range(4):
        start = 68*r
        matrix[start:start+16, 16*r:16*r+16] = np.eye(16)
        matrix[start+16:start+28, 64+12*r:76+12*r] = np.eye(12)
        matrix[start+28:start+40, 112+12*r:124+12*r] = np.eye(12)
        matrix[start+40:start+56, 160+16*r:176+16*r] = np.eye(16)
        for i in (1, 2, 3):
            time_pair = pairs.index(tuple(sorted((r, 0))))
            space_pair = pairs.index(tuple(sorted((r, i))))
            for a in range(4):
                row = start+56+4*(i-1)+a
                matrix[row, 224+16*time_pair+4*a+i] += 1
                matrix[row, 224+16*space_pair+4*a] -= 1
    return matrix


def eliminate(matrix, response):
    """Retain all left-null directions, including those of tall matrices."""
    left, singular, right = np.linalg.svd(matrix, full_matrices=True)
    cutoff = max(1e-9, singular[0]*1e-10)
    rank = int(np.sum(singular > cutoff))
    inverse = (right[:rank].T/singular[:rank]) @ left[:, :rank].T
    null = left[:, rank:]
    gate = null.T @ response
    values = np.linalg.svd(gate, compute_uv=False)
    return {"rank": rank, "inverse": inverse, "left_null": null,
            "gate": gate, "gate_rank": int(np.sum(values > 1e-8)),
            "gate_singular": values}


def load_system():
    services = prior.create_container().services()
    prepared, masked, _ = lift.quadratic.load_problem(services)
    _, point, jets, _, saved = source.neighborhood.load_data()
    report = json.loads(Path(__file__).with_name(
        "HC_Cartan_Compatible_Tangential_Lift.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != lift.input_fingerprints():
        raise ValueError("Stale compatible-lift report")
    coordinates = np.asarray(saved["jet_coordinates"])
    highest = np.concatenate((saved["connection_coordinates"],
                              np.asarray(saved["fourth_spinor_real"]).ravel()))
    reduction = source.normal.build_reduction(prepared, point)
    q = np.array([.01, -.005, .003, .002, .004, -.001])
    changed = source.normal.remaining.normal_point(point, reduction["sources"] @ q)
    lc = prior.joint.third.lc_cubic(prepared, changed)
    response = lift.higher_response(prepared, changed, coordinates, highest, lc,
        masked, prior.highest_matrix(prepared, services=services), services=services, workers=2)
    full_matrix = np.column_stack((response["jacobian"][:384], response["matrix"][:384, :960]))
    full_source, affinity = source.normal.higher_source_response(prepared, point, jets, reduction)
    base = source.regular.equations(prepared, point, jets)["vector"]
    return prepared, point, jets, reduction, coordinates, report, q, full_matrix, full_source, base, affinity


def evaluate():
    prepared, point, jets, reduction, coordinates, fitted, q, full, response, base, affinity = load_system()
    extract = extraction_matrix()
    matrix, b, sources = extract @ full, extract @ base, extract @ response
    blocks = source.allowed_cauchy_coordinates()
    allowed = np.array(blocks["psi2"]+blocks["lambda2"]+blocks["e3"])
    fixed = np.setdiff1d(np.arange(1200), allowed)
    model = eliminate(matrix[:, allowed], sources)
    z = np.asarray(fitted["fitted_coordinates"])-coordinates
    target = b+matrix[:, fixed] @ z[fixed]
    rhs = -model["left_null"].T @ target
    recovered = np.linalg.lstsq(model["gate"], rhs, rcond=1e-10)[0]
    errors = []
    rng = np.random.default_rng(20261019)
    for scale in (0., .003):
        trial_q = q+rng.normal(size=6)*scale
        trial_z = z+rng.normal(size=1200)*scale
        p, j = source.changed_fields(point, jets, reduction["sources"], trial_q, trial_z)
        actual = extract @ source.regular.equations(prepared, p, j)["vector"]
        errors.append(float(np.linalg.norm(actual-(b+sources @ trial_q+matrix @ trial_z))))
    time_model = eliminate(matrix[:68, allowed], sources[:68])
    return {"input_sha256": input_fingerprints(), "scope": "first primary prolongation; finite jet only",
        "equations": 272, "normal_higher_coordinates": len(allowed),
        "higher_rank": model["rank"], "left_nullity": model["left_null"].shape[1],
        "source_gate_rank": model["gate_rank"], "source_gate_singular_values": model["gate_singular"].tolist(),
        "time_only_gate_rank": time_model["gate_rank"],
        "psi3_response_norm": float(np.linalg.norm(matrix[:, 720:])),
        "candidate_residual_norm": float(np.linalg.norm(b+sources @ q+matrix @ z)),
        "recovered_source": recovered.tolist(), "source_recovery_error": float(np.linalg.norm(recovered-q)),
        "projected_compatibility_norm": float(np.linalg.norm(model["gate"] @ recovered-rhs)),
        "direct_affinity_errors": errors, "prior_source_affinity_error_norm": float(np.linalg.norm(affinity))}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "input_sha256"}, indent=2))
