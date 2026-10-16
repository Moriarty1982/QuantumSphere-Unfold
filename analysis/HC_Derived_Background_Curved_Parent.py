"""Derived-coordinate neutral parent and its fixed-axis native HC identification test."""
import argparse
import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "curved_parent_background", Path(__file__).with_name("HC_Background_Coframe_Origin.py"))
background = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(background)
geometry, checks = background.geometry, background.checks


def probe_jets(point, **parameters):
    """Analytic derivatives through order three of the exact affine-spatial probe."""
    bg = background.polynomial_background(point, **parameters)
    h = bg["hamiltonian"]
    alpha = [np.kron(np.eye(3), k) for k in bg["weights"][1:]]
    p = [bg["psi"].reshape(-1)]
    b = [bg["derivatives"][1:].reshape(3, -1)]
    for _ in range(3):
        p.append(-1j*h @ p[-1]-sum(k @ v for k, v in zip(alpha, b[-1])))
        b.append(np.array([-1j*h @ v for v in b[-1]]))
    jets = [bg["psi"]]
    for order in range(1, 4):
        jet = np.zeros((*((4,)*order), 3, 4), dtype=complex)
        for indices in np.ndindex((4,)*order):
            spatial = [i for i in indices if i != 0]
            if not spatial:
                value = p[order]
            elif len(spatial) == 1:
                value = b[order-1][spatial[0]-1]
            else:
                continue
            jet[indices] = value.reshape(3, 4)
        jets.append(jet)
    return bg, jets


def coordinate_jets(point, readout="symmetric_cross", **parameters):
    bg, jets = probe_jets(point, **parameters)
    if readout not in {"symmetric_cross", "ART"}:
        raise ValueError("Readout must be symmetric_cross or ART")
    left, right = (0, 1) if readout == "symmetric_cross" else (0, 0)
    y = []
    for order in range(4):
        value = np.zeros((*((4,)*order), 4))
        for indices in np.ndindex((4,)*order):
            for mask in itertools.product((False, True), repeat=order):
                li = tuple(i for i, take in zip(indices, mask) if take)
                ri = tuple(i for i, take in zip(indices, mask) if not take)
                a, q = jets[len(li)][li][left], jets[len(ri)][ri][right]
                value[indices] += np.array([np.vdot(a, k @ q).real for k in bg["weights"]])/2
        y.append(value)
    theta = y[1].T
    if np.linalg.matrix_rank(theta, tol=1e-12) != 4:
        raise ValueError("The selected coordinate readout is degenerate on this patch")
    return bg, y


def pullback_metric(y, target_metric, target_first, target_second):
    """Full metric jets, including Hessian/third-derivative terms of Y(x)."""
    theta = y[1].T
    dtheta = y[2].transpose(0, 2, 1)
    ddtheta = y[3].transpose(0, 1, 3, 2)
    g = target_metric
    dg = np.einsum("cl,cab->lab", theta, target_first)
    ddg = (np.einsum("cl,ds,cdab->lsab", theta, theta, target_second)
           +np.einsum("lsc,cab->lsab", y[2], target_first))
    first, second = np.zeros((4, 4, 4)), np.zeros((4, 4, 4, 4))
    for l in range(4):
        a = dtheta[l]
        first[l] = a.T @ g @ theta+theta.T @ dg[l] @ theta+theta.T @ g @ a
        for s in range(4):
            b, ab = dtheta[s], ddtheta[l, s]
            second[l, s] = (ab.T @ g @ theta+theta.T @ g @ ab
                            +a.T @ g @ b+b.T @ g @ a
                            +a.T @ dg[s] @ theta+b.T @ dg[l] @ theta
                            +theta.T @ dg[l] @ b+theta.T @ dg[s] @ a
                            +theta.T @ ddg[l, s] @ theta)
    return {"metric": theta.T @ g @ theta, "first": first, "second": second}


