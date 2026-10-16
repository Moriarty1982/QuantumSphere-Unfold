"""Conditional null-axis curvature/action checks, not a native stability or mass proof."""
import argparse
import json
import math
from pathlib import Path

import numpy as np


METRIC = np.diag([-1.0, 1.0, 1.0, 1.0])
NULL_COVECTOR = np.array([-1.0, 0.0, 0.0, 1.0])


def _finite(value, name):
    value = np.asarray(value, dtype=complex)
    if not np.all(np.isfinite(value)):
        raise ValueError(f"Finite {name} required")
    return value


def _real(value, shape, name):
    value = _finite(value, name)
    if value.shape != shape or np.any(np.abs(value.imag) > 1e-12):
        raise ValueError(f"Real {name} of shape {shape} required")
    return value.real


def _scalar(value, name):
    return float(_real(value, (), name))


def _generator(value):
    value = _finite(value, "internal generator")
    if (value.ndim != 2 or value.shape[0] == 0 or value.shape[0] != value.shape[1]
            or not np.allclose(value, value.conj().T, atol=1e-12, rtol=0)):
        raise ValueError("A finite square Hermitian internal generator required")
    return value


def _curvature(value):
    value = _finite(value, "curvature")
    if (value.ndim != 4 or value.shape[:2] != (4, 4) or value.shape[2] == 0
            or value.shape[2] != value.shape[3]
            or not np.allclose(value, -value.swapaxes(0, 1), atol=1e-12, rtol=0)):
        raise ValueError("An antisymmetric (4,4,N,N) curvature required")
    return value


def connection_curvature(connection, derivative):
    """F_mu_nu for a general matrix connection; derivative[mu,nu]=partial_mu B_nu."""
    connection = _finite(connection, "connection")
    if (connection.ndim != 3 or connection.shape[0] != 4 or connection.shape[1] == 0
            or connection.shape[1] != connection.shape[2]):
        raise ValueError("A (4,N,N) matrix connection required")
    derivative = _finite(derivative, "connection derivative")
    if derivative.shape != (4, *connection.shape):
        raise ValueError("A (4,4,N,N) connection derivative required")
    products = connection[:, None] @ connection[None, :]
    return derivative-derivative.swapaxes(0, 1)+products-products.swapaxes(0, 1)


def null_axis_curvature(gradient, n_covector, generator, coupling):
    """Fixed T,n and commuting backgrounds; H_C=h T, not an arbitrary native profile."""
    gradient = _real(gradient, (4,), "covariant scalar gradient")
    n = _real(n_covector, (4,), "axis covector")
    generator, coupling = _generator(generator), _scalar(coupling, "coupling")
    wedge = np.outer(gradient, n)-np.outer(n, gradient)
    return coupling*wedge[:, :, None, None]*generator


def curvature_lagrangian(curvature, pairing="literal"):
    """Return complex L; taking Re and using the dagger pairing are distinct choices."""
    curvature = _curvature(curvature)
    raised = np.einsum("ma,nb,abij->mnij", METRIC, METRIC, curvature)
    if pairing == "literal":
        left = curvature
    elif pairing == "dagger_comparison":
        left = curvature.conj().swapaxes(-1, -2)
    else:
        raise ValueError("Pairing must be literal or dagger_comparison")
    return complex(-np.einsum("mnij,mnji->", left, raised)/4)


def scalar_kinetic_tensor(n_covector, generator, coupling):
    n = _real(n_covector, (4,), "axis covector")
    generator, coupling = _generator(generator), _scalar(coupling, "coupling")
    n_up = METRIC @ n
    trace_t_squared = float(np.trace(generator @ generator).real)
    return coupling**2*trace_t_squared*(np.outer(n_up, n_up)-(n @ n_up)*METRIC)


def scalar_lagrangian(gradient, n_covector, generator, coupling):
    gradient = _real(gradient, (4,), "covariant scalar gradient")
    kinetic = scalar_kinetic_tensor(n_covector, generator, coupling)
    return float(gradient @ kinetic @ gradient/2)


