"""Probe-source and positive-cone HC reductions, not native mass predictions."""
import argparse
import importlib.util
import json
import math
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "hc_phase_selection", Path(__file__).with_name("Phase_Selection_Derivation.py"))
phase = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(phase)

LOWER_THRESHOLD = (33-23*math.sqrt(2))/12
UPPER_THRESHOLD = (2-math.sqrt(3))/4
U = np.roll(np.eye(3), 1, axis=0)


def _hermitian(value, name):
    value = phase._finite_square(value, name)
    if not np.allclose(value, value.conj().T, atol=1e-12, rtol=0):
        raise ValueError(f"{name} must be Hermitian")
    return value


def spin_bilinear_source(psi, spin_weight):
    """Real variation source; psi has generation rows and spin columns."""
    psi = np.asarray(psi, dtype=complex)
    c = phase._finite_square(spin_weight, "Spin bilinear weight")
    if (psi.ndim != 2 or psi.shape[0] == 0 or psi.shape[1] != c.shape[0]
            or not np.all(np.isfinite(psi))):
        raise ValueError("Finite generation-by-spin amplitudes must match the spin weight")
    source = psi @ c.T @ psi.conj().T
    return (source+source.conj().T)/2


def selfconsistent_source_rhs(density, closure, coupling=1.0, penalty=1.0):
    """CONDITIONAL canonical unitary mean-field dynamics after unconstrained H elimination."""
    density, closure = (_hermitian(v, n) for v, n in
                        ((density, "Probe density"), (closure, "Lambda")))
    if (density.shape != closure.shape or not math.isfinite(coupling)
            or not math.isfinite(penalty) or penalty <= 0
            or np.linalg.eigvalsh(density)[0] < -1e-12):
        raise ValueError("Compatible positive density and finite coupling/positive penalty required")
    effective = coupling*closure-coupling**2*density/(2*penalty)
    return -1j*(effective @ density-density @ effective)


def positive_hc_minimum(closure, source, penalty=1.0):
    """Minimize lambda||H-Lambda||_F^2+<J,H> over H >= 0, NOT H=Lambda."""
    unconstrained, _, _ = phase.relaxed_hc(closure, source, penalty)
    closure, source = np.asarray(closure, dtype=complex), np.asarray(source, dtype=complex)
    values, vectors = np.linalg.eigh(unconstrained)
    h = (vectors*np.maximum(values, 0)) @ vectors.conj().T
    residual = h-closure
    slack = 2*penalty*residual+source
    energy = penalty*np.vdot(residual, residual).real+np.vdot(source, h).real
    return h, slack, float(energy)


def cyclic_gram_and_derivative(phi):
    """Reuse the earlier conditional cyclic Gram family and its exact derivative."""
    _, _, closure, derivative = phase.native_cyclic_closure(phi)
    return closure[:3, :3], derivative[:3, :3]


def symmetric_cone_energy(phi, threshold, scale=1.0, penalty=1.0):
    """Three equally populated modes; threshold=g/(2 lambda_H t) is an INPUT."""
    if (not math.isfinite(phi) or abs(phi) > math.pi/4
            or not math.isfinite(threshold) or threshold <= 0
            or not math.isfinite(scale) or scale <= 0
            or not math.isfinite(penalty) or penalty <= 0):
        raise ValueError("Positive finite parameters and a phase in the positive-root chamber required")
    q, qp = cyclic_gram_and_derivative(phi)
    h, slack, energy = positive_hc_minimum(scale*q, 2*penalty*scale*threshold*np.eye(3), penalty)
    derivative = -2*penalty*np.vdot(h-scale*q, scale*qp).real
    return h, slack, energy, float(derivative)


def critical_threshold(phi):
    """Threshold that selects Phi on the two-clamped-mode interior branch."""
    if not math.isfinite(phi) or not 0 <= phi <= math.pi/4:
        raise ValueError("The phase must lie on the declared nonnegative chamber branch")
    x = math.cos(phi/3)
    a = 1+math.sqrt(2)*x
    return a*a/6-0.75*(4*x*x-1)/a


def critical_threshold_derivative(phi):
    critical_threshold(phi)
    x = math.cos(phi/3)
    a = 1+math.sqrt(2)*x
    dx = math.sqrt(2)*a/3-0.75*(8*x*a-math.sqrt(2)*(4*x*x-1))/(a*a)
    return -math.sin(phi/3)*dx/3


