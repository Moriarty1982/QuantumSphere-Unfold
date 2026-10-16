"""Two-frame trace tests and an explicitly modified neutral affine-coframe model."""
import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "two_frame_geometry", Path(__file__).with_name("HC_Bilinear_Geometry_Bridge.py"))
geometry = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(geometry)
checks = geometry.curvature


def _frame(value, name):
    value = checks._real(value, (4, 4), name)
    if np.linalg.matrix_rank(value) != 4:
        raise ValueError(f"An invertible {name} required")
    return value


def relative_frame(coframe, reference):
    coframe = checks._real(coframe, (4, 4), "coframe")
    reference = _frame(reference, "reference coframe")
    relative = np.linalg.solve(reference.T, coframe.T).T
    defect = relative-np.eye(4)
    trace = float(np.trace(relative))
    return {"relative": relative, "trace": trace,
            "distance_frobenius": float(np.linalg.norm(defect)),
            "distance_operator": float(np.linalg.norm(defect, ord=2)),
            "trace_bound_frobenius": abs(trace-4)/2,
            "trace_bound_operator": abs(trace-4)/4}


def mixed_probe_trace(psi, derivatives, frame_gamma, spin_metric, resonance_image,
                      reference=None, background=None, scale=1.0):
    """First-jet identity, not a construction of a native global probe solution."""
    psi = checks._finite(psi, "probe")
    beta = geometry.probe.sources._hermitian(spin_metric, "spin adjoint")
    gamma = checks._finite(frame_gamma, "frame gamma")
    image = checks._finite(resonance_image, "resonance image")
    scale = checks._scalar(scale, "coframe normalization")
    if (psi.ndim != 2 or psi.shape[0] == 0 or psi.shape[1] != len(beta)
            or gamma.shape != (4, *beta.shape) or image.shape != psi.shape or scale == 0):
        raise ValueError("Compatible probe, gamma, image and nonzero normalization required")
    dcov = geometry.probe._derivatives(derivatives, psi)
    reference = _frame(np.eye(4) if reference is None else reference, "reference coframe")
    background = checks._real(np.zeros((4, 4)) if background is None else background,
                              (4, 4), "background coframe")
    weights = beta @ gamma
    bilinear = np.array([[np.vdot(psi, d @ k.T) for d in dcov] for k in weights])
    coframe = background+scale*bilinear.real
    inverse = np.linalg.inv(reference)
    coordinate_gamma = np.einsum("ma,aij->mij", inverse, gamma)
    residual = 1j*sum(d @ g.T for d, g in zip(dcov, coordinate_gamma))-image
    scalar_residual = complex(np.vdot(psi, residual @ beta.T))
    scalar_mass = complex(np.vdot(psi, image @ beta.T))
    frame = relative_frame(coframe, reference)
    background_trace = float(np.trace(background @ inverse))
    prediction = (frame["trace"]-background_trace)/scale-scalar_mass.imag
    return {**frame, "coframe": coframe, "background_trace": background_trace,
            "residual": residual, "scalar_residual": scalar_residual,
            "scalar_mass": scalar_mass, "imaginary_residual_prediction": float(prediction)}


def multiplier_probe_weight(multiplier, derivative, weights, amplitude, coupling, scale=1.0):
    """Wirtinger probe EL of -lambda.C, after integrating its gradient term by parts."""
    multiplier = checks._real(multiplier, (4, 4), "multiplier density [frame,coordinate]")
    derivative = checks._real(derivative, (4, 4, 4), "multiplier derivative [coordinate,frame,coordinate]")
    weights = checks._finite(weights, "spin weights")
    if (weights.ndim != 3 or weights.shape[0] != 4 or weights.shape[1] != weights.shape[2]
            or not np.allclose(weights, weights.conj().swapaxes(-1, -2), atol=1e-12, rtol=0)):
        raise ValueError("Four Hermitian spin weights required")
    amplitude, coupling, scale = [checks._scalar(x, "real coefficient")
                                  for x in (amplitude, coupling, scale)]
    divergence = np.einsum("mam->a", derivative)
    coefficients = scale*(divergence/2-coupling*amplitude*(multiplier @ geometry.N_COV))
    return np.einsum("a,aij->ij", coefficients, weights)


