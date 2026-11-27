"""Abnahme der Baustufe 2 (Software-Referenz): Aufruf  python -m qam.examples.coprocessor.stufe2.check > check_out.txt"""
import math, os, numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import DensityMatrix, Statevector, partial_trace, Operator
from .qtape import QTape, cg_maps, drop_maps, spin_ops, PrimeNoise
here = os.path.dirname(__file__); ok = True
def chk(name, cond, extra=""):
    global ok; ok &= bool(cond); print(f"   {'OK  ' if cond else 'FEHL'} {name} {extra}")

print("== 1 Spin-Bausteine gegen Qiskit (symmetrische Zustaende aus Qubits) ==")
def sym_basis(k):
    """Spalten: |j, m> als Vektor auf k Qubits (Qiskit-Reihenfolge egal, da symmetrisch); |0> = auf."""
    cols = []
    for nd in range(k + 1):
        v = np.zeros(2 ** k)
        for i in range(2 ** k):
            if bin(i).count("1") == nd: v[i] = 1
        cols.append(v / np.linalg.norm(v))
    return np.array(cols).T
rng = np.random.default_rng(3); worst_d = worst_a = worst_r = 0
for k in (1, 2, 3, 4):
    B = sym_basis(k); a = rng.standard_normal((k + 1, k + 1)) + 1j * rng.standard_normal((k + 1, k + 1)); r = a @ a.conj().T; r /= np.trace(r)
    big = DensityMatrix(B @ r @ B.T)
    # DROP: Teilspur ueber ein Qubit
    red = partial_trace(big, [0]).data; Bm = sym_basis(k - 1) if k > 1 else np.ones((1, 1)); mine = sum(A @ r @ A.T for A in drop_maps(k))
    worst_d = max(worst_d, np.abs(Bm.T @ red @ Bm - mine).max(), abs(np.trace(Bm.T @ red @ Bm) - 1))
    # ADD: frisches Qubit |+> ankoppeln, Projektion auf den symmetrischen Raum (j + 1/2) und den Rest (j - 1/2)
    plus = DensityMatrix(np.full((2, 2), 0.5)); tot = big.expand(plus).data if False else np.kron(np.full((2, 2), 0.5), B @ r @ B.T)
    Bp = sym_basis(k + 1); U, D = cg_maps(k, (1 / math.sqrt(2), 1 / math.sqrt(2))); up = Bp.T @ tot @ Bp
    worst_a = max(worst_a, np.abs(up - U @ r @ U.conj().T).max(), abs(np.trace(up) + np.real(np.trace(D @ r @ D.conj().T)) - 1))
    # Drehung: kollektives RY
    al = 0.37; qc = QuantumCircuit(k); [qc.ry(2 * al, q) for q in range(k)]; rot = Bm.T @ Bm if False else B.T @ big.evolve(qc).data @ B
    sy = spin_ops(k)[1]; w, v = np.linalg.eigh(sy); u = (v * np.exp(-1j * 2 * al * w)) @ v.conj().T
    worst_r = max(worst_r, np.abs(rot - u @ r @ u.conj().T).max())
chk("DROP = Teilspur ueber ein Qubit (k = 1..4)", worst_d < 1e-12, f"groesste Abweichung {worst_d:.1e}")
chk("ADD = Projektion auf Gesamtspin j+1/2, Spur von j-1/2 ergaenzt zu 1 (k = 1..4)", worst_a < 1e-12, f"groesste Abweichung {worst_a:.1e}")
chk("ROT = kollektives RY(2 alpha) (k = 1..4)", worst_r < 1e-12, f"groesste Abweichung {worst_r:.1e}")
for k in (1, 2, 5):
    sx, sy, sz = spin_ops(k); j = k / 2
    chk(f"Spin-Algebra Band {k}: [S_x, S_y] = i S_z und S^2 = j(j+1)", np.abs(sx @ sy - sy @ sx - 1j * sz).max() < 1e-12 and np.abs(sx @ sx + sy @ sy + sz @ sz - j * (j + 1) * np.eye(k + 1)).max() < 1e-12)

