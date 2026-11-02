"""Phase-selection and explicit minimal-HC audits, not a native prediction."""
import argparse
import importlib.util
import json
import math
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "phase_coupling_candidate", Path(__file__).with_name("Coupling_Scale_Candidate.py"))
candidate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(candidate)
LOWER_COS = math.sqrt(2)/2


def cyclic_tensor(phi):
    """Fixed-radius Hermitian family; outside the chamber it is NOT a mass root."""
    if not math.isfinite(phi):
        raise ValueError("A finite loop phase is required")
    theta = (2*math.pi+phi)/3
    u = np.roll(np.eye(3), 1, axis=0)
    z = np.exp(1j*theta)/math.sqrt(12)
    return np.eye(3)/math.sqrt(6)+z*u+z.conjugate()*u.T


def _finite_square(value, name):
    value = np.asarray(value, dtype=complex)
    if (value.ndim != 2 or value.shape[0] != value.shape[1] or value.size == 0
            or not np.all(np.isfinite(value))):
        raise ValueError(f"{name} must be a nonempty finite square matrix")
    return value


def minimal_native_closure(m, p, rho=0.5, sigma=0.5):
    """Evaluate the source Lambda on an orthogonal finite positive carrier."""
    m, p = _finite_square(m, "M"), _finite_square(p, "P")
    if (m.shape != p.shape or not np.allclose(p, p.conj().T, atol=1e-12, rtol=0)
            or not np.allclose(p @ p, p, atol=1e-12, rtol=0)):
        raise ValueError("P must be an orthogonal projector on the M carrier")
    if not all(math.isfinite(c) and c >= 0 for c in (rho, sigma)):
        raise ValueError("The source coefficients must be finite and nonnegative")
    pp = np.eye(p.shape[0])-p
    commutator = m @ p-p @ m
    residue = pp @ m @ p+p @ m @ pp
    return rho*(commutator.conj().T @ commutator)+sigma*(residue.conj().T @ residue)


def native_cyclic_closure(phi, bridge_scale=1.0, rho=0.5, sigma=0.5):
    """CONDITIONAL M mixed block s_M B, not an identification with native M."""
    if not math.isfinite(bridge_scale) or bridge_scale <= 0:
        raise ValueError("A positive finite Millennium bridge scale is required")
    b = cyclic_tensor(phi)
    theta = (2*math.pi+phi)/3
    u = np.roll(np.eye(3), 1, axis=0)
    z = np.exp(1j*theta)/math.sqrt(12)
    bp = (1j*z*u-1j*z.conjugate()*u.T)/3
    zero = np.zeros_like(b)
    m = bridge_scale*np.block([[zero, b.conj().T], [b, zero]])
    p = np.diag([1, 1, 1, 0, 0, 0])
    closure = minimal_native_closure(m, p, rho, sigma)
    qp = bp.conj().T @ b+b.conj().T @ bp
    closure_prime = (rho+sigma)*bridge_scale**2*np.block([[qp, zero], [zero, qp]])
    return m, p, closure, closure_prime


def relaxed_hc(closure, source, penalty=1.0):
    """Unconstrained Hermitian minimizer of lambda||H-L||_F^2+<J,H>."""
    closure, source = (_finite_square(v, n) for v, n in
                       ((closure, "Lambda"), (source, "Energy source")))
    if (closure.shape != source.shape
            or not np.allclose(closure, closure.conj().T, atol=1e-12, rtol=0)
            or not np.allclose(source, source.conj().T, atol=1e-12, rtol=0)
            or not math.isfinite(penalty) or penalty <= 0):
        raise ValueError("Matching Hermitian data and lambda_H > 0 are required")
    h = closure-source/(2*penalty)
    residual = h-closure
    energy = penalty*np.vdot(residual, residual).real+np.vdot(source, h).real
    return h, residual, float(energy)


