"""First-order odd-cross parent: independent connection, constraint and coframe variations.

Conditional neutral Einstein-Cartan comparison, not a native action or full field solution.
"""
import argparse
import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "cross_cartan_odd", Path(__file__).with_name("HC_Antisymmetric_Cross_Geometry.py"))
odd = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(odd)
dirac, checks = odd.dirac, odd.checks
ETA, GAMMA, WEIGHTS, BETA = odd.ETA, dirac.GAMMA, odd.WEIGHTS, odd.BETA
PAIRS = tuple(itertools.combinations(range(4), 2))
OMEGA_BASIS = np.zeros((24, 4, 4, 4))
for mu, (a, b) in itertools.product(range(4), PAIRS):
    index = 6*mu+PAIRS.index((a, b))
    OMEGA_BASIS[index, mu, a, b] = 1
    OMEGA_BASIS[index, mu, b, a] = -1
SPIN_BASIS = -np.einsum("pmab,aij,bjk->pmik", OMEGA_BASIS, GAMMA, GAMMA)/4
GAMMA5 = 1j*GAMMA[0] @ GAMMA[1] @ GAMMA[2] @ GAMMA[3]


def frame_data(coframe):
    e = checks._real(coframe, (4, 4), "invertible real coframe")
    if np.linalg.slogdet(e)[0] == 0:
        raise ValueError("Nondegenerate coframe required")
    return e, np.linalg.inv(e), float(abs(np.linalg.det(e)))


def unpack(coefficients):
    k = checks._real(coefficients, (24,), "24 real lower Lorentz connection coefficients")
    return np.einsum("p,pmab->mab", k, OMEGA_BASIS)


def pack(omega):
    omega = checks._real(omega, (4, 4, 4), "lower Lorentz connection")
    if not np.allclose(omega, -omega.swapaxes(1, 2), atol=1e-10, rtol=1e-10):
        raise ValueError("Lorentz connection must be antisymmetric in its lowered frame indices")
    return np.array([omega[mu, a, b] for mu in range(4) for a, b in PAIRS])


def spin_connection(omega):
    return -np.einsum("mab,aij,bjk->mik", omega, GAMMA, GAMMA)/4


def curvature_upper(omega, first=None):
    """R_mu,nu^{a,b}; first[r,mu,a,b] differentiates the lower connection."""
    omega = unpack(pack(omega))
    mixed = np.einsum("ab,mbc->mac", ETA, omega)
    result = np.array([[(a @ b-b @ a) @ ETA for b in mixed] for a in mixed])
    if first is not None:
        first = checks._real(first, (4, 4, 4, 4), "connection first jet")
        result += np.einsum("ab,mnbc,cd->mnad", ETA, first-first.swapaxes(0, 1), ETA)
    return result


def palatini_density(coframe, curvature, coefficient=1., vacuum=0.):
    _, inverse, volume = frame_data(coframe)
    curvature = checks._real(curvature, (4, 4, 4, 4), "upper Lorentz curvature")
    coefficient, vacuum = checks._scalar(coefficient, "Einstein coefficient"), checks._scalar(vacuum, "vacuum density")
    scalar = np.einsum("ma,nb,mnab", inverse, inverse, curvature)
    return float(volume*(coefficient*scalar/2-vacuum))


def contorsion_hessian(coframe, coefficient=1.):
    """Bulk EH Hessian in omega=omega_LC(E)+k, modulo the boundary divergence."""
    coefficient = checks._scalar(coefficient, "nonzero Einstein coefficient")
    if coefficient == 0:
        raise ValueError("Nonzero Einstein coefficient required")

    def quadratic(k):
        return palatini_density(coframe, curvature_upper(unpack(k)), coefficient)

    basis = np.eye(24)
    diagonal = np.array([quadratic(e) for e in basis])
    result = np.diag(2*diagonal)
    for r, s in itertools.combinations(range(24), 2):
        result[r, s] = result[s, r] = quadratic(basis[r]+basis[s])-diagonal[r]-diagonal[s]
    return result


