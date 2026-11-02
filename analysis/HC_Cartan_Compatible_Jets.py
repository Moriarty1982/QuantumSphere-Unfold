"""Construct local compatible jets of the declared neutral odd-cross Cartan parent.

Pointwise Taylor data, not Cauchy data on a surface or an evolved native solution.
"""
import argparse
import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "compatible_jets_cartan", Path(__file__).with_name("HC_Cross_Cartan_Parent.py"))
cartan = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(cartan)
odd, dirac, checks = cartan.odd, cartan.dirac, cartan.checks
ETA, WEIGHTS, BETA, Q = cartan.ETA, cartan.WEIGHTS, cartan.BETA, odd.Q_PHASE
MASS = odd.background.triadic_mass()
MASS_WEIGHT = np.kron(MASS, BETA)
PAIR2 = tuple(itertools.combinations_with_replacement(range(4), 2))


def realify(value):
    z = np.asarray(value, complex).reshape(-1)
    return np.concatenate((z.real, z.imag))


def complexify(value, shape):
    value = np.asarray(value, float)
    size = int(np.prod(shape))
    if value.shape != (2*size,):
        raise ValueError("Real/imaginary vector size must match the requested complex shape")
    return (value[:size]+1j*value[size:]).reshape(shape)


def weighted_mass(psi):
    return float(np.vdot(psi, Q @ MASS @ psi @ BETA.T).real)


def normalize_probe(psi):
    psi = checks._finite(psi, "initial three-channel spinors")
    if psi.shape != (3, 4):
        raise ValueError("Three four-component spinors required")
    value = weighted_mass(psi)
    if value >= -1e-12:
        raise ValueError("Negative nonzero weighted mass needed for the lambda=0 branch")
    return psi*np.sqrt(-4/value)


def seed_probe(seed=183):
    """Deterministic free state preparation; no resonance eigenvalue or physical mass is fitted."""
    rng = np.random.default_rng(seed)
    psi = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
    if weighted_mass(psi) > 0:
        psi = psi.conj()
    return normalize_probe(psi)


def zero_multiplier_connection(coframe, psi, coefficient=1.):
    _, source = cartan.spin_maps(coframe, psi)
    hessian = cartan.contorsion_hessian(coframe, coefficient)
    return cartan.unpack(np.linalg.solve(hessian, -source))


def covariant_probe_residual(psi, covariant):
    return 1j*np.einsum("aij,arj->ri", WEIGHTS, covariant)-MASS @ psi @ BETA.T


def first_jet(psi=None, coefficient=1.):
    """E=I, dE=lambda=d lambda=0; solve E=C and the complete real probe equation at a point."""
    psi = seed_probe() if psi is None else checks._finite(psi, "prepared probe")
    coframe = np.eye(4)
    omega = zero_multiplier_connection(coframe, psi, coefficient)

    def image(vector):
        covariant = complexify(vector, (4, 3, 4))
        frame = odd.channels(psi, covariant)["odd"]
        kinetic = 1j*np.einsum("aij,arj->ri", WEIGHTS, covariant)
        return np.concatenate((frame.reshape(-1), realify(kinetic)))

    matrix = np.column_stack([image(e) for e in np.eye(96)])
    rhs = np.concatenate((coframe.reshape(-1), realify(MASS @ psi @ BETA.T)))
    solution, _, rank, singular = np.linalg.lstsq(matrix, rhs, rcond=1e-11)
    _, _, vh = np.linalg.svd(matrix, full_matrices=True)
    covariant = complexify(solution, (4, 3, 4))
    first = covariant-np.einsum("mij,rj->mri", cartan.spin_connection(omega), psi)
    connection = np.array([np.kron(np.eye(3), b) for b in cartan.spin_connection(omega)])
    weights = cartan.kinetic_weights(coframe, np.zeros((4, 4)))
    operator = odd.real_law.real_operator(psi.reshape(-1), first.reshape(4, 12), weights,
                                          connection, MASS_WEIGHT, np.zeros((12, 12)))
    return {"psi": psi, "coframe": coframe, "coframe_first": np.zeros((4, 4, 4)),
            "omega": omega, "covariant": covariant, "first": first, "matrix": matrix,
            "rhs": rhs, "rank": int(rank), "singular_values": singular,
            "solution": solution, "nullspace": vh[rank:].T,
            "linear_residual": matrix @ solution-rhs,
            "probe_operator": operator, "coframe_residual": odd.channels(psi, covariant)["odd"]-coframe,
            "weighted_mass": weighted_mass(psi), "coefficient": coefficient}


