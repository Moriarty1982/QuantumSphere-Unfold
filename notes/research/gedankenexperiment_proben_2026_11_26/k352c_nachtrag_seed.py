"""k352c (H161, nachtraeglich): Kontrolle zu K-c mit unabhaengigen Zufallsstroemen.
Anlass: in k352 lag das Mittel der Trefferquote bei 0.5116 (20 Zustaende je 4096 Laeufe), mehr als die reine Zaehlstatistik
des Mittels (0.0017) erwarten laesst. k352 benutzt fuer alle Schaltungen denselben Startwert des Simulators; die Laeufe sind
dann nicht unabhaengig. Erster Versuch dieser Kontrolle mit benachbarten Startwerten 1000 + k: Mittel 0.4893, wieder dieselbe
Art Abweichung (benachbarte Startwerte geben im Aer-Simulator ueberlappende Zufallsstroeme je Lauf). Deshalb hier drei Stufen:
(1) benachbarte Startwerte (zeigt den Effekt), (2) weit getrennte Zufalls-Startwerte, (3) eine Schaltung mit 2 000 000 Laeufen,
dazu die exakte Wahrscheinlichkeit.
Aufruf: python k352c_nachtrag_seed.py > k352c_out.txt
"""
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector

SHOTS = 4096
rng = np.random.default_rng(20261127)
def lauf(seed, shots, qc):
    sim = AerSimulator(seed_simulator=int(seed))
    c = sim.run(transpile(qc, sim), shots=shots).result().get_counts(); hit = 0
    for bits, n in c.items():
        y, z, x = (int(b) for b in bits); hit += n * (y == (x ^ z))
    return hit / shots

def schaltung():
    qc = QuantumCircuit(1, 3); qc.u(*rng.uniform(0, 2 * np.pi, 3), 0)
    qc.h(0); qc.measure(0, 0); qc.h(0)
    qc.measure(0, 1)
    qc.sdg(0); qc.h(0); qc.measure(0, 2)
    return qc

def bericht(name, r):
    r = np.array(r); se = r.std(ddof=1) / np.sqrt(len(r))
    print(f"{name}: Trefferquote Mittel {r.mean():.5f}, Streuung {r.std(ddof=1):.5f} (erwartet {0.5/np.sqrt(SHOTS):.5f}), min {r.min():.4f}, max {r.max():.4f}; Mittel - 0.5 = {(r.mean()-0.5)/se:+.2f} Standardfehler")

bericht("(1) 200 Zustaende, Startwerte 1000 + k (benachbart)", [lauf(1000 + k, SHOTS, schaltung()) for k in range(200)])
seeds = rng.integers(1, 2**31 - 1, 200)
bericht("(2) 200 Zustaende, Zufalls-Startwerte (weit getrennt)", [lauf(sd, SHOTS, schaltung()) for sd in seeds])
big = lauf(424242, 2_000_000, schaltung())
print(f"(3) eine Schaltung, 2 000 000 Laeufe: Trefferquote {big:.5f} (Zaehlstatistik +-{0.5/np.sqrt(2e6):.5f})")
rates = []
for k in range(0):
    qc = QuantumCircuit(1, 3); qc.u(*rng.uniform(0, 2 * np.pi, 3), 0)
    qc.h(0); qc.measure(0, 0); qc.h(0)
    qc.measure(0, 1)
    qc.sdg(0); qc.h(0); qc.measure(0, 2)
    sim = AerSimulator(seed_simulator=1000 + k)
    c = sim.run(transpile(qc, sim), shots=SHOTS).result().get_counts(); hit = 0
    for bits, n in c.items():
        y, z, x = (int(b) for b in bits); hit += n * (y == (x ^ z))
    rates.append(hit / SHOTS)
# exakt: nach der Z-Messung ist der Zustand |0> oder |1>; Wahrscheinlichkeit fuer Y-Bit 0
for name, sv in (("|0>", Statevector([1, 0])), ("|1>", Statevector([0, 1]))):
    qc = QuantumCircuit(1); qc.sdg(0); qc.h(0)
    p = sv.evolve(qc).probabilities()
    print(f"  exakt: nach Z-Ergebnis {name} ist P(Y-Bit = 0) = {p[0]:.12f}")

