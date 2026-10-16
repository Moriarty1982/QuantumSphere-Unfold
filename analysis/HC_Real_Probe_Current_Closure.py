"""Real probe action, matrix sources and Ward identity in a conditional HC sector."""
import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "real_probe_null_action", Path(__file__).with_name("HC_Null_Axis_Action_Check.py"))
curvature = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(curvature)
SPEC = importlib.util.spec_from_file_location(
    "real_probe_sources", Path(__file__).with_name("HC_Source_Backreaction.py"))
sources = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sources)


def _weights(value):
    value = curvature._finite(value, "spin kinetic weights")
    if (value.ndim != 3 or value.shape[0] != 4 or value.shape[1] == 0
            or value.shape[1] != value.shape[2]
            or not np.allclose(value, value.conj().swapaxes(-1, -2), atol=1e-12, rtol=0)):
        raise ValueError("Four finite Hermitian spin kinetic weights required")
    return value


def _fields(psi, gauge, hc, spin_weights, spin_metric):
    weights = _weights(spin_weights)
    metric = sources._hermitian(spin_metric, "Spin adjoint matrix")
    psi = curvature._finite(psi, "generation-by-spin probe")
    hc = sources._hermitian(hc, "Compensator")
    gauge = curvature._finite(gauge, "gauge matrices")
    if (metric.shape != weights.shape[1:] or psi.shape != (hc.shape[0], metric.shape[0])
            or gauge.shape != (4, *hc.shape)
            or not np.allclose(gauge, gauge.conj().swapaxes(-1, -2), atol=1e-12, rtol=0)):
        raise ValueError("Compatible Hermitian spin/internal fields and probe required")
    return psi, gauge, hc, weights, metric


def _derivatives(value, psi):
    value = curvature._finite(value, "probe derivatives")
    if value.shape != (4, *psi.shape):
        raise ValueError("Four ordinary derivatives matching the probe required")
    return value


def probe_currents(psi, spin_weights, spin_metric):
    weights = _weights(spin_weights)
    metric = sources._hermitian(spin_metric, "Spin adjoint matrix")
    if metric.shape != weights.shape[1:]:
        raise ValueError("The adjoint and kinetic spin carriers must agree")
    return {"gauge": np.array([sources.spin_bilinear_source(psi, weight) for weight in weights]),
            "scalar": sources.spin_bilinear_source(psi, metric)}


def real_probe_density(psi, derivatives, gauge, hc, spin_weights, spin_metric, mass=0.0, yukawa=1.0):
    """Real symmetric kinetic term; commuting internal HC transport has canceled."""
    psi, gauge, hc, weights, metric = _fields(psi, gauge, hc, spin_weights, spin_metric)
    derivatives = _derivatives(derivatives, psi)
    mass, yukawa = curvature._scalar(mass, "central mass"), curvature._scalar(yukawa, "Yukawa coefficient")
    kinetic = -sum(np.vdot(psi, derivative @ weight.T).imag for derivative, weight in zip(derivatives, weights))
    currents = probe_currents(psi, weights, metric)
    interaction = sum(np.trace(a @ j).real for a, j in zip(gauge, currents["gauge"]))
    interaction += mass*np.trace(currents["scalar"]).real+yukawa*np.trace(hc @ currents["scalar"]).real
    return float(kinetic-interaction)


def literal_probe_density(psi, derivatives, gauge, hc, spin_weights, spin_metric,
                          n_covector, coupling, mass=0.0, yukawa=1.0):
    """Complex native-style ordered term in this declared factorized carrier."""
    psi, gauge, hc, weights, metric = _fields(psi, gauge, hc, spin_weights, spin_metric)
    derivatives = _derivatives(derivatives, psi)
    n, coupling = curvature._real(n_covector, (4,), "axis covector"), curvature._scalar(coupling, "coupling")
    mass, yukawa = curvature._scalar(mass, "central mass"), curvature._scalar(yukawa, "Yukawa coefficient")
    covariant = derivatives+1j*gauge @ psi+coupling*n[:, None, None]*(hc @ psi)
    kinetic = 1j*sum(np.vdot(psi, derivative @ weight.T) for derivative, weight in zip(covariant, weights))
    potential = np.vdot(psi, (mass*psi+yukawa*hc @ psi) @ metric.T)
    return complex(kinetic-potential)