def solve_positive_cone_phase(threshold):
    """Unique positive interior branch; conjugate phase has the same energy."""
    if not math.isfinite(threshold) or not LOWER_THRESHOLD < threshold < UPPER_THRESHOLD:
        raise ValueError("A threshold strictly inside the proved interior-selection interval is required")
    lower, upper = 0.0, math.pi/4
    for _ in range(80):
        mid = (lower+upper)/2
        if critical_threshold(mid) < threshold:
            lower = mid
        else:
            upper = mid
    phi = (lower+upper)/2
    h, slack, energy, derivative = symmetric_cone_energy(phi, threshold)
    q = np.linalg.eigvalsh(cyclic_gram_and_derivative(phi)[0])
    r, a = 1/math.sqrt(12), 1/math.sqrt(6)
    largest_q_prime = -(4*r/3)*(a+2*r*math.cos(phi/3))*math.sin(phi/3)
    curvature = -2*largest_q_prime*critical_threshold_derivative(phi)
    return {
        "input_threshold_not_native_prediction": threshold,
        "phase_radians": phi,
        "conjugate_phase_radians": -phi,
        "theta_local_branch_radians": (2*math.pi+phi)/3,
        "gram_eigenvalues": q.tolist(),
        "positive_compensator_eigenvalues_per_t": np.linalg.eigvalsh(h).tolist(),
        "constraint_reaction_eigenvalues_per_lambda_t": np.linalg.eigvalsh(slack).tolist(),
        "numerical_eigenvalue_tolerance": 1e-12,
        "energy_per_lambda_t_squared": energy,
        "phase_force_per_lambda_t_squared": derivative,
        "phase_curvature_per_lambda_t_squared": curvature,
        "compensator_rank": 1,
        "matching_residual_norm_per_t": float(np.linalg.norm(h-cyclic_gram_and_derivative(phi)[0])),
    }


def _normalized_gram(value):
    value = _hermitian(value, "Normalized three-mode Gram matrix")
    if (value.shape != (3, 3) or np.linalg.eigvalsh(value)[0] < -1e-12
            or not math.isclose(np.trace(value).real, 1, abs_tol=1e-12, rel_tol=0)):
        raise ValueError("A positive three-mode Gram matrix with trace one is required")
    return value


def positive_root(value):
    value = _hermitian(value, "Positive root input")
    values, vectors = np.linalg.eigh(value)
    if values[0] < -1e-12:
        raise ValueError("A positive-semidefinite root input is required")
    return (vectors*np.sqrt(np.maximum(values, 0))) @ vectors.conj().T


def cyclic_root_with_radius(phi, ratio):
    """Trace-normalized principal-root family with s=r/a allowed to vary."""
    if not math.isfinite(phi) or not math.isfinite(ratio) or ratio < 0:
        raise ValueError("A finite phase and nonnegative finite radius ratio required")
    theta = (2*math.pi+phi)/3
    b = (np.eye(3)+ratio*(np.exp(1j*theta)*U+np.exp(-1j*theta)*U.T))
    b = b/math.sqrt(3+6*ratio**2)
    if np.linalg.eigvalsh(b)[0] < -1e-12:
        raise ValueError("The proposed cyclic family leaves the principal-root chamber")
    return b


def radius_energy_and_derivative(phi, ratio, threshold):
    if not math.isfinite(threshold) or threshold <= 0:
        raise ValueError("A positive finite threshold required")
    b = cyclic_root_with_radius(phi, ratio)
    theta = (2*math.pi+phi)/3
    denominator = 3+6*ratio**2
    bp = (np.exp(1j*theta)*U+np.exp(-1j*theta)*U.T)/math.sqrt(denominator)
    bp -= 6*ratio*b/denominator
    q, qp = b @ b, bp @ b+b @ bp
    h, _, energy = positive_hc_minimum(q, 2*threshold*np.eye(3))
    return energy, float(-2*np.vdot(h-q, qp).real)


def mix_toward_equal_modes(gram, fraction):
    gram = _normalized_gram(gram)
    if not math.isfinite(fraction) or not 0 <= fraction <= 1:
        raise ValueError("A mixing fraction in [0,1] required")
    return (1-fraction)*gram+fraction*np.eye(3)/3


def fixed_trace_minimum(threshold):
    """Exact phase/radius-unrestricted minimum at Tr Q=1, still with three modes."""
    if not math.isfinite(threshold) or threshold <= 0:
        raise ValueError("A positive finite threshold required")
    if threshold < 1/3:
        return 2*threshold-3*threshold**2
    return 1/3


def scale_energy_and_derivative(gram, scale, coupling=0.1, penalty=1.0):
    """Vary t at FIXED g,lambda and Q, not at fixed g/(2 lambda t)."""
    gram = _normalized_gram(gram)
    if (not math.isfinite(scale) or scale < 0 or not math.isfinite(coupling)
            or coupling <= 0 or not math.isfinite(penalty) or penalty <= 0):
        raise ValueError("Nonnegative scale and positive finite coupling/penalty required")
    h, _, energy = positive_hc_minimum(scale*gram, coupling*np.eye(3), penalty)
    derivative = -2*penalty*np.vdot(h-scale*gram, gram).real
    return energy, float(derivative)


