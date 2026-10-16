"""Conditional HC/coframe geometry and null stress matching, not full native gravity."""
import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "geometry_real_probe", Path(__file__).with_name("HC_Real_Probe_Current_Closure.py"))
probe = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(probe)
curvature = probe.curvature
ETA = curvature.METRIC
N_COV = curvature.NULL_COVECTOR
L_VECTOR = ETA @ N_COV
PAULI = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]])


def spin_weights():
    beta = np.diag([1.0, 1.0, -1.0, -1.0])
    zero = np.zeros((2, 2))
    weights = np.array([np.eye(4), *[np.block([[zero, sigma], [sigma, zero]]) for sigma in PAULI]])
    return weights, beta


def timelike_current_spinor(current):
    """One smooth positive-time Dirac realization of a strictly timelike current."""
    current = curvature._real(current, (4,), "frame current")
    m2 = current[0]**2-current[1:] @ current[1:]
    if current[0] <= 0 or m2 <= 0:
        raise ValueError("A strictly future timelike frame current required")
    norm = np.sqrt(m2)
    denominator = current[0]+norm
    denominator_derivative = np.eye(4)[0]+np.r_[current[0], -current[1:]]/norm
    amplitude = np.sqrt(denominator/2)
    amplitude_derivative = denominator_derivative/(4*amplitude)
    chi = np.array([1.0, 0.0])
    spatial = np.einsum("i,ijk,k->j", current[1:], PAULI, chi)
    spatial_derivative = np.vstack([np.zeros(2), PAULI @ chi])
    state = np.r_[amplitude*chi, amplitude*spatial/denominator]
    upper = np.outer(amplitude_derivative, chi)
    lower = np.outer(amplitude_derivative/denominator-amplitude*denominator_derivative/denominator**2, spatial)
    lower += amplitude*spatial_derivative/denominator
    return state, np.concatenate([upper, lower], axis=1)


def probe_coframe(psi, derivatives, gauge, hc, weights, spin_metric, n_covector, coupling):
    psi, gauge, hc, weights, _ = probe._fields(psi, gauge, hc, weights, spin_metric)
    derivatives = probe._derivatives(derivatives, psi)
    n, coupling = curvature._real(n_covector, (4,), "axis covector"), curvature._scalar(coupling, "coupling")
    covariant = derivatives+1j*gauge @ psi+coupling*n[:, None, None]*(hc @ psi)
    coframe = np.array([[np.vdot(psi, derivative @ weight.T).real
                         for derivative in covariant] for weight in weights])
    baseline = np.array([[np.vdot(psi, derivative @ weight.T).real
                          for derivative in derivatives] for weight in weights])
    direction = np.array([np.vdot(psi, hc @ psi @ weight.T).real for weight in weights])
    return {"coframe": coframe, "baseline": baseline, "direction": direction,
            "metric": coframe.T @ ETA @ coframe}


def rank_one_update(background, direction, n_covector, coupling):
    background = curvature._real(background, (4, 4), "baseline coframe")
    direction = curvature._real(direction, (4,), "frame direction")
    n, coupling = curvature._real(n_covector, (4,), "axis covector"), curvature._scalar(coupling, "coupling")
    if np.linalg.matrix_rank(background) != 4:
        raise ValueError("An invertible baseline coframe required for inverse/determinant identities")
    axis_vector = np.linalg.solve(background, direction)
    denominator = float(1+coupling*n @ axis_vector)
    if abs(denominator) < 1e-12:
        raise ValueError("The updated coframe is singular at this rank-one denominator")
    coframe = background+coupling*np.outer(direction, n)
    baseline_metric = background.T @ ETA @ background
    w = background.T @ ETA @ direction
    expanded = (baseline_metric+coupling*(np.outer(n, w)+np.outer(w, n))
                +coupling**2*(direction @ ETA @ direction)*np.outer(n, n))
    inverse_coframe = (np.eye(4)-coupling*np.outer(axis_vector, n)/denominator) @ np.linalg.inv(background)
    return {"coframe": coframe, "metric": coframe.T @ ETA @ coframe, "expanded_metric": expanded,
            "inverse_metric": inverse_coframe @ ETA @ inverse_coframe.T,
            "determinant_factor": denominator, "baseline_metric": baseline_metric,
            "baseline_null_square": float(n @ np.linalg.solve(baseline_metric, n)),
            "updated_null_square_prediction": float(n @ np.linalg.solve(baseline_metric, n)/denominator**2)}