def covariant_jet(psi, first, omega):
    return first+np.einsum("mij,rj->mri", spin_connection(omega), psi)


def spin_maps(coframe, psi, q=odd.Q_PHASE):
    """C=C_partial+L omega; s0 is the independent Dirac connection derivative."""
    _, inverse, volume = frame_data(coframe)
    psi = checks._finite(psi, "three-channel probe")
    q = checks._finite(q, "Hermitian readout weight")
    if psi.shape != (3, 4) or q.shape != (3, 3) or not np.allclose(q, q.conj().T):
        raise ValueError("Three spinor channels and a Hermitian selector required")
    response = np.empty((16, 24))
    source = np.zeros(24)
    for p, spin in enumerate(SPIN_BASIS):
        dpsi = np.einsum("mij,rj->mri", spin, psi)
        qpair = odd.readouts.pairing(psi, dpsi, q).imag
        response[:, p] = qpair.reshape(-1)
        source[p] = -volume*np.sum(inverse.T*odd.readouts.pairing(psi, dpsi).imag)
    return response, source


def axial_currents(psi, q=odd.Q_PHASE):
    def current(weight):
        return np.array([np.vdot(psi, weight @ psi @ (k @ GAMMA5).T).real for k in WEIGHTS])
    return current(np.eye(3)), current(q)


def dirac_drive_formula(coframe, psi):
    """Exact L H_1^{-1} s0 in coordinate coframe indices, from the axial Clifford contraction."""
    e, _, _ = frame_data(coframe)
    a, aq = axial_currents(psi)
    return -(float(aq @ ETA @ a)*np.eye(4)-np.outer(a, ETA @ aq)) @ e/8


def canonical_spacelike_schur(weighted_axial_component):
    """Exact S for E=I, c=1 and A_Q=(0,0,0,a); rows/columns use flattened [a,mu]."""
    a = checks._scalar(weighted_axial_component, "spacelike axial component")

    def image(l):
        return a*a/8*np.array([
            [-l[0, 0]+l[1, 1]+l[2, 2], l[0, 1]-l[1, 0], l[0, 2]-l[2, 0], l[0, 3]],
            [-l[0, 1]+l[1, 0], l[0, 0]-l[1, 1]+l[2, 2], -l[1, 2]-l[2, 1], -l[1, 3]],
            [-l[0, 2]+l[2, 0], -l[1, 2]-l[2, 1], l[0, 0]+l[1, 1]-l[2, 2], -l[2, 3]],
            [0, 0, 0, 0]])
    return np.column_stack([image(e.reshape(4, 4)).reshape(-1) for e in np.eye(16)])


def kinetic_weights(coframe, multiplier):
    _, inverse, volume = frame_data(coframe)
    multiplier = checks._real(multiplier, (4, 4), "real multiplier density")
    coordinate = np.einsum("ma,aij->mij", inverse, WEIGHTS)
    return np.array([volume*np.kron(np.eye(3), coordinate[mu])
                     +np.kron(odd.Q_PHASE, np.einsum("a,aij->ij", multiplier[:, mu], WEIGHTS))
                     for mu in range(4)])


def matter_density(coframe, psi, first, omega, mass):
    _, inverse, volume = frame_data(coframe)
    covariant = covariant_jet(psi, first, omega)
    kinetic = -np.sum(inverse.T*odd.readouts.pairing(psi, covariant).imag)
    return float(volume*(kinetic-np.vdot(psi, mass @ psi @ BETA.T).real))


def direct_parent_density(coframe, psi, first, omega, curvature, mass, multiplier,
                          coefficient=1., vacuum=0.):
    cross = odd.channels(psi, covariant_jet(psi, first, omega))["odd"]
    return (palatini_density(coframe, curvature, coefficient, vacuum)
            +matter_density(coframe, psi, first, omega, mass)+np.sum(multiplier*(coframe-cross)))


