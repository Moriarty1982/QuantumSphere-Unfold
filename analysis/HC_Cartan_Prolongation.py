"""Joint next-order prolongation of the declared neutral odd-cross Cartan parent.

Finite numerical jets, not a local-existence proof or an evolved native solution.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "cartan_prolongation_prior", Path(__file__).with_name("HC_Cartan_Compatible_Jets.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
cartan, odd, dirac = prior.cartan, prior.odd, prior.dirac
ETA, Q, WEIGHTS, MASS, BETA = prior.ETA, prior.Q, prior.WEIGHTS, prior.MASS, prior.BETA
PAIR2 = prior.PAIR2
PAIR3 = tuple(itertools.combinations_with_replacement(range(4), 3))
FLAT_WEIGHTS = np.array([np.kron(np.eye(3), k) for k in WEIGHTS])
Q_WEIGHTS = np.array([np.kron(Q, k) for k in WEIGHTS])


def load_prior():
    payload = json.loads(Path(__file__).with_name("HC_Cartan_Compatible_Jets.json").read_text(encoding="utf-8"))
    arrays = payload["Taylor_data"]
    psi = np.array(arrays["psi_real"])+1j*np.array(arrays["psi_imag"])
    first = np.array(arrays["psi_first_real"])+1j*np.array(arrays["psi_first_imag"])
    data = prior.first_jet(psi)
    data["first"] = first
    data["covariant"] = cartan.covariant_jet(psi, first, data["omega"])
    return data, {"e2": np.array(arrays["coframe_second"]),
                  "p2": np.array(arrays["psi_second_real"])+1j*np.array(arrays["psi_second_imag"]),
                  "l1": np.array(arrays["multiplier_first"]),
                  "l2": np.zeros((4, 4, 4, 4)), "e3": np.zeros((4, 4, 4, 4, 4)),
                  "p3": np.zeros((4, 4, 4, 3, 4), complex)}


def normal_lorentz(first):
    """Linear LC spin connection at E=I; also applies to its higher normal-point jets."""
    gfirst = np.array([d.T @ ETA+ETA @ d for d in first])
    christoffel = np.empty((4, 4, 4))
    for rho, mu, nu in np.ndindex((4, 4, 4)):
        christoffel[rho, mu, nu] = sum(ETA[rho, s]*(gfirst[mu, s, nu]+gfirst[nu, s, mu]-gfirst[s, mu, nu]) for s in range(4))/2
    return np.array([ETA @ (christoffel[:, mu, :]-first[mu]) for mu in range(4)])


def unpack_third(vector, probe=False):
    trailing = (3, 4) if probe else (4, 4)
    values = prior.complexify(vector, (20, *trailing)) if probe else np.asarray(vector, float).reshape(20, *trailing)
    result = np.zeros((4, 4, 4, *trailing), complex if probe else float)
    for pair, value in zip(PAIR3, values):
        for permutation in set(itertools.permutations(pair)):
            result[permutation] = value
    return result


def unpack(vector):
    vector = np.asarray(vector, float)
    if vector.shape != (1424,):
        raise ValueError("1424 real second/third-order and multiplier coordinates required")
    return {"e2": prior.unpack_second(vector[:160]), "p2": prior.unpack_second(vector[160:400], True),
            "l1": vector[400:464].reshape(4, 4, 4), "l2": prior.unpack_second(vector[464:624]),
            "e3": unpack_third(vector[624:944]), "p3": unpack_third(vector[944:], True)}


def gravity_euler(curvature):
    """Independent coframe EH derivative at E=I and c=1, allowing torsion curvature."""
    scalar = np.einsum("mnmn", curvature)
    return scalar*np.eye(4)/2-np.einsum("anbn->ab", curvature)


def spin_lift(omega):
    return -np.einsum("...mab,aij,bjk->...mik", omega, cartan.GAMMA, cartan.GAMMA)/4


def prepare(data=None):
    data = load_prior()[0] if data is None else data
    psi, first = data["psi"], data["first"]
    response, source = cartan.spin_maps(np.eye(4), psi)
    hessian = cartan.contorsion_hessian(np.eye(4))
    source_forms, source_components, component_forms = [], [], []
    for basis in cartan.SPIN_BASIS:
        terms = np.array([[k @ s for s in basis] for k in WEIGHTS])
        forms = 0.5j*(terms-terms.conj().swapaxes(-1, -2))
        component_forms.append(forms)
        source_forms.append(np.einsum("aaij->ij", forms))
        source_components.append(np.einsum("ri,amij,rj->am", psi.conj(), forms, psi).real)
    source_forms, source_components = np.array(source_forms), np.array(source_components)
    source_first = 2*np.einsum("ri,pij,srj->sp", psi.conj(), source_forms, first).real
    response_first = []
    for u in first:
        response_first.append(cartan.spin_maps(np.eye(4), psi+u)[0]-response-cartan.spin_maps(np.eye(4), u)[0])
    basis_curvature = np.array([cartan.curvature_upper(b) for b in cartan.OMEGA_BASIS])
    curvature_hessian = np.empty((24, 24, 4, 4, 4, 4))
    for p in range(24):
        curvature_hessian[p, p] = 2*basis_curvature[p]
        for q in range(p):
            curvature_hessian[p, q] = curvature_hessian[q, p] = (
                cartan.curvature_upper(cartan.OMEGA_BASIS[p]+cartan.OMEGA_BASIS[q])-basis_curvature[p]-basis_curvature[q])
    hessian_first = []
    for direction in np.eye(16).reshape(16, 4, 4):
        hessian_first.append(np.trace(direction)*hessian
                             -0.5*np.einsum("ma,nb,pqmnab->pq", direction, np.eye(4), curvature_hessian)
                             -0.5*np.einsum("ma,nb,pqmnab->pq", np.eye(4), direction, curvature_hessian))
    return {"data": data, "response": response, "response_first": np.array(response_first),
            "source": source, "source_forms": source_forms, "source_first": source_first,
            "component_forms": np.array(component_forms), "curvature_hessian": curvature_hessian,
            "source_components": source_components, "hessian": hessian, "inverse_hessian": np.linalg.inv(hessian),
            "hessian_first": np.array(hessian_first).reshape(4, 4, 24, 24),
            "k0": cartan.pack(data["omega"])}


def connection_jets(prepared, jets):
    d = prepared
    psi, first = d["data"]["psi"], d["data"]["first"]
    e2, p2, l1, l2, e3 = (jets[k] for k in ("e2", "p2", "l1", "l2", "e3"))
    source_second = (2*np.einsum("ri,pij,strj->stp", psi.conj(), d["source_forms"], p2).real
                     +2*np.einsum("sri,pij,trj->stp", first.conj(), d["source_forms"], first).real
                     +np.einsum("staa,p->stp", e2, d["source"])
                     -np.einsum("stma,pam->stp", e2, d["source_components"]))
    hessian_second = np.einsum("stam,ampq->stpq", e2, d["hessian_first"])
    rhs1 = -d["source_first"]+l1.reshape(4, 16) @ d["response"]
    k1 = rhs1 @ d["inverse_hessian"].T
    rhs2 = -source_second.copy()
    rhs2 += np.einsum("spv,tv->stp", d["response_first"].transpose(0, 2, 1), l1.reshape(4, 16))
    rhs2 += np.einsum("tpv,sv->stp", d["response_first"].transpose(0, 2, 1), l1.reshape(4, 16))
    rhs2 += l2.reshape(4, 4, 16) @ d["response"]
    rhs2 -= hessian_second @ d["k0"]
    k2 = rhs2 @ d["inverse_hessian"].T
    omega1 = np.array([normal_lorentz(second) for second in e2])+np.einsum("sp,pmab->smab", k1, cartan.OMEGA_BASIS)
    omega2 = np.array([[normal_lorentz(third) for third in row] for row in e3])+np.einsum("stp,pmab->stmab", k2, cartan.OMEGA_BASIS)
    return omega1, omega2


def evaluate_jets(prepared, jets):
    data = prepared["data"]
    psi, first, omega0 = data["psi"], data["first"], data["omega"]
    e2, p2, l1, l2, p3 = (jets[k] for k in ("e2", "p2", "l1", "l2", "p3"))
    omega1, omega2 = connection_jets(prepared, jets)
    b0, b1, b2 = (spin_lift(w) for w in (omega0, omega1, omega2))
    cov0 = first+np.einsum("mij,rj->mri", b0, psi)
    cov1 = p2+np.einsum("smij,rj->smri", b1, psi)+np.einsum("mij,srj->smri", b0, first)
    cov2 = (p3+np.einsum("stmij,rj->stmri", b2, psi)
            +np.einsum("smij,trj->stmri", b1, first)+np.einsum("tmij,srj->stmri", b1, first)
            +np.einsum("mij,strj->stmri", b0, p2))
    pair = odd.readouts.pairing
    c0 = pair(psi, cov0, Q).imag-np.eye(4)
    c1 = np.array([(pair(first[s], cov0, Q)+pair(psi, cov1[s], Q)).imag for s in range(4)])
    c2 = np.array([[(pair(p2[s, t], cov0, Q)+pair(first[s], cov1[t], Q)
                     +pair(first[t], cov1[s], Q)+pair(psi, cov2[s, t], Q)).imag-e2[s, t]
                    for t in range(4)] for s in range(4)])
    weight1 = np.einsum("sam,aij->smij", l1, Q_WEIGHTS)
    weight2 = (np.einsum("staa,mij->stmij", e2, FLAT_WEIGHTS)
               -np.einsum("stma,aij->stmij", e2, FLAT_WEIGHTS)
               +np.einsum("stam,aij->stmij", l2, Q_WEIGHTS))
    bc0 = np.array([np.kron(np.eye(3), b) for b in b0])
    bc1 = np.array([[np.kron(np.eye(3), b) for b in row] for row in b1])
    z0 = np.einsum("mmij->ij", weight1)-np.sum(bc0.conj().swapaxes(-1, -2) @ FLAT_WEIGHTS+FLAT_WEIGHTS @ bc0, axis=0)
    z1 = np.einsum("smmij->sij", weight2)-np.sum(
        bc1.conj().swapaxes(-1, -2) @ FLAT_WEIGHTS+bc0.conj().swapaxes(-1, -2) @ weight1
        +weight1 @ bc0+FLAT_WEIGHTS @ bc1, axis=1)
    pf = psi.reshape(-1)
    r0 = 1j*np.einsum("mij,mj->i", FLAT_WEIGHTS, cov0.reshape(4, 12))-prior.MASS_WEIGHT @ pf+0.5j*z0 @ pf
    r1 = (1j*np.einsum("smij,mj->si", weight1, cov0.reshape(4, 12))
          +1j*np.einsum("mij,smj->si", FLAT_WEIGHTS, cov1.reshape(4, 4, 12))
          -np.einsum("ij,sj->si", prior.MASS_WEIGHT, first.reshape(4, 12))
          +0.5j*np.einsum("sij,j->si", z1, pf)+0.5j*np.einsum("ij,sj->si", z0, first.reshape(4, 12)))
    curvature0 = cartan.curvature_upper(omega0, omega1)
    curvature1 = np.array([cartan.curvature_upper(omega0+w)-cartan.curvature_upper(omega0)
                           -cartan.curvature_upper(w)+cartan.curvature_upper(np.zeros((4, 4, 4)), dw)
                           for w, dw in zip(omega1, omega2)])
    x0 = pair(psi, cov0).imag
    x1 = np.array([(pair(first[s], cov0)+pair(psi, cov1[s])).imag for s in range(4)])
    ld0 = -np.trace(x0)-np.vdot(psi, MASS @ psi @ BETA.T).real
    ld1 = -np.trace(x1, axis1=1, axis2=2)-2*np.array([np.vdot(psi, MASS @ u @ BETA.T).real for u in first])
    fe0 = ld0*np.eye(4)+x0.T+gravity_euler(curvature0)
    fe1 = np.array([v*np.eye(4)+x.T+gravity_euler(r)+l for v, x, r, l in zip(ld1, x1, curvature1, l1)])
    vector = np.concatenate((c1.reshape(-1), fe0.reshape(-1), np.einsum("mam->a", l1),
                             prior.realify(r1), np.array([c2[p] for p in PAIR2]).reshape(-1), fe1.reshape(-1)))
    return {"vector": vector, "constraint": c0, "constraint_first": c1, "constraint_second": c2,
            "probe": r0, "probe_first": r1, "coframe_Euler": fe0, "coframe_Euler_first": fe1,
            "omega_first": omega1, "omega_second": omega2, "curvature": curvature0}


def scalar_gate(prepared, jets):
    data = prepared["data"]
    psi, first = data["psi"], data["first"]
    h = (Q @ MASS+MASS @ Q)/2
    derivative = 2*np.array([np.vdot(psi, h @ u @ BETA.T).real for u in first])
    q2 = odd.readouts.pairing(psi, data["covariant"], Q @ Q).imag
    return derivative+np.einsum("ram,am->r", jets["l1"], q2)


def fast_cartan_data(prepared, coframe, psi):
    """Same independent-source/Hessian formulas, evaluated without repeated polarization."""
    _, inverse, volume = cartan.frame_data(coframe)
    forms = prepared["component_forms"]
    source_components = np.einsum("ri,pamij,rj->pam", psi.conj(), forms, psi).real
    source = volume*np.einsum("ma,pam->p", inverse, source_components)
    response = -np.einsum("ri,pamij,rj->amp", psi.conj(), forms, Q @ psi).real.reshape(16, 24)
    hessian = volume*np.einsum("ma,nb,pqmnab->pq", inverse, inverse, prepared["curvature_hessian"])/2
    return hessian, response, source


def taylor_fields(prepared, jets, point):
    """Cubic E/Psi and quadratic multiplier fields, with the full Cartan equation eliminated."""
    x = cartan.checks._real(point, (4,), "comparison coordinate displacement")
    data = prepared["data"]
    e2, p2, l1, l2, e3, p3 = (jets[k] for k in ("e2", "p2", "l1", "l2", "e3", "p3"))
    coframe = np.eye(4)+np.einsum("r,s,rsam->am", x, x, e2)/2+np.einsum("r,s,t,rstam->am", x, x, x, e3)/6
    first_e = np.einsum("s,rsam->ram", x, e2)+np.einsum("s,t,rstam->ram", x, x, e3)/2
    second_e = e2+np.einsum("t,rstam->rsam", x, e3)
    psi = data["psi"]+np.einsum("r,rij->ij", x, data["first"])+np.einsum("r,s,rsij->ij", x, x, p2)/2+np.einsum("r,s,t,rstij->ij", x, x, x, p3)/6
    first_p = data["first"]+np.einsum("s,rsij->rij", x, p2)+np.einsum("s,t,rstij->rij", x, x, p3)/2
    multiplier = np.einsum("r,ram->am", x, l1)+np.einsum("r,s,rsam->am", x, x, l2)/2
    first_l = l1+np.einsum("s,rsam->ram", x, l2)
    bundle = dirac.bundle(coframe, first_e, second_e)
    hessian, response, source = fast_cartan_data(prepared, coframe, psi)
    coefficients = np.linalg.solve(hessian, -source+response.T @ multiplier.reshape(-1))
    omega = bundle["omega"]+cartan.unpack(coefficients)
    inverse, volume = np.linalg.inv(coframe), abs(np.linalg.det(coframe))
    inverse_first = np.array([-inverse @ d @ inverse for d in first_e])
    volume_first = volume*np.einsum("ma,ram->r", inverse, first_e)
    weights_first = (np.einsum("r,ma,aij->rmij", volume_first, inverse, FLAT_WEIGHTS)
                     +volume*np.einsum("rma,aij->rmij", inverse_first, FLAT_WEIGHTS)
                     +np.einsum("ram,aij->rmij", first_l, Q_WEIGHTS))
    connection = np.array([np.kron(np.eye(3), b) for b in spin_lift(omega)])
    operator = odd.real_law.real_operator(psi.reshape(-1), first_p.reshape(4, 12),
                                          cartan.kinetic_weights(coframe, multiplier), connection,
                                          volume*prior.MASS_WEIGHT, np.einsum("mmij->ij", weights_first))
    cross = odd.channels(psi, cartan.covariant_jet(psi, first_p, omega))["odd"]
    return {"coframe": coframe, "first_e": first_e, "second_e": second_e, "psi": psi,
            "first_p": first_p, "multiplier": multiplier, "omega": omega, "bundle": bundle,
            "cross": cross, "constraint": cross-coframe, "probe": operator,
            "Cartan_residual": hessian @ coefficients+source-response.T @ multiplier.reshape(-1),
            "weights": cartan.kinetic_weights(coframe, multiplier)}


def field_euler(prepared, jets, point, step=2e-6):
    fields = taylor_fields(prepared, jets, point)
    first = np.array([(taylor_fields(prepared, jets, point+step*u)["omega"]
                       -taylor_fields(prepared, jets, point-step*u)["omega"])/(2*step) for u in np.eye(4)])
    return cartan.coframe_euler(fields["coframe"], fields["psi"], fields["first_p"], fields["omega"],
                                cartan.curvature_upper(fields["omega"], first), MASS, fields["multiplier"])


def independent_checks(solved):
    prepared, jets = solved["prepared"], solved["jets"]
    direction = np.array([1., 0.3, -0.2, 0.1])
    direction /= np.linalg.norm(direction)
    samples = []
    for radius in (0.002, 0.001, 0.0005):
        point = radius*direction
        fields = taylor_fields(prepared, jets, point)
        samples.append({"step": radius, "constraint_norm": float(np.linalg.norm(fields["constraint"])),
                        "probe_norm": float(np.linalg.norm(fields["probe"]["symmetric"])),
                        "coframe_Euler_norm": float(np.linalg.norm(field_euler(prepared, jets, point))),
                        "Cartan_norm": float(np.linalg.norm(fields["Cartan_residual"]))})
    step = 2e-5
    origin = taylor_fields(prepared, jets, np.zeros(4))
    omega2 = np.zeros((4, 4, 4, 4, 4))
    cross1, cross2 = np.zeros((4, 4, 4)), np.zeros((4, 4, 4, 4))
    for r, s in PAIR2:
        a, b = np.eye(4)[r], np.eye(4)[s]
        if r == s:
            plus, minus = (taylor_fields(prepared, jets, sign*step*a) for sign in (1, -1))
            cross1[r] = (plus["cross"]-minus["cross"])/(2*step)
            cross2[r, r] = (plus["cross"]-2*origin["cross"]+minus["cross"])/step**2
            omega2[r, r] = (plus["omega"]-2*origin["omega"]+minus["omega"])/step**2
        else:
            corners = [taylor_fields(prepared, jets, step*(sa*a+sb*b)) for sa, sb in ((1, 1), (1, -1), (-1, 1), (-1, -1))]
            cross2[r, s] = cross2[s, r] = (corners[0]["cross"]-corners[1]["cross"]-corners[2]["cross"]+corners[3]["cross"])/(4*step**2)
            omega2[r, s] = omega2[s, r] = (corners[0]["omega"]-corners[1]["omega"]-corners[2]["omega"]+corners[3]["omega"])/(4*step**2)
    cross_bundle = dirac.bundle(origin["cross"], cross1, cross2)
    expected_bundle = origin["bundle"]
    first_step = 2e-5
    probe_first, euler_first = [], []
    for u in np.eye(4):
        plus, minus = (taylor_fields(prepared, jets, sign*first_step*u) for sign in (1, -1))
        probe_first.append((plus["probe"]["symmetric"]-minus["probe"]["symmetric"])/(2*first_step))
        euler_first.append((field_euler(prepared, jets, first_step*u)-field_euler(prepared, jets, -first_step*u))/(2*first_step))
    return {"samples_not_exact_solutions": samples,
            "second_difference_step": step,
            "connection_second_fd_error": float(np.linalg.norm(omega2-solved["result"]["omega_second"])),
            "cross_second_fd_error": float(np.linalg.norm(cross2-jets["e2"])),
            "curvature_match_fd_error": float(np.linalg.norm(cross_bundle["curvature"]["riemann"]-expected_bundle["curvature"]["riemann"])),
            "probe_first_fd_error": float(np.linalg.norm(np.array(probe_first)-solved["result"]["probe_first"])),
            "coframe_Euler_first_fd_error": float(np.linalg.norm(np.array(euler_first)-solved["result"]["coframe_Euler_first"])),
            "coframe_LC_scalar_unscaled": float(expected_bundle["curvature"]["scalar"]),
            "cross_LC_scalar_fd_unscaled": float(cross_bundle["curvature"]["scalar"])}


def temporal_ball_bound(jets):
    e2, e3 = float(np.linalg.norm(jets["e2"])), float(np.linalg.norm(jets["e3"]))
    l1, l2 = float(np.linalg.norm(jets["l1"][:, :, 0])), float(np.linalg.norm(jets["l2"][:, :, :, 0]))
    radius = 1.
    for _ in range(60):
        delta = e2*radius**2/2+e3*radius**3/6
        bound = ((1-delta)**4*(1-np.sqrt(2)*delta/(1-delta))
                 -(radius*l1+radius**2*l2/2)/np.sqrt(2)) if delta < 1 else -1.
        if delta <= 0.1 and bound > 0.25:
            return {"radius_in_arbitrary_comparison_coordinates": radius,
                    "coframe_perturbation_bound": delta, "temporal_eigenvalue_lower_bound": float(bound),
                    "not_full_constraint_hyperbolicity_or_stability": True}
        radius /= 2
    raise ValueError("No positive normal-point temporal ball resolved")


def solve(prepared=None, verbose=False):
    prepared = prepare() if prepared is None else prepared
    zero = unpack(np.zeros(1424))
    base = evaluate_jets(prepared, zero)["vector"]
    matrix = np.empty((404, 1424))
    for column in range(1424):
        value = np.zeros(1424)
        value[column] = 1
        matrix[:, column] = evaluate_jets(prepared, unpack(value))["vector"]-base
        if verbose and column % 200 == 0:
            print("prolongation column", column, flush=True)
    solution, _, rank, singular = np.linalg.lstsq(matrix, -base, rcond=1e-10)
    jets = unpack(solution)
    result = evaluate_jets(prepared, jets)
    return {"prepared": prepared, "jets": jets, "result": result, "matrix": matrix, "solution": solution,
            "base": base, "rank": int(rank), "singular_values": singular,
            "norm": float(np.linalg.norm(result["vector"])), "scalar_gate": scalar_gate(prepared, jets)}


def evaluate(solved=None):
    data, previous = load_prior()
    prepared = prepare(data) if solved is None else solved["prepared"]
    solved = solve(prepared) if solved is None else solved
    result = solved["result"]
    success = solved["norm"] < 1e-8
    return {"status": "numerically compatible next-order neutral Cartan jets; no evolved/native solution" if success
                       else "failed next-order prolongation; no compatible jet found",
            "parent_and_M_Q_c_u_unchanged": True,
            "previous_input_sha256": hashlib.sha256(Path(__file__).with_name("HC_Cartan_Compatible_Jets.json").read_bytes()).hexdigest(),
            "previous_scalar_gate": scalar_gate(prepared, previous).tolist(),
            "matrix_shape": list(solved["matrix"].shape), "matrix_rank": solved["rank"],
            "joint_residual_norm": solved["norm"],
            "constraint_first_norm": float(np.linalg.norm(result["constraint_first"])),
            "constraint_second_norm": float(np.linalg.norm(result["constraint_second"])),
            "probe_first_norm": float(np.linalg.norm(result["probe_first"])),
            "coframe_Euler_norm": float(np.linalg.norm(result["coframe_Euler"])),
            "coframe_Euler_first_norm": float(np.linalg.norm(result["coframe_Euler_first"])),
            "point_probe_norm": float(np.linalg.norm(result["probe"])),
            "point_constraint_norm": float(np.linalg.norm(result["constraint"])),
            "new_scalar_gate": solved["scalar_gate"].tolist(),
            "prolonged_equations_numerically_satisfied": success,
            "second_order_cross_curvature_matching_at_origin_only": success,
            "positive_temporal_ball": temporal_ball_bound(solved["jets"]),
            "independent_checks": independent_checks(solved),
            "jet_coordinate_blocks": {"e2": [0, 160], "psi2_real_then_imag": [160, 400], "lambda1": [400, 464],
                                      "lambda2": [464, 624], "e3": [624, 944], "psi3_real_then_imag": [944, 1424]},
            "jet_coordinates": solved["solution"].tolist(),
            "remaining": ["third constraint derivatives and second probe/coframe derivatives", "formal integrability and full Cauchy-surface data/propagation",
                          "interval certification, actual local/global evolution and native action/gauge/HC/C7/scale identification"],
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