def scalar_curvature_el(metric, metric_first, gradient, hessian, coupling, trace=1.0):
    """EL_h = kappa c_T div_g(n_nu F^{mu nu}); fixed coordinate covector n."""
    metric = _frame(metric, "metric")
    if not np.allclose(metric, metric.T, atol=1e-12, rtol=0):
        raise ValueError("A symmetric metric required")
    first = checks._real(metric_first, (4, 4, 4), "metric first derivative")
    gradient = checks._real(gradient, (4,), "scalar gradient")
    hessian = checks._real(hessian, (4, 4), "scalar Hessian")
    coupling, trace = checks._scalar(coupling, "coupling"), checks._scalar(trace, "generator trace")
    if trace <= 0 or not np.allclose(hessian, hessian.T, atol=1e-12, rtol=0):
        raise ValueError("Positive generator trace and symmetric Hessian required")
    inverse, n = np.linalg.inv(metric), geometry.N_COV
    inverse_first = -np.einsum("ap,lpq,qb->lab", inverse, first, inverse)
    f = coupling*(np.outer(gradient, n)-np.outer(n, gradient))
    df = np.array([coupling*(np.outer(row, n)-np.outer(n, row)) for row in hessian])
    raised = inverse @ f @ inverse
    raised_first = np.array([di @ f @ inverse+inverse @ df[d] @ inverse+inverse @ f @ di
                             for d, di in enumerate(inverse_first)])
    flux = coupling*trace*raised @ n
    flux_first = coupling*trace*np.einsum("dmn,n->dm", raised_first, n)
    log_volume_first = np.einsum("ab,lba->l", inverse, first)/2
    return {"EL": float(np.trace(flux_first)+log_volume_first @ flux), "flux": flux,
            "flux_first": flux_first}


def affine_neutral_branch(xy=(0.2, 0.3), coupling=0.4, einstein_coupling=1.0,
                          intercept=2.0, slope=(0.1, 0.0)):
    """Local solution of the declared MODIFIED massless neutral scalar-HC parent only."""
    coupling = checks._scalar(coupling, "coupling")
    einstein_coupling = checks._scalar(einstein_coupling, "Einstein coupling")
    if coupling == 0 or einstein_coupling <= 0:
        raise ValueError("Nonzero HC and positive Einstein couplings required")
    profile = geometry.logarithmic_profile(xy, coupling, einstein_coupling,
                                            intercept=intercept, slope=slope)
    h, gradient, hessian = profile["amplitude"], np.zeros(4), np.zeros((4, 4))
    gradient[1:3], hessian[1:3, 1:3] = profile["gradient"], profile["hessian"]
    fields = geometry.null_geometry(h, profile["gradient"], profile["hessian"], coupling)
    weights, beta = geometry.spin_weights()
    psi = np.array([[1, 0, 1, 0]], dtype=complex)/np.sqrt(2)
    derivative = np.zeros((4, 1, 4), dtype=complex)
    ordered = derivative+coupling*h*geometry.N_COV[:, None, None]*psi
    frame = mixed_probe_trace(psi, ordered, beta @ weights, beta, np.zeros_like(psi),
                               background=np.eye(4))
    coframe = frame["coframe"]
    mismatch = fields["einstein"]-einstein_coupling*fields["hc_stress"]
    inverse = np.linalg.inv(fields["metric"])
    # delta S_geom = integral sqrt|g| Ecal^{mu nu} delta g_mu_nu / 2.
    ecal = -inverse @ mismatch @ inverse/einstein_coupling
    pi = abs(np.linalg.det(coframe))*geometry.ETA @ coframe @ ecal
    scalar = scalar_curvature_el(fields["metric"], fields["metric_first"], gradient,
                                  hessian, coupling)
    frame_current = np.array([np.vdot(psi, psi @ k.T).real for k in weights])
    de = coupling*np.einsum("l,a,m->lam", gradient, geometry.L_VECTOR, geometry.N_COV)
    induced_current = geometry.coordinate_current_balance(frame_current, np.zeros((4, 4)), coframe, de)
    return {"profile": profile, "coframe": coframe, "metric": fields["metric"],
            "geometry": fields, "reference_probe_residual": frame["residual"],
            "coframe_constraint_residual": coframe-np.eye(4)-coupling*h*np.outer(geometry.L_VECTOR, geometry.N_COV),
            "Einstein_residual": mismatch, "coframe_EL_at_zero_multiplier": pi,
            "scalar_EL": scalar["EL"], "scalar_flux": scalar["flux"],
            "reference_phase_current": frame_current, "reference_phase_current_divergence": 0.0,
            "induced_current_divergence": induced_current["divergence"],
            "ordered_HC_transport_image_norm": float(np.linalg.norm(frame["residual"])),
            "relative_trace": frame["trace"], "background_trace": frame["background_trace"],
            "psi": psi, "weights": weights, "spin_metric": beta,
            "native_mass_Yukawa_restoration_residual_norm": float(abs(0.6+0.2*h)*np.linalg.norm(psi)),
            "charged_zero_gauge_Gauss_source_norm": float(np.linalg.norm(psi)**2),
            "zero_target_penalty_restoration_EL": -h}


