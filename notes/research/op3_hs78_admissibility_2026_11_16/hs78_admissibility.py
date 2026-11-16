"""Zulaessigkeit von HS(7) und HS(8) nach den Atlas-Regeln (v470/32).  (Erkundung, nicht blind.)

Atlas: HS(4)-Tor  Leak^(4)(M) = (1-Q) M Q + Q M (1-Q) = 0  (Q = meta-septum-Projektor);
       HS(5)-Schuld Debt^(5)(T) = (1-P5) T P5 + P5 T (1-P5) = 0 mit P5 = diag(P, P) (Verdopplung vorne/hinten).
Verallgemeinerung (hier gesetzt, nicht im Atlas): HS(n+1) = HS(n) (+) HS(n), P^(n+1) = diag(P^(n), P^(n)) = 1_2 (x) P^(n).
Geprueft:
 (1) Jede Operation nur auf dem Kopienindex, X (x) 1, vertauscht mit 1 (x) P: Schuld und Leck verschwinden identisch.
 (2) Die Operationen aus r25 (Hadamard/Phasen auf dem Kopien-Qubit, Projektion auf Triplett/Singulett auf zwei Kopien-Qubits)
     sind Kopienoperationen: Schuld 0.
 (3) Gegenbeispiel: Kopienmischung zusammen mit einer Bewegung aus dem Sektor (A (x) X, [A, P] != 0) hat Schuld != 0.
 (4) Die Stufen bleiben genestet: P^(8) eingeschraenkt auf eine Haelfte ist P^(7), auf ein Viertel P^(6).
Platzhalter: P ist ein zufaelliger Projektor vom Rang 7 auf 16 Kanaelen (die echte HS(4)-Matrix M_16 wird nicht benutzt);
die Aussagen (1)-(4) haengen nur an der Blockgestalt.
"""
import numpy as np

rng = np.random.default_rng(1123)


def projector(n, r):
    q, _ = np.linalg.qr(rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))
    return q[:, :r] @ q[:, :r].conj().T


def debt(T, P):
    I = np.eye(P.shape[0])
    return np.linalg.norm((I - P) @ T @ P + P @ T @ (I - P))


P = projector(16, 7)                       # Platzhalter fuer das HS(4)-Tor
H = np.array([[1, 1], [1, -1]]) / np.sqrt(2); S = np.diag([1, 1j])
for k, name in ((1, "HS(5) = 2 x HS(4)"), (2, "4 Kopien von HS(4) (Muster fuer HS(8) = 4 x HS(6))")):
    Pn = np.kron(np.eye(2 ** k), P)
    X = rng.normal(size=(2 ** k, 2 ** k)) + 1j * rng.normal(size=(2 ** k, 2 ** k))
    print(f"(1) {name}: beliebige Kopienoperation X (x) 1: Schuld = {debt(np.kron(X, np.eye(16)), Pn):.1e}")

# (2) Operationen aus r25
P8 = np.kron(np.eye(4), P)
ops = {"Hadamard auf Kopien-Qubit 1": np.kron(np.kron(H, np.eye(2)), np.eye(16)),
       "Phase S auf Kopien-Qubit 2": np.kron(np.kron(np.eye(2), S), np.eye(16))}
eps = np.array([0, 1, -1, 0]) / np.sqrt(2)
Psing = np.outer(eps, eps.conj()); Ptrip = np.eye(4) - Psing
ops["Projektion aufs Singulett"] = np.kron(Psing, np.eye(16))
ops["Projektion aufs Triplett"] = np.kron(Ptrip, np.eye(16))
for name, T in ops.items():
    print(f"(2) {name:28s}: Schuld = {debt(T, P8):.1e}")

# (3) Gegenbeispiel
A = rng.normal(size=(16, 16)) + 1j * rng.normal(size=(16, 16))
print(f"(3) Kopienmischung mit Sektorbewegung A (x) X ([A, P] != 0): Schuld = {debt(np.kron(np.kron(H, np.eye(2)), A), P8):.2f}"
      f"  (dagegen A allein je Kopie, 1 (x) A: {debt(np.kron(np.eye(4), A), P8):.2f})")

# (4) Verschachtelung
half = P8[:32, :32]; quarter = P8[:16, :16]
print(f"(4) P^(8) auf einer Haelfte = P^(7): {np.allclose(half, np.kron(np.eye(2), P))}; auf einem Viertel = P^(6): {np.allclose(quarter, P)}")