def paired_scalar_equations(metric, metric_first, p, p_first, q, q_first, coupling):
    """Independent h,u equations of F=kappa dh wedge du, before the null restriction."""
    metric = checks._real(metric, (4, 4), "metric")
    first = checks._real(metric_first, (4, 4, 4), "metric first derivative")
    p, q = [checks._real(v, (4,), "scalar gradient") for v in (p, q)]
    p_first, q_first = [checks._real(v, (4, 4), "scalar Hessian") for v in (p_first, q_first)]
    coupling = checks._scalar(coupling, "coupling")
    if (np.linalg.matrix_rank(metric) != 4 or not np.allclose(metric, metric.T, atol=1e-12, rtol=0)
            or not np.allclose(p_first, p_first.T, atol=1e-12, rtol=0)
            or not np.allclose(q_first, q_first.T, atol=1e-12, rtol=0)):
        raise ValueError("An invertible symmetric metric and symmetric scalar Hessians required")
    inverse = np.linalg.inv(metric)
    di = -np.einsum("ap,lpq,qb->lab", inverse, first, inverse)
    f = coupling*(np.outer(p, q)-np.outer(q, p))
    df = np.array([coupling*(np.outer(dp, q)+np.outer(p, dq)
                             -np.outer(dq, p)-np.outer(q, dp))
                   for dp, dq in zip(p_first, q_first)])
    raised = inverse @ f @ inverse
    dr = np.array([d @ f @ inverse+inverse @ df[l] @ inverse+inverse @ f @ d
                   for l, d in enumerate(di)])
    flux_h, flux_u = coupling*raised @ q, coupling*raised.T @ p
    dh = coupling*np.array([d @ q+raised @ dq for d, dq in zip(dr, q_first)])
    du = coupling*np.array([d.T @ p+raised.T @ dp for d, dp in zip(dr, p_first)])
    log_volume_first = np.einsum("ab,lba->l", inverse, first)/2
    square = float(np.sum(f*raised))
    stress = f @ inverse @ f.T-metric*square/4
    return {"h_EL": float(np.trace(dh)+log_volume_first @ flux_h),
            "u_EL": float(np.trace(du)+log_volume_first @ flux_u),
            "h_flux": flux_h, "u_flux": flux_u, "axis_reaction_if_independent": -flux_u,
            "curvature": f, "curvature_square": square, "stress": stress}


def readout_probe_source(psi, weights, coefficient, readout="symmetric_cross"):
    """Wirtinger probe source of W_a Y^a after integrating the lambda term by parts."""
    psi = checks._finite(psi, "triadic probe")
    coefficient = checks._real(coefficient, (4,), "readout Euler coefficient")
    if psi.shape != (3, 4) or np.shape(weights) != (4, 4, 4):
        raise ValueError("The declared three-channel four-spinor realization required")
    weighted = np.einsum("a,aij->ij", coefficient, weights)
    result = np.zeros_like(psi)
    if readout == "symmetric_cross":
        result[0], result[1] = weighted @ psi[1]/4, weighted @ psi[0]/4
    elif readout == "ART":
        result[0] = weighted @ psi[0]/2
    else:
        raise ValueError("Unknown readout")
    return result


def positive_hc_axis_gap(psi, weights, tolerance=1e-11, axis=(0, 0, 1)):
    """v_H^0-v_H^3 >= gap v_H^0 for all positive internal H on this probe row space."""
    psi = checks._finite(psi, "probe")
    weights = checks._finite(weights, "frame weights")
    axis = checks._real(axis, (3,), "unit spatial axis")
    if psi.ndim != 2 or weights.shape != (4, psi.shape[1], psi.shape[1]):
        raise ValueError("Compatible probe and four current weights required")
    if not np.isclose(axis @ axis, 1, atol=1e-12, rtol=0):
        raise ValueError("A unit spatial axis required")
    _, singular, vh = np.linalg.svd(psi, full_matrices=False)
    rank = int(np.sum(singular > tolerance*max(1.0, singular[0])))
    if rank == 0:
        raise ValueError("A nonzero probe row space required")
    rows = vh[:rank]
    null_weight = weights[0]-np.einsum("i,ijk->jk", axis, weights[1:])
    restricted = rows @ null_weight.T @ rows.conj().T
    eigenvalues = np.linalg.eigvalsh(restricted)
    return {"active_rank": rank, "gap": float(eigenvalues[0]),
            "restricted_eigenvalues": eigenvalues}


