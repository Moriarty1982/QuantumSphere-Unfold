"""Fixed triadic resonance, Gauss propagation and a hard-dependent eigenmode lift.

The finite prepared resonance is not M_16 or a native mass/scale identification.
"""
import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "triadic_massive_closure", Path(__file__).with_name("HC_Massive_Soft_Closure.py"))
massive = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(massive)
source, checks, dirac = massive.source, massive.checks, massive.dirac
commutator = massive.commutator
TRIAD = dirac.parent.background.triadic_mass()


def real_mass(value):
    value = checks._real(value, (3, 3), "three-channel comparison resonance")
    if not np.allclose(value, value.T, atol=1e-12, rtol=0):
        raise ValueError("A real symmetric comparison resonance required")
    return value


def stationary_jet(u, v, a, electric, mass=TRIAD, omega=0.9, gauge=0.8):
    """Dirac plus temporal Gauss jet; the remaining spatial equation is NOT imposed."""
    mass = real_mass(mass)
    u, v = (checks._real(x, (3,), name) for x, name in ((u, "u"), (v, "v")))
    a, electric = (real_mass(x) for x in (a, electric))
    omega, gauge = checks._scalar(omega, "frequency"), checks._scalar(gauge, "gauge coupling")
    if gauge <= 0:
        raise ValueError("Positive gauge coupling required")
    uu, vv = np.outer(u, u), np.outer(v, v)
    rho, scalar = uu+vv, uu-vv
    du = (omega*np.eye(3)-a+mass) @ v
    dv = (mass-omega*np.eye(3)+a) @ u
    wedge = np.outer(u, v)-np.outer(v, u)
    wedge_first = np.outer(du, v)+np.outer(u, dv)-np.outer(dv, u)-np.outer(v, du)
    electric_first = -gauge*gauge*rho
    constraint = commutator(a, electric)-gauge*gauge*wedge
    constraint_first = commutator(a, electric_first)-gauge*gauge*wedge_first
    return {"u": u, "v": v, "a": a, "electric": electric, "mass": mass,
            "omega": omega, "gauge": gauge, "u_first": du, "v_first": dv,
            "a_first": electric, "electric_first": electric_first,
            "rho": rho, "scalar": scalar, "wedge": wedge, "wedge_first": wedge_first,
            "constraint": constraint, "constraint_first": constraint_first,
            "torque": commutator(mass, scalar)}


def flat_probe_checks(jet):
    """Independent spinor bilinears and current derivatives in the fixed flat spin frame."""
    psi = np.zeros((3, 4), complex)
    psi[:, 1], psi[:, 3] = jet["u"], 1j*jet["v"]
    derivative = np.zeros((4, 3, 4), complex)
    derivative[0] = -1j*jet["omega"]*psi
    derivative[3, :, 1], derivative[3, :, 3] = jet["u_first"], 1j*jet["v_first"]
    gauge = np.zeros((4, 3, 3), complex)
    gauge[0] = jet["a"]
    currents = source.probe.probe_currents(psi, dirac.WEIGHTS, dirac.BETA)
    residual = dirac.dirac_data(psi, derivative+1j*gauge @ psi, jet["mass"])["residual"]
    divergence = source.probe.covariant_current_divergence(
        psi, derivative, gauge, dirac.WEIGHTS, dirac.BETA)
    return {"probe_residual": residual, "current": currents["gauge"],
            "scalar": currents["scalar"], "current_divergence": divergence}


def centralizer_projection(value, mass=TRIAD):
    """Orthogonal matrix projection to the constant resonance's stabilizer algebra."""
    mass = real_mass(mass)
    value = checks._finite(value, "matrix for stabilizer projection")
    if value.shape != (3, 3):
        raise ValueError("A three-channel matrix required")
    eigenvalues, vectors = np.linalg.eigh(mass)
    same = abs(eigenvalues[:, None]-eigenvalues[None, :]) <= 1e-10*max(1, np.max(abs(eigenvalues)))
    return vectors @ (same*(vectors.conj().T @ value @ vectors)) @ vectors.conj().T


