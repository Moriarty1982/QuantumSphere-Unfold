"""Local massive charged Dirac/gauge/soft-HC comparison, not native hard closure."""
import argparse
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import mpmath as mp
import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "massive_sourced_closure", Path(__file__).with_name("HC_Sourced_Closure_Current.py"))
source = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(source)
checks, commutator, dirac = source.checks, source.commutator, source.dirac
DEFAULT_PARAMETERS = (0.6, 0.9, 0.8, 0.7, 0.4, 0.3)
DEFAULT_INITIAL = (0.5, 0.1, 0.0, 0.03, 0.2, 0.0)
HARD_INITIAL = (0.5, 0.1, 0.0, 0.03, 0.0, 0.0)
STATE_NAMES = ("u", "v", "a", "a_first", "h", "h_first")


def parameters(value=DEFAULT_PARAMETERS):
    p = checks._real(value, (6,), "m,omega,g,kappa,gamma,lambda")
    if p[0] <= 0 or p[2] <= 0 or p[3] == 0 or p[5] < 0:
        raise ValueError("Positive comparison mass/g, nonzero kappa and nonnegative matching coefficient required")
    return tuple(float(x) for x in p)


def rhs(state, params=DEFAULT_PARAMETERS, domain="soft"):
    if domain not in ("soft", "hard"):
        raise ValueError("Declared hard or soft HC domain required")
    m, omega, gauge, kappa, gamma, penalty = params
    u, v, a, electric, h, hc_first = state
    effective, frequency = m+gamma*h, omega-a
    return [(frequency+effective)*v, (effective-frequency)*u,
            electric, -gauge*gauge*(u*u+v*v), hc_first if domain == "soft" else 0,
            -gauge*gauge*(2*penalty*h+gamma*(u*u-v*v))/(kappa*kappa) if domain == "soft" else 0]


def jacobian(state, params=DEFAULT_PARAMETERS):
    m, omega, gauge, kappa, gamma, penalty = parameters(params)
    u, v, a, electric, h, hc_first = checks._real(state, (6,), "state")
    result = np.zeros((6, 6))
    result[0, 1], result[0, 2], result[0, 4] = omega-a+m+gamma*h, -v, gamma*v
    result[1, 0], result[1, 2], result[1, 4] = m+gamma*h-omega+a, u, gamma*u
    result[2, 3] = result[4, 5] = 1
    result[3, 0], result[3, 1] = -2*gauge*gauge*u, -2*gauge*gauge*v
    result[5, 0], result[5, 1], result[5, 4] = (-2*gauge*gauge*gamma*u/(kappa*kappa),
                                               2*gauge*gauge*gamma*v/(kappa*kappa),
                                               -2*gauge*gauge*penalty/(kappa*kappa))
    return result


@lru_cache(maxsize=24)
def coefficients(order=32, params=DEFAULT_PARAMETERS, initial=DEFAULT_INITIAL, domain="soft"):
    params = parameters(params)
    initial = tuple(float(x) for x in checks._real(initial, (6,), "initial state"))
    if isinstance(order, bool) or not isinstance(order, int) or not 2 <= order <= 80:
        raise ValueError("Taylor order between 2 and 80 required")
    if domain not in ("soft", "hard") or (domain == "hard" and initial[4:] != (0.0, 0.0)):
        raise ValueError("Declared domain and exactly zero hard-HC initial data required")
    with mp.workdps(60):
        m, omega, gauge, kappa, gamma, penalty = [mp.mpf(str(x)) for x in params]
        c = [[mp.mpf(str(x))]+[mp.mpf(0)]*order for x in initial]

        def product(a, b, n):
            return sum(c[a][j]*c[b][n-j] for j in range(n+1))

        for n in range(order):
            terms = [(omega+m)*c[1][n]-product(2, 1, n)+gamma*product(4, 1, n),
                     (m-omega)*c[0][n]+product(2, 0, n)+gamma*product(4, 0, n),
                     c[3][n], -gauge*gauge*(product(0, 0, n)+product(1, 1, n)),
                     c[5][n], -gauge*gauge*(2*penalty*c[4][n]
                                           +gamma*(product(0, 0, n)-product(1, 1, n)))/(kappa*kappa)]
            if domain == "hard":
                terms[4:] = [mp.mpf(0), mp.mpf(0)]
            for row, term in zip(c, terms):
                row[n+1] = term/(n+1)
        return tuple(tuple(row) for row in c)


