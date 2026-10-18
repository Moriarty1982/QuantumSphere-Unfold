"""First spatial-constraint integrability of the neutral odd-cross Cartan parent.

Pointwise prolongation and rank checks, not a Cauchy propagation theorem.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "cartan_spatial_rank", Path(__file__).with_name("HC_Cartan_Cauchy_Rank.py"))
rank_model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(rank_model)
prolong, cartan, prior, odd = rank_model.prolong, rank_model.cartan, rank_model.prior, rank_model.odd
Q, A = rank_model.Q, rank_model.A
PAIRS = cartan.PAIRS


def load_point():
    prepared, _ = rank_model.load_data()
    payload = json.loads(Path(__file__).with_name("HC_Cartan_Cauchy_Rank.json").read_text(encoding="utf-8"))
    point = payload["reprepared_regular_point"]
    x = np.array(point["point_coordinates"])
    return prepared, {"multiplier": np.array(point["multiplier_value"]),
                      "psi_first": prior.complexify(x[:96], (4, 3, 4)),
                      "coframe_second": prior.unpack_second(x[96:256]),
                      "multiplier_first": x[256:].reshape(4, 4, 4)}


def connection_first(prepared, point):
    """Algebraic Cartan solution and its derivative at E=I, dE=0, general lambda."""
    psi, first = prepared["data"]["psi"], point["psi_first"]
    multiplier, l1 = point["multiplier"], point["multiplier_first"]
    inverse, response = prepared["inverse_hessian"], prepared["response"]
    k = inverse @ (-prepared["source"]+response.T @ multiplier.reshape(-1))
    source_first = 2*np.einsum("ri,pij,srj->sp", psi.conj(), prepared["source_forms"], first).real
    response_first = -2*np.einsum("ri,pamij,srj->samp", (Q @ psi).conj(), prepared["component_forms"], first).real
    k1 = (-source_first+np.einsum("samp,am->sp", response_first, multiplier)
          +l1.reshape(4, 16) @ response) @ inverse.T
    omega1 = (np.array([prolong.normal_lorentz(v) for v in point["coframe_second"]])
              +np.einsum("sp,pmab->smab", k1, cartan.OMEGA_BASIS))
    return cartan.unpack(k), omega1


def constraint_first(prepared, point, psi_second=None):
    psi = prepared["data"]["psi"]
    first = point["psi_first"]
    psi_second = np.zeros((4, 4, 3, 4), complex) if psi_second is None else psi_second
    omega, omega1 = connection_first(prepared, point)
    b0, b1 = prolong.spin_lift(omega), prolong.spin_lift(omega1)
    cov0 = cartan.covariant_jet(psi, first, omega)
    cov1 = (psi_second+np.einsum("smij,rj->smri", b1, psi)
            +np.einsum("mij,srj->smri", b0, first))
    pair = odd.readouts.pairing
    return np.array([(pair(first[r], cov0, Q)+pair(psi, cov1[r], Q)).imag for r in range(4)])


def curl_constraints(prepared, point):
    first = constraint_first(prepared, point)
    return np.array([first[r, :, s]-first[s, :, r] for r, s in PAIRS])


def constraint_principal_map(psi):
    """Four real linear functionals on one second spinor derivative."""
    p = psi.reshape(-1)
    return np.column_stack([np.array([np.vdot(p, a @ prior.complexify(e, (12,))).imag for a in A])
                            for e in np.eye(24)])


def symmetric_constraint_completion(prepared, point):
    base = constraint_first(prepared, point)
    principal = constraint_principal_map(prepared["data"]["psi"])
    if np.linalg.matrix_rank(principal, tol=1e-10) != 4:
        raise ValueError("Surjective spinor-to-coframe principal map required")
    inverse = np.linalg.pinv(principal, rcond=1e-10)
    second = np.zeros((4, 4, 3, 4), complex)
    for r, s in prior.PAIR2:
        target = -(base[r, :, s]+base[s, :, r])/2
        second[r, s] = second[s, r] = prior.complexify(inverse @ target, (3, 4))
    return {"psi_second": second, "residual": constraint_first(prepared, point, second),
            "principal": principal}


def explicit_curl(prepared, point):
    """Coordinate product rule, without any second spinor derivative."""
    psi, first = prepared["data"]["psi"], point["psi_first"]
    omega, omega1 = connection_first(prepared, point)
    b0, b1 = prolong.spin_lift(omega), prolong.spin_lift(omega1)
    p = psi.reshape(-1)
    f = first.reshape(4, 12)
    bc = np.array([np.kron(np.eye(3), b) for b in b0])
    bc1 = np.array([[np.kron(np.eye(3), b) for b in row] for row in b1])
    return np.array([[np.imag(
        np.vdot(f[r], a @ (f[s]+bc[s] @ p))-np.vdot(f[s], a @ (f[r]+bc[r] @ p))
        +np.vdot(p, a @ ((bc1[r, s]-bc1[s, r]) @ p+bc[s] @ f[r]-bc[r] @ f[s])))
                      for a in A] for r, s in PAIRS])


def affine_system(evaluate, size):
    base = evaluate(np.zeros(size))
    matrix = np.column_stack([evaluate(e)-base for e in np.eye(size)])
    solution, _, rank, singular = np.linalg.lstsq(matrix, -base, rcond=1e-10)
    return {"matrix": matrix, "base": base, "solution": solution, "rank": int(rank),
            "singular_values": singular, "residual": evaluate(solution), "evaluate": evaluate}


def normal_curl_system(prepared, point):
    """Original normal unknowns plus the twelve mixed temporal/spatial curl conditions."""
    def image(x):
        p = dict(point)
        p["coframe_second"] = point["coframe_second"].copy()
        p["psi_first"] = point["psi_first"].copy()
        p["multiplier_first"] = point["multiplier_first"].copy()
        p["coframe_second"][0, 0] = x[:16].reshape(4, 4)
        p["psi_first"][0] = prior.complexify(x[16:40], (3, 4))
        p["multiplier_first"][0] = x[40:].reshape(4, 4)
        equations = rank_model.point_equations(prepared, p["psi_first"], p["coframe_second"],
                                               p["multiplier"], p["multiplier_first"])["vector"]
        return np.concatenate((equations, curl_constraints(prepared, p)[:3].reshape(-1)))
    solved = affine_system(image, 56)
    matrix, base = solved["matrix"], solved["base"]
    normal, curl = matrix[:56], matrix[56:]
    _, sv, vh = np.linalg.svd(normal)
    normal_rank = int(np.sum(sv > sv[0]*1e-10))
    kernel = vh[normal_rank:].T
    induced = curl @ kernel
    u, sv, _ = np.linalg.svd(induced, full_matrices=True)
    induced_rank = int(np.sum(sv > sv[0]*1e-10))
    null_left = u[:, induced_rank:]
    particular = np.linalg.lstsq(normal, -base[:56], rcond=1e-10)[0]
    _, _, vh = np.linalg.svd(matrix, full_matrices=True)
    full_kernel = vh[solved["rank"]:].T
    indices = [40+4*a+i for a in range(4) for i in range(1, 4)]
    return dict(solved, original_rank=normal_rank, original_kernel=kernel,
                induced_curl=induced, induced_rank=induced_rank, left_null=null_left,
                compatibility_projection=null_left.T @ (curl @ particular+base[56:]),
                remaining_kernel=full_kernel,
                remaining_spatial_multiplier_rank=int(np.linalg.matrix_rank(full_kernel[indices], tol=1e-10)))


def reprepare_curls(prepared, point):
    """Keep the regular point's psi and first psi jet; vary E2 and d lambda."""
    def fields(x):
        return dict(point, coframe_second=prior.unpack_second(x[:160]),
                    multiplier_first=x[160:].reshape(4, 4, 4))

    def image(x):
        p = fields(x)
        equations = rank_model.point_equations(prepared, p["psi_first"], p["coframe_second"],
                                               p["multiplier"], p["multiplier_first"])["vector"]
        return np.concatenate((equations, curl_constraints(prepared, p).reshape(-1)))
    solved = affine_system(image, 224)
    return dict(solved, point=fields(solved["solution"]))


