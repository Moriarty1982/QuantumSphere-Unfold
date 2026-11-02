"""Separate probe channels from gauge indices and test a coherent sourced branch.

This is a declared hard-dependent comparison, not an identification of native C7.
"""
import argparse
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import mpmath as mp
import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "factorized_triadic_gate", Path(__file__).with_name("HC_Triadic_Gauss_Compatibility.py"))
gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gate)
source, checks, dirac = gate.source, gate.checks, gate.dirac
commutator, TRIAD = gate.commutator, gate.TRIAD
INITIAL = (0.5, 0, 0, 0.1, 0, 0, 0, 0.03)
OMEGA, GAUGE, MULTIPLICITY = 0.9, 0.8, 3


def partial_trace_channels(matrix):
    matrix = checks._finite(matrix, "gauge-by-channel matrix")
    if matrix.shape[-2:] != (6, 6):
        raise ValueError("A C2 gauge tensor C3 channel matrix required")
    return np.einsum("...aibi->...ab", matrix.reshape(*matrix.shape[:-2], 2, 3, 2, 3))


def gauge_projection(matrix):
    reduced = partial_trace_channels(matrix)/MULTIPLICITY
    return np.einsum("...ab,ij->...aibj", reduced, np.eye(3)).reshape(*reduced.shape[:-2], 6, 6)


def charge_intertwiner(charges):
    charges = checks._real(charges, (3,), "probe-channel charges")
    return commutator(np.diag(charges), TRIAD)


def _rhs(state, mass, omega, gauge, multiplicity):
    u, v, a, electric = state[:3], state[3:6], state[6], state[7]
    du = [(omega-a)*v[i]+sum(mass[i][j]*v[j] for j in range(3)) for i in range(3)]
    dv = [sum(mass[i][j]*u[j] for j in range(3))-(omega-a)*u[i] for i in range(3)]
    return du+dv+[electric, -gauge*gauge*sum(x*x for x in (*u, *v))/multiplicity]


def rhs(state, mass=TRIAD, omega=OMEGA, gauge=GAUGE, multiplicity=MULTIPLICITY):
    state = checks._real(state, (8,), "three u, three v, potential and electric field")
    mass = gate.real_mass(mass)
    omega, gauge = checks._scalar(omega, "frequency"), checks._scalar(gauge, "full-carrier gauge coupling")
    if (isinstance(multiplicity, bool) or not isinstance(multiplicity, int)
            or multiplicity <= 0 or gauge <= 0):
        raise ValueError("Positive gauge coupling and integer trace multiplicity required")
    return np.array(_rhs(state, mass, omega, gauge, multiplicity))


def jacobian(state):
    y = checks._real(state, (8,), "reference state")
    result = np.zeros((8, 8))
    result[:3, 3:6] = (OMEGA-y[6])*np.eye(3)+TRIAD
    result[3:6, :3] = TRIAD-(OMEGA-y[6])*np.eye(3)
    result[:3, 6], result[3:6, 6] = -y[3:6], y[:3]
    result[6, 7] = 1
    result[7, :6] = -2*GAUGE*GAUGE*y[:6]/MULTIPLICITY
    return result


@lru_cache(maxsize=8)
def coefficients(order=32):
    if isinstance(order, bool) or not isinstance(order, int) or not 2 <= order <= 80:
        raise ValueError("Taylor order between 2 and 80 required")
    with mp.workdps(60):
        mass = [[mp.mpf(str(x)) for x in row] for row in TRIAD]
        omega, gauge = mp.mpf(str(OMEGA)), mp.mpf(str(GAUGE))
        c = [[mp.mpf(str(x))]+[mp.mpf(0)]*order for x in INITIAL]

        def product(i, j, n):
            return sum(c[i][k]*c[j][n-k] for k in range(n+1))

        for n in range(order):
            du = [omega*c[i+3][n]-product(6, i+3, n)
                  +sum(mass[i][j]*c[j+3][n] for j in range(3)) for i in range(3)]
            dv = [sum(mass[i][j]*c[j][n] for j in range(3))
                  -omega*c[i][n]+product(6, i, n) for i in range(3)]
            terms = du+dv+[c[7][n], -gauge*gauge*sum(product(i, i, n) for i in range(6))/MULTIPLICITY]
            for row, value in zip(c, terms):
                row[n+1] = value/(n+1)
        return tuple(tuple(row) for row in c)


def series_jet(z=0.02, order=32, high_precision=False):
    z = checks._scalar(z, "local normal coordinate")
    if abs(z) > 0.03:
        raise ValueError("Only the proved |z|<=.03 local reference interval is evaluated")
    with mp.workdps(60):
        z = mp.mpf(str(z))
        jets = [[], [], []]
        for row in coefficients(order):
            polynomials = [row, [i*row[i] for i in range(1, len(row))],
                           [i*(i-1)*row[i] for i in range(2, len(row))]]
            for values, polynomial in zip(jets, polynomials):
                values.append(mp.polyval(list(reversed(polynomial)), z))
        return jets if high_precision else tuple(np.array([float(x) for x in values]) for values in jets)