def series_jet(z=0.15, order=32, params=DEFAULT_PARAMETERS, initial=DEFAULT_INITIAL, high_precision=False, domain="soft"):
    z = checks._scalar(z, "normal position")
    if abs(z) > 0.2:
        raise ValueError("This comparison evaluates only |z|<=0.2; no global extension is asserted")
    c = coefficients(order, tuple(params), tuple(initial), domain)
    with mp.workdps(60):
        point = mp.mpf(str(z))
        value, first, second = [], [], []
        for row in c:
            value.append(mp.polyval(list(reversed(row)), point))
            first.append(mp.polyval(list(reversed([n*row[n] for n in range(1, len(row))])), point))
            second.append(mp.polyval(list(reversed([n*(n-1)*row[n] for n in range(2, len(row))])), point))
        if high_precision:
            return value, first, second
        return tuple(np.array([float(x) for x in values]) for values in (value, first, second))


def series_defect(z=0.15, order=32, params=DEFAULT_PARAMETERS, initial=DEFAULT_INITIAL, domain="soft"):
    p = parameters(params)
    with mp.workdps(60):
        value, first, _ = series_jet(z, order, p, initial, high_precision=True, domain=domain)
        target = rhs(value, tuple(mp.mpf(str(x)) for x in p), domain)
        return float(max(abs(a-b) for a, b in zip(first, target)))


def spatial_integral(state, params=DEFAULT_PARAMETERS):
    m, omega, gauge, kappa, gamma, penalty = params
    u, v, a, electric, h, hc_first = state
    return (-(omega-a)*(u*u+v*v)+(m+gamma*h)*(u*u-v*v)
            +(electric*electric+kappa*kappa*hc_first*hc_first)/(2*gauge*gauge)+penalty*h*h)


def existence_box():
    """Explicit bounds for the fixed DEFAULT example, not arbitrary input parameters."""
    lower, upper = np.array(DEFAULT_INITIAL)-0.1, np.array(DEFAULT_INITIAL)+0.1
    m, omega, gauge, kappa, gamma, penalty = DEFAULT_PARAMETERS
    umax, vmax, emax, hmax, rmax = upper[0], upper[1], upper[3], upper[4], upper[5]
    uv_coefficient = omega-lower[2]+m+gamma*hmax
    vu_coefficient = max(abs(m+gamma*lower[4]-omega+lower[2]),
                         abs(m+gamma*upper[4]-omega+upper[2]))
    bounds = np.array([uv_coefficient*vmax, vu_coefficient*umax, emax,
                       gauge*gauge*(umax*umax+vmax*vmax), rmax,
                       gauge*gauge*(2*penalty*hmax+abs(gamma)*(umax*umax+vmax*vmax))/(kappa*kappa)])
    lip = 2.01
    interval = 0.2
    return {"lower": lower.tolist(), "upper": upper.tolist(), "rhs_abs_bounds": bounds.tolist(),
            "interval": interval, "max_displacement_bound": float(interval*max(bounds)),
            "available_box_radius": 0.1, "Jacobian_infinity_norm_bound": lip,
            "Picard_contraction_bound": interval*lip,
            "h_lower_bound": float(lower[4]), "scalar_source_lower_bound": float(lower[0]**2-upper[1]**2)}


def hard_existence_box():
    initial = np.array(HARD_INITIAL[:4])
    bounds = np.array([0.32, 0.24, 0.13, 0.256])
    return {"lower": (initial-0.1).tolist(), "upper": (initial+0.1).tolist(),
            "rhs_abs_bounds": bounds.tolist(), "interval": 0.2,
            "max_displacement_bound": float(0.2*max(bounds)), "available_box_radius": 0.1,
            "Jacobian_infinity_norm_bound": 1.81, "Picard_contraction_bound": 0.362}