def first_probe(prepared, point, psi_second, multiplier_second, connection=None):
    """First derivative of the complete real probe equation at E=I, dE=0."""
    psi, p1, e2, l1 = (prepared["data"]["psi"], point["psi_first"],
                       point["coframe_second"], point["multiplier_first"])
    omega, omega1 = connection_first(prepared, point) if connection is None else connection
    b0, b1 = prolong.spin_lift(omega), prolong.spin_lift(omega1)
    cov0 = cartan.covariant_jet(psi, p1, omega).reshape(4, 12)
    cov1 = (psi_second+np.einsum("smij,rj->smri", b1, psi)
            +np.einsum("mij,srj->smri", b0, p1)).reshape(4, 4, 12)
    w0 = cartan.kinetic_weights(np.eye(4), point["multiplier"])
    w1 = np.einsum("sam,aij->smij", l1, A)
    w2 = (np.einsum("staa,mij->stmij", e2, prolong.FLAT_WEIGHTS)
          -np.einsum("stma,aij->stmij", e2, prolong.FLAT_WEIGHTS)
          +np.einsum("stam,aij->stmij", multiplier_second, A))
    bc0 = np.array([np.kron(np.eye(3), b) for b in b0])
    bc1 = np.array([[np.kron(np.eye(3), b) for b in row] for row in b1])
    z0 = np.einsum("mmij->ij", w1)-np.sum(bc0.conj().swapaxes(-1, -2) @ w0+w0 @ bc0, axis=0)
    z1 = np.einsum("smmij->sij", w2)-np.sum(
        bc1.conj().swapaxes(-1, -2) @ w0+bc0.conj().swapaxes(-1, -2) @ w1
        +w1 @ bc0+w0 @ bc1, axis=1)
    return (1j*np.einsum("smij,mj->si", w1, cov0)
            +1j*np.einsum("mij,smj->si", w0, cov1)
            -np.einsum("ij,sj->si", prior.MASS_WEIGHT, p1.reshape(4, 12))
            +0.5j*np.einsum("sij,j->si", z1, psi.reshape(-1))
            +0.5j*np.einsum("ij,sj->si", z0, p1.reshape(4, 12)))


