"""Next scalar gate of the explicitly added neutral odd-cross Cartan comparison.

Full affine finite-jet compatibility only, not a Cauchy solution or native physics.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "next_scalar_regular_gravity", Path(__file__).with_name("HC_Cartan_Regular_Gravity.py"))
regular = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(regular)
spatial, prolong, prior, cartan, odd = (
    regular.spatial, regular.prolong, regular.prior, regular.cartan, regular.odd)
Q, MASS, BETA, PAIR2 = regular.Q, regular.MASS, regular.BETA, prior.PAIR2
H_MASS = (Q @ MASS+MASS @ Q)/2
Q_FULL = np.kron(Q, np.eye(4))
Q2_WEIGHTS = np.array([np.kron(Q @ Q, k) for k in prolong.WEIGHTS])
INPUTS = ("HC_Cartan_Regular_Gravity.py", "HC_Cartan_Regular_Gravity.json",
          "HC_Cartan_Regular_Gravity.md", "HC_Cartan_Spatial_Propagation.py",
          "HC_Cartan_Spatial_Propagation.json", "HC_Cartan_Spatial_Propagation.md")


def input_fingerprints():
    result = {}
    for name in INPUTS:
        data = Path(__file__).with_name(name).read_bytes()
        if Path(name).suffix in (".py", ".md"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def load_data():
    prepared, point, _ = regular.load_data()
    payload = json.loads(Path(__file__).with_name("HC_Cartan_Regular_Gravity.json").read_text(encoding="utf-8"))
    coordinates = np.array(payload["joint_completion"]["jet_coordinates"], float)
    return prepared, point, coordinates


def off_shell_identity(coframe, coframe_first, psi, psi_first, omega, multiplier, multiplier_first):
    """No field equation, normal-point assumption or Cartan elimination is used here."""
    e, inverse, volume = cartan.frame_data(coframe)
    inverse_first = -np.einsum("ma,rav,vb->rmb", inverse, coframe_first, inverse)
    volume_first = volume*np.einsum("ma,ram->r", inverse, coframe_first)
    weights_first = (np.einsum("r,ma,aij->rmij", volume_first, inverse, prolong.FLAT_WEIGHTS)
                     +volume*np.einsum("rma,aij->rmij", inverse_first, prolong.FLAT_WEIGHTS)
                     +np.einsum("ram,aij->rmij", multiplier_first, prolong.Q_WEIGHTS))
    spin = prolong.spin_lift(omega)
    connection = np.array([np.kron(np.eye(3), b) for b in spin])
    p = psi.reshape(-1)
    operator = odd.real_law.real_operator(
        p, psi_first.reshape(4, 12), cartan.kinetic_weights(e, multiplier), connection,
        volume*prior.MASS_WEIGHT, np.einsum("mmij->ij", weights_first))
    covariant = operator["covariant"]
    cq = np.einsum("i,aij,mj->am", p.conj(), prolong.Q_WEIGHTS, covariant).imag
    cq2 = np.einsum("i,aij,mj->am", p.conj(), Q2_WEIGHTS, covariant).imag
    scalar = volume*(4+prior.weighted_mass(psi))+np.sum(multiplier*cq2)
    probe_contraction = np.vdot(p, Q_FULL @ operator["symmetric"]).real
    constraint_contraction = volume*np.sum(inverse.T*(cq-e))
    z_contraction = np.vdot(p, 0.5j*Q_FULL @ operator["defect"] @ p)
    return {"scalar": float(scalar), "probe_contraction": float(probe_contraction),
            "constraint_contraction": float(constraint_contraction),
            "identity_error": float(scalar+probe_contraction+constraint_contraction),
            "Z_real_contraction": float(z_contraction.real),
            "Z_contraction_magnitude": float(abs(z_contraction)),
            "Z_norm": float(np.linalg.norm(operator["defect"])),
            "Q_Z_commutator_norm": float(np.linalg.norm(Q_FULL @ operator["defect"]-operator["defect"] @ Q_FULL)),
            "probe": operator["symmetric"], "constraint": cq-e, "q2_cross": cq2}


def covariant_jets(prepared, point, jets):
    connection = regular.connection_second(prepared, point, jets)
    b0, b1, b2 = (prolong.spin_lift(connection[k]) for k in ("omega", "first", "second"))
    psi, p1, p2 = prepared["data"]["psi"], point["psi_first"], jets["p2"]
    d0 = cartan.covariant_jet(psi, p1, connection["omega"])
    d1 = p2+np.einsum("smij,rj->smri", b1, psi)+np.einsum("mij,srj->smri", b0, p1)
    d2 = (jets["p3"]+np.einsum("stmij,rj->stmri", b2, psi)
          +np.einsum("smij,trj->stmri", b1, p1)+np.einsum("tmij,srj->stmri", b1, p1)
          +np.einsum("mij,strj->stmri", b0, p2))
    return d0, d1, d2


def scalar_jet(prepared, point, jets):
    """A, dA and symmetric d2A at E=I, dE=0, without assuming lambda=0."""
    psi, p1, p2 = prepared["data"]["psi"], point["psi_first"], jets["p2"]
    l0, l1, l2 = point["multiplier"], point["multiplier_first"], jets["l2"]
    d0, d1, d2 = covariant_jets(prepared, point, jets)
    pair = odd.readouts.pairing
    q2 = Q @ Q
    t0 = pair(psi, d0, q2).imag
    t1 = np.array([(pair(p1[r], d0, q2)+pair(psi, d1[r], q2)).imag for r in range(4)])
    t2 = np.array([[(pair(p2[r, s], d0, q2)+pair(p1[r], d1[s], q2)
                     +pair(p1[s], d1[r], q2)+pair(psi, d2[r, s], q2)).imag
                    for s in range(4)] for r in range(4)])
    b0 = prior.weighted_mass(psi)
    b1 = np.array([2*np.vdot(psi, H_MASS @ p @ BETA.T).real for p in p1])
    b2 = np.array([[2*np.vdot(psi, H_MASS @ p2[r, s] @ BETA.T).real
                   +2*np.vdot(p1[r], H_MASS @ p1[s] @ BETA.T).real
                   for s in range(4)] for r in range(4)])
    pieces = {
        "volume": np.einsum("rsaa->rs", point["coframe_second"])*(4+b0),
        "mass": b2,
        "lambda_second": np.einsum("rsam,am->rs", l2, t0),
        "lambda_first_cross": np.einsum("ram,sam->rs", l1, t1)+np.einsum("sam,ram->rs", l1, t1),
        "lambda_value_cross_second": np.einsum("am,rsam->rs", l0, t2)}
    return {"value": float(4+b0+np.sum(l0*t0)),
            "first": b1+np.einsum("ram,am->r", l1, t0)+np.einsum("am,ram->r", l0, t1),
            "hessian": sum(pieces.values()), "pieces": pieces,
            "cross_q2": t0, "cross_q2_first": t1, "cross_q2_second": t2}


def scalar_field(prepared, point, jets, displacement):
    fields = regular.taylor_fields(prepared, point, jets, displacement)
    psi = fields["psi"].reshape(-1)
    covariant = cartan.covariant_jet(fields["psi"], fields["psi_first"], fields["omega"]).reshape(4, 12)
    q2 = np.einsum("i,aij,mj->am", psi.conj(), Q2_WEIGHTS, covariant).imag
    return float(abs(np.linalg.det(fields["coframe"]))*(4+prior.weighted_mass(fields["psi"]))
                 +np.sum(fields["multiplier"]*q2))


def hessian_difference(prepared, point, jets, step):
    """Symmetric stencil on the actual eliminated-Cartan Taylor fields, not the jet formula."""
    result = np.zeros((4, 4))
    origin = scalar_field(prepared, point, jets, np.zeros(4))
    for r, s in PAIR2:
        a, b = np.eye(4)[r], np.eye(4)[s]
        if r == s:
            value = (scalar_field(prepared, point, jets, step*a)-2*origin
                     +scalar_field(prepared, point, jets, -step*a))/step**2
        else:
            corners = [scalar_field(prepared, point, jets, step*(u*a+v*b))
                       for u, v in ((1, 1), (1, -1), (-1, 1), (-1, -1))]
            value = (corners[0]-corners[1]-corners[2]+corners[3])/(4*step**2)
        result[r, s] = result[s, r] = value
    return result


def independent_differences(prepared, point, jets):
    analytic = scalar_jet(prepared, point, jets)["hessian"]
    checks = []
    for step in (0.001, 0.0003, 0.0001):
        coarse = hessian_difference(prepared, point, jets, step)
        fine = hessian_difference(prepared, point, jets, step/2)
        extrapolated = (4*fine-coarse)/3
        checks.append({"step": step, "coarse_error": float(np.linalg.norm(coarse-analytic)),
                       "fine_error": float(np.linalg.norm(fine-analytic)),
                       "Richardson_error": float(np.linalg.norm(extrapolated-analytic)),
                       "Richardson_hessian": extrapolated.tolist()})
    return checks


def packed_hessian(prepared, point, coordinates):
    hessian = scalar_jet(prepared, point, regular.unpack(coordinates))["hessian"]
    return np.array([hessian[p] for p in PAIR2])


def joint_system(prepared, point):
    """Retain every prior equation and all ten Hessian entries, without row projection."""
    first_connection = spatial.connection_first(prepared, point)

    def image(x):
        jets = regular.unpack(x)
        return np.concatenate((regular.equations(prepared, point, jets, first_connection)["vector"],
                               packed_hessian(prepared, point, x)))

    return spatial.affine_system(image, 1200)


def random_identity_checks(seed=20261018, count=12):
    rng = np.random.default_rng(seed)
    result = []
    for index in range(count):
        e = np.eye(4)+rng.normal(size=(4, 4))*.1
        de = rng.normal(size=(4, 4, 4))*.2
        psi = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
        p1 = rng.normal(size=(4, 3, 4))+1j*rng.normal(size=(4, 3, 4))
        omega = cartan.unpack(rng.normal(size=24)*.3)
        lam = rng.normal(size=(4, 4))*.2
        dl = rng.normal(size=(4, 4, 4))*.3
        audit = off_shell_identity(e, de, psi, p1, omega, lam, dl)
        result.append({k: audit[k] for k in ("scalar", "probe_contraction", "constraint_contraction",
                                            "identity_error", "Z_real_contraction", "Z_contraction_magnitude",
                                            "Z_norm", "Q_Z_commutator_norm")})
    return result


def residual_summary(prepared, point, coordinates):
    jets = regular.unpack(coordinates)
    equations = regular.equations(prepared, point, jets)
    scalar = scalar_jet(prepared, point, jets)
    combined = np.concatenate((equations["vector"], np.array([scalar["hessian"][p] for p in PAIR2])))
    return {"all_394_norm": float(np.linalg.norm(combined)), "all_394_max_abs": float(np.max(abs(combined))),
            "previous_384_norm": float(np.linalg.norm(equations["vector"])),
            "constraint_first_norm": float(np.linalg.norm(equations["constraint_first"])),
            "probe_first_norm": float(np.linalg.norm(equations["probe_first"])),
            "coframe_Euler_first_norm": float(np.linalg.norm(equations["coframe_Euler_first"])),
            "constraint_second_full_symmetric_norm": float(np.linalg.norm(equations["constraint_second"])),
            "scalar_value": scalar["value"], "scalar_first": scalar["first"].tolist(),
            "scalar_hessian": scalar["hessian"].tolist(),
            "scalar_hessian_full_symmetric_norm": float(np.linalg.norm(scalar["hessian"])),
            "hessian_piece_norms": {k: float(np.linalg.norm(v)) for k, v in scalar["pieces"].items()},
            "full_394_residual": combined.tolist()}


def evaluate():
    fingerprints = input_fingerprints()
    identities = random_identity_checks()
    prepared, point, saved = load_data()
    solved = joint_system(prepared, point)
    matrix, base = solved["matrix"], solved["base"]
    old_rank = int(np.linalg.matrix_rank(matrix[:384], tol=np.linalg.svd(matrix[:384], compute_uv=False)[0]*1e-10))
    hessian_rank = int(np.linalg.matrix_rank(matrix[384:], tol=1e-9))
    rng = np.random.default_rng(2121)
    random_coordinates = rng.normal(size=1200)*.2
    affine_error = np.linalg.norm(solved["evaluate"](random_coordinates)-base-matrix @ random_coordinates)
    old = residual_summary(prepared, point, saved)
    new = residual_summary(prepared, point, solved["solution"])
    point_equations = spatial.rank_model.point_equations(
        prepared, point["psi_first"], point["coframe_second"], point["multiplier"], point["multiplier_first"])
    kept = {"psi_real": prepared["data"]["psi"].real.tolist(), "psi_imag": prepared["data"]["psi"].imag.tolist(),
            "psi_first_real": point["psi_first"].real.tolist(), "psi_first_imag": point["psi_first"].imag.tolist(),
            "coframe_value": np.eye(4).tolist(), "coframe_first": np.zeros((4, 4, 4)).tolist(),
            "coframe_second": point["coframe_second"].tolist(), "multiplier": point["multiplier"].tolist(),
            "multiplier_first": point["multiplier_first"].tolist(), "Q_real": Q.real.tolist(), "Q_imag": Q.imag.tolist(),
            "M_real": MASS.real.tolist(), "M_imag": MASS.imag.tolist(), "Einstein_coefficient": 1., "vacuum": 0.}
    if fingerprints != input_fingerprints():
        raise RuntimeError("Authoritative inputs changed during the audit; results not saved")
    return {"status": "bounded next scalar gate in added neutral odd-cross Cartan comparison; no Cauchy solution or native physics",
            "date": "2026-10-18", "input_sha256": fingerprints,
            "off_shell_identity": {"formula": "A = -Re(Psi^dagger Q R) - v e_a^mu F^a_mu; F=C[Q]-E",
                                   "assumptions": ["constant Hermitian internal Q", "common neutral Lorentz spin connection commuting with Q",
                                                   "real coframe and multiplier", "Hermitian M; no assumption [M,Q]=0",
                                                   "complete variable-weight real probe operator, including Z"],
                                   "random_controls": identities},
            "fixed_lower_point_and_couplings": kept,
            "original_point_56_residual_norm": float(np.linalg.norm(point_equations["vector"])),
            "frozen_saved_1200_jet": old,
            "frozen_saved_jet_independent_differences": independent_differences(prepared, point, regular.unpack(saved)),
            "joint_394_system": {"shape": list(matrix.shape), "previous_384_rank": old_rank,
                                 "rank": solved["rank"], "hessian_10_rank": hessian_rank,
                                 "additional_rank": solved["rank"]-old_rank,
                                 "kernel_dimension": 1200-solved["rank"],
                                 "singular_values": solved["singular_values"].tolist(),
                                 "coefficient_block_ranks": {name: int(np.linalg.matrix_rank(matrix[384:, a:b], tol=1e-9))
                                                             for name, a, b in (("Psi2", 0, 240), ("lambda2", 240, 400),
                                                                               ("E3", 400, 720), ("Psi3", 720, 1200))},
                                 "affine_random_control_error": float(affine_error),
                                 "full_unprojected": True,
                                 "lower_point_unchanged": True,
                                 "coordinate_layout": "Psi2 real/imag 0:240; lambda2 240:400; E3 400:720; Psi3 real/imag 720:1200; symmetric lexicographic pairs/triples",
                                 "jet_coordinates": solved["solution"].tolist(),
                                 "coordinate_change_norm": float(np.linalg.norm(solved["solution"]-saved)),
                                 "residuals": new},
            "completed_jet_independent_differences": independent_differences(prepared, point, regular.unpack(solved["solution"])),
            "highest_derivatives_used": {"Psi": 3, "E": 3, "lambda": 2},
            "new_higher_derivatives_cannot_change_the_frozen_hessian": True,
            "affine_only_after_fixing_the_lower_point": True,
            "remaining": ["full third constraint and second probe/gravity systems are not solved",
                          "no open-surface Cauchy data, propagation, convergence or local existence",
                          "no native action/HC/C7 or physical-scale identification"],
            "main_TeX_PDF_release_changed": False, "git_operations": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = evaluate()
    encoded = json.dumps(payload, indent=2, allow_nan=False)+"\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    print(json.dumps({"status": payload["status"], "frozen": payload["frozen_saved_1200_jet"]["scalar_hessian_full_symmetric_norm"],
                      "joint_shape": payload["joint_394_system"]["shape"], "rank": payload["joint_394_system"]["rank"],
                      "residual_norm": payload["joint_394_system"]["residuals"]["all_394_norm"]}, indent=2))


if __name__ == "__main__":
    main()
