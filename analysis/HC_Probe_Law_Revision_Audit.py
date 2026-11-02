"""Active-source audit, real probe variation and a curved same-coframe control.

No replacement native equation or solution of the full field system is adopted.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "revision_audit_dirac", Path(__file__).with_name("HC_Dirac_State_Gravity.py"))
dirac = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(dirac)
SPEC = importlib.util.spec_from_file_location(
    "revision_audit_hard_transport", Path(__file__).with_name("HC_Hard_Closure_Transport.py"))
hard_transport = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(hard_transport)
checks = dirac.checks
K_FRAME, BETA = dirac.WEIGHTS, dirac.BETA


def _data(psi, derivative, weights, connection, mass_weight, divergence):
    values = [checks._finite(v, name) for v, name in (
        (psi, "probe vector"), (derivative, "probe derivative"), (weights, "kinetic weights"),
        (connection, "connection"), (mass_weight, "mass weight"), (divergence, "weighted weight divergence"))]
    psi, derivative, weights, connection, mass_weight, divergence = values
    n = psi.size
    if (psi.shape != (n,) or not n or derivative.shape != (4, n)
            or weights.shape != (4, n, n) or connection.shape != (4, n, n)
            or mass_weight.shape != (n, n) or divergence.shape != (n, n)):
        raise ValueError("Compatible four-dimensional probe jets and matrix weights required")
    for value in (weights, mass_weight, divergence):
        if not np.allclose(value, value.conj().swapaxes(-1, -2), atol=1e-12, rtol=0):
            raise ValueError("Hermitian kinetic, mass and divergence weights required")
    return values


def real_operator(psi, derivative, weights, connection, mass_weight, divergence):
    """EL/volume for fixed external weights, density and connection; not a composite EL."""
    psi, derivative, weights, connection, mass_weight, divergence = _data(
        psi, derivative, weights, connection, mass_weight, divergence)
    covariant = derivative+connection @ psi
    defect = divergence-np.sum(connection.conj().swapaxes(-1, -2) @ weights+weights @ connection, axis=0)
    ordered = 1j*np.einsum("mij,mj->i", weights, covariant)-mass_weight @ psi
    symmetric = ordered+0.5j*defect @ psi
    current_divergence = (np.vdot(psi, divergence @ psi).real
                          +2*np.einsum("i,mij,mj->", psi.conj(), weights, derivative).real)
    return {"ordered": ordered, "symmetric": symmetric, "defect": defect,
            "current_divergence": float(current_divergence), "covariant": covariant}


def action_density(psi, derivative, weights, connection, mass_weight):
    data = _data(psi, derivative, weights, connection, mass_weight, np.zeros_like(mass_weight))
    psi, derivative, weights, connection, mass_weight, _ = data
    return float(-np.einsum("i,mij,mj->", psi.conj(), weights, derivative+connection @ psi).imag
                 -np.vdot(psi, mass_weight @ psi).real)


def coframe(psi, covariant):
    return np.einsum("i,aij,mj->am", psi.conj(), K_FRAME, covariant).real


def cone_data(time=1.2, mass=0.6):
    """Kinematically self-consistent curved E=Re(bar psi Gamma D psi), OFF SHELL."""
    time, mass = checks._scalar(time, "positive cone time"), checks._scalar(mass, "real mass")
    if time <= 0:
        raise ValueError("A strictly positive cone time is required")
    frame = np.diag([1., time, time, time])
    first = np.zeros((4, 4, 4))
    first[0] = np.diag([0., 1, 1, 1])
    bundle = dirac.bundle(frame, first)
    inverse = np.linalg.inv(frame)
    inverse_first = -np.einsum("ma,lav,vb->lmb", inverse, first, inverse)
    weights = np.einsum("ma,aij->mij", inverse, K_FRAME)
    weights_first = np.einsum("lma,aij->lmij", inverse_first, K_FRAME)
    log_volume_first = np.einsum("ma,lam->l", inverse, first)
    divergence = np.einsum("mmij->ij", weights_first)+np.einsum("m,mij->ij", log_volume_first, weights)
    psi = np.array([np.sqrt(2*time), 0, 0, 0], complex)
    derivative = np.zeros((4, 4), complex)
    derivative[0] = psi/(2*time)
    operator = real_operator(psi, derivative, weights, bundle["spin"], mass*BETA, divergence)
    frame_current = np.einsum("i,aij,j->a", psi.conj(), K_FRAME, psi).real
    frame_current_first = 2*np.einsum("i,aij,mj->ma", psi.conj(), K_FRAME, derivative).real
    coordinate_current = inverse @ frame_current
    coordinate_first = np.einsum("lma,a->lm", inverse_first, frame_current)+frame_current_first @ inverse.T
    covariant_current_first = coordinate_first+np.einsum("nmr,r->mn", bundle["curvature"]["connection"], coordinate_current)
    return {"time": time, "mass": mass, "frame": frame, "first": first, "bundle": bundle,
            "weights": weights, "weights_first": weights_first, "log_volume_first": log_volume_first,
            "volume": time**3, "divergence": divergence, "psi": psi, "derivative": derivative,
            "operator": operator, "reconstructed": coframe(psi, operator["covariant"]),
            "frame_current": frame_current, "coordinate_current": coordinate_current,
            "covariant_current_first": covariant_current_first}


def half_density_control(data):
    root_volume = np.sqrt(data["volume"])
    q = root_volume*data["psi"]
    derivative = root_volume*data["derivative"]+0.5*data["log_volume_first"][:, None]*q
    connection = data["bundle"]["spin"]-0.5*data["log_volume_first"][:, None, None]*np.eye(4)
    divergence = np.einsum("mmij->ij", data["weights_first"])
    result = real_operator(q, derivative, data["weights"], connection, data["mass"]*BETA, divergence)
    transported = coframe(q, result["covariant"])/data["volume"]
    naive = coframe(q, derivative+data["bundle"]["spin"] @ q)/data["volume"]
    return {"probe": q, "operator": result, "coframe": transported, "naive_coframe": naive,
            "scaled_original_residual": root_volume*data["operator"]["symmetric"],
            "normalized_imaginary_trace": float(np.vdot(q, result["symmetric"]).imag/data["volume"])}


def background_dirac_control(data):
    """An actual Dirac solution on the prescribed cone; NOT its coframe reconstruction."""
    time, mass = data["time"], data["mass"]
    psi = np.array([time**(-1.5)*np.exp(-1j*mass*time), 0, 0, 0])
    derivative = np.zeros((4, 4), complex)
    derivative[0] = (-1.5/time-1j*mass)*psi
    result = real_operator(psi, derivative, data["weights"], data["bundle"]["spin"], mass*BETA, data["divergence"])
    return {"psi": psi, "operator": result, "coframe": coframe(psi, result["covariant"])}


def projection_control(data, mix=0.0):
    """Isometric spectral-projector comparison, not the native C/M16 representation."""
    texture = hard_transport.texture(point=(data["time"], 0.2, -0.1, 0.0), mix=mix, eta=0)
    p, v, dv = texture["P"], texture["frame"], texture["frame_first"]
    mass = data["mass"]*p+(data["mass"]+0.6)*(np.eye(2)-p)
    reduced = hard_transport.reduce_frame(v, dv, texture["frame_second"], texture["connection"],
                                          texture["connection_first"], mass)
    chi = data["psi"][None, :]
    dchi = data["derivative"][:, None, :]
    psi = v @ chi
    derivative = dv @ chi+v @ dchi
    full = dirac.dirac_data(psi, derivative+texture["connection"] @ psi, mass,
                           gamma=data["bundle"]["gamma"], metric=data["bundle"]["metric"], spin=data["bundle"]["spin"])
    small = dirac.dirac_data(chi, dchi+reduced["connection"] @ chi, reduced["omega"],
                            gamma=data["bundle"]["gamma"], metric=data["bundle"]["metric"], spin=data["bundle"]["spin"])
    frame = np.array([[np.vdot(psi, d @ k.T).real for d in full["covariant"]] for k in K_FRAME])
    commutator = mass @ p-p @ mass
    residue = (np.eye(2)-p) @ mass @ p+p @ mass @ (np.eye(2)-p)
    visible_hc = commutator.conj().T @ commutator+residue.conj().T @ residue
    return {"texture": texture, "mass": mass, "reduced": reduced, "visible_hc": visible_hc,
            "full": full, "small": small, "coframe": frame,
            "lift_error": float(np.linalg.norm(full["residual"]-v @ small["residual"])),
            "imaginary_full_trace": float(np.vdot(psi, full["residual"] @ BETA.T).imag)}


def multiplier_weight(multiplier, first, bundle):
    """Psi reaction of -lambda.C at fixed E, with C=(d j+omega j)/2."""
    multiplier = checks._real(multiplier, (4, 4), "real coframe multiplier density")
    first = checks._real(first, (4, 4, 4), "multiplier density derivative")
    omega = np.einsum("ab,mbc->mac", dirac.ETA, bundle["omega"])
    coefficients = (np.einsum("mbm->b", first)-np.einsum("am,mab->b", multiplier, omega))/2
    return np.einsum("a,aij->ij", coefficients, K_FRAME)


def periodic_fixture(count=65):
    """One periodic coordinate for off-shell variation, not a causal evolution."""
    if isinstance(count, bool) or not isinstance(count, int) or count < 17 or count % 2 != 1:
        raise ValueError("An odd periodic grid with at least 17 points is required")
    x = 2*np.pi*np.arange(count)/count
    rng = np.random.default_rng(931617)
    matrices = rng.normal(size=(8, 4, 4))+1j*rng.normal(size=(8, 4, 4))
    matrices = (matrices+matrices.conj().swapaxes(-1, -2))/8
    vectors = rng.normal(size=(5, 4))+1j*rng.normal(size=(5, 4))
    psi = vectors[0]+0.2*np.sin(x[:, None])*vectors[1]+0.1j*np.cos(2*x[:, None])*vectors[2]
    variation = 0.3*np.cos(x[:, None])*vectors[3]+0.2j*np.sin(3*x[:, None])*vectors[4]
    volume = 1+0.2*np.cos(x)+0.05*np.sin(2*x)
    weights = np.tile(K_FRAME, (count, 1, 1, 1))
    weights[:, 0] += 0.12*np.sin(x[:, None, None])*matrices[0]
    connection = np.array([np.array([0.1*np.cos(q)*matrices[m]+0.13j*np.sin(2*q)*matrices[m+4]
                                    for m in range(4)]) for q in x])
    mass = 0.6*BETA+0.1*np.sin(x[:, None, None])*matrices[7]

    def derivative(value):
        k = np.fft.fftfreq(count, d=1/count).reshape((count,)+(1,)*(value.ndim-1))
        return np.fft.ifft(1j*k*np.fft.fft(value, axis=0), axis=0)

    divergence = derivative(volume[:, None, None]*weights[:, 0])/volume[:, None, None]
    # Remove roundoff from differentiating exact Hermitian trigonometric weights.
    divergence = (divergence+divergence.conj().swapaxes(-1, -2))/2
    return {"x": x, "psi": psi, "variation": variation, "volume": volume,
            "weights": weights, "connection": connection, "mass": mass,
            "divergence": divergence, "differentiate": derivative}


def periodic_variation_check(count=65):
    data = periodic_fixture(count)
    psi, variation, derivative = data["psi"], data["variation"], data["differentiate"]
    first = np.zeros((count, 4, 4), complex)
    first[:, 0] = derivative(psi)
    variation_first = np.zeros_like(first)
    variation_first[:, 0] = derivative(variation)
    kwargs = (data["weights"], data["connection"], data["mass"], data["divergence"])
    operators = [real_operator(psi[i], first[i], *(v[i] for v in kwargs)) for i in range(count)]
    measure = data["volume"]*2*np.pi/count
    predicted = 2*sum(w*np.vdot(d, op["symmetric"]).real for w, d, op in zip(measure, variation, operators))
    ordered = 2*sum(w*np.vdot(d, op["ordered"]).real for w, d, op in zip(measure, variation, operators))

    def action(p, dp):
        return sum(measure[i]*action_density(p[i], dp[i], *(v[i] for v in kwargs[:3])) for i in range(count))

    direct = 0.
    for i in range(count):
        k, b, w = (v[i] for v in kwargs[:3])
        cov, dcov = first[i]+b @ psi[i], variation_first[i]+b @ variation[i]
        kinetic = np.einsum("i,mij,mj->", variation[i].conj(), k, cov)
        kinetic += np.einsum("i,mij,mj->", psi[i].conj(), k, dcov)
        direct += measure[i]*(-kinetic.imag-2*np.vdot(variation[i], w @ psi[i]).real)
    step = 1e-5
    numeric = (action(psi+step*variation, first+step*variation_first)
               -action(psi-step*variation, first-step*variation_first))/(2*step)
    return {"grid_points": count, "direct_action_variation": float(direct),
            "derived_EL_variation": float(predicted), "analytic_variation_error": float(abs(direct-predicted)),
            "finite_difference_variation_error": float(abs(numeric-predicted)),
            "unchanged_ordered_equation_variation_error": float(abs(direct-ordered)),
            "Ward_identity_max_error": float(max(abs(op["current_divergence"]-2*np.vdot(p, op["symmetric"]).imag)
                                                 for p, op in zip(psi, operators)))}


def source_audit():
    records = (
        ("entrypoint", "sources/research/v480-companion.tex", ["parts/hc-dynamics-and-geometry", "parts/v470/10_sphaera_and_physics", "parts/v470/13_hc_hypotheses", "parts/v470/16_master_model"]),
        ("legacy_probe", "sources/research/parts/v470/10_sphaera_and_physics.tex", ["thm:dirac-probe", "thm:master-field-equation", "prop:triadic-two-probe", "thm:variational-form", "thm:closed-master-system", "prop:bilinear-einstein-reconstruction"]),
        ("structural_core", "sources/research/parts/v470/12_structural_core.tex", ["thm:hc-spectral-projector", "rem:hc-shadow-vs-core"]),
        ("later_hypotheses", "sources/research/parts/v470/13_hc_hypotheses.tex", ["hyp:hc-meta-generator", "hyp:frame-dependent-defect-readout", "thm:theorem-level-shadow-fluid-type-readout"]),
        ("later_synthesis", "sources/research/parts/v470/16_master_model.tex", ["thm:minimal-mmhc-field-equation"]),
        ("current_qualification", "sources/research/parts/hc-dynamics-and-geometry.tex", ["v480:hc-dynamics-geometry", "A genuinely real symmetric probe action", "v480:hc-same-frame-obstruction"]))
    result = {}
    for role, relative, anchors in records:
        path = ROOT / relative
        raw = path.read_bytes()
        lines = raw.decode("utf-8-sig").splitlines()
        found = {anchor: [i+1 for i, line in enumerate(lines) if anchor in line] for anchor in anchors}
        result[role] = {"path": relative, "sha256": hashlib.sha256(raw).hexdigest(),
                        "canonical_LF_sha256": hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest(), "anchors": found,
                        "all_anchors_found": all(found.values())}
    return result


def evaluate():
    data = cone_data()
    operator, curvature = data["operator"], data["bundle"]["curvature"]
    half = half_density_control(data)
    on_shell = background_dirac_control(data)
    projected = projection_control(data)
    ricci_prediction = np.diag([0., 2, 2, 2])
    phase_gradient = np.array([0.2, -0.3, 0.4, -0.1])
    phase = np.exp(0.37j)
    changed_psi = phase*data["psi"]
    changed_derivative = phase*(data["derivative"]+1j*phase_gradient[:, None]*data["psi"])
    changed_covariant = changed_derivative+data["bundle"]["spin"] @ changed_psi
    return {
        "status": "active-source/variational audit and curved same-coframe OFF-SHELL control; NOT a new native probe law or full solution",
        "audited_sources": source_audit(),
        "source_conclusions": {
            "later_active_synthesis_still_prints_ordered_master_equation": True,
            "free_Dirac_block_is_a_limit_not_the_full_transport_law": True,
            "later_fluid_shadow_explicitly_retains_original_kernel": True,
            "deeper_frame_dependent_HC_is_not_identical_to_minimal_visible_defect": True,
            "no_evaluated_superseding_native_probe_law_found_in_audited_blocks": True,
            "real_action_and_composite_geometry_require_distinct_variations": True},
        "fixed_background_real_action": {
            "EL": "R_sym=i K^mu D_mu psi-W psi+(i/2) Z psi",
            "compatibility_defect": "Z=volume^(-1) partial_mu(volume K^mu)-B_mu^dagger K^mu-K^mu B_mu",
            "Ward_identity": "volume^(-1) partial_mu(volume j^mu)=2 Im(psi^dagger R_sym), W Hermitian",
            "composite_chain_reactions_are_additional_not_included_in_this_partial_EL": True},
        "independent_periodic_action_check": periodic_variation_check(),
        "curved_same_coframe_control": {
            "time": data["time"], "metric": data["bundle"]["metric"].tolist(),
            "frame": data["frame"].tolist(), "frame_reconstruction_error": float(np.linalg.norm(data["reconstructed"]-data["frame"])),
            "ricci": curvature["ricci"].tolist(), "ricci_formula_error": float(np.linalg.norm(curvature["ricci"]-ricci_prediction)),
            "scalar_curvature": curvature["scalar"], "scalar_prediction": 6/data["time"]**2,
            "compatibility_defect_norm": float(np.linalg.norm(operator["defect"])),
            "same_induced_probe_residual_norm": float(np.linalg.norm(operator["symmetric"])),
            "imaginary_probe_trace": float(np.vdot(data["psi"], operator["symmetric"]).imag),
            "phase_current_divergence": operator["current_divergence"],
            "homothetic_current_error": float(np.linalg.norm(data["covariant_current_first"]-2*np.eye(4))),
            "curvature_annihilates_current_error": float(np.linalg.norm(np.einsum("abcd,b->acd", curvature["riemann"], data["coordinate_current"]))),
            "curved_geometry_does_not_solve_probe_gauge_or_einstein_equations": True},
        "half_density_control": {
            "coframe_transport_error": float(np.linalg.norm(half["coframe"]-data["frame"])),
            "probe_equation_transport_error": float(np.linalg.norm(half["operator"]["symmetric"]-half["scaled_original_residual"])),
            "naively_keeping_old_connection_changes_coframe_error": float(np.linalg.norm(half["naive_coframe"]-data["frame"])),
            "normalized_imaginary_probe_trace": half["normalized_imaginary_trace"]},
        "on_shell_fixed_cone_control": {
            "probe_residual_norm": float(np.linalg.norm(on_shell["operator"]["symmetric"])),
            "phase_current_divergence": on_shell["operator"]["current_divergence"],
            "coframe_definition_error": float(np.linalg.norm(on_shell["coframe"]-data["frame"])),
            "does_not_solve_the_joint_reconstruction": True},
        "surviving_projector_comparison": {
            "projector_norm": float(np.linalg.norm(projected["texture"]["P"])),
            "visible_minimal_HC_norm": float(np.linalg.norm(projected["visible_hc"])),
            "reduced_connection_Hermitian_part_norm": float(np.linalg.norm(projected["reduced"]["connection"]+projected["reduced"]["connection"].conj().swapaxes(-1, -2))),
            "internal_bundle_curvature_norm": float(np.linalg.norm(projected["reduced"]["curvature"])),
            "coframe_change_norm": float(np.linalg.norm(projected["coframe"]-data["frame"])),
            "probe_operator_lift_error": projected["lift_error"],
            "imaginary_full_probe_trace": projected["imaginary_full_trace"],
            "orthogonal_factorized_model_not_native_C_M16_or_a_sourced_gauge_solution": True},
        "phase_blind_composite_constraint": {
            "local_phase_coframe_error": float(np.linalg.norm(coframe(changed_psi, changed_covariant)-data["reconstructed"])),
            "real_phase_invariant_geometry_and_constraint_do_not_supply_extra_phase_current": True,
            "under_compatible_same_frame_HC_zero_hypotheses_current_divergence_is_eight_so_closed_phase_symmetric_action_cannot_be_stationary": True,
            "not_a_no_go_for_all_native_readouts_adjoint_choices_or_quantum_completions": True},
        "main_TeX_changed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = json.dumps(evaluate(), indent=2, allow_nan=False)+"\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
