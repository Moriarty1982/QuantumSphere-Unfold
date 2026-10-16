"""Exact projected-residual identities and finite tests; no native mode extraction."""
import argparse
import importlib.util
import json
import math
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "projected_root_phase", Path(__file__).with_name("HC_Root_Phase_Dynamics.py"))
phase = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(phase)
readout = phase.readout
backreaction = phase.backreaction
ROTATION = phase.REAL_ROTATION
IMAGINARY_READOUT = np.hstack([np.zeros((2, 2)), np.eye(2)])


def _square(value, name):
    return backreaction.phase._finite_square(value, name)


def _real(value, name, ndim):
    value = np.asarray(value)
    if (value.ndim != ndim or np.any(value.imag != 0)
            or not np.all(np.isfinite(value))):
        raise ValueError(f"A finite real {name} required")
    return value.real.astype(float)


def temporal_generator(gamma_time, resonance, connection_time, spatial_slash):
    """Rearrange the native first-order equation in a DECLARED finite time chart.

    spatial_slash represents sum Gamma^a(partial_a+B_a); no self-adjointness,
    positive physical norm, or native mode truncation is inferred here.
    """
    gamma_time, resonance, connection_time, spatial_slash = [
        _square(value, name) for value, name in [
            (gamma_time, "Gamma^0"), (resonance, "Omega"),
            (connection_time, "Time connection"), (spatial_slash, "Spatial slash")]]
    if len({value.shape for value in [gamma_time, resonance, connection_time, spatial_slash]}) != 1:
        raise ValueError("All time-chart operators must act on the same finite carrier")
    try:
        return -connection_time-np.linalg.solve(gamma_time, spatial_slash+1j*resonance)
    except np.linalg.LinAlgError as error:
        raise ValueError("An invertible Gamma^0 on the selected time chart required") from error


def realification(generator):
    generator = _square(generator, "Complex-linear generator")
    return np.block([[generator.real, -generator.imag], [generator.imag, generator.real]])


def compensator_generator(gamma_time, gamma_null, compensator, kappa=1.0, resonance_coupling=0.0):
    """Complete displayed HC contribution, with matrix order retained, not a damping claim."""
    gamma_time, gamma_null = _square(gamma_time, "Gamma^0"), _square(gamma_null, "Gamma.n")
    compensator = backreaction._hermitian(compensator, "Positive mismatch field")
    if (gamma_time.shape != gamma_null.shape or gamma_time.shape != compensator.shape
            or not math.isfinite(kappa) or not math.isfinite(resonance_coupling)
            or np.linalg.eigvalsh(compensator)[0] < -1e-12):
        raise ValueError("Compatible gamma matrices, positive field and finite real coefficients required")
    try:
        return -np.linalg.solve(gamma_time, kappa*gamma_null @ compensator+1j*resonance_coupling*compensator)
    except np.linalg.LinAlgError as error:
        raise ValueError("An invertible time symbol required") from error


def real_state(state):
    state = np.asarray(state, dtype=complex)
    if state.ndim != 1 or state.size == 0 or not np.all(np.isfinite(state)):
        raise ValueError("A finite nonempty complex carrier vector required")
    return np.concatenate([state.real, state.imag])


def projected_blocks(transfer, transfer_rate, generator):
    """Exact real-linear factorization; the remaining kernel term is not dropped."""
    transfer = _real(transfer, "two-mode extraction", 2)
    transfer_rate = _real(transfer_rate, "extraction derivative", 2)
    generator = _real(generator, "carrier generator", 2)
    if (transfer.shape[0] != 2 or transfer.shape[1] < 2
            or transfer_rate.shape != transfer.shape
            or generator.shape != (transfer.shape[1], transfer.shape[1])
            or np.linalg.matrix_rank(transfer) != 2):
        raise ValueError("A full-row-rank two-mode transfer and compatible derivative/generator required")
    right_inverse = transfer.T @ np.linalg.solve(transfer @ transfer.T, np.eye(2))
    derivative_map = transfer_rate+transfer @ generator
    kernel_projector = np.eye(transfer.shape[1])-right_inverse @ transfer
    return {"right_inverse": right_inverse,
            "kernel_projector": kernel_projector,
            "derivative_map": derivative_map,
            "local_generator": derivative_map @ right_inverse,
            "hidden_coupling": derivative_map @ kernel_projector}


