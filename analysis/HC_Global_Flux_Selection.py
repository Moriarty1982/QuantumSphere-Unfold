"""Global flux and constrained connection selection on an ASSUMED round S2."""
import argparse
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import Legendre, leggauss

import importlib.util


SPEC = importlib.util.spec_from_file_location(
    "global_hard_transport", Path(__file__).with_name("HC_Hard_Closure_Transport.py"))
transport = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(transport)
checks, PAULI = transport.checks, transport.PAULI


def _scale(radius, coupling):
    r, g = checks._scalar(radius, "sphere radius"), checks._scalar(coupling, "coupling")
    if r <= 0 or g <= 0:
        raise ValueError("Positive finite radius and curvature coupling required")
    return r, g


def sphere_data(theta=0.9, phi=0.4, shape=0.0, amplitude=0.0, mode=1, alpha=1.0):
    """Auxiliary surface occupies slots 1,2 for the existing curvature helpers."""
    theta, phi, shape, amplitude, alpha = [checks._scalar(x, label) for x, label in
                                        ((theta, "polar angle"), (phi, "azimuth"), (shape, "shape"),
                                         (amplitude, "block amplitude"), (alpha, "connection scaling"))]
    if not 0 < theta < np.pi or abs(shape) >= 0.5:
        raise ValueError("Interior polar angle and |shape|<1/2 required")
    if isinstance(mode, bool) or not isinstance(mode, int) or mode < 1:
        raise ValueError("Positive integer Legendre mode required")
    s, x = np.sin(theta), np.cos(theta)
    u, ux, uxx = x+shape*(1-x*x), 1-2*shape*x, -2*shape
    ut, utt = -s*ux, -x*ux+s*s*uxx
    radial = np.sqrt(1-u*u)
    rt = -u*ut/radial
    rtt = -(ut*ut+u*utt)/radial-u*u*ut*ut/radial**3
    c, ss = np.cos(phi), np.sin(phi)
    n = np.array([radial*c, radial*ss, u])
    dn, ddn = np.zeros((4, 3)), np.zeros((4, 4, 3))
    dn[1], dn[2] = [rt*c, rt*ss, ut], [-radial*ss, radial*c, 0]
    ddn[1, 1] = [rtt*c, rtt*ss, utt]
    ddn[1, 2] = ddn[2, 1] = [-rt*ss, rt*c, 0]
    ddn[2, 2] = [-radial*c, -radial*ss, 0]
    p = (np.eye(2)+np.einsum("a,aij->ij", n, PAULI))/2
    dp, ddp = np.einsum("ma,aij->mij", dn, PAULI)/2, np.einsum("mna,aij->mnij", ddn, PAULI)/2
    geometric = transport.commutator(p, dp)
    derivative = np.array([[transport.commutator(dp[nu], dp[mu])+transport.commutator(p, ddp[nu, mu])
                            for mu in range(4)] for nu in range(4)])
    polynomial = Legendre.basis(mode)
    c_phi = -amplitude*s*s*polynomial.deriv()(x)
    dc_theta_phi = amplitude*s*((1-x*x)*polynomial.deriv(2)(x)-2*x*polynomial.deriv()(x))
    k = 2*p-np.eye(2)
    b = alpha*geometric.copy()
    db = alpha*derivative.copy()
    b[2] += 1j*c_phi*k
    db[:, 2] += 2j*c_phi*dp
    db[1, 2] += 1j*dc_theta_phi*k
    f = checks.connection_curvature(b, db)
    dp_covariant = dp+transport.commutator(b, p)
    compressed = transport.compressed_curvature(p, dp, b, f)
    return {"P": p, "P_first": dp, "P_second": ddp, "connection": b,
            "connection_first": db, "curvature": f, "covariant_P_first": dp_covariant,
            "compressed_curvature": compressed, "c_phi": float(c_phi),
            "dc_theta_phi": float(dc_theta_phi), "sin_theta": s,
            "u": float(u), "u_theta": float(ut)}


