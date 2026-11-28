"""k460 (Test H243): Z3-Klassen der Mischungsstrukturen in der T-Eigenbasis (Ladungsbasis der geladenen Leptonen).
Majorana-Regel (H242): Eintrag t_i^T N t_j hat Klasse (i+j) mod 3; Dirac-Regel: t_i^dagger D t_j hat Klasse (j-i) mod 3.
Maschinerie unveraendert aus k370/k371. Vorab Vorab_H243_Z3_Mischung.md. Aufruf aus diesem Ordner: python3 k460_test_h243.py > k460_out.txt
"""
import numpy as np

src = open("../mischung_h174/k370_test_h174.py").read().split('print("== Kontrolle')[0]
ns = {}; exec(src, ns)
T, C, Nhat, eig_sorted, pmns, X_LEP = (ns[k] for k in ("T", "C", "Nhat", "eig_sorted", "pmns", "X_LEP"))
r2 = np.sqrt(2)


def E(i, j):
    M = np.zeros((3, 3)); M[i, j] = 1; return M


DIRS = {
    "S+b": (E(0, 1) + E(1, 0) - E(1, 2) - E(2, 1)) / r2, "S+c": E(0, 2) + E(2, 0), "S+d": E(1, 1),
    "S-p": (E(0, 1) + E(1, 0) + E(1, 2) + E(2, 1)) / r2, "S-q": (E(0, 0) - E(2, 2)) / r2,
    "K+": 1j * (E(0, 1) - E(1, 0) + E(1, 2) - E(2, 1)) / r2, "K-1": 1j * (E(0, 2) - E(2, 0)),
    "K-2": 1j * (-E(0, 1) + E(1, 0) + E(1, 2) - E(2, 1)) / r2,
}
w = np.exp(2j * np.pi / 3)
ev, V = np.linalg.eig(T)
tk = []
for k in range(3):
    i = np.argmin(abs(ev - w ** k)); v = V[:, i]; tk.append(v / np.linalg.norm(v))
Tb = np.column_stack(tk)
print("=" * 96)
print("H243 (k460)  Z3-Klassen in der T-Eigenbasis (Ladungsbasis)")
print("=" * 96)
print(f"T^3 = I: {np.allclose(np.linalg.matrix_power(T, 3), np.eye(3))};  Eigenwerte {np.round(ev, 6)};  t_k Eigenwert w^k: "
      f"{[bool(np.allclose(T @ tk[k], w**k * tk[k])) for k in range(3)]}")
print(f"C(rho, delta) diagonal in der Ladungsbasis (Dirac-Klasse 0): {np.allclose(np.triu(Tb.conj().T @ C(1.3, 0.7) @ Tb, 1), 0)}")


def W_major(N):
    M = Tb.T @ N @ Tb; tot = np.sum(abs(M) ** 2)
    return np.array([sum(abs(M[i, j]) ** 2 for i in range(3) for j in range(3) if (i + j) % 3 == c) for c in range(3)]) / tot


def W_dirac(D):
    M = Tb.conj().T @ D @ Tb; tot = np.sum(abs(M) ** 2)
    return np.array([sum(abs(M[i, j]) ** 2 for i in range(3) for j in range(3) if (j - i) % 3 == c) for c in range(3)]) / tot


def W_conj(N):  # Gegenprobe: Majorana mit Konjugations-Regel (j - i)
    return W_dirac(N)