def projected_rhs(state, transfer, transfer_rate, generator):
    state = _real(state, "carrier vector", 1)
    blocks = projected_blocks(transfer, transfer_rate, generator)
    transfer = np.asarray(transfer).real.astype(float)
    if state.shape != (transfer.shape[1],):
        raise ValueError("The carrier vector must match the extraction")
    residual = transfer @ state
    hidden = blocks["kernel_projector"] @ state
    return {"residual": residual,
            "rate": blocks["derivative_map"] @ state,
            "local_rate": blocks["local_generator"] @ residual,
            "hidden_rate": blocks["derivative_map"] @ hidden}


def mode_generator(hamiltonian, damping=None):
    """An extra positive finite realization G=-iH-D, not the full native field law."""
    hamiltonian = backreaction._hermitian(hamiltonian, "Two-mode Hamiltonian")
    damping = np.zeros((2, 2)) if damping is None else backreaction._hermitian(damping, "Damping")
    if (hamiltonian.shape != (2, 2) or damping.shape != (2, 2)
            or np.linalg.eigvalsh(damping)[0] < -1e-12):
        raise ValueError("A two-mode Hamiltonian and positive two-mode damping required")
    return -1j*hamiltonian-damping


def residual_angle_rate(residual, rate):
    residual, rate = _real(residual, "residual", 1), _real(rate, "residual rate", 1)
    if residual.shape != (2,) or rate.shape != (2,):
        raise ValueError("Two real residual coordinates and rates required")
    squared_norm = float(residual @ residual)
    if not math.isfinite(squared_norm) or squared_norm <= 0:
        raise ValueError("A nonzero finite residual norm required for an angle")
    wedge = float(residual[0]*rate[1]-residual[1]*rate[0])
    return {"norm_squared": squared_norm,
            "norm_squared_rate": float(2*residual @ rate),
            "theta_rate": 2*wedge/squared_norm,
            "Phi_rate": 6*wedge/squared_norm}


def linear_angle_rate(generator, theta):
    generator = _real(generator, "two-mode generator", 2)
    if generator.shape != (2, 2) or not math.isfinite(theta):
        raise ValueError("A real two-mode generator and a finite coefficient angle required")
    residual = np.array([math.cos(theta/2), math.sin(theta/2)])
    return residual_angle_rate(residual, generator @ residual)["theta_rate"]


def chamber_boundary_rates(generator):
    rows = []
    for chamber in range(3):
        center = 2*math.pi*chamber/3
        rows.append({"chamber": chamber,
                     "left_theta_rate": linear_angle_rate(generator, center-math.pi/12),
                     "right_theta_rate": linear_angle_rate(generator, center+math.pi/12)})
    return rows


def moving_frame_residual_rhs(state, hamiltonian, frame, frame_rate):
    """Local imaginary-part derivative includes the moving-frame connection."""
    state = readout._two_mode(state)
    frame = readout._mode_frame(frame)
    frame_rate = np.asarray(frame_rate, dtype=complex)
    hamiltonian = backreaction._hermitian(hamiltonian, "Hamiltonian")
    if (hamiltonian.shape != (2, 2) or frame_rate.shape != (2, 2)
            or not np.all(np.isfinite(frame_rate))
            or not np.allclose(frame.conj().T @ frame_rate+frame_rate.conj().T @ frame,
                               np.zeros((2, 2)), atol=1e-12, rtol=0)):
        raise ValueError("A compatible unitary-frame derivative and two-mode Hamiltonian required")
    local_state = frame.conj().T @ state
    local_hamiltonian = frame.conj().T @ hamiltonian @ frame-1j*frame.conj().T @ frame_rate
    return {"local_state": local_state,
            "local_hamiltonian": local_hamiltonian,
            "residual": local_state.imag,
            "residual_rate": (-1j*local_hamiltonian @ local_state).imag}


def unitary_state(hamiltonian, state, time):
    hamiltonian = backreaction._hermitian(hamiltonian, "Hamiltonian")
    state = np.asarray(state, dtype=complex)
    if (state.shape != (hamiltonian.shape[0],) or not np.all(np.isfinite(state))
            or not math.isfinite(time)):
        raise ValueError("A compatible finite state and time required")
    values, vectors = np.linalg.eigh(hamiltonian)
    return (vectors*np.exp(-1j*values*time)) @ vectors.conj().T @ state