def first_completion(prepared, point):
    def fields(x):
        return prior.unpack_second(x[:240], True), prior.unpack_second(x[240:])

    def image(x):
        p2, l2 = fields(x)
        return np.concatenate((constraint_first(prepared, point, p2).reshape(-1),
                               prior.realify(first_probe(prepared, point, p2, l2))))
    solved = affine_system(image, 400)
    p2, l2 = fields(solved["solution"])
    return dict(solved, psi_second=p2, multiplier_second=l2)


def point_fields(multiplier, x):
    return {"multiplier": multiplier, "psi_first": prior.complexify(x[:96], (4, 3, 4)),
            "coframe_second": prior.unpack_second(x[96:256]),
            "multiplier_first": x[256:].reshape(4, 4, 4)}


def curl_quadratic(x):
    first = prior.complexify(x[:96], (4, 12))
    return np.array([[2*np.vdot(first[r], a @ first[s]).imag for a in A] for r, s in PAIRS]).reshape(-1)


def prepare_integrable_point(prepared, point, max_iterations=20):
    """Re-solve first spinor derivatives as well; keep psi value, lambda value and couplings."""
    multiplier = point["multiplier"]

    def image(x):
        p = point_fields(multiplier, x)
        equations = rank_model.point_equations(prepared, p["psi_first"], p["coframe_second"],
                                               multiplier, p["multiplier_first"])["vector"]
        return np.concatenate((equations, curl_constraints(prepared, p).reshape(-1)))

    base = image(np.zeros(320))
    linear = np.column_stack([image(e)-base for e in np.eye(320)])
    x = np.concatenate((prior.realify(point["psi_first"]),
                        np.array([point["coframe_second"][p] for p in prior.PAIR2]).reshape(-1),
                        point["multiplier_first"].reshape(-1)))
    history = []
    directions = np.eye(96, 320)
    for iteration in range(max_iterations+1):
        value = image(x)
        norm = float(np.linalg.norm(value))
        jacobian = linear.copy()
        q = curl_quadratic(x)
        jacobian[56:, :96] += np.column_stack([curl_quadratic(x+e)-q for e in directions])
        delta, _, rank, singular = np.linalg.lstsq(jacobian, -value, rcond=1e-10)
        history.append({"iteration": iteration, "residual_norm": norm, "jacobian_rank": int(rank)})
        if norm < 1e-11 or iteration == max_iterations:
            break
        for power in range(20):
            step = 2.**-power
            if np.linalg.norm(image(x+step*delta)) < norm:
                x += step*delta
                break
        else:
            break
    return {"point": point_fields(multiplier, x), "solution": x, "residual": image(x),
            "linear": linear, "base": base, "jacobian": jacobian,
            "rank": int(rank), "singular_values": singular, "history": history}