def mixed_initial_jet():
    # C=0 initially, but the matrix Ward torque need not vanish there.
    return stationary_jet([0.5, 0, 0], [0.1, 0, 0], np.zeros((3, 3)), 0.03*np.eye(3))


def eigenmode(mass=TRIAD):
    mass = real_mass(mass)
    eigenvalues, vectors = np.linalg.eigh(mass)
    value, vector = float(eigenvalues[-1]), vectors[:, -1].copy()
    if value <= 0:
        raise ValueError("This lifted comparison requires a positive eigenvalue")
    if vector[-1] < 0:
        vector *= -1
    return value, vector, np.outer(vector, vector)


def carrier_gate():
    """Compare inclusion/exclusion of the third component without identifying native C7."""
    visible = np.diag([1.0, 1.0, 0.0])
    complement = np.eye(3)-visible
    _, selected, _ = eigenmode()
    dark = np.array([-0.7, 4, 0])/np.sqrt(16.49)
    dark_projector = np.outer(dark, dark)
    return {"visible": visible, "leakage": complement @ TRIAD @ visible,
            "selected_outside_probability": float(np.vdot(selected, complement @ selected).real),
            "dark_vector": dark, "dark_projector": dark_projector,
            "dark_eigen_residual": TRIAD @ dark-0.6*dark}


def eigenmode_box():
    """Analytic Picard bounds for the NEW positive-eigenmode reference, not the old m=.6 box."""
    mass, _, _ = eigenmode()
    _, omega, gauge, _, _, _ = massive.DEFAULT_PARAMETERS
    bounds = np.array([(omega+0.1+mass)*0.2, (mass-omega+0.1)*0.6,
                       0.13, gauge*gauge*(0.6**2+0.2**2)])
    lipschitz = max(omega+0.1+mass+0.2, mass-omega+0.1+0.6, 1, 2*gauge*gauge*0.8)
    interval = 0.03
    initial = np.array(massive.HARD_INITIAL[:4])
    return {"lower": (initial-0.1).tolist(), "upper": (initial+0.1).tolist(),
            "rhs_abs_bounds": bounds.tolist(), "available_box_radius": 0.1,
            "interval": interval, "max_displacement_bound": float(interval*max(bounds)),
            "Jacobian_infinity_norm_bound": float(lipschitz),
            "Picard_contraction_bound": float(interval*lipschitz)}


def lifted_data(point=(0.4, 0.9, 0.4, 0.02), radius=1.0, eta=0.7):
    """Six-dimensional Hopf x generation carrier; independent H variation is excluded."""
    mass, vector, mode_projector = eigenmode()
    params = (mass, *massive.DEFAULT_PARAMETERS[1:])
    point = checks._real(point, (4,), "product coordinates")
    if abs(point[3]) > eigenmode_box()["interval"]:
        raise ValueError("Only the proved local positive-eigenmode interval is evaluated")
    eta = checks._scalar(eta, "closure coupling")
    base = massive.field_data(point, params=params, domain="hard", radius=radius, eta=eta)
    sphere = source.load.flux.sphere_data(point[1], point[2])
    p = np.kron(base["P"], np.eye(3))
    dp = np.array([np.kron(x, np.eye(3)) for x in base["P_first"]])
    charged = np.kron(base["P"], mode_projector)
    charged_first = np.array([np.kron(x, mode_projector) for x in base["P_first"]])
    a, electric = base["state"][2:4]
    unitary = np.array([np.kron(x, np.eye(3)) for x in sphere["connection"]])
    derivative = np.array([[np.kron(x, np.eye(3)) for x in row] for row in sphere["connection_first"]])
    unitary[0] += 1j*a*charged
    derivative[:, 0] += 1j*a*charged_first
    derivative[3, 0] += 1j*electric*charged
    axis = source.dynamics.AXIS
    connection = unitary+eta*axis[:, None, None]*(np.eye(6)-p)
    dconnection = derivative-eta*dp[:, None]*axis[None, :, None, None]
    psi = np.einsum("as,b->abs", base["psi"], vector).reshape(6, 4)
    dpsi = np.einsum("mas,b->mabs", base["psi_first"], vector).reshape(4, 6, 4)
    currents = source.probe.probe_currents(psi, dirac.BETA @ base["bundle"]["gamma"], dirac.BETA)
    return {"P": p, "P_first": dp, "charged_projector": charged,
            "unitary": unitary, "unitary_first": derivative, "connection": connection,
            "connection_first": dconnection, "G": checks.connection_curvature(unitary, derivative),
            "F": checks.connection_curvature(connection, dconnection),
            "psi": psi, "psi_first": dpsi, "mass_operator": np.kron(np.eye(2), TRIAD),
            "current_up": currents["gauge"], "scalar": currents["scalar"],
            "bundle": base["bundle"], "base": base, "eigenvalue": mass, "eigenvector": vector,
            "point": point, "radius": base["radius"]}


