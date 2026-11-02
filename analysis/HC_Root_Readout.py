"""Explicit HC/root-map tests and a conditional quadratic readout, not native masses."""
import argparse
import importlib.util
import json
import math
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "root_backreaction", Path(__file__).with_name("HC_Source_Backreaction.py"))
backreaction = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(backreaction)
U = backreaction.U
E0 = np.eye(3)/math.sqrt(3)
E1 = (U+U.T)/math.sqrt(6)
E2 = 1j*(U-U.T)/math.sqrt(6)
FOURIER = np.exp(-2j*math.pi*np.outer(np.arange(3), np.arange(3))/3)/math.sqrt(3)
SIGMA_Z = np.diag([1, -1])
SIGMA_X = np.array([[0, 1], [1, 0]])
FULL_CONE_WEIGHT_BOUND = 1/math.sqrt(2)


def _two_mode(value):
    value = np.asarray(value, dtype=complex)
    if value.shape != (2,) or not np.all(np.isfinite(value)):
        raise ValueError("Two finite dimensionless internal mode amplitudes required")
    return value


def _mode_frame(frame):
    frame = np.eye(2) if frame is None else np.asarray(frame, dtype=complex)
    if (frame.shape != (2, 2) or not np.all(np.isfinite(frame))
            or not np.allclose(frame.conj().T @ frame, np.eye(2), atol=1e-12, rtol=0)):
        raise ValueError("A unitary two-mode frame required")
    return frame


def antiunitary_reversal(state, frame=None):
    """Declared J=V K V*, not an identification of the native convention."""
    state, frame = _two_mode(state), _mode_frame(frame)
    return frame @ (frame.conj().T @ state).conjugate()


def odd_residual(state, frame=None):
    state = _two_mode(state)
    return (state-antiunitary_reversal(state, frame))/2


def quadratic_coordinates(state, frame=None):
    """Real Pauli-type bilinears in a specified INTERNAL two-mode frame."""
    local = _mode_frame(frame).conj().T @ _two_mode(state)
    u, v = local
    cross = u.conjugate()*v
    values = np.array([abs(u)**2+abs(v)**2, abs(u)**2-abs(v)**2,
                       2*cross.real, 2*cross.imag])
    if not np.all(np.isfinite(values)):
        raise ValueError("The quadratic mode coordinates must remain finite")
    return values


def _readout_weight(weight):
    if not math.isfinite(weight) or weight < 0:
        raise ValueError("A nonnegative finite relative readout weight required")
    return weight


def quadratic_root(state, weight=1.0, frame=None):
    """Candidate L=X0 E0+eta X1 E1+eta X2 E2; positivity is NOT automatic."""
    weight = _readout_weight(weight)
    x0, x1, x2, _ = quadratic_coordinates(state, frame)
    return x0*E0+weight*(x1*E1+x2*E2)


def density_root(density, weight=1.0):
    """Same readout, extended linearly to positive two-mode matrices, not a new mass law."""
    weight = _readout_weight(weight)
    density = backreaction._hermitian(density, "Internal two-mode density")
    if density.shape != (2, 2) or np.linalg.eigvalsh(density)[0] < -1e-12:
        raise ValueError("A positive two-mode matrix required")
    x0 = float(np.trace(density).real)
    x1 = float(np.trace(SIGMA_Z @ density).real)
    x2 = float(np.trace(SIGMA_X @ density).real)
    return x0*E0+weight*(x1*E1+x2*E2)


def normalized_root_forms(weight=1.0):
    """Sum-to-identity forms; positive effects only if eta<=1/sqrt(2).

    In the fixed Fourier order, eigenvalue_k(L)=sqrt(3) Tr(F_k density).
    Their normalization is algebraic, not a native probability interpretation.
    """
    weight = _readout_weight(weight)
    angles = 2*math.pi*np.arange(3)/3
    return np.array([(np.eye(2)+math.sqrt(2)*weight*(
        math.cos(angle)*SIGMA_Z-math.sin(angle)*SIGMA_X))/3 for angle in angles])


def aligned_root_eigenvalues(theta, weight=1.0):
    """Signed Fourier-ordered roots for a unit-norm aligned odd mode, not sorted."""
    weight = _readout_weight(weight)
    if not math.isfinite(theta):
        raise ValueError("A finite internal coefficient angle required")
    angles = theta+2*math.pi*np.arange(3)/3
    return (1+math.sqrt(2)*weight*np.cos(angles))/math.sqrt(3)


