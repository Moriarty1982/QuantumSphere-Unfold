"""Conditional root-chamber dynamics, not a native HC evolution or mass prediction."""
import argparse
import importlib.util
import json
import math
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "hc_root_phase_readout", Path(__file__).with_name("HC_Root_Readout.py"))
readout = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(readout)
backreaction = readout.backreaction
CHAMBER_EDGE = math.pi/4
SIGMA_Y = np.array([[0, -1j], [1j, 0]])
REAL_ROTATION = np.array([[0, -1], [1, 0]])


def _threshold(threshold):
    if (not math.isfinite(threshold)
            or not backreaction.LOWER_THRESHOLD < threshold < backreaction.UPPER_THRESHOLD):
        raise ValueError("A threshold strictly inside the proved interior-phase window required")
    return threshold


def _phase(phi):
    if not math.isfinite(phi) or abs(phi) > CHAMBER_EDGE:
        raise ValueError("A phase in the closed positive-root chamber required")
    return phi


def _positive(value, name):
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"A positive finite {name} required")
    return value


def aligned_mode(phi, amplitude=1.0, chamber=1):
    """A chosen eta=1 aligned-odd branch; no native preparation of it is asserted."""
    phi = _phase(phi)
    amplitude = _positive(amplitude, "internal amplitude")
    if not isinstance(chamber, int) or isinstance(chamber, bool) or chamber not in range(3):
        raise ValueError("One of the three chamber indices required")
    theta = (2*math.pi*chamber+phi)/3
    return 1j*amplitude*np.array([math.cos(theta/2), math.sin(theta/2)])


def phase_energy(phi, threshold):
    """Dimensionless static F=E/(lambda_H t^2), not a kinetic law."""
    _phase(phi)
    _threshold(threshold)
    _, _, energy, derivative = backreaction.symmetric_cone_energy(phi, threshold)
    return energy, derivative


def gradient_phase_rhs(phi, threshold, mobility=1.0):
    """ADDED overdamped law dPhi/dtau=-m F'; tau and m are not native time data."""
    _positive(mobility, "phase mobility")
    return -mobility*phase_energy(phi, threshold)[1]


def gradient_mode_rhs(phi, threshold, amplitude=1.0, chamber=1, mobility=1.0):
    mode = aligned_mode(phi, amplitude, chamber)
    return gradient_phase_rhs(phi, threshold, mobility)*REAL_ROTATION @ mode/6


def mechanical_phase_rhs(phi, velocity, threshold, inertia=1.0, damping=0.0):
    """Different ADDED law: I Phi''+Gamma Phi'+F'=0; velocity is independent input."""
    _positive(inertia, "phase inertia")
    if not math.isfinite(velocity) or not math.isfinite(damping) or damping < 0:
        raise ValueError("A finite angular velocity and nonnegative finite damping required")
    derivative = phase_energy(phi, threshold)[1]
    return np.array([velocity, -(damping*velocity+derivative)/inertia])


def mechanical_energy(phi, velocity, threshold, inertia=1.0):
    _positive(inertia, "phase inertia")
    if not math.isfinite(velocity):
        raise ValueError("A finite angular velocity required")
    return inertia*velocity**2/2+phase_energy(phi, threshold)[0]


def barrier_audit(threshold=0.05, inertia=1.0):
    """Fixed-radius/scale barrier, sufficient trapping criterion and an escape witness."""
    _threshold(threshold)
    _positive(inertia, "phase inertia")
    minimum = backreaction.solve_positive_cone_phase(threshold)
    phi = minimum["phase_radians"]
    energy = minimum["energy_per_lambda_t_squared"]
    boundary_energy = 2*threshold-2*threshold**2
    barrier = boundary_energy-energy
    if not math.isfinite(barrier) or barrier <= 0:
        raise ValueError("The positive phase barrier is numerically unresolved near the endpoint")
    # Above this finite barrier the outward undamped trajectory cannot turn before the edge.
    escape_energy = energy+1.1*barrier
    boundary_speed = math.sqrt(2*(escape_energy-boundary_energy)/inertia)
    return {
        "input_threshold_not_a_prediction": threshold,
        "input_dimensionless_inertia": inertia,
        "positive_minimum_phase": phi,
        "minimum_energy": energy,
        "edge_energy": boundary_energy,
        "barrier_above_minimum": barrier,
        "energy_gap_is_in_units_lambda_H_t_squared": True,
        "critical_speed_at_minimum": math.sqrt(2*barrier/inertia),
        "subbarrier_trapping_is_sufficient_not_necessary_with_damping": True,
        "undamped_escape_witness": {
            "initial_outward_speed": math.sqrt(2.2*barrier/inertia),
            "total_energy": escape_energy,
            "speed_at_edge": boundary_speed,
            "time_to_edge_upper_bound": (CHAMBER_EDGE-phi)/boundary_speed,
            "finite_time_crossing_follows_from_monotone_outward_energy_path": True,
        },
    }