def constructive_probe(point, hc_amplitude, coupling, time_offset=3.0):
    """Realize E0=I and v_H=h l with the SAME local triadic amplitudes; off shell."""
    point = curvature._real(point, (4,), "spacetime point")
    hc_amplitude = curvature._scalar(hc_amplitude, "HC amplitude")
    time_offset = curvature._scalar(time_offset, "current time offset")
    weights, beta = spin_weights()
    total_current = 2*(point+np.array([time_offset, 0, 0, 0]))
    second, second_derivative = timelike_current_spinor(total_current-L_VECTOR)
    psi = np.array([[1, 0, 1, 0], np.zeros(4), np.zeros(4)], dtype=complex)/np.sqrt(2)
    psi[1] = second
    derivatives = np.zeros((4, 3, 4), dtype=complex)
    derivatives[:, 1, :] = 2*second_derivative
    gauge = np.zeros((4, 3, 3), dtype=complex)
    hc = np.diag([hc_amplitude, 0.0, 0.0])
    reading = probe_coframe(psi, derivatives, gauge, hc, weights, beta, N_COV, coupling)
    currents = probe.probe_currents(psi, weights, beta)
    return {**reading, "psi": psi, "derivatives": derivatives, "hc": hc, "gauge": gauge,
            "weights": weights, "spin_metric": beta,
            "frame_current": np.trace(currents["gauge"], axis1=-2, axis2=-1).real,
            "unsatisfied_zero_gauge_Gauss_source_norm": float(np.linalg.norm(currents["gauge"][0]))}


def metric_curvature(metric, first, second):
    """R^a_bcd=[nabla_c,nabla_d]^a_b from independent analytic metric jets."""
    metric = curvature._real(metric, (4, 4), "metric")
    first = curvature._real(first, (4, 4, 4), "metric first derivative")
    second = curvature._real(second, (4, 4, 4, 4), "metric second derivative")
    if (not np.allclose(metric, metric.T, atol=1e-12, rtol=0) or np.linalg.matrix_rank(metric) != 4
            or not np.allclose(first, first.swapaxes(1, 2), atol=1e-12, rtol=0)
            or not np.allclose(second, second.swapaxes(0, 1), atol=1e-12, rtol=0)
            or not np.allclose(second, second.swapaxes(2, 3), atol=1e-12, rtol=0)):
        raise ValueError("A nondegenerate symmetric metric and consistent symmetric metric jets required")
    inverse = np.linalg.inv(metric)
    inverse_first = -np.einsum("ap,lpq,qb->lab", inverse, first, inverse)
    lower_connection = np.empty((4, 4, 4))
    lower_derivative = np.empty((4, 4, 4, 4))
    for a, b, c in np.ndindex((4, 4, 4)):
        lower_connection[a, b, c] = (first[b, a, c]+first[c, a, b]-first[a, b, c])/2
        for d in range(4):
            lower_derivative[d, a, b, c] = (second[d, b, a, c]+second[d, c, a, b]-second[d, a, b, c])/2
    connection = np.einsum("ad,dbc->abc", inverse, lower_connection)
    connection_derivative = (np.einsum("lad,dbc->labc", inverse_first, lower_connection)
                             +np.einsum("ad,ldbc->labc", inverse, lower_derivative))
    riemann = np.empty((4, 4, 4, 4))
    for a, b, c, d in np.ndindex((4, 4, 4, 4)):
        riemann[a, b, c, d] = (connection_derivative[c, a, d, b]-connection_derivative[d, a, c, b]
                               +connection[a, c, :] @ connection[:, d, b]
                               -connection[a, d, :] @ connection[:, c, b])
    ricci = np.einsum("abad->bd", riemann)
    scalar = float(np.einsum("ab,ab", inverse, ricci))
    return {"connection": connection, "connection_derivative": connection_derivative,
            "riemann": riemann, "lower_riemann": np.einsum("ae,ebcd->abcd", metric, riemann),
            "ricci": ricci, "scalar": scalar, "einstein": ricci-metric*scalar/2}