def probe_check(data, multiplier_first=None):
    """Complete density-valued residual for this normal-point E=I, dE=lambda=0 ansatz."""
    dlambda = np.zeros((4, 4, 4)) if multiplier_first is None else multiplier_first
    divergence = sum(np.kron(Q, WEIGHTS[a])*np.einsum("mam->a", dlambda)[a] for a in range(4))
    connection = np.array([np.kron(np.eye(3), b) for b in cartan.spin_connection(data["omega"])])
    return odd.real_law.real_operator(data["psi"].reshape(-1), data["first"].reshape(4, 12),
                                      cartan.kinetic_weights(data["coframe"], np.zeros((4, 4))),
                                      connection, MASS_WEIGHT, divergence)


def change_first(data, parameters):
    result = dict(data)
    vector = data["solution"]+data["nullspace"] @ parameters
    result["covariant"] = complexify(vector, (4, 3, 4))
    result["first"] = result["covariant"]-np.einsum(
        "mij,rj->mri", cartan.spin_connection(data["omega"]), data["psi"])
    return result


def unpack_second(vector, complex_probe=False):
    trailing = (3, 4) if complex_probe else (4, 4)
    values = complexify(vector, (10, *trailing)) if complex_probe else np.asarray(vector, float).reshape(10, *trailing)
    result = np.zeros((4, 4, *trailing), complex if complex_probe else float)
    for value, (r, s) in zip(values, PAIR2):
        result[r, s] = result[s, r] = value
    return result


def connection_first(data, coframe_second, multiplier_first=None):
    """Differentiate the actually eliminated Cartan connection, not an unrelated curvature jet."""
    e, psi, first = data["coframe"], data["psi"], data["first"]
    hessian = cartan.contorsion_hessian(e, data["coefficient"])
    response, source = cartan.spin_maps(e, psi)
    multiplier_first = np.zeros((4, 4, 4)) if multiplier_first is None else multiplier_first
    derivatives = []
    for r, (u, second) in enumerate(zip(first, coframe_second)):
        _, mixed = cartan.spin_maps(e, psi+u)
        _, quadratic = cartan.spin_maps(e, u)
        dsource = mixed-source-quadratic
        dcontorsion = cartan.unpack(np.linalg.solve(hessian, -dsource+response.T @ multiplier_first[r].reshape(-1)))
        dlc = dirac.bundle(e, second)["omega"]
        derivatives.append(dlc+dcontorsion)
    return np.array(derivatives)


def prolonged_constraint(data, psi_second, omega_first):
    psi, first, omega = data["psi"], data["first"], data["omega"]
    spin = cartan.spin_connection(omega)
    result = []
    for r in range(4):
        spin_first = cartan.spin_connection(omega_first[r])
        dcovariant = (psi_second[r]+np.einsum("mij,rj->mri", spin_first, psi)
                      +np.einsum("mij,rj->mri", spin, first[r]))
        result.append((odd.readouts.pairing(first[r], data["covariant"], Q)
                       +odd.readouts.pairing(psi, dcovariant, Q)).imag)
    return np.array(result)-data["coframe_first"]


