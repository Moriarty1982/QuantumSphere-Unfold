"""k310: Test H137 -- reversible band circuit (FiniteBand) on superpositions.

Run from the repository root:
    python notes/research/bandschaltung_ueberlagerung_2026_11_25/k310_test_h137.py
Pre-registration: notes/research/predictions/Vorab_Notiz_H137_Bandschaltung_Ueberlagerungen.md
"""

import itertools
import json
import sys
from pathlib import Path

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import DensityMatrix, Operator, Statevector, entropy, partial_trace

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "qam" / "examples" / "zuse_machine"))
from machine_qiskit import STATUSES, FiniteBand  # noqa: E402

RNG = np.random.default_rng(20261125)
P = json.loads((ROOT / "qam/examples/zuse_machine/machine.json").read_text(encoding="utf-8"))
R = {
    "states": ["a", "b", "halt"],
    "halt": "halt",
    "rules": [
        {"state": "a", "read": 0, "write": 1, "move": 0, "next": "b"},
        {"state": "a", "read": 1, "write": 0, "move": 0, "next": "b"},
        {"state": "b", "read": 0, "write": 0, "move": 0, "next": "a"},
        {"state": "b", "read": 1, "write": 1, "move": 0, "next": "a"},
    ],
}


def encode(m, tape, head, state):
    return sum(b << i for i, b in enumerate(tape)) | (m._position_code(head, m.states.index(state)) << m.cells)


def valid_configs(m):
    for tape in itertools.product((0, 1), repeat=m.cells):
        for head in range(m.cells):
            for state in m.states:
                yield list(tape), head, state


def step_map(m):
    """Classical step f: input code -> output code (config | status << width), read from the circuit on basis states."""
    f = {}
    for tape, head, state in valid_configs(m):
        x = encode(m, tape, head, state)
        sv = evolve(Statevector.from_int(x, (2,) * m.circuit.num_qubits), m.circuit)
        probs = sv.probabilities_dict(decimals=12)
        assert len(probs) == 1
        out = int(next(iter(probs)), 2) >> m.width
        f[x] = out
    return f


def random_superposition(m, codes, k):
    pick = RNG.choice(len(codes), size=k, replace=False)
    amps = RNG.normal(size=k) + 1j * RNG.normal(size=k)
    amps /= np.linalg.norm(amps)
    return {codes[i]: a for i, a in zip(pick, amps)}


def vec(dim_bits, coeffs):
    v = np.zeros(2 ** dim_bits, dtype=complex)
    for idx, a in coeffs.items():
        v[idx] += a
    return Statevector(v)


def xor_oracle(n_in, n_out, table):
    """|y>|z> -> |y>|z xor table[y]>; table maps y (int) to int, missing y -> 0."""
    qc = QuantumCircuit(n_in + n_out)
    ctrls = list(range(n_in))
    for y, val in table.items():
        for bit in range(n_out):
            if (val >> bit) & 1:
                qc.mcx(ctrls, n_in + bit, ctrl_state=y)
    return qc


def unitarity(qc):
    """Max |U^dag U - I| for small circuits (Operator); for larger ones the circuit consists only of
    (multi-)controlled X and SWAP gates, i.e. a basis permutation, and unitarity is checked as bijectivity of the
    classical basis map on all 2^nq inputs."""
    nq = qc.num_qubits
    if nq <= 10:
        U = Operator(qc).data
        return {"method": "Operator", "max_dev_UdagU": float(np.max(np.abs(U.conj().T @ U - np.eye(2 ** nq)))),
                "max_dev_UUdag": float(np.max(np.abs(U @ U.conj().T - np.eye(2 ** nq)))),
                "permutation_matrix": bool(np.all(np.isclose(np.abs(U), 0) | np.isclose(np.abs(U), 1)))}
    xs = np.arange(2 ** nq, dtype=np.int64)
    for inst in qc.data:
        name = inst.operation.name
        qs = [qc.find_bit(q).index for q in inst.qubits]
        if name == "swap":
            a, b = qs
            ba, bb = (xs >> a) & 1, (xs >> b) & 1
            xs = xs ^ ((ba ^ bb) << a) ^ ((ba ^ bb) << b)
            continue
        op = inst.operation
        assert name == "x" or (hasattr(op, "base_gate") and op.base_gate.name == "x"), name
        ctrls, tgt = qs[:-1], qs[-1]
        cs = getattr(inst.operation, "ctrl_state", (1 << len(ctrls)) - 1)
        fire = np.ones_like(xs, dtype=bool)
        for i, c in enumerate(ctrls):
            fire &= ((xs >> c) & 1) == ((cs >> i) & 1)
        xs = np.where(fire, xs ^ (1 << tgt), xs)
    return {"method": "basis permutation (only X-type gates; Operator for nq <= 10)", "bijective": bool(len(np.unique(xs)) == 2 ** nq)}