def lifted_residuals(point=(0.4, 0.9, 0.4, 0.02), step=1e-5, **kwargs):
    step = checks._scalar(step, "derivative step")
    if step <= 0:
        raise ValueError("Positive derivative step required")
    d = lifted_data(point, **kwargs)
    inverse = source.load.inverse_metric(d["point"][1], d["radius"])
    raised = inverse[:, None, None, None]*inverse[None, :, None, None]*d["F"]
    resonance = np.sum(commutator(d["connection"][:, None], raised), axis=0)
    divergence = np.sum(commutator(d["unitary"], d["current_up"]), axis=0)
    density = d["radius"]**2*np.sin(d["point"][1])
    for mu, direction in enumerate(np.eye(4)):
        samples = []
        for sign in (1, -1):
            other = lifted_data(d["point"]+sign*step*direction, **kwargs)
            inv = source.load.inverse_metric(other["point"][1], d["radius"])
            volume = d["radius"]**2*np.sin(other["point"][1])
            samples.append((volume*inv[mu]*inv[:, None, None]*other["F"][mu],
                            volume*other["current_up"][mu]))
        resonance += (samples[0][0]-samples[1][0])/(2*step*density)
        divergence += (samples[0][1]-samples[1][1])/(2*step*density)
    lower_current = np.einsum("mn,nij->mij", d["bundle"]["metric"], d["current_up"])
    gauge = d["base"]["params"][2]
    residual = dirac.dirac_data(
        d["psi"], d["psi_first"]+d["connection"] @ d["psi"], d["mass_operator"],
        gamma=d["bundle"]["gamma"], metric=d["bundle"]["metric"], spin=d["bundle"]["spin"])["residual"]
    return {"Dirac": residual,
            "gauge": resonance/inverse[:, None, None]-1j*gauge*gauge*lower_current,
            "current_divergence": divergence,
            "Ward": divergence+1j*commutator(d["mass_operator"], d["scalar"])}


