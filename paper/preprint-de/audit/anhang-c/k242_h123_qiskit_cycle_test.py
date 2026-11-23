"""H123, unabhaengige Kontrolle der Setzung S123 als Quantenschaltung (Qiskit).

Zyklustest: Hilfsqubit in |+>, kontrollierte zyklische Vertauschung dreier Register mit den Zustaenden
|a>, |b>, |c> (Spin-j-kohaerente Zustaende als |n>^{(x)2j}, symmetrischer Teilraum), Hadamard-Test fuer Re und Im.
Verglichen wird mit B_tau = 2^(-3j) exp(i tau eps j pi/2) (H123a). Exakt per Zustandsvektor und mit 10^5 Schuessen.

Vorab-Notiz: llm/Vorab_Notiz_H123_Zeitliche_Oktantauslese.md. Aufruf: python3 llm/k242_h123_qiskit_cycle_test.py > llm/k242_out.txt
"""
import itertools
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.primitives import StatevectorSampler

SHOTS = 100_000
SEED = 123
TOL_EXACT = 1e-12

# Pole auf der Kugel (theta, phi) fuer Achse und Vorzeichen; Konvention wie h123_temporal_octant.wl
POLE = {
    ("z", 1): (0.0, 0.0), ("z", -1): (np.pi, 0.0),
    ("x", 1): (np.pi / 2, 0.0), ("x", -1): (np.pi / 2, np.pi),
    ("y", 1): (np.pi / 2, np.pi / 2), ("y", -1): (np.pi / 2, -np.pi / 2),
}


def prepare(qc, qubits, theta, phi):
    # |n> = U3 |0>; globale Phase irrelevant fuer B.
    for q in qubits:
        qc.u(theta, phi, 0.0, q)


def cycle_circuit(k, states, imag):
    """k Qubits je Register; states = drei (theta, phi); misst <Z> des Hilfsqubits."""
    n = 1 + 3 * k
    qc = QuantumCircuit(n, 1)
    regs = [list(range(1 + r * k, 1 + (r + 1) * k)) for r in range(3)]
    for reg, (th, ph) in zip(regs, states):
        prepare(qc, reg, th, ph)
    qc.h(0)
    # kontrollierte Permutation P: Register (1,2,3) -> (2,3,1) qubitweise, als zwei kontrollierte SWAPs
    for i in range(k):
        qc.cswap(0, regs[0][i], regs[1][i])
        qc.cswap(0, regs[1][i], regs[2][i])
    if imag:
        qc.sdg(0)
    qc.h(0)
    return qc


def z_expect_exact(qc):
    sv = Statevector.from_instruction(qc)
    p0 = sv.probabilities([0])[0]
    return 2 * p0 - 1


def direct_bargmann(k, states):
    vecs = []
    for th, ph in states:
        # u(theta, phi, 0)|0> = (cos th/2, e^{i phi} sin th/2)
        v1 = np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])
        v = v1
        for _ in range(k - 1):
            v = np.kron(v, v1)
        vecs.append(v)
    a, b, c = vecs
    return np.vdot(a, b) * np.vdot(b, c) * np.vdot(c, a)


def main():
    print("H123 Qiskit-Zyklustest (Kontrolle von S123), qiskit", __import__("qiskit").__version__)
    sampler = StatevectorSampler(seed=SEED)
    worst_exact = 0.0
    worst_sigma = 0.0
    convention = None
    for twoj in (1, 2, 4):  # j = 1/2, 1, 2
        j = twoj / 2
        k = twoj
        for sz, sx, sy in itertools.product((1, -1), repeat=3):
            eps = sz * sx * sy
            for tau in (1, -1):
                order = [("z", sz), ("x", sx), ("y", sy)] if tau == 1 else [("z", sz), ("y", sy), ("x", sx)]
                states = [POLE[o] for o in order]
                formula = 2 ** (-3 * j) * np.exp(1j * tau * eps * j * np.pi / 2)
                direct = direct_bargmann(k, states)
                re = z_expect_exact(cycle_circuit(k, states, imag=False))
                im = z_expect_exact(cycle_circuit(k, states, imag=True))
                circ = re + 1j * im
                # Der Zyklustest liefert <abc|P|abc> fuer die gewaehlte Permutation; die Konvention (B oder conj B)
                # wird einmal am ersten Fall festgestellt und dann fuer alle Faelle festgehalten.
                if convention is None:
                    convention = "B" if abs(circ - direct) < abs(circ - np.conj(direct)) else "conjB"
                    print("Konvention des Zyklustests:", convention)
                circ_b = circ if convention == "B" else np.conj(circ)
                dev_formula = abs(direct - formula)
                dev_circ = abs(circ_b - direct)
                worst_exact = max(worst_exact, dev_formula, dev_circ)
                # Stichprobe mit Schuessen
                vals = []
                for imag in (False, True):
                    qc = cycle_circuit(k, states, imag)
                    qc.measure(0, 0)
                    counts = sampler.run([qc], shots=SHOTS).result()[0].data.c.get_counts()
                    p0 = counts.get("0", 0) / SHOTS
                    vals.append(2 * p0 - 1)
                est = vals[0] + 1j * vals[1]
                est_b = est if convention == "B" else np.conj(est)
                sig = np.sqrt((1 - vals[0] ** 2) / SHOTS) + np.sqrt((1 - vals[1] ** 2) / SHOTS)
                nsig = abs(est_b - formula) / sig
                worst_sigma = max(worst_sigma, nsig)
                print(f"j={j:3.1f} (sz,sx,sy)=({sz:+d},{sx:+d},{sy:+d}) eps={eps:+d} tau={tau:+d} "
                      f"B_formel={formula.real:+.6f}{formula.imag:+.6f}i  B_schaltung={circ_b.real:+.6f}{circ_b.imag:+.6f}i  "
                      f"Abw={max(dev_formula, dev_circ):.1e}  Schuesse={est_b.real:+.4f}{est_b.imag:+.4f}i ({nsig:.2f} sigma)")
        # Orientierung m -> -m: sz -> -sz bei sx = sy = +1, tau = +1
        bp = direct_bargmann(k, [POLE[("z", 1)], POLE[("x", 1)], POLE[("y", 1)]])
        bm = direct_bargmann(k, [POLE[("z", -1)], POLE[("x", 1)], POLE[("y", 1)]])
        print(f"j={j}: B(+j)={bp:.6f}, B(-j)={bm:.6f}, |B| gleich: {abs(abs(bp)-abs(bm))<TOL_EXACT}, unterschieden: {abs(bp-bm)>1e-9}")
    print(f"groesste exakte Abweichung (Formel/Schaltung): {worst_exact:.2e}  Schranke {TOL_EXACT:.0e}: {worst_exact <= TOL_EXACT}")
    print(f"groesste Abweichung der Schuesse: {worst_sigma:.2f} sigma  Schranke 5: {worst_sigma <= 5}")


if __name__ == "__main__":
    main()