def taylor_fields(prepared, point, completion, displacement):
    x = cartan.checks._real(displacement, (4,), "comparison coordinate displacement")
    e2, p1, l1 = point["coframe_second"], point["psi_first"], point["multiplier_first"]
    p2, l2 = completion["psi_second"], completion["multiplier_second"]
    e3 = completion.get("coframe_third", np.zeros((4, 4, 4, 4, 4)))
    p3 = completion.get("psi_third", np.zeros((4, 4, 4, 3, 4), complex))
    e = np.eye(4)+np.einsum("r,s,rsam->am", x, x, e2)/2
    e += np.einsum("r,s,t,rstam->am", x, x, x, e3)/6
    de = np.einsum("s,rsam->ram", x, e2)
    de += np.einsum("s,t,rstam->ram", x, x, e3)/2
    dde = e2+np.einsum("t,rstam->rsam", x, e3)
    psi = prepared["data"]["psi"]+np.einsum("r,rij->ij", x, p1)+np.einsum("r,s,rsij->ij", x, x, p2)/2
    psi += np.einsum("r,s,t,rstij->ij", x, x, x, p3)/6
    dp = p1+np.einsum("s,rsij->rij", x, p2)
    dp += np.einsum("s,t,rstij->rij", x, x, p3)/2
    lam = point["multiplier"]+np.einsum("r,ram->am", x, l1)+np.einsum("r,s,rsam->am", x, x, l2)/2
    dl = l1+np.einsum("s,rsam->ram", x, l2)
    bundle = prolong.dirac.bundle(e, de, dde)
    hessian, response, source = prolong.fast_cartan_data(prepared, e, psi)
    k = np.linalg.solve(hessian, -source+response.T @ lam.reshape(-1))
    omega = bundle["omega"]+cartan.unpack(k)
    inverse, volume = np.linalg.inv(e), abs(np.linalg.det(e))
    inverse_first = np.array([-inverse @ d @ inverse for d in de])
    volume_first = volume*np.einsum("ma,ram->r", inverse, de)
    weights_first = (np.einsum("r,ma,aij->rmij", volume_first, inverse, prolong.FLAT_WEIGHTS)
                     +volume*np.einsum("rma,aij->rmij", inverse_first, prolong.FLAT_WEIGHTS)
                     +np.einsum("ram,aij->rmij", dl, A))
    connection = np.array([np.kron(np.eye(3), b) for b in prolong.spin_lift(omega)])
    probe = odd.real_law.real_operator(psi.reshape(-1), dp.reshape(4, 12),
                                      cartan.kinetic_weights(e, lam), connection,
                                      volume*prior.MASS_WEIGHT, np.einsum("mmij->ij", weights_first))["symmetric"]
    cross = odd.channels(psi, cartan.covariant_jet(psi, dp, omega))["odd"]
    return {"coframe": e, "coframe_first": de, "coframe_second": dde, "bundle": bundle,
            "psi": psi, "psi_first": dp, "multiplier": lam, "omega": omega,
            "constraint": cross-e, "probe": probe,
            "Cartan": hessian @ k+source-response.T @ lam.reshape(-1)}


