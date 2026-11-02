"""Second constitutive compatibility with free symmetric higher spinor jets.

The mixed first constitutive curls are tested, never imposed as equations.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "second_closure_first", Path(__file__).with_name("HC_Cartan_Constitutive_First_Closure.py"))
first = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(first)
regular, spatial, prior, prolong = first.regular, first.spatial, first.prior, first.prolong
neighborhood = first.neighborhood


def shifted(point, jets, basis, vector):
    n = basis.shape[1]
    x = np.asarray(vector, float)
    if x.shape != (n+1200,) or not np.all(np.isfinite(x)):
        raise ValueError("Finite normal-kernel and 1200 higher-jet coordinates required")
    changed = first.transport.normal_point(point, basis @ x[:n], 1.)
    delta = regular.unpack(x[n:])
    higher = {key: jets[key]+delta[key] for key in jets}
    return changed, higher


def residual(prepared, point, jets):
    result = regular.equations(prepared, point, jets)
    c = result["constraint_first"]
    c2 = result["constraint_second"]
    return np.r_[c[1:].reshape(-1), c[0, :, 0], prior.realify(result["probe_first"]),
                 result["coframe_Euler_first"].reshape(-1),
                 np.array([c2[p] for p in prior.PAIR2]).reshape(-1)]


def assemble(prepared, point, jets, basis):
    size = basis.shape[1]+1200
    base = residual(prepared, point, jets)
    matrix = np.column_stack([
        residual(prepared, *shifted(point, jets, basis, v))-base for v in np.eye(size)])
    curl = np.zeros((12, size))
    normal = spatial.normal_curl_system(prepared, point)
    curl[:, :basis.shape[1]] = normal["matrix"][56:] @ basis
    rank, singular, cutoff = first.matrix_rank(matrix)
    _, _, vh = np.linalg.svd(matrix, full_matrices=True)
    kernel = vh[rank:].T
    response = curl @ kernel
    response_rank, response_singular, response_cutoff = first.matrix_rank(response)
    _, _, response_vh = np.linalg.svd(response, full_matrices=False)
    direction = kernel @ response_vh[0]
    if direction[np.argmax(abs(direction))] < 0:
        direction = -direction
    return {"base": base, "matrix": matrix, "curl": curl, "kernel": kernel,
            "rank": rank, "singular": singular, "cutoff": cutoff,
            "response": response, "response_rank": response_rank,
            "response_singular": response_singular, "response_cutoff": response_cutoff,
            "direction": direction}


def second_field_checks(prepared, point, jets):
    """Central second differences of actual C-E, with derivative multiplicities."""
    analytic = regular.equations(prepared, point, jets)["constraint_second"]
    origin = regular.taylor_fields(prepared, point, jets, np.zeros(4))["constraint"]
    results = []
    measured_values = []
    for step in (1e-4, 5e-5, 2.5e-5):
        measured = np.zeros((4, 4, 4, 4))
        for r, s in prior.PAIR2:
            u, v = np.eye(4)[[r, s]]
            if r == s:
                plus = regular.taylor_fields(prepared, point, jets, step*u)["constraint"]
                minus = regular.taylor_fields(prepared, point, jets, -step*u)["constraint"]
                measured[r, r] = (plus-2*origin+minus)/step**2
            else:
                fields = [regular.taylor_fields(prepared, point, jets, step*(a*u+b*v))["constraint"]
                          for a, b in ((1, 1), (1, -1), (-1, 1), (-1, -1))]
                measured[r, s] = measured[s, r] = (fields[0]-fields[1]-fields[2]+fields[3])/(4*step**2)
        results.append({"step": step, "full_symmetric_second_constitutive_fd_error":
                        float(np.linalg.norm(measured-analytic))})
        measured_values.append(measured)
    richardson = (4*measured_values[-1]-measured_values[-2])/3
    return {"steps": results, "richardson_error": float(np.linalg.norm(richardson-analytic))}


def multiplier_gate(point):
    """Rows: lambda^0, partial_1 lambda^0, partial_2 lambda^0, partial_3 lambda^0."""
    return np.vstack((point["multiplier"][:, 0], point["multiplier_first"][1:, :, 0]))


def differentiated_ward_terms(prepared, point, jets, fe2=None):
    """Full first coordinate-Ward derivative at E=I, dE=0; no sources dropped."""
    lower = neighborhood.rank_model.point_equations(
        prepared, point["psi_first"], point["coframe_second"],
        point["multiplier"], point["multiplier_first"])
    current = regular.equations(prepared, point, jets)
    if fe2 is None:
        fe2 = neighborhood.joint.gravity.coframe_euler_second(prepared, point, jets)
    e2, lam, dl = point["coframe_second"], point["multiplier"], point["multiplier_first"]
    f, df, ddf = lower["constraint"], current["constraint_first"], current["constraint_second"]
    div_lam = np.einsum("mam->a", dl)
    result = {key: np.zeros((4, 4)) for key in (
        "Euler_second_divergence", "Euler_coframe_second_curl", "multiplier_first_constraint_curl",
        "multiplier_constraint_second_curl", "constraint_first_multiplier_divergence",
        "constraint_multiplier_second_divergence", "probe_source")}
    for r, nu in np.ndindex(4, 4):
        result["Euler_second_divergence"][r, nu] = sum(fe2[r, mu, nu, mu] for mu in range(4))
        result["Euler_coframe_second_curl"][r, nu] = sum(
            lower["coframe"][a, mu]*(e2[r, mu, a, nu]-e2[r, nu, a, mu])
            for a, mu in np.ndindex(4, 4))
        result["multiplier_first_constraint_curl"][r, nu] = sum(
            dl[r, a, mu]*(df[mu, a, nu]-df[nu, a, mu]) for a, mu in np.ndindex(4, 4))
        result["multiplier_constraint_second_curl"][r, nu] = sum(
            lam[a, mu]*(ddf[r, mu, a, nu]-ddf[r, nu, a, mu]) for a, mu in np.ndindex(4, 4))
        result["constraint_first_multiplier_divergence"][r, nu] = df[r, :, nu] @ div_lam
        result["constraint_multiplier_second_divergence"][r, nu] = sum(
            f[a, nu]*jets["l2"][r, mu, a, mu] for a, mu in np.ndindex(4, 4))
        result["probe_source"][r, nu] = -2*(
            np.vdot(jets["p2"][r, nu], lower["probe"]).real
            +np.vdot(point["psi_first"][nu], current["probe_first"][r]).real)
    return result


def input_fingerprints():
    result = first.input_fingerprints()
    result[Path(__file__).name] = hashlib.sha256(
        Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


def evaluate():
    fingerprints = input_fingerprints()
    prepared, point, jets, _, _ = neighborhood.load_data()
    basis, _, _, _ = first.normal_basis(prepared, point)
    system = assemble(prepared, point, jets, basis)
    gate = first.ward_gate(point["multiplier"])
    rows, field_checks = [], None
    ward_checks = []
    for amplitude in (0., .01, -.01, .02):
        vector = amplitude*system["direction"]
        changed, higher = shifted(point, jets, basis, vector)
        result = regular.equations(prepared, changed, higher)
        c = result["constraint_first"]
        mixed = np.array([c[0, :, i]-c[i, :, 0] for i in range(1, 4)])
        lower = neighborhood.rank_model.point_equations(
            prepared, changed["psi_first"], changed["coframe_second"],
            changed["multiplier"], changed["multiplier_first"])
        rows.append({"amplitude": amplitude,
                     "point_equations_norm": float(np.linalg.norm(lower["vector"])),
                     "spatial_constraint_gradient_norm": float(np.linalg.norm(c[1:])),
                     "temporal_column_gradient_norm": float(np.linalg.norm(c[:, :, 0])),
                     "probe_first_norm": float(np.linalg.norm(result["probe_first"])),
                     "coframe_Euler_first_norm": float(np.linalg.norm(result["coframe_Euler_first"])),
                     "second_constitutive_full_symmetric_norm": float(np.linalg.norm(result["constraint_second"])),
                     "mixed_defect": mixed.tolist(), "mixed_defect_norm": float(np.linalg.norm(mixed)),
                     "coordinate_Ward_gate_norm": float(np.linalg.norm(gate @ mixed.reshape(-1))),
                     "affine_prediction_error": float(np.linalg.norm(
                         residual(prepared, changed, higher)-system["base"]-system["matrix"] @ vector))})
        if amplitude == .01:
            field_checks = second_field_checks(prepared, changed, higher)
        if amplitude in (0., .01):
            terms = differentiated_ward_terms(prepared, changed, higher)
            expected = changed["multiplier_first"][1:, :, 0] @ mixed.T
            ward_checks.append({"amplitude": amplitude,
                                "full_differentiated_Ward_error": float(np.linalg.norm(sum(terms.values()))),
                                "spatial_Euler_second_divergence": terms["Euler_second_divergence"][1:, 1:].tolist(),
                                "spatial_multiplier_gradient_gate": expected.tolist(),
                                "spatial_multiplier_gradient_gate_norm": float(np.linalg.norm(expected)),
                                "reduced_spatial_identity_error": float(np.linalg.norm(
                                    terms["Euler_second_divergence"][1:, 1:]+expected))})
    if fingerprints != input_fingerprints():
        raise RuntimeError("Second constitutive closure inputs changed")
    return {"scope": "Fixed-point normal-kernel compatibility with full second constitutive derivative",
            "input_sha256": fingerprints, "normal_kernel_dimension": basis.shape[1],
            "affine_shape": list(system["matrix"].shape), "affine_rank": system["rank"],
            "affine_singular_values": system["singular"].tolist(), "affine_cutoff": system["cutoff"],
            "mixed_defect_rank_after_second_constitutive_stage": system["response_rank"],
            "mixed_defect_singular_values": system["response_singular"].tolist(),
            "mixed_defect_rank_cutoff": system["response_cutoff"],
            "normal_kernel_basis": basis.tolist(), "direction": system["direction"].tolist(),
            "witnesses": rows, "actual_field_second_derivative_checks": field_checks,
            "second_coordinate_Ward_checks": ward_checks,
            "complete_multiplier_gate": multiplier_gate(point).tolist(),
            "complete_multiplier_gate_singular_values": np.linalg.svd(multiplier_gate(point), compute_uv=False).tolist(),
            "spatial_multiplier_gate_rank_on_remaining_defects": first.matrix_rank(
                np.kron(np.eye(3), point["multiplier_first"][1:, :, 0]) @ system["response"])[0],
            "spinor_value_and_first_jet_and_action_couplings_fixed": True,
            "mixed_first_curls_not_imposed": True,
            "second_probe_and_second_gravity_not_imposed": True,
            "not_a_regional_solution_or_full_propagation_disproof": True,
            "main_TeX_PDF_changed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = evaluate()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in (
        "affine_shape", "affine_rank", "mixed_defect_rank_after_second_constitutive_stage", "witnesses")}))


if __name__ == "__main__":
    main()