def radius_and_closure_audit():
    """New unconstrained directions; does not negate the proved fixed-radius result."""
    threshold = 0.05
    result = solve_positive_cone_phase(threshold)
    phi = result["phase_radians"]
    q, _ = cyclic_gram_and_derivative(phi)
    values = np.linalg.eigvalsh(q)
    slope = -2*sum((threshold-v)*(1/3-v) for v in values if v < threshold)
    minimum_fraction = max((threshold-v)/(1/3-v) for v in values if v < threshold)
    mixed = mix_toward_equal_modes(q, 0.2)
    root = positive_root(mixed)
    a = np.trace(root).real/3
    z = np.trace(U.conj().T @ root)/3
    _, _, mixed_energy = positive_hc_minimum(mixed, 2*threshold*np.eye(3))
    _, radial_derivative = radius_energy_and_derivative(phi, 1/math.sqrt(2), threshold)
    _, scale_derivative = scale_energy_and_derivative(q, 1)
    h = symmetric_cone_energy(phi, threshold)[0]
    return {
        "source_boundary": {
            "deep_compensator_hypothesis": "hyp:frame-dependent-defect-readout in v470/13_hc_hypotheses.tex",
            "deeper_generator_and_defect_field_are_not_identified": True,
            "native_readout_map_is_not_evaluated": True,
            "positive_compression_zero": "S* H_core S=0 and H_core>=0 imply H_core S=0",
            "zero_mismatch_is_different": "[H_core,P]=0 allows a nonzero internal block P H_core P",
            "renaming_H_does_not_derive_a_new_action_or_source_ratio": True,
            "effective_coefficients_not_numerically_fixed_in_displayed_field_definitions": True,
        },
        "radius_relaxation": {
            "hypotheses": "same static cone energy, fixed t and Tr Q=1; no independent fixed root trace or radius law",
            "exact_energy_identity": "F=2k-3k^2+sum_i (k-q_i)_+^2",
            "global_minimum_for_0_lt_k_lt_one_third": "F_min=2k-3k^2, attained by every Tr Q=1 with Q>=k I",
            "global_minimum_for_k_ge_one_third": "F_min=1/3, attained only by Q=I/3",
            "cyclic_descent_path": "Q_e=(1-e)Q+e I/3; B_e=sqrt(Q_e) stays positive, cyclic and unit Frobenius norm",
            "descent_slope": "F_e'(0)=-2 sum_(q_i<k) (k-q_i)(1/3-q_i)<0 in the interior-selection interval",
            "illustrative_threshold": threshold,
            "old_fixed_radius_energy": result["energy_per_lambda_t_squared"],
            "unrestricted_fixed_trace_minimum": fixed_trace_minimum(threshold),
            "old_energy_excess": result["energy_per_lambda_t_squared"]-fixed_trace_minimum(threshold),
            "mixing_descent_derivative": slope,
            "pure_radius_derivative_at_fixed_phase": radial_derivative,
            "minimum_mixing_fraction_for_global_plateau": minimum_fraction,
            "example_mixing_fraction": 0.2,
            "mixed_energy": mixed_energy,
            "mixed_root_radius_ratio_r_over_a": float(abs(z)/a),
            "mixed_root_Koide_ratio": float(1/np.trace(root).real**2),
            "old_phase_minimum_is_not_a_full_shape_stationary_point": True,
        },
        "scale_relaxation": {
            "hypotheses": "same static cone energy; t variable at fixed g, lambda_H and Q; no other scale force",
            "derivative": "E_t'=2 lambda_H sum_i q_i min(t q_i,g/(2 lambda_H))>0 for t>0",
            "global_minimum": "t=0, H=0, E=0; normalized shape and phase are then not selected by this energy",
            "M_was_not_listed_as_an_independent_native_field_variable": True,
            "therefore_not_a_proved_native_time_evolution": True,
            "illustrative_derivative_at_t_one_g_point_one": scale_derivative,
        },
        "exact_matching_and_units": {
            "relative_residual_scope": "analyzed three-mode block; matched spectator blocks change the full Frobenius denominator",
            "relative_residual_norm_at_example": float(np.linalg.norm(h-q)/np.linalg.norm(q)),
            "relative_residual_lower_bound_in_phase_window": LOWER_THRESHOLD,
            "bound_argument": "largest active mode has residual t k; ||Lambda||_F=t||Q||_F<=t",
            "hard_matching_limit_at_fixed_g_t": "lambda_H->infinity gives k->0 and removes this interior-selection mechanism",
            "field_unit_covariance": "H'=cH,t'=ct,lambda_H'=lambda_H/c^2,g'=g/c leaves energy and k unchanged",
        },
        "required_native_shape_condition": {
            "at_trace_B_squared_one": "Tr B=sqrt(3/2) iff a=1/sqrt(6), r=1/sqrt(12) iff Koide=2/3",
            "existing_equal_norm_condition": "v480:koide-equal-norm and v480:koide-hc-mixing are conditional on the native root map and its orthogonality",
            "imposing_the_constraint_is_not_deriving_it": True,
        },
    }