def patch_data(theta, phi, patch="north", shape=0.0, amplitude=0.0, mode=1):
    d = sphere_data(theta, phi, shape, amplitude, mode)
    c, h = np.sqrt((1+d["u"])/2), np.sqrt((1-d["u"])/2)
    if patch == "north":
        frame = np.array([c, np.exp(1j*phi)*h])
        a_phi = 1j*((1-d["u"])/2+d["c_phi"])
    elif patch == "south":
        frame = np.array([np.exp(-1j*phi)*c, h])
        a_phi = 1j*(-(1+d["u"])/2+d["c_phi"])
    else:
        raise ValueError("Patch must be north or south")
    return {"frame": frame, "a_phi": a_phi, "P": d["P"]}


def energy_bound(charge=1, radius=1.0, coupling=1.0):
    r, g = _scale(radius, coupling)
    if isinstance(charge, bool) or not isinstance(charge, int):
        raise ValueError("Integer oriented flux charge required")
    return np.pi*charge**2/(g*g*r*r)


def surface_integrals(shape=0.0, amplitude=0.0, mode=1, alpha=1.0,
                      radius=1.0, coupling=1.0, nodes=40):
    """Integrate the actual matrix curvature; rotational symmetry removes phi integral."""
    r, g = _scale(radius, coupling)
    if isinstance(nodes, bool) or not isinstance(nodes, int) or nodes < 8:
        raise ValueError("At least eight Gauss-Legendre nodes required")
    x, weights = leggauss(nodes)
    ambient_flux = bundle_flux = energy = compatibility = 0.0
    for xx, w in zip(x, weights):
        d = sphere_data(np.arccos(xx), 0.37, shape, amplitude, mode, alpha)
        p, f, s = d["P"], d["curvature"][1, 2], d["sin_theta"]
        ambient_flux += w*(-1j*np.trace(p @ f)/s).real
        bundle_flux += w*(-1j*np.trace(d["compressed_curvature"][1, 2])/s).real
        energy += w*np.vdot(f, f).real/(s*s)
        compatibility = max(compatibility, float(np.linalg.norm(d["covariant_P_first"])))
    return {"ambient_projected_flux": float(ambient_flux), "bundle_flux": float(bundle_flux),
            "energy": float(np.pi*energy/(g*g*r*r)), "unit_charge_bound": energy_bound(1, r, g),
            "max_covariant_P_derivative": compatibility, "radius": r, "coupling": g}


def yang_mills_check(shape=0.0, amplitude=0.0, theta=0.9, phi=0.4, radius=1.0, step=1e-5):
    r, _ = _scale(radius, 1)
    step = checks._scalar(step, "derivative step")
    if step <= 0:
        raise ValueError("Positive derivative step required")
    data = sphere_data(theta, phi, shape, amplitude)
    star = -1j*data["curvature"][1, 2]/(r*r*np.sin(theta))
    result = []
    for mu in (1, 2):
        plus_angles, minus_angles = [theta, phi], [theta, phi]
        plus_angles[mu-1] += step
        minus_angles[mu-1] -= step
        plus, minus = sphere_data(*plus_angles, shape, amplitude), sphere_data(*minus_angles, shape, amplitude)
        plus_star = -1j*plus["curvature"][1, 2]/(r*r*np.sin(plus_angles[0]))
        minus_star = -1j*minus["curvature"][1, 2]/(r*r*np.sin(minus_angles[0]))
        result.append((plus_star-minus_star)/(2*step)+transport.commutator(data["connection"][mu], star))
    return np.asarray(result)


def hodge_rayleigh(mode, radius=1.0, nodes=40):
    r, _ = _scale(radius, 1)
    if isinstance(mode, bool) or not isinstance(mode, int) or mode < 1:
        raise ValueError("Positive integer coexact mode required")
    if isinstance(nodes, bool) or not isinstance(nodes, int) or nodes < mode+2:
        raise ValueError("Enough quadrature nodes for the polynomial mode required")
    x, weights = leggauss(nodes)
    p = Legendre.basis(mode)
    laplacian = ((1-x*x)*p.deriv(2)(x)-2*x*p.deriv()(x))/(r*r)
    one_form_norm = 2*np.pi*np.dot(weights, (1-x*x)*p.deriv()(x)**2)
    derivative_norm = 2*np.pi*r*r*np.dot(weights, laplacian**2)
    return {"mode": mode, "one_form_norm_squared": float(one_form_norm),
            "derivative_norm_squared": float(derivative_norm),
            "Rayleigh": float(derivative_norm/one_form_norm), "expected": mode*(mode+1)/(r*r)}