def coframe_euler(coframe, psi, first, omega, curvature, mass, multiplier,
                   coefficient=1., vacuum=0.):
    """Independent E variation at fixed omega, d omega, psi and multiplier; no LC substitution."""
    _, inverse, volume = frame_data(coframe)
    covariant = covariant_jet(psi, first, omega)
    imag = odd.readouts.pairing(psi, covariant).imag
    ld = matter_density(coframe, psi, first, omega, mass)
    result = ld*inverse.T+volume*(inverse @ imag @ inverse).T+multiplier
    lg = palatini_density(coframe, curvature, coefficient, vacuum)
    result += lg*inverse.T
    for a, nu in np.ndindex((4, 4)):
        dinverse = -np.outer(inverse[:, a], inverse[nu])
        dr = (np.einsum("ma,nb,mnab", dinverse, inverse, curvature)
              +np.einsum("ma,nb,mnab", inverse, dinverse, curvature))
        result[a, nu] += coefficient*volume*dr/2
    return result


def torsion(coframe, first, omega):
    mixed = np.einsum("ab,mbc->mac", ETA, omega)
    connection = np.einsum("mab,bn->amn", mixed, coframe)
    return first.transpose(1, 0, 2)-first.transpose(1, 2, 0)+connection-connection.swapaxes(1, 2)


def torsion_free_check(coframe, psi):
    response, source = spin_maps(coframe, psi)
    multiplier, _, rank, _ = np.linalg.lstsq(response.T, source, rcond=1e-11)
    a, aq = axial_currents(psi)
    gram = np.array([[a @ a, a @ aq], [a @ aq, aq @ aq]])
    return {"best_multiplier": multiplier.reshape(4, 4), "map_rank": int(rank),
            "spin_residual_norm": float(np.linalg.norm(source-response.T @ multiplier)),
            "source_norm": float(np.linalg.norm(source)), "axial": a, "weighted_axial": aq,
            "axial_euclidean_Gram_determinant_not_Lorentz_invariant": float(np.linalg.det(gram)),
            "axial_pair_rank": int(np.linalg.matrix_rank(np.column_stack((a, aq)), tol=1e-10))}


def transverse_obstruction(coframe, weighted_axial, target):
    """Necessary range conditions, in particular for the nonzero spacelike weighted axial case."""
    _, inverse, _ = frame_data(coframe)
    aq = checks._real(weighted_axial, (4,), "weighted axial current")
    norm = float(aq @ ETA @ aq)
    if abs(norm) < 1e-16:
        raise ValueError("Non-null weighted axial current required for this projector")
    projector = np.eye(4)-np.outer(aq, ETA @ aq)/norm
    target = checks._real(target, (4, 4), "coordinate coframe target") @ inverse
    projected = projector.T @ ETA @ target @ projector
    return {"weighted_axial_square": norm, "row_contraction": aq @ ETA @ target,
            "transverse_antisymmetric": (projected-projected.T)/2}


def schur_compatibility(geometry=None):
    """Eliminate contorsion before solving; retain null-space compatibility, not just a fit."""
    g = odd.reference_geometry() if geometry is None else geometry
    e, d, lc = g["frame"], g["data"], g["bundle"]["omega"]
    response, source = spin_maps(e, d["psi"])
    hessian = contorsion_hessian(e)
    schur = response @ np.linalg.solve(hessian, response.T)
    drive = response @ np.linalg.solve(hessian, source)
    base = odd.channels(d["psi"], covariant_jet(d["psi"], d["first"], lc))["odd"]
    target = (e-base).reshape(-1)
    _, singular, vh = np.linalg.svd(schur)
    rank = int(np.sum(singular > singular[0]*1e-10))
    null = vh[rank:].T
    _, aq = axial_currents(d["psi"])
    obstruction = transverse_obstruction(e, aq, target.reshape(4, 4))
    return {"schur": schur, "drive": drive, "target": target, "rank": rank, "nullspace": null,
            "projected_target": null.T @ target, "projected_drive": null.T @ drive,
            "obstruction": obstruction,
            "nonzero_coefficient_c_requires": "N^T(c b+d)=0, S lambda=c b+d",
            "coupling_rescaling_cannot_remove_nonzero_target_if_drive_projection_vanishes": True}