print("== 2 Band der Schleife L3 aus k395 auf der Maschine ==")
L3 = open(os.path.join(here, "baender", "l3_schleife.qtape")).read()
m = QTape(L3).run(); res = m.result(); m.write_trace(os.path.join(here, "l3_schleife_protokoll.jsonl"))
print(f"   Stopgrund {res['stopgrund']}, Status {res['status']}, Schritte {res['schritte']}, b = {res['b']:.12f}, Hash {res['hash'][:16]}")
chk("L3 haelt an und landet bei b = 1/2", res["stopgrund"] == "halted" and abs(res["b"] - 0.5) < 1e-12)
b = 0.9; seq = []
for _ in range(8): b = 1 - 2 * b * (1 - b); seq.append(b)
got = [r["b"] for r in m.trace if r["zelle"].startswith("READ")][1:9]
chk("Verlauf gleich der geschlossenen Form b' = 1 - 2b(1-b)", np.abs(np.array(got) - np.array(seq)).max() < 1e-11, "erste Werte " + " ".join(f"{g:.8f}" for g in got[:5]))
print("   Auszug aus dem Protokoll (erste Runde):")
for r in m.trace[5:13]: print(f"      Schritt {r['schritt']:3d} | {r['zelle']:34s} | {r['getan']} | weil: {r['warum']}")

print("== 3 Guards und Stopgruende ==")
chk("verbotener Befehl -> reject", QTape("QTAPE 2\nALLOW INIT HALT\nINIT 1 0.5\nHC\nHALT").run().result()["stopgrund"] == "reject")
chk("falsche Kennung -> reject, nichts gerechnet", QTape("BAND 1\nHALT").run().result()["stopgrund"] == "reject")
chk("Budget erschoepft -> step_limit", QTape("QTAPE 2\nBUDGET 20\nINIT 1 0.5\nLOOP 100\nHC\nEND\nHALT").run().result()["stopgrund"] == "step_limit")
chk("SWAP mit x > 1 -> guard", QTape("QTAPE 2\nINIT 1 0.5\nSWAP 1.5\nHALT").run().result()["stopgrund"] == "guard")
chk("Band ohne HALT -> boundary", QTape("QTAPE 2\nINIT 1 0.5\nHC").run().result()["stopgrund"] == "boundary")
chk("KMAX ueberschritten -> guard", QTape("QTAPE 2\nKMAX 3\nINIT 1 1\nLOOP 5\nADD 1\nEND\nHALT").run().result()["stopgrund"] == "guard")
a, b2 = QTape(L3).run().result()["hash"], QTape(L3).run().result()["hash"]; chk("gleicher Lauf, gleicher Hash", a == b2)

print("== 4 Messung im Lauf und Verzweigung ==")
T = "QTAPE 2\nINIT 1 0.5\nMEASURE bit\nJUMP_IF bit 2\nSET z = 0\nREAD b b\nHALT"
n1 = sum(QTape(T, seed=s, trace_every=0).run().reg["bit"] for s in range(4000)) / 4000
chk("MEASURE: Anteil '+' bei b = 0,5 nahe 0,75", abs(n1 - 0.75) < 0.03, f"gemessen {n1:.4f} aus 4000 Laeufen (Stichprobe, SEED 0..3999)")
r1 = QTape(T, seed=0).run(); chk("nach selektiver Messung ist der Zustand rein (|b| = 1)", abs(abs(r1.result()["b"]) - 1) < 1e-12)

print("== 5 Primzahl-Rauschgenerator ==")
pn = PrimeNoise(); first = [pn.next("prime_gap") for _ in range(8)]
print("   erste Ausgaben (Primzahl, normierte Luecke - 1):", ", ".join(f"{p}: {v:+.3f}" for p, v in first))
pn = PrimeNoise(); v = np.array([pn.next("prime_gap")[1] for _ in range(100000)])
print(f"   100000 Werte: Mittel {v.mean():+.4f}, Streuung {v.std():.4f}, Korrelation aufeinanderfolgender Werte {np.corrcoef(v[:-1], v[1:])[0, 1]:+.4f}")
chk("Primzahlen stimmen (die 100000. Primzahl ist 1299709)", int(pn.p[99999]) == 1299709)
print("\nGESAMT:", "alle Pruefungen bestanden" if ok else "FEHLER")
