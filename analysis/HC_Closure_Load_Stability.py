"""Existing closure load on an assumed R1,1 x S2: reality and static stability audit."""
import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


SPEC = importlib.util.spec_from_file_location(
    "closure_global_flux", Path(__file__).with_name("HC_Global_Flux_Selection.py"))
flux = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(flux)
checks, commutator = flux.checks, flux.transport.commutator
NULL_AXIS = np.array([-1.0, 0.0, 0.0, 1.0])


def product_data(theta=0.9, phi=0.4, alpha=1.0, eta=0.7, axis=NULL_AXIS):
    d = flux.sphere_data(theta, phi, alpha=alpha)
    eta, axis = checks._scalar(eta, "closure coupling"), checks._real(axis, (4,), "axis")
    if np.any(axis[1:3] != 0):
        raise ValueError("Constant axis in the flat normal t,z factor required")
    p, dp = d["P"], d["P_first"]
    b = d["connection"]+eta*axis[:, None, None]*(np.eye(2)-p)
    db = d["connection_first"]-eta*dp[:, None]*axis[None, :, None, None]
    f = checks.connection_curvature(b, db)
    w = dp+commutator(d["connection"], p)
    load = -eta*(w[:, None]*axis[None, :, None, None]-axis[:, None, None, None]*w[None, :])
    return {**d, "unitary_connection": d["connection"], "unitary_curvature": d["curvature"],
            "connection": b, "connection_first": db, "curvature": f,
            "load_curvature": load, "projector_transport": w, "axis": axis, "eta": eta}


def inverse_metric(theta=0.9, radius=1.0, signature="Lorentz"):
    theta = checks._scalar(theta, "polar angle")
    radius, _ = flux._scale(radius, 1)
    if not 0 < theta < np.pi or signature not in ("Lorentz", "Euclidean"):
        raise ValueError("Interior polar angle and declared metric signature required")
    return np.array([-1 if signature == "Lorentz" else 1,
                     1/radius**2, 1/(radius*np.sin(theta))**2, 1.0])


def curvature_density(curvature, inverse, coupling=1.0, pairing="dagger"):
    """Return +Tr(left F^up)/(4g^2); the Lorentz Lagrangians have a minus sign."""
    f = checks._curvature(curvature)
    inverse = checks._real(inverse, (4,), "diagonal inverse metric")
    _, coupling = flux._scale(1, coupling)
    if np.any(inverse == 0) or pairing not in ("dagger", "literal"):
        raise ValueError("Nondegenerate diagonal metric and declared pairing required")
    raised = inverse[:, None, None, None]*inverse[None, :, None, None]*f
    left = f.conj().swapaxes(-1, -2) if pairing == "dagger" else f
    return complex(np.einsum("mnij,mnji->", left, raised)/(4*coupling**2))


def dagger_stress(curvature, inverse, coupling=1.0):
    """Metric variation of the declared dagger action, with F held covariantly fixed."""
    f = checks._curvature(curvature)
    inverse = checks._real(inverse, (4,), "diagonal inverse metric")
    density = curvature_density(f, inverse, coupling)
    first = np.einsum("mlij,l,nlij->mn", f.conj(), inverse, f).real/coupling**2
    return first-np.diag(1/inverse)*density.real


def surface_action(alpha=1.0, eta=0.7, radius=1.0, coupling=1.0,
                   axis=NULL_AXIS, signature="Lorentz", nodes=24):
    radius, coupling = flux._scale(radius, coupling)
    if isinstance(nodes, bool) or not isinstance(nodes, int) or nodes < 8:
        raise ValueError("At least eight quadrature nodes required")
    xs, weights = leggauss(nodes)
    dagger, literal, stress00 = 0j, 0j, 0.0
    for x, weight in zip(xs, weights):
        theta = np.arccos(x)
        d = product_data(theta, 0.37, alpha, eta, axis)
        inverse = inverse_metric(theta, radius, signature)
        factor = 2*np.pi*radius**2*weight
        dagger += factor*curvature_density(d["curvature"], inverse, coupling)
        literal += factor*curvature_density(d["curvature"], inverse, coupling, "literal")
        stress00 += factor*dagger_stress(d["load_curvature"], inverse, coupling)[0, 0]
    return {"plus_dagger_contraction": float(dagger.real),
            "minus_literal_contraction": float(-literal.real),
            "literal_imaginary_part": float(literal.imag),
            "dagger_load_T00_integral": float(stress00)}