def _symmetric_derivative(value, order):
    value = _real(value, (4,)*order, "scalar derivative tensor")
    for axis in range(1, order):
        if not np.allclose(value, value.swapaxes(0, axis), atol=1e-12, rtol=0):
            raise ValueError("Symmetric derivatives of a smooth scalar required")
    return value


def abelian_residual(hessian, n_covector, generator, coupling):
    """E_nu=partial^mu F_mu_nu, not a proof that native currents vanish."""
    hessian = _symmetric_derivative(hessian, 2)
    n = _real(n_covector, (4,), "axis covector")
    generator, coupling = _generator(generator), _scalar(coupling, "coupling")
    wave_operator = float(np.einsum("ab,ab", METRIC, hessian))
    components = n*wave_operator-hessian @ (METRIC @ n)
    return coupling*components[:, None, None]*generator


def abelian_residual_derivative(third_derivative, n_covector, generator, coupling):
    third = _symmetric_derivative(third_derivative, 3)
    n = _real(n_covector, (4,), "axis covector")
    generator, coupling = _generator(generator), _scalar(coupling, "coupling")
    components = (np.einsum("n,ab,dab->dn", n, METRIC, third)
                  -np.einsum("a,dna->dn", METRIC @ n, third))
    return coupling*components[:, :, None, None]*generator


def scalar_el(hessian, n_covector, generator, coupling):
    """EL=partial L/partial h-partial_mu(partial L/partial h_mu); curvature only."""
    hessian = _symmetric_derivative(hessian, 2)
    return float(-np.einsum("ab,ab", scalar_kinetic_tensor(n_covector, generator, coupling), hessian))


def constant_paired_field_equations(gauge, hc, n_covector, coupling):
    """Alternative dagger action only: constant Hermitian A,H; no sources or penalties."""
    hc = _generator(hc)
    gauge = _finite(gauge, "gauge field")
    if (gauge.shape != (4, *hc.shape)
            or not np.allclose(gauge, gauge.conj().swapaxes(-1, -2), atol=1e-12, rtol=0)):
        raise ValueError("Four Hermitian gauge matrices on the compensator carrier required")
    n, coupling = _real(n_covector, (4,), "axis covector"), _scalar(coupling, "coupling")
    products = gauge[:, None] @ gauge[None, :]
    f_a = 1j*(products-products.swapaxes(0, 1))
    dh = 1j*(gauge @ hc-hc @ gauge)
    x = dh[:, None]*n[None, :, None, None]-n[:, None, None, None]*dh[None, :]
    f_up = np.einsum("ma,nb,abij->mnij", METRIC, METRIC, f_a)
    x_up = np.einsum("ma,nb,abij->mnij", METRIC, METRIC, x)
    a_el = 1j*np.sum(gauge[:, None] @ f_up-f_up @ gauge[:, None], axis=0)
    a_el += 1j*coupling**2*np.einsum("m,mnij->nij", n, hc @ x_up-x_up @ hc)
    h_el = 1j*coupling**2*np.einsum("n,mnij->ij", n, gauge[:, None] @ x_up-x_up @ gauge[:, None])
    curvature = 1j*f_a+coupling*x
    return {"L": curvature_lagrangian(curvature, "dagger_comparison").real,
            "gauge_EL": a_el, "hc_EL": h_el, "curvature": curvature}


def null_wave_profile(time, position_z, wavenumber=1.0, offset=0.0):
    """h=offset+t cos(k(z-t)); a smooth restricted-equation witness, not a solution."""
    time, z, k, offset = [_scalar(value, "profile parameter")
                          for value in [time, position_z, wavenumber, offset]]
    s = k*(z-time)
    q, e0 = np.array([-k, 0.0, 0.0, k]), np.eye(4)[0]
    cosine, sine = math.cos(s), math.sin(s)
    gradient = e0*cosine-time*sine*q
    hessian = -sine*(np.outer(e0, q)+np.outer(q, e0))-time*cosine*np.outer(q, q)
    third = -cosine*(np.einsum("d,n,a->dna", e0, q, q)
                     +np.einsum("d,n,a->dna", q, e0, q)
                     +np.einsum("d,n,a->dna", q, q, e0))
    third += time*sine*np.einsum("d,n,a->dna", q, q, q)
    return {"value": offset+time*cosine, "gradient": gradient,
            "hessian": hessian, "third_derivative": third}