def density_energy_gradient(density, threshold):
    """Explicit extension F(Q(rho)), Q=L(rho)^2/Tr L^2, and its Hermitian gradient.

    Signed L is permitted in this auxiliary extension to test local canonical
    dynamics. It is not silently promoted to a physical principal root.
    """
    _threshold(threshold)
    density = backreaction._hermitian(density, "Two-mode matrix")
    l = readout.density_root(density)
    norm_squared = float(np.vdot(l, l).real)
    if not math.isfinite(norm_squared) or norm_squared <= 0:
        raise ValueError("A nonzero two-mode matrix with finite root norm required")
    q = l @ l/norm_squared
    values, vectors = np.linalg.eigh(q)
    values = np.maximum(values, 0)
    energy = np.sum(np.where(values <= threshold, values**2, 2*threshold*values-threshold**2))
    gradient_q = (vectors*(2*np.minimum(values, threshold))) @ vectors.conj().T
    radial = float(np.trace(gradient_q @ q).real)
    gradient_l = (l @ gradient_q+gradient_q @ l-2*radial*l)/norm_squared
    h0, hz, hx = [float(np.trace(gradient_l @ e).real) for e in [readout.E0, readout.E1, readout.E2]]
    hamiltonian = h0*np.eye(2)+hz*readout.SIGMA_Z+hx*readout.SIGMA_X
    return float(energy), hamiltonian, q


def canonical_density_rhs(density, threshold):
    """ADDED canonical internal law i rho'= [dF/drho,rho], not the phase gradient law."""
    density = backreaction._hermitian(density, "Two-mode matrix")
    _, hamiltonian, _ = density_energy_gradient(density, threshold)
    return -1j*(hamiltonian @ density-density @ hamiltonian)


def pure_mode_density(phi, imaginary_bilinear=0.0):
    """Unit pure two-mode matrix with X3=y; y=0 is the aligned real plane."""
    _phase(phi)
    if not math.isfinite(imaginary_bilinear) or abs(imaginary_bilinear) >= 1:
        raise ValueError("A finite imaginary bilinear strictly between -1 and 1 required")
    theta = (2*math.pi+phi)/3
    radius = math.sqrt(1-imaginary_bilinear**2)
    return (np.eye(2)+radius*math.cos(theta)*readout.SIGMA_Z
            +radius*math.sin(theta)*readout.SIGMA_X+imaginary_bilinear*SIGMA_Y)/2


def canonical_coordinate_rhs(phi, imaginary_bilinear, threshold):
    density = pure_mode_density(phi, imaginary_bilinear)
    rhs = canonical_density_rhs(density, threshold)
    x1, x2 = [float(np.trace(sigma @ density).real) for sigma in [readout.SIGMA_Z, readout.SIGMA_X]]
    x1p, x2p = [float(np.trace(sigma @ rhs).real) for sigma in [readout.SIGMA_Z, readout.SIGMA_X]]
    theta_prime = (x1*x2p-x2*x1p)/(x1*x1+x2*x2)
    return np.array([3*theta_prime, float(np.trace(SIGMA_Y @ rhs).real)])


def canonical_saddle_audit(threshold=0.05):
    """The old radial descent is accessible transversely even at fixed pure-mode norm."""
    _threshold(threshold)
    minimum = backreaction.solve_positive_cone_phase(threshold)
    phi, phase_curvature = minimum["phase_radians"], minimum["phase_curvature_per_lambda_t_squared"]
    ratio = 1/math.sqrt(2)
    radial_derivative = backreaction.radius_energy_and_derivative(phi, ratio, threshold)[1]
    transverse_curvature = -ratio*radial_derivative
    growth_rate = 6*math.sqrt(-phase_curvature*transverse_curvature)
    return {
        "input_threshold_not_a_prediction": threshold,
        "stationary_phase": phi,
        "coordinates": "Phi and y=X3; unit pure modes have X1^2+X2^2=1-y^2",
        "root_radius": "s(y)=sqrt(1-y^2)/sqrt(2), with the readout eta kept at one",
        "phase_curvature": phase_curvature,
        "old_radial_derivative": radial_derivative,
        "transverse_curvature": transverse_curvature,
        "curvature_identity": "F_yy=-(1/sqrt(2)) F_s<0 at y=0",
        "canonical_coordinate_law": "Phi_dot=6 F_y; y_dot=-6 F_Phi",
        "linearization": [[0.0, 6*transverse_curvature], [-6*phase_curvature, 0.0]],
        "linearized_growth_and_decay_rates": [-growth_rate, growth_rate],
        "stationary_point_is_hyperbolic_saddle_for_this_canonical_extension": True,
        "positive_phase_curvature_is_not_full_two_mode_stability": True,
        "conditional_repair_target": "an independently derived even-y correction, stationary at the same phase, needs added F_yy > -current F_yy and positive total phase curvature",
        "minimum_extra_transverse_curvature_if_other_hessian_entries_unchanged": -transverse_curvature,
        "no_repair_potential_or_fitted_stiffness_was_added": True,
        "rate_is_dimensionless_not_a_physical_lifetime": True,
        "does_not_apply_if_native_constraints_exclude_this_transverse_mode": True,
    }