_AER = {}


def evolve(sv, qc, force_aer=False):
    """Statevector evolution: qiskit.quantum_info for up to 14 qubits; above that qiskit-aer (statevector method),
    because the pure-Python evolution takes several seconds per instruction-heavy 16-qubit circuit."""
    if qc.num_qubits <= 14 and not force_aer:
        return sv.evolve(qc)
    from qiskit import transpile
    from qiskit_aer import AerSimulator
    key = id(qc)
    if key not in _AER:
        sim = AerSimulator(method="statevector")
        _AER[key] = (sim, transpile(qc, sim, optimization_level=0))
    sim, tqc = _AER[key]
    circ = QuantumCircuit(qc.num_qubits)
    circ.set_statevector(sv.data)
    circ.compose(tqc, inplace=True)
    circ.save_statevector()
    return Statevector(np.asarray(sim.run(circ).result().get_statevector()))


def report(tag, obj):
    print(json.dumps({"k310": tag, **obj}, separators=(",", ":")), flush=True)


# --- control (iv, added for the method change): qiskit-aer and quantum_info agree on a 14-qubit circuit
_m = FiniteBand(P, 3)
_codes = [encode(_m, t, h, st) for t, h, st in valid_configs(_m)]
_sv = vec(_m.circuit.num_qubits, random_superposition(_m, _codes, 6))
report("control_iv_aer_vs_quantum_info", {"qubits": _m.circuit.num_qubits,
       "max_abs_diff": float(np.max(np.abs(evolve(_sv, _m.circuit).data - evolve(_sv, _m.circuit, force_aer=True).data)))})

# --- control (i): basis traces vs verification.md
for ex in P["examples"]:
    trace = FiniteBand(P, len(ex["tape"])).trace(ex)
    report("control_i_trace", {"example": ex["name"], "trace": trace})

for n in (2, 3):
    m = FiniteBand(P, n)
    nq = m.circuit.num_qubits
    unit = unitarity(m.circuit)
    f = step_map(m)
    codes = sorted(f)
    # H137c
    image = {}
    for x, y in f.items():
        image.setdefault(y, []).append(x)
    collisions = sum(len(v) - 1 for v in image.values())
    report("H137c_P", {"n": n, "qubits": nq, "domain": len(codes), "image": len(image), "collisions": collisions,
                       "expected_collisions": n * 2 ** (n - 1)})
    example_pairs = [v for v in image.values() if len(v) > 1][:2]
    report("H137c_P_examples", {"n": n, "colliding_input_codes": example_pairs})
    # H137a, H137b
    fid_min, offmax, purities = 1.0, 0.0, []
    out_qubits = list(range(m.width, nq))
    for trial in range(200):
        k = int(RNG.integers(2, min(8, len(codes)) + 1))
        sup = random_superposition(m, codes, k)
        psi = evolve(vec(nq, sup), m.circuit)
        expected = vec(nq, {x | (f[x] << m.width): a for x, a in sup.items()})
        fid_min = min(fid_min, abs(np.vdot(expected.data, psi.data)) ** 2)
        rho_out = partial_trace(psi, list(range(m.width))).data  # keep output register
        off = rho_out - np.diag(np.diag(rho_out))
        offmax = max(offmax, float(np.max(np.abs(off))))
        purities.append(float(np.real(np.trace(rho_out @ rho_out))))
        # predicted purity
        w = {}
        for x, a in sup.items():
            w[f[x]] = w.get(f[x], 0) + abs(a) ** 2
        pred = sum(v ** 2 for v in w.values())
        assert abs(pred - purities[-1]) < 1e-10, (pred, purities[-1])
    report("H137a_P", {"n": n, "unitarity": unit, "min_fidelity_200": fid_min})
    report("H137b_P", {"n": n, "max_offdiag_rho_out": offmax, "purity_min": min(purities), "purity_max": max(purities),
                       "purity_matches_prediction": True})
    # collision pair with a relative phase: where does the phase go?
    x1, x2 = example_pairs[0][:2]
    phi = 0.7
    sup = {x1: 1 / np.sqrt(2), x2: np.exp(1j * phi) / np.sqrt(2)}
    psi = evolve(vec(nq, sup), m.circuit)
    rho_out = DensityMatrix(partial_trace(psi, list(range(m.width))))
    rho_in = partial_trace(psi, out_qubits).data
    report("H137b_phase_on_collision_pair", {"n": n, "out_purity": float(np.real(rho_out.purity())),
                                             "in_offdiag": [float(abs(rho_in[x1, x2])), float(np.angle(rho_in[x2, x1]))]})