def cartan_constraint_completion(geometry=None, coefficient=1.):
    """Solve only the algebraic connection/constraint block at one already prepared point."""
    g = odd.reference_geometry() if geometry is None else geometry
    e, de, d = g["frame"], g["first"], g["data"]
    lc = g["bundle"]["omega"]
    response, source = spin_maps(e, d["psi"])
    hessian = contorsion_hessian(e, coefficient)
    base = odd.channels(d["psi"], covariant_jet(d["psi"], d["first"], lc))["odd"]
    target = (e-base).reshape(-1)
    matrix = np.block([[hessian, -response.T], [-response, np.zeros((16, 16))]])
    rhs = np.concatenate((-source, -target))
    solution, _, rank, singular = np.linalg.lstsq(matrix, rhs, rcond=1e-11)
    k, multiplier = solution[:24], solution[24:].reshape(4, 4)
    omega = lc+unpack(k)
    rebuilt = odd.channels(d["psi"], covariant_jet(d["psi"], d["first"], omega))["odd"]
    _, _, vh = np.linalg.svd(matrix)
    return {"matrix": matrix, "rhs": rhs, "solution": solution, "rank": int(rank),
            "singular_values": singular, "nullspace": vh[rank:].T, "contorsion": unpack(k),
            "omega": omega, "multiplier": multiplier, "response": response, "hessian": hessian,
            "connection_residual": hessian @ k+source-response.T @ multiplier.reshape(-1),
            "constraint_residual": e-rebuilt, "full_residual": matrix @ solution-rhs,
            "torsion": torsion(e, de, omega),
            "temporal_eigenvalues": np.linalg.eigvalsh(kinetic_weights(e, multiplier)[0]),
            "not_probe_or_coframe_Euler_or_gauge_solution": True}


