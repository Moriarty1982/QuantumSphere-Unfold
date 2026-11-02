"""Collective phase/amplitude action with its hidden canonical partners; not native masses."""
import argparse
import importlib.util
import json
import math
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "collective_projected_modes", Path(__file__).with_name("HC_Projected_Residual_Dynamics.py"))
projected = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(projected)
phase, readout = projected.phase, projected.readout


def _coordinates(value):
    value = projected._real(value, "collective coordinate vector", 1)
    if value.shape != (4,) or value[0] <= 0:
        raise ValueError("Coordinates (b,theta,a,c) with b>0 required")
    return value


def _two_real(value, name):
    value = projected._real(value, name, 1)
    if value.shape != (2,):
        raise ValueError(f"Two real {name} coordinates required")
    return value


def modal_state(coordinates):
    b, theta, a, c = _coordinates(coordinates)
    e = np.array([math.cos(theta/2), math.sin(theta/2)])
    normal = projected.ROTATION @ e
    return (a+1j*b)*e+c*normal


def modal_coordinates(state):
    state = readout._two_mode(state)
    b = float(np.linalg.norm(state.imag))
    if b <= 0 or not math.isfinite(b):
        raise ValueError("The polar residual chart requires a nonzero imaginary component")
    e = state.imag/b
    normal = projected.ROTATION @ e
    return np.array([b, 2*math.atan2(e[1], e[0]), state.real @ e, state.real @ normal])


def modal_tangents(coordinates):
    b, theta, a, c = _coordinates(coordinates)
    e = np.array([math.cos(theta/2), math.sin(theta/2)])
    normal = projected.ROTATION @ e
    return np.column_stack([1j*e, ((a+1j*b)*normal-c*e)/2, e, normal])


def kinetic_one_form(coordinates):
    b, _, a, c = _coordinates(coordinates)
    return np.array([-a, -b*c, b, 0.0])


def symplectic_form(coordinates):
    b, _, _, c = _coordinates(coordinates)
    return np.array([[0, -c, 2, 0], [c, 0, 0, b], [-2, 0, 0, 0], [0, -b, 0, 0]])


def probe_energy_gradient(coordinates, hamiltonian):
    """Fixed Hermitian modal H; field-dependent H also needs its own derivative."""
    state, tangents = modal_state(coordinates), modal_tangents(coordinates)
    hamiltonian = projected.backreaction._hermitian(hamiltonian, "Modal Hamiltonian")
    if hamiltonian.shape != (2, 2):
        raise ValueError("A Hermitian two-mode Hamiltonian required")
    image = hamiltonian @ state
    return float(np.vdot(state, image).real), 2*(tangents.conj().T @ image).real


def collective_lagrangian(coordinates, coordinate_rates, hamiltonian):
    rates = projected._real(coordinate_rates, "coordinate rates", 1)
    if rates.shape != (4,):
        raise ValueError("Four real coordinate rates required")
    energy, _ = probe_energy_gradient(coordinates, hamiltonian)
    return float(kinetic_one_form(coordinates) @ rates-energy)


def collective_rhs(coordinates, hamiltonian):
    _, gradient = probe_energy_gradient(coordinates, hamiltonian)
    return np.linalg.solve(symplectic_form(coordinates), gradient)


def _hidden_inputs(amplitude, velocity, hessian, source):
    if not math.isfinite(amplitude) or amplitude <= 0:
        raise ValueError("A positive finite residual amplitude required")
    velocity, source = _two_real(velocity, "velocity"), _two_real(source, "hidden source")
    hessian = projected._real(hessian, "hidden Hessian", 2)
    if (hessian.shape != (2, 2) or not np.allclose(hessian, hessian.T, atol=1e-12, rtol=0)
            or np.linalg.eigvalsh(hessian)[0] <= 0):
        raise ValueError("A positive definite symmetric two-mode hidden Hessian required")
    return np.diag([2, amplitude]), velocity, hessian, source


