"""Evaluate a declared cyclic coupling candidate, not a native mass prediction.

The radius and frame-phase law are inherited hypotheses. Historical masses
enter comparisons/calibrations only, never the coupling construction.
"""
import argparse
import json
import math
from pathlib import Path

import numpy as np


PLANCK_GEV = 1.220890e19
FERMI_GEV_MINUS_2 = 1.1663787e-5
HISTORICAL_MASSES_MEV = np.array([0.51100, 105.658, 1776.86])
REFERENCE_SOURCES = {
    "planck_energy": "https://physics.nist.gov/cgi-bin/cuu/Value?plkmc2gev",
    "fermi_constant": "https://physics.nist.gov/cgi-bin/cuu/Value?gf",
    "newton_constant": "https://physics.nist.gov/cgi-bin/cuu/Value?bg",
    "historical_mass_comparison":
        "sources/research/parts/v470/10_sphaera_and_physics.tex:thm:koide-triolic",
}


def normalized_cyclic_root(radius, theta):
    """A declared positive cyclic root shape, not a native coupling law."""
    if not math.isfinite(radius) or radius < 0 or not math.isfinite(theta):
        raise ValueError("Finite radius >= 0 and finite theta are required")
    u = np.roll(np.eye(3), 1, axis=0)
    a = 1/math.sqrt(3+6*radius*radius)
    z = a*radius*np.exp(1j*theta)
    b = a*np.eye(3)+z*u+z.conjugate()*u.T
    if np.linalg.eigvalsh(b)[0] < -1e-12:
        raise ValueError("The inherited phase lies outside the positive-root chamber")
    return b


def cyclic_candidate(beta=0.5493):
    """Unit-Frobenius root candidate on the declared positive phase branch."""
    if not math.isfinite(beta) or abs(beta) >= 1:
        raise ValueError("The frame input must be finite with abs(beta) < 1")
    theta = math.pi-math.sqrt(2)*math.asin(beta)
    b = normalized_cyclic_root(1/math.sqrt(2), theta)
    return theta, b, b.conj().T @ b


def light_masses(q, mu, gap):
    """Positive magnitudes for A=0, H_perp=gap*I and V=mu*B."""
    q = np.asarray(q, dtype=float)
    if (q.ndim != 1 or q.size == 0 or not np.all(np.isfinite(q))
            or np.any(q < 0)):
        raise ValueError("q must be a nonempty finite nonnegative spectrum")
    if not math.isfinite(mu) or mu < 0 or not math.isfinite(gap) or gap <= 0:
        raise ValueError("A finite mu >= 0 and finite gap > 0 are required")
    coupling = mu*np.sqrt(q)
    # Rationalization avoids subtracting nearly equal Planck-scale numbers.
    return coupling*(2*coupling/(np.hypot(gap, 2*coupling)+gap))


def koide_diagnostic(masses):
    masses = np.asarray(masses, dtype=float)
    if (masses.ndim != 1 or masses.size != 3 or not np.all(np.isfinite(masses))
            or np.any(masses < 0) or not np.any(masses > 0)):
        raise ValueError("Three finite nonnegative, not all zero, masses are required")
    masses = masses/np.max(masses)
    return float(np.sum(masses)/np.sum(np.sqrt(masses))**2)


def scale_scenario(q, mu, gap):
    masses = light_masses(q, mu, gap)
    return {
        "mu_GeV": float(mu), "gap_GeV": float(gap),
        "kappa_leading_GeV": float(mu*mu/gap),
        "mass_magnitudes_GeV": masses.tolist(),
        "ratios_to_largest": (masses/masses[-1]).tolist(),
        "complementary_weights": (masses/(gap+2*masses)).tolist(),
        "koide_diagnostic": koide_diagnostic(masses),
    }


