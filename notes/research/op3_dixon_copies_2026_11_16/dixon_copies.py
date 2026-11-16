"""OP3: zwei und vier Dixon-Kopien (Tensor-Shift HS(7), HS(8)).  (Erkundung, nicht blind.)

(1) Kommutant von Eich- und Lorentzgruppe auf n Kopien einer Generation (16 Weyl-Multiplettkomponenten x 2 Spinorkomponenten
    = 32 komplex = 64 reell, wie C (x) H (x) O): dim_C = 6 n^2 (r19: n = 1 gibt C^6).  Kopienindex: Eichgruppe wirkt trivial.
(2) HS(7), n = 2: Kopien-Qubit.  Drei unverzerrte Zustaende (+x, +y, +z): Ueberlappung 1/2, K = 2/3, Bargmann-Phase pi/4,
    det G = 0 (flacher Oktant, eine Masse null).
(3) HS(8), n = 4 = 2 x 2: C^2 (x) C^2 = Sym^2 (Triplett, Spin 1) + Lambda^2 (Singulett, eps).  Spin-1-Dreieck (r15, Erkundung
    15.11.) im Triplett: Ueberlappung 1/2, K = 2/3, Phase 0.679042, det G = 0.0503.
(4) Die einzige SU(2)-aequivariante Abbildung Lambda^3(Triplett) -> Singulett ist die Determinante (Spatprodukt
    v1 . (v2 x v3)); |det V|^2 = det G.  Die "Normale" der drei liegt also kanonisch im Singulett und ist genau dann != 0,
    wenn das Dreieck gebogen ist.  Ladungsneutral, weil die Eichgruppe auf dem Kopienindex trivial wirkt.
"""
import numpy as np
from itertools import product

rng = np.random.default_rng(1122)
s = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1, -1]).astype(complex)]
lam = []
for (i, j) in [(0, 1), (0, 2), (1, 2)]:
    for kind in ("x", "y"):
        L = np.zeros((3, 3), complex)
        if kind == "x": L[i, j] = L[j, i] = 1
        else: L[i, j] = -1j; L[j, i] = 1j
        lam.append(L)
lam.append(np.diag([1, -1, 0]).astype(complex)); lam.append(np.diag([1, 1, -2]).astype(complex) / np.sqrt(3))

# Multipletts (SU(3)-Darstellung, SU(2)-Darstellung, Y): 3, 3bar, 1 ; 2, 1
mult = [("3", "2", 1/6), ("1", "2", -1/2), ("3b", "1", -2/3), ("3b", "1", 1/3), ("1", "1", 1), ("1", "1", 0)]


def gens_for(m):
    c3, c2, y = m
    d3 = 3 if c3 != "1" else 1; d2 = 2 if c2 == "2" else 1
    out = []
    for L in lam:
        A = (L / 2) if c3 == "3" else (-L.conj() / 2) if c3 == "3b" else np.zeros((1, 1))
        out.append(np.kron(np.kron(A if d3 > 1 else np.zeros((1, 1)), np.eye(d2)), np.eye(2)))
    for P in s:
        B = P / 2 if d2 == 2 else np.zeros((1, 1))
        out.append(np.kron(np.kron(np.eye(d3), B if d2 > 1 else np.zeros((1, 1))), np.eye(2)))
    out.append(y * np.eye(d3 * d2 * 2))
    for P in s:                              # Lorentz (Drehanteil) auf dem Spinorindex
        out.append(np.kron(np.eye(d3 * d2), P / 2))
    return out


def block_diag(ms):
    n = sum(m.shape[0] for m in ms); out = np.zeros((n, n), complex); k = 0
    for m in ms:
        d = m.shape[0]; out[k:k + d, k:k + d] = m; k += d
    return out


per = [gens_for(m) for m in mult]
G1 = [block_diag([p[i] for p in per]) for i in range(len(per[0]))]
dim1 = G1[0].shape[0]
print(f"(1) eine Generation: komplexe Dimension {dim1} (= 64 reell)")
# Hyperladung-Normierung so, dass verschiedene Multipletts unterscheidbar bleiben: Lorentz-Boost-Anteil fehlt -> nur Drehungen;
# fuer die Dimension des Kommutanten genuegt das, weil die Multipletts schon durch Eichladungen getrennt sind.
# Kommutant blockweise: X = sum_ab E_ab (x) X_ab auf C^n (x) V; X vertauscht mit 1 (x) g genau dann, wenn jedes X_ab mit g
# vertauscht.  Also dim = n^2 * dim End_G(V).  dim End_G(V) wird direkt berechnet, n = 1, 2 zusaetzlich voll.
def commutant_dim(gens):
    N = gens[0].shape[0]
    M = np.vstack([np.kron(np.eye(N), g) - np.kron(g.T, np.eye(N)) for g in gens])
    sv = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(sv < 1e-9))
d1 = commutant_dim(G1)
for n in (1, 2):
    print(f"    n = {n} Kopien: dim_C Kommutant = {commutant_dim([np.kron(np.eye(n), g) for g in G1])} (blockweise n^2 * {d1} = {n * n * d1})")
for n in (4,):
    print(f"    n = {n} Kopien: dim_C Kommutant = n^2 * {d1} = {n * n * d1} (blockweise, Kopienanteil M_{n}(C))")