def static_residual(theta=0.9, phi=0.4, alpha=1.0, eta=0.7,
                    radius=1.0, axis=NULL_AXIS, step=1e-5):
    """Direct curved-coordinate D^mu F_mu,nu for the PRINTED complex equation."""
    step = checks._scalar(step, "finite difference step")
    if step <= 0:
        raise ValueError("Positive finite difference step required")
    d = product_data(theta, phi, alpha, eta, axis)
    inverse = inverse_metric(theta, radius)
    raised = inverse[:, None, None, None]*inverse[None, :, None, None]*d["curvature"]
    divergence = np.sum(commutator(d["connection"][:, None], raised), axis=0)
    for mu in (1, 2):
        angles = np.array([theta, phi])
        delta = np.eye(2)[mu-1]*step
        neighbors = []
        for sign in (1, -1):
            th, ph = angles+sign*delta
            other = product_data(th, ph, alpha, eta, axis)
            inv = inverse_metric(th, radius)
            density = radius**2*np.sin(th)
            neighbors.append(density*inv[mu]*inv[:, None, None]*other["curvature"][mu])
        divergence += (neighbors[0]-neighbors[1])/(2*step*radius**2*np.sin(theta))
    return divergence/inverse[:, None, None]


def expected_static_residual(theta=0.9, phi=0.4, alpha=1.0, eta=0.7,
                             radius=1.0, axis=NULL_AXIS):
    """Closed formula only for a null normal axis on the assumed product metric."""
    d = product_data(theta, phi, alpha, eta, axis)
    inverse = inverse_metric(theta, radius)
    if abs(np.dot(inverse*d["axis"], d["axis"])) > 1e-12:
        raise ValueError("Null axis required for this residual identity")
    k, s = 2*d["P"]-np.eye(2), 1-alpha
    result = eta*s*s*d["axis"][:, None, None]*k/radius**2
    result[1] += -1j*(2*alpha-alpha**2)*s*d["P_first"][2]/(radius**2*np.sin(theta))
    result[2] += 1j*(2*alpha-alpha**2)*s*np.sin(theta)*d["P_first"][1]/radius**2
    return result


def projector_divergence(theta=0.9, phi=0.4, alpha=1.0, radius=1.0):
    d = product_data(theta, phi, alpha, eta=0)
    dp, ddp, b = d["P_first"], d["P_second"], d["unitary_connection"]
    inverse = inverse_metric(theta, radius)
    return (1-alpha)*(inverse[1]*(ddp[1, 1]+np.cos(theta)/np.sin(theta)*dp[1]
                                 +commutator(b[1], dp[1]))
                       +inverse[2]*(ddp[2, 2]+commutator(b[2], dp[2])))


def probe_penalty_and_leakage(alpha=1.0, eta=0.7, radius=1.0):
    """Instantaneously closed finite probe, not an on-shell sourced solution."""
    d = product_data(alpha=alpha, eta=eta)
    p = d["P"]
    v = flux.patch_data(0.9, 0.4)["frame"]
    psi = v[:, None]*np.array([1, 0, 0, 0])
    h = flux.transport.hessian.phase.minimal_native_closure(0.6*np.eye(2), p)
    scale = np.sqrt(np.abs(inverse_metric(0.9, radius)))[:, None, None]
    normal = flux.transport.normal_operator(p, scale*d["P_first"],
                                            scale*d["connection"], 0.6*np.eye(2))
    return {"U_C7_unit_coefficient": float(np.linalg.norm((np.eye(2)-p) @ psi)**2),
            "H_equals_Lambda_norm": float(np.linalg.norm(h)),
            "U_HC_on_matching_branch": 0.0,
            "normal_operator_norm_squared": normal["norm_squared"]}