def native_hc_phase_audit():
    """Explicit substitution, with no historical-mass inputs or selected phase."""
    phi = 0.5
    m, p, closure, closure_prime = native_cyclic_closure(phi)
    source = np.zeros_like(closure)
    h, residual, energy = relaxed_hc(closure, source)
    frozen_curvature = float(2*np.vdot(closure_prime, closure_prime).real)
    hessian_cancellation = float(np.vdot(2*closure_prime, 2*closure_prime).real/2)
    # The static test source is illustrative, not a computed native current.
    j = np.diag([-0.2, -0.3, -0.4, -0.1, -0.2, -0.3])
    _, _, sourced_energy = relaxed_hc(closure, j)
    return {
        "native_identity": "Lambda=(rho+sigma) diag(G*G,F*F) for M=[[A,F],[G,D]]",
        "norm_independent_on_shell_result": "H_C=Lambda implies R=0 and U_HC=0 for every admissible phase",
        "exact_closure_result": "[M,P]=0 implies Lambda=H_C=0 in the minimal source system",
        "conditional_bridge_not_source_identification": "F=s_M B*, G=s_M B; s_M is NOT the field coupling mu",
        "comparison_for_quartic_and_source_checks": "positive finite carrier; Hilbert-Schmidt (Frobenius) matrix norm squared",
        "cyclic_matrix_identity": "B^2=(a^2+2r^2)I+(2ar exp(i theta)+r^2 exp(-2i theta))U+adjoint",
        "affine_cosine_matrix_residual_not_derived": True,
        "trace_B4": "3a^4+36a^2r^2+18r^4+24ar^3 cos(Phi)",
        "normalized_trace_B4_coefficients": {"constant": 17/24, "cos_phi": math.sqrt(2)/6},
        "frozen_isotropic_HC_penalty": "constant+48 lambda_H t^2 a r^3 cos(Phi), t=(rho+sigma)s_M^2",
        "frozen_isotropic_minimum_in_chamber": "zero-root boundary unless t=0, which is phase blind",
        "source_free_relaxation_check": {
            "illustrative_phase_radians": phi,
            "matching_residual_norm": float(np.linalg.norm(residual)),
            "effective_penalty": energy,
            "frozen_H_second_derivative_at_match": frozen_curvature,
            "elimination_Hessian_subtraction": hessian_cancellation,
            "relaxed_second_derivative": frozen_curvature-hessian_cancellation,
            "commutator_norm": float(np.linalg.norm(m @ p-p @ m)),
            "bridge_family_is_not_exactly_closed": True,
            "H_equals_Lambda_is_not_by_itself_exact_closure": True,
            "positive_H_example": bool(np.linalg.eigvalsh(h)[0] >= 0),
        },
        "other_action_terms": {
            "H_variation": "probe bilinear + curvature variation - 2 lambda_H <H-Lambda,delta H> = 0",
            "probe_term": "bar(Psi) (i kappa Gamma.n-gamma) delta H Psi",
            "curvature_term_after_boundary_free_integration": "kappa n_nu Tr[(D_mu^ad F^{mu nu}) delta H]",
            "H_equals_Lambda_requires_other_H_forces_to_cancel": True,
            "full_variational_equivalence_needs_this_additional_condition": True,
        },
        "conditional_static_source_elimination": {
            "hypotheses": "E=lambda_H||H-Lambda||_F^2+<J,H>; J fixed Hermitian; unconstrained or interior H variation",
            "H_star": "Lambda-J/(2 lambda_H)",
            "effective_energy": "<J,Lambda>-||J||_F^2/(4 lambda_H)",
            "isotropic_block_source_has_no_phase_force": True,
            "generation_resolved_phase_force": "-(4t/3) Im[j (ar exp(i theta)-r^2 exp(-2i theta))], j=Tr[(J11+J22)U]",
            "native_state_or_current_not_computed": True,
            "illustrative_source_energy_at_phi_half": sourced_energy,
        },
        "conclusion": "The minimal HC penalty alone does not derive a nontrivial numerical phase or the earlier residual coefficients.",
    }


def _residual_data(r0, r1, metric):
    r0, r1, metric = (np.asarray(value, dtype=complex) for value in (r0, r1, metric))
    if (r0.ndim != 1 or r0.size == 0 or r1.shape != r0.shape
            or not np.all(np.isfinite(r0)) or not np.all(np.isfinite(r1))):
        raise ValueError("Two matching nonempty finite residual vectors are required")
    candidate.positive_metric_root(metric)
    if metric.shape != (r0.size, r0.size):
        raise ValueError("Residual and comparison index spaces must agree")
    return r0, r1, metric


def phase_penalty(phi, r0, r1, metric):
    if not math.isfinite(phi):
        raise ValueError("A finite phase is required")
    r0, r1, metric = _residual_data(r0, r1, metric)
    residual = r0+math.cos(phi)*r1
    value = float(np.vdot(residual, metric @ residual).real)
    if not math.isfinite(value):
        raise ValueError("The residual penalty must remain finite")
    return value