def evaluate():
    threshold, initial_phi = 0.05, 0.3  # Illustrative inputs, not fitted masses/phases.
    mode = aligned_mode(initial_phi)
    density = np.outer(mode, mode.conj())
    energy, derivative = phase_energy(initial_phi, threshold)
    _, hamiltonian, _ = density_energy_gradient(density, threshold)
    rhs = canonical_density_rhs(density, threshold)
    residual_rate = float(np.trace(SIGMA_Y @ rhs).real)
    barriers = barrier_audit(threshold)
    phi_star = barriers["positive_minimum_phase"]
    stationary = aligned_mode(phi_star)
    stationary_rhs = canonical_density_rhs(np.outer(stationary, stationary.conj()), threshold)
    return {
        "status": "conditional chamber dynamics; no native domain preparation, damping, phase or mass prediction",
        "source_boundary": {
            "main_TeX_changed": False,
            "historical_masses_or_target_phase_used": False,
            "eta_one_norm_transfer_still_assumed": True,
            "independent_positive_compensator_completion_still_not_native_H_equals_Lambda": True,
            "phase_kinetic_and_mobility_not_derived_from_native_action": True,
            "radius_and_scale_are_held_fixed_and_have_prior_descent_obstructions": True,
        },
        "exact_phase_dictionary_on_the_candidate": {
            "mode": "chi=i b(cos(theta/2),sin(theta/2)); b>0",
            "phase": "Phi=3 theta-2pi j, j=0,1,2, with |Phi|<=pi/4",
            "root": "L/(sqrt(2) b^2)=[I+(exp(i theta)U+adjoint)/sqrt(2)]/sqrt(6)=B_j(Phi)",
            "earlier_matrix_is_j_one": "other j permute Fourier roots and leave this symmetric spectral energy unchanged",
            "gram": "Q=L^2/Tr(L^2)=B_j^2",
            "does_not_derive_the_native_beta_phase_law": True,
        },
        "added_overdamped_phase_law": {
            "equation": "Phi_dot=-m F'(Phi), m>0; F=E/(lambda_H t^2)",
            "energy_rate": "F_dot=-m [F']^2<=0",
            "edge_energy": "F(+/-pi/4)=2k-2k^2",
            "edge_first_derivative": "F'(+/-pi/4)=0, not a strictly inward boundary force",
            "edge_second_derivative_for_strict_interior_threshold": "F''(+/-pi/4)=-2k/27<0",
            "local_Lipschitz_flow_preserves_closed_chamber": True,
            "interior_nonzero_phase_converges_to_same_sign_minimum": True,
            "center_and_edges_are_stationary_unstable_points": True,
            "odd_mode_lift": "chi_dot=(Phi_dot/6) [[0,-1],[1,0]] chi preserves norm and fixed-J oddness",
            "native_dissipation_or_preparation_is_not_proved": True,
            "arbitrary_extra_phase_force_is_not_automatically_admissible": True,
        },
        "added_inertial_phase_law": {
            "equation": "I Phi_ddot+Gamma Phi_dot+F'=0; I>0,Gamma>=0",
            "energy_rate": "d(I Phi_dot^2/2+F)/dtau=-Gamma Phi_dot^2",
            "sufficient_no_escape_condition": "initial phase inside and total energy strictly below 2k-2k^2",
            "zero_edge_force_does_not_stop_nonzero_velocity": True,
            "dimensionless_example": barriers,
            "inertia_and_time_unit_not_native_predictions": True,
        },
        "different_canonical_two_mode_law": {
            "auxiliary_energy_extension": "F(Q(rho)); Q=L_eta=1(rho)^2/Tr L^2",
            "equation": "rho_dot=-i[H,rho], H=gradient_rho F=h0 I+hz sigma_z+hx sigma_x",
            "on_the_pure_real_plane": "X3_dot=2(hz X2-hx X1)=-2 dF/dtheta=-6 F'(Phi)",
            "energy_and_purity_are_conserved_not_dissipated": True,
            "nonstationary_odd_plane_is_not_invariant_under_this_canonical_law": True,
            "a_common_phase_cannot_remove_X3": True,
            "leading_ratio_deficit_on_unit_pure_positive_branch": "2/3-K=12 [F'(Phi_initial)]^2 dtau^2+O(dtau^3)",
            "initial_phase": initial_phi,
            "initial_energy": energy,
            "initial_F_prime": derivative,
            "initial_X3_rate": residual_rate,
            "expected_initial_X3_rate": -6*derivative,
            "initial_energy_rate": float(np.trace(hamiltonian @ rhs).real),
            "stationary_minimum_density_rhs_norm": float(np.linalg.norm(stationary_rhs)),
            "not_the_native_probe_equation_or_a_universal_Hamiltonian_no_go": True,
        },
        "canonical_transverse_stability": canonical_saddle_audit(threshold),
        "remaining_native_obligations": [
            "derive extraction, eta=1 and native Gram/root equality independently of masses",
            "identify whether chi is a constrained background or a freely superposable canonical probe",
            "derive the relevant kinetic/constraint or dissipative law, not just a static minimum",
            "derive state preparation or an independently justified subbarrier bound",
            "include other phase forces, changing sources, radius, scale and gauge/current matching",
        ],
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
