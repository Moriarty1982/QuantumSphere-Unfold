"""Time-dependent null-load closure: complex constraints versus declared real actions."""
import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


SPEC = importlib.util.spec_from_file_location(
    "dynamical_load", Path(__file__).with_name("HC_Closure_Load_Stability.py"))
load = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(load)
checks, commutator = load.checks, load.commutator
AXIS = load.NULL_AXIS


def mode_jet(w, v, dw, dv, ddw, ddv):
    result = {"w": checks._scalar(w, "w"), "v": checks._scalar(v, "v")}
    for name, value, shape in (("dw", dw, (2,)), ("dv", dv, (2,)),
                               ("ddw", ddw, (2, 2)), ("ddv", ddv, (2, 2))):
        result[name] = checks._real(value, shape, name)
        if len(shape) == 2 and not np.allclose(result[name], result[name].T, atol=1e-12, rtol=0):
            raise ValueError("Symmetric scalar Hessians required")
    return result


def polynomial_profile(t, z):
    t, z = checks._scalar(t, "time"), checks._scalar(z, "position")
    w = 0.12+0.17*t-0.08*z+0.04*t*t+0.03*t*z-0.02*z*z
    v = -0.07+0.05*t+0.11*z-0.03*t*t+0.02*t*z+0.06*z*z
    return mode_jet(w, v, [0.17+0.08*t+0.03*z, -0.08+0.03*t-0.04*z],
                    [0.05-0.06*t+0.02*z, 0.11+0.02*t+0.12*z],
                    [[0.08, 0.03], [0.03, -0.04]], [[-0.06, 0.02], [0.02, 0.12]])


def pulse_profile(t, z=0.0, radius=1.0, center=0.0):
    t, z, center = [checks._scalar(x, name) for x, name in ((t, "time"), (z, "position"), (center, "center"))]
    radius, _ = load.flux._scale(radius, 1)
    tau = (t-center)/radius
    exponential = np.exp(-abs(tau))
    w = 2*np.sqrt(2)*exponential/(1+exponential**2)
    dw = -w*np.tanh(tau)/radius
    ddw = w*(2*np.tanh(tau)**2-1)/radius**2
    return mode_jet(w, 0, [dw, 0], [0, 0], [[ddw, 0], [0, 0]], np.zeros((2, 2)))


def growing_profile(t, z, radius=1.0, epsilon=0.02, wavenumber=0.4):
    radius, _ = load.flux._scale(radius, 1)
    t, z, epsilon, k = [checks._scalar(x, name) for x, name in
                         ((t, "time"), (z, "position"), (epsilon, "amplitude"), (wavenumber, "wave number"))]
    if abs(k) >= 1/radius:
        raise ValueError("Growing-mode wave number requires |k|<1/R")
    rate = np.sqrt(1/radius**2-k*k)
    amplitude = epsilon*np.exp(rate*t)
    w, wz = amplitude*np.cos(k*z), -k*amplitude*np.sin(k*z)
    return mode_jet(w, 0, [rate*w, wz], [0, 0],
                    [[rate*rate*w, rate*wz], [rate*wz, -k*k*w]], np.zeros((2, 2)))


def field_data(point=(0.4, 0.9, 0.4, -0.2), profile=polynomial_profile, eta=0.7):
    point = checks._real(point, (4,), "product coordinates")
    t, theta, phi, z = point
    eta = checks._scalar(eta, "closure coupling")
    raw = profile(t, z)
    jet = mode_jet(**raw)
    base = load.flux.sphere_data(theta, phi)
    a, da, p, dp, ddp = [base[x] for x in ("connection", "connection_first", "P", "P_first", "P_second")]
    w, v = jet["w"], jet["v"]
    dw, dv = np.zeros(4), np.zeros(4)
    dw[[0, 3]], dv[[0, 3]] = jet["dw"], jet["dv"]
    unitary = (1+w)*a+1j*v*dp
    derivative = (1+w)*da+1j*v*ddp+dw[:, None, None, None]*a[None]+1j*dv[:, None, None, None]*dp[None]
    b = unitary+eta*AXIS[:, None, None]*(np.eye(2)-p)
    db = derivative-eta*dp[:, None]*AXIS[None, :, None, None]
    g = checks.connection_curvature(unitary, derivative)
    f = checks.connection_curvature(b, db)
    transported = dp+commutator(unitary, p)
    x = -eta*(transported[:, None]*AXIS[None, :, None, None]-AXIS[:, None, None, None]*transported[None])
    return {"P": p, "P_first": dp, "P_second": ddp, "geometric": a, "geometric_first": da,
            "unitary": unitary, "unitary_first": derivative, "connection": b, "connection_first": db,
            "G": g, "F": f, "X": x, "W": transported, "jet": jet, "point": point, "eta": eta}