def matrix_diagnosis():
    """Post-hoc decomposition of the historical benchmark, never a prediction."""
    beta = 0.5493
    theta, b, qmatrix = cyclic_candidate(beta)
    q = np.linalg.eigvalsh(qmatrix)
    roots = np.sqrt(HISTORICAL_MASSES_MEV/np.sum(HISTORICAL_MASSES_MEV))
    phases = 2*math.pi*np.arange(3)/3
    a_target = float(np.mean(roots))
    z_target = np.sum(roots*np.exp(-1j*phases))/3
    theta_target = float(np.angle(z_target))
    radius_target = float(abs(z_target)/a_target)
    beta_equivalent = math.sin((math.pi-theta_target)/math.sqrt(2))
    radius = 1/math.sqrt(2)

    def shape_ratios(r, phase):
        root = normalized_cyclic_root(r, phase)
        values = np.linalg.eigvalsh(root.conj().T @ root)
        return (values/values[-1]).tolist()

    raw_roots = 1+2*radius*np.cos(theta+phases)
    log_root_theta = -2*radius*np.sin(theta+phases)/raw_roots
    log_root_radius = 2*np.cos(theta+phases)/raw_roots
    derivative_theta = 2*(log_root_theta-log_root_theta[-1])
    derivative_radius = 2*(log_root_radius-log_root_radius[-1])
    derivative_beta = derivative_theta*(-math.sqrt(2)/math.sqrt(1-beta*beta))
    gamma_string = math.log(2)/(math.pi*math.sqrt(3))
    beta_from_quoted_gbi = math.sqrt((0.2375-gamma_string)/(0.2375+gamma_string))
    theta_from_quoted_gbi = math.pi-math.sqrt(2)*math.asin(beta_from_quoted_gbi)
    rounded_b = np.round(b.real, 6)+1j*np.round(b.imag, 6)
    rounded_q = np.linalg.eigvalsh(rounded_b.conj().T @ rounded_b)
    return {
        "status": "post-hoc historical benchmark inversion, not a derived phase law",
        "benchmark_root_a": a_target,
        "benchmark_root_z_real": float(z_target.real),
        "benchmark_root_z_imag": float(z_target.imag),
        "benchmark_radius": radius_target,
        "imposed_radius": radius,
        "relative_radius_difference": radius_target/radius-1,
        "benchmark_phase_radians": theta_target,
        "phase_difference_radians": theta_target-theta,
        "phase_difference_degrees": math.degrees(theta_target-theta),
        "effective_beta_from_benchmark_phase": beta_equivalent,
        "beta_difference": beta_equivalent-beta,
        "decimal_rounding_halfstep": 0.00005,
        "required_shift_in_rounding_halfsteps": (beta_equivalent-beta)/0.00005,
        "log_ratio_derivative_theta": derivative_theta.tolist(),
        "log_ratio_derivative_radius": derivative_radius.tolist(),
        "log_ratio_derivative_beta": derivative_beta.tolist(),
        "phase_only_corrected_ratios": shape_ratios(radius, theta_target),
        "radius_only_corrected_ratios": shape_ratios(radius_target, theta),
        "both_benchmark_reconstructed_ratios": shape_ratios(radius_target, theta_target),
        "six_decimal_matrix_relative_ratio_errors":
            ((rounded_q/rounded_q[-1])/(q/q[-1])-1).tolist(),
        "rounding_interval_ratios": {
            str(value): shape_ratios(radius, math.pi-math.sqrt(2)*math.asin(value))
            for value in (beta-0.00005, beta+0.00005)
        },
        "source_ratio_recomputed_not_exact_native_input": {
            "gamma_string": gamma_string,
            "quoted_gamma_BI": 0.2375,
            "beta": beta_from_quoted_gbi,
            "ratios": shape_ratios(radius, theta_from_quoted_gbi),
            "gamma_BI_needed_for_benchmark_phase":
                gamma_string*(1+beta_equivalent**2)/(1-beta_equivalent**2),
        },
    }


def planck_diagnosis():
    """Audit units and extra Planck-gap assumptions; fits are labelled as such."""
    _, _, qmatrix = cyclic_candidate()
    q = np.linalg.eigvalsh(qmatrix)
    hbar_si = 6.62607015e-34/(2*math.pi)
    c_si = 299792458
    g_si = 6.67430e-11
    joule_per_gev = 1.602176634e-10
    planck_kg = math.sqrt(hbar_si*c_si/g_si)
    planck_length = math.sqrt(hbar_si*g_si/c_si**3)
    planck_gev_si = planck_kg*c_si*c_si/joule_per_gev
    mu_ew = 1/math.sqrt(2*math.sqrt(2)*FERMI_GEV_MINUS_2)
    reference_masses = light_masses(q, mu_ew, PLANCK_GEV)
    targets_gev = HISTORICAL_MASSES_MEV/1000
    tau = targets_gev[-1]
    mu_tau = math.sqrt(tau*(tau+PLANCK_GEV)/q[-1])
    nonflat_gaps = mu_tau**2*q/targets_gev-targets_gev
    fitted_masses = np.array([
        light_masses([qi], mu_tau, gap)[0] for qi, gap in zip(q, nonflat_gaps)
    ])
    delta_tau_ew = mu_ew**2*q[-1]/tau-tau
    gamma = (1+0.5493**2)/(1-0.5493**2)
    return {
        "scope": "Delta=Planck and A=0 were additional test assumptions, not paper-derived identities",
        "si_inputs": {"hbar_Js": hbar_si, "c_m_per_s": c_si,
                      "G_m3_per_kg_s2": g_si, "J_per_GeV": joule_per_gev},
        "si_planck_mass_kg": planck_kg,
        "si_planck_length_m": planck_length,
        "si_planck_energy_GeV": planck_gev_si,
        "relative_si_vs_rounded_codata_energy_difference": planck_gev_si/PLANCK_GEV-1,
        "reference_mass_shortfall_factor_vs_quoted_tau": tau/reference_masses[-1],
        "reduced_planck_gap_mass_magnitudes_eV":
            (light_masses(q, mu_ew, PLANCK_GEV/math.sqrt(8*math.pi))*1e9).tolist(),
        "conditional_paper_frame_factors": {
            "gamma_L": gamma,
            "planck_length_photon_over_matter": gamma**-1.5,
            "consistent_planck_mass_photon_over_matter": gamma**0.5,
            "mixed_hbar_wrong_planck_mass_photon_over_matter": gamma**1.5,
            "not_a_standard_Lorentz_transformation_of_constants": True,
        },
        "tau_calibrations_not_predictions": {
            "planck_gap_required_mu_GeV": mu_tau,
            "relative_to_electroweak_mixing_reference": mu_tau/mu_ew,
            "electroweak_mixing_required_gap_GeV": delta_tau_ew,
            "gap_inverse_energy_length_m": hbar_si*c_si/(joule_per_gev*delta_tau_ew),
            "gap_length_over_fundamental_planck_length":
                hbar_si*c_si/(joule_per_gev*delta_tau_ew*planck_length),
        },
        "nonflat_planck_gap_full_mass_fit_not_prediction": {
            "assumption": "Gap diagonal in the output singular basis of B",
            "mu_GeV": mu_tau,
            "gaps_GeV": nonflat_gaps.tolist(),
            "gaps_over_tau_gap": (nonflat_gaps/PLANCK_GEV).tolist(),
            "fitted_mass_magnitudes_GeV": fitted_masses.tolist(),
            "complementary_weights": (fitted_masses/(nonflat_gaps+2*fitted_masses)).tolist(),
        },
        "direct_mass_block_scenario": {
            "assumptions": "Hermitian A retained; H_perp >= Planck*I; abs(lambda)<=2 GeV; ||V||^2=mu_EW^2*q_max",
            "light_eigenvalue_distance_to_spectrum_A_bound_eV":
                mu_ew**2*q[-1]/(PLANCK_GEV-2)*1e9,
            "native_A_not_evaluated": True,
        },
    }