def second_jet_attempt(data=None, allow_multiplier_first=True):
    """Try coframe Euler and first constraint derivative, retaining symmetric jets and d lambda."""
    data = first_jet() if data is None else data
    zero_e = np.zeros((4, 4, 4, 4))
    zero_p = np.zeros((4, 4, 3, 4), complex)
    base_omega_first = connection_first(data, zero_e)

    def residual(e_second, p_second, dw, multiplier_first=None):
        constraint = prolonged_constraint(data, p_second, dw)
        curvature = cartan.curvature_upper(data["omega"], dw)
        fe = cartan.coframe_euler(data["coframe"], data["psi"], data["first"], data["omega"],
                                  curvature, MASS, np.zeros((4, 4)), data["coefficient"])
        if allow_multiplier_first:
            dlambda = np.zeros((4, 4, 4)) if multiplier_first is None else multiplier_first
            divergence = np.einsum("mam->a", dlambda)
            return np.concatenate((constraint.reshape(-1), fe.reshape(-1), divergence))
        return np.concatenate((constraint.reshape(-1), fe.reshape(-1)))

    base = residual(zero_e, zero_p, base_omega_first)
    columns = []
    for value in np.eye(160):
        e_second = unpack_second(value)
        dlc = np.array([dirac.bundle(data["coframe"], second)["omega"] for second in e_second])
        columns.append(residual(e_second, zero_p, base_omega_first+dlc)-base)
    for value in np.eye(240):
        columns.append(residual(zero_e, unpack_second(value, True), base_omega_first)-base)
    if allow_multiplier_first:
        response, _ = cartan.spin_maps(data["coframe"], data["psi"])
        hessian = cartan.contorsion_hessian(data["coframe"], data["coefficient"])
        for value in np.eye(64):
            dlambda = value.reshape(4, 4, 4)
            change = np.array([cartan.unpack(np.linalg.solve(hessian, response.T @ l.reshape(-1))) for l in dlambda])
            columns.append(residual(zero_e, zero_p, base_omega_first+change, dlambda)-base)
    matrix = np.column_stack(columns)
    solution, _, rank, singular = np.linalg.lstsq(matrix, -base, rcond=1e-11)
    e_second, p_second = unpack_second(solution[:160]), unpack_second(solution[160:400], True)
    dlambda = solution[400:].reshape(4, 4, 4) if allow_multiplier_first else np.zeros((4, 4, 4))
    dw = connection_first(data, e_second, dlambda)
    result = residual(e_second, p_second, dw, dlambda)
    return {"data": data, "coframe_second": e_second, "psi_second": p_second,
            "omega_first": dw, "multiplier_first": dlambda, "matrix": matrix, "base": base, "rank": int(rank),
            "singular_values": singular, "residual": result,
            "constraint_first_residual": result[:64].reshape(4, 4, 4),
            "coframe_Euler_residual": result[64:80].reshape(4, 4)}


def solve_compatible_first(max_steps=25, verbose=False):
    """Use free first derivatives to meet the second-jet compatibility equations, not fit constants."""
    original = first_jet()
    second = second_jet_attempt(original)
    u, singular, _ = np.linalg.svd(second["matrix"], full_matrices=True)
    null = u[:, second["rank"]:]
    hessian = cartan.contorsion_hessian(original["coframe"], original["coefficient"])
    inverse = np.linalg.inv(hessian)
    forms = []
    for basis in cartan.SPIN_BASIS:
        matrix = sum(np.kron(np.eye(3), WEIGHTS[mu] @ basis[mu]) for mu in range(4))
        forms.append(0.5j*(matrix-matrix.conj().T))
    forms = np.array(forms)
    psi = original["psi"].reshape(-1)

    def base_for(data):
        dsource = 2*np.einsum("i,pij,rj->rp", psi.conj(), forms, data["first"].reshape(4, 12)).real
        dw = np.einsum("rp,pmab->rmab", -dsource @ inverse.T, cartan.OMEGA_BASIS)
        dc = prolonged_constraint(data, np.zeros((4, 4, 3, 4), complex), dw)
        fe = cartan.coframe_euler(np.eye(4), data["psi"], data["first"], data["omega"],
                                  cartan.curvature_upper(data["omega"], dw), MASS, np.zeros((4, 4)),
                                  data["coefficient"])
        return np.concatenate((dc.reshape(-1), fe.reshape(-1), np.zeros(4)))

    parameters = np.zeros(original["nullspace"].shape[1])
    history = []
    for iteration in range(max_steps):
        base = base_for(change_first(original, parameters))
        error = null.T @ base
        norm = float(np.linalg.norm(error))
        history.append(norm)
        if verbose:
            print("compatibility", iteration, norm, flush=True)
        if norm < 1e-10:
            break
        step = 1e-5
        jacobian = np.column_stack([
            null.T @ (base_for(change_first(original, parameters+step*e))
                      -base_for(change_first(original, parameters-step*e)))/(2*step)
            for e in np.eye(len(parameters))])
        update = np.linalg.lstsq(jacobian, -error, rcond=1e-9)[0]
        accepted = False
        for scale in 2.**(-np.arange(16)):
            candidate = parameters+scale*update
            if np.linalg.norm(null.T @ base_for(change_first(original, candidate))) < norm:
                parameters = candidate
                accepted = True
                break
        if not accepted:
            break
    data = change_first(original, parameters)
    completion = second_jet_attempt(data)
    return {"data": data, "second": completion, "parameters": parameters,
            "history": history, "left_null": null,
            "converged": float(np.linalg.norm(completion["residual"])) < 1e-8}