def aligned_chamber_half_width(weight=1.0):
    """Allowed half-width around 2 pi k/3; None means no positive pure odd mode.

    At eta<=1/sqrt(2) the intervals cover the full circle. At eta=sqrt(2)
    only the three centers remain. This is a cone test, not a native selector.
    """
    weight = _readout_weight(weight)
    if weight <= FULL_CONE_WEIGHT_BOUND:
        return math.pi/3
    if weight > math.sqrt(2):
        return None
    return max(0.0, math.acos(-1/(math.sqrt(2)*weight))-2*math.pi/3)


def root_diagnostic(root):
    root = backreaction._hermitian(root, "Principal mass-root candidate")
    if root.shape != (3, 3) or np.linalg.eigvalsh(root)[0] < -1e-12:
        raise ValueError("Three nonnegative principal roots required; signed roots are not admissible")
    trace = float(np.trace(root).real)
    norm_squared = float(np.vdot(root, root).real)
    if not math.isfinite(norm_squared):
        raise ValueError("The root comparison must remain finite")
    singlet = trace*np.eye(3)/3
    traceless = root-singlet
    return {
        "root_eigenvalues": np.linalg.eigvalsh(root).tolist(),
        "root_trace": trace,
        "gram_trace": norm_squared,
        "singlet_norm_squared": float(np.vdot(singlet, singlet).real),
        "traceless_norm_squared": float(np.vdot(traceless, traceless).real),
        "Koide_ratio": norm_squared/trace**2 if trace > 0 else None,
        "balance_difference": float(np.vdot(traceless, traceless).real-np.vdot(singlet, singlet).real),
    }


def transition_root(transition):
    """The nonlinear root map for the previously declared Gram mass-law candidate."""
    transition = np.asarray(transition, dtype=complex)
    if (transition.ndim != 2 or transition.shape[0] == 0 or transition.shape[1] != 3
            or not np.all(np.isfinite(transition))):
        raise ValueError("A finite transition with three generation inputs required")
    return backreaction.positive_root(transition.conj().T @ transition)


def balanced_hc_clock_witness(gram):
    """Fixed M,P,J,S and fixed simple clock spectrum; Q still varies.

    This is a finite countermodel to sufficiency, NOT the native Riemann clock.
    """
    gram = backreaction._hermitian(gram, "Cyclic Gram contraction")
    if (gram.shape != (3, 3) or np.linalg.eigvalsh(gram)[0] < -1e-12
            or np.linalg.eigvalsh(gram)[-1] > 1+1e-12
            or not np.allclose(gram @ U, U @ gram, atol=1e-12, rtol=0)):
        raise ValueError("A cyclic three-mode positive contraction required")
    values = np.clip(np.diag(FOURIER.conj().T @ gram @ FOURIER).real, 0, 1)
    high, low, dark = np.array([4, 6, 8]), np.array([1, 2, 3]), np.array([10, 11, 12])
    angles = np.arcsin(2*np.sqrt(values)/(high-low))/2
    def mode_matrix(diagonal):
        return (FOURIER*diagonal) @ FOURIER.conj().T
    identity, zero = np.eye(3), np.zeros((3, 3))
    cosine, sine = mode_matrix(np.cos(angles)), mode_matrix(np.sin(angles))
    rotation = np.block([[cosine, -sine, zero], [sine, cosine, zero], [zero, zero, identity]])
    spectrum = np.block([[mode_matrix(high), zero, zero],
                         [zero, mode_matrix(low), zero], [zero, zero, mode_matrix(dark)]])
    split = np.block([[identity, zero, zero],
                      [zero, identity/math.sqrt(2), identity/math.sqrt(2)],
                      [zero, identity/math.sqrt(2), -identity/math.sqrt(2)]])
    clock = split @ rotation @ spectrum @ rotation.conj().T @ split.conj().T
    projector = np.diag([1]*3+[0]*6)
    embedding = np.eye(9)[:, :3]
    reversal = np.diag([-1]*3+[1]*3+[-1]*3)
    compensator = (np.eye(9)+reversal)/2
    millennium = compensator+3*(np.eye(9)-compensator)
    transition = (np.eye(9)-projector) @ clock @ embedding
    return {"P": projector, "S": embedding, "J": reversal, "C": compensator,
            "M": millennium, "R": clock, "A": transition}