def gram(states):
    return np.array([[np.vdot(a, b) for b in states] for a in states])


def bargmann(states):
    a, b, c = states
    return np.angle(np.vdot(a, b) * np.vdot(b, c) * np.vdot(c, a))


def koide_from_overlaps(G):
    off = [abs(G[i, j]) ** 2 for i in range(3) for j in range(3) if i < j]
    return (1 + 2 * np.mean(off)) / 3


# (2) HS(7): Kopien-Qubit
def spinor(n):
    th, ph = np.arccos(n[2]), np.arctan2(n[1], n[0])
    return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])


q = [spinor(v) for v in np.eye(3)]
Gq = gram(q)
print(f"(2) HS(7), Qubit-Zustaende +x, +y, +z: |Ueberlappung|^2 = {abs(Gq[0,1])**2:.3f}, K = {koide_from_overlaps(Gq):.4f},"
      f" Phase = {abs(bargmann(q)):.6f} (pi/4 = {np.pi/4:.6f}), det G = {np.linalg.det(Gq).real:.2e}")

# (3) HS(8): Triplett + Singulett, Spin-1-Dreieck
ca = np.sqrt(2) - 1; cpsi = np.sqrt((2 * np.sqrt(2) - 1) / 3); spsi = np.sqrt(1 - cpsi ** 2)
dirs = [np.array([spsi * np.cos(2 * np.pi * k / 3), spsi * np.sin(2 * np.pi * k / 3), cpsi]) for k in range(3)]
print(f"    Spin-1-Dreieck: cos(Seitenwinkel) = {dirs[0] @ dirs[1]:.6f} (sqrt2 - 1 = {ca:.6f})")
trip = [np.kron(spinor(d), spinor(d)) for d in dirs]           # kohaerente Spin-1-Zustaende in C^2 (x) C^2
eps = np.array([0, 1, -1, 0]) / np.sqrt(2)                      # Singulett
Gt = gram(trip)
print(f"(3) HS(8): Singulettanteil der drei Zustaende = {max(abs(np.vdot(eps, t)) for t in trip):.1e} (alle im Triplett);"
      f" |Ueberlappung|^2 = {abs(Gt[0,1])**2:.4f}, K = {koide_from_overlaps(Gt):.4f}, Phase = {abs(bargmann(trip)):.6f},"
      f" det G = {np.linalg.det(Gt).real:.6f}")
# (4) Spatprodukt im Triplett: Orthonormalbasis des Tripletts (Sym^2) und Koordinaten der drei Zustaende
B = np.array([[1, 0, 0, 0], [0, 1 / np.sqrt(2), 1 / np.sqrt(2), 0], [0, 0, 0, 1]], complex)
V = np.array([[np.vdot(b, t) for t in trip] for b in B])        # 3 x 3, Spalten = Generationen
detV = np.linalg.det(V)
print(f"(4) Spatprodukt det V = {detV:.6f}; |det V|^2 = {abs(detV)**2:.6f} = det G = {np.linalg.det(Gt).real:.6f}")
# Aequivarianz: SU(2) auf beiden Kopien-Qubits gleich -> Triplett dreht, det V aendert nur um det = 1 (Phase 1)
U = np.linalg.qr(rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)))[0]; U = U / np.sqrt(np.linalg.det(U))
trip2 = [np.kron(U, U) @ t for t in trip]
V2 = np.array([[np.vdot(b, t) for t in trip2] for b in B])
print(f"    nach gemeinsamer SU(2)-Drehung: det V' = {np.linalg.det(V2):.6f} (unveraendert), Singulett invariant:"
      f" {np.allclose(np.kron(U, U) @ eps, eps)}")
# Vergleich: Leptonphase 2/3 und flacher Fall
for name, ph in (("flach pi/4", np.pi / 4), ("Spin-1-Dreieck", 0.679042), ("Leptonen 2/3", 2 / 3)):
    print(f"    {name:15s}: det G = (sqrt2 cos phi - 1)/2 = {(np.sqrt(2) * np.cos(ph) - 1) / 2:.6f}")

# (5) Halbierung: HS(8) = HS(7) + HS(7), HS(7) = HS(6) + HS(6).  Kopienindex C^2 (x) C^2 mit Produktbasis |00>,|01>,|10>,|11>:
#     die vier Kaesten sind die vier Dixon-Kopien; erstes Bit halbiert HS(8) in zwei HS(7), zweites Bit HS(7) in zwei HS(6).
#     Die Zerlegung Triplett + Singulett liegt quer dazu: |01> und |10> mischen.
P0 = np.kron(np.diag([1, 0]), np.eye(2)); P1 = np.eye(4) - P0
print(f"(5) Halbierung nach dem ersten Bit: Raenge {int(np.trace(P0).real)} + {int(np.trace(P1).real)} (je ein HS(7) aus zwei Dixon-Kopien);"
      f" Singulett in einer Haelfte? {np.allclose(P0 @ eps, eps) or np.allclose(P1 @ eps, eps)}"
      f" (Gewicht in der ersten Haelfte {np.linalg.norm(P0 @ eps)**2:.2f})")
print("    Triplett-Gewichte der drei Generationen je Dixon-Kasten |00>,|01>,|10>,|11>:")
for k, t3 in enumerate(trip):
    print(f"      Generation {k+1}: {np.round(abs(t3)**2, 4)}")