def field_data(point=(0.4, 0.9, 0.4, 0.15), params=DEFAULT_PARAMETERS,
               initial=None, radius=1.0, eta=0.7, order=32, domain="soft"):
    p = parameters(params)
    point = checks._real(point, (4,), "product coordinates")
    radius, _ = source.load.flux._scale(radius, 1)
    eta = checks._scalar(eta, "closure coupling")
    t, theta, phi, z = point
    initial = (HARD_INITIAL if domain == "hard" else DEFAULT_INITIAL) if initial is None else initial
    state, first, second = series_jet(z, order, p, initial, domain=domain)
    u, v, a, electric, h, hc_first = state
    m, omega, gauge, kappa, gamma, penalty = p
    base = source.load.flux.sphere_data(theta, phi)
    projector, dp = base["P"], base["P_first"]
    unitary = base["connection"].copy()
    unitary[0] += 1j*a*projector
    derivative = base["connection_first"].copy()
    derivative[:, 0] += 1j*a*dp
    derivative[3, 0] += 1j*first[2]*projector
    hc = h*projector
    dh = h*dp
    dh[3] += first[4]*projector
    axis = source.dynamics.AXIS
    load = kappa*hc+eta*(np.eye(2)-projector)
    dload = kappa*dh-eta*dp
    connection = unitary+axis[:, None, None]*load
    dconnection = derivative+dload[:, None]*axis[None, :, None, None]
    g = checks.connection_curvature(unitary, derivative)
    f = checks.connection_curvature(connection, dconnection)
    vector = np.array([np.cos(theta/2), np.exp(1j*phi)*np.sin(theta/2)])
    dv = np.zeros((4, 2), complex)
    dv[1], dv[2] = [-np.sin(theta/2)/2, np.exp(1j*phi)*np.cos(theta/2)/2], [0, 1j*vector[1]]
    phase = np.exp(-1j*(omega*t+phi/2))
    chi = phase*np.array([0, u, 0, 1j*v])
    dchi = np.zeros((4, 4), complex)
    dchi[0], dchi[2] = -1j*omega*chi, -0.5j*chi
    dchi[3] = phase*np.array([0, first[0], 0, 1j*first[1]])
    psi = vector[:, None]*chi
    dpsi = dv[:, :, None]*chi+vector[None, :, None]*dchi[:, None]
    bundle = source.product_spin_bundle(theta, radius)
    currents = source.probe.probe_currents(psi, dirac.BETA @ bundle["gamma"], dirac.BETA)
    lowered = np.einsum("mn,nij->mij", bundle["metric"], currents["gauge"])
    return {"P": projector, "P_first": dp, "state": state, "state_first": first, "state_second": second,
            "unitary": unitary, "unitary_first": derivative, "connection": connection,
            "connection_first": dconnection, "G": g, "F": f, "X": f-g,
            "H": hc, "H_first": dh, "psi": psi, "psi_first": dpsi, "bundle": bundle,
            "current_up": currents["gauge"], "current_lower": lowered, "scalar_source": currents["scalar"],
            "mass_operator": m*np.eye(2)+gamma*hc, "params": p, "point": point, "radius": radius,
            "domain": domain}


def probe_residual(data, ordered=False):
    b = data["connection"] if ordered else data["unitary"]
    return dirac.dirac_data(data["psi"], data["psi_first"]+b @ data["psi"], data["mass_operator"],
                            gamma=data["bundle"]["gamma"], metric=data["bundle"]["metric"],
                            spin=data["bundle"]["spin"])["residual"]