def evaluate():
    spin = np.array([1, 0], dtype=complex)
    localized = np.array([1, 0, 0], dtype=complex)
    uniform = np.ones(3)/math.sqrt(3)
    c = np.diag([1, -1])
    local_source = spin_bilinear_source(np.outer(localized, spin), c)
    uniform_source = spin_bilinear_source(np.outer(uniform, spin), c)
    example = solve_positive_cone_phase(0.05)
    return {
        "status": "conditional source and positive-cone derivation; NOT a native phase or mass prediction",
        "source_dictionary": {
            "inherited_file": "sources/research/parts/v470/10_sphaera_and_physics.tex",
            "source_action_labels": ["thm:variational-form", "thm:master-field-equation"],
            "probe_source": "Herm Tr_spin[(I_gen tensor C) |Psi><Psi|], C=eta_D(i kappa Gamma.n-gamma)",
            "spin_internal_factorization_and_adjoint_must_be_supplied": True,
            "curvature_source": "Herm(kappa n_nu D_mu^ad F^{mu nu}) in the declared real variation",
            "scalar_current_traces_do_not_determine_generation_matrix": True,
            "native_generation_resolved_state_not_evaluated": True,
        },
        "same_scalar_current_different_coherence_witness": {
            "scope": "factorized finite amplitudes, not complete native field solutions",
            "scalar_bilinears": [float(np.trace(s).real) for s in (local_source, uniform_source)],
            "cycle_source_coherences": [float(np.trace(s @ U).real) for s in (local_source, uniform_source)],
        },
        "circulant_dynamics_obstruction": {
            "hypotheses": "canonical unitary modal dynamics; scalar spin coupling; Lambda=t Q; no other torques",
            "unconstrained_H_star": "Lambda-g rho/(2 lambda_H)",
            "density_equation": "i rho_dot=[g Lambda-g^2 rho/(2 lambda_H),rho]=g[Lambda,rho]",
            "cycle_coherence": "j=Tr(rho U); j_dot=i g Tr(rho[Lambda,U])=0",
            "arbitrary_local_coherence_is_not_the_needed_cycle_coherence": True,
            "does_not_exclude_noncirculant_native_interactions": True,
        },
        "positive_cone_model": {
            "energy": "lambda_H||H-t Q||_F^2+g Tr(H), H>=0, g>0",
            "requires_independent_positive_H_instead_of_exact_H_equals_Lambda": True,
            "three_equal_mode_occupations_not_the_empty_vacuum": True,
            "solution": "H_star=t (Q-k I)_+, k=g/(2 lambda_H t)",
            "KKT": "2 lambda_H(H-t Q)+g I-S=0; H>=0; S>=0; H S=0",
            "energy_per_lambda_t_squared": "sum f_k(q_i), f_k(q)=q^2 if q<=k else 2kq-k^2",
            "reaction_force_for_isotropic_source": "E_eff'=-Tr(S Lambda') because Tr(Lambda')=0",
            "spectral_clipping_is_not_a_low_degree_polynomial": True,
            "strict_interior_threshold_interval": [LOWER_THRESHOLD, UPPER_THRESHOLD],
            "lower_endpoint_exact": "(33-23 sqrt(2))/12",
            "upper_endpoint_exact": "(2-sqrt(3))/4",
            "implicit_phase_law": "k=(1+sqrt(2)x)^2/6-3(4x^2-1)/(4(1+sqrt(2)x)), x=cos(Phi/3)",
            "proved_local_and_chamber_global_phase_minimum": True,
            "does_not_prove_radial_or_full_field_stability": True,
            "releasing_radius_or_scale_without_extra_forces_invalidates_full_stationarity": True,
            "illustrative_unfitted_threshold": example,
        },
        "radius_and_closure_audit": radius_and_closure_audit(),
        "remaining_obligations": [
            "derive the generation carrier and cyclic Millennium bridge instead of assuming them",
            "decide whether native H is defined as Lambda or is an independently constrained field",
            "derive a static positive energy and the occupied probe/background state",
            "compute g/(2 lambda_H t) independently; do not infer it from a target angle or masses",
            "derive the fixed root trace/radius and scale support; releasing them gives shape descent and scale collapse in this reduced energy",
            "evaluate exact closure, other direct phase terms, gauge dynamics, kinetics and chiral mass matching",
            "do not read the rank-one compensator as three positive lepton masses",
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
