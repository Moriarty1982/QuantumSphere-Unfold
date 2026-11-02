"""Differentiated gravity and second constraints on the regular neutral Cartan branch.

Finite pointwise completion, not a full evolution or native-gravity theorem.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "cartan_regular_spatial", Path(__file__).with_name("HC_Cartan_Spatial_Propagation.py"))
spatial = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(spatial)
prolong, prior, cartan, odd = spatial.prolong, spatial.prior, spatial.cartan, spatial.odd
Q, ETA, MASS, BETA = spatial.Q, prior.ETA, prior.MASS, prior.BETA
LC_LINEAR = np.array([prolong.normal_lorentz(v) for v in np.eye(64).reshape(64, 4, 4, 4)]).reshape(64, 64)


def load_data():
    prepared, old_point = spatial.load_point()
    payload = json.loads(Path(__file__).with_name("HC_Cartan_Spatial_Propagation.json").read_text(encoding="utf-8"))
    saved = payload["reprepared_first_jet"]
    point = spatial.point_fields(old_point["multiplier"], np.array(saved["point_coordinates"]))
    x = np.array(saved["higher_coordinates"])
    return prepared, point, {"p2": prior.unpack_second(x[:240], True),
                              "l2": prior.unpack_second(x[240:]),
                              "e3": prolong.unpack_third(np.zeros(320)),
                              "p3": prolong.unpack_third(np.zeros(480), True)}


def unpack(x):
    x = cartan.checks._real(x, (1200,), "1200 real regular-branch higher-jet coordinates")
    return {"p2": prior.unpack_second(x[:240], True), "l2": prior.unpack_second(x[240:400]),
            "e3": prolong.unpack_third(x[400:720]), "p3": prolong.unpack_third(x[720:], True)}


def connection_second(prepared, point, jets, first_connection=None):
    """Differentiate H k=-s+L.T lambda twice, keeping the nonzero lambda value."""
    psi, p1 = prepared["data"]["psi"], point["psi_first"]
    e2, l0, l1 = point["coframe_second"], point["multiplier"], point["multiplier_first"]
    p2, l2 = jets["p2"], jets["l2"]
    omega0, omega1 = spatial.connection_first(prepared, point) if first_connection is None else first_connection
    k0 = cartan.pack(omega0)
    source_second = (2*np.einsum("ri,pij,strj->stp", psi.conj(), prepared["source_forms"], p2).real
                     +2*np.einsum("sri,pij,trj->stp", p1.conj(), prepared["source_forms"], p1).real
                     +np.einsum("staa,p->stp", e2, prepared["source"])
                     -np.einsum("stma,pam->stp", e2, prepared["source_components"]))
    response_first = -2*np.einsum("ri,pamij,srj->samp", (Q @ psi).conj(), prepared["component_forms"], p1).real
    response_second = (-2*np.einsum("ri,pamij,strj->stamp", (Q @ psi).conj(), prepared["component_forms"], p2).real
                       -2*np.einsum("sri,pamij,trj->stamp", np.einsum("uv,svi->sui", Q, p1).conj(),
                                     prepared["component_forms"], p1).real)
    hessian_second = np.einsum("stam,ampq->stpq", e2, prepared["hessian_first"])
    lambda_value_reaction = np.einsum("stamp,am->stp", response_second, l0)
    rhs = (-source_second+lambda_value_reaction
           +np.einsum("samp,tam->stp", response_first, l1)
           +np.einsum("tamp,sam->stp", response_first, l1)
           +l2.reshape(4, 4, 16) @ prepared["response"]-hessian_second @ k0)
    k2 = rhs @ prepared["inverse_hessian"].T
    omega2 = ((jets["e3"].reshape(16, 64) @ LC_LINEAR).reshape(4, 4, 4, 4, 4)
              +np.einsum("stp,pmab->stmab", k2, cartan.OMEGA_BASIS))
    return {"omega": omega0, "first": omega1, "second": omega2,
            "response_second": response_second, "source_second": source_second,
            "hessian_second": hessian_second, "lambda_value_reaction": lambda_value_reaction,
            "k_second": k2, "rhs": rhs}


def equations(prepared, point, jets, first_connection=None):
    psi, p1, e2, l1 = (prepared["data"]["psi"], point["psi_first"],
                       point["coframe_second"], point["multiplier_first"])
    connection = connection_second(prepared, point, jets, first_connection)
    omega0, omega1, omega2 = (connection[k] for k in ("omega", "first", "second"))
    b0, b1, b2 = (prolong.spin_lift(w) for w in (omega0, omega1, omega2))
    cov0 = cartan.covariant_jet(psi, p1, omega0)
    cov1 = jets["p2"]+np.einsum("smij,rj->smri", b1, psi)+np.einsum("mij,srj->smri", b0, p1)
    cov2 = (jets["p3"]+np.einsum("stmij,rj->stmri", b2, psi)
            +np.einsum("smij,trj->stmri", b1, p1)+np.einsum("tmij,srj->stmri", b1, p1)
            +np.einsum("mij,strj->stmri", b0, jets["p2"]))
    pair = odd.readouts.pairing
    c1 = np.array([(pair(p1[r], cov0, Q)+pair(psi, cov1[r], Q)).imag for r in range(4)])
    c2 = np.array([[(pair(jets["p2"][r, s], cov0, Q)+pair(p1[r], cov1[s], Q)
                     +pair(p1[s], cov1[r], Q)+pair(psi, cov2[r, s], Q)).imag-e2[r, s]
                    for s in range(4)] for r in range(4)])
    curvature0 = cartan.curvature_upper(omega0, omega1)
    curvature1 = np.array([cartan.curvature_upper(omega0+w)-cartan.curvature_upper(omega0)
                           -cartan.curvature_upper(w)+cartan.curvature_upper(np.zeros((4, 4, 4)), dw)
                           for w, dw in zip(omega1, omega2)])
    x1 = np.array([(pair(p1[r], cov0)+pair(psi, cov1[r])).imag for r in range(4)])
    ld1 = -np.trace(x1, axis1=1, axis2=2)-2*np.array([np.vdot(psi, MASS @ u @ BETA.T).real for u in p1])
    fe1 = np.array([v*np.eye(4)+x.T+prolong.gravity_euler(r)+l for v, x, r, l in zip(ld1, x1, curvature1, l1)])
    probe1 = spatial.first_probe(prepared, point, jets["p2"], jets["l2"], (omega0, omega1))
    vector = np.concatenate((c1.reshape(-1), prior.realify(probe1), fe1.reshape(-1),
                             np.array([c2[p] for p in prior.PAIR2]).reshape(-1)))
    return {"vector": vector, "constraint_first": c1, "probe_first": probe1,
            "coframe_Euler_first": fe1, "constraint_second": c2,
            "curvature": curvature0, "curvature_first": curvature1, "connection": connection}


def solve(prepared, point):
    first_connection = spatial.connection_first(prepared, point)

    def image(x):
        return equations(prepared, point, unpack(x), first_connection)["vector"]

    solved = spatial.affine_system(image, 1200)
    jets = unpack(solved["solution"])
    return dict(solved, jets=jets, result=equations(prepared, point, jets))


def frozen_completion(prepared, point, previous, joint):
    second = np.concatenate((prior.realify(np.array([previous["p2"][p] for p in prior.PAIR2])),
                             np.array([previous["l2"][p] for p in prior.PAIR2]).reshape(-1)))
    matrix = joint["matrix"][:, 400:]
    base = joint["base"]+joint["matrix"][:, :400] @ second
    x, _, rank, singular = np.linalg.lstsq(matrix, -base, rcond=1e-10)
    jets = dict(previous, e3=prolong.unpack_third(x[:320]), p3=prolong.unpack_third(x[320:], True))
    return {"matrix": matrix, "base": base, "solution": x, "rank": int(rank),
            "singular_values": singular, "residual": equations(prepared, point, jets)["vector"], "jets": jets}


def coframe_normal_gauge_basis():
    """Ten leading normal gauge directions: four coordinate and six Lorentz generators."""
    directions = []
    for a in range(4):
        e = np.zeros((4, 4))
        e[a, 0] = 1
        directions.append(e)
    for a, b in cartan.PAIRS:
        lower = np.zeros((4, 4))
        lower[a, b], lower[b, a] = 1, -1
        directions.append(ETA @ lower)
    result = np.zeros((56, 10))
    result[:16] = np.array(directions).reshape(10, 16).T
    return result


def noether_dependencies(prepared, point):
    """24 curl, 24 differentiated Lorentz and four diffeomorphism row identities."""
    rows = np.zeros((52, 384))
    for g, (r, s) in enumerate(cartan.PAIRS):
        for a in range(4):
            rows[4*g+a, 16*r+4*a+s] = 1
            rows[4*g+a, 16*s+4*a+r] = -1
    generators = coframe_normal_gauge_basis()[:16, 4:].T.reshape(6, 4, 4)
    lower = np.einsum("ab,gbc->gac", ETA, generators)
    spin = -np.einsum("gab,aij,bjk->gik", lower, cartan.GAMMA, cartan.GAMMA)/4
    variations = np.einsum("gij,rj->gri", spin, prepared["data"]["psi"]).reshape(6, 12)
    for r in range(4):
        for g, generator in enumerate(generators):
            row = rows[24+6*r+g]
            row[16*r:16*(r+1)] = (generator.T @ point["multiplier"]).reshape(-1)
            row[64+12*r:64+12*(r+1)] = 2*variations[g].real
            row[112+12*r:112+12*(r+1)] = 2*variations[g].imag
            row[160+16*r:160+16*(r+1)] = generator.reshape(-1)
    for nu in range(4):
        row = rows[48+nu]
        for a, mu in np.ndindex((4, 4)):
            row[16*mu+4*a+nu] += point["multiplier"][a, mu]
            row[16*nu+4*a+mu] -= point["multiplier"][a, mu]
        for mu in range(4):
            row[160+16*mu+4*nu+mu] += 1
    return rows


def taylor_fields(prepared, point, jets, displacement):
    completion = {"psi_second": jets["p2"], "multiplier_second": jets["l2"],
                  "coframe_third": jets["e3"], "psi_third": jets["p3"]}
    return spatial.taylor_fields(prepared, point, completion, displacement)


def field_euler(prepared, point, jets, displacement, step=2e-6):
    fields = taylor_fields(prepared, point, jets, displacement)
    first = np.array([(taylor_fields(prepared, point, jets, displacement+step*u)["omega"]
                       -taylor_fields(prepared, point, jets, displacement-step*u)["omega"])/(2*step)
                      for u in np.eye(4)])
    return cartan.coframe_euler(fields["coframe"], fields["psi"], fields["psi_first"], fields["omega"],
                                cartan.curvature_upper(fields["omega"], first), MASS, fields["multiplier"])


def independent_checks(prepared, point, jets, step=2e-5):
    origin = taylor_fields(prepared, point, jets, np.zeros(4))
    connection2 = np.zeros((4, 4, 4, 4, 4))
    constraint2 = np.zeros((4, 4, 4, 4))
    cross_first = np.zeros((4, 4, 4))
    for r, s in prior.PAIR2:
        a, b = np.eye(4)[r], np.eye(4)[s]
        if r == s:
            plus, minus = (taylor_fields(prepared, point, jets, sign*step*a) for sign in (1, -1))
            connection2[r, r] = (plus["omega"]-2*origin["omega"]+minus["omega"])/step**2
            constraint2[r, r] = (plus["constraint"]-2*origin["constraint"]+minus["constraint"])/step**2
            cross_first[r] = (plus["constraint"]+plus["coframe"]-minus["constraint"]-minus["coframe"])/(2*step)
        else:
            corners = [taylor_fields(prepared, point, jets, step*(sa*a+sb*b)) for sa, sb in ((1, 1), (1, -1), (-1, 1), (-1, -1))]
            connection2[r, s] = connection2[s, r] = (corners[0]["omega"]-corners[1]["omega"]-corners[2]["omega"]+corners[3]["omega"])/(4*step**2)
            constraint2[r, s] = constraint2[s, r] = (corners[0]["constraint"]-corners[1]["constraint"]-corners[2]["constraint"]+corners[3]["constraint"])/(4*step**2)
    fe1 = np.array([(field_euler(prepared, point, jets, step*u)-field_euler(prepared, point, jets, -step*u))/(2*step)
                    for u in np.eye(4)])
    analytic = equations(prepared, point, jets)
    analytic_cross = prolong.dirac.bundle(origin["coframe"]+origin["constraint"],
                                         analytic["constraint_first"],
                                         point["coframe_second"]+analytic["constraint_second"])
    difference_cross = prolong.dirac.bundle(origin["coframe"]+origin["constraint"], cross_first,
                                           point["coframe_second"]+constraint2)
    reference = origin["bundle"]["curvature"]
    direction = np.array([1., .3, -.2, .1])
    direction /= np.linalg.norm(direction)
    samples = []
    for radius in (.002, .001, .0005):
        fields = taylor_fields(prepared, point, jets, radius*direction)
        samples.append({"radius": radius, "constraint_norm": float(np.linalg.norm(fields["constraint"])),
                        "probe_norm": float(np.linalg.norm(fields["probe"])),
                        "coframe_Euler_norm": float(np.linalg.norm(field_euler(prepared, point, jets, radius*direction))),
                        "Cartan_norm": float(np.linalg.norm(fields["Cartan"]))})
    return {"step": step, "connection_second_fd_error": float(np.linalg.norm(connection2-analytic["connection"]["second"])),
            "constraint_second_fd_error": float(np.linalg.norm(constraint2-analytic["constraint_second"])),
            "coframe_Euler_first_fd_error": float(np.linalg.norm(fe1-analytic["coframe_Euler_first"])),
            "analytic_cross_E_curvature_match_error": float(np.linalg.norm(analytic_cross["curvature"]["riemann"]-reference["riemann"])),
            "difference_cross_E_curvature_match_error": float(np.linalg.norm(difference_cross["curvature"]["riemann"]-reference["riemann"])),
            "coframe_LC_scalar_unscaled": float(reference["scalar"]),
            "samples_not_evolved_solutions": samples}


def evaluate():
    prepared, point, previous = load_data()
    solved = solve(prepared, point)
    frozen = frozen_completion(prepared, point, previous, solved)
    normal = spatial.normal_curl_system(prepared, point)
    result = solved["result"]
    dependencies = noether_dependencies(prepared, point)
    return {"status": "regular-branch finite gravitational prolongation; no full evolution or native theorem",
            "previous_input_sha256": hashlib.sha256(Path(__file__).with_name("HC_Cartan_Spatial_Propagation.json").read_bytes()).hexdigest(),
            "frozen_second_jet_attempt": {"shape": list(frozen["matrix"].shape), "rank": frozen["rank"],
                                          "residual_norm": float(np.linalg.norm(frozen["residual"]))},
            "joint_completion": {"shape": list(solved["matrix"].shape), "rank": solved["rank"],
                                  "residual_norm": float(np.linalg.norm(solved["residual"])),
                                  "constraint_first_norm": float(np.linalg.norm(result["constraint_first"])),
                                  "probe_first_norm": float(np.linalg.norm(result["probe_first"])),
                                  "coframe_Euler_first_norm": float(np.linalg.norm(result["coframe_Euler_first"])),
                                  "constraint_second_norm": float(np.linalg.norm(result["constraint_second"])),
                                  "jet_coordinates": solved["solution"].tolist()},
            "normal_gauge_basis_rank": int(np.linalg.matrix_rank(coframe_normal_gauge_basis())),
            "normal_gauge_annihilation_norm": float(np.linalg.norm(normal["matrix"] @ coframe_normal_gauge_basis())),
            "remaining_normal_kernel_dimension": normal["remaining_kernel"].shape[1],
            "normal_quotient_after_ten_leading_gauge_directions": normal["remaining_kernel"].shape[1]-10,
            "remaining_spatial_multiplier_velocity_projection_rank": normal["remaining_spatial_multiplier_rank"],
            "derived_row_identities_rank": int(np.linalg.matrix_rank(dependencies, tol=1e-10)),
            "derived_row_identities_matrix_error": float(np.linalg.norm(dependencies @ solved["matrix"])),
            "derived_row_identities_rhs_error": float(np.linalg.norm(dependencies @ solved["base"])),
            "independent_checks": independent_checks(prepared, point, solved["jets"]),
            "remaining": ["third coframe constraints and second probe/gravitational equations",
                          "closure of the remaining multiplier/gauge constraint hierarchy and constant-rank control",
                          "surface data, propagation, existence, native action/HC/C7 and physical normalization"],
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