def expected_residuals(point=(0.4, 0.9, 0.4, -0.2), profile=polynomial_profile,
                       eta=0.7, radius=1.0):
    radius, _ = load.flux._scale(radius, 1)
    d = field_data(point, profile, eta)
    j, a, dp, p = d["jet"], d["geometric"], d["P_first"], d["P"]
    w, v, k = j["w"], j["v"], 2*p-np.eye(2)
    height = 1-w*w-v*v
    ew = -j["ddw"][0, 0]+j["ddw"][1, 1]+height*w/radius**2
    ev = -j["ddv"][0, 0]+j["ddv"][1, 1]+height*v/radius**2
    real = ew*a+1j*ev*dp
    for mu, rho in enumerate((0, 3)):
        real[rho] = 1j*(v*j["dw"][mu]-w*j["dv"][mu])*k/radius**2
    normal_w = -sum(j["dw"])*dp-1j*sum(j["dv"])*a
    printed = real+2*eta*normal_w
    printed += eta*(w*w+v*v)*AXIS[:, None, None]*k/radius**2
    return {"unitary": real, "printed": printed, "projector": np.zeros((2, 2), complex)}


def residuals(point=(0.4, 0.9, 0.4, -0.2), profile=polynomial_profile,
              eta=0.7, radius=1.0, step=1e-5):
    """Full curved-coordinate divergences, including normal equations omitted by reduction."""
    radius, _ = load.flux._scale(radius, 1)
    step = checks._scalar(step, "derivative step")
    if step <= 0:
        raise ValueError("Positive derivative step required")
    d = field_data(point, profile, eta)
    inverse = load.inverse_metric(d["point"][1], radius)
    results = {}
    for key, connection in (("G", "unitary"), ("F", "connection"), ("X", "unitary")):
        raised = inverse[:, None, None, None]*inverse[None, :, None, None]*d[key]
        results[key] = np.sum(commutator(d[connection][:, None], raised), axis=0)
    for mu, direction in enumerate(np.eye(4)):
        samples = []
        for sign in (1, -1):
            other = field_data(d["point"]+sign*step*direction, profile, eta)
            inv = load.inverse_metric(other["point"][1], radius)
            density = radius**2*np.sin(other["point"][1])
            samples.append({key: density*inv[mu]*inv[:, None, None]*other[key][mu] for key in ("G", "F", "X")})
        for key in results:
            results[key] += (samples[0][key]-samples[1][key])/(2*step*radius**2*np.sin(d["point"][1]))
    results = {key: value/inverse[:, None, None] for key, value in results.items()}
    phi = eta*(np.eye(2)-d["P"])
    raised_x = inverse[:, None, None, None]*inverse[None, :, None, None]*d["X"]
    force = np.einsum("m,mnij->nij", AXIS, commutator(phi, raised_x))/inverse[:, None, None]
    projector_force = -eta*np.einsum("m,mij->ij", inverse*AXIS, results["X"])
    p, q = d["P"], np.eye(2)-d["P"]
    tangent = p @ projector_force @ q+q @ projector_force @ p
    return {"unitary": results["G"], "printed": results["F"],
            "dagger_unitary_EL": results["G"]-force,
            "real_literal_unitary_EL": -results["G"]-force,
            "projector_EL": tangent, "load_force": force}