def probe_residual(psi, derivatives, gauge, hc, spin_weights, spin_metric, mass=0.0, yukawa=1.0):
    """EL_{psi^dagger} of the real action, for constant Hermitian kinetic weights."""
    psi, gauge, hc, weights, metric = _fields(psi, gauge, hc, spin_weights, spin_metric)
    derivatives = _derivatives(derivatives, psi)
    mass, yukawa = curvature._scalar(mass, "central mass"), curvature._scalar(yukawa, "Yukawa coefficient")
    kinetic = sum(1j*derivative @ weight.T-a @ psi @ weight.T
                  for derivative, a, weight in zip(derivatives, gauge, weights))
    return kinetic-(mass*psi+yukawa*hc @ psi) @ metric.T


def covariant_current_divergence(psi, derivatives, gauge, spin_weights, spin_metric):
    weights = _weights(spin_weights)
    currents = probe_currents(psi, weights, spin_metric)
    psi = curvature._finite(psi, "probe")
    derivatives = _derivatives(derivatives, psi)
    gauge = curvature._finite(gauge, "gauge matrices")
    if (gauge.shape != currents["gauge"].shape
            or not np.allclose(gauge, gauge.conj().swapaxes(-1, -2), atol=1e-12, rtol=0)):
        raise ValueError("Four compatible Hermitian gauge matrices required")
    result = np.zeros_like(currents["scalar"])
    for derivative, weight, a, j in zip(derivatives, weights, gauge, currents["gauge"]):
        product = derivative @ weight.T @ psi.conj().T
        result += product+product.conj().T+1j*(a @ j-j @ a)
    return result


def homogeneous_probe_rates(psi, gauge, hc, spin_weights, spin_metric,
                            n_covector, coupling, mass=0.0, yukawa=1.0):
    psi, gauge, hc, weights, metric = _fields(psi, gauge, hc, spin_weights, spin_metric)
    n, coupling = curvature._real(n_covector, (4,), "axis covector"), curvature._scalar(coupling, "coupling")
    if np.linalg.eigvalsh(weights[0])[0] <= 0:
        raise ValueError("A positive temporal kinetic comparison required for norm statements")
    zero = np.zeros((4, *psi.shape), dtype=complex)
    residual_at_rest = probe_residual(psi, zero, gauge, hc, weights, metric, mass, yukawa)
    inverse_time = np.linalg.inv(weights[0].T)
    conservative = 1j*residual_at_rest @ inverse_time
    slash = np.einsum("m,mij->ij", n, weights)
    raw = conservative-coupling*hc @ psi @ slash.T @ inverse_time
    norm = np.vdot(psi, psi @ weights[0].T).real
    return {"real_action_rate": conservative, "raw_equation_rate": raw, "norm": float(norm),
            "real_norm_rate": float(2*np.vdot(psi, conservative @ weights[0].T).real),
            "raw_norm_rate": float(2*np.vdot(psi, raw @ weights[0].T).real),
            "raw_balance": float(-2*coupling*np.trace(hc @ sources.spin_bilinear_source(psi, slash)).real)}


def constant_field_system(psi, gauge, hc, target, spin_weights, spin_metric,
                          n_covector, coupling, penalty=1.0, mass=0.0, yukawa=1.0):
    """Alternative real A,H,Psi sector; target is an adjoint spurion, not solved Lambda[M,P]."""
    psi, gauge, hc, weights, metric = _fields(psi, gauge, hc, spin_weights, spin_metric)
    target, penalty = sources._hermitian(target, "Matching target"), curvature._scalar(penalty, "Penalty")
    mass, yukawa = curvature._scalar(mass, "central mass"), curvature._scalar(yukawa, "Yukawa coefficient")
    if target.shape != hc.shape or penalty <= 0:
        raise ValueError("A compatible Hermitian target and positive matching penalty required")
    field = curvature.constant_paired_field_equations(gauge, hc, n_covector, coupling)
    currents = probe_currents(psi, weights, metric)
    zero = np.zeros((4, *psi.shape), dtype=complex)
    residual = probe_residual(psi, zero, gauge, hc, weights, metric, mass, yukawa)
    difference = hc-target
    a_el = field["gauge_EL"]-currents["gauge"]
    h_el = field["hc_EL"]-2*penalty*difference-yukawa*currents["scalar"]
    target_el = 2*penalty*difference
    divergence = 1j*np.sum(gauge @ a_el-a_el @ gauge, axis=0)
    matter = 1j*(psi @ residual.conj().T-residual @ psi.conj().T)
    identity = (divergence+1j*(hc @ h_el-h_el @ hc)
                +1j*(target @ target_el-target_el @ target)+matter)
    density = field["L"]-penalty*np.vdot(difference, difference).real
    density += real_probe_density(psi, zero, gauge, hc, weights, metric, mass, yukawa)
    return {"L": float(density), "gauge_EL": a_el, "hc_EL": h_el, "target_EL": target_el,
            "probe_EL": residual, "ward_identity": identity,
            "external_target_torque": 1j*(target @ target_el-target_el @ target)}