def taylor_fields(constructed, point):
    """Actual smooth comparison fields realizing the jets; not assumed on shell away from zero."""
    point = checks._real(point, (4,), "local coordinate displacement")
    data, second = constructed["data"], constructed["second"]
    e2, p2 = second["coframe_second"], second["psi_second"]
    coframe = np.eye(4)+0.5*np.einsum("r,s,rsam->am", point, point, e2)
    de = np.einsum("s,rsam->ram", point, e2)
    psi = data["psi"]+np.einsum("r,rij->ij", point, data["first"])+0.5*np.einsum("r,s,rsij->ij", point, point, p2)
    first = data["first"]+np.einsum("s,rsij->rij", point, p2)
    multiplier = np.einsum("r,ram->am", point, second["multiplier_first"])
    bundle = dirac.bundle(coframe, de, e2)
    response, source = cartan.spin_maps(coframe, psi)
    hessian = cartan.contorsion_hessian(coframe, data["coefficient"])
    contorsion = cartan.unpack(np.linalg.solve(hessian, -source+response.T @ multiplier.reshape(-1)))
    omega = bundle["omega"]+contorsion
    inverse, volume = np.linalg.inv(coframe), abs(np.linalg.det(coframe))
    dinverse = np.array([-inverse @ d @ inverse for d in de])
    dvolume = volume*np.einsum("ma,ram->r", inverse, de)
    dw = []
    for r in range(4):
        dw.append(np.array([
            np.kron(np.eye(3), sum((dvolume[r]*inverse[mu, a]+volume*dinverse[r, mu, a])*WEIGHTS[a] for a in range(4)))
            +sum(second["multiplier_first"][r, a, mu]*np.kron(Q, WEIGHTS[a]) for a in range(4))
            for mu in range(4)]))
    divergence = np.einsum("mmij->ij", np.array(dw))
    connection = np.array([np.kron(np.eye(3), b) for b in cartan.spin_connection(omega)])
    operator = odd.real_law.real_operator(psi.reshape(-1), first.reshape(4, 12),
                                          cartan.kinetic_weights(coframe, multiplier), connection,
                                          volume*MASS_WEIGHT, divergence)
    constraint = odd.channels(psi, cartan.covariant_jet(psi, first, omega))["odd"]-coframe
    return {"coframe": coframe, "first_coframe": de, "psi": psi, "first_psi": first,
            "multiplier": multiplier, "omega": omega, "bundle": bundle, "contorsion": contorsion,
            "constraint": constraint, "probe": operator,
            "Cartan_residual": hessian @ cartan.pack(contorsion)+source-response.T @ multiplier.reshape(-1),
            "weights": cartan.kinetic_weights(coframe, multiplier)}


def temporal_ball_bound(constructed):
    """Conservative positive temporal-weight ball for the Taylor fields, not a full PDE theorem."""
    second = constructed["second"]
    en = float(np.linalg.norm(second["coframe_second"]))
    ln = float(np.linalg.norm(second["multiplier_first"][:, :, 0]))
    radius = min(1., np.sqrt(0.2/en) if en else 1., 1/(2*np.sqrt(2)*ln) if ln else 1.)
    delta = en*radius**2/2
    bound = (1-delta)**4*(1-np.sqrt(2)*delta/(1-delta))-radius*ln/np.sqrt(2)
    return {"radius_in_unscaled_comparison_coordinates": float(radius),
            "coframe_perturbation_bound": float(delta), "temporal_eigenvalue_lower_bound": float(bound),
            "not_a_stability_or_full_constrained_hyperbolicity_theorem": True}