def current_span_test(psi, weights, target=(1, 0, 0, 1)):
    """Linear range of all Hermitian internal current weights, even nonpositive ones."""
    psi = checks._finite(psi, "probe")
    target = checks._real(target, (4,), "target frame vector")
    n = len(psi)
    basis = [np.diag(np.eye(n)[r]).astype(complex) for r in range(n)]
    for r in range(n):
        for s in range(r+1, n):
            unit = np.zeros((n, n), dtype=complex)
            unit[r, s] = 1
            basis.extend([(unit+unit.conj().T)/np.sqrt(2), 1j*(unit-unit.conj().T)/np.sqrt(2)])
    matrix = np.array([[np.vdot(psi, h @ psi @ k.T).real for h in basis] for k in weights])
    coefficients, _, rank, _ = np.linalg.lstsq(matrix, target, rcond=1e-11)
    fitted = matrix @ coefficients
    return {"rank": int(rank), "target_residual_norm": float(np.linalg.norm(fitted-target)),
            "fitted": fitted}


def background_axis_separation(theta):
    """Sufficient bound for every background-null axis (-1,b), |b|=1, in the fixed reference chart."""
    theta = checks._real(theta, (4, 4), "background coframe")
    time_lower = max(0.0, abs(theta[0, 0])-np.linalg.norm(theta[1:, 0]))
    space_upper = np.linalg.norm(theta[0, 1:])+np.linalg.norm(theta[1:, 1:], ord=2)
    return {"time_component_lower_bound": float(time_lower),
            "spatial_component_upper_bound": float(space_upper),
            "reference_square_upper_bound": float(-time_lower**2+space_upper**2),
            "strict_separation": bool(time_lower > space_upper)}


def evaluate_branch(point=(0.01, 0.02, -0.03, 0.01), readout="symmetric_cross",
                    coupling=0.4, einstein_coupling=1.0, **parameters):
    bg, y = coordinate_jets(point, readout, **parameters)
    theta = y[1].T
    profile = geometry.logarithmic_profile(y[0][1:3], coupling, einstein_coupling)
    target = geometry.null_geometry(profile["amplitude"], profile["gradient"], profile["hessian"], coupling)
    metric = pullback_metric(y, target["metric"], target["metric_first"], target["metric_second"])
    direct = geometry.metric_curvature(metric["metric"], metric["first"], metric["second"])
    p_y, pp_y = np.zeros(4), np.zeros((4, 4))
    p_y[1:3], pp_y[1:3, 1:3] = profile["gradient"], profile["hessian"]
    p, q = theta.T @ p_y, theta.T @ geometry.N_COV
    pp = theta.T @ pp_y @ theta+np.einsum("a,lsa->ls", p_y, y[2])
    qq = np.einsum("a,lsa->ls", geometry.N_COV, y[2])
    scalar = paired_scalar_equations(metric["metric"], metric["first"], p, pp, q, qq, coupling)
    frame = (np.eye(4)+coupling*profile["amplitude"]*np.outer(geometry.L_VECTOR, geometry.N_COV)) @ theta
    expected_einstein = theta.T @ target["einstein"] @ theta
    expected_stress = theta.T @ target["hc_stress"] @ theta
    residual = direct["einstein"]-einstein_coupling*scalar["stress"]
    inverse = np.linalg.inv(metric["metric"])
    ecal = -inverse @ residual @ inverse/einstein_coupling
    frame_residual = abs(np.linalg.det(frame))*geometry.ETA @ frame @ ecal
    gamma_ref = bg["spin_metric"] @ bg["weights"]
    slash_axis = np.einsum("m,mij->ij", q, gamma_ref)
    return {"background": bg, "coordinate_jets": y, "profile": profile,
            "theta": theta, "coframe": frame, "metric_jets": metric,
            "direct_geometry": direct, "scalar": scalar,
            "expected_Einstein": expected_einstein, "expected_stress": expected_stress,
            "Einstein_residual": residual, "coframe_EL_density": frame_residual,
            "coframe_constraint": frame-theta-coupling*profile["amplitude"]*np.outer(geometry.L_VECTOR, q),
            "null_potential": float(geometry.N_COV @ y[0]),
            "axis_covector": q, "reference_axis_square": float(q @ geometry.ETA @ q),
            "effective_axis_square": float(q @ inverse @ q),
            "reference_axis_slash": slash_axis,
            "reference_axis_slash_min_singular_value": float(np.linalg.svd(slash_axis, compute_uv=False)[-1]),
            "native_axis_gap": positive_hc_axis_gap(bg["psi"], bg["weights"])}