def evaluate():
    jet = mixed_initial_jet()
    flat = flat_probe_checks(jet)
    d, residuals = lifted_data(), lifted_residuals()
    mass, vector, q = eigenmode()
    carrier = carrier_gate()
    weak = np.array([1, 0, 0])
    defect = TRIAD @ weak-float(weak @ TRIAD @ weak)*weak
    return {
        "status": "conditional fixed-triadic Gauss compatibility and local hard-dependent eigenmode comparison; NOT native M_16/C7 identification or physical masses",
        "native_HC_domain_audit": {
            "source": "sources/research/parts/v470/10_sphaera_and_physics.tex",
            "hard_reading": "prop:closure-equation and thm:closed-master-system impose H=Lambda; exact closure sets H=0",
            "finite_penalty_reading": "thm:variational-form lists H as a field with finite ||H-Lambda||^2; this alone does not derive algebraic equality",
            "independent_soft_H_equation_is_not_silently_added_to_hard_lift": True},
        "fixed_matrix_gate": {
            "Ward": "D_mu j^mu=-i[Omega,S] with ordinary adjoint and fixed Hermitian resonance",
            "Gauss": "A''=-g^2 rho; C=[A,A']-g^2(U V^T-V U^T)=0 is the remaining spatial gauge equation",
            "propagation": "C'=g^2[Omega,S]; solving Dirac plus temporal Gauss does not automatically preserve C",
            "scope": "full unitary matrix source with no additional adjoint-field currents; not every native gauge algebra or dynamical resonance",
            "mixed_initial_C_norm": float(np.linalg.norm(jet["constraint"])),
            "mixed_initial_C_first_norm": float(np.linalg.norm(jet["constraint_first"])),
            "mixed_initial_torque_norm": float(np.linalg.norm(jet["torque"])),
            "flat_Dirac_residual_norm": float(np.linalg.norm(flat["probe_residual"])),
            "flat_Ward_residual_norm": float(np.linalg.norm(flat["current_divergence"]+1j*jet["torque"])),
            "ordinary_trace_divergence_abs": float(abs(np.trace(flat["current_divergence"]))),
            "stabilizer_projected_torque_norm": float(np.linalg.norm(centralizer_projection(jet["torque"])))},
        "prepared_resonance": {"matrix": TRIAD.tolist(), "eigenvalues": np.linalg.eigvalsh(TRIAD).tolist(),
                               "selected_positive_eigenvalue": mass, "selected_vector": vector.tolist(),
                               "component_weights": (vector*vector).tolist(),
                               "unchanged_weak_basis_vector_residual": float(np.linalg.norm(defect)),
                               "not_native_M16_or_measured_masses": True},
        "carrier_gate": {"comparison_lift_admits_all_three_generation_components": True,
                         "if_third_component_is_excluded": {
                             "visible_projector": carrier["visible"].tolist(),
                             "resonance_off_sector_norm": float(np.linalg.norm(carrier["leakage"])),
                             "selected_eigenmode_outside_probability": carrier["selected_outside_probability"],
                             "single_dark_vector": carrier["dark_vector"].tolist(),
                             "dark_eigen_residual_norm": float(np.linalg.norm(carrier["dark_eigen_residual"])),
                             "dark_state_does_not_make_the_whole_visible_projector_invariant": True},
                         "native_C7_assignment_of_the_orthogonal_triadic_component_remains_unknown": True},
        "eigenmode_lift": {"carrier": "Hopf rank-one image in C2 tensor C3; P=P_Hopf tensor I3",
                           "connection": "B^u=B_geom tensor I3+i a(z) P_Hopf tensor q dt; Omega=I2 tensor prepared triad",
                           "domain": "H=Lambda=0 eliminated before variation, not the independent finite-penalty domain",
                           "local_existence_bounds": eigenmode_box(),
                           "point": d["point"].tolist(), "rho": float(np.trace(d["current_up"][0]).real),
                           "scalar": float(np.trace(d["scalar"]).real),
                           "closure_transport_norm": float(np.linalg.norm(d["P_first"]+commutator(d["connection"], d["P"]))),
                           "resonance_projector_commutator_norm": float(np.linalg.norm(commutator(d["mass_operator"], d["P"]))),
                           "resonance_scalar_commutator_norm": float(np.linalg.norm(commutator(d["mass_operator"], d["scalar"]))),
                           "full_matrix_residual_norms": {name: float(np.linalg.norm(value)) for name, value in residuals.items()},
                           "independent_HC_equation_not_solved_or_imposed": True},
        "remaining_native_obligations": [
            "fix hard/soft field domain and real action/current dictionary before interpreting any comparison as native",
            "identify actual gauge algebra and Omega=m0 I+alpha P M16 P+beta gY T+gamma H on the same carrier",
            "choose a compatible state/gauge stabilizer OR derive the dynamical adjoint torque current; a basis rotation alone does not remove a nonzero torque",
            "evaluate global patching, finite-energy data, metric/axis backreaction and temporal stability"],
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