def null_geometry(amplitude, gradient, hessian, coupling, trace_t_squared=1.0):
    """Transverse h(x,y), independent-metric paired-curvature stress, no other sources."""
    amplitude, coupling = curvature._scalar(amplitude, "HC amplitude"), curvature._scalar(coupling, "coupling")
    trace_t_squared = curvature._scalar(trace_t_squared, "Tr(T^2)")
    gradient = curvature._real(gradient, (2,), "transverse gradient")
    hessian = curvature._real(hessian, (2, 2), "transverse Hessian")
    if trace_t_squared <= 0 or not np.allclose(hessian, hessian.T, atol=1e-12, rtol=0):
        raise ValueError("A positive generator trace and symmetric transverse Hessian required")
    full_gradient, full_hessian = np.zeros(4), np.zeros((4, 4))
    full_gradient[1:3], full_hessian[1:3, 1:3] = gradient, hessian
    nn = np.outer(N_COV, N_COV)
    metric = ETA+2*coupling*amplitude*nn
    first = 2*coupling*np.einsum("l,mn->lmn", full_gradient, nn)
    second = 2*coupling*np.einsum("ls,mn->lsmn", full_hessian, nn)
    geometry = metric_curvature(metric, first, second)
    inverse = np.linalg.inv(metric)
    f = coupling*(np.outer(full_gradient, N_COV)-np.outer(N_COV, full_gradient))
    f_squared = float(np.einsum("ab,ac,bd,cd", f, inverse, inverse, f))
    stress = trace_t_squared*(f @ inverse @ f.T-metric*f_squared/4)
    return {**geometry, "metric": metric, "metric_first": first, "metric_second": second,
            "hc_curvature": f, "hc_curvature_squared_trace": trace_t_squared*f_squared,
            "hc_stress": stress, "ricci_coefficient": float(-coupling*np.trace(hessian)),
            "stress_coefficient": float(coupling**2*trace_t_squared*(gradient @ gradient)),
            "restricted_metric_tangent": 2*coupling*nn}


def logarithmic_profile(xy, coupling, einstein_coupling, trace_t_squared=1.0,
                        intercept=2.0, slope=(0.1, 0.0)):
    """Solve Delta h+a|grad h|^2=0 locally via exp(a h)=positive affine harmonic F."""
    xy, slope = curvature._real(xy, (2,), "transverse position"), curvature._real(slope, (2,), "affine slope")
    coupling, einstein_coupling, trace_t_squared, intercept = [curvature._scalar(value, "profile coefficient")
                                                             for value in [coupling, einstein_coupling, trace_t_squared, intercept]]
    a = einstein_coupling*coupling*trace_t_squared
    harmonic = float(intercept+slope @ xy)
    if a == 0 or trace_t_squared <= 0 or harmonic <= 0:
        raise ValueError("Nonzero a=kappa_eff kappa Tr(T^2), positive trace and positive affine harmonic F required")
    return {"amplitude": float(np.log(harmonic)/a), "gradient": slope/(a*harmonic),
            "hessian": -np.outer(slope, slope)/(a*harmonic**2), "a": a, "harmonic": harmonic}