def independent_checks(prepared, point, completion, step=2e-5):
    first_c, first_p, first_omega = [], [], []
    for direction in np.eye(4):
        plus, minus = (taylor_fields(prepared, point, completion, sign*step*direction) for sign in (1, -1))
        first_c.append((plus["constraint"]-minus["constraint"])/(2*step))
        first_p.append((plus["probe"]-minus["probe"])/(2*step))
        first_omega.append((plus["omega"]-minus["omega"])/(2*step))
    samples = []
    direction = np.array([1., .3, -.2, .1])
    direction /= np.linalg.norm(direction)
    for radius in (.002, .001, .0005):
        fields = taylor_fields(prepared, point, completion, radius*direction)
        samples.append({"radius": radius, "constraint_norm": float(np.linalg.norm(fields["constraint"])),
                        "probe_norm": float(np.linalg.norm(fields["probe"])),
                        "Cartan_norm": float(np.linalg.norm(fields["Cartan"]))})
    return {"step": step,
            "constraint_first_difference_error": float(np.linalg.norm(np.array(first_c)-constraint_first(prepared, point, completion["psi_second"]))),
            "probe_first_difference_error": float(np.linalg.norm(np.array(first_p)-first_probe(prepared, point, completion["psi_second"], completion["multiplier_second"]))),
            "connection_first_difference_error": float(np.linalg.norm(np.array(first_omega)-connection_first(prepared, point)[1])),
            "samples_not_evolved_solutions": samples}


def evaluate():
    prepared, point = load_point()
    normal = normal_curl_system(prepared, point)
    fixed = first_completion(prepared, point)
    repaired = reprepare_curls(prepared, point)
    completed = first_completion(prepared, repaired["point"])
    integrable = prepare_integrable_point(prepared, point)
    integrable_first = first_completion(prepared, integrable["point"])
    integrable_normal = normal_curl_system(prepared, integrable["point"])
    return {"status": "pointwise spatial integrability audit; not a full propagation or native theorem",
            "previous_input_sha256": hashlib.sha256(Path(__file__).with_name("HC_Cartan_Cauchy_Rank.json").read_bytes()).hexdigest(),
            "frozen_regular_point_curl": curl_constraints(prepared, point).tolist(),
            "normal_with_mixed_curls": {"shape": list(normal["matrix"].shape), "rank": normal["rank"],
                                         "residual_norm": float(np.linalg.norm(normal["residual"])),
                                         "added_rank_on_original_kernel": normal["induced_rank"],
                                         "secondary_compatibility_projection_norm": float(np.linalg.norm(normal["compatibility_projection"]))},
            "frozen_first_completion": {"rank": fixed["rank"], "residual_norm": float(np.linalg.norm(fixed["residual"]))},
            "fixed_spinor_jet_repair_attempt": {
                "shape": list(repaired["matrix"].shape), "rank": repaired["rank"],
                "residual_norm": float(np.linalg.norm(repaired["residual"])),
                "not_a_successful_repair": True},
            "E2_lambda1_only_repair_first_completion": {
                "shape": list(completed["matrix"].shape), "rank": completed["rank"],
                "residual_norm": float(np.linalg.norm(completed["residual"])),
                "not_a_successful_repair": True},
            "spinor_hessian_constraint_principal_rank": int(np.linalg.matrix_rank(constraint_principal_map(prepared["data"]["psi"]), tol=1e-10)),
            "reprepared_first_jet": {"residual_norm": float(np.linalg.norm(integrable["residual"])),
                                      "jacobian_rank": integrable["rank"], "history": integrable["history"],
                                      "point_coordinates": integrable["solution"].tolist(),
                                      "first_completion_shape": list(integrable_first["matrix"].shape),
                                      "first_completion_rank": integrable_first["rank"],
                                      "first_completion_residual_norm": float(np.linalg.norm(integrable_first["residual"])),
                                      "normal_plus_mixed_curl_rank": integrable_normal["rank"],
                                      "normal_plus_mixed_curl_residual_norm": float(np.linalg.norm(integrable_normal["residual"])),
                                      "remaining_normal_kernel_dimension": 56-integrable_normal["rank"],
                                      "remaining_spatial_multiplier_velocity_projection_rank": integrable_normal["remaining_spatial_multiplier_rank"],
                                      "higher_coordinates": integrable_first["solution"].tolist()},
            "independent_checks": independent_checks(prepared, integrable["point"], integrable_first),
            "not_first_coframe_Euler_or_second_constraint_completion": True,
            "main_TeX_changed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = json.dumps(evaluate(), indent=2, allow_nan=False)+"\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
