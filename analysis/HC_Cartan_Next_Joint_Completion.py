"""Joint finite-jet R2/FE2/C3 completion with fixed psi2 and fixed couplings.

Not a PDE solution, native gravitational identification, or a scale prediction.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


def local_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


third = local_module("next_joint_third", "HC_Cartan_Third_Constraint_Reprepare.py")
probe = local_module("next_joint_probe", "HC_Cartan_Second_Probe_Affine.py")
gravity = local_module("next_joint_gravity", "HC_Cartan_Second_Gravity_Affine.py")
scalar, regular, prior, prolong, cartan = third.scalar, third.regular, third.prior, third.prolong, third.cartan


def input_fingerprints():
    names = ("HC_Cartan_Third_Constraint_Reprepare.py", "HC_Cartan_Second_Probe_Affine.py",
             "HC_Cartan_Second_Gravity_Affine.py", "HC_Cartan_Third_Constraint_Diagnostic.py",
             "HC_Cartan_Next_Scalar_Compatibility.py", "HC_Cartan_Next_Scalar_Compatibility.json")
    result = scalar.input_fingerprints()
    for name in names:
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def packed_probe(value):
    return prior.realify(np.array([value[p] for p in prior.PAIR2]))


def packed_gravity(value):
    return np.array([value[p] for p in prior.PAIR2]).reshape(-1)


def lower_fields(prepared, point, jets, lc_third):
    connection = third.connection_third(prepared, point, jets, lc_third)
    return {"old": third.old_equations(prepared, point, jets),
            "probe": probe.probe_second(prepared, point, jets),
            "gravity": gravity.coframe_euler_second(prepared, point, jets, omega3=connection["third"]),
            "constraint": third.constraint_third(prepared, point, jets, lc_third)}


def joint_vector(fields, complement):
    return np.concatenate((fields["old"], packed_probe(fields["probe"]),
                           packed_gravity(fields["gravity"]), complement.T @ fields["constraint"].reshape(-1)))


def highest_maps(prepared):
    c3maps = third.new_jet_maps(prepared)
    u, _, _ = np.linalg.svd(c3maps["symmetric"], full_matrices=True)
    complement = u[:, 140:]
    eta = cartan.ETA
    p = prepared["data"]["psi"].reshape(12)
    columns = []
    for i in range(880):
        basis = np.zeros(880)
        basis[i] = 1
        e4, l3 = basis[:560].reshape(35, 4, 4), basis[560:].reshape(20, 4, 4)
        omega3 = gravity.highest_delta_omega3(prepared, e4, l3)
        curvature = np.einsum("ac,rsmncd,db->rsmnab", eta, omega3-omega3.swapaxes(2, 3), eta)
        fe2 = np.array([prolong.gravity_euler(curvature[pair]) for pair in prior.PAIR2]).reshape(-1)
        full_l3 = prolong.unpack_third(basis[560:])
        r2 = .5j*np.einsum("rsmam,aij,j->rsi", full_l3, prolong.Q_WEIGHTS, p)
        columns.append(np.concatenate((np.zeros(394), packed_probe(r2), fe2,
                                       complement.T @ c3maps["connection"][:, i])))
    return dict(c3maps, complement=complement, joint=np.column_stack(columns))


def fit(prepared, point, saved, lc_third, maps):
    fixed = third.coordinates(saved)
    def image(delta):
        jets = regular.unpack(fixed+np.concatenate((np.zeros(240), delta)))
        return joint_vector(lower_fields(prepared, point, jets, lc_third), maps["complement"])
    base = image(np.zeros(960))
    columns = []
    scale = 64.
    for i in range(960):
        delta = np.zeros(960)
        delta[i] = scale
        columns.append((image(delta)-base)/scale)
    older = np.column_stack(columns)
    matrix = np.column_stack((older, maps["joint"]))
    u, singular, vt = np.linalg.svd(matrix, full_matrices=False)
    rank = int(np.sum(singular > singular[0]*1e-10))
    def inverse(rhs):
        return vt[:rank].T @ ((u[:, :rank].T @ rhs)/singular[:rank])
    solution = inverse(-base)
    history = []
    for _ in range(4):
        residual = image(solution[:960])+maps["joint"] @ solution[960:]
        history.append(float(np.linalg.norm(residual)))
        if history[-1] < 1e-8:
            break
        correction = inverse(-residual)
        if np.linalg.norm(correction) < 1e-10:
            break
        solution += correction
    rng = np.random.default_rng(11142026)
    random = rng.normal(size=960)*.3
    affine_error = float(np.linalg.norm(image(random)-base-older @ random))
    return {"solution": solution, "matrix": matrix, "base": base, "rank": rank,
            "singular_values": singular, "history": history, "affine_error": affine_error,
            "coordinates": fixed+np.concatenate((np.zeros(240), solution[:960]))}


def full_residual(prepared, point, coordinates, connection_coordinates, p4, lc_third):
    jets = regular.unpack(coordinates)
    e4 = connection_coordinates[:560].reshape(35, 4, 4)
    l3 = connection_coordinates[560:].reshape(20, 4, 4)
    c3 = (third.constraint_third(prepared, point, jets, lc_third)
          +third.diagnostic.connection_image(prepared, e4, l3)
          +third.diagnostic.principal_image(third.spatial.constraint_principal_map(prepared["data"]["psi"]), p4))
    r2 = probe.probe_second(prepared, point, jets, connection_coordinates[560:])
    fe2 = gravity.coframe_euler_second(prepared, point, jets, e4=e4, l3=l3, lc_third=lc_third)
    old = third.old_equations(prepared, point, jets)
    vector = np.concatenate((old, packed_probe(r2), packed_gravity(fe2), c3.reshape(-1)))
    return {"vector": vector, "old": old, "probe": r2, "gravity": fe2, "constraint": c3}


def evaluate():
    fingerprints = input_fingerprints()
    prepared, point, saved, fingerprint = third.diagnostic.load_data()
    lc_third = third.lc_cubic(prepared, point)
    maps = highest_maps(prepared)
    solved = fit(prepared, point, saved, lc_third, maps)
    updated = regular.unpack(solved["coordinates"])
    conn = solved["solution"][960:]
    c3source = (third.constraint_third(prepared, point, updated, lc_third)
                +(maps["connection"] @ conn).reshape(20, 4, 4))
    principal = third.spatial.constraint_principal_map(prepared["data"]["psi"])
    p4, _ = third.diagnostic.spinor_only_completion(c3source, principal)
    residual = full_residual(prepared, point, solved["coordinates"], conn, p4, lc_third)
    if fingerprints != input_fingerprints():
        raise RuntimeError("Source inputs changed while computing joint completion")
    return {"scope": "Pointwise added neutral Cartan finite jet; no PDE propagation or native physics",
            "input_sha256": fingerprints, "input_scalar_completion_sha256": fingerprint,
            "fixed": "Lower point, psi2, Q, M, Einstein coefficient 1, vacuum 0",
            "variable_layout": "960 earlier lambda2/E3/psi3 deltas; 560 E4 then 320 lambda3; psi4 recovered separately",
            "matrix_shape": list(solved["matrix"].shape), "matrix_rank": solved["rank"],
            "matrix_singular_values": solved["singular_values"].tolist(),
            "random_affine_error_norm": solved["affine_error"], "refinement_residual_history": solved["history"],
            "older_coordinate_change_norm": float(np.linalg.norm(solved["solution"][:960])),
            "highest_coordinate_norm": float(np.linalg.norm(solved["solution"][960:])),
            "jet_coordinates": solved["coordinates"].tolist(), "connection_coordinates": conn.tolist(),
            "fourth_spinor_real": p4.tolist(),
            "all_1114_residual_norm": float(np.linalg.norm(residual["vector"])),
            "all_1114_max_abs": float(np.max(abs(residual["vector"]))),
            "all_1114_residual": residual["vector"].tolist(),
            "old_394_norm": float(np.linalg.norm(residual["old"])),
            "R2_full_symmetric_norm": float(np.linalg.norm(residual["probe"])),
            "FE2_full_symmetric_norm": float(np.linalg.norm(residual["gravity"])),
            "C3_unique_triples_norm": float(np.linalg.norm(residual["constraint"])),
            "limitations": ["No next derivative hierarchy, surface data, formal integrability or existence proof",
                            "Higher Taylor coefficients changed; old neighborhood bound must not be inherited",
                            "No native action/HC/C7, physical frames, coupling or scale identification"],
            "main_TeX_PDF_changed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = evaluate()
    encoded = json.dumps(report, indent=2, allow_nan=False)+"\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded)
    print(json.dumps({k: report[k] for k in ("matrix_rank", "all_1114_residual_norm", "old_394_norm",
                                            "R2_full_symmetric_norm", "FE2_full_symmetric_norm", "C3_unique_triples_norm")}))


if __name__ == "__main__":
    main()