def _on_shell_jet(seed=53):
    rng = np.random.default_rng(seed)
    weights, beta = geometry.spin_weights()
    gamma = beta @ weights
    psi = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
    derivative = rng.normal(size=(4, 3, 4))+1j*rng.normal(size=(4, 3, 4))
    image = 0.6*psi
    spatial = sum(derivative[mu] @ gamma[mu].T for mu in range(1, 4))
    derivative[0] = (-spatial-1j*image) @ np.linalg.inv(gamma[0]).T
    return mixed_probe_trace(psi, derivative, gamma, beta, image)


def evaluate():
    jet = _on_shell_jet()
    branch = affine_neutral_branch()
    fields, profile = branch["geometry"], branch["profile"]
    return {
        "status": "conditional two-frame obstruction and a local solution of an explicitly MODIFIED neutral parent; NOT native closure",
        "two_frames_without_changing_the_coframe": {
            "definition": "E=s Re(bar(Psi)Gamma^a D_mu Psi), reference inverse f=theta^(-1), Gamma_ref^mu=f_a^mu Gamma^a",
            "identity": "Im(bar(Psi) R_ref)=Tr(E theta^(-1))/s-Im w",
            "real_mass_on_shell_requirement": "Tr(E theta^(-1))=0",
            "distance_from_identity": "||E theta^(-1)-I||_F >= 2 and ||.||_op >= 1 for real mass on shell; declared common spin frame",
            "not_a_Lorentz_invariant_metric_distance": True,
            "point_jet_trace": jet["trace"],
            "point_jet_residual_norm": float(np.linalg.norm(jet["residual"])),
            "point_jet_coframe_rank": int(np.linalg.matrix_rank(jet["coframe"])),
            "does_not_exclude_every_separate_frame_geometry": True,
            "pure_Lorentz_trace_zero_negative_control": "diag(1,1,-1,-1) has trace zero and the same metric as I; spin-frame identification matters",
        },
        "common_parent_action": {
            "form": "S_parent=S_micro[Psi;theta]+S_geom[E,H]+integral lambda_a^mu(E^a_mu-Ebg^a_mu-C^a_mu[Psi,H])",
            "equations": "E-Ebg-C=0; pi_E+lambda=0; EL_micro-(DC)^*lambda=0; EL_H,geom-(D_H C)^*lambda=0",
            "elimination": "lambda=-pi_E reproduces EL_micro+(DC)^*pi_E=0 of the composite action",
            "independent_Einstein_equation_does_not_follow_from_this_constraint_alone": True,
            "phase_blind_fixed_Hermitian_dictionary": "C=s partial_mu j^a/2+s kappa h n_mu j^a",
            "real_probe_multiplier_weight": "V_lambda=s[(partial_mu lambda_a^mu)/2-kappa h lambda_a^mu n_mu]K^a",
            "Hermitian_multiplier_weight_does_not_automatically_supply_Im_w": True,
            "no_extra_central_phase_current_from_this_phase_blind_C": True,
        },
        "affine_model_change": {
            "definition": "E=theta+C, not the unchanged native E=C",
            "identity": "Im(bar(Psi) R_ref)=[Tr(E theta^(-1))-4]/s-Im w",
            "same_induced_frame_variant": "Im(bar(Psi) R_induced)=[4-Tr(E^(-1)theta)]/s-Im w",
            "new_background_is_not_a_QAM_tag_shift_or_derived_native_term": True,
        },
        "explicit_modified_neutral_parent": {
            "field_space": "independent real nonsingular E, real h, complex commuting Psi and real multiplier density; fixed theta=I,n=(-1,0,0,1)",
            "action": "S_free_real_massless[Psi;theta]+integral sqrt|g(E)|[R/(2 kappa_eff)-F_mu_nu F^mu_nu/4]+integral lambda.(E-theta-C)",
            "curvature": "F=kappa dh wedge n, scalar real curvature; not a charged probe gauge connection",
            "dictionary": "C=Re(Psi^dagger K^a partial_mu Psi)+kappa h n_mu Psi^dagger K^a Psi",
            "profile": "Psi=(1,0,1,0)/sqrt(2) constant, lambda=0, h=log(2+0.1x)/(kappa_eff kappa)",
            "coframe": "E=I+kappa h l n^T, g=eta+2 kappa h n n^T",
            "sample_h": profile["amplitude"],
            "sample_reference_trace": branch["relative_trace"],
            "reference_probe_residual_norm": float(np.linalg.norm(branch["reference_probe_residual"])),
            "coframe_constraint_residual_norm": float(np.linalg.norm(branch["coframe_constraint_residual"])),
            "full_independent_metric_residual_norm": float(np.linalg.norm(branch["Einstein_residual"])),
            "coframe_EL_at_zero_multiplier_norm": float(np.linalg.norm(branch["coframe_EL_at_zero_multiplier"])),
            "scalar_HC_EL": branch["scalar_EL"],
            "reference_phase_current_divergence": branch["reference_phase_current_divergence"],
            "induced_current_divergence": branch["induced_current_divergence"],
            "Riemann_component_norm_not_invariant": float(np.linalg.norm(fields["lower_riemann"])),
            "no_new_charged_Gauss_equation_exists_in_this_declared_neutral_field_space": True,
            "local_all_declared_EL_equations_satisfied_not_a_global_or_native_solution": True,
        },
        "restoring_native_terms_is_not_free": {
            "central_mass_0p6_and_Yukawa_0p2_residual_norm": branch["native_mass_Yukawa_restoration_residual_norm"],
            "charged_probe_at_zero_gauge_Gauss_source_norm": branch["charged_zero_gauge_Gauss_source_norm"],
            "penalty_lambda_0p5_target_zero_scalar_EL": branch["zero_target_penalty_restoration_EL"],
            "nonzero_h_is_not_exact_minimal_HC_zero_closure": True,
            "background_adjoint_gauge_mass_projector_and_collective_scales_not_derived": True,
            "no_well_posedness_global_boundary_stability_or_empirical_claim": True,
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