def stationary_hidden(amplitude, velocity, hessian, source):
    d, velocity, hessian, source = _hidden_inputs(amplitude, velocity, hessian, source)
    return -np.linalg.solve(hessian, d @ velocity+source)


def effective_coefficients(amplitude, hessian, source, potential):
    d, _, hessian, source = _hidden_inputs(amplitude, [0, 0], hessian, source)
    if not math.isfinite(potential):
        raise ValueError("A finite modal potential required")
    return {"kinetic_metric": d @ np.linalg.solve(hessian, d),
            "velocity_one_form": d @ np.linalg.solve(hessian, source),
            "potential": float(potential-source @ np.linalg.solve(hessian, source)/2)}


def effective_lagrangian(amplitude, velocity, hessian, source, potential):
    d, velocity, hessian, source = _hidden_inputs(amplitude, velocity, hessian, source)
    if not math.isfinite(potential):
        raise ValueError("A finite modal potential required")
    shifted = d @ velocity+source
    return float(shifted @ np.linalg.solve(hessian, shifted)/2-potential)


def _cartesian_inputs(residual, rate, hamiltonian):
    residual, rate = _two_real(residual, "residual"), _two_real(rate, "residual rate")
    hamiltonian = projected.backreaction._hermitian(hamiltonian, "Modal Hamiltonian")
    if hamiltonian.shape != (2, 2) or np.linalg.eigvalsh(hamiltonian.real)[0] <= 0:
        raise ValueError("A positive definite real Hamiltonian block required for this kinetic reduction")
    return residual, rate, hamiltonian.real, hamiltonian.imag


def cartesian_effective_lagrangian(residual, rate, hamiltonian):
    residual, rate, s, b = _cartesian_inputs(residual, rate, hamiltonian)
    shifted = rate-b @ residual
    return float(shifted @ np.linalg.solve(s, shifted)-residual @ s @ residual)


def cartesian_acceleration(residual, rate, hamiltonian):
    """Exact constant-H local second-order form; the initial rate retains the hidden state."""
    residual, rate, s, b = _cartesian_inputs(residual, rate, hamiltonian)
    conjugated = np.linalg.solve(s.T, (s @ b).T).T
    return (b+conjugated) @ rate-(conjugated @ b+s @ s) @ residual


def _isotropic_inputs(configuration, velocity, mass_coefficient, rotation):
    configuration, velocity = _two_real(configuration, "configuration"), _two_real(velocity, "velocity")
    if (configuration[0] <= 0 or not math.isfinite(mass_coefficient) or mass_coefficient <= 0
            or not math.isfinite(rotation)):
        raise ValueError("A positive amplitude, positive modal coefficient and finite rotation required")
    return configuration, velocity


def isotropic_reconstruction(configuration, velocity, mass_coefficient=2.0, rotation=0.3):
    (b, theta), (bdot, thetadot) = _isotropic_inputs(configuration, velocity, mass_coefficient, rotation)
    a = -bdot/mass_coefficient
    c = -b*(thetadot-2*rotation)/(2*mass_coefficient)
    return np.array([b, theta, a, c])


def isotropic_accelerations(configuration, velocity, mass_coefficient=2.0, rotation=0.3):
    (b, _), (bdot, thetadot) = _isotropic_inputs(configuration, velocity, mass_coefficient, rotation)
    relative = thetadot-2*rotation
    return np.array([b*relative**2/4-mass_coefficient**2*b, -2*bdot*relative/b])


def embedding_residual(state, rate, hamiltonian, embedding):
    """Check omitted MODE equations too; this is not a check of every native background field."""
    state, rate = readout._two_mode(state), readout._two_mode(rate)
    hamiltonian = projected.backreaction._hermitian(hamiltonian, "Full modal Hamiltonian")
    embedding = np.asarray(embedding, dtype=complex)
    if (embedding.shape != (hamiltonian.shape[0], 2) or not np.all(np.isfinite(embedding))
            or not np.allclose(embedding.conj().T @ embedding, np.eye(2), atol=1e-12, rtol=0)):
        raise ValueError("An isometric fixed two-mode embedding into the full modal carrier required")
    residual = 1j*embedding @ rate-hamiltonian @ embedding @ state
    tangent = embedding.conj().T @ residual
    return {"full": residual, "tangent": tangent, "normal": residual-embedding @ tangent}