def positive_metric_root(metric, inverse=False):
    """Finite positive Hermitian metric root; no implicit index-space matching."""
    metric = np.asarray(metric, dtype=complex)
    if (metric.ndim != 2 or metric.shape[0] == 0
            or metric.shape[0] != metric.shape[1]
            or not np.all(np.isfinite(metric))
            or not np.allclose(metric, metric.conj().T, rtol=1e-12, atol=1e-12)):
        raise ValueError("A finite nonempty Hermitian square metric is required")
    values, vectors = np.linalg.eigh(metric)
    if values[0] <= 0:
        raise ValueError("The comparison/kinetic metric must be positive definite")
    factors = 1/np.sqrt(values) if inverse else np.sqrt(values)
    return (vectors*factors) @ vectors.conj().T


def tensor_coupling(b, input_metric, output_metric):
    """Canonical coupling for a declared map B: (V,K) -> (W,H)."""
    b = np.asarray(b, dtype=complex)
    if b.ndim != 2 or not np.all(np.isfinite(b)):
        raise ValueError("A finite matrix cross block is required")
    kinv = positive_metric_root(input_metric, inverse=True)
    hout = positive_metric_root(output_metric)
    if b.shape != (hout.shape[0], kinv.shape[0]):
        raise ValueError("Cross-block and metric index-space dimensions disagree")
    canonical = hout @ b @ kinv
    gram = canonical.conj().T @ canonical
    return canonical, gram, np.linalg.eigvalsh(gram)


def tensor_shift_diagnosis():
    """Separate tag shifts, covariant chart changes and added physical metrics."""
    _, b, qmatrix = cyclic_candidate()
    q, f = np.linalg.eigh(qmatrix)
    eye = np.eye(3)
    # Deliberately nonunitary charts, not claimed to be a native frame map.
    a = np.array([[1.4, 0.2j, 0], [0, 0.8, 0.15], [0, 0, 1.1]])
    d = np.array([[0.9, 0.1, 0], [0, 1.2, 0.2j], [0, 0, 1.3]])
    b_chart = np.linalg.solve(d, b @ a)
    _, _, chart_q = tensor_coupling(b_chart, a.conj().T @ a, d.conj().T @ d)
    naive_q = np.linalg.eigvalsh(b_chart.conj().T @ b_chart)

    # Post-hoc metric witness: masses fix weights, never the reverse.
    target = q[-1]*HISTORICAL_MASSES_MEV/HISTORICAL_MASSES_MEV[-1]
    weights = target/q
    h_fit = (f*weights) @ f.conj().T
    _, _, fitted_q = tensor_coupling(b, eye, h_fit)
    mu_ew = 1/math.sqrt(2*math.sqrt(2)*FERMI_GEV_MINUS_2)
    tau = HISTORICAL_MASSES_MEV[-1]/1000
    needed_gain = tau*(tau+PLANCK_GEV)/(mu_ew**2*q[-1])
    doubled_b = np.kron(b, np.eye(2))
    seed = np.kron(eye, np.array([[1], [1]])/math.sqrt(2))
    pulled_back = seed.conj().T @ doubled_b.conj().T @ doubled_b @ seed
    return {
        "scope": "positive finite metric extension; no native tensor metric extracted",
        "source_shift_is_tag_only": {
            "tag_support_before": [0, 2, 5], "tag_support_after": [1, 3, 6],
            "packed_mask_before": sum(1 << k for k in (0, 2, 5)),
            "packed_mask_after": sum(1 << k for k in (1, 3, 6)),
            "numeric_payload_changed": False,
            "source": "def:v400-r01-shifted-tensor-payload-migration",
        },
        "canonical_euclidean_eigenvalues": q.tolist(),
        "nonunitary_chart_test_not_native_frame": {
            "covariant_eigenvalues": chart_q.tolist(),
            "max_absolute_eigenvalue_difference": float(np.max(np.abs(chart_q-q))),
            "incorrect_identity_metric_ratios": (naive_q/naive_q[-1]).tolist(),
            "correct_covariant_ratios": (chart_q/chart_q[-1]).tolist(),
        },
        "posthoc_output_metric_fit_not_prediction": {
            "input_metric": "identity; output metric aligned with B singular vectors",
            "output_eigenweights_ascending_B_modes": weights.tolist(),
            "output_metric_real": h_fit.real.tolist(),
            "output_metric_imag": h_fit.imag.tolist(),
            "fitted_leading_ratios": (fitted_q/fitted_q[-1]).tolist(),
            "exact_flat_gap_correction_still_applies": True,
        },
        "planck_metric_bound": {
            "assumptions": "A=0; canonical flat gap=Planck; fixed numerical B and mu=mu_EW",
            "required_h_max_over_k_min_at_least": needed_gain,
            "equivalent_canonical_coupling_norm_enhancement": math.sqrt(needed_gain),
            "fitted_shape_metric_max_weight": float(np.max(weights)),
            "not_a_coordinate_shift_or_a_predicted_scale": True,
        },
        "identity_tensor_extension": {
            "ancilla_dimension": 2,
            "max_absolute_compressed_gram_difference":
                float(np.max(np.abs(pulled_back-qmatrix))),
            "requires_new_interaction_for_new_effect": True,
        },
    }