# --- R: injective program, Bennett step on the configuration register
for n in (2, 3):
    m = FiniteBand(R, n)
    w = m.width
    f = step_map(m)
    codes = sorted(f)
    image = {}
    for x, y in f.items():
        image.setdefault(y, []).append(x)
    collisions = sum(len(v) - 1 for v in image.values())
    mask = (1 << w) - 1
    finv = {y & mask: x | ((y >> w) << w) for y, (x,) in ((y, v) for y, v in image.items())}
    # Bennett: register A (w), register B (w+2). U_f; swap config parts; oracle on A xoring (f^-1(y), status) into B
    nq = 2 * w + 2
    qc = QuantumCircuit(nq)
    qc.compose(m.circuit, inplace=True)
    for i in range(w):
        qc.swap(i, w + i)
    qc.compose(xor_oracle(w, w + 2, finv), inplace=True)
    dev = unitarity(qc)
    clean = all(int(next(iter(evolve(Statevector.from_int(x, (2,) * nq), qc).probabilities_dict(decimals=12))), 2) >> w == 0
                for x in codes)
    fid_min, pur_min = 1.0, 1.0
    for trial in range(200):
        k = int(RNG.integers(2, min(8, len(codes)) + 1))
        sup = random_superposition(m, codes, k)
        psi = evolve(vec(nq, sup), qc)
        expected = vec(nq, {f[x] & mask: a for x, a in sup.items()})
        fid_min = min(fid_min, abs(np.vdot(expected.data, psi.data)) ** 2)
        rho_a = partial_trace(psi, list(range(w, nq)))
        pur_min = min(pur_min, float(np.real(rho_a.purity())))
    report("H137c_R_control", {"n": n, "collisions": collisions, "bennett_unitary_dev": dev, "ancilla_clean_all_basis": clean,
                               "min_fidelity_200": fid_min, "min_purity_config_register": pur_min})
    # H137d: tape 0..0, state a, head (|0>+|1>)/sqrt2
    sup = {encode(m, [0] * n, 0, "a"): 1 / np.sqrt(2), encode(m, [0] * n, 1, "a"): 1 / np.sqrt(2)}
    psi = evolve(vec(nq, sup), qc)
    rho_a = partial_trace(psi, list(range(w, nq)))  # configuration register (pure)
    cells = list(range(n))
    rest = list(range(n, w))
    s_cells = float(entropy(partial_trace(rho_a, rest), base=2))
    rho01 = partial_trace(rho_a, [q for q in range(w) if q not in (0, 1)]).data
    # partial transpose on qubit 1 (qiskit little endian: index = q0 + 2 q1)
    r = rho01.reshape(2, 2, 2, 2)  # [q1, q0, q1', q0']
    pt = r.transpose(2, 1, 0, 3).reshape(4, 4)
    neg = float(sum(abs(e) for e in np.linalg.eigvalsh(pt) if e < 0))
    report("H137d_R", {"n": n, "S_cells_vs_head_state_bits": s_cells, "negativity_cell0_cell1": neg,
                       "rho_cell0_cell1_diag": np.round(np.real(np.diag(rho01)), 12).tolist(),
                       "rho_cell0_cell1_max_offdiag": float(np.max(np.abs(rho01 - np.diag(np.diag(rho01)))))})
    if n == 2:
        report("H137d_R_state", {"amplitudes": {format(i, f"0{w}b"): [round(float(a.real), 12), round(float(a.imag), 12)]
                                                for i, a in enumerate(np.asarray(rho_a.to_statevector().data)) if abs(a) > 1e-12}})