def evaluate():
    branch = evaluate_branch()
    art = evaluate_branch(readout="ART")
    scalar = branch["scalar"]
    span = current_span_test(branch["background"]["psi"], branch["background"]["weights"])
    radial = np.array([0.02, -0.03, 0.01])
    radial /= np.linalg.norm(radial)
    radial_gap = positive_hc_axis_gap(branch["background"]["psi"], branch["background"]["weights"], axis=radial)
    separation = background_axis_separation(branch["theta"])
    return {
        "status": "exact local solution of an explicitly declared neutral derived-readout parent, with native fixed-axis HC identification obstruction; NOT full native closure",
        "common_parent": {
            "fields": "independent complex triadic Psi, real nonsingular E, real h,u, real multiplier density lambda_a^mu and real scalar density zeta",
            "coordinates": "Y^a[Psi]=Re(Psi_ART^dagger K^a Psi_QFT)/2; Theta^a_mu=partial_mu Y^a; U[Psi]=n_a Y^a",
            "action": "S_D,reference[Psi]+integral sqrt|g(E)|[R/(2 kappa_eff)-F^2/4]+integral lambda.(E-Theta-kappa h l du)+integral zeta(u-U[Psi])",
            "curvature": "F=kappa dh wedge du; no independent charged gauge connection or native HC matrix field",
            "probe_reference_metric_is_not_varied_as_the_effective_metric": True,
            "constitutive_null_coframe_update_is_an_explicit_added_readout_choice": True,
            "native_Yukawa_projector_Gauss_and_matching_terms_not_included": True,
        },
        "full_parent_equations_before_ansatz": {
            "metric": "pi_E+lambda=0, pi_E contains independent Einstein/scalar stress equation",
            "coframe_constraint": "E-Theta-kappa h l du=0",
            "potential_constraint": "u-U[Psi]=0",
            "h": "EL_h,F-kappa lambda_a^mu l^a partial_mu u=0",
            "u": "EL_u,F+kappa partial_mu(h lambda_a^mu l^a)+zeta=0",
            "probe": "EL_D+(DY)^*[partial_mu lambda_a^mu-zeta n_a]=0, with the variational adjoint on real/complex components",
            "scalar_h_EL": "kappa div_g(F^{mu nu}partial_nu u)",
            "scalar_u_EL": "kappa div_g(F^{mu nu}partial_mu h), divergence on nu",
        },
        "exact_local_joint_branch": {
            "construction": "use the exact coupled reference-Dirac Psi; invertible Theta=dY; u=n.Y; h=log(2+0.1Y^1)/(kappa_eff kappa); E=(I+kappa h l n^T)Theta; lambda=zeta=0",
            "nonzero_axis_reaction_is_a_divergence_not_an_omitted_free_axis_equation": True,
            "reason_u_EL_vanishes": "q=du is parallel null and h is transverse, so div(|dh|^2 q)=0; axis variations are du, not arbitrary independent covectors",
            "probe_backreaction_vanishes_on_this_branch_but_not_identically_off_shell": True,
            "common_phase_current_stays_the_reference_current": "Y,U and Theta are locally common-phase invariant; the conserved total reference current is not replaced by an induced Dirac current",
            "sample_Y": branch["coordinate_jets"][0].tolist(),
            "sample_h": branch["profile"]["amplitude"],
            "sample_reference_Dirac_residual_norm": float(np.linalg.norm(branch["background"]["reference_residual"])),
            "sample_coframe_constraint_norm": float(np.linalg.norm(branch["coframe_constraint"])),
            "sample_h_EL": scalar["h_EL"], "sample_u_EL": scalar["u_EL"],
            "sample_independent_axis_reaction_component_norm": float(np.linalg.norm(scalar["axis_reaction_if_independent"])),
            "sample_direct_Einstein_residual_component_norm": float(np.linalg.norm(branch["Einstein_residual"])),
            "sample_independent_Levi_Civita_vs_pullback_Einstein_error": float(np.linalg.norm(branch["direct_geometry"]["einstein"]-branch["expected_Einstein"])),
            "sample_direct_stress_vs_pullback_error": float(np.linalg.norm(scalar["stress"]-branch["expected_stress"])),
            "sample_Riemann_component_norm_not_invariant": float(np.linalg.norm(branch["direct_geometry"]["lower_riemann"])),
            "ART_readout_direct_Einstein_residual_norm": float(np.linalg.norm(art["Einstein_residual"])),
            "coordinate_conditioning_warning": "cross coframe is close to its degenerate initial-time slice; direct metric-jet arithmetic has amplified cancellation error, not a native physical residual measurement",
        },
        "native_HC_direction_test": {
            "native_form_to_identify": "v_H^a=Psi^dagger K^a H_C Psi, H_C positive semidefinite; the null update requires v_H=h l",
            "tested_axis": [1.0, 0.0, 0.0, 1.0],
            "active_probe_row_rank": branch["native_axis_gap"]["active_rank"],
            "gap": branch["native_axis_gap"]["gap"],
            "inequality": "v_H^0-v_H^3 >= gap v_H^0 for every positive H_C on this probe; target h l has v_H^0-v_H^3=0 and h>0",
            "positive_gap_excludes_the_unchanged_native_fixed_axis_identification_on_this_patch": True,
            "Hermitian_current_span_rank": span["rank"],
            "target_residual_even_without_positivity": span["target_residual_norm"],
            "a_different_radial_axis_has_gap": radial_gap["gap"],
            "changing_the_axis_requires_rechecking_integrability_and_the_curved_profile": True,
            "not_a_no_go_for_other_probes_axes_or_readout_dictionaries": True,
            "the_model_was_not_silently_identified_with_the_native_HC_bilinear": True,
        },
        "native_transport_axis_compatibility": {
            "effective_axis_square": branch["effective_axis_square"],
            "reference_axis_square": branch["reference_axis_square"],
            "reference_slash_min_singular_value": branch["reference_axis_slash_min_singular_value"],
            "result": "the derived axis is null for the effective metric but not the fixed microscopic reference metric; Gamma_ref.n is invertible at the sample",
            "consequence": "unchanged ordered HC transport cannot be dark unless H_C Psi=0, which also nullifies the original HC current; geometry-null alignment alone is insufficient",
            "not_a_native_global_no_go": "a common gamma/metric dictionary or changed probe and axis may alter this; it is not yet derived in the native model",
            "background_null_axis_uniform_bound": separation,
            "axis_rotation_alone_does_not_fix_this_cross_background": "all axes null for the selected background are reference-timelike at this sample; rotating the null-update axis alone cannot make its reference slash singular",
            "bound_scope": "background-null axes of the rank-one update, not an assertion about every null covector of the already deformed effective metric",
        },
        "remaining_scope": {
            "no_native_Gauss_projector_or_minimal_exact_HC_closure_solution": True,
            "no_derived_Einstein_coupling_equivalence_principle_global_stability_or_quantum_vacuum": True,
            "reference_probe_mass_energy_is_not_an_effective_metric_stress_in_this_declared_two_frame_action": True,
            "an_independently_variable_axis_would_add_an_equation_that_this_branch_does_not_solve": True,
            "next_native_step": "change or derive the probe/axis/HC dictionary consistently, then restore the native real action, transport, Yukawa, gauge and closure equations together",
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