def evaluate():
    shape = 0.3
    before, selected = surface_integrals(shape), surface_integrals(shape, -shape/2)
    soft = [surface_integrals(alpha=a) for a in (0, 0.9, 1, 1.1, 2)]
    return {
        "status": "conditional global S2 bundle/positive-curvature-functional selection, NOT a derived native topological sector, stable unconstrained vacuum or spacetime metric",
        "assumptions": ["closed oriented round S2 with given radius R; not identified with physical spacetime",
                        "smooth rank-one projector in a trivial C2 bundle, chosen oriented flux number +1",
                        "hard D P=0, unitary traceless connection, fixed P/topological class",
                        "positive functional E=(1/(2g^2)) integral Tr(F^dagger wedge *F), g and R inputs",
                        "native C7/HC spectral-admissibility and integration measure not supplied"],
        "global_flux": {"definition": "q=(1/(2 pi i)) integral Tr(P F) for compatible connections; oriented sign fixed here",
                        "north_connection": "a_N=i(1-u)dphi/2+i c",
                        "south_connection": "a_S=-i(1+u)dphi/2+i c",
                        "transition": "V_S=exp(-i phi) V_N; a_S=a_N-i dphi",
                        "flat_compatible_connection_impossible_for_q_nonzero": True,
                        "ambient_rank_two_bundle_itself_is_trivial": True},
        "constrained_selection": {"general_form": "B=[P,dP]+i c (2P-I), c a globally smooth real one-form",
                                  "bound": "E >= (2 pi q)^2/(g^2 Area)=pi q^2/(g^2 R^2)",
                                  "minimizer": "f=(2 pi q/Area) dArea; curvature unique, connection unique modulo gauge on S2",
                                  "identity_projector_integrals": surface_integrals(),
                                  "nonuniform_projector": "u=x+epsilon(1-x^2), x=cos(theta), epsilon=0.3",
                                  "selected_block": "c_phi=epsilon sin(theta)^2/2, equivalently Legendre stream amplitude -epsilon/2",
                                  "unselected": before, "selected": selected,
                                  "unselected_D_star_F_norm": float(np.linalg.norm(yang_mills_check(shape))),
                                  "selected_D_star_F_norm": float(np.linalg.norm(yang_mills_check(shape, -shape/2)))},
        "constrained_Hessian": {"gauge": "c=d chi+*d psi; remove exact gauge part; constant psi gives no one-form",
                                "Rayleigh_modes": [hodge_rayleigh(l) for l in (1, 2, 3, 4)],
                                "energy_Hessian": "2 l(l+1)/(g^2 R^2) for L2-normalized coexact one-forms",
                                "not_a_four_dimensional_mass_or_particle_spectrum": True},
        "relaxed_compatibility_negative_control": {
            "path": "B_alpha=alpha [P,dP], P fixed; D_alpha P=(1-alpha) dP",
            "curvature": "F_alpha=(2 alpha-alpha^2) F_1",
            "energy": "E_alpha=(2 alpha-alpha^2)^2 E_1",
            "second_derivative_at_alpha_1": float(-4*np.pi),
            "samples": [{"alpha": alpha, **data} for alpha, data in zip((0, 0.9, 1, 1.1, 2), soft)],
            "global_flat_incompatible_connections_do_not_violate_the_bundle_flux_theorem": True,
            "compressed_curvature_keeps_q_1_while_P_F_P_alone_does_not": True,
            "not_an_unconstrained_Yang_Mills_minimum": True},
        "native_source_audit": {"path": "sources/research/parts/v470/10_sphaera_and_physics.tex", "label": "thm:hopf",
                                "anchor": "the standard S1 -> S3 -> S2 fibration is present",
                                "gap": "no evaluation identifies native P_C7 with this degree-one rank-one projector or derives R,g and a hard integration domain"},
        "remaining_obligations": ["native projector bundle, its actual topological class and admissibility",
                                  "derive whether D P=0 is an operator/measure constraint or only a particular-probe condition",
                                  "native real action and stability against all allowed modes, not only block variations",
                                  "metric/scale origin, common probe backreaction and quantum determinant/vacuum matching"],
        "main_TeX_changed": False,
        "sources": ["https://www.math.utoronto.ca/mgualt/Morse%20Theory/Atiyah-Bott.pdf",
                    "https://authors.library.caltech.edu/records/2pepc-k9f58"]}


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