def phase_penalty_selection(r0, r1, metric):
    """Constrained minimizer for R=R0+cos(Phi) R1, constant positive G only."""
    r0, r1, metric = _residual_data(r0, r1, metric)
    if not np.any(r1):
        return {"status": "phase_blind", "phase_radians": None,
                "unconstrained_cosine": None, "selected_cosine": None,
                "minimum_penalty": phase_penalty(0, r0, r1, metric)}
    denominator = float(np.vdot(r1, metric @ r1).real)
    numerator = float(np.vdot(r1, metric @ r0).real)
    if not math.isfinite(denominator) or denominator <= 0 or not math.isfinite(numerator):
        raise ValueError("A finite strictly positive phase-channel norm is required")
    unconstrained = -numerator/denominator
    if not math.isfinite(unconstrained):
        raise ValueError("The residual projection must remain finite")
    cosine = min(1.0, max(LOWER_COS, unconstrained))
    phi = math.acos(cosine)
    if unconstrained <= LOWER_COS:
        status = "zero_root_boundary"
    elif unconstrained >= 1:
        status = "two_equal_roots"
    else:
        status = "stable_interior_conditional"
    return {
        "status": status, "phase_radians": phi,
        "conjugate_phase_radians": -phi,
        "theta_positive_branch_radians": (2*math.pi+phi)/3,
        "unconstrained_cosine": unconstrained, "selected_cosine": cosine,
        "minimum_penalty": phase_penalty(phi, r0, r1, metric),
        "interior_phase_curvature": 2*denominator*math.sin(phi)**2
            if status == "stable_interior_conditional" else None,
        "first_harmonic_coefficient": 2*numerator,
        "second_harmonic_coefficient": denominator/2,
    }


def penalty_derivative(residual, residual_prime, metric, metric_prime=None):
    """Full derivative of R*G R, including an independently supplied G'."""
    residual, residual_prime, metric = _residual_data(residual, residual_prime, metric)
    if metric_prime is None:
        metric_prime = np.zeros_like(metric)
    metric_prime = np.asarray(metric_prime, dtype=complex)
    if (metric_prime.shape != metric.shape or not np.all(np.isfinite(metric_prime))
            or not np.allclose(metric_prime, metric_prime.conj().T, atol=1e-12, rtol=1e-12)):
        raise ValueError("The metric variation must be a compatible finite Hermitian matrix")
    return float((2*np.vdot(residual_prime, metric @ residual).real
                  + np.vdot(residual, metric_prime @ residual).real))


def stable_two_harmonic_phase(lambda1, lambda2):
    """Interior minimum on the positive-root chamber; coefficients are INPUTS."""
    if not math.isfinite(lambda1) or not math.isfinite(lambda2) or lambda2 <= 0:
        raise ValueError("Finite coefficients and lambda2 > 0 are required")
    scale = max(abs(lambda1), abs(lambda2))
    l1, l2 = lambda1/scale, lambda2/scale
    if l2 <= 0:
        raise ValueError("No strict interior minimum in the positive-root chamber")
    cosine = -l1/(4*l2)
    if not LOWER_COS < cosine < 1:
        raise ValueError("No strict interior minimum in the positive-root chamber")
    return math.acos(cosine)


def trace_harmonics(power, samples=64):
    """Global algebraic trace family, not positive-root physics at all samples."""
    if not isinstance(power, int) or power < 1 or power > 6:
        raise ValueError("This diagnostic covers integer powers 1 through 6")
    if not isinstance(samples, int) or samples < 16:
        raise ValueError("At least 16 uniform samples are required")
    phases = 2*math.pi*np.arange(samples)/samples
    values = np.array([np.trace(np.linalg.matrix_power(cyclic_tensor(phi), power)).real
                       for phi in phases])
    fourier = np.fft.rfft(values)/samples
    return {"constant": float(fourier[0].real),
            "cos_phi": float(2*fourier[1].real),
            "cos_2phi": float(2*fourier[2].real),
            "max_sine_or_higher_harmonic": float(max(
                np.max(np.abs(2*fourier[1:3].imag)), np.max(np.abs(2*fourier[3:]))))}


def trimer_ground_state_check():
    """One-excitation trimer energy, not a QFT vacuum or a lepton mass action."""
    a1, a2, d, c, w1, w2 = 0.5, 0.9, 3.0, 0.2, 0.15, 0.12
    def matrix(phi):
        link = w2*np.exp(1j*phi)
        return np.array([[a1, c, w1], [c, a2, link.conjugate()], [w1, link, d]])
    phi = 0.4
    energies, vectors = np.linalg.eigh(matrix(phi))
    derivative = np.zeros((3, 3), dtype=complex)
    derivative[2, 1] = 1j*w2*np.exp(1j*phi)
    derivative[1, 2] = derivative[2, 1].conjugate()
    analytic = -2*abs(c*w1*w2)*math.sin(phi)/np.prod(energies[0]-energies[1:])
    direct = np.vdot(vectors[:, 0], derivative @ vectors[:, 0]).real
    return {
        "scope": "fixed scalar link moduli, simple lowest one-excitation level",
        "analytic_ground_energy_derivative": float(analytic),
        "full_matrix_derivative": float(direct),
        "minimum_loop_phase_mod_2pi": math.pi,
        "endpoint_low_energies": [float(np.linalg.eigvalsh(matrix(p))[0]) for p in (0, math.pi)],
        "not_the_native_quantum_vacuum": True,
    }