def periodic_variations(count=33):
    """Direct integrated Palatini connection variation, plus independent probe/multiplier variations."""
    fixture = odd.real_law.periodic_fixture(count)
    x, differentiate = fixture["x"], fixture["differentiate"]
    rng = np.random.default_rng(4681)
    amplitude = rng.normal(size=(4, 4))*0.025
    coframes = np.eye(4)[None]+np.sin(x[:, None, None])*amplitude
    dcoframes = np.zeros((count, 4, 4, 4))
    dcoframes[:, 0] = np.cos(x[:, None, None])*amplitude
    lc = np.array([dirac.bundle(e, de)["omega"] for e, de in zip(coframes, dcoframes)])
    k = 0.03*np.cos(x[:, None]+np.arange(24)[None]/5)
    omega = lc+np.array([unpack(c) for c in k])
    variation = 0.05*np.sin(2*x[:, None]+np.arange(24)[None]/7)
    domega = np.zeros((count, 4, 4, 4, 4))
    domega[:, 0] = differentiate(omega).real
    dvariation = np.zeros_like(domega)
    dvariation[:, 0] = differentiate(np.array([unpack(c) for c in variation])).real
    vectors = rng.normal(size=(3, 12))+1j*rng.normal(size=(3, 12))
    psi = vectors[0]+0.1*np.sin(x[:, None])*vectors[1]
    pvariation = 0.1*np.cos(2*x[:, None])*vectors[2]
    first, pfirst = np.zeros((count, 4, 12), complex), np.zeros((count, 4, 12), complex)
    first[:, 0], pfirst[:, 0] = differentiate(psi), differentiate(pvariation)
    lam = 0.02*np.sin(x[:, None, None]+np.arange(16).reshape(4, 4))
    lvariation = 0.03*np.cos(2*x[:, None, None]+np.arange(16).reshape(4, 4)/3)
    mass = odd.background.triadic_mass()
    coefficient, dx = 0.7, 2*np.pi/count
    weights = np.array([kinetic_weights(e, l) for e, l in zip(coframes, lam)])
    divergence = differentiate(weights[:, 0])
    divergence = (divergence+divergence.conj().swapaxes(-1, -2))/2

    def action(p, dp, w, dw, l):
        return dx*sum(direct_parent_density(e, a.reshape(3, 4), b.reshape(4, 3, 4), c,
                                            curvature_upper(c, dc), mass, lm, coefficient)
                      for e, a, b, c, dc, lm in zip(coframes, p, dp, w, dw, l))

    spin_prediction, probe_prediction, multiplier_prediction = 0., 0., 0.
    ward_error = 0.
    for i in range(count):
        response, source = spin_maps(coframes[i], psi[i].reshape(3, 4))
        spin_el = contorsion_hessian(coframes[i], coefficient) @ k[i]+source-response.T @ lam[i].reshape(-1)
        spin_prediction += dx*spin_el @ variation[i]
        _, _, volume = frame_data(coframes[i])
        connection = np.array([np.kron(np.eye(3), s) for s in spin_connection(omega[i])])
        op = odd.real_law.real_operator(psi[i], first[i], weights[i], connection,
                                       volume*np.kron(mass, BETA), divergence[i])
        probe_prediction += 2*dx*np.vdot(pvariation[i], op["symmetric"]).real
        ward_error = max(ward_error, abs(op["current_divergence"]-2*np.vdot(psi[i], op["symmetric"]).imag))
        cross = odd.channels(psi[i].reshape(3, 4),
                             covariant_jet(psi[i].reshape(3, 4), first[i].reshape(4, 3, 4), omega[i]))["odd"]
        multiplier_prediction += dx*np.sum(lvariation[i]*(coframes[i]-cross))
    step = 1e-5
    wvariation = np.array([unpack(c) for c in variation])
    spin_numeric = (action(psi, first, omega+step*wvariation, domega+step*dvariation, lam)
                    -action(psi, first, omega-step*wvariation, domega-step*dvariation, lam))/(2*step)
    probe_numeric = (action(psi+step*pvariation, first+step*pfirst, omega, domega, lam)
                     -action(psi-step*pvariation, first-step*pfirst, omega, domega, lam))/(2*step)
    multiplier_numeric = (action(psi, first, omega, domega, lam+step*lvariation)
                          -action(psi, first, omega, domega, lam-step*lvariation))/(2*step)

    evariation = 0.03*np.sin(2*x[:, None, None]+np.arange(16).reshape(4, 4)/5)

    def lift(frames):
        derivatives = np.zeros((count, 4, 4, 4))
        derivatives[:, 0] = differentiate(frames).real
        connections = np.array([dirac.bundle(e, de)["omega"] for e, de in zip(frames, derivatives)])
        jets = np.zeros((count, 4, 4, 4, 4))
        jets[:, 0] = differentiate(connections).real
        return connections, jets

    plus, minus = coframes+step*evariation, coframes-step*evariation
    wplus, dwplus = lift(plus)
    wminus, dwminus = lift(minus)
    wlc, dwlc = lift(coframes)
    dlift = (wplus-wminus)/(2*step)
    fixed_prediction, chain_prediction = 0., 0.
    for e, p, dp, w, dw, l, ve, vw in zip(coframes, psi, first, wlc, dwlc, lam, evariation, dlift):
        pp, ddp = p.reshape(3, 4), dp.reshape(4, 3, 4)
        fe = coframe_euler(e, pp, ddp, w, curvature_upper(w, dw), mass, l, coefficient)
        response, source = spin_maps(e, pp)
        fw = source-response.T @ l.reshape(-1)
        fixed_prediction += dx*np.sum(fe*ve)
        chain_prediction += dx*fw @ pack(vw)
    fixed_numeric = dx*sum(
        (direct_parent_density(ep, p.reshape(3, 4), dp.reshape(4, 3, 4), w,
                               curvature_upper(w, dw), mass, l, coefficient)
         -direct_parent_density(em, p.reshape(3, 4), dp.reshape(4, 3, 4), w,
                                curvature_upper(w, dw), mass, l, coefficient))/(2*step)
        for ep, em, p, dp, w, dw, l in zip(plus, minus, psi, first, wlc, dwlc, lam))
    # The LC path must vary E as well as its connection.
    def lc_action(frames, connections, jets):
        return dx*sum(direct_parent_density(e, p.reshape(3, 4), dp.reshape(4, 3, 4), w,
                                            curvature_upper(w, dw), mass, l, coefficient)
                      for e, p, dp, w, dw, l in zip(frames, psi, first, connections, jets, lam))
    lc_numeric = (lc_action(plus, wplus, dwplus)-lc_action(minus, wminus, dwminus))/(2*step)
    return {"points": count, "connection_variation_error": float(abs(spin_numeric-spin_prediction)),
            "probe_variation_error": float(abs(probe_numeric-probe_prediction)),
            "multiplier_variation_error": float(abs(multiplier_numeric-multiplier_prediction)),
            "independent_coframe_variation_error": float(abs(fixed_numeric-fixed_prediction)),
            "LC_coframe_chain_rule_error": float(abs(lc_numeric-fixed_prediction-chain_prediction)),
            "omitted_LC_spin_reaction": float(chain_prediction),
            "phase_Ward_error": float(ward_error), "off_shell_test_not_field_solution": True}


