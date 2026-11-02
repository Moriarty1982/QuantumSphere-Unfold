"""Source typing, hard-closure trace and a local charged massless comparison branch."""
import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "sourced_closure_dynamics", Path(__file__).with_name("HC_Null_Axis_Dynamical_Closure.py"))
dynamics = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(dynamics)
load, checks = dynamics.load, dynamics.checks
transport = load.flux.transport
dirac, commutator = transport.dirac, transport.commutator
probe = dirac.geometry.probe


def closure_trace_current(m, dm, p, dp):
    m, p = checks._generator(m), transport.hessian.projector(p)
    dm, dp = checks._finite(dm, "matrix jet"), checks._finite(dp, "projector jet")
    if m.shape != p.shape or dm.shape != (4, *m.shape) or dp.shape != dm.shape:
        raise ValueError("Matrix/projector jets on the same carrier required")
    return np.trace(dm @ p+m @ dp, axis1=-2, axis2=-1)


def product_spin_bundle(theta=0.9, radius=1.0):
    load.inverse_metric(theta, radius)
    e = np.diag([1.0, radius, radius*np.sin(theta), 1.0])
    de, dde = np.zeros((4, 4, 4)), np.zeros((4, 4, 4, 4))
    de[1, 2, 2], dde[1, 1, 2, 2] = radius*np.cos(theta), -radius*np.sin(theta)
    return dirac.bundle(e, de, dde)


def charged_data(point=(0.4, 0.9, 0.4, -0.2), radius=1.0, density=0.4,
                 coupling=1.0, eta=0.7, axis_shape=0.0, sign=1, patch="north"):
    point = checks._real(point, (4,), "product coordinates")
    radius, coupling = load.flux._scale(radius, coupling)
    density, eta, shape = [checks._scalar(x, name) for x, name in
                            ((density, "probe density"), (eta, "closure coupling"), (axis_shape, "axis shape"))]
    if density < 0 or isinstance(sign, bool) or sign not in (-1, 1) or patch not in ("north", "south"):
        raise ValueError("Nonnegative density, source sign +/-1 and named patch required")
    t, theta, phi, z = point
    base = load.flux.sphere_data(theta, phi)
    p, dp = base["P"], base["P_first"]
    coefficient = sign*coupling**2*density
    potential = np.array([0, 0, 0, coefficient*(t*z-t*t/2)])
    dpotential = np.zeros((4, 4))
    dpotential[0, 3], dpotential[3, 3] = coefficient*(z-t), coefficient*t
    u = base["connection"]+1j*potential[:, None, None]*p
    du = (base["connection_first"]+1j*dpotential[:, :, None, None]*p
          +1j*potential[None, :, None, None]*dp[:, None])
    axis = (1+shape*z*z/2)*dynamics.AXIS
    daxis = np.zeros((4, 4))
    daxis[3] = shape*z*dynamics.AXIS
    b = u+eta*axis[:, None, None]*(np.eye(2)-p)
    db = du-eta*dp[:, None]*axis[None, :, None, None]+eta*daxis[:, :, None, None]*(np.eye(2)-p)
    g, f = checks.connection_curvature(u, du), checks.connection_curvature(b, db)
    vector = np.array([np.cos(theta/2), np.exp(1j*phi)*np.sin(theta/2)])
    dv = np.zeros((4, 2), complex)
    dv[1] = [-np.sin(theta/2)/2, np.exp(1j*phi)*np.cos(theta/2)/2]
    dv[2] = [0, 1j*vector[1]]
    angle, angular_rate = -phi/2, -0.5
    if patch == "south":
        dv[2] -= 1j*vector
        vector, dv = np.exp(-1j*phi)*vector, np.exp(-1j*phi)*dv
        angle, angular_rate = phi/2, 0.5
    phase = coefficient*(t*t*z/2-t**3/3)
    dphase = np.array([coefficient*(t*z-t*t), 0, 0, coefficient*t*t/2])
    spinor = np.sqrt(density)*np.exp(1j*(angle-phase))*np.array([0, 1, 0, -1])/np.sqrt(2)
    dspinor = -1j*dphase[:, None]*spinor
    dspinor[2] += 1j*angular_rate*spinor
    psi = vector[:, None]*spinor
    first = dv[:, :, None]*spinor+vector[None, :, None]*dspinor[:, None]
    bundle = product_spin_bundle(theta, radius)
    weights = dirac.BETA @ bundle["gamma"]
    currents = probe.probe_currents(psi, weights, dirac.BETA)
    metric = bundle["metric"]
    current_lower = np.einsum("mn,nij->mij", metric, currents["gauge"])
    return {"P": p, "P_first": dp, "unitary": u, "unitary_first": du,
            "connection": b, "connection_first": db, "G": g, "F": f,
            "axis": axis, "axis_first": daxis, "psi": psi, "psi_first": first,
            "bundle": bundle, "weights": weights, "current_up": currents["gauge"],
            "current_lower": current_lower, "scalar_source": currents["scalar"],
            "phase": float(phase), "potential": potential, "point": point,
            "density": density, "coupling": coupling, "eta": eta, "axis_shape": shape,
            "sign": sign, "radius": radius}