def reduced_action(jet, radius=1.0, coupling=1.0, eta=0.7):
    radius, coupling = load.flux._scale(radius, coupling)
    eta = checks._scalar(eta, "closure coupling")
    j = mode_jet(**jet)
    kinetic = sum(d[0]**2-d[1]**2 for d in (j["dw"], j["dv"]))
    height = 1-j["w"]**2-j["v"]**2
    dagger = 2*np.pi*kinetic/coupling**2-np.pi*height**2/(coupling**2*radius**2)
    phase_current = j["v"]*sum(j["dw"])-j["w"]*sum(j["dv"])
    return {"dagger_L": float(dagger), "real_literal_L": float(-dagger),
            "literal_imaginary_L": float(-4*np.pi*eta*phase_current/coupling**2)}


def integrated_action(t=0.4, z=-0.2, profile=polynomial_profile, eta=0.7,
                      radius=1.0, coupling=1.0, nodes=20):
    radius, coupling = load.flux._scale(radius, coupling)
    if isinstance(nodes, bool) or not isinstance(nodes, int) or nodes < 8:
        raise ValueError("At least eight quadrature nodes required")
    xs, weights = leggauss(nodes)
    dagger = literal = 0j
    for x, weight in zip(xs, weights):
        theta = np.arccos(x)
        d = field_data([t, theta, 0.37, z], profile, eta)
        inv = load.inverse_metric(theta, radius)
        factor = -2*np.pi*radius**2*weight
        dagger += factor*load.curvature_density(d["F"], inv, coupling)
        literal += factor*load.curvature_density(d["F"], inv, coupling, "literal")
    return {"dagger_L": float(dagger.real), "real_literal_L": float(literal.real),
            "literal_imaginary_L": float(literal.imag)}


def projector_identity(point=(0.4, 0.9, 0.4, -0.2), profile=polynomial_profile,
                       angular_addition=None, angular_first=None, radius=1.0):
    """Pointwise positive projector identity, also for nonsymmetric unitary jets."""
    d = field_data(point, profile)
    u, du = d["unitary"].copy(), d["unitary_first"].copy()
    if angular_addition is not None or angular_first is not None:
        b = checks._finite(angular_addition, "angular connection addition")
        db = checks._finite(angular_first, "angular connection jet")
        if b.shape != (2, 2, 2) or db.shape != (2, 2, 2, 2):
            raise ValueError("Two angular connection matrices and their two derivatives required")
        if not np.allclose(b, -b.conj().swapaxes(-1, -2), atol=1e-12, rtol=0):
            raise ValueError("Unitary angular addition required")
        if not np.allclose(db, -db.conj().swapaxes(-1, -2), atol=1e-12, rtol=0):
            raise ValueError("Unitary angular first jet required")
        u[1:3] += b
        du[1:3, 1:3] += db
    p, dp, ddp = d["P"], d["P_first"], d["P_second"]
    w = dp+commutator(u, p)
    inv = load.inverse_metric(d["point"][1], radius)
    laplacian = np.zeros((2, 2), complex)
    norm = 0.0
    for a in (1, 2):
        term = ddp[a, a]+commutator(du[a, a], p)+commutator(u[a], dp[a])+commutator(u[a], w[a])
        if a == 1:
            term += np.cos(d["point"][1])/np.sin(d["point"][1])*w[a]
        laplacian += inv[a]*term
        norm += inv[a]*np.vdot(w[a], w[a]).real
    return {"laplacian": laplacian, "trace_P_laplacian": complex(np.trace(p @ laplacian)),
            "positive_transport_norm_squared": float(norm)}


