"""Analytic C3 and bounded affine re-preparation with the spinor Hessian fixed.

Only the added neutral Cartan comparison is considered, not native identification.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "reprepare_third_diagnostic", Path(__file__).with_name("HC_Cartan_Third_Constraint_Diagnostic.py"))
diagnostic = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(diagnostic)
scalar = diagnostic.scalar
regular, spatial, prolong, prior, cartan = scalar.regular, scalar.spatial, scalar.prolong, scalar.prior, scalar.cartan
TRIPLES = diagnostic.TRIPLES


def cyclic_one_two(value):
    return value+value.swapaxes(0, 1)+value.swapaxes(0, 2)


def bilinear_third(forms, psi, p1, p2, p3, left_operator=None):
    left0, left1 = psi, p1
    if left_operator is not None:
        left0 = left_operator @ psi
        left1 = np.einsum("uv,rvj->ruj", left_operator, p1)
    result = 2*np.einsum("ui,...ij,rstuj->rst...", left0.conj(), forms, p3).real
    cross = 2*np.einsum("rui,...ij,stuj->rst...", left1.conj(), forms, p2).real
    return result+cyclic_one_two(cross)


def lc_cubic(prepared, point):
    """Third LC derivative for E4=0, E1=0; independent of E3."""
    e2, eta = point["coframe_second"], prolong.ETA
    w1 = np.array([prolong.normal_lorentz(e2[r]) for r in range(4)])
    g4 = np.empty((4,)*6)
    for r, s, t, u in np.ndindex((4,)*4):
        g4[r, s, t, u] = sum(
            e2[a, b].T @ eta @ e2[c, d]+e2[c, d].T @ eta @ e2[a, b]
            for a, b, c, d in ((r, s, t, u), (r, t, s, u), (r, u, s, t)))
    result = np.empty((4,)*6)
    for r, s, t, mu in np.ndindex((4,)*4):
        result[r, s, t, mu] = np.array([
            [(g4[r, s, t, mu, a, b]+g4[r, s, t, b, a, mu]
              -g4[r, s, t, a, mu, b])/2 for b in range(4)] for a in range(4)])
        for a, b, c in ((r, s, t), (r, t, s), (s, t, r)):
            result[r, s, t, mu] -= (e2[a, b].T @ (w1[c, mu]+eta @ e2[c, mu])
                                         +w1[c, mu] @ e2[a, b])
    return result


def connection_third(prepared, point, jets, lc_third):
    psi, p1, p2, p3 = prepared["data"]["psi"], point["psi_first"], jets["p2"], jets["p3"]
    e2, e3 = point["coframe_second"], jets["e3"]
    l0, l1, l2 = point["multiplier"], point["multiplier_first"], jets["l2"]
    old = regular.connection_second(prepared, point, jets)
    source3 = bilinear_third(prepared["source_forms"], psi, p1, p2, p3)
    component_first = 2*np.einsum("ui,pamij,ruj->rpam", psi.conj(), prepared["component_forms"], p1).real
    source1 = np.einsum("rpaa->rp", component_first)
    source3 += (np.einsum("rstaa,p->rstp", e3, prepared["source"])
                -np.einsum("rstma,pam->rstp", e3, prepared["source_components"]))
    geometric_cross = (np.einsum("staa,rp->rstp", e2, source1)
                       -np.einsum("stma,rpam->rstp", e2, component_first))
    source3 += cyclic_one_two(geometric_cross)
    response3 = -bilinear_third(prepared["component_forms"], psi, p1, p2, p3, scalar.Q)
    response1 = -2*np.einsum("ui,pamij,ruj->ramp", (scalar.Q @ psi).conj(), prepared["component_forms"], p1).real
    # bilinear_third keeps the form index p first; the Cartan response uses it last.
    response3 = np.moveaxis(response3, 3, -1)
    h2 = old["hessian_second"]
    h3 = np.einsum("rstam,ampq->rstpq", e3, prepared["hessian_first"])
    k0 = cartan.pack(old["omega"])
    lc1 = (e2.reshape(4, 64) @ regular.LC_LINEAR).reshape(4, 4, 4, 4)
    k1 = np.array([cartan.pack(w) for w in old["first"]-lc1])
    rhs = -source3+np.einsum("rstamp,am->rstp", response3, l0)-h3 @ k0
    cross = (np.einsum("stamp,ram->rstp", old["response_second"], l1)
             +np.einsum("ramp,stam->rstp", response1, l2)
             -np.einsum("stpq,rq->rstp", h2, k1))
    rhs += cyclic_one_two(cross)
    k3 = rhs @ prepared["inverse_hessian"].T
    omega3 = lc_third+np.einsum("rstp,pmab->rstmab", k3, cartan.OMEGA_BASIS)
    return dict(old, third=omega3, source_third=source3, response_third=response3,
                hessian_third=h3, k_third=k3, rhs_third=rhs)


def constraint_third(prepared, point, jets, lc_third):
    connection = connection_third(prepared, point, jets, lc_third)
    b0, b1, b2, b3 = [prolong.spin_lift(connection[k]) for k in ("omega", "first", "second", "third")]
    psi, p1, p2, p3 = prepared["data"]["psi"], point["psi_first"], jets["p2"], jets["p3"]
    d0, d1, d2 = scalar.covariant_jets(prepared, point, jets)
    pair = scalar.odd.readouts.pairing
    result = []
    for r, s, t in TRIPLES:
        d3 = (np.einsum("mij,uj->mui", b3[r, s, t], psi)
              +np.einsum("mij,uj->mui", b0, p3[r, s, t]))
        for i, j, k in ((r, s, t), (s, r, t), (t, r, s)):
            d3 += (np.einsum("mij,uj->mui", b1[i], p2[j, k])
                   +np.einsum("mij,uj->mui", b2[j, k], p1[i]))
        value = pair(p3[r, s, t], d0, scalar.Q)+pair(psi, d3, scalar.Q)
        for i, j, k in ((r, s, t), (s, r, t), (t, r, s)):
            value += pair(p1[i], d2[j, k], scalar.Q)+pair(p2[j, k], d1[i], scalar.Q)
        result.append(value.imag-jets["e3"][r, s, t])
    return np.asarray(result)


def coordinates(jets):
    return np.concatenate((prior.realify(np.array([jets["p2"][p] for p in prior.PAIR2])),
                           np.array([jets["l2"][p] for p in prior.PAIR2]).reshape(-1),
                           np.array([jets["e3"][p] for p in TRIPLES]).reshape(-1),
                           prior.realify(np.array([jets["p3"][p] for p in TRIPLES]))))


def new_jet_maps(prepared):
    symmetric = np.zeros((320, 140))
    for q, rows in enumerate(diagnostic.groups()):
        for a in range(4):
            for t, mu in rows:
                symmetric[(t*4+a)*4+mu, q*4+a] = 1
    connection = []
    for i in range(880):
        v = np.zeros(880)
        v[i] = 1
        connection.append(diagnostic.connection_image(prepared, v[:560].reshape(35, 4, 4),
                                                       v[560:].reshape(20, 4, 4)).reshape(-1))
    connection = np.column_stack(connection)
    full = np.column_stack((symmetric, connection))
    u, singular, _ = np.linalg.svd(full, full_matrices=False)
    rank = int(np.sum(singular > singular[0]*1e-10))
    return {"full": full, "connection": connection, "symmetric": symmetric,
            "cokernel": u[:, rank:], "rank": rank, "singular_values": singular}


def old_equations(prepared, point, jets):
    old = regular.equations(prepared, point, jets)["vector"]
    hessian = scalar.scalar_jet(prepared, point, jets)["hessian"]
    return np.concatenate((old, np.array([hessian[p] for p in prior.PAIR2])))


def affine_reprepare(prepared, point, saved, lc_third, maps):
    """Keep psi2 fixed while varying the remaining 960 older coordinates."""
    fixed = coordinates(saved)
    def image(delta):
        jets = regular.unpack(fixed+np.concatenate((np.zeros(240), delta)))
        source = constraint_third(prepared, point, jets, lc_third)
        return np.concatenate((old_equations(prepared, point, jets), maps["cokernel"].T @ source.reshape(-1)))
    base = image(np.zeros(960))
    columns = []
    for i in range(960):
        delta = np.zeros(960)
        delta[i] = 1
        columns.append(image(delta)-base)
    matrix = np.column_stack(columns)
    delta, _, rank, singular = np.linalg.lstsq(matrix, -base, rcond=1e-10)
    updated = fixed+np.concatenate((np.zeros(240), delta))
    rng = np.random.default_rng(39445)
    random = rng.normal(size=960)*.3
    affine_error = np.linalg.norm(image(random)-base-matrix @ random)
    return {"matrix": matrix, "base": base, "delta": delta, "coordinates": updated,
            "rank": int(rank), "singular_values": singular,
            "residual": image(delta), "affine_error": float(affine_error)}


def finish_c3(prepared, point, jets, lc_third, maps):
    source = constraint_third(prepared, point, jets, lc_third)
    quotient = np.column_stack([diagnostic.project(c.reshape(20, 4, 4))[1].reshape(-1)
                                for c in maps["connection"].T])
    conn, _, rank, _ = np.linalg.lstsq(quotient, -diagnostic.project(source)[1].reshape(-1), rcond=1e-10)
    principal = spatial.constraint_principal_map(prepared["data"]["psi"])
    remainder = source+(maps["connection"] @ conn).reshape(20, 4, 4)
    p4, residual = diagnostic.spinor_only_completion(remainder, principal)
    return {"source": source, "connection_coordinates": conn, "fourth_spinor_real": p4,
            "residual": residual, "connection_quotient_rank": int(rank)}


def evaluate():
    prepared, point, saved, fingerprint = diagnostic.load_data()
    lc_third = lc_cubic(prepared, point)
    maps = new_jet_maps(prepared)
    old_c3 = constraint_third(prepared, point, saved, lc_third)
    frozen = json.loads(Path(__file__).with_name("HC_Cartan_Third_Constraint_Diagnostic.json").read_text(encoding="utf-8"))
    solved = affine_reprepare(prepared, point, saved, lc_third, maps)
    jets = regular.unpack(solved["coordinates"])
    finished = finish_c3(prepared, point, jets, lc_third, maps)
    prior_summary = scalar.residual_summary(prepared, point, solved["coordinates"])
    combined = np.concatenate((np.array(prior_summary["full_394_residual"]), finished["residual"].reshape(-1)))
    return {
        "scope": "Affine C3 reprepare in added neutral model, psi2 fixed. R2 and FE2 NOT imposed.",
        "input_scalar_completion_sha256": fingerprint,
        "fixed_inputs": "All lower point data, Q, M, Einstein coefficient, vacuum and saved psi2",
        "changed_older_jets": ["lambda2", "E3", "psi3"],
        "highest_map": {"shape": list(maps["full"].shape), "rank": maps["rank"],
                        "cokernel_shape": list(maps["cokernel"].shape),
                        "cokernel_map_annihilation_norm": float(np.linalg.norm(maps["cokernel"].T @ maps["full"])),
                        "cokernel_orthonormality_norm": float(np.linalg.norm(maps["cokernel"].T @ maps["cokernel"]-np.eye(45))),
                        "singular_values": maps["singular_values"].tolist()},
        "analytic_frozen_C3": old_c3.tolist(),
        "analytic_versus_prior_FD_C3_norm": float(np.linalg.norm(old_c3-np.array(frozen["frozen_source"]))),
        "frozen_unreachable_C3_norm": float(np.linalg.norm(maps["cokernel"].T @ old_c3.reshape(-1))),
        "affine_439_system": {"shape": list(solved["matrix"].shape), "rank": solved["rank"],
                              "singular_values": solved["singular_values"].tolist(),
                              "old_394_matrix_rank": int(np.linalg.matrix_rank(solved["matrix"][:394], tol=1e-8)),
                              "random_affine_error_norm": solved["affine_error"],
                              "residual_norm": float(np.linalg.norm(solved["residual"])),
                              "residual": solved["residual"].tolist(),
                              "older_coordinate_change_norm": float(np.linalg.norm(solved["delta"])),
                              "jet_coordinates": solved["coordinates"].tolist()},
        "old_394_rechecked": prior_summary,
        "new_jet_completion": {"connection_coordinates": finished["connection_coordinates"].tolist(),
                               "fourth_spinor_real": finished["fourth_spinor_real"].tolist(),
                               "full_C3_residual_norm": float(np.linalg.norm(finished["residual"])),
                               "full_C3_residual": finished["residual"].tolist()},
        "all_714_residual_norm": float(np.linalg.norm(combined)),
        "all_714_max_abs": float(np.max(abs(combined))),
        "limitations": ["R2 and FE2 remain unsolved", "No propagation or local existence",
                        "Numerical ranks are not exact symbolic certificates",
                        "No native action, frame or physical scale identification"],
        "main_TeX_PDF_changed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = evaluate()
    encoded = json.dumps(result, indent=2, allow_nan=False)+"\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded)
    print(json.dumps({k: result[k] for k in ("frozen_unreachable_C3_norm", "all_714_residual_norm", "all_714_max_abs")}))


if __name__ == "__main__":
    main()
