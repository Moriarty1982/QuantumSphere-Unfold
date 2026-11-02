"""Temporal constraint rank of the neutral odd-cross Cartan comparison.

Positive probe weights do not imply an invertible coupled evolution block.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "cartan_cauchy_prolongation", Path(__file__).with_name("HC_Cartan_Prolongation.py"))
prolong = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prolong)
cartan, prior, odd = prolong.cartan, prolong.prior, prolong.odd
Q, WEIGHTS, ETA, MASS = prolong.Q, prolong.WEIGHTS, prolong.ETA, prolong.MASS
A = prolong.Q_WEIGHTS
SIGMA = np.array([-1j*WEIGHTS[j] @ WEIGHTS[k] for j, k in ((2, 3), (3, 1), (1, 2))])
DIRECTION = np.array([0.1, 0.2, -0.3, 0.4])


def load_data():
    prepared = prolong.prepare()
    payload = json.loads(Path(__file__).with_name("HC_Cartan_Prolongation.json").read_text(encoding="utf-8"))
    return prepared, prolong.unpack(payload["jet_coordinates"])


def temporal_selector(ell):
    ell = cartan.checks._real(ell, (4,), "temporal multiplier column")
    multiplier = np.zeros((4, 4))
    multiplier[:, 0] = ell
    return multiplier


def probe_constraint_block(coframe, psi, multiplier):
    """Schur block after solving the real probe equation for its time derivative."""
    psi = cartan.checks._finite(psi, "three-channel spinor value")
    if psi.shape != (3, 4):
        raise ValueError("Three four-component spinors required")
    p = psi.reshape(-1)
    k0 = cartan.kinetic_weights(coframe, multiplier)[0]
    eigenvalues = np.linalg.eigvalsh(k0)
    if eigenvalues[0] <= 0:
        raise ValueError("Positive invertible temporal probe density required for this reduction")
    vectors = np.array([np.linalg.solve(k0, a @ p) for a in A])
    block = np.array([[-0.5*np.vdot(p, a @ vector).imag for vector in vectors] for a in A])
    return {"block": block, "weights": k0, "weight_eigenvalues": eigenvalues,
            "singular_values": np.linalg.svd(block, compute_uv=False),
            "pfaffian": float(block[0, 1]*block[2, 3]-block[0, 2]*block[1, 3]+block[0, 3]*block[1, 2])}


def spin_vectors(psi):
    values, basis = np.linalg.eigh(Q)
    channels = basis.conj().T @ psi
    s = np.array([np.array([np.vdot(p, sigma @ p).real for sigma in SIGMA]) for p in channels])
    return {"minus": s[0], "plus": s[-1],
            "weighted_second": np.einsum("r,ri->i", values**2, s),
            "weighted_third": np.einsum("r,ri->i", values**3, s)}


def zero_multiplier_formula(psi):
    w = spin_vectors(psi)["weighted_second"]
    block = np.zeros((4, 4))
    block[1:, 1:] = np.array([[0, -w[2], w[1]], [w[2], 0, -w[0]], [-w[1], w[0], 0]])/2
    return block


def pfaffian_formula(psi, ell):
    """Exact for E=I and the declared Q spectrum (-1/2,0,+1/2)."""
    ell = cartan.checks._real(ell, (4,), "temporal multiplier column")
    s = spin_vectors(psi)
    dplus = (1+ell[0]/2)**2-np.dot(ell[1:], ell[1:])/4
    dminus = (1-ell[0]/2)**2-np.dot(ell[1:], ell[1:])/4
    if abs(dplus*dminus) < 1e-15:
        raise ValueError("Singular spectral temporal block excluded")
    return float(np.dot(ell[1:], np.cross(s["plus"], s["minus"]))/(64*dplus*dminus))


def point_equations(prepared, psi_first, coframe_second, multiplier, multiplier_first):
    """Original independent equations after eliminating the same Cartan connection."""
    psi = prepared["data"]["psi"]
    response, source, inverse = prepared["response"], prepared["source"], prepared["inverse_hessian"]
    k0 = inverse @ (-source+response.T @ multiplier.reshape(-1))
    omega = cartan.unpack(k0)
    source_first = 2*np.einsum("ri,pij,srj->sp", psi.conj(), prepared["source_forms"], psi_first).real
    response_first = -2*np.einsum("ri,pamij,srj->samp", (Q @ psi).conj(), prepared["component_forms"], psi_first).real
    rhs = (-source_first+np.einsum("samp,am->sp", response_first, multiplier)
           +multiplier_first.reshape(4, 16) @ response)
    k1 = rhs @ inverse.T
    omega_first = np.array([prolong.normal_lorentz(v) for v in coframe_second])+np.einsum("sp,pmab->smab", k1, cartan.OMEGA_BASIS)
    covariant = cartan.covariant_jet(psi, psi_first, omega)
    constraint = odd.channels(psi, covariant)["odd"]-np.eye(4)
    connection = np.array([np.kron(np.eye(3), b) for b in prolong.spin_lift(omega)])
    weights = cartan.kinetic_weights(np.eye(4), multiplier)
    divergence = np.einsum("mam,aij->ij", multiplier_first, A)
    operator = odd.real_law.real_operator(psi.reshape(-1), psi_first.reshape(4, 12), weights,
                                          connection, prior.MASS_WEIGHT, divergence)
    coframe = cartan.coframe_euler(np.eye(4), psi, psi_first, omega,
                                  cartan.curvature_upper(omega, omega_first), MASS, multiplier)
    return {"constraint": constraint, "probe": operator["symmetric"], "coframe": coframe,
            "vector": np.concatenate((constraint.reshape(-1), prior.realify(operator["symmetric"]), coframe.reshape(-1)))}


def normal_matrix(prepared, jets, multiplier=None):
    """56 equations for E_,00 (16), Psi_,0 (24), lambda_,0 (16), other jets fixed."""
    multiplier = np.zeros((4, 4)) if multiplier is None else multiplier

    def evaluate(vector):
        e2, p1, l1 = (v.copy() for v in (jets["e2"], prepared["data"]["first"], jets["l1"]))
        e2[0, 0] = vector[:16].reshape(4, 4)
        p1[0] = prior.complexify(vector[16:40], (3, 4))
        l1[0] = vector[40:].reshape(4, 4)
        return point_equations(prepared, p1, e2, multiplier, l1)["vector"]

    base = evaluate(np.zeros(56))
    matrix = np.column_stack([evaluate(e)-base for e in np.eye(56)])
    _, singular, _ = np.linalg.svd(matrix)
    solution = np.linalg.lstsq(matrix, -base, rcond=1e-10)[0]
    return {"matrix": matrix, "base": base, "rank": int(np.sum(singular > singular[0]*1e-10)),
            "singular_values": singular, "best_residual": float(np.linalg.norm(matrix @ solution+base)),
            "evaluate": evaluate}


def normal_probe_matrix(psi, multiplier):
    """28-by-28 temporal probe/coframe-column coefficient matrix, before gravitational equations."""
    weights = cartan.kinetic_weights(np.eye(4), multiplier)[0]
    p = psi.reshape(-1)

    def image(vector):
        time = prior.complexify(vector[:24], (12,))
        dlambda = vector[24:]
        residual = 1j*weights @ time+0.5j*sum(d*a @ p for d, a in zip(dlambda, A))
        frame = np.array([np.vdot(p, a @ time).imag for a in A])
        return np.concatenate((prior.realify(residual), frame))
    return np.column_stack([image(e) for e in np.eye(28)])


def scalar_second_gate(prepared, jets):
    """Second derivative of the existing scalar on-shell consequence, at the normal point."""
    psi, first = prepared["data"]["psi"], prepared["data"]["first"]
    h = (Q @ MASS+MASS @ Q)/2
    omega1, _ = prolong.connection_jets(prepared, jets)
    spin0 = prolong.spin_lift(prepared["data"]["omega"])
    cov0 = prepared["data"]["covariant"]
    cov1 = (jets["p2"]+np.einsum("smij,rj->smri", prolong.spin_lift(omega1), psi)
            +np.einsum("mij,srj->smri", spin0, first))
    c2 = odd.readouts.pairing(psi, cov0, Q @ Q).imag
    c2_first = np.array([(odd.readouts.pairing(u, cov0, Q @ Q)
                          +odd.readouts.pairing(psi, v, Q @ Q)).imag for u, v in zip(first, cov1)])
    result = np.empty((4, 4))
    for r, s in np.ndindex((4, 4)):
        result[r, s] = (2*np.vdot(psi, h @ jets["p2"][r, s] @ prior.BETA.T).real
                         +2*np.vdot(first[r], h @ first[s] @ prior.BETA.T).real
                         +np.sum(jets["l2"][r, s]*c2)
                         +np.sum(jets["l1"][r]*c2_first[s])+np.sum(jets["l1"][s]*c2_first[r]))
    return result


def scalar_density(prepared, jets, point):
    fields = prolong.taylor_fields(prepared, jets, point)
    volume = abs(np.linalg.det(fields["coframe"]))
    covariant = cartan.covariant_jet(fields["psi"], fields["first_p"], fields["omega"])
    q2 = odd.readouts.pairing(fields["psi"], covariant, Q @ Q).imag
    return float(volume*(4+prior.weighted_mass(fields["psi"]))+np.sum(fields["multiplier"]*q2))


def scalar_second_difference(prepared, jets, step=0.0001):
    result = np.zeros((4, 4))
    base = scalar_density(prepared, jets, np.zeros(4))
    for r, s in prior.PAIR2:
        a, b = np.eye(4)[r], np.eye(4)[s]
        if r == s:
            result[r, r] = (scalar_density(prepared, jets, step*a)-2*base+scalar_density(prepared, jets, -step*a))/step**2
        else:
            values = [scalar_density(prepared, jets, step*(sa*a+sb*b)) for sa, sb in ((1, 1), (1, -1), (-1, 1), (-1, -1))]
            result[r, s] = result[s, r] = (values[0]-values[1]-values[2]+values[3])/(4*step**2)
    return result


def normal_probe_source(prepared, psi_first, coframe_second, multiplier, multiplier_first):
    first, l1 = psi_first.copy(), multiplier_first.copy()
    first[0], l1[0, :, 0] = 0, 0
    residual = point_equations(prepared, first, coframe_second, multiplier, l1)
    return np.concatenate((prior.realify(residual["probe"]), residual["constraint"][:, 0]))


def regular_point(prepared, multiplier=None):
    """Reprepare all point equations on a regular temporal block; no differentiated constraints."""
    multiplier = temporal_selector(0.1*DIRECTION) if multiplier is None else multiplier

    def unpack_point(vector):
        return (prior.complexify(vector[:96], (4, 3, 4)),
                prior.unpack_second(vector[96:256]), vector[256:].reshape(4, 4, 4))

    def evaluate_point(vector):
        p1, e2, l1 = unpack_point(vector)
        return point_equations(prepared, p1, e2, multiplier, l1)

    base = evaluate_point(np.zeros(320))["vector"]
    matrix = np.column_stack([evaluate_point(e)["vector"]-base for e in np.eye(320)])
    solution, _, rank, singular = np.linalg.lstsq(matrix, -base, rcond=1e-10)
    p1, e2, l1 = unpack_point(solution)
    return {"multiplier": multiplier, "psi_first": p1, "coframe_second": e2, "multiplier_first": l1,
            "rank": int(rank), "matrix": matrix, "base": base, "solution": solution,
            "singular_values": singular, "equations": evaluate_point(solution)}


def evaluate():
    prepared, jets = load_data()
    psi = prepared["data"]["psi"]
    points = []
    for scale in (0., 0.0001, 0.001, 0.01, 0.1):
        ell = scale*DIRECTION
        block = probe_constraint_block(np.eye(4), psi, temporal_selector(ell))
        points.append({"scale": scale, "temporal_multiplier_column": ell.tolist(),
                       "minimum_temporal_probe_eigenvalue": float(block["weight_eigenvalues"][0]),
                       "constraint_block_singular_values": block["singular_values"].tolist(),
                       "pfaffian": block["pfaffian"], "analytic_pfaffian": pfaffian_formula(psi, ell),
                       "inverse_constraint_norm": float(1/block["singular_values"][-1]) if scale else None,
                       "probe_temporal_28_rank": int(np.linalg.matrix_rank(normal_probe_matrix(psi, temporal_selector(ell)), tol=1e-10))})
    zero = normal_matrix(prepared, jets)
    regular = normal_matrix(prepared, jets, temporal_selector(0.1*DIRECTION))
    secondary = scalar_second_gate(prepared, jets)
    point = regular_point(prepared)
    point_prepared = dict(prepared)
    point_prepared["data"] = dict(prepared["data"], first=point["psi_first"])
    point_jets = dict(jets, e2=point["coframe_second"], l1=point["multiplier_first"])
    point_normal = normal_matrix(point_prepared, point_jets, point["multiplier"])
    _, _, vh = np.linalg.svd(regular["matrix"])
    kernel = vh[regular["rank"]:].T
    spatial_multiplier_indices = [40+4*a+i for a in range(4) for i in range(1, 4)]
    return {"status": "temporal rank/constraint propagation audit of a neutral comparison; not a full Cauchy or native solution",
            "previous_input_sha256": hashlib.sha256(Path(__file__).with_name("HC_Cartan_Prolongation.json").read_bytes()).hexdigest(),
            "zero_multiplier_constraint_block": zero_multiplier_formula(psi).tolist(),
            "spin_vectors": {k: v.tolist() for k, v in spin_vectors(psi).items()}, "positive_weight_rank_change": points,
            "full_normal_56_zero_multiplier_rank": zero["rank"],
            "full_normal_56_regular_control_rank": regular["rank"],
            "full_normal_fixed_spatial_data_zero_best_residual": zero["best_residual"],
            "regular_control_fixed_spatial_data_best_residual": regular["best_residual"],
            "regular_control_is_off_shell_not_reprepared_initial_data": True,
            "regular_normal_kernel_dimension": 56-regular["rank"],
            "normal_coframe_acceleration_block_rank": int(np.linalg.matrix_rank(regular["matrix"][:, :16], tol=1e-10)),
            "normal_kernel_spatial_multiplier_projection_rank": int(np.linalg.matrix_rank(kernel[spatial_multiplier_indices], tol=1e-10)),
            "frozen_previous_second_scalar_gate": secondary.tolist(),
            "frozen_previous_second_scalar_gate_norm": float(np.linalg.norm(secondary)),
            "second_scalar_gate_independent_difference_error": float(np.linalg.norm(scalar_second_difference(prepared, jets)-secondary)),
            "reprepared_regular_point": {
                "matrix_shape": list(point["matrix"].shape), "matrix_rank": point["rank"],
                "joint_point_residual_norm": float(np.linalg.norm(point["equations"]["vector"])),
                "full_normal_rank": point_normal["rank"], "full_normal_best_residual": point_normal["best_residual"],
                "not_surface_data_or_first_constraint_prolongation": True,
                "multiplier_value": point["multiplier"].tolist(),
                "point_coordinates": point["solution"].tolist()},
            "remaining": ["propagation of spatial constitutive and gravitational constraints on a constant-rank branch",
                          "gauge reduction and remaining multiplier evolution", "native action/gauge/HC/C7 identification, physical scales and full local/global existence"],
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