def evaluate():
    point, eta, radius = np.array([0.4, 0.9, 0.4, -0.2]), 0.7, 1.0
    direct, expected = residuals(point), expected_residuals(point)
    pulse = residuals(point, pulse_profile)
    mode = residuals(point, growing_profile)
    j = pulse_profile(point[0])
    energy = 2*np.pi*j["dw"][0]**2+np.pi*(1-j["w"]**2)**2
    identity = projector_identity(point)
    return {
        "status": "conditional dynamical closure/real-form distinction on a fixed auxiliary R1,1 x S2; NOT native C7 stability, gravity or a selected physical action",
        "assumptions": ["fixed product metric, degree-one round P independent of t,z, unitary normal connection zero",
                        "M scalar, H_C=Lambda=0, empty probe and zero printed currents; no native C7/scale identification",
                        "B^u_a=(1+w)[P,d_a P]+i v d_a P, w,v real; B=B^u+eta Q(-dt+dz)",
                        "normal connection equations are checked after variation, not discarded by this ansatz",
                        "real literal and dagger actions are distinct comparisons; neither is silently adopted"],
        "two_mode_curvature": {"G_angular": "(1-w^2-v^2) G_background", "W": "-w dP-i v [P,dP]",
                               "printed_angular": "D_u^mu G_mu,a +2 eta (partial_t+partial_z) W_a",
                               "printed_normal": "i(v partial_rho w-w partial_rho v)K/R^2+eta(w^2+v^2)K n_rho/R^2",
                               "full_printed_residual_error": float(np.linalg.norm(direct["printed"]-expected["printed"])),
                               "unitary_residual_error": float(np.linalg.norm(direct["unitary"]-expected["unitary"]))},
        "constraint_theorem": {"identity": "Tr(P D_a W^a)=-Tr(W_a W^a), W=D_u P Hermitian and purely angular",
                               "trace_P_laplacian": float(identity["trace_P_laplacian"].real),
                               "positive_transport_norm_squared": identity["positive_transport_norm_squared"],
                               "consequence": "Hermitian normal part of the printed source-free equation forces D_a W^a=0, hence W=0 pointwise",
                               "equivariant_consequence_for_eta_nonzero": "w=v=0 exactly",
                               "requires_nonzero_eta_and_this_source_normal_sector": True,
                               "not_a_general_native_or_sourced_superselection_theorem": True},
        "linearized_dynamics": {"real_action_equations": "(partial_t^2-partial_z^2)w-w/R^2=0, and likewise v",
                                "growth_rate": "sqrt(R^-2-k^2) for |k|<R^-1; no derived physical mass",
                                "example_R": radius, "example_k": 0.4, "example_growth_rate": float(np.sqrt(1-0.4**2)),
                                "printed_additional_conditions_eta_nonzero": "(partial_t+partial_z)w=(partial_t+partial_z)v=0",
                                "joint_equations_have_only_zero_mode_at_finite_R_in_this_sector": True,
                                "not_damping_of_arbitrary_Cauchy_data": True,
                                "growing_mode_real_action_residual_norm": float(np.linalg.norm(mode["dagger_unitary_EL"])),
                                "growing_mode_printed_residual_norm": float(np.linalg.norm(mode["printed"]))},
        "exact_real_action_pulse": {"profile": "w=sqrt(2) sech((t-t0)/R), v=0",
                                    "equation": "w_tt=w(1-w^2)/R^2",
                                    "dagger_gauge_residual_norm": float(np.linalg.norm(pulse["dagger_unitary_EL"])),
                                    "real_literal_gauge_residual_norm": float(np.linalg.norm(pulse["real_literal_unitary_EL"])),
                                    "projector_tangent_residual_norm": float(np.linalg.norm(pulse["projector_EL"])),
                                    "printed_complex_residual_norm": float(np.linalg.norm(pulse["printed"])),
                                    "homogeneous_reduced_energy_R_g_1": float(energy),
                                    "energy_formula": "pi/(g^2 R^2), conserved along the pulse, not irreversible damping",
                                    "not_a_native_on_shell_probe_metric_solution": True},
        "reduced_actions": {"dagger": "2pi[(w_t^2+v_t^2)-(w_z^2+v_z^2)]/g^2-pi(1-w^2-v^2)^2/(g^2 R^2)",
                            "real_literal": "minus the dagger action on this null sector; full actions differ outside it",
                            "literal_imaginary": "-4pi eta [v(partial_t+partial_z)w-w(partial_t+partial_z)v]/g^2",
                            "full_matrix_integral": integrated_action(),
                            "formula": reduced_action(polynomial_profile(point[0], point[3])),
                            "varying_only_w_after_setting_v_and_normal_connection_zero_misses_constraints": True},
        "remaining_obligations": ["native adjoint, real versus complex stationarity and consistent field space",
                                  "nonempty currents, dynamical projector/axis and normal connection/curvature",
                                  "constraint propagation and full Cauchy problem outside the declared truncation",
                                  "actual C7 carrier, M spectrum, metric/backreaction and physical scales"],
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