def evaluate():
    n, generator, coupling = NULL_COVECTOR, np.diag([1.0, 2.0]), 0.4
    trace_t_squared = float(np.trace(generator @ generator).real)
    kinetic = scalar_kinetic_tensor(n, generator, coupling)
    electric = null_axis_curvature([1, 0, 0, 0], n, generator, coupling)
    profile = null_wave_profile(0.7, 0.4, 1.3, 2.0)
    residual = abelian_residual(profile["hessian"], n, generator, coupling)
    residual_derivative = abelian_residual_derivative(profile["third_derivative"], n, generator, coupling)
    identity = np.einsum("dn,dnij->ij", METRIC, residual_derivative)
    tangent = coupling*np.einsum("n,ij,nji->", METRIC @ n, generator, residual)
    return {
        "status": "conditional curvature pullback, rank and real-form audit; no full native solution",
        "native_anchor": {
            "source": "v470/10_sphaera_and_physics.tex, thm:variational-form and thm:resonance-field-eq",
            "connection": "D_mu=partial_mu+i A_mu+kappa H_C n_mu+eta (I-P_C7)n_mu",
            "literal_curvature_action": "-Tr(F_mu_nu F^mu_nu)/4; no dagger printed",
            "signature_used": "(-,+,+,+)",
            "native_internal_adjoint_real_form_and_current_representation_not_fixed_here": True,
        },
        "commuting_compensator_branch": {
            "assumptions": "flat fixed metric, constant n and Hermitian T, H_C=h T, A=0, constant commuting closure background",
            "curvature": "F_mu_nu=kappa T (n_nu partial_mu h-n_mu partial_nu h)",
            "L": "-kappa^2 Tr(T^2) [n^2 (partial h)^2-(n.partial h)^2]/2",
            "null_limit": "L=kappa^2 Tr(T^2) (n.partial h)^2/2",
            "principal_tensor": "K^{mu nu}=kappa^2 Tr(T^2)(n^mu n^nu-n^2 g^{mu nu})",
            "example_coupling_not_a_native_value": coupling,
            "example_ordinary_trace_T_squared": trace_t_squared,
            "kinetic_tensor": kinetic.tolist(),
            "null_tensor_rank": int(np.linalg.matrix_rank(kinetic)),
            "null_tensor_eigenvalues": np.linalg.eigvalsh(kinetic).tolist(),
            "homogeneous_time_inertia": float(kinetic[0, 0]),
            "homogeneous_inertia_does_not_prove_full_wave_stability": True,
            "no_irreversible_viscosity_derived": True,
        },
        "mixed_reality_diagnostic": {
            "assumptions": "ordinary trace, real couplings, Hermitian A_mu and H_C, real part of the literal action",
            "decomposition": "F=i F_A+kappa X; F_A and X Hermitian in internal indices",
            "real_action": "Re L=Tr(F_A_mu_nu F_A^mu_nu)/4-kappa^2 Tr(X_mu_nu X^mu_nu)/4",
            "same_electric_profile_Re_L_gauge": curvature_lagrangian(1j*electric).real,
            "same_electric_profile_Re_L_compensator": curvature_lagrangian(electric).real,
            "simultaneous_literal_L_real": curvature_lagrangian((1+1j)*electric).real,
            "simultaneous_literal_L_imaginary": curvature_lagrangian((1+1j)*electric).imag,
            "dagger_comparison_gauge_L": curvature_lagrangian(1j*electric, "dagger_comparison").real,
            "dagger_comparison_compensator_L": curvature_lagrangian(electric, "dagger_comparison").real,
            "opposite_electric_signs_are_conditional_not_a_native_ghost_theorem": True,
            "dagger_pairing_is_a_different_action_not_a_silent_fix": True,
            "mixed_real_action_does_not_automatically_vary_to_the_printed_complex_resonance_equation": True,
        },
        "explicit_alternative_real_completion": {
            "status": "comparison only, not adopted in the native paper",
            "action": "L_dagger=-Tr(F_mu_nu^dagger F^mu_nu)/4=-Tr(F_A^2)/4-kappa^2 Tr(X^2)/4",
            "scope": "constant real n, Hermitian A,H, unitary gauge transformations, closure background omitted or fixed commuting",
            "gauge_EL": "D_mu^A F_A^{mu nu}+i kappa^2 n_mu [H,X^{mu nu}]=0",
            "hc_EL": "kappa^2 n_nu D_mu^A X^{mu nu}=0",
            "sources_penalties_and_other_background_variations_must_be_added": True,
            "printed_complex_resonance_equation_not_automatically_equivalent": True,
            "commuting_wave_witness_solves_these_curvature_only_equations": True,
            "no_claim_that_it_solves_the_native_penalty_or_probe_equations": True,
            "null_rank_deficiency_not_removed": True,
        },
        "conditional_existing_penalty_oscillator": {
            "assumptions": "independent H=h T, fixed matching target Lambda=h_Lambda T, positive lambda_H, homogeneous profile, no other sources",
            "potential_already_printed": "U_HC=lambda_H Tr(T^2)(h-h_Lambda)^2",
            "equation": "h_ddot+2 lambda_H [h-h_Lambda]/[kappa^2 (n^0)^2]=0",
            "frequency_squared": "2 lambda_H/[kappa^2 (n^0)^2], not a native numerical prediction or particle mass",
            "independent_example_lambda_H": 0.3,
            "example_frequency_squared": 2*0.3/(coupling**2*(METRIC @ n)[0]**2),
            "not_simultaneous_with_exact_H_equals_Lambda_constraint_for_nonzero_oscillations": True,
            "other_field_equations_and_background_reaction_still_required": True,
            "no_additional_potential_or_irreversible_damping": True,
        },
        "full_equation_vs_null_projection": {
            "full_source_free_comparison": "E_nu=partial^mu F_mu_nu=0 for an independent real Abelian connection",
            "pullback_EL": "EL_h=kappa Tr(T n^nu E_nu), not every E_nu=0",
            "null_restricted_equation": "(partial_t+partial_z)^2 h=0",
            "witness": "h=2+t cos(1.3(z-t)), evaluated at t=0.7,z=0.4",
            "h_at_sample": profile["value"],
            "restricted_EL": scalar_el(profile["hessian"], n, generator, coupling),
            "full_residual_components_in_units_of_T": (residual[:, 0, 0]/generator[0, 0]).real.tolist(),
            "full_residual_norm": float(np.linalg.norm(residual)),
            "pullback_projection": float(tangent.real),
            "differential_identity_norm": float(np.linalg.norm(identity)),
            "identity_does_not_imply_normal_equations": True,
            "scope": "valid parent-field counterexample and test of a separately imposed adjoint resonance equation; not an automatic native Hermitian A variation",
            "native_source_free_branch_and_all_other_field_equations_not_established": True,
            "homogeneous_commuting_h_has_E_0_zero": True,
            "nonzero_homogeneous_temporal_source_needs_other_fields_or_flux": True,
        },
        "remaining_native_obligations": [
            "fix the internal adjoint, real action, trace pairing and allowed connection variations",
            "derive the generator-resolved native currents from that same real action",
            "decide independent H_C versus functional H_C=Lambda[M,P] and apply the correct variational chain rule",
            "evaluate all normal, Gauss, projector and compensator equations with spatial profiles and boundaries",
            "match any positive kinetic coefficient to the actual residual/readout carrier before adding it to modal inertia",
        ],
        "closure_boundary": "If H_C=Lambda=0 identically on an exact commuting closure branch, its derivatives and this HC kinetic contribution vanish; H_C=0 at one point alone does not suffice.",
        "main_TeX_changed": False,
        "empirical_masses_target_phase_or_new_damping_coefficient_used": False,
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