def recycling_completion(density, hamiltonian, damping):
    """One trace-preserving algebraic completion of G=-iH-D, not a native bath."""
    density, hamiltonian, damping = [sources._hermitian(value, name) for value, name in
                                     [(density, "Density"), (hamiltonian, "Hamiltonian"), (damping, "Damping")]]
    if len({density.shape, hamiltonian.shape, damping.shape}) != 1:
        raise ValueError("A common finite carrier required")
    values, vectors = np.linalg.eigh(damping)
    if values[0] < -1e-12 or np.linalg.eigvalsh(density)[0] < -1e-12:
        raise ValueError("Positive density and damping required for this completion")
    jump = (vectors*np.sqrt(2*np.maximum(values, 0))) @ vectors.conj().T
    conditional = -1j*(hamiltonian @ density-density @ hamiltonian)-damping @ density-density @ damping
    recycling = jump @ density @ jump.conj().T
    return {"jump": jump, "conditional_rate": conditional,
            "recycling": recycling, "trace_preserving_rate": conditional+recycling}


def recycling_step(density, hamiltonian, damping, time_step):
    """One exact positive trace-preserving discrete step with the declared generator."""
    completion = recycling_completion(density, hamiltonian, damping)
    density, hamiltonian, damping = [np.asarray(value, dtype=complex) for value in [density, hamiltonian, damping]]
    time_step = curvature._scalar(time_step, "time step")
    values, vectors = np.linalg.eigh(damping)
    if time_step < 0 or 2*time_step*values[-1] > 1:
        raise ValueError("A nonnegative step with 2 dt lambda_max(D)<=1 required")
    h_values, h_vectors = np.linalg.eigh(hamiltonian)
    unitary = (h_vectors*np.exp(-1j*time_step*h_values)) @ h_vectors.conj().T
    survival = (vectors*np.sqrt(np.maximum(1-2*time_step*values, 0))) @ vectors.conj().T
    m0, m1 = unitary @ survival, np.sqrt(time_step)*completion["jump"]
    return {"density": m0 @ density @ m0.conj().T+m1 @ density @ m1.conj().T,
            "completeness": m0.conj().T @ m0+m1.conj().T @ m1}


def comparison_balance(generator, comparison, comparison_rate=None):
    """Q_dot+G^dagger Q+Q G; with rate zero also tests a curvature's Q-skewness."""
    comparison = sources._hermitian(comparison, "Positive comparison")
    generator = sources.phase._finite_square(generator, "Generator or curvature matrix")
    rate = np.zeros_like(comparison) if comparison_rate is None else sources._hermitian(comparison_rate, "Comparison rate")
    if (generator.shape != comparison.shape or rate.shape != comparison.shape
            or np.linalg.eigvalsh(comparison)[0] <= 0):
        raise ValueError("A compatible strictly positive comparison and Hermitian rate required")
    return rate+generator.conj().T @ comparison+comparison @ generator


def example_fields():
    sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_y = np.array([[0, -1j], [1j, 0]])
    spin_metric = np.diag([1.0, -1.0])
    weights = np.array([np.eye(2), np.zeros((2, 2)), np.zeros((2, 2)), sigma_x])
    psi = np.array([[1, 1], [0, 0]], dtype=complex)/np.sqrt(2)
    gauge = np.array([0.1*sigma_y, 0.2*sigma_x, np.zeros((2, 2)), 0.3*spin_metric])
    return {"psi": psi, "gauge": gauge, "hc": np.diag([0.7, 1.2]),
            "target": 0.4*np.eye(2)+0.1*sigma_x, "weights": weights, "spin_metric": spin_metric,
            "n": np.array([1.0, 0.0, 0.0, 1.0]), "coupling": 0.4, "mass": 0.6,
            "yukawa": 0.2, "penalty": 0.3}