def probe_residual(data, mass=0.0, ordered=True):
    mass = checks._scalar(mass, "comparison mass")
    connection = data["connection"] if ordered else data["unitary"]
    bundle = data["bundle"]
    return dirac.dirac_data(data["psi"], data["psi_first"]+connection @ data["psi"],
                            mass*np.eye(2), gamma=bundle["gamma"], metric=bundle["metric"],
                            spin=bundle["spin"])["residual"]


def resonance(point=(0.4, 0.9, 0.4, -0.2), step=1e-5, **kwargs):
    step = checks._scalar(step, "derivative step")
    if step <= 0:
        raise ValueError("Positive finite difference step required")
    d = charged_data(point, **kwargs)
    radius = d["radius"]
    inverse = load.inverse_metric(d["point"][1], radius)
    raised = inverse[:, None, None, None]*inverse[None, :, None, None]*d["F"]
    result = np.sum(commutator(d["connection"][:, None], raised), axis=0)
    for mu, direction in enumerate(np.eye(4)):
        samples = []
        for sign in (1, -1):
            other = charged_data(d["point"]+sign*step*direction, **kwargs)
            inv = load.inverse_metric(other["point"][1], radius)
            samples.append(radius**2*np.sin(other["point"][1])*inv[mu]*inv[:, None, None]*other["F"][mu])
        result += (samples[0]-samples[1])/(2*step*radius**2*np.sin(d["point"][1]))
    return result/inverse[:, None, None]


def expected_resonance(data):
    result = 1j*data["sign"]*data["coupling"]**2*data["current_lower"]
    result[0] -= data["eta"]*data["axis_shape"]*(np.eye(2)-data["P"])
    return result


def source_variation(data, direction, component=0, step=1e-5):
    direction = checks._generator(direction)
    step = checks._scalar(step, "variation step")
    if direction.shape != (2, 2) or isinstance(component, bool) or component not in range(4) or step <= 0:
        raise ValueError("Hermitian carrier direction, coordinate component and positive step required")
    gauge = -1j*data["unitary"]
    values = []
    for sign in (1, -1):
        other = gauge.copy()
        other[component] += sign*step*direction
        values.append(probe.real_probe_density(data["psi"], data["psi_first"], other,
                                               np.zeros((2, 2)), data["weights"], dirac.BETA,
                                               mass=0, yukawa=0))
    return (values[0]-values[1])/(2*step)