def field_residuals(point=(0.4, 0.9, 0.4, 0.15), step=1e-5, **kwargs):
    step = checks._scalar(step, "derivative step")
    if step <= 0:
        raise ValueError("Positive derivative step required")
    d = field_data(point, **kwargs)
    inverse = source.load.inverse_metric(d["point"][1], d["radius"])
    result = {}
    for name, connection in (("G", "unitary"), ("X", "unitary"), ("F", "connection")):
        raised = inverse[:, None, None, None]*inverse[None, :, None, None]*d[name]
        result[name] = np.sum(commutator(d[connection][:, None], raised), axis=0)
    for mu, direction in enumerate(np.eye(4)):
        samples = []
        for sign in (1, -1):
            other = field_data(d["point"]+sign*step*direction, **kwargs)
            inv = source.load.inverse_metric(other["point"][1], d["radius"])
            density = d["radius"]**2*np.sin(other["point"][1])
            samples.append({name: density*inv[mu]*inv[:, None, None]*other[name][mu] for name in result})
        for name in result:
            result[name] += (samples[0][name]-samples[1][name])/(2*step*d["radius"]**2*np.sin(d["point"][1]))
    result = {name: value/inverse[:, None, None] for name, value in result.items()}
    m, omega, gauge, kappa, gamma, penalty = d["params"]
    n = source.dynamics.AXIS
    phi = kappa*d["H"]+kwargs.get("eta", 0.7)*(np.eye(2)-d["P"])
    x_up = inverse[:, None, None, None]*inverse[None, :, None, None]*d["X"]
    force = np.einsum("m,mnij->nij", n, commutator(phi, x_up))/inverse[:, None, None]
    hc_curvature = kappa*np.einsum("m,mij->ij", inverse*n, result["X"])/(gauge*gauge)
    hc_el = hc_curvature-2*penalty*d["H"]-gamma*d["scalar_source"]
    projector_force = -kwargs.get("eta", 0.7)*np.einsum("m,mij->ij", inverse*n, result["X"])/(gauge*gauge)
    projector = d["P"]
    complement = np.eye(2)-projector
    return {"gauge": result["G"]-force-1j*gauge*gauge*d["current_lower"],
            "HC": hc_el, "HC_curvature": hc_curvature,
            "projector_tangent": projector @ projector_force @ complement+complement @ projector_force @ projector,
            "projector_normal_reaction": projector_force,
            "printed_complex_extra": result["F"]-1j*gauge*gauge*d["current_lower"],
            "gauge_HC_commutator_force": force}