def evaluate():
    theta = 2.25  # Admitted illustrative angle, not a historical mass inversion.
    state = 1j*np.array([math.cos(theta/2), math.sin(theta/2)])
    residual = odd_residual(state)
    root = quadratic_root(residual)
    weights = []
    for weight in [0.0, 0.5, 1.0]:
        candidate = quadratic_root(residual, weight)
        diagnostic = root_diagnostic(candidate)
        q = candidate @ candidate/diagnostic["gram_trace"]
        witness = balanced_hc_clock_witness(q)
        a, c, j = witness["A"], witness["C"], witness["J"]
        weights.append({
            "input_readout_weight": weight,
            "Koide_ratio": diagnostic["Koide_ratio"],
            "same_M_P_J_C_and_closed_odd_seeds": True,
            "equal_HC_channel_Gram_error": float(np.linalg.norm(a.conj().T @ c @ a-q/2)),
            "HC_null_transition_error": float(np.linalg.norm(a.conj().T @ j @ a)),
            "clock_spectrum": np.linalg.eigvalsh(witness["R"]).tolist(),
        })
    rotated_frame = np.diag([1, 1j])
    rotated_state = rotated_frame @ state
    aligned = quadratic_root(odd_residual(rotated_state, rotated_frame), frame=rotated_frame)
    misaligned = quadratic_root(odd_residual(rotated_state, rotated_frame))
    full_cone_examples = []
    for weight in [0.0, FULL_CONE_WEIGHT_BOUND, 1.0]:
        full_cone_examples.append({
            "relative_weight": weight,
            "form_eigenvalues": np.linalg.eigvalsh(normalized_root_forms(weight)).tolist(),
            "all_positive_two_mode_inputs_have_positive_roots": weight <= FULL_CONE_WEIGHT_BOUND,
            "aligned_pure_ratio_on_admitted_branch": (1+weight**2)/3,
        })
    left = 1j*np.array([0.5, math.sqrt(3)/2])
    right = 1j*np.array([-0.5, math.sqrt(3)/2])
    mixed = np.outer(left, left.conj())+np.outer(right, right.conj())
    half_width = aligned_chamber_half_width()
    return {
        "status": "explicit conditional HC/root identification test; no native mass law or radius prediction",
        "source_dictionary": {
            "fragment": "sources/research/parts/v470/10_sphaera_and_physics.tex",
            "labels": ["sec:central", "thm:three-generations", "thm:hopf", "thm:gauge-invariance"],
            "unitary_and_antiunitary_J_conventions_are_not_identified": True,
            "native_two_mode_extraction_and_readout_metric_not_evaluated": True,
        },
        "actual_root_readout_candidate": {
            "transition": "A=(I-P) R_tilde S",
            "principal_root": "L=sqrt(A* A)",
            "candidate_physical_roots": "sqrt(kappa) eig(L), conditional on M_mass=kappa A*A",
            "nonlinear_and_spectral_not_linear_HC_output": True,
            "native_J_on_transition_output_is_lost_by_Gram": "L(J A)=L(A) for unitary J",
        },
        "strong_balance_countermodels": {
            "hypotheses": "positive carrier, fixed complex-linear orthogonal J, C=(I+J)/2, exact Millennium closure, cyclic R",
            "C_is_exact_M_spectral_projector": "M=C+3(I-C), eigenvalue 1 only on im(C)",
            "all_seedwise_HC_channel_norms_equal": "A* C A=A*(I-C)A=Q/2; A*J A=0",
            "clock_scope": "fixed finite simple self-adjoint spectrum, not native Riemann zero data or a full field solution",
            "examples": weights,
            "channel_balance_does_not_imply_root_singlet_doublet_balance": True,
        },
        "quadratic_two_mode_candidate": {
            "input": "dimensionless INTERNAL chi=(u,v), not identified with the physical spin of a lepton",
            "coordinates": "X0=|u|^2+|v|^2; X1=|u|^2-|v|^2; X2=2Re(conj(u)v); X3=2Im(conj(u)v)",
            "identity": "X0^2=X1^2+X2^2+X3^2",
            "root_operator": "L_eta=X0 E0+eta X1 E1+eta X2 E2",
            "basis": "E0=I/sqrt(3), E1=(U+U*)/sqrt(6), E2=i(U-U*)/sqrt(6)",
            "physical_ratio_only_if_L_is_nonzero_positive": "K=[1+eta^2(1-(X3/X0)^2)]/3",
            "antiunitary_odd_condition_in_aligned_basis": "J=conjugation, J chi=-chi implies X3=0",
            "reduced_ratio": "K=(1+eta^2)/3",
            "Koide_requires_independent_isometric_readout_eta_one": True,
            "norm_isometry_is_not_proved_by_HC_idempotence": True,
            "illustrative_angle_radians_not_predicted": theta,
            "example": root_diagnostic(root),
        },
        "alignment_and_state_cone_checks": {
            "rotated_odd_state_with_fixed_readout_K": root_diagnostic(misaligned)["Koide_ratio"],
            "rotated_odd_state_with_cotransported_readout_K": root_diagnostic(aligned)["Koide_ratio"],
            "state_only_global_phase_at_fixed_J_can_annihilate_residual": float(np.linalg.norm(odd_residual(1j*state))),
            "only_joint_frame_covariance_was_checked_not_a_native_local_gauge_theory": True,
            "some_odd_states_give_negative_signed_roots_and_are_not_admissible": True,
            "raw_quadratic_map_is_degree_two_and_mass_Gram_degree_four": True,
            "internal_background_vs_probe_amplitude_role_remains_to_be_identified": True,
        },
        "comparison_tensor_freedom": {
            "native_definition": "def:two-sided-admissible-contractions requires a declared comparison, not its numerical weights",
            "shift_contract": "def:v3370-readout-package-translation preserves the declared comparison tensor",
            "even_assuming_coefficient_plane_C3_symmetry": "G=diag(g_s,g_d,g_d), with independent g_s,g_d>0",
            "not_cycle_conjugation_on_circulants": "U L U*=L acts trivially and is not the coefficient-plane rotation",
            "pullback_of_fixed_Hilbert_Schmidt_comparison": "diag(1,eta^2,eta^2)",
            "declaring_the_pullback_metric_is_not_a_prediction_of_eta": True,
            "commuting_readout_is_not_a_Clifford_algebra_embedding": True,
        },
        "full_cone_positivity_obstruction": {
            "scope": "this linear-in-density quadratic-amplitude candidate, not every nonlinear native mass law",
            "signed_root_forms": "F_k=[I+sqrt(2)eta(cos(phi_k)sigma_z-sin(phi_k)sigma_x)]/3; phi_k=2pi k/3",
            "root_eigenvalue_identity": "ell_k=sqrt(3)Tr(F_k rho); sum_k F_k=I",
            "form_eigenvalues": "(1-sqrt(2)eta)/3 and (1+sqrt(2)eta)/3",
            "all_input_positivity_iff": "0<=eta<=1/sqrt(2), including all aligned odd inputs",
            "max_relative_weight": FULL_CONE_WEIGHT_BOUND,
            "max_Koide_ratio_for_this_globally_positive_family": 0.5,
            "isometric_eta_one_is_outside_this_bound": True,
            "examples": full_cone_examples,
            "negative_odd_witness_at_eta_one": {
                "state": "chi=(0,i)",
                "minimum_signed_root": float(np.linalg.eigvalsh(quadratic_root([0, 1j]))[0]),
                "absolute_root_repair_K": root_diagnostic(transition_root(quadratic_root([0, 1j])))["Koide_ratio"],
            },
        },
        "restricted_isometric_cone": {
            "aligned_angle": "chi=i(cos(theta/2),sin(theta/2))",
            "allowed_angles": "theta=2pi k/3+delta modulo 2pi; |delta|<=pi/12",
            "half_width_radians": half_width,
            "fraction_of_coefficient_angle_circle": 3*half_width/math.pi,
            "this_geometric_fraction_is_not_a_physical_probability": True,
            "coherent_superposition_is_not_closed": {
                "two_admitted_states": "i(1/2,sqrt(3)/2) and i(-1/2,sqrt(3)/2)",
                "input_minimum_roots": [float(np.linalg.eigvalsh(quadratic_root(s))[0]) for s in [left, right]],
                "sum_minimum_root": float(np.linalg.eigvalsh(quadratic_root(left+right))[0]),
                "incoherent_density_sum_minimum_root": float(np.linalg.eigvalsh(density_root(mixed))[0]),
            },
            "constant_nonzero_angular_drift_preserves_chambers": False,
            "autonomous_angle_flow_boundary_guard": "theta_dot=f(theta): f(left)>=0 and f(right)<=0 at each chamber edge",
            "passive_joint_frame_covariance_does_not_select_eta_or_an_active_phase_flow": True,
            "native_domain_and_invariance_not_derived": True,
        },
        "remaining_native_identification": [
            "construct a specified two-mode extraction from the native carrier and resolve the J convention",
            "prove its reversal/readout-frame alignment independently of the masses",
            "derive the singlet/doublet metric transfer eta=1 AND a physically admitted restricted cone, or replace this candidate map",
            "derive the native equality A*A=L_eta^2, or a physical alternative mass readout",
            "prove the admitted principal-root cone, gauge covariance and physical background/state role",
            "derive phase and scale; the quadratic construction alone fixes neither",
        ],
        "historical_masses_or_target_phase_used": False,
        "main_TeX_changed": False,
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