def evaluate():
    point = [0.4, 0.9, 0.4, -0.2]
    d = charged_data(point)
    e = resonance(point)
    covariant = d["current_lower"]
    norm = np.linalg.norm(probe_residual(d))
    shaped = charged_data(point, axis_shape=d["density"]/d["eta"])
    shaped_e = resonance(point, axis_shape=d["density"]/d["eta"])
    h = (shaped_e+shaped_e.conj().swapaxes(-1, -2))/2
    m = 0.6*np.eye(2)
    return {
        "status": "conditional current/closure typing identities plus a local CHARGED MASSLESS real-comparison probe/gauge branch; NOT a native massive C7, global spinor or gravity solution",
        "native_audit": {"source_path": "sources/research/parts/v470/10_sphaera_and_physics.tex",
                         "source_labels": ["thm:variational-form", "thm:resonance-field-eq", "thm:closed-master-system"],
                         "printed_bilinear_is_scalar_without_specified_gauge_generator_or_phase": True,
                         "fixed_M_exact_closure_current": closure_trace_current(m, np.zeros((4, 2, 2)), d["P"], d["P_first"]).real.tolist(),
                         "fixed_M_identity": "[M,P]=0 and P^2=P imply Tr(M dP)=0; for variable M retain Tr((dM)P)",
                         "hard_trace": "Re Tr(F)=d[(kappa Tr(H_C)+eta rank(Q))n]; H_C=0 and dn=0 give Re Tr(D.F)=0",
                         "consequence": "a positive-time Hermitian probe current cannot be the sole literal scalar/matrix source under this ordinary real-form reading",
                         "not_a_no_go_for_an_unspecified_native_adjoint_or_current_embedding": True},
        "supported_source": {"identity": "Q Psi=0 gives j=P j P; for compatible transport and H_C=0, Herm(D.F)=eta Q div(dn)",
                             "consequence": "even a variable null axis supplies its Hermitian response in Q, not the closed probe's P block",
                             "trace_matched_axis_control": {"axis_shape": shaped["axis_shape"],
                                                            "real_trace_E_t": float(np.trace(h[0]).real),
                                                            "trace_probe_j_t": float(np.trace(covariant[0]).real),
                                                            "matrix_mismatch_norm": float(np.linalg.norm(h[0]-covariant[0]))},
                             "anti_Hermitian_source_is_distinct_from_direct_Hermitian_insertion": True},
        "charged_comparison": {"assumptions": ["fixed R1,1 x round S2, local polar patch; no native bilinear metric or global spinor extension asserted",
                                                "degree-one P, compatible B^u=[P,dP]+i a P, n=-dt+dz, H_C=0, M scalar",
                                                "F is internal gauge/closure curvature; the additional Levi-Civita spin curvature is not identified with native full [D,D]",
                                                "ordinary spin adjoint and real symmetric massless probe action; Omega=0 is an additional comparison assumption",
                                                "dagger bosonic action coefficient 1/g^2 gives D_u G=i g^2 j; the real-literal action has the opposite source sign",
                                                "projector/HC first variations vanish in this comparison; metric/axis backreaction and native resonance identification not solved"],
                               "normal_potential": "a_t=0, a_z=s g^2 rho(t z-t^2/2), s=+1 dagger or -1 real-literal",
                               "phase": "S=s g^2 rho(t^2 z/2-t^3/3)",
                               "local_probe": "Psi_N=V_N sqrt(rho) exp[-i S-i phi/2](0,1,0,-1)/sqrt(2)",
                               "south_patch_probe": "V_S=exp(-i phi)V_N, spin phase exp(+i phi/2); same local coordinate field on overlap",
                               "source": "j^t=rho P, j^z=rho P, j^theta=j^phi=0, S_scalar=0",
                               "full_Dirac_residual_norm": float(norm),
                               "full_matrix_gauge_residual_norm": float(np.linalg.norm(e-1j*d["coupling"]**2*covariant)),
                               "direct_Hermitian_source_residual_norm": float(np.linalg.norm(e-d["coupling"]**2*covariant)),
                               "restored_mass_0p6_residual_norm": float(np.linalg.norm(probe_residual(d, mass=0.6))),
                               "comparison_density": d["density"], "comparison_radius": d["radius"],
                               "current_time_trace": float(np.trace(d["current_up"][0]).real),
                               "current_scalar_source_norm": float(np.linalg.norm(d["scalar_source"])),
                               "normal_electric_field": "f_tz=s g^2 rho(z-t); nonzero central trace supplies Gauss flux",
                               "infinite_homogeneous_normal_direction_not_a_global_finite_energy_configuration": True},
        "remaining_obligations": ["native gauge algebra/current generator, phase and real action fixed together",
                                  "massive/nonzero triadic resonance, actual M/C7 carrier and physical scales",
                                  "global spinor patching, boundary/finite-energy charge data and full sourced constraints",
                                  "metric/axis dynamics, stress backreaction and quantum current interpretation"],
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
