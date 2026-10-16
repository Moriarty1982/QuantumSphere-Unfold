"""Source-backed background candidates and an exact reference-Dirac triadic example."""
import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "background_two_frame", Path(__file__).with_name("HC_Two_Frame_Action_Bridge.py"))
two_frame = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(two_frame)
geometry, checks = two_frame.geometry, two_frame.checks


def coframe(psi, covariant_derivative, weights, scale=1.0):
    psi = checks._finite(psi, "probe")
    derivative = geometry.probe._derivatives(covariant_derivative, psi)
    weights = checks._finite(weights, "frame weights")
    scale = checks._scalar(scale, "coframe scale")
    if (psi.ndim != 2 or psi.shape[0] == 0 or weights.shape != (4, psi.shape[1], psi.shape[1])
            or not np.allclose(weights, weights.conj().swapaxes(-1, -2), atol=1e-12, rtol=0)
            or scale == 0):
        raise ValueError("Compatible probe data, four Hermitian weights and nonzero scale required")
    return scale*np.array([[np.vdot(psi, d @ k.T).real for d in derivative] for k in weights])


def background_expansion(psi0, fluctuation, d0_psi0, d0_fluctuation, weights,
                          delta_connection=None, scale=1.0):
    psi0, fluctuation = checks._finite(psi0, "background probe"), checks._finite(fluctuation, "fluctuation")
    if psi0.shape != fluctuation.shape or psi0.ndim != 2:
        raise ValueError("Background and fluctuation on the same carrier required")
    d0_psi0 = geometry.probe._derivatives(d0_psi0, psi0)
    d0_fluctuation = geometry.probe._derivatives(d0_fluctuation, psi0)
    delta = checks._finite(np.zeros((4, len(psi0), len(psi0))) if delta_connection is None
                            else delta_connection, "connection fluctuation")
    if delta.shape != (4, len(psi0), len(psi0)):
        raise ValueError("Four internal connection variations required")
    total = psi0+fluctuation
    theta = coframe(psi0, d0_psi0, weights, scale)
    quadratic = coframe(fluctuation, d0_fluctuation, weights, scale)
    cross = scale*np.array([[np.vdot(psi0, d @ k.T).real+np.vdot(fluctuation, d0 @ k.T).real
                             for d0, d in zip(d0_psi0, d0_fluctuation)] for k in weights])
    connection = coframe(total, delta @ total, weights, scale)
    full = coframe(total, d0_psi0+d0_fluctuation+delta @ total, weights, scale)
    return {"background": theta, "quadratic_fluctuation": quadratic, "cross": cross,
            "connection_change": connection, "total": full,
            "expansion_residual": full-theta-cross-quadratic-connection}


def triadic_mass(mass=0.6, art_coupling=4.0, qft_coupling=0.7):
    mass, a, b = [checks._scalar(v, "real mass/coupling") for v in (mass, art_coupling, qft_coupling)]
    return np.array([[mass, 0.0, a], [0.0, mass, b], [a, b, mass]])


def polynomial_background(point=(0, 0, 0, 0), mass=0.6, art_coupling=4.0,
                          qft_coupling=0.7, phase=np.pi/2):
    """Exact affine-spatial reference-Dirac solution, not a native field vacuum."""
    point = checks._real(point, (4,), "spacetime point")
    phase = checks._scalar(phase, "initial mediator phase")
    omega = triadic_mass(mass, art_coupling, qft_coupling)
    weights, beta = geometry.spin_weights()
    gamma = beta @ weights
    hamiltonian = np.kron(omega, beta)
    alpha = np.array([np.kron(np.eye(3), k) for k in weights[1:]])
    initial = np.zeros((3, 4), dtype=complex)
    initial[0, 0], initial[2, 0] = 1, np.exp(1j*phase)
    spatial = np.zeros((3, 3, 4), dtype=complex)
    spatial[:, 0, :] = np.array([[0, 0, 0, 1], [0, 0, 0, 1j], [0, 0, 1, 0]])
    spatial[:, 2, :] = -np.exp(1j*phase)*spatial[:, 0, :]
    a0, b0 = initial.reshape(-1), spatial.reshape(3, -1)
    eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
    t = point[0]

    def spectral(values):
        return (eigenvectors*values) @ eigenvectors.conj().T

    u = spectral(np.exp(-1j*eigenvalues*t))
    # Integral of exp(-2 i H s), using sinc also on the exact zero modes.
    integral = spectral(t*np.exp(-1j*eigenvalues*t)*np.sinc(eigenvalues*t/np.pi))
    integral_dot = spectral(np.exp(-2j*eigenvalues*t))
    a = u @ (a0-sum(k @ integral @ b for k, b in zip(alpha, b0)))
    b = np.array([u @ v for v in b0])
    adot = -1j*hamiltonian @ a-u @ sum(k @ integral_dot @ v for k, v in zip(alpha, b0))
    bdot = np.array([-1j*hamiltonian @ v for v in b])
    psi = (a+point[1:] @ b).reshape(3, 4)
    derivative = np.array([adot+point[1:] @ bdot, *b]).reshape(4, 3, 4)
    image = omega @ psi
    residual = 1j*sum(d @ g.T for d, g in zip(derivative, gamma))-image
    coframes = np.array([coframe(psi[r:r+1], derivative[:, r:r+1], weights) for r in range(3)])
    currents = np.array([[np.vdot(row, k @ row).real for k in weights] for row in psi])
    current_first = 2*np.array([[[np.vdot(row, k @ d[r]).real for k in weights]
                                for d in derivative] for r, row in enumerate(psi)])
    w = np.array([np.vdot(row, beta @ im) for row, im in zip(psi, image)])
    divergence = np.trace(current_first, axis1=1, axis2=2)
    p = np.diag([1.0, 0.0, 0.0])
    commutator_image = (p @ omega-omega @ p) @ psi
    commutator_expectation = complex(np.vdot(psi, commutator_image @ beta.T)/(2j))
    cross_aq = coframe(psi[0:1], derivative[:, 1:2], weights)
    cross_qa = coframe(psi[1:2], derivative[:, 0:1], weights)
    return {"psi": psi, "derivatives": derivative, "mass_operator": omega,
            "weights": weights, "spin_metric": beta, "hamiltonian": hamiltonian,
            "reference_residual": residual, "coframes": coframes, "currents": currents,
            "current_derivative": current_first, "channel_divergence": divergence,
            "channel_exchange": 2*w.imag, "mass_bilinears": w,
            "ART_commutator_imaginary_mass": commutator_expectation,
            "cross_ART_QFT": cross_aq, "cross_QFT_ART": cross_qa,
            "symmetric_cross_coframe": (cross_aq+cross_qa)/2,
            "total_coframe": np.sum(coframes, axis=0),
            "background_metric": coframes[0].T @ geometry.ETA @ coframes[0]}