def independent_field_checks(constructed):
    direction = np.array([1., 0.3, -0.2, 0.1])
    direction /= np.linalg.norm(direction)
    values = []
    for step in (0.002, 0.001, 0.0005):
        data = taylor_fields(constructed, step*direction)
        values.append({"step": step, "constraint_norm": float(np.linalg.norm(data["constraint"])),
                       "probe_residual_norm": float(np.linalg.norm(data["probe"]["symmetric"])),
                       "Cartan_residual_norm": float(np.linalg.norm(data["Cartan_residual"]))})
    step = 2e-6
    omega_first = np.array([(taylor_fields(constructed, step*u)["omega"]-taylor_fields(constructed, -step*u)["omega"])/(2*step)
                            for u in np.eye(4)])
    first = constructed["data"]
    fe = cartan.coframe_euler(np.eye(4), first["psi"], first["first"], first["omega"],
                              cartan.curvature_upper(first["omega"], omega_first), MASS, np.zeros((4, 4)),
                              first["coefficient"])
    return {"samples_off_shell_away_from_origin": values,
            "independent_connection_first_difference_error": float(np.linalg.norm(omega_first-constructed["second"]["omega_first"])),
            "coframe_Euler_with_independent_curvature_error": float(np.linalg.norm(fe))}


def evaluate(constructed=None):
    constructed = solve_compatible_first() if constructed is None else constructed
    first, second = constructed["data"], constructed["second"]
    a, aq = cartan.axial_currents(first["psi"])
    probe = probe_check(first, second["multiplier_first"])
    geometry = dirac.bundle(np.eye(4), np.zeros((4, 4, 4)), second["coframe_second"])
    _, source = cartan.spin_maps(np.eye(4), first["psi"])
    hessian = cartan.contorsion_hessian(np.eye(4), first["coefficient"])
    constraint = odd.channels(first["psi"], first["covariant"])["odd"]-np.eye(4)
    base_connection = cartan.pack(first["omega"])
    cartan_residual = hessian @ base_connection+source
    return {"status": "numerically compatible local jets of an added neutral Cartan comparison; not a Cauchy-surface or evolved solution"
                       if constructed["converged"] else "failed compatibility attempt; no joint local jet found",
            "same_comparison_parent_as": "HC_Cross_Cartan_Parent.md; Q and the matrix M unchanged, Einstein coefficient c=1 arbitrary, vacuum u=0",
            "chosen_local_branch": "E=I, dE=0, lambda=0, divergence(lambda)=0 at the point; d lambda allowed nonzero",
            "weighted_mass": first["weighted_mass"], "first_jet_linear_rank": first["rank"],
            "first_jet_free_derivatives": first["nullspace"].shape[1],
            "point_constraint_error": float(np.linalg.norm(constraint)),
            "point_real_probe_error": float(np.linalg.norm(probe["symmetric"])),
            "point_density_defect": float(np.linalg.norm(probe["defect"])),
            "point_Cartan_error": float(np.linalg.norm(cartan_residual)),
            "weighted_axial_square": float(aq @ ETA @ aq),
            "metric_signature_at_origin": [-1, 1, 1, 1],
            "LC_Ricci_scalar_unscaled_not_a_physical_prediction": float(geometry["curvature"]["scalar"]),
            "LC_Riemann_component_norm_not_invariant": float(np.linalg.norm(geometry["curvature"]["riemann"])),
            "second_order_cross_readout_curvature_identification_not_established": True,
            "second_jet_matrix_rank": second["rank"],
            "second_jet_constraint_derivative_error": float(np.linalg.norm(second["constraint_first_residual"])),
            "second_jet_coframe_Euler_error": float(np.linalg.norm(second["coframe_Euler_residual"])),
            "multiplier_first_norm_not_invariant": float(np.linalg.norm(second["multiplier_first"])),
            "multiplier_divergence_norm": float(np.linalg.norm(np.einsum("mam->a", second["multiplier_first"]))),
            "compatibility_history": constructed["history"], "compatible_second_jet_found": constructed["converged"],
            "positive_temporal_ball": temporal_ball_bound(constructed),
            "independent_Taylor_field_checks": independent_field_checks(constructed),
            "Taylor_data": {"psi_real": first["psi"].real.tolist(), "psi_imag": first["psi"].imag.tolist(),
                           "psi_first_real": first["first"].real.tolist(), "psi_first_imag": first["first"].imag.tolist(),
                           "psi_second_real": second["psi_second"].real.tolist(), "psi_second_imag": second["psi_second"].imag.tolist(),
                           "coframe_second": second["coframe_second"].tolist(), "multiplier_first": second["multiplier_first"].tolist()},
            "remaining": ["full Cauchy-surface constraints and their propagation", "second constraint derivatives and differentiated probe/coframe equations",
                          "higher-order compatibility and actual local evolution; numerical jet is not interval certified",
                          "full constrained principal symbol, native adjoint/gauge/HC/C7 identification, physical normalization and boundary data"],
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