def evaluate():
    m, rotation, time = 2.0, 0.3, 0.5  # Unfitted dimensionless witness, not native masses/time.
    h = m*np.eye(2)+rotation*phase.SIGMA_Y
    initial_q = np.array([1.0, 2*math.pi/3, 0.0, 0.0])
    initial = modal_state(initial_q)
    evolved = projected.unitary_state(h, initial, time)
    coordinates = modal_coordinates(evolved)
    rates = collective_rhs(coordinates, h)
    b, theta, a, c = coordinates
    reconstructed = isotropic_reconstruction(coordinates[:2], rates[:2], m, rotation)
    coefficients = effective_coefficients(b, 2*m*np.eye(2), [0, -2*rotation*b], m*b*b)
    effective_energy = rates[:2] @ coefficients["kinetic_metric"] @ rates[:2]/2+coefficients["potential"]
    embedding = np.vstack([np.eye(2), np.zeros((1, 2))])
    full_h = np.zeros((3, 3), dtype=complex)
    full_h[:2, :2] = h
    full_h[2, 2] = 5
    full_h[0, 2] = full_h[2, 0] = 0.1
    omitted = embedding_residual(initial, -1j*h @ initial, full_h, embedding)
    before_root, after_root = readout.quadratic_root(1j*initial.imag), readout.quadratic_root(1j*evolved.imag)
    return {
        "status": "exact collective pullback and conditional conservative modal reduction; native field profiles not evaluated",
        "full_native_action_contract": {
            "source": "v470/10_sphaera_and_physics.tex, thm:variational-form",
            "fields": "Psi, bar(Psi), A_mu, P_C7, H_C, with allowed projector and reality variations",
            "substitution": "S_coll[q,h]=S_native[Phi^I(x;q,h)] retaining every named field contribution",
            "restricted_EL": "EL_coll=(D Phi)^* EL_full; tangent stationarity does not imply normal stationarity",
            "required_extra_check": "EL_full normal to the admitted field ansatz must also vanish, including connection, projector and compensator equations",
            "native_field_profiles_and_real_positive_kinetic_reduction_missing": True,
            "no_inferred_general_relativity_or_EIH_equations_for_this_model": True,
        },
        "exact_complete_two_mode_chart": {
            "state": "f=(a+i b)e(theta/2)+c n(theta/2), b>0, n=[[0,-1],[1,0]]e",
            "coordinates": "(b,theta,a,c), with theta a lifted residual angle",
            "kinetic_term": "L_kin=b a_dot-a b_dot-b c theta_dot",
            "canonical_pairs_up_to_boundary_term": "p_b=-2a, p_theta=-b c; L=p_b b_dot+p_theta theta_dot-E",
            "symplectic_determinant": "det Omega=4b^2, nonzero for b>0",
            "equations": "b_dot=-E_a/2; theta_dot=-E_c/b; a_dot=(E_b+c theta_dot)/2; c_dot=(E_theta-c b_dot)/b",
            "pure_odd_submanifold": "a=c=0 makes the pulled-back kinetic form zero, not a phase gradient law",
            "odd_state_consistency_requires_normal_equations": "E_b=0 and E_theta=0 there, in addition to the retained coordinate equations",
            "hidden_input_is_canonical_information_not_generically_discardable": True,
        },
        "conditional_hidden_elimination": {
            "assumption": "E=V(b,theta)+j^T h+h^T W h/2, h=(a,c), W positive definite and no extra hidden kinetic term",
            "D": "diag(2,b)",
            "hidden_solution": "h=-W^(-1)(D q_dot+j), q=(b,theta)",
            "effective_action": "L_eff=(D q_dot+j)^T W^(-1)(D q_dot+j)/2-V",
            "derived_coefficients": "M=D W^(-1)D; A=D W^(-1)j; V_eff=V-j^T W^(-1)j/2",
            "coordinate_derivatives_of_W_D_j_V_must_be_kept_in_EL": True,
            "positive_metric_is_conditional_not_a_native_value": True,
            "no_irreversible_friction_from_this_closed_local_elimination": True,
            "other_dynamic_fields_can_produce_memory_or_flux_and_are_not_excluded": True,
            "constant_H_cartesian_specialization": "H=S+iB, S>0: L_eff=(r_dot-B r)^T S^(-1)(r_dot-B r)-r^T S r",
            "exact_second_order_equation": "r_ddot=(B+S B S^(-1))r_dot-(S B S^(-1)B+S^2)r",
            "initial_velocity_preserves_the_missing_state_information": "x0=S^(-1)(B r0-r_dot0); no loss of memory data and no Markov friction approximation",
        },
        "isotropic_probe_example": {
            "input_H": "H=m I+omega sigma_y; m>0, witness m>|omega|",
            "effective_L": "b_dot^2/m+b^2(theta_dot-2omega)^2/(4m)-m b^2",
            "derived_phase_inertia": "I_theta=b^2/(2m), I_Phi=b^2/(18m)",
            "equations": "b_ddot=b(theta_dot-2omega)^2/4-m^2 b; theta_ddot=-2(b_dot/b)(theta_dot-2omega)",
            "conserved_phase_momentum": "p_theta=b^2(theta_dot-2omega)/(2m)=-b c",
            "conserved_energy": "E=b_dot^2/m+b^2 theta_dot^2/(4m)+(m-omega^2/m)b^2",
            "apparent_damping": "2 b_dot/b changes sign under contraction; reversible amplitude/phase exchange, not viscosity",
            "dimensionless_m_not_identified_with_native_bare_or_lepton_mass": m,
            "dimensionless_rotation_input": rotation,
            "dimensionless_time": time,
            "exact_odd_initial_solution": "b=cos(m t), a=sin(m t), c=0, theta=theta0+2omega t until the b=0 chart node",
            "coordinates_at_example_time": coordinates.tolist(),
            "coordinate_rates": rates.tolist(),
            "hidden_reconstruction_error": float(np.linalg.norm(reconstructed-coordinates)),
            "full_state_norm_squared": float(np.vdot(evolved, evolved).real),
            "probe_energy": probe_energy_gradient(coordinates, h)[0],
            "effective_energy": float(effective_energy),
            "minimum_principal_root_before": float(np.linalg.eigvalsh(before_root)[0]),
            "minimum_signed_root_after": float(np.linalg.eigvalsh(after_root)[0]),
            "deriving_inertia_does_not_prove_root_chamber_preservation": True,
        },
        "normal_equation_countercheck": {
            "scope": "two-mode ansatz inside a positive three-mode Hermitian example, not the complete native field space",
            "hidden_coupling_input": 0.1,
            "tangent_residual_norm": float(np.linalg.norm(omitted["tangent"])),
            "normal_residual_norm": float(np.linalg.norm(omitted["normal"])),
            "normal_equation_would_be_missed_by_restricting_the_action_first": True,
        },
        "remaining_native_obligations": [
            "construct spatial mode profiles and the native field/carrier/readout map with a real positive kinetic form",
            "substitute the connection, closure projector and compensator backgrounds along with the probe",
            "derive the native hidden Hessian/source and phase/scale dependence rather than fit m, W, j or a potential",
            "check full normal field equations, constraint propagation and positive-root boundary signs",
            "derive any irreversible reduction from retained fields/fluxes rather than call the inertial exchange viscosity",
        ],
        "main_TeX_changed": False,
        "historical_masses_or_target_phase_used": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = json.dumps(evaluate(), indent=2, allow_nan=False)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