def schur_response(v, complement, energy=0.0):
    """Return N(E) and N'(E); the induced self-energy is -N(E)."""
    v = np.asarray(v, dtype=complex)
    complement = np.asarray(complement, dtype=complex)
    if not math.isfinite(energy):
        raise ValueError("A finite real energy is required")
    positive_metric_root(complement)
    if (v.ndim != 2 or v.shape[0] != complement.shape[0]
            or v.shape[1] == 0 or not np.all(np.isfinite(v))):
        raise ValueError("A finite nonempty compatible cross block is required")
    shifted = complement-energy*np.eye(complement.shape[0])
    if np.linalg.eigvalsh(shifted)[0] <= 0:
        raise ValueError("Energy must lie strictly below the positive complementary spectrum")
    response = np.linalg.solve(shifted, v)
    return v.conj().T @ response, response.conj().T @ response


def physical_origin_diagnosis():
    """Discriminate mechanisms within declared finite models, not identify nature."""
    theta, b, qmatrix = cyclic_candidate()
    q, f = np.linalg.eigh(qmatrix)
    mu_ew = 1/math.sqrt(2*math.sqrt(2)*FERMI_GEV_MINUS_2)
    tau = HISTORICAL_MASSES_MEV[-1]/1000
    mu_tau = math.sqrt(tau*(tau+PLANCK_GEV)/q[-1])
    _, delta_k_ew = schur_response(mu_ew*b, PLANCK_GEV*np.eye(3))
    _, delta_k_tau = schur_response(mu_tau*b, PLANCK_GEV*np.eye(3))
    weights = (q[-1]*HISTORICAL_MASSES_MEV/HISTORICAL_MASSES_MEV[-1])/q
    phase_target = matrix_diagnosis()["benchmark_phase_radians"]
    b_phase = normalized_cyclic_root(1/math.sqrt(2), phase_target)
    q_phase = np.linalg.eigvalsh(b_phase.conj().T @ b_phase)
    target_ratios = HISTORICAL_MASSES_MEV/HISTORICAL_MASSES_MEV[-1]

    # A response tensor comes from inverse gaps; it is not a new Hilbert norm.
    gaps = PLANCK_GEV/weights
    d_fit = (f*gaps) @ f.conj().T
    response_fit, _ = schur_response(b, d_fit)
    _, _, weighted_q = tensor_coupling(b, np.eye(3), (f*weights) @ f.conj().T)
    reference_gram = (f*weighted_q) @ f.conj().T

    # Same phase label, different interference: disconnected vs coupled outputs.
    vm, vt = np.array([[0.2]]), np.array([[0.3j]])
    phases = [0.0, math.pi/2, math.pi]
    separated, connected = [], []
    for phi in phases:
        v = np.vstack([vm, np.exp(1j*phi)*vt])
        separated.append(float(schur_response(v, np.diag([2.0, 3.0]))[0][0, 0].real))
        connected.append(float(schur_response(v, np.array([[2.0, 0.4], [0.4, 3.0]]))[0][0, 0].real))
    alpha_illustrative = 1/137.036
    qed_delta = 3*alpha_illustrative/(2*math.pi)*np.log(q[-1]/q)
    return {
        "status": "conditional mechanism discrimination, not a physical-cause determination",
        "native_source_candidate": {
            "operator": "Omega = m0 I + alpha P M P + c_T T + gamma H_C",
            "cross_block_under_minimal_commuting_penalty": "(I-P) Omega P = c_T (I-P) T P",
            "c_T_not_identified_with_frame_beta": True,
            "source_labels": ["thm:master-field-equation", "prop:triadic-two-probe", "thm:variational-form"],
            "triadic_probe_slots_not_automatically_lepton_generations": True,
        },
        "induced_kinetic_dressing": {
            "assumptions": "positive Hermitian complement; energy below gap; canonical full carrier",
            "mass_response": "N(E)=V* (D-E I)^(-1) V; self-energy=-N(E)",
            "norm_response": "N'(E)=V* (D-E I)^(-2) V; K_eff=I+N'(0) to first energy order",
            "planck_gap_electroweak_mu_max_delta_K": float(np.linalg.eigvalsh(delta_k_ew)[-1]),
            "planck_gap_tau_calibrated_mu_max_delta_K": float(np.linalg.eigvalsh(delta_k_tau)[-1]),
            "minimum_delta_K_norm_for_aligned_kinetic_only_ratio_fit":
                float(np.max(weights)/np.min(weights)-1),
            "kinetic_only_bound_scope": "fixed numerator and aligned modes; K=I+positive dressing",
            "does_not_cover_gapless_strong_or_nonpositive_sectors": True,
        },
        "response_tensor_from_inverse_gaps": {
            "formula": "H_resp(E)=Delta_ref (D-E I)^(-1)",
            "leading_mass_response": "N(E)=(mu^2/Delta_ref) B* H_resp(E) B",
            "not_a_kinetic_metric_redefinition": True,
            "historical_leading_fit_gap_weights": (gaps/PLANCK_GEV).tolist(),
            "relative_gram_identity_error": float(np.linalg.norm(
                PLANCK_GEV*response_fit-reference_gram)/np.linalg.norm(reference_gram)),
            "fit_uses_target_masses": True,
            "exact_energy_dependence_not_equal_to_flat_gap_metric_model": True,
        },
        "coherent_phase_test": {
            "phase_change_is_historical_calibration_not_prediction": True,
            "delta_phase_radians": phase_target-theta,
            "relative_Frobenius_coupling_change": float(np.linalg.norm(b_phase-b, "fro")/np.linalg.norm(b, "fro")),
            "relative_operator_norm_coupling_change": float(np.linalg.norm(b_phase-b, 2)/np.linalg.norm(b, 2)),
            "corrected_leading_ratios": (q_phase/q_phase[-1]).tolist(),
            "remaining_relative_ratio_errors": ((q_phase/q_phase[-1])/target_ratios-1).tolist(),
            "orthogonal_channel_phase_samples": phases,
            "disconnected_complement_mass_response": separated,
            "coupled_complement_mass_response": connected,
            "hidden_mediator_vertex": "delta V(E) = -Y* (D_med-E I)^(-1) X",
            "mediator_also_changes_direct_gap_and_kinetic_blocks": True,
            "not_a_prediction_of_tachyons_or_wormholes": True,
        },
        "ordinary_one_loop_qed_matching_check": {
            "source": "https://arxiv.org/html/0812.2090v2#S0.E2",
            "alpha_illustrative_not_precision_input": alpha_illustrative,
            "assumption": "candidate masses are common-scale MSbar running masses; benchmark treated as pole masses",
            "relative_ratio_changes_first_order": qed_delta.tolist(),
            "needed_relative_ratio_changes": (weights-1).tolist(),
            "same_sign_qed_cannot_supply_opposite_sign_required_changes": True,
            "native_scheme_and_matching_scale_not_assigned": True,
        },
        "external_method_reference": "https://arxiv.org/abs/1105.0675",
        "remaining_identification": [
            "represented triadic matrix elements and generation embedding",
            "complementary propagator/gap with index-space and units fixed",
            "coherent mixed-sector matrix elements if a relative frame phase is invoked",
            "consistent mass, kinetic and vertex matching in one scheme",
            "independent phase/gap selection law, not historical-mass fitting",
        ],
    }