N0 = Nhat(np.pi / 6, 1)
h = 1e-6
dN = (Nhat(np.pi / 6 - h, 1) - Nhat(np.pi / 6 - 2 * h, 1)) / h  # einseitig (b reell nur fuer delta_nu <= pi/6)
dN2 = (Nhat(np.pi / 6 - 2 * h, 1) - Nhat(np.pi / 6 - 4 * h, 1)) / (2 * h)
Nx = Nhat(np.pi / 6 - X_LEP, 1)
print("\nN-hat(pi/6) =\n", np.round(N0, 6))
print("Ableitung nach delta_nu (einseitig, links von pi/6; b ~ sqrt(pi/6 - delta_nu) divergiert, daher getrennt b- und c-Anteil):")
dc = (Nhat(np.pi / 6 - h, 1)[0, 2] - N0[0, 2]) / (-h)
print(f"  dc/d delta_nu = {dc:.6f};  b(pi/6 - x) = {Nx[0,1]:.6f} (b ~ sqrt(x): fuehrende Versatzrichtung ist S+b-artig)")
Bdir = (E(0, 1) + E(1, 0) - E(1, 2) - E(2, 1)) / r2
Cdir = E(0, 2) + E(2, 0)
print("\nMajorana-Regel (i+j): Gewichte [W0, W1, W2]")
for name, M in (("A1  N-hat(pi/6)  (Baum)", N0), ("    N-hat(pi/6 - x)", Nx), ("A2  b-Richtung (fuehrende Versatzrichtung, ~sqrt x)", Bdir),
                ("A2' c-Richtung (dc/d delta_nu)", Cdir), ("    N-hat(pi/6-x) - N-hat(pi/6)", Nx - N0), ("    Einheit 1", np.eye(3))):
    print(f"  {name:52s}: {np.round(W_major(M), 12)}")
print("\nDirac-Regel (j-i) fuer die geladenen Richtungen DIRS: [W0, W1, W2]")
for n, D in DIRS.items():
    print(f"  {n:5s}: {np.round(W_dirac(D), 12)}")
print("\nGegenprobe Majorana mit Konjugations-Regel (j-i):")
for name, M in (("N-hat(pi/6)", N0), ("b-Richtung", Bdir), ("c-Richtung", Cdir)):
    print(f"  {name:12s}: {np.round(W_conj(M), 12)}")

v0 = np.array([1, 0, 1]) / r2
a = Tb.conj().T @ v0
print(f"\nNur Bericht: v0 in der Ladungsbasis: |Komponenten|^2 = {np.round(abs(a)**2, 6)}")
# Projektion auf Klasse 0 und Mischung
M0 = Tb.T @ N0 @ Tb
P0 = np.array([[M0[i, j] if (i + j) % 3 == 0 else 0 for j in range(3)] for i in range(3)])
Nproj = np.real_if_close(np.linalg.inv(Tb.T) @ P0 @ np.linalg.inv(Tb))
print(f"Nur Bericht: Klasse-0-Projektion von N-hat(pi/6) zurueck in der Flavourbasis (reell: {np.allclose(np.imag(Nproj),0)}):\n", np.round(np.real(Nproj), 6))
Ue = eig_sorted(C(1.0, ns["DSTAR"] + 2 * np.pi / 3))[1]
for name, N in (("N-hat(pi/6)", N0), ("Klasse-0-Projektion", np.real(Nproj))):
    print(f"  PMNS mit {name:20s}: s12, s23, s13, sin d = {np.round(pmns(Ue, eig_sorted(N)[1]), 6)}")

rng = np.random.default_rng(460)
ws = []; wd = []
for _ in range(10000):
    A = rng.normal(size=(3, 3)); S = A + A.T; ws.append(W_major(S)[0])
    B = rng.normal(size=(3, 3)); K = 1j * (B - B.T); wd.append(W_dirac(K)[0])
ws = np.array(ws); wd = np.array(wd)
print(f"\nZufallskontrolle: symmetrisch (Majorana): W0 >= 1-1e-6 in {np.sum(ws >= 1-1e-6)}/10000, mittleres W0 = {ws.mean():.4f};"
      f"  antisymmetrisch (Dirac): W0 <= 1e-6 in {np.sum(wd <= 1e-6)}/10000, mittleres W0 = {wd.mean():.4f}")
a1 = W_major(N0)[0] >= 1 - 1e-12; a2 = W_major(Bdir)[0] <= 1e-12
print("\n" + "=" * 96)
print(f"A1 Baum geschlossen: {a1};  A2 fuehrende Versatzrichtung rein geladen: {a2};  A3 W0(K2) = {W_dirac(DIRS['K-2'])[0]:.1e}")
