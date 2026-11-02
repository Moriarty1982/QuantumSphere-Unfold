"""Constitutive curl transport and a point-jet non-implication control.

The normal equations at one point are not an open-set evolution theorem.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "constitutive_joint_neighborhood", Path(__file__).with_name("HC_Cartan_Joint_Neighborhood.py"))
neighborhood = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(neighborhood)
spatial = neighborhood.third.spatial
prior, prolong, cartan = neighborhood.prior, neighborhood.prolong, neighborhood.cartan


def gradient(psi, first, second, spin, spin_first, coframe_first):
    """Direct product derivative of F; indices (derivative, frame, one-form)."""
    p, f = psi.reshape(12), first.reshape(4, 12)
    p2 = second.reshape(4, 4, 12)
    cov = f+np.einsum("mij,j->mi", spin, p)
    dcov = (p2+np.einsum("rmij,j->rmi", spin_first, p)
            +np.einsum("mij,rj->rmi", spin, f))
    return (np.einsum("ri,aij,mj->ram", f.conj(), prolong.Q_WEIGHTS, cov)
            +np.einsum("i,aij,rmj->ram", p.conj(), prolong.Q_WEIGHTS, dcov)).imag-coframe_first


def curl(psi, first, spin, spin_first, coframe_first):
    """Exterior derivative of F with no spinor Hessian in the expression."""
    p, f = psi.reshape(12), first.reshape(4, 12)
    result = []
    for r, s in cartan.PAIRS:
        result.append(np.array([
            (np.vdot(f[r], a @ (f[s]+spin[s] @ p))
             -np.vdot(f[s], a @ (f[r]+spin[r] @ p))
             +np.vdot(p, a @ ((spin_first[r, s]-spin_first[s, r]) @ p
                              +spin[s] @ f[r]-spin[r] @ f[s]))).imag
            for a in prolong.Q_WEIGHTS])-coframe_first[r, :, s]+coframe_first[s, :, r])
    return np.array(result)


def normal_point(point, direction, amplitude):
    x = cartan.checks._real(direction, (56,), "normal direction")
    amplitude = cartan.checks._scalar(amplitude, "normal amplitude")
    result = dict(point)
    for key in ("coframe_second", "psi_first", "multiplier_first"):
        result[key] = point[key].copy()
    result["coframe_second"][0, 0] += amplitude*x[:16].reshape(4, 4)
    result["psi_first"][0] += amplitude*prior.complexify(x[16:40], (3, 4))
    result["multiplier_first"][0] += amplitude*x[40:].reshape(4, 4)
    return result


def independent_spin_jets(prepared, point):
    omega, omega_first = spatial.connection_first(prepared, point)
    spin = np.array([np.kron(np.eye(3), b) for b in prolong.spin_lift(omega)])
    spin_first = np.array([[np.kron(np.eye(3), b) for b in row]
                           for row in prolong.spin_lift(omega_first)])
    return spin, spin_first


def adapted_hessian(prepared, point, reference):
    """Cancel spatial F derivatives, not the antisymmetric mixed curl defect."""
    first = spatial.constraint_first(prepared, point, reference)
    principal = spatial.constraint_principal_map(prepared["data"]["psi"])
    inverse = np.linalg.pinv(principal, rcond=1e-10)
    result = reference.copy()
    for r, s in prior.PAIR2:
        # For 0i, cancel d_i F_0; symmetry then leaves d_0 F_i = curl_0i.
        target = first[s, :, r] if r == 0 and s > 0 else (first[r, :, s]+first[s, :, r])/2
        correction = prior.complexify(inverse @ (-target), (3, 4))
        result[r, s] += correction
        if r != s:
            result[s, r] += correction
    return result


def witness_data():
    prepared, point, jets, _, _ = neighborhood.load_data()
    system = spatial.normal_curl_system(prepared, point)
    kernel = system["original_kernel"]
    _, singular, vh = np.linalg.svd(system["induced_curl"], full_matrices=False)
    direction = kernel @ vh[0]
    # SVD sign is arbitrary; make the retained witness reproducible.
    pivot = np.argmax(np.abs(direction))
    if direction[pivot] < 0:
        direction = -direction
    rows = []
    for amplitude in (0., .01, -.01, .02):
        changed = normal_point(point, direction, amplitude)
        second = adapted_hessian(prepared, changed, jets["p2"])
        df = spatial.constraint_first(prepared, changed, second)
        equations = neighborhood.rank_model.point_equations(
            prepared, changed["psi_first"], changed["coframe_second"],
            changed["multiplier"], changed["multiplier_first"])
        spin, spin_first = independent_spin_jets(prepared, changed)
        direct = gradient(prepared["data"]["psi"], changed["psi_first"], second,
                          spin, spin_first, np.zeros((4, 4, 4)))
        defect = curl(prepared["data"]["psi"], changed["psi_first"], spin,
                      spin_first, np.zeros((4, 4, 4)))
        differentiated_probe = spatial.first_probe(prepared, changed, second, jets["l2"])
        rows.append({"amplitude": amplitude,
                     "point_equations_norm": float(np.linalg.norm(equations["vector"])),
                     "spatial_constraint_gradient_norm": float(np.linalg.norm(df[1:])),
                     "temporal_column_gradient_norm": float(np.linalg.norm(df[:, :, 0])),
                     "spatial_constraint_time_gradient": df[0, :, 1:].tolist(),
                     "spatial_constraint_time_gradient_norm": float(np.linalg.norm(df[0, :, 1:])),
                     "mixed_curl_norm": float(np.linalg.norm(defect[:3])),
                     "frozen_higher_first_probe_norm": float(np.linalg.norm(differentiated_probe)),
                     "independent_gradient_error": float(np.linalg.norm(direct-df)),
                     "transport_identity_error": float(np.linalg.norm(df[0, :, 1:]-df[1:, :, 0].T-defect[:3].T))})
    return prepared, point, jets, system, direction, singular, rows


def input_fingerprints():
    result = neighborhood.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Spatial_Propagation.py", "HC_Cartan_Cauchy_Rank.py"):
        data = Path(__file__).with_name(name).read_bytes().replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def evaluate():
    fingerprints = input_fingerprints()
    _, _, _, system, direction, singular, rows = witness_data()
    if fingerprints != input_fingerprints():
        raise RuntimeError("Constitutive transport inputs changed")
    return {"scope": "Neutral odd-cross Cartan comparison: exact coordinate curl and point-jet control",
            "input_sha256": fingerprints, "normal_equations_rank": system["original_rank"],
            "normal_plus_mixed_curl_rank": system["rank"],
            "mixed_curl_rank_on_normal_kernel": system["induced_rank"],
            "induced_singular_values": singular.tolist(), "normal_direction": direction.tolist(),
            "normal_kernel_error": float(np.linalg.norm(system["matrix"][:56] @ direction)),
            "witnesses": rows,
            "couplings_and_state_value_fixed": True,
            "not_a_solution_of_prolonged_or_open_set_equations": True,
            "not_a_disproof_of_full_parent_propagation": True,
            "native_identification_or_full_existence_proved": False,
            "main_TeX_PDF_changed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = evaluate()
    if args.output:
        args.output.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({"ranks": [report[key] for key in (
        "normal_equations_rank", "normal_plus_mixed_curl_rank", "mixed_curl_rank_on_normal_kernel")],
        "witnesses": report["witnesses"]}))


if __name__ == "__main__":
    main()