def series_defect(z=0.02, order=32):
    with mp.workdps(60):
        y, dy, _ = series_jet(z, order, high_precision=True)
        mass = [[mp.mpf(str(x)) for x in row] for row in TRIAD]
        target = _rhs(y, mass, mp.mpf(str(OMEGA)), mp.mpf(str(GAUGE)), MULTIPLICITY)
        return float(max(abs(a-b) for a, b in zip(dy, target)))


def spatial_integral(state):
    y = checks._real(state, (8,), "reference state")
    u, v, a, electric = y[:3], y[3:6], y[6], y[7]
    return float(-(OMEGA-a)*(u @ u+v @ v)+u @ TRIAD @ u-v @ TRIAD @ v
                 +MULTIPLICITY*electric*electric/(2*GAUGE*GAUGE))


def existence_box():
    initial = np.array(INITIAL)
    bounds = np.array([0.72, 0.23, 1.03, 0.64, 0.11, 2.51, 0.13, GAUGE*GAUGE*0.44/MULTIPLICITY])
    return {"lower": (initial-0.1).tolist(), "upper": (initial+0.1).tolist(),
            "rhs_abs_bounds": bounds.tolist(), "Jacobian_infinity_norm_bound": 6.4,
            "interval": 0.03, "available_box_radius": 0.1,
            "max_displacement_bound": 0.0753, "Picard_contraction_bound": 0.192}


def field_data(point=(0.4, 0.9, 0.4, 0.02), radius=1.0, eta=0.7):
    point = checks._real(point, (4,), "product coordinates")
    t, theta, phi, z = point
    y, dy, ddy = series_jet(z)
    radius, _ = source.load.flux._scale(radius, 1)
    eta = checks._scalar(eta, "closure coupling")
    base = source.load.flux.sphere_data(theta, phi)
    p0, dp0, a, electric = base["P"], base["P_first"], y[6], y[7]
    u0, du0 = base["connection"].copy(), base["connection_first"].copy()
    u0[0] += 1j*a*p0
    du0[:, 0] += 1j*a*dp0
    du0[3, 0] += 1j*electric*p0
    axis = source.dynamics.AXIS
    b0 = u0+eta*axis[:, None, None]*(np.eye(2)-p0)
    db0 = du0-eta*dp0[:, None]*axis[None, :, None, None]
    p = np.kron(p0, np.eye(3))
    unitary, connection = (np.array([np.kron(x, np.eye(3)) for x in value]) for value in (u0, b0))
    dconnection = np.array([[np.kron(x, np.eye(3)) for x in row] for row in db0])
    angular = np.array([np.cos(theta/2), np.exp(1j*phi)*np.sin(theta/2)])
    dangular = np.zeros((4, 2), complex)
    dangular[1] = [-np.sin(theta/2)/2, np.exp(1j*phi)*np.cos(theta/2)/2]
    dangular[2] = [0, 1j*angular[1]]
    phase = np.exp(-1j*(OMEGA*t+phi/2))
    chi = np.zeros((3, 4), complex)
    chi[:, 1], chi[:, 3] = phase*y[:3], 1j*phase*y[3:6]
    dchi = np.zeros((4, 3, 4), complex)
    dchi[0], dchi[2] = -1j*OMEGA*chi, -0.5j*chi
    dchi[3, :, 1], dchi[3, :, 3] = phase*dy[:3], 1j*phase*dy[3:6]
    psi = np.einsum("a,bs->abs", angular, chi).reshape(6, 4)
    dpsi = (np.einsum("ma,bs->mabs", dangular, chi)
            +np.einsum("a,mbs->mabs", angular, dchi)).reshape(4, 6, 4)
    bundle = source.product_spin_bundle(theta, radius)
    currents = source.probe.probe_currents(psi, dirac.BETA @ bundle["gamma"], dirac.BETA)
    return {"P": p, "P_first": np.array([np.kron(x, np.eye(3)) for x in dp0]),
            "connection": connection, "connection_first": dconnection, "unitary": unitary,
            "F": np.array([[np.kron(x, np.eye(3)) for x in row]
                           for row in checks.connection_curvature(b0, db0)]),
            "psi": psi, "psi_first": dpsi, "mass_operator": np.kron(np.eye(2), TRIAD),
            "current": currents["gauge"], "scalar": currents["scalar"], "bundle": bundle,
            "state": y, "state_first": dy, "state_second": ddy, "point": point, "radius": radius}