def triadic_response(a1, a2, c12, w1, w2, complement, energy=0.0):
    """Eliminate the third probe without dropping its diagonal/norm responses."""
    a1, a2, c12, w1, w2, complement = (
        np.asarray(block, dtype=complex)
        for block in (a1, a2, c12, w1, w2, complement))
    for block in (a1, a2, c12, w1, w2, complement):
        if block.ndim != 2 or not np.all(np.isfinite(block)):
            raise ValueError("Finite two-dimensional triadic blocks are required")
    for block in (a1, a2):
        if (block.shape[0] == 0 or block.shape[0] != block.shape[1]
                or not np.allclose(block, block.conj().T, rtol=1e-12, atol=1e-12)):
            raise ValueError("Nonempty Hermitian direct probe blocks are required")
    n1, n2, m = a1.shape[0], a2.shape[0], complement.shape[0]
    if (c12.shape != (n1, n2) or w1.shape != (m, n1)
            or w2.shape != (m, n2)):
        raise ValueError("Triadic block index-space dimensions disagree")
    direct = np.block([[a1, c12], [c12.conj().T, a2]])
    response, norm_response = schur_response(np.hstack([w1, w2]), complement, energy)
    return direct-response, norm_response, response


def triadic_loop_phase(c12, w1, w2):
    """Scalar oriented cycle phase; undefined if any edge vanishes."""
    edges = [complex(value) for value in (c12, w1, w2)]
    if any(not math.isfinite(z.real) or not math.isfinite(z.imag) or z == 0 for z in edges):
        raise ValueError("Three finite nonzero scalar links are required for a loop phase")
    phase = -np.angle(edges[0])-np.angle(edges[1])+np.angle(edges[2])
    return float(np.angle(np.exp(1j*phase)))


