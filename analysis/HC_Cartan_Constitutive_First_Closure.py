"""First probe/gravity prolongation versus mixed constitutive transport.

Affine finite-jet kernel test at fixed spinor first jet, not regional closure.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "first_closure_transport", Path(__file__).with_name("HC_Cartan_Constitutive_Transport.py"))
transport = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(transport)
neighborhood = transport.neighborhood
regular, spatial, prior, prolong = neighborhood.regular, transport.spatial, transport.prior, transport.prolong


def matrix_rank(matrix):
    singular = np.linalg.svd(matrix, compute_uv=False)
    cutoff = max(1e-9, singular[0]*1e-10) if singular.size else 1e-9
    return int(np.sum(singular > cutoff)), singular, cutoff


def normal_basis(prepared, point):
    """Hold psi1 and lambda_,0^0 exactly fixed, rather than relying on roundoff."""
    system = spatial.normal_curl_system(prepared, point)
    indices = list(range(16))+[40+4*a+i for a in range(4) for i in range(1, 4)]
    reduced = system["matrix"][:56, indices]
    _, singular, vh = np.linalg.svd(reduced, full_matrices=True)
    rank, _, cutoff = matrix_rank(reduced)
    basis = np.zeros((56, len(indices)-rank))
    basis[indices] = vh[rank:].T
    return basis, reduced, singular, cutoff


def shifted(point, jets, basis, vector):
    n = basis.shape[1]
    x = np.asarray(vector, float)
    if x.shape != (n+720,) or not np.all(np.isfinite(x)):
        raise ValueError("Finite normal-kernel and 720 higher-jet coordinates required")
    changed = transport.normal_point(point, basis @ x[:n], 1.)
    higher = dict(jets)
    delta = regular.unpack(np.r_[x[n:], np.zeros(480)])
    for key in ("p2", "l2", "e3"):
        higher[key] = jets[key]+delta[key]
    return changed, higher


def residual(prepared, point, jets):
    result = regular.equations(prepared, point, jets)
    c = result["constraint_first"]
    return np.r_[c[1:].reshape(-1), c[0, :, 0],
                 prior.realify(result["probe_first"]), result["coframe_Euler_first"].reshape(-1)]


def assemble(prepared, point, jets, basis):
    size = basis.shape[1]+720
    zero = np.zeros(size)
    base = residual(prepared, point, jets)
    matrix = np.column_stack([
        residual(prepared, *shifted(point, jets, basis, v))-base for v in np.eye(size)])
    curl = np.zeros((12, size))
    system = spatial.normal_curl_system(prepared, point)
    curl[:, :basis.shape[1]] = system["matrix"][56:] @ basis
    rank, singular, cutoff = matrix_rank(matrix)
    _, _, vh = np.linalg.svd(matrix, full_matrices=True)
    kernel = vh[rank:].T
    response = curl @ kernel
    response_rank, response_singular, response_cutoff = matrix_rank(response)
    _, _, response_vh = np.linalg.svd(response, full_matrices=False)
    direction = kernel @ response_vh[0]
    pivot = np.argmax(np.abs(direction))
    if direction[pivot] < 0:
        direction = -direction
    return {"base": base, "matrix": matrix, "curl": curl, "kernel": kernel,
            "rank": rank, "singular": singular, "cutoff": cutoff,
            "response": response, "response_rank": response_rank,
            "response_singular": response_singular, "response_cutoff": response_cutoff,
            "direction": direction}


def ward_gate(multiplier):
    """At F0 derivatives and spatial F derivatives zero, lambda^0_a J^a_0i=0."""
    result = np.zeros((3, 12))
    for i in range(3):
        result[i, 4*i:4*(i+1)] = multiplier[:, 0]
    return result


def input_fingerprints():
    result = transport.input_fingerprints()
    name = Path(__file__).name
    result[name] = hashlib.sha256(Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


def field_difference_checks(prepared, point, jets):
    """Actual polynomial fields, separate from the affine jet residual matrix."""
    analytic = regular.equations(prepared, point, jets)
    results = []
    for step in (2e-5, 1e-5):
        probe = np.array([
            (regular.taylor_fields(prepared, point, jets, step*v)["probe"]
             -regular.taylor_fields(prepared, point, jets, -step*v)["probe"])/(2*step)
            for v in np.eye(4)])
        gravity = np.array([
            (regular.field_euler(prepared, point, jets, step*v)
             -regular.field_euler(prepared, point, jets, -step*v))/(2*step)
            for v in np.eye(4)])
        results.append({"step": step,
                        "probe_first_fd_error": float(np.linalg.norm(probe-analytic["probe_first"])),
                        "coframe_Euler_first_fd_error": float(np.linalg.norm(gravity-analytic["coframe_Euler_first"]))})
    return results


def evaluate():
    fingerprints = input_fingerprints()
    prepared, point, jets, _, _ = neighborhood.load_data()
    basis, reduced, normal_singular, normal_cutoff = normal_basis(prepared, point)
    system = assemble(prepared, point, jets, basis)
    gate = ward_gate(point["multiplier"])
    normal_curl = system["curl"][:, :basis.shape[1]]
    gate_rank, gate_singular, _ = matrix_rank(gate @ normal_curl)
    rows = []
    field_checks = None
    for amplitude in (0., .01, -.01, .02):
        vector = amplitude*system["direction"]
        changed, higher = shifted(point, jets, basis, vector)
        equations = regular.equations(prepared, changed, higher)
        c = equations["constraint_first"]
        mixed = np.array([c[0, :, i]-c[i, :, 0] for i in range(1, 4)])
        lower = neighborhood.rank_model.point_equations(
            prepared, changed["psi_first"], changed["coframe_second"],
            changed["multiplier"], changed["multiplier_first"])
        actual = residual(prepared, changed, higher)
        rows.append({"amplitude": amplitude,
                     "point_equations_norm": float(np.linalg.norm(lower["vector"])),
                     "spatial_constraint_gradient_norm": float(np.linalg.norm(c[1:])),
                     "temporal_column_gradient_norm": float(np.linalg.norm(c[:, :, 0])),
                     "probe_first_norm": float(np.linalg.norm(equations["probe_first"])),
                     "coframe_Euler_first_norm": float(np.linalg.norm(equations["coframe_Euler_first"])),
                     "mixed_defect": mixed.tolist(), "mixed_defect_norm": float(np.linalg.norm(mixed)),
                     "coordinate_Ward_gate_norm": float(np.linalg.norm(gate @ mixed.reshape(-1))),
                     "affine_prediction_error": float(np.linalg.norm(actual-system["base"]-system["matrix"] @ vector)),
                     "unimposed_constraint_second_norm": float(np.linalg.norm(equations["constraint_second"]))})
        if amplitude == .01:
            field_checks = field_difference_checks(prepared, changed, higher)
    if fingerprints != input_fingerprints():
        raise RuntimeError("First closure inputs changed")
    return {"scope": "First differentiated probe/gravity and spatial constitutive jets at one point",
            "input_sha256": fingerprints, "normal_restricted_rank": matrix_rank(reduced)[0],
            "normal_restricted_singular_values": normal_singular.tolist(), "normal_cutoff": normal_cutoff,
            "normal_kernel_dimension": basis.shape[1], "affine_shape": list(system["matrix"].shape),
            "affine_rank": system["rank"], "affine_cutoff": system["cutoff"],
            "affine_singular_values": system["singular"].tolist(),
            "mixed_defect_rank_before_first_prolongation": matrix_rank(normal_curl)[0],
            "coordinate_Ward_gate_rank_on_normal_curls": gate_rank,
            "coordinate_Ward_gate_singular_values": gate_singular.tolist(),
            "mixed_defect_rank_after_first_prolongation": system["response_rank"],
            "mixed_defect_singular_values": system["response_singular"].tolist(),
            "mixed_defect_rank_cutoff": system["response_cutoff"],
            "normal_kernel_basis": basis.tolist(), "direction": system["direction"].tolist(),
            "witnesses": rows, "actual_field_first_derivative_checks": field_checks,
            "spinor_value_and_first_jet_and_action_couplings_fixed": True,
            "not_all_constitutive_derivatives_imposed": True,
            "not_a_regional_solution_or_full_propagation_disproof": True,
            "main_TeX_PDF_changed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = evaluate()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items()
                      if key in ("affine_shape", "affine_rank", "normal_kernel_dimension",
                                 "coordinate_Ward_gate_rank_on_normal_curls",
                                 "mixed_defect_rank_after_first_prolongation", "witnesses")}))


if __name__ == "__main__":
    main()