def evaluate():
    d = field_data()
    residual = field_residuals()
    state = d["state"]
    hard = field_data(domain="hard")
    hard_residual = field_residuals(domain="hard")
    m, omega, gauge, kappa, gamma, penalty = d["params"]
    points = [-0.2, -0.1, 0, 0.1, 0.2]
    samples = []
    for z in points:
        y, _, _ = series_jet(z)
        samples.append({"z": z, "state": dict(zip(STATE_NAMES, y.tolist())),
                        "rho": float(y[0]**2+y[1]**2), "scalar": float(y[0]**2-y[1]**2),
                        "spatial_first_integral": float(spatial_integral(y)), "series_ODE_defect": series_defect(z)})
    return {
        "status": "local massive charged Dirac/gauge/INDEPENDENT SOFT HC comparison with a certified reference existence box; NOT native hard H=Lambda, physical mass selection, metric or global finite-energy solution",
        "assumptions": ["same prescribed R1,1 x round S2 and unit-flux projector, ordinary spin adjoint, U(2) carrier",
                        "real symmetric probe plus dagger bosonic action, internal/spin curvature kept distinct",
                        "H_C is an independent Hermitian field with finite lambda ||H_C-Lambda||^2; Lambda=0 for scalar M",
                        "bare comparison mass m=0.6 and Yukawa coefficient gamma=0.4 are declared inputs, not native eigenvalues/scales",
                        "stationary zero longitudinal current, local polar patch, fixed metric and axis; no global energy or stability claim"],
        "reduced_equations": {"ansatz": "Psi=V_N exp(-i omega t-i phi/2)(0,u,0,i v), A_t=a(z)P, H=h(z)P",
                              "spinor": "u'=(omega-a+m+gamma h)v; v'=(m+gamma h-omega+a)u",
                              "gauge": "a''=-g^2(u^2+v^2)",
                              "HC": "h''=-(g^2/kappa^2)[2 lambda h+gamma(u^2-v^2)]",
                              "scalar_source": "S=(u^2-v^2)P, j^t=(u^2+v^2)P, j^z=0",
                              "density": "L=(omega-a)rho+u v'-v u'-(m+gamma h)sigma+(a'^2+kappa^2 h'^2)/(2g^2)-lambda h^2, up to sphere constant/factor",
                              "spatial_first_integral": "I=-(omega-a)rho+(m+gamma h)sigma+(a'^2+kappa^2 h'^2)/(2g^2)+lambda h^2; not a temporal energy"},
        "reference_parameters": dict(zip(("m", "omega", "g", "kappa", "gamma", "lambda"), DEFAULT_PARAMETERS)),
        "reference_initial": dict(zip(STATE_NAMES, DEFAULT_INITIAL)),
        "existence_certificate": existence_box(),
        "sample_profiles": samples,
        "full_matrix_checks": {"point": d["point"].tolist(),
                               "real_massive_Dirac_residual_norm": float(np.linalg.norm(probe_residual(d))),
                               "gauge_residual_norm": float(np.linalg.norm(residual["gauge"])),
                               "independent_HC_residual_norm": float(np.linalg.norm(residual["HC"])),
                               "projector_tangent_residual_norm": float(np.linalg.norm(residual["projector_tangent"])),
                               "projector_normal_reaction_norm": float(np.linalg.norm(residual["projector_normal_reaction"])),
                               "ordered_probe_residual_norm": float(np.linalg.norm(probe_residual(d, ordered=True))),
                               "complex_connection_extra_residual_norm": float(np.linalg.norm(residual["printed_complex_extra"])),
                               "HC_source_norm": float(np.linalg.norm(gamma*d["scalar_source"])),
                               "hard_H_equals_Lambda_mismatch_norm": float(np.linalg.norm(d["H"])),
                               "rho": float(state[0]**2+state[1]**2), "scalar": float(state[0]**2-state[1]**2),
                               "HC_eigenvalues": np.linalg.eigvalsh(d["H"]).tolist()},
        "hard_branch_boundary": {"at_H_0_independent_HC_equation_requires_gamma_S_0": True,
                                 "restricted_stationary_no_go": "IF the independent soft-HC equation is retained AND H=0 is additionally imposed with gamma nonzero, u^2=v^2; Dirac then gives a=omega and Gauss forces u=v=0",
                                 "not_a_no_go_for_all_massive_native_probes_or_nonstationary_currents": True,
                                 "gamma_0_is_a_changed_coupling_control_not_an_adopted_native_repair": True},
        "hard_dependent_comparison": {"domain": "H=Lambda=0 substituted before variation; no independent H equation",
                                      "existence_certificate": hard_existence_box(),
                                      "gamma_is_not_set_to_zero": hard["params"][4],
                                      "massive_Dirac_residual_norm": float(np.linalg.norm(probe_residual(hard))),
                                      "gauge_residual_norm": float(np.linalg.norm(hard_residual["gauge"])),
                                      "independent_soft_HC_residual_if_inappropriately_imposed": float(np.linalg.norm(hard_residual["HC"])),
                                      "formal_equality_multiplier": "Z=gamma S for +Tr[Z(H-Lambda)]; reacts to the excluded independent-H direction",
                                      "HC_residual_plus_multiplier_norm": float(np.linalg.norm(hard_residual["HC"]+hard["params"][4]*hard["scalar_source"])),
                                      "minimal_Lambda_first_variation_at_scalar_M_is_zero": True,
                                      "not_a_derivation_of_the_native_HC_domain_or_gauge_current_dictionary": True},
        "remaining_obligations": ["choose native hard/soft HC domain and its consistent real action/adjoint",
                                  "derive actual mass/triadic/gauge carrier and all coefficients instead of these inputs",
                                  "global spin/charge boundary data, causal/dynamical stability and metric/axis backreaction",
                                  "if retaining ordered HC transport or printed complex connection equation, solve their additional nonzero residuals"],
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