def evaluate():
    theta = candidate.cyclic_candidate()[0]
    target_theta = candidate.matrix_diagnosis()["benchmark_phase_radians"]
    phi, target_phi = 3*theta-2*math.pi, 3*target_theta-2*math.pi
    ratio, target_ratio = -4*math.cos(phi), -4*math.cos(target_phi)
    demo = phase_penalty_selection([-0.8, 0.2], [1, 0], np.eye(2))
    return {
        "status": "explicit minimal-HC substitution and conditional selection rules; no native numerical phase prediction",
        "explicit_minimal_HC_audit": native_hc_phase_audit(),
        "source_action_audit": {
            "source": "sources/research/parts/v470/10_sphaera_and_physics.tex",
            "label": "thm:variational-form",
            "explicit_tensor_term": "-bar(Psi) c_T T Psi",
            "HC_penalty": "lambda_H ||H_C-Lambda[M,P]||^2",
            "T_as_external_operator_has_no_independent_Euler_Lagrange_equation": True,
            "T_as_free_multiplier_gives_bilinear_constraint_not_T_value": True,
            "fixed_other_fields_zero_probe_action_is_phase_independent": True,
            "could_be_closed_by_T_as_evaluated_function_of_existing_fields": True,
            "no_claim_about_complete_quantum_effective_action": True,
        },
        "spectral_invariants": {
            "assumptions": "fixed Hermitian cyclic family, radius a/sqrt(2), no extra generation spurion",
            "determinant": "a^3-3*a*r^2+2*r^3*cos(Phi)",
            "positive_root_chamber_Phi": [-math.pi/4, math.pi/4],
            "trace_harmonics": {str(n): trace_harmonics(n) for n in range(1, 7)},
            "first_nonlinear_phase_spectral_polynomial_degree": 6,
            "not_a_universal_bound_with_extra_generation_tensors": True,
        },
        "HC_penalty_selection_rule": {
            "general_derivative": "U'=lambda_H [2 Re(R'* G R)+R* G' R]",
            "extra_reduction_assumptions": "R=R0+cos(Phi)R1; constant positive G; lambda_H>0; other phase forces vanish",
            "cosine_stationary": "-Re(R1* G R0)/(R1* G R1)",
            "native_R0_R1_and_G_not_extracted": True,
            "minimal_native_residual_vanishes_when_H_matches_Lambda": True,
            "two_harmonic_equivalent": "lambda1=2 lambda_H Re(R1*G R0); lambda2=lambda_H(R1*G R1)/2",
            "unfitted_illustrative_residual_selection": demo,
        },
        "two_harmonic_completion": {
            "formula": "V=lambda1*cos(Phi)+lambda2*cos(2*Phi)",
            "stationary_rule": "cos(Phi)=-lambda1/(4*lambda2)",
            "interior_positive_chamber_ratio_interval": [-4, -2*math.sqrt(2)],
            "lambda2_must_be_positive": True,
            "is_not_already_a_source_potential": True,
        },
        "historical_target_condition_not_prediction": {
            "baseline_assumed_phase_radians": phi,
            "benchmark_inverted_phase_radians": target_phi,
            "baseline_equivalent_lambda1_over_lambda2": ratio,
            "benchmark_required_lambda1_over_lambda2": target_ratio,
            "relative_ratio_shift": target_ratio/ratio-1,
            "required_residual_projection_cosine": math.cos(target_phi),
            "target_phase_curvature_per_lambda2": 4*math.sin(target_phi)**2,
            "masses_enter_only_this_diagnostic_not_selection_functions": True,
        },
        "minimal_trimer_ground_energy_test": trimer_ground_state_check(),
        "scale_boundary": {
            "mu_product": "sqrt(2)*abs(chi)*||T_perp1||_F under the previous canonical equal-leg assumptions",
            "phase_selection_alone_does_not_fix_mu_or_Delta": True,
            "radius_and_generation_embedding_still_assumed": True,
        },
        "remaining_native_derivation": [
            "derive the generation tensor from existing carrier/field data, or give its dynamics",
            "evaluate the non-penalty probe/curvature forces; the minimal matching residual alone is zero on shell",
            "retain other phase-dependent forces and metric derivatives in the full stationarity equation",
            "fix radial/kinetic and gap/scale data independently of historical masses",
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