def geometric_hc_source(psi, weights, spin_metric, coframe, einstein_residual_up, n_covector, coupling):
    """Metric-action chain rule at fixed Psi,n and fixed internal/spin comparison."""
    coframe = curvature._real(coframe, (4, 4), "coframe")
    residual = curvature._real(einstein_residual_up, (4, 4), "symmetric metric Euler tensor")
    n, coupling = curvature._real(n_covector, (4,), "axis covector"), curvature._scalar(coupling, "coupling")
    if not np.allclose(residual, residual.T, atol=1e-12, rtol=0):
        raise ValueError("A symmetric metric Euler tensor required")
    currents = probe.probe_currents(psi, weights, spin_metric)["gauge"]
    coefficients = ETA @ coframe @ residual @ n
    return coupling*np.einsum("a,aij->ij", coefficients, currents)


def coordinate_current_balance(frame_current, current_derivative, coframe, coframe_derivative):
    """J^mu=e_a^mu j^a and div J=(1/|det E|)partial_mu(|det E|J^mu)."""
    current = curvature._real(frame_current, (4,), "frame current")
    derivative = curvature._real(current_derivative, (4, 4), "current derivative [coordinate,frame]")
    coframe = curvature._real(coframe, (4, 4), "coframe")
    de = curvature._real(coframe_derivative, (4, 4, 4), "coframe derivative [coordinate,frame,coordinate]")
    if np.linalg.matrix_rank(coframe) != 4:
        raise ValueError("An invertible coframe required for the induced coordinate current")
    inverse = np.linalg.inv(coframe)
    coordinate_current = inverse @ current
    inverse_derivative = -np.einsum("ma,lav,vb->lmb", inverse, de, inverse)
    coordinate_derivative = (np.einsum("lma,a->lm", inverse_derivative, current)
                              +np.einsum("ma,la->lm", inverse, derivative))
    log_volume_derivative = np.einsum("ma,lam->l", inverse, de)
    divergence = float(np.trace(coordinate_derivative)+log_volume_derivative @ coordinate_current)
    return {"current": coordinate_current, "current_derivative": coordinate_derivative,
            "volume": float(abs(np.linalg.det(coframe))), "divergence": divergence}


def induced_dirac_contraction(psi, covariant_derivatives, frame_gamma, spin_metric,
                              resonance_image, coframe_scale=1.0):
    """Same-frame algebra only; does NOT assume the native paper already identifies these gammas."""
    psi = curvature._finite(psi, "probe")
    beta = probe.sources._hermitian(spin_metric, "Spin adjoint")
    gamma = curvature._finite(frame_gamma, "frame gamma matrices")
    dcov = probe._derivatives(covariant_derivatives, psi)
    image = curvature._finite(resonance_image, "Omega Psi")
    scale = curvature._scalar(coframe_scale, "coframe normalization")
    if (psi.ndim != 2 or psi.shape[0] == 0 or psi.shape[1] != beta.shape[0]
            or gamma.shape != (4, *beta.shape) or image.shape != psi.shape or scale == 0
            or np.linalg.matrix_rank(beta) != beta.shape[0]):
        raise ValueError("Compatible finite probe/gamma/adjoint/image data and nonzero normalization required")
    weights = beta @ gamma
    coframe = scale*np.array([[np.vdot(psi, derivative @ k.T).real for derivative in dcov] for k in weights])
    if np.linalg.matrix_rank(coframe) != 4:
        raise ValueError("The real bilinear coframe is degenerate; no same-frame inverse exists")
    inverse = np.linalg.inv(coframe)
    coordinate_gamma = np.einsum("ma,aij->mij", inverse, gamma)
    slash = sum(derivative @ g.T for derivative, g in zip(dcov, coordinate_gamma))
    residual = 1j*slash-image
    scalar_residual = complex(np.vdot(psi, residual @ beta.T))
    scalar_mass = complex(np.vdot(psi, image @ beta.T))
    target = 4/scale-scalar_mass.imag
    dual_norm = float(np.linalg.norm(psi @ beta.T))
    return {"coframe": coframe, "coordinate_gamma": coordinate_gamma, "slash": slash,
            "probe_residual": residual, "scalar_residual": scalar_residual,
            "scalar_mass": scalar_mass, "imaginary_residual_prediction": float(target),
            "coframe_trace": float(np.einsum("ma,am", inverse, coframe)),
            "residual_norm": float(np.linalg.norm(residual)),
            "residual_norm_lower_bound": float(abs(target)/dual_norm)}