def residuals(point=(0.4, 0.9, 0.4, 0.02), step=1e-5, **kwargs):
    step = checks._scalar(step, "coordinate derivative step")
    if step <= 0:
        raise ValueError("Positive derivative step required")
    d = field_data(point, **kwargs)
    inverse = source.load.inverse_metric(d["point"][1], d["radius"])
    raised = inverse[:, None, None, None]*inverse[None, :, None, None]*d["F"]
    resonance = np.sum(commutator(d["connection"][:, None], raised), axis=0)
    divergence = np.sum(commutator(d["unitary"], d["current"]), axis=0)
    volume = d["radius"]**2*np.sin(d["point"][1])
    for mu, direction in enumerate(np.eye(4)):
        samples = []
        for sign in (1, -1):
            other = field_data(d["point"]+sign*step*direction, **kwargs)
            inv = source.load.inverse_metric(other["point"][1], d["radius"])
            density = d["radius"]**2*np.sin(other["point"][1])
            samples.append((density*inv[mu]*inv[:, None, None]*other["F"][mu],
                            density*other["current"][mu]))
        resonance += (samples[0][0]-samples[1][0])/(2*step*volume)
        divergence += (samples[0][1]-samples[1][1])/(2*step*volume)
    lower = np.einsum("mn,nij->mij", d["bundle"]["metric"], d["current"])
    full = resonance/inverse[:, None, None]-1j*GAUGE*GAUGE*lower
    probe = dirac.dirac_data(
        d["psi"], d["psi_first"]+d["connection"] @ d["psi"], d["mass_operator"],
        gamma=d["bundle"]["gamma"], metric=d["bundle"]["metric"], spin=d["bundle"]["spin"])["residual"]
    return {"Dirac": probe, "projected_gauge": gauge_projection(full),
            "projected_current_divergence": gauge_projection(divergence),
            "full_Ward": divergence+1j*commutator(d["mass_operator"], d["scalar"]),
            "unprojected_equation_not_imposed": full, "full_current_divergence": divergence}


def evaluate():
    d, r = field_data(), residuals()
    torque = commutator(d["mass_operator"], d["scalar"])
    y = d["state"]
    _, vectors = np.linalg.eigh(TRIAD)
    weights = (vectors.T @ y[:3])**2+(vectors.T @ y[3:6])**2
    samples = []
    for z in (-0.03, 0, 0.03):
        state, _, _ = series_jet(z)
        samples.append({"z": z, "state": state.tolist(), "ODE_defect": series_defect(z),
                        "spatial_first_integral": spatial_integral(state)})
    return {
        "status": "conditional coherent triadic probe channels with separate gauge factor; NOT native C7, gauge representation or mass/geometry identification",
        "native_source_audit": {
            "closed_triad": "10_sphaera_and_physics.tex, concrete route to the Einstein limit: entire Psi_triangle is called closed",
            "same_carrier": "12_structural_core.tex, thm:theorem-level-shadow-bidirectional-probe-lensing: ART/QFT/orthogonal channel share a closure-stable carrier",
            "color_is_distinct": "10_sphaera_and_physics.tex, sec:gauge: SU(3) acts on color indices",
            "channel_is_not_generation": "parts/native-operator-link.tex: triadic entries label probe channels, not generation coordinates",
            "limits": "these are architectural statements in the text, not evaluated embeddings or field-existence proofs"},
        "representation_gate": {
            "general": "T_i^a Omega_ij = Omega_ij T_j^a for fixed equivariant off-diagonal couplings",
            "projected_Ward": "D_mu j_a^mu=-i Tr([T_a,Omega] S); if all generators commute with Omega it vanishes for arbitrary coherent probe states",
            "same_charge_intertwiner_norm": float(np.linalg.norm(charge_intertwiner([1, 1, 1]))),
            "different_third_charge_intertwiner_norm": float(np.linalg.norm(charge_intertwiner([1, 1, 0]))),
            "same_representations_are_assumed_not_derived": True},
        "trace_normalization": {"channel_multiplicity": MULTIPLICITY, "full_carrier_coupling": GAUGE,
                                "effective_gauge_squared": GAUGE**2/MULTIPLICITY,
                                "action": "Tr_6(F^dagger F)=3 Tr_2(F_g^dagger F_g); keep the full trace and vary only B_g tensor I3",
                                "gauge_equation": "D G_g=i(g_full^2/3) Tr_channel(j); not the unprojected U(6) equation"},
        "local_solution": {"carrier": "C2 auxiliary gauge/Hopf factor tensor C3 probe-channel factor; P=P_Hopf tensor I3, H=0 eliminated before variation",
                           "mass": "I2 tensor prepared finite triad; it is not native M16",
                           "equations": "U'=[(omega-a)I+Omega]V; V'=[Omega-(omega-a)I]U; a''=-(g_full^2/3)(|U|^2+|V|^2)",
                           "initial": list(INITIAL), "existence_box": existence_box(), "samples": samples,
                           "point": d["point"].tolist(), "channel_densities": (y[:3]**2+y[3:6]**2).tolist(),
                           "mass_eigenmode_densities": weights.tolist(),
                           "full_matrix_torque_norm": float(np.linalg.norm(torque)),
                           "gauge_projected_torque_norm": float(np.linalg.norm(gauge_projection(torque))),
                           "residual_norms": {name: float(np.linalg.norm(value)) for name, value in r.items()}},
        "scope": ["the matrix Ward identity is unchanged; only the actually varied gauge algebra determines the source equation",
                  "no claim that all three native channels carry identical charges; unequal charges need intertwiners or additional charged fields",
                  "no identification of auxiliary U(2) with the full electroweak representation or of channels with colors/generations",
                  "hard/soft action choice, common C7 embedding, physical scales, bilinear metric, global energy and stability remain open"],
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