def evaluate():
    e = example_fields()
    fields = [e[key] for key in ["psi", "gauge", "hc", "weights", "spin_metric"]]
    rates = homogeneous_probe_rates(*fields, e["n"], e["coupling"], e["mass"], e["yukawa"])
    zero = np.zeros((4, *e["psi"].shape), dtype=complex)
    literal = literal_probe_density(e["psi"], zero, *fields[1:], e["n"], e["coupling"], e["mass"], e["yukawa"])
    system = constant_field_system(e["psi"], e["gauge"], e["hc"], e["target"], e["weights"],
                                   e["spin_metric"], e["n"], e["coupling"], e["penalty"], e["mass"], e["yukawa"])
    damping = e["coupling"]*np.kron(e["hc"], np.einsum("m,mij->ij", e["n"], e["weights"]))
    hamiltonian = sum(np.kron(a, k) for a, k in zip(e["gauge"], e["weights"]))
    hamiltonian += np.kron(e["mass"]*np.eye(2)+e["yukawa"]*e["hc"], e["spin_metric"])
    state = e["psi"].reshape(-1)
    completion = recycling_completion(np.outer(state, state.conj()), hamiltonian, damping)
    return {
        "status": "conditional real probe/gauge/HC sector, exact current identities; no native full closure or adopted action change",
        "assumptions": {
            "carrier": "generation tensor spin, internal fields commute with spin matrices",
            "adjoint": "bar(Psi)=Psi^dagger eta_D, eta_D Hermitian, K^mu=eta_D Gamma^mu Hermitian and constant",
            "mass_term": "eta_D Omega Hermitian; tested central mass plus gamma H_C",
            "positive_time_comparison_required_for_norm_claims": True,
            "native_carrier_adjoint_gamma_and_background_identification_not_derived": True,
        },
        "real_probe_action": {
            "L": "i(Psi^dagger K^mu partial_mu Psi-partial_mu Psi^dagger K^mu Psi)/2-Tr(A_mu j^mu)-m Tr(S)-gamma Tr(H S)",
            "matrix_currents": "j^mu=Tr_spin(K^mu |Psi><Psi|), S=Tr_spin(eta_D |Psi><Psi|)",
            "commuting_real_HC_transport": "Re[i kappa bar(Psi) Gamma.n H Psi]=0; the same holds for Hermitian closure load",
            "general_noncommuting_rule": "Herm(i K.n H)=i[K.n,H]/2, not the original ordered transport",
            "raw_equation_and_real_action_not_generally_equivalent": True,
            "same_HC_bosonic_kinetic_term_and_gamma_Yukawa_source_can_remain": True,
        },
        "paired_bosonic_sector_plus_sources": {
            "curvature_choice": "alternative -Tr(F^dagger F)/4 from HC_Null_Axis_Action_Check, not a native correction",
            "gauge_equation": "D_mu^A F_A^{mu nu}+i kappa^2 n_mu[H,X^{mu nu}]-j^nu=0",
            "hc_equation": "kappa^2 n_nu D_mu^A X^{mu nu}-2lambda_H(H-Lambda)-gamma S=0",
            "target_reaction": "E_Lambda=2lambda_H(H-Lambda) for an external covariant matching target",
            "projector_and_noncentral_native_mass_background_terms_not_evaluated": True,
            "algebraic_matching_penalty_has_no_direct_A_variation_at_fixed_H_Lambda": True,
            "printed_gradient_trace_currents_not_automatically_recovered": True,
        },
        "ward_identity": {
            "off_shell": "D_mu E_A^mu+i[H,E_H]+i[Lambda,E_Lambda]+i Tr_spin(Psi R^dagger-R Psi^dagger)=0",
            "R": "real-action probe Euler derivative",
            "matter_on_shell": "D_mu j^mu=-i gamma[H,S]; its ordinary trace is conserved",
            "fixed_target_consistency": "If A,H,Psi solve these equations and Lambda is not varied, lambda_H>0 requires [H,Lambda]=0 unless extra background reactions are retained",
            "functional_Lambda_requires_chain_rule_to_M_P_equations_not_an_extra_free_field": True,
            "constant_noncommuting_example_identity_norm": float(np.linalg.norm(system["ward_identity"])),
            "same_example_external_target_torque_norm": float(np.linalg.norm(system["external_target_torque"])),
        },
        "norm_balance_example": {
            "n_covector": e["n"].tolist(),
            "orientation": "chosen null covector with K.n=I+sigma_x positive; reversing n reverses the raw HC norm source",
            "dimensionless_kappa": e["coupling"],
            "dimensionless_gamma": e["yukawa"],
            "norm": rates["norm"],
            "real_action_norm_rate": rates["real_norm_rate"],
            "raw_equation_norm_rate": rates["raw_norm_rate"],
            "raw_continuity_rhs": rates["raw_balance"],
            "literal_probe_L_real": literal.real,
            "literal_probe_L_imaginary": literal.imag,
            "physical_probe_probability_interpretation_not_native_input": True,
        },
        "open_model_comparison": {
            "assumption": "positive damping D in an already positive modal metric; not automatic for native gamma-ordered HC",
            "conditional_rate": "rho_dot_cond=-i[H_modal,rho]-{D,rho}",
            "one_recycling_choice": "L_jump=sqrt(2D); add L_jump rho L_jump^dagger",
            "example_conditional_trace_rate": float(np.trace(completion["conditional_rate"]).real),
            "example_recycling_trace_rate": float(np.trace(completion["recycling"]).real),
            "example_completed_trace_rate": float(np.trace(completion["trace_preserving_rate"]).real),
            "recycling_or_charged_environment_not_supplied_by_native_action": True,
            "same_no_jump_D_does_not_determine_unique_recycling_or_environment": True,
            "not_a_derivation_of_gravity_as_a_bath_or_viscosity": True,
        },
        "moving_comparison_route": {
            "time_chart_condition": "Q_dot+G^dagger Q+Q G=0 makes f^dagger Q f conserved for f_dot=G f",
            "formal_solution": "Q(t)=U(t)^(-dagger) Q0 U(t)^(-1); this is not a native metric derivation",
            "constant_commuting_decay_example": "G=-D, Q(t)=exp(2Dt), f(t)=exp(-Dt) f0",
            "stronger_bundle_condition": "partial_mu Q=B_mu^dagger Q+Q B_mu",
            "integrability": "F_mu_nu^dagger Q+Q F_mu_nu=0",
            "pure_HC_branch_obstruction": "Nonzero ordinary Hermitian F_mu_nu cannot be skew for any strictly positive Q. The pure commuting HC wedge must vanish for this strong bundle route.",
            "flat_HC_example": "constant H, B_mu=kappa n_mu H, Q(x)=exp(2kappa H n.x) has F=0 and compatible positive Q",
            "not_a_general_no_go_for_noncommuting_full_connection_or_contracted_Dirac_current": True,
            "QAM_comparison_not_identified_with_this_spacetime_kinetic_metric": True,
        },
        "native_comparison_anchors_checked": {
            "QAM": "07_qam_infrastructure.tex, def:two-sided-admissible-contractions and ex:two-sided-residual-comparison: typed residual comparison, not an evaluated Dirac kinetic metric",
            "Einstein_route": "10_sphaera_and_physics.tex, prop:bilinear-einstein-reconstruction: assumed spacetime metric compatibility after geometric/internal splitting, not positive internal compatibility",
            "quaternionic_inner_product": "10_sphaera_and_physics.tex, prop:orthogonality-third-kernel: basis inner product, not an evaluated probe-adjoint/carrier map",
        },
        "remaining_choices": [
            "use a closed real probe action with HC bosonic kinetics and gamma coupling, explicitly changing the raw transport law",
            "or retain raw norm-changing transport as an open/conditional law and derive its missing environment, metric and currents",
            "an independent adjoint needs a specified real/doubled field space; a moving comparison needs its background law, adjoint and derivative terms",
            "do not interpret a Hermitian-to-anti-Hermitian HC shift as harmless: with free A its vector shift can be absorbed into the total connection",
        ],
        "main_TeX_changed": False,
        "native_masses_phase_viscosity_or_microscopic_environment_derived": False,
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