def kernel_real_slice(phases=(0.0, 0.0, 0.0)):
    """Polarize the DISPLAYED modulus expression; not a repaired quaternion norm."""
    phases = checks._real(phases, (3,), "spatial complex phases")
    target = np.diag([-1.0, *np.ones(6)])
    embedding = np.zeros((7, 4))
    embedding[0, 0] = 1
    for i, angle in enumerate(phases):
        embedding[1+2*i, i+1] = np.cos(angle)
        embedding[2+2*i, i+1] = np.sin(angle)
    return {"displayed_real_form": target, "chosen_embedding": embedding,
            "pullback": embedding.T @ target @ embedding}


def evaluate():
    bg = polynomial_background()
    rng = np.random.default_rng(318)
    fluctuation = 0.02*(rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4)))
    derivative = 0.02*(rng.normal(size=(4, 3, 4))+1j*rng.normal(size=(4, 3, 4)))
    expansion = background_expansion(bg["psi"], fluctuation, bg["derivatives"], derivative, bg["weights"])
    samples = [polynomial_background((t, 0.02, -0.03, 0.01)) for t in (-0.01, 0.0, 0.01)]
    cross_sample = samples[-1]
    return {
        "status": "conditional background provenance and exact coupled reference-Dirac example; NOT native full-coframe closure or adopted geometry",
        "source_anchors": [
            {"path": "sources/research/parts/v470/10_sphaera_and_physics.tex", "label": "def:biquaternion",
             "role": "kinematic quadratic form, not an evaluated four-dimensional coframe map"},
            {"path": "sources/research/parts/v470/10_sphaera_and_physics.tex", "label": "prop:bilinear-einstein-reconstruction",
             "role": "full closed triadic bilinear with maximal rank assumed, not a background-plus-fluctuation prescription"},
            {"path": "sources/research/parts/v470/12_structural_core.tex", "label": "hyp:bidirectional-probe-lensing",
             "role": "ART/QFT probes, intrinsic orthogonal mediator, phase and cross-bilinear readouts; hypothesis-grade geometry"},
            {"path": "sources/research/parts/v470/16_master_model.tex", "label": "eq:toe_master_semiconcrete",
             "role": "declared inter-sector coupling slots, not their numerical values"},
            {"path": "sources/research/parts/v470/36_frame_typed_endpoint.tex", "label": "subsec:r81-photon-frame-null-note",
             "role": "photon/clock candidate does not establish exact global zero or a rank-four background"},
        ],
        "exact_background_expansion": {
            "definition": "theta=C[Psi0,D0], E=C[Psi0+phi,D0+delta B]",
            "identity": "E=theta+cross(Psi0,phi;D0)+C[phi,D0]+C[Psi0+phi,delta B]",
            "linear_and_connection_cross_terms_are_mandatory": True,
            "sample_exact_expansion_residual_norm": float(np.linalg.norm(expansion["expansion_residual"])),
            "sample_error_if_only_theta_plus_quadratic_fluctuation_is_used": float(np.linalg.norm(expansion["cross"])),
            "fixed_connection_zero_mean_sign_pair_can_cancel_linear_cross_terms": True,
            "correlated_connection_fluctuations_need_not_cancel": True,
            "a_change_of_origin_does_not_evade_the_full_same_field_same_frame_trace_obstruction": True,
        },
        "channel_background_exchange_identity": {
            "definition": "theta_P=s Re(bar(Psi)P Gamma^a D_mu Psi), P an internal Hermitian subprojector",
            "on_shell_reference_trace": "Tr(theta_P theta_ref^(-1))/s=Im(bar(Psi)P Omega Psi)",
            "Hermitian_total_mass_can_have_complex_channel_bilinear": "Im w_P=bar(Psi)[P,Omega]Psi/(2i), with the declared weighted adjoint and spin commutation",
            "channel_continuity": "partial_mu j_P^mu=2 Im w_P; summed exchange vanishes",
            "commuting_channel_projector_has_zero_exchange": True,
            "selected_ART_subprojector_not_identified_with_native_C7_projector": True,
        },
        "exact_reference_Dirac_example": {
            "representation": "declared three internal four-spinor amplitudes, fixed reference gamma; not a native C7 embedding",
            "mass_operator": bg["mass_operator"].tolist(),
            "direct_ART_QFT_entry": float(bg["mass_operator"][0, 1]),
            "initial_mediator_relative_phase": "pi/2",
            "solution_type": "affine in spatial coordinates with exact matrix-function time evolution; local use, not a normalizable ground state",
            "origin_reference_residual_norm": float(np.linalg.norm(bg["reference_residual"])),
            "origin_ART_coframe": bg["coframes"][0].tolist(),
            "origin_ART_rank": int(np.linalg.matrix_rank(bg["coframes"][0])),
            "origin_QFT_coframe_norm": float(np.linalg.norm(bg["coframes"][1])),
            "origin_mediator_coframe": bg["coframes"][2].tolist(),
            "origin_total_coframe_norm": float(np.linalg.norm(bg["total_coframe"])),
            "origin_channel_mass_imaginary_parts": bg["mass_bilinears"].imag.tolist(),
            "origin_channel_current_divergences": bg["channel_divergence"].tolist(),
            "origin_total_current_divergence": float(np.sum(bg["channel_divergence"])),
            "reference_residual_norms_nearby": [float(np.linalg.norm(x["reference_residual"])) for x in samples],
            "ART_determinants_nearby": [float(np.linalg.det(x["coframes"][0])) for x in samples],
            "derived_selected_background_is_locally_flat": "K^a fixed, H_C=0: theta_ART=d(j_ART/2), rank four gives local Minkowski coordinates",
            "does_not_solve_the_original_full_bilinear_coframe": "the sum is degenerate at the origin, and gamma is the reference gamma, not the reconstructed one away from the origin",
        },
        "prepared_ART_QFT_cross_readout": {
            "source_definition": "E_AQ=Re(bar(Psi_ART)Gamma^a partial_mu Psi_QFT), and E_QA with probes exchanged",
            "sample_point": [0.01, 0.02, -0.03, 0.01],
            "ordered_cross_rank": int(np.linalg.matrix_rank(cross_sample["cross_ART_QFT"])),
            "ordered_cross_determinant": float(np.linalg.det(cross_sample["cross_ART_QFT"])),
            "symmetric_cross_rank": int(np.linalg.matrix_rank(cross_sample["symmetric_cross_coframe"])),
            "symmetric_cross_determinant": float(np.linalg.det(cross_sample["symmetric_cross_coframe"])),
            "symmetric_cross_gradient_identity": "(E_AQ+E_QA)/2 = partial_mu Re(Psi_ART^dagger K^a Psi_QFT)/2, so invertible symmetric cross coframe is locally flat here",
            "cross_coframe_at_origin_is_degenerate": True,
            "interpretation": "nondegenerate local candidate from the prepared two-probe dictionary, not a unique native reference state or a new curved Einstein solution",
        },
        "other_source_candidates": {
            "kernel_displayed_modulus_signature_without_a_real_slice": [1, 6],
            "a_chosen_real_spatial_slice_has_signature": [1, 3],
            "does_not_validate_the_sources_quaternion_conjugation_or_Lorentz_derivation": True,
            "Hopf_internal_S3_plus_clock": "needs an explicit internal-to-spacetime map, three independent spatial forms, a time form and physical scale; not supplied by the Hopf label",
            "a_single_clock_form_is_rank_at_most_one": True,
        },
        "remaining_native_burdens": {
            "background_state_and_numerical_couplings_not_selected_by_the_native_theory": True,
            "background_plus_fluctuation_parent_needs_background_field_variations": True,
            "no_native_gauge_Gauss_projector_or_Einstein_solution_claim": True,
            "no_derived_Newton_scale_vacuum_stability_or_photon_rest_frame": True,
            "native_C7_closure_not_implied_by_channel_selection": True,
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