def evaluate():
    g = odd.reference_geometry()
    tf = torsion_free_check(g["frame"], g["data"]["psi"])
    complete = cartan_constraint_completion(g)
    schur = schur_compatibility(g)
    return {"status": "first-order neutral odd-cross parent and pointwise Cartan/constraint block; not a native or full field solution",
            "parent": "S=integral[v(c R(E,omega)/2-u)+L_D(E,Psi,omega)+lambda:(E-C_minus(Psi,omega))]",
            "independent_fields": ["invertible E", "real lower Lorentz omega", "three complex commuting spinors", "real multiplier density"],
            "fixed_comparison_data": ["prepared Hermitian three-channel M", "Hermitian Q=i(E12-E21)/2", "neutral sector; no solved internal gauge equation"],
            "torsion_free_reference_test": {k: v.tolist() if isinstance(v, np.ndarray) else v for k, v in tf.items()},
            "failed_reference_connection_constraint_attempt": {
                "Einstein_coefficient_arbitrary_not_calibrated": 1., "matrix_size": 40, "matrix_rank": complete["rank"],
                "response_rank": int(np.linalg.matrix_rank(complete["response"], tol=1e-10)),
                "nullity": 40-complete["rank"], "residual_norm": float(np.linalg.norm(complete["full_residual"])),
                "connection_residual_norm": float(np.linalg.norm(complete["connection_residual"])),
                "constraint_residual_norm": float(np.linalg.norm(complete["constraint_residual"])),
                "least_squares_vector_is_not_a_solution_or_a_stability_test": True,
                "coframe_probe_normal_equations_not_solved": True},
            "scale_independent_reference_compatibility": {
                "Schur_rank": schur["rank"], "Schur_nullity": 16-schur["rank"],
                "null_projected_target_norm": float(np.linalg.norm(schur["projected_target"])),
                "null_projected_Dirac_drive_norm": float(np.linalg.norm(schur["projected_drive"])),
                "analytic_Dirac_drive_identity_error": float(np.linalg.norm(schur["drive"].reshape(4, 4)-dirac_drive_formula(g["frame"], g["data"]["psi"]))),
                "weighted_axial_Lorentz_square": schur["obstruction"]["weighted_axial_square"],
                "transverse_antisymmetric_component_norm_not_invariant": float(np.linalg.norm(schur["obstruction"]["transverse_antisymmetric"])),
                "equation": schur["nonzero_coefficient_c_requires"],
                "no_nonzero_Einstein_coefficient_repairs_this_fixed_reference_jet": True},
            "independent_action_variations": periodic_variations(),
            "remaining": ["coframe curvature and probe differential equations with all multiplier derivatives",
                          "local constraint propagation, temporal positivity and global boundary data",
                          "actual native field/adjoint/gauge/readout identification and physical scales"],
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