def triadic_propagator_diagnosis():
    """Native block architecture, conditional realizations and loop-phase guards."""
    beta = 0.5493
    a1, a2, d = np.array([[0.5]]), np.array([[0.9]]), np.array([[3.0]])
    c, w1, w2 = 0.2+0j, 0.15+0j, 0.12+0j
    base = np.array([[a1[0, 0], c, w1.conjugate()],
                     [c.conjugate(), a2[0, 0], w2.conjugate()], [w1, w2, d[0, 0]]])
    frame_phases = np.array([math.pi*beta, -math.pi*beta, 0])
    chart = np.diag(np.exp(1j*frame_phases))
    shifted = chart.conj().T @ base @ chart
    energies, vectors = np.linalg.eigh(base)
    residuals = []
    for i in range(2):
        effective, _, _ = triadic_response(a1, a2, [[c]], [[w1]], [[w2]], d, energies[i])
        residuals.append(float(np.linalg.norm(effective @ vectors[:2, i]-energies[i]*vectors[:2, i])))

    loop_samples = []
    for phi in (0.0, 0.4, 0.9):
        w2_phi = w2*np.exp(1j*phi)
        full = base.copy()
        full[2, 1], full[1, 2] = w2_phi, w2_phi.conjugate()
        loop_samples.append({
            "loop_phase_radians": triadic_loop_phase(c, w1, w2_phi),
            "eigenvalues_in_declared_arbitrary_energy_units": np.linalg.eigvalsh(full).tolist(),
            "determinant_real": float(np.linalg.det(full).real),
        })

    theta = cyclic_candidate()[0]
    theta_target = matrix_diagnosis()["benchmark_phase_radians"]
    delta_theta = theta_target-theta
    # An existence witness, not a determination of the native triadic links.
    delta_c = c*(np.exp(1j*delta_theta)-1)
    witness_w1 = math.sqrt(float(d[0, 0].real)*abs(delta_c))
    witness_w2 = -d[0, 0]*delta_c/witness_w1
    effective, norm, response = triadic_response(
        a1, a2, [[c]], [[witness_w1]], [[witness_w2]], d)
    mu_ew = 1/math.sqrt(2*math.sqrt(2)*FERMI_GEV_MINUS_2)
    direct_link = mu_ew/math.sqrt(12)
    target_delta_link = 2*direct_link*abs(math.sin(delta_theta/2))
    mediated_link_bound = mu_ew**2/PLANCK_GEV

    # The prepared OP5 note uses a fixed probe exchange. Internal generations
    # are a separate tensor factor, not a relabelling of the three probes.
    eye, zero = np.eye(3), np.zeros((3, 3))
    exchange = np.block([[zero, eye, zero], [eye, zero, zero], [zero, zero, eye]])
    even = np.block([[eye/math.sqrt(2), zero], [eye/math.sqrt(2), zero], [zero, eye]])
    odd = np.vstack([eye/math.sqrt(2), -eye/math.sqrt(2), zero])
    visible_projector = even[:, :3] @ even[:, :3].conj().T
    gen_c, gen_mu, gen_gap = 0.2, 0.4, 3.0
    internal = []
    for phase in (theta, theta_target):
        b = normalized_cyclic_root(1/math.sqrt(2), phase)
        w = gen_mu*b/math.sqrt(2)
        full = np.block([[-gen_c*eye, gen_c*eye, w.conj().T],
                         [gen_c*eye, -gen_c*eye, w.conj().T], [w, w, gen_gap*eye]])
        compressed = even.conj().T @ full @ even
        light = -np.linalg.eigvalsh(compressed)[:3][::-1]
        q = np.linalg.eigvalsh(b.conj().T @ b)
        internal.append({
            "theta_radians": phase,
            "fixed_exchange_commutator_frobenius": float(np.linalg.norm(full @ exchange-exchange @ full, "fro")),
            "odd_even_coupling_frobenius": float(np.linalg.norm(odd.conj().T @ full @ even, "fro")),
            "visible_projector_commutator_frobenius": float(np.linalg.norm(
                full @ visible_projector-visible_projector @ full, "fro")),
            "compressed_gap_model_error_frobenius": float(np.linalg.norm(
                compressed-np.block([[zero, gen_mu*b.conj().T], [gen_mu*b, gen_gap*eye]]), "fro")),
            "light_magnitudes_arbitrary_energy_units": light.tolist(),
            "maximum_exact_mass_formula_error": float(np.max(np.abs(light-light_masses(q, gen_mu, gen_gap)))),
        })

    # Fixed-energy phase sensitivity of a two-mode complementary response.
    wc1 = np.array([[0.2], [0.15]])
    wc2 = np.array([[0.1], [0.12j]])
    dc = np.diag([3.0, 5.0])
    dd = np.diag([0.1, -0.07])
    r1, r2 = np.linalg.solve(dc, wc1), np.linalg.solve(dc, wc2)
    u = (wc1.conj().T @ r2)[0, 0]
    du = -(r1.conj().T @ dd @ r2)[0, 0]

    # Pole differentiation includes the norm derivative, not only delta A_eff.
    w = np.array([[w1, w2]])
    dw = np.array([[0.02, 0.01j]])
    da = np.array([[0.01, 0.005j], [-0.005j, 0.02]])
    delta_d = np.array([[0.1]])
    energy, x = energies[0], vectors[:2, 0]
    rw = np.linalg.solve(d-energy*np.eye(1), w)
    delta_n = dw.conj().T @ rw+rw.conj().T @ dw-rw.conj().T @ delta_d @ rw
    pole_norm = np.eye(2)+rw.conj().T @ rw
    pole_derivative = float((np.vdot(x, (da-delta_n) @ x)/np.vdot(x, pole_norm @ x)).real)
    delta_full = np.block([[da, dw.conj().T], [dw, delta_d]])
    full_derivative = float(np.vdot(vectors[:, 0], delta_full @ vectors[:, 0]).real)
    return {
        "status": "exact conditional triadic elimination; native coefficients and phase not identified",
        "native_source_labels": ["prop:triadic-two-probe", "thm:master-field-equation", "thm:variational-form"],
        "source_block_dictionary": {
            "C12": "g_Y T_12, with the reverse block its adjoint",
            "Wi": "chi T_perp_i, on a declared common positive carrier",
            "D": "Omega_perp, assumed Hermitian and gapped for this calculation",
            "effective_link": "C12_eff(E)=C12-W1* (D-E I)^(-1) W2",
            "joint_positive_response": "N_ij(E)=Wi* (D-E I)^(-1) Wj",
            "joint_norm_response": "K_eff(E)=I+[Wi* (D-E I)^(-2) Wj]_ij",
            "probe_slots_not_automatically_generations_or_physical_frames": True,
        },
        "exact_pole_test_arbitrary_energy_units": {
            "full_eigenvalues": energies.tolist(),
            "low_pole_schur_residuals": residuals,
            "not_a_charged_lepton_prediction": True,
        },
        "independent_frame_rephasing_test": {
            "illustrative_frame_phases": frame_phases.tolist(),
            "not_a_source_derived_three_link_phase_law": True,
            "maximum_eigenvalue_difference": float(np.max(np.abs(np.linalg.eigvalsh(shifted)-energies))),
            "oriented_loop_phase_after_rephasing": triadic_loop_phase(shifted[0, 1], shifted[2, 0], shifted[2, 1]),
            "pure_endpoint_differences_have_zero_cycle_sum": True,
        },
        "fixed_moduli_nontrivial_loop_examples": loop_samples,
        "cyclic_root_loop_requirement": {
            "scope": "only if a generation embedding identifies the native cycle with the declared cyclic B",
            "orientation": "Phi_B=arg(B_10 B_21 B_02)=3 theta modulo 2pi",
            "baseline_loop_phase_radians": float(np.angle(np.exp(3j*theta))),
            "benchmark_calibrated_loop_phase_radians": float(np.angle(np.exp(3j*theta_target))),
            "benchmark_calibrated_loop_phase_change_radians": 3*delta_theta,
            "benchmark_calibrated_loop_phase_change_degrees": math.degrees(3*delta_theta),
            "not_a_native_phase_prediction": True,
        },
        "phase_rotated_link_existence_witness": {
            "scope": "arbitrary energy units, at E=0, fitted link rotation only; not a three-generation fit",
            "effective_link_real": float(effective[0, 1].real),
            "effective_link_imag": float(effective[0, 1].imag),
            "target_link_real": float((c*np.exp(1j*delta_theta)).real),
            "target_link_imag": float((c*np.exp(1j*delta_theta)).imag),
            "mandatory_diagonal_response": np.diag(response).real.tolist(),
            "mandatory_norm_response_eigenvalues": np.linalg.eigvalsh(norm).tolist(),
            "response_determinant_real": float(np.linalg.det(response).real),
            "zero_mode_roundoff_tolerance": 1e-15,
            "cauchy_schwarz_saturated": True,
            "diagonal_terms_cannot_be_discarded": True,
        },
        "conditional_planck_mediator_phase_bound": {
            "assumptions": "scalar links |W1|,|W2|<=mu_EW, D=Planck, E=0, |C12|=mu_EW/sqrt(12)",
            "largest_mediated_link_GeV": mediated_link_bound,
            "max_phase_change_radians_bound": math.asin(mediated_link_bound/direct_link),
            "benchmark_calibrated_fixed_modulus_link_change_GeV": target_delta_link,
            "link_change_shortfall_factor": target_delta_link/mediated_link_bound,
            "does_not_exclude_other_gaps_or_couplings": True,
        },
        "source_connection_route": {
            "connection": "Gamma_mu=i A_mu+kappa H_C n_mu+eta (I-P) n_mu",
            "curvature_named_in_source": "F_mu_nu=[D_mu,D_nu]",
            "unitary_holonomy_requires_metric_compatibility_not_established": True,
            "conditional_abelian_loop": "U_loop=exp(-i integral_Sigma f), only for a norm-preserving Abelian connection on a declared contractible loop",
            "not_identified_with_gravitational_riemann_curvature": True,
            "reference": "https://www.damtp.cam.ac.uk/user/tong/gaugetheory/2ym.pdf",
        },
        "prepared_op5_interface": {
            "source": "analysis/OP5_QAM_Residual_Lift.tex",
            "sections": ["sec:native-triadic-phase-metric-test", "sec:native-normalized-readout", "sec:hc-even-slow-supply"],
            "relay_and_loop_phase_already_prepared": True,
            "scalar_fixed_exchange_requires": "A1=A2, C12 real, W1=W2; scalar loop phase then 0 or pi",
            "native_global_involution_not_identified_with_probe_exchange": True,
        },
        "internal_generation_tensor_witness": {
            "scope": "conditional 3 probe slots tensor 3 internal generations; not a native embedding",
            "common_source_legs": "W1=W2=mu B(theta)/sqrt(2); A1=A2=-c I; C12=c I; D=Delta I",
            "canonical_equal_leg_scale_identity": "mu=sqrt(2)*abs(chi)*||T_perp1||_F when W1=W2=chi*T_perp1",
            "common_scalar_chi_phase_cancels_from_normalized_gram": True,
            "arbitrary_energy_units": {"c": gen_c, "mu": gen_mu, "Delta": gen_gap},
            "phase_samples": internal,
            "preserves_declared_fixed_exchange_not_all_native_guards": True,
            "visible_three_generation_projector_not_invariant": True,
            "phase_and_zero_direct_block_are_chosen_not_derived": True,
        },
        "gap_to_phase_derivative_example": {
            "scope": "fixed scalar probe vertices, two hidden modes, arbitrary energy units, at E=0",
            "direct_link_real": c.real,
            "indirect_link_real": float(u.real), "indirect_link_imag": float(u.imag),
            "d_loop_phase_per_parameter": float(np.imag(du/u)),
            "d_effective_link_phase_per_parameter": float(np.imag(-du/(c-u))),
            "one_scalar_positive_gap_cannot_rotate_indirect_phase_by_itself": True,
            "two_modes_can_rotate_indirect_phase_by_changing_relative_real_gaps": True,
            "native_curvature_or_parameter_not_evaluated": True,
        },
        "pole_response_example": {
            "scope": "simple low pole in the declared toy triad; not a physical lepton shift",
            "formula": "delta E = x*(delta A-delta N_fixed_E)x / x*(I+N'(E))x",
            "schur_pole_derivative": pole_derivative,
            "full_hamiltonian_derivative": full_derivative,
            "absolute_derivative_difference": abs(pole_derivative-full_derivative),
        },
        "remaining_free_native_data": [
            "represented generation/sector embedding and adjoint conventions",
            "g_Y T_12, chi T_perp_1, chi T_perp_2 and Omega_perp",
            "phase-sensitive action or evaluated connection/transport paths",
            "canonical chiral mass and kinetic matching, including diagonal terms",
        ],
    }