def evaluate():
    eta, alpha = 0.7, 0.8
    d = product_data(alpha=alpha, eta=eta)
    inv = inverse_metric()
    residual = static_residual(alpha=alpha, eta=eta)
    expected = expected_static_residual(alpha=alpha, eta=eta)
    euclidean_axis_squared = float(NULL_AXIS @ NULL_AXIS)
    hessian_dagger = -4*np.pi+4*np.pi*eta**2*euclidean_axis_squared
    hessian_literal = -4*np.pi-4*np.pi*eta**2*euclidean_axis_squared
    return {
        "status": "existing-load curvature/constraint audit in a declared R1,1 x S2 realization; NOT a full native stability, Wick rotation or C7 identification",
        "assumptions": ["fixed product metric -dt^2+dz^2+R^2 dOmega^2, coordinates (t,theta,phi,z)",
                        "rank-one round degree-one projector, M=0.6 I, H=Lambda=0",
                        "unitary part B^u=alpha[P,dP], full B=B^u+eta Q n, constant n=-dt+dz",
                        "empty probe for the source-free residual; nonzero closed probe only for an instantaneous penalty test",
                        "R,g,eta are comparison inputs; actual native domain, adjoint and metric not evaluated"],
        "existing_penalties": {"reason": "U_C7 penalizes Q Psi, not D P; U_HC vanishes on H=Lambda; Lambda has no connection argument",
                               "samples": [{"alpha": a, **probe_penalty_and_leakage(a, eta)} for a in (0, 0.8, 1, 1.2, 2)],
                               "eta_does_not_change_the_normal_operator": True},
        "curvature_identity": {"formula": "F=G-eta[(D^u P) wedge n], G=F(B^u), D^u P=(1-alpha)dP",
                               "full_matrix_error": float(np.linalg.norm(d["curvature"]-d["unitary_curvature"]-d["load_curvature"])),
                               "load_curvature_norm": float(np.linalg.norm(d["load_curvature"])),
                               "null_load_dagger_scalar": float(curvature_density(d["load_curvature"], inv).real),
                               "null_load_literal_scalar": float(curvature_density(d["load_curvature"], inv, pairing="literal").real)},
        "null_axis": {"n_squared": float(NULL_AXIS @ (inv*NULL_AXIS)),
                      "static_integrals": [{"alpha": a, **surface_action(a, eta)} for a in (0, 0.8, 1, 1.2, 2)],
                      "dagger_load_stress": "T_mu,nu=eta^2 (1-alpha)^2 n_mu n_nu/(g^2 R^2)",
                      "nonzero_stress_does_not_prove_native_on_shell_or_stability": True,
                      "zero_scalar_is_not_zero_field_or_zero_stress": True},
        "printed_complex_resonance": {"equation": "D^mu F_mu,nu=0 (empty probe, scalar M, H=0)",
                                      "formula": "angular YM residual plus eta (1-alpha)^2 K n_nu/R^2",
                                      "direct_curved_coordinate_error": float(np.linalg.norm(residual-expected)),
                                      "background_residual_norm": float(np.linalg.norm(static_residual(eta=eta))),
                                      "linearized_static_angular_residual_independent_of_eta": True,
                                      "not_a_complete_hyperbolic_stability_analysis": True},
        "Euclidean_real_axis_comparison": {
            "not_a_derived_Wick_rotation": True,
            "axis_squared": euclidean_axis_squared,
            "dagger_energy": "pi (2alpha-alpha^2)^2/(g^2 R^2)+2pi eta^2 |n_E|^2 (1-alpha)^2/g^2",
            "minus_literal_energy": "pi (2alpha-alpha^2)^2/(g^2 R^2)-2pi eta^2 |n_E|^2 (1-alpha)^2/g^2",
            "dagger_Hessian_at_alpha_1_R_g_1_eta_0p7": float(hessian_dagger),
            "minus_literal_Hessian_at_alpha_1_R_g_1_eta_0p7": float(hessian_literal),
            "dagger_no_negative_alpha_direction_condition": "eta^2 |n_E|^2 R^2 >= 1; equality has a quartic minimum along this path",
            "not_a_full_field_stability_threshold_or_native_mass": True,
            "samples": [{"eta": e, **surface_action(alpha, e, signature="Euclidean")} for e in (0, 0.7, 1)],
        },
        "remaining_obligations": ["derive hard D P=0 or evaluate all native stabilizing interactions without imposing it",
                                  "fix the native real form/action and its relation to the printed complex resonance equation",
                                  "solve the full time-dependent constrained system, source reactions and metric/background variations",
                                  "identify actual C7 bundle, admissible M spectrum and physical R,g,eta"],
        "main_TeX_changed": False,
        "literature_context_only": "https://arxiv.org/html/1902.07281v3",
        "not_claimed_to_be_a_universal_or_VSI_Yang_Mills_solution": True}


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