def evaluate():
    coupling, einstein_coupling, trace = 0.4, 1.0, 1.0
    point = np.array([0.0, 0.2, 0.3, 0.0])
    profile = logarithmic_profile(point[1:3], coupling, einstein_coupling, trace)
    geometry = null_geometry(profile["amplitude"], profile["gradient"], profile["hessian"], coupling, trace)
    witness = constructive_probe(point, profile["amplitude"], coupling)
    frame_n = np.linalg.solve(witness["coframe"].T, N_COV)
    null_slash = np.einsum("a,aij->ij", frame_n, witness["weights"])
    hc_probe_image = witness["hc"] @ witness["psi"] @ null_slash.T
    dcov = witness["derivatives"]+coupling*N_COV[:, None, None]*(witness["hc"] @ witness["psi"])
    resonance_image = 0.6*witness["psi"]+0.2*witness["hc"] @ witness["psi"]
    trace_check = induced_dirac_contraction(witness["psi"], dcov,
                                            witness["spin_metric"] @ witness["weights"],
                                            witness["spin_metric"], resonance_image)
    h_gradient = np.r_[0.0, profile["gradient"], 0.0]
    coframe_derivative = coupling*np.einsum("l,a,m->lam", h_gradient, L_VECTOR, N_COV)
    continuity = coordinate_current_balance(witness["frame_current"], 2*np.eye(4),
                                             witness["coframe"], coframe_derivative)
    mismatch = geometry["einstein"]-einstein_coupling*geometry["hc_stress"]
    off_shell = null_geometry(0.7, [0.02, -0.03], [[0.1, 0], [0, -0.1]], coupling, trace)
    off_residual = off_shell["einstein"]-einstein_coupling*off_shell["hc_stress"]
    inverse = np.linalg.inv(off_shell["metric"])
    raised_residual = inverse @ off_residual @ inverse
    tangent_contraction = float(np.einsum("ab,ab", raised_residual, off_shell["restricted_metric_tangent"])/2)
    return {
        "status": "conditional coframe geometry/stress match, now strengthened by current and same-frame exclusion; NOT a full native solution",
        "native_anchor": "v470/10_sphaera_and_physics.tex, prop:bilinear-einstein-reconstruction: E^a_mu=Re(bar(Psi) Gamma^a D_mu Psi), g=E^T eta E",
        "standard_factorized_branch": {
            "assumptions": "fixed Hermitian K^a=eta_D Gamma^a, Hermitian internal A,H commuting with spin, constant n, no closure load in this isolated calculation",
            "identity": "E^a_mu=partial_mu j^a/2+kappa n_mu v_H^a; j^a=bar(Psi)Gamma^a Psi, v_H^a=bar(Psi)Gamma^a H Psi",
            "internal_unitary_gauge_A_drops_from_this_real_coframe": True,
            "HC_survives_here_although_its_i_weighted_probe_transport_drops_from_real_action": True,
            "HC_free_nonzero_rank_case": "E=d(j/2) is an exact coframe; if rank four, g is locally flat in coordinates Y=j/2",
            "not_a_flatness_theorem_for_varying_spin_frames_spin_connections_or_nonfactorized_native_carriers": True,
        },
        "rank_one_geometry": {
            "coframe": "E=E0+kappa v n^T",
            "metric": "g=g0+kappa(n w^T+w n^T)+kappa^2(v^T eta v)n n^T, w=E0^T eta v",
            "determinant": "det E=det E0 [1+kappa n^T E0^(-1)v]",
            "null_axis_preservation": "n^T g^(-1)n=[n^T g0^(-1)n]/[1+kappa n^T E0^(-1)v]^2",
            "rank_one_HC_alone_does_not_supply_a_rank_four_coframe": True,
            "anholonomy_dE_nonzero_does_not_alone_prove_Riemann_curvature": True,
        },
        "same_probe_constructive_local_witness": {
            "representation": "three internal four-spinor amplitudes, a valid declared 3+1 Clifford test; NOT matched to native C7/M16",
            "frame_current": witness["frame_current"].tolist(),
            "baseline_E_minus_identity_norm": float(np.linalg.norm(witness["baseline"]-np.eye(4))),
            "HC_direction_minus_h_l_norm": float(np.linalg.norm(witness["direction"]-profile["amplitude"]*L_VECTOR)),
            "coframe_metric_match_error": float(np.linalg.norm(witness["metric"]-geometry["metric"])),
            "positive_HC_at_sample": bool(profile["amplitude"] > 0),
            "same_null_covector_in_induced_frame_error": float(np.linalg.norm(frame_n-N_COV)),
            "raw_HC_probe_transport_image_norm": float(np.linalg.norm(hc_probe_image)),
            "geometrically_active_but_direct_probe_transport_dark_on_this_ansatz": True,
            "mass_like_and_other_evolution_can_break_that_alignment": True,
            "unsatisfied_zero_gauge_Gauss_source_norm": witness["unsatisfied_zero_gauge_Gauss_source_norm"],
            "probe_gauge_projector_and_matching_equations_not_solved": True,
        },
        "local_null_geometry_and_stress": {
            "null_profile": "E=I+kappa h l n^T, l=eta^(-1)n, n=(-1,0,0,1), h=h(x,y)",
            "metric": "g=eta+2kappa h n n^T; det g=-1 and n remains null",
            "curvature": "Ricci_mu_nu=-kappa Delta_perp h n_mu n_nu, R=0; full Riemann need not vanish",
            "stress_assumptions": "paired curvature action, independent unconstrained metric variation at fixed n and F, then evaluate on the null branch",
            "HC_stress": "T_mu_nu=kappa^2 Tr(T^2)|grad_perp h|^2 n_mu n_nu",
            "adding_a_metric_null_constraint_or_other_metric_dependencies_changes_variation": True,
            "n_is_parallel_in_this_specific_metric": True,
            "conditional_Einstein_match": "Delta_perp h+a|grad_perp h|^2=0, a=kappa_eff kappa Tr(T^2)",
            "linearization": "Delta_perp exp(a h)=0 for a!=0",
            "profile": "h=log(F0+b.x)/a on a patch with F0+b.x>0, and h>=0 if desired",
            "dimensionless_kappa": coupling,
            "unevaluated_independent_Einstein_coupling_example": einstein_coupling,
            "sample_h": profile["amplitude"],
            "sample_Ricci_coefficient": geometry["ricci_coefficient"],
            "sample_HC_stress_coefficient": geometry["stress_coefficient"],
            "Einstein_minus_kappa_eff_HC_stress_norm": float(np.linalg.norm(mismatch)),
            "sample_scalar_curvature": geometry["scalar"],
            "sample_Riemann_component_norm_not_a_scalar_invariant": float(np.linalg.norm(geometry["lower_riemann"])),
            "cosmological_probe_penalty_and_other_stresses_omitted_in_this_matching_exercise": True,
        },
        "variation_boundary": {
            "metric_convention": "delta S_metric=integral sqrt|g| E^{mu nu} delta g_mu_nu/2",
            "HC_metric_source": "delta_H S_metric=kappa integral sqrt|g| n_mu E^{mu nu} eta_ab E^a_nu Tr(j^b delta H)",
            "same_null_ansatz_warning": "R and Tr(F^dagger F) both vanish on this profile family; restricting the action first loses the remaining Einstein equation",
            "nonmatching_example_full_residual_norm": float(np.linalg.norm(off_residual)),
            "same_example_restricted_metric_variation": tangent_contraction,
            "independent_Einstein_matching_is_stronger_than_the_HC_tangent_equation": True,
        },
        "follow_through_current_and_same_frame_obstruction": {
            "strengthening_of_previous_gap": "A=0 is not the only issue: this unchanged probe/current ansatz is not repaired by an internal unitary gauge field alone",
            "induced_current": "J^mu=(E^(-1))^mu_a j^a; divergence uses |det E|, not only flat-frame component derivatives",
            "example_induced_current": continuity["current"].tolist(),
            "example_covariant_divergence": continuity["divergence"],
            "gradient_coframe_branch": "If E=d(j/2) is invertible and J=e j, then in Y=j/2 coordinates div J=8, not 0",
            "aligned_transverse_branch": "j=2(x+c), E=I+kappa h l n^T, h transverse and n.l=0 also gives div J=8",
            "gauge_commutator_trace_cannot_cancel_this": True,
            "same_frame_extra_assumption": "Gamma^mu=(E^(-1))^mu_a Gamma^a in the SAME ordered master equation and coframe, with SAME Psi, adjoint and D_mu",
            "pointwise_identity": "Im[bar(Psi) R]=4/s-Im[bar(Psi)Omega Psi], R=(i Gamma^mu D_mu-Omega)Psi, E=s Re(bar(Psi)Gamma^a D_mu Psi)",
            "on_shell_requirement": "Im[bar(Psi)Omega Psi]=4/s for finite nonzero real s",
            "real_mass_bilinear_obstruction": "If bar(Psi)Omega Psi is real, no full-rank same-frame solution exists under these assumptions, independently of the detailed connection",
            "sample_scalar_mass_imaginary": trace_check["scalar_mass"].imag,
            "sample_Im_barPsi_R": trace_check["scalar_residual"].imag,
            "sample_probe_residual_norm": trace_check["residual_norm"],
            "sample_residual_norm_lower_bound": trace_check["residual_norm_lower_bound"],
            "not_a_global_no_go_for_the_paper": "The source does not yet fix the microscopic Gamma^mu to the induced inverse coframe. Separate effective/microscopic geometries, a different coframe or altered equations must be stated and checked, not silently identified.",
            "connection_spin_frame_changes_alone_do_not_evade_the_trace_identity_when_all_same_frame_assumptions_remain": True,
            "nonreal_mass_or_different_coframe_is_a_real_model_change_not_an_automatic_fix": True,
        },
        "native_scope_boundary": {
            "exact_minimal_closure": "R_C=0 with the minimal functional implies H_C=0; a nonzero HC geometric profile is NOT that exact native Einstein-limit branch",
            "other_possible_curvature_sources": "kinematically: geometric spin connection, varying Clifford/adjoint data, nonfactorized transport, or a justified independent/deeper HC completion; none automatically evades the on-shell same-frame trace identity",
            "full_variation": "if g is defined by the probes, pull back the metric action to ALL fields, or impose its definition with multipliers; do not also vary it freely without justification",
            "coordinate_gamma_and_geometric_spin_connection_require_the_same_induced_frame": True,
            "previous_same_frame_requirement_scope": "This is the tested direct induced-geometric Dirac interpretation, not an identification already derived for all native microscopic/effective gammas",
            "same_induced_gamma_identification_is_now_explicitly_tested_and_obstructed_for_real_mass_bilinear": True,
            "no_native_G_Newton_mass_phase_gravitational_bath_or_full_solution_derived": True,
        },
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
