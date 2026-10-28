"""Finite two-qubit controls for OP5_Readout_Interaction_Energy.md.

Comparison Hamiltonians, not native QAM energies or gravitating vacuum densities.
Run: python -B analysis/OP5_Readout_Interaction_Energy_Check.py
"""
import json
import math

import numpy as np

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
H = (I+Z)/2  # comparison omega=1; |0> excited, |1> ground
SWAP = np.array([[1, 0, 0, 0], [0, 0, 1, 0],
                 [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)


def ptr(rho, keep):
    r = rho.reshape(2, 2, 2, 2)
    return np.trace(r, axis1=1, axis2=3) if keep == 0 else np.trace(r, axis1=0, axis2=2)


def E(h, rho):
    return float(np.trace(h @ rho).real)


def rho_of(b):
    return (I+b[0]*X+b[1]*Y+b[2]*Z)/2


def check_close(a, b, tol=3e-13):
    assert np.max(np.abs(np.asarray(a)-np.asarray(b))) < tol, (a, b)


def main():
    energy0 = np.kron(H, I)+np.kron(I, H)
    check_close(SWAP @ energy0, energy0 @ SWAP)
    theta = math.pi/4
    u = math.cos(theta)*np.eye(4)-1j*math.sin(theta)*SWAP
    ground = np.diag([0, 1]).astype(complex)
    excited = np.diag([1, 0]).astype(complex)
    joint = np.kron(ground, excited)
    revival = []
    for n in range(5):
        es, em = E(H, ptr(joint, 0)), E(H, ptr(joint, 1))
        check_close(es, math.sin(n*theta)**2)
        check_close(es+em, 1)
        revival.append({"pulses": n, "system_energy": es, "meter_energy": em})
        joint = u @ joint @ u.conj().T

    # Fixed diagonal thermal-comparison bath: its state is stationary and
    # repeated fresh collisions converge in this finite example.
    bath = np.diag([0.2, 0.8]).astype(complex)
    state = rho_of([math.sqrt(3)/2, 0, 0.5])
    theta = math.pi/6
    u = math.cos(theta)*np.eye(4)-1j*math.sin(theta)*SWAP
    check_close(ptr(u @ np.kron(bath, bath) @ u.conj().T, 0), bath)
    accumulated_bath_energy = 0.
    initial_energy = E(H, state)
    for _ in range(160):
        before = E(H, state)+E(H, bath)
        out = u @ np.kron(state, bath) @ u.conj().T
        newstate, newbath = ptr(out, 0), ptr(out, 1)
        check_close(E(H, newstate)+E(H, newbath), before)
        accumulated_bath_energy += E(H, newbath)-E(H, bath)
        state = newstate
    check_close(state, bath, tol=1e-9)
    check_close(E(H, state)-initial_energy+accumulated_bath_energy, 0)

    # Refreshed opposite Bloch vector: exact r28-like radial map for one
    # collision, with the Hermitian energy checked independently.
    state0 = rho_of([math.sqrt(3)/2, 0, 0.5])
    opposite = rho_of([-math.sqrt(3)/2, 0, -0.5])
    out = u @ np.kron(state0, opposite) @ u.conj().T
    check_close(ptr(out, 0), rho_of(math.cos(2*theta)*np.array([math.sqrt(3)/2, 0, 0.5])))
    counterpart_balance = {"system_change": E(H, ptr(out, 0))-E(H, state0),
                           "meter_change": E(H, ptr(out, 1))-E(H, opposite)}
    check_close(sum(counterpart_balance.values()), 0)

    # Ideal non-selective readout as a joint premeasurement gate. Meter Hm=0.
    axis = (X+Z)/math.sqrt(2)
    plus, minus = (I+axis)/2, (I-axis)/2
    um = np.kron(plus, I)+np.kron(minus, X)
    pulse_K = math.pi/2*np.kron(minus, I-X)  # tau=1
    h0 = np.kron(H, I)
    v = pulse_K-h0
    check_close(um.conj().T @ um, np.eye(4))
    check_close(um @ um, np.eye(4))
    check_close(pulse_K @ um, um @ pulse_K)
    meter0 = np.diag([1, 0]).astype(complex)
    timed = []
    for phi in (0, math.pi/2, math.pi):
        b = np.array([math.sqrt(3)/2*math.cos(phi),
                      math.sqrt(3)/2*math.sin(phi), 0.5])
        r = rho_of(b)
        joint0 = np.kron(r, meter0)
        after = um @ joint0 @ um.conj().T
        rs = ptr(after, 0)
        expected = plus @ r @ plus + minus @ r @ minus
        check_close(rs, expected)
        de = E(H, rs)-E(H, r)
        formula = (math.sqrt(3)*math.cos(phi)-1)/8
        check_close(de, formula)
        won = E(v, joint0)
        woff = -E(v, after)
        check_close(won+woff, de)
        check_close(um @ after @ um.conj().T, joint0)
        # A fixed scalar shift changes absolute energies but not pulse work,
        # probabilities or energy transfers.
        shifted_H = H+2.3*I
        check_close(E(shifted_H, rs)-E(shifted_H, r), de)
        timed.append({"free_phase": phi, "system_energy_before": E(H, r),
                      "system_energy_after": E(H, rs), "system_change": de,
                      "meter_change": 0., "switch_on_work": won,
                      "switch_off_work": woff, "total_switch_work": won+woff})

    print(json.dumps({"comparison_energy_gap": 1,
                      "closed_meter_revival": revival,
                      "fixed_bath_after_160_energy": E(H, state),
                      "accumulated_bath_energy": accumulated_bath_energy,
                      "opposite_state_collision": counterpart_balance,
                      "timed_noncommuting_readout": timed,
                      "checks": "unitarity, reduced maps, per-collision energy conservation, switching first law, finite meter revival, bath fixed point, scalar-shift invariance",
                      "non_claims": ["No native QAM Hamiltonian identification", "No physical energy/time units", "No universal erasure-work value", "No gravitating vacuum density prediction"]}, indent=2))


if __name__ == "__main__":
    main()