def evaluate():
    theta, b, qmatrix = cyclic_candidate()
    q = np.linalg.eigvalsh(qmatrix)
    ratios = q/q[-1]
    benchmark = HISTORICAL_MASSES_MEV/HISTORICAL_MASSES_MEV[-1]
    v_fermi = 1/math.sqrt(math.sqrt(2)*FERMI_GEV_MINUS_2)
    mu_ew = v_fermi/math.sqrt(2)
    tau_gev = HISTORICAL_MASSES_MEV[-1]/1000
    calibrated_mu = math.sqrt(tau_gev*(tau_gev+PLANCK_GEV)/q[-1])
    calibrated_gap = mu_ew**2*q[-1]/tau_gev-tau_gev
    return {
        "status": "conditional effective candidate; not native identification",
        "assumptions": [
            "orthogonal common carrier with three normalized closed seeds",
            "cyclic Hermitian root coupling with r/a=1/sqrt(2), not derived",
            "inherited theta=pi-sqrt(2)*asin(beta), not derived",
            "rounded inherited beta=0.5493; not a first-principles extraction",
            "Tr(B*B)=1 is a normalization convention, not a physical scale",
            "flat positive complementary gap and zero direct mass block",
            "V=mu*B is an added field/pacer identification",
        ],
        "beta": 0.5493, "theta_radians": theta,
        "B_real": b.real.tolist(), "B_imag": b.imag.tolist(),
        "Q_real": qmatrix.real.tolist(), "Q_imag": qmatrix.imag.tolist(),
        "q_eigenvalues_ascending": q.tolist(),
        "leading_ratios_to_largest": ratios.tolist(),
        "leading_koide_diagnostic": koide_diagnostic(q),
        "historical_comparison_only": {
            "quoted_masses_MeV": HISTORICAL_MASSES_MEV.tolist(),
            "ratios_to_largest": benchmark.tolist(),
            "relative_ratio_errors": (ratios/benchmark-1).tolist(),
            "no_positive_flat_gap_scale_fit_for_fixed_shape": bool(ratios[1] > benchmark[1]),
            "reason": "Exact positive-gap corrections increase every smaller/largest ratio",
        },
        "external_references": {
            "planck_GeV": PLANCK_GEV, "fermi_GeV_minus_2": FERMI_GEV_MINUS_2,
            "defined_v_F_GeV": v_fermi,
            "defined_electroweak_mixing_reference_GeV": mu_ew,
            "sources": REFERENCE_SOURCES,
        },
        "illustrative_not_derived_scale_choices": {
            "planck_gap_planck_mixing": scale_scenario(q, PLANCK_GEV, PLANCK_GEV),
            "planck_gap_electroweak_mixing": scale_scenario(q, mu_ew, PLANCK_GEV),
        },
        "one_mass_calibrations_not_predictions": {
            "planck_gap_tau_calibrated_mixing": scale_scenario(q, calibrated_mu, PLANCK_GEV),
            "electroweak_mixing_tau_calibrated_gap": scale_scenario(q, mu_ew, calibrated_gap),
        },
        "posthoc_matrix_diagnosis_not_prediction": matrix_diagnosis(),
        "planck_assumption_diagnosis": planck_diagnosis(),
        "tensor_shift_diagnosis": tensor_shift_diagnosis(),
        "physical_origin_diagnosis": physical_origin_diagnosis(),
        "triadic_propagator_diagnosis": triadic_propagator_diagnosis(),
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