def closed_rotation_witness(speed=1.0):
    """C7 closure and oddness hold, but a constant rotation exits the root chamber."""
    if not math.isfinite(speed) or speed <= 0:
        raise ValueError("A positive finite illustrative rotation speed required")
    projector = np.diag([1, 1, 0])
    millennium = np.diag([1, 2, 3])
    hamiltonian = np.zeros((3, 3), dtype=complex)
    hamiltonian[:2, :2] = speed*phase.SIGMA_Y
    state = np.r_[phase.aligned_mode(0), 0]
    exit_time = (math.pi/4+0.02)/(6*speed)
    evolved = unitary_state(hamiltonian, state, exit_time)
    root_before = readout.quadratic_root(state[:2])
    root_after = readout.quadratic_root(1j*evolved[:2].imag)
    defect = backreaction.phase.minimal_native_closure(millennium, projector)
    return {"P": projector, "M": millennium, "H": hamiltonian,
            "initial_state": state, "evolved_state": evolved,
            "exit_time": exit_time, "defect": defect,
            "minimum_root_before": float(np.linalg.eigvalsh(root_before)[0]),
            "minimum_signed_root_after": float(np.linalg.eigvalsh(root_after)[0])}


def evaluate():
    zero = np.zeros((2, 4))
    h = np.diag([1, 2])
    g = mode_generator(h)
    carrier_g = realification(g)
    blocks = projected_blocks(IMAGINARY_READOUT, zero, carrier_g)
    residual = math.sqrt(0.96)*phase.aligned_mode(0).imag
    hidden_rows = []
    for sign in [-1, 1]:
        state = sign*np.array([0.2, 0])+1j*residual
        rates = projected_rhs(real_state(state), IMAGINARY_READOUT, zero, carrier_g)
        hidden_rows.append({"sign_of_hidden_real_component": sign,
                            "full_norm_squared": float(np.vdot(state, state).real),
                            "same_residual": rates["residual"].tolist(),
                            "Phi_rate": residual_angle_rate(rates["residual"], rates["rate"])["Phi_rate"]})
    chi = phase.aligned_mode(0)
    later = unitary_state(h, chi, 0.3)
    scalar_time = math.pi/2
    scalar_node = unitary_state(np.eye(2), chi, scalar_time)
    rotation = closed_rotation_witness()
    symmetric_damping = np.diag([0, 1])
    tracked = moving_frame_residual_rhs(chi, np.eye(2), np.eye(2), -1j*np.eye(2))
    return {
        "status": "exact projected identities and conditional obstructions; native extraction and dynamics not evaluated",
        "source_dictionary": {
            "fragment": "sources/research/parts/v470/10_sphaera_and_physics.tex",
            "labels": ["thm:master-field-equation", "thm:closed-master-system", "prop:equivalent-closure-criteria"],
            "second_field_reading": "v470/16_master_model.tex, thm:minimal-mmhc-field-equation",
            "time_chart": "G=-B_0-(Gamma^0)^(-1)sum_a Gamma^a(partial_a+B_a)-i(Gamma^0)^(-1)Omega",
            "native_derivative_connection": "B_mu=i A_mu+kappa H_C n_mu+eta(I-P_C7)n_mu",
            "invertible_time_symbol_common_carrier_and_domains_required": True,
            "f_equals_native_Psi_and_two_mode_extraction_are_not_given": True,
            "antiunitary_J_and_complex_linear_J_conventions_not_interchanged": True,
        },
        "exact_projected_equation": {
            "definition": "r=T(t) u, chi=i r; T real-linear includes alignment, extraction and field/carrier identification",
            "factorization_scope": "fixed instantaneous linear probe/background operator; field-dependent nonlinear lifts need their own fibre-consistency test",
            "equation": "r_dot=(T_dot+T G_real)u",
            "decomposition": "u=R r+z, T R=I, T z=0; r_dot=K r+q, K=(T_dot+T G_real)R, q=(T_dot+T G_real)z",
            "autonomy_iff": "(T_dot+T G_real) ker T=0 for all allowed lifts, or the corresponding restricted-carrier condition",
            "norm_and_angle": "(r.r)_dot=2r.r_dot; theta_dot=2det(r,r_dot)/(r.r); Phi_dot=3theta_dot",
            "zero_residual_has_no_angle_or_nonzero_root_scale": True,
            "X3_is_zero_by_projected_output_typing_not_by_unprojected_state_invariance": True,
        },
        "fixed_frame_Hermitian_case": {
            "split": "H=S+iB, S real symmetric, B real skew; f=x+i r",
            "equations": "x_dot=B x+S r; r_dot=B r-S x",
            "autonomy_for_all_hidden_inputs_iff": "S=0, equivalently J H J^(-1)=-H for J=conjugation",
            "commutation_with_antiunitary_J_does_not_imply_same_time_odd_invariance": True,
            "memory_equation_constant_operators": "r_dot=B r-S exp(Bt)x0-integral_0^t S exp(B(t-s)) S r(s) ds",
            "finite_skew_B_does_not_supply_a_decaying_Markov_friction_kernel": True,
            "hidden_coupling_norm_in_example": float(np.linalg.norm(blocks["hidden_coupling"])),
            "same_normalized_state_norm_and_same_residual_different_velocity": hidden_rows,
            "pure_odd_initial_state_is_not_sufficient_for_autonomy": {
                "initial_projected_rate_norm": float(np.linalg.norm((g @ chi).imag)),
                "later_projected_difference_from_frozen_compression": float(np.linalg.norm(later.imag-chi.imag)),
                "scalar_unitary_phase_can_annihilate_residual": float(np.linalg.norm(scalar_node.imag)),
            },
        },
        "moving_frame_and_damping": {
            "moving_local_H": "V* H V-i V* V_dot, with J=V K_complex V*",
            "moving_odd_invariance": "(I-P_-)G P_-=P_minus_dot P_-; not merely [M,P_C7]=0",
            "tracked_scalar_H_example_local_H_norm": float(np.linalg.norm(tracked["local_hamiltonian"])),
            "choosing_a_frame_to_track_the_state_is_not_a_native_frame_prediction": True,
            "positive_damping_specialization": "G=-iH-D; full odd autonomy requires Re H=0 and Im D=0; then K=Im H-Re D",
            "isotropic_damping_changes_amplitude_not_angle": True,
            "anisotropic_constant_damping_need_not_preserve_all_chambers": chamber_boundary_rates(-symmetric_damping),
            "native_temporal_compensator_piece": "-kappa n_0 H_C is only one piece, not the complete native HC generator",
            "complete_native_compensator_contribution": "G_HC=-(Gamma^0)^(-1)[kappa Gamma^mu n_mu+i gamma I] H_C",
            "positive_H_C_alone_does_not_prove_full_generator_attenuation": True,
            "minimal_exact_closure_sets_H_C_and_on_sector_penalty_to_zero": True,
        },
        "linear_three_chamber_obstruction": {
            "scope": "a fixed state-independent autonomous real 2x2 generator, all three chambers and all nonzero residuals",
            "angular_law": "theta_dot=2[omega+c cos(theta)+d sin(theta)], omega=(K21-K12)/2, c=(K21+K12)/2, d=(K22-K11)/2",
            "boundary_guards": "v(left_j)>=0 and v(right_j)<=0 for every j=0,1,2",
            "conclusion": "K=a I: amplitude scaling only; if norm preserving, K=0",
            "proof": "three disjoint admitted intervals require at least three zeros; a nonzero first-harmonic function has at most two",
            "does_not_exclude_a_selected_single_chamber_or_nonlinear_field_feedback": True,
            "closed_unitary_rotation_counterexample": {
                "P_C7_closure_error": float(np.linalg.norm(rotation["P"] @ rotation["evolved_state"]-rotation["evolved_state"])),
                "oddness_error": float(np.linalg.norm(rotation["evolved_state"].conj()+rotation["evolved_state"])),
                "native_minimal_defect_norm": float(np.linalg.norm(rotation["defect"])),
                "minimum_root_before": rotation["minimum_root_before"],
                "minimum_signed_root_after": rotation["minimum_signed_root_after"],
                "time_is_illustrative_not_native": rotation["exit_time"],
                "finite_sufficiency_test_not_a_full_native_field_solution": True,
            },
        },
        "native_invariance_and_matching_targets": {
            "exact_test": "6 det(r,(T_dot+T G_real)u)/(r.r) has inward signs at Phi=+/-pi/4 for every admitted lift u",
            "bounded_hidden_term": "||q||<=epsilon||r|| gives |delta theta_dot|<=2epsilon and |delta Phi_dot|<=6epsilon",
            "conditional_normalized_coisometric_bound": "if ||u||=1 and TT*=I, ||q||/||r||<=||hidden_coupling||sqrt(1-||r||^2)/||r||; no uniform bound near zero residual",
            "robust_full_chamber_guards": "unforced theta velocity at left >=2epsilon and at right <=-2epsilon",
            "old_zero_boundary_gradient_has_no_uniform_margin_against_arbitrary_hidden_forcing": True,
            "gradient_matching_if_norm_constant": "(T_dot+T G_real)u=-(m/6) F'(Phi) A r; A=[[0,-1],[1,0]]; this is a target not a derived identity",
            "native_matrices_extraction_frame_motion_and_hidden_state_still_needed": True,
        },
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
