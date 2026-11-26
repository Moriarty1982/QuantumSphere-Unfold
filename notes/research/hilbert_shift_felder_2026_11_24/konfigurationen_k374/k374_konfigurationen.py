"""k374 (Erkundung, NICHT BLIND, 26.11.2026): noetige Konfiguration je Sektor (Massen und Mischungen), zum Vergleich nebeneinander.
Auftrag des Autors: erst je Teil das System justieren, dann ansehen, welche Konfigurationen gesetzt sein muessen und wie sie zusammenhaengen; HS-Stufe beachten.
Alles hier ist angepasst, nicht hergeleitet. Aufruf aus diesem Ordner: python3 -u k374_konfigurationen.py > k374_out.txt
"""
import sys
import numpy as np
from scipy.optimize import least_squares, minimize, brentq
sys.path.insert(0, "../mischung_h175")
import k371_test_h175 as K
r2 = np.sqrt(2)
T = np.array([[0, 0, 1], [-1, 0, 0], [0, -1, 0]], float); T2 = T @ T
C = K.C
names = list(K.DIRS); D = [K.DIRS[n] for n in names]

MASS = {  # MeV; Quarks bei M_Z wie k367 (delta_h172), Leptonen Polmassen
    "e (geladene Leptonen)": [0.51099895, 105.6583755, 1776.93],
    "d (Down-Quarks, M_Z)": [1.54e-2, 3.06e-1, 16.30],
    "u (Up-Quarks, M_Z)": [7.04e-3, 3.56, 967.0],
}


def brannen(m):
    s = np.sqrt(np.array(m)); a = s.sum() / 3
    rho2 = 2 * (np.sum(s**2) / (3 * a**2) - 1)       # Summe lambda^2 = 3 a^2 (1 + rho^2/... ) -> K = (1 + rho^2)/3
    Kk = np.sum(s**2) / s.sum()**2
    rho = np.sqrt(3 * Kk - 1)
    lam = s / a
    # delta aus cos(3 delta): Produkt bzw. direkt aus groesstem Eigenwert
    d = np.arccos(np.clip((lam[2] - 1) / (r2 * rho), -1, 1))
    return Kk, rho, d, lam


print("== 1. Massen je Sektor: Brannen-Form lambda_k = 1 + sqrt2 rho cos(delta + 2 pi k/3), K = (1 + rho^2)/3 ==")
print("   Sektor | K | rho | delta (gefaltet) | Polwinkel theta mit K = 1/(3 cos^2 theta) | naechster Baumwert n*pi/12 und Abstand")
CONF = {}
for nm, m in MASS.items():
    Kk, rho, d, lam = brannen(m)
    chk = np.sort(abs(np.array([1 + r2 * rho * np.cos(d + 2 * np.pi * k / 3) for k in range(3)])))
    th = np.degrees(np.arccos(np.sqrt(1 / (3 * Kk))))
    n = int(round(d / (np.pi / 12)))
    CONF[nm] = (rho, d, lam)
    print(f"   {nm} | {Kk:.5f} | {rho:.5f} | {d:.6f} | {th:.2f} Grad | {n}*pi/12, Abstand {d - n*np.pi/12:+.5f}; Kontrolle {np.max(abs(chk - np.sort(lam))):.1e}")
R_OBS = 0.030016
def Rr(d, rho=1.0):
    m = np.sort(np.array([1 + r2 * rho * np.cos(d + 2 * np.pi * k / 3) for k in range(3)])**2)
    return (m[1]**2 - m[0]**2) / (m[2]**2 - m[0]**2)
xR = brentq(lambda x: Rr(np.pi / 6 - x) - R_OBS, 0.01, 0.1)
print(f"   nu (Neutrinos; nur R bekannt) | K = 2/3 gesetzt | 1 | {np.pi/6 - xR:.6f} (aus R) bzw. {np.pi/6 - 0.04478:.6f} (H176) | 45.00 Grad | 2*pi/12, Abstand {-xR:+.5f} bzw. -0.04478")
print("   Hinweis: K und delta der Quarks haengen von der Skala ab (H172: K_u 0,888 bei M_Z, 0,849 bei PDG-Skalen; K_d 0,748 / 0,731).")

print("\n== 2. Mischungen: Baumwert und kleinster Z3-brechender Term (direkte Konstruktion, Massen exakt) ==")
print("Verfahren: Zielmatrix V vorgeben; U = U_Baum-Partner * V (bis auf freie Phasen); M = U diag(lambda) U^+; nicht zirkulanter Anteil = M minus Z3-Mittel.")
print("Norm = Frobenius-Norm des nicht zirkulanten Anteils in Einheiten der mittleren Diagonale (a = 1); minimiert ueber die freien Phasen.")
A = np.array([[0, 0, -1], [0, 1, 0], [-1, 0, 0]], float)
w3 = np.exp(2j * np.pi / 3)
tv, tvec = np.linalg.eig(T)


def Fmat(order):
    o = [int(np.argmin(abs(tv - t))) for t in order]
    return tvec[:, o]


def std(s12, s23, s13, dl):
    c12, c23, c13 = np.sqrt(1 - s12**2), np.sqrt(1 - s23**2), np.sqrt(1 - s13**2)
    e = np.exp(1j * dl)
    return np.array([[c12 * c13, s12 * c13, s13 / e],
                     [-s12 * c23 - c12 * s23 * s13 * e, c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
                     [s12 * s23 - c12 * c23 * s13 * e, -c12 * s23 - s12 * c23 * s13 * e, c23 * c13]])


def parts(M):
    circ = (M + T @ M @ T.T + T2 @ M @ T2.T) / 3
    nc = M - circ
    S, Kp = nc.real, nc.imag
    Se, So = (S + A.T @ S @ A) / 2, (S - A.T @ S @ A) / 2
    Ke, Ko = (Kp + A.T @ Kp @ A) / 2, (Kp - A.T @ Kp @ A) / 2
    n2 = np.linalg.norm(nc)**2
    fr = [np.linalg.norm(X)**2 / n2 if n2 > 0 else 0 for X in (Se, So, Ke, Ko)]
    Kk, rho, d, lam = brannen_lam(np.linalg.eigvalsh(circ))
    return np.linalg.norm(nc), fr, rho, d


def brannen_lam(l):
    l = np.sort(abs(l)) if False else np.array(l); a = l.sum() / 3; l = l / a
    rho = np.sqrt(np.sum((l - 1)**2) / 3 * 2) / r2 * r2 / r2 * r2      # sum (l-1)^2 = 3 rho^2
    rho = np.sqrt(np.sum((l - 1)**2) / 3)
    d = np.arccos(np.clip((l.max() - 1) / (r2 * rho), -1, 1))
    return (1 + rho**2) / 3, rho, d, l


def lam_of(nm):
    rho, d, lam = CONF[nm]
    return np.sort(lam)            # e, mu, tau bzw. leicht -> schwer (alle positiv)


def minimal(build, nph, label):
    best = None
    rng_ = np.random.default_rng(1)
    for trial in range(40):
        r = minimize(lambda p: parts(build(p))[0], rng_.uniform(0, 2 * np.pi, nph), method='Nelder-Mead', options={'xatol': 1e-9, 'fatol': 1e-12, 'maxiter': 6000})
        if best is None or r.fun < best.fun - 1e-10: best = r
    nrm, fr, rho, d = parts(build(best.x))
    print(f"   {label}: Norm {nrm:.4f}; Anteile S A-gerade {fr[0]:.3f}, S A-ungerade {fr[1]:.3f}, K A-gerade {fr[2]:.3f}, K A-ungerade {fr[3]:.3f} (reell {fr[0]+fr[1]:.3f}, imaginaer {fr[2]+fr[3]:.3f}); zirkulanter Teil: rho = {rho:.5f}, delta = {d:.5f}; Phasen {np.round(np.mod(best.x, 2*np.pi), 3).tolist()}")
    return nrm, fr, rho, d, best.x


F1 = Fmat((1, w3, np.conj(w3)))
# --- CKM ---
VUS, VCB, VUB, DCKM = 0.2250, 0.0418, 0.00373, 1.14      # aus Vorwissen (PDG-Groessenordnung), nicht aus dem Repo
Vckm = std(VUS, VCB, VUB, DCKM)
print(f"CKM-Ziel (aus Vorwissen): s12 = {VUS}, s23 = {VCB}, s13 = {VUB}, delta = {DCKM}. Baumwert: beide Sektoren zirkulant in derselben Basis, V = 1.")
lu, ld = lam_of("u (Up-Quarks, M_Z)"), lam_of("d (Down-Quarks, M_Z)")
ph = lambda a, b: np.diag([1, np.exp(1j * a), np.exp(1j * b)])
# Brechung im Down-Sektor: U_d = F Phi V ; im Up-Sektor: U_u = F Phi V^+
r_d = minimal(lambda p: (F1 @ ph(*p) @ Vckm) @ np.diag(ld) @ (F1 @ ph(*p) @ Vckm).conj().T, 2, "CKM, Brechung nur im Down-Sektor")
r_u = minimal(lambda p: (F1 @ ph(*p) @ Vckm.conj().T) @ np.diag(lu) @ (F1 @ ph(*p) @ Vckm.conj().T).conj().T, 2, "CKM, Brechung nur im Up-Sektor")
# nur Cabibbo-Winkel
V12 = std(VUS, 0, 0, 0)
minimal(lambda p: (F1 @ ph(*p) @ V12) @ np.diag(ld) @ (F1 @ ph(*p) @ V12).conj().T, 2, "nur Cabibbo-Winkel, Down-Sektor")
print(f"   zum Vergleich: theta*(lambda_j - lambda_i) Down: 12: {VUS*(ld[1]-ld[0]):.4f}, 23: {VCB*(ld[2]-ld[1]):.4f}, 13: {VUB*(ld[2]-ld[0]):.4f}; Up: 12: {VUS*(lu[1]-lu[0]):.4f}, 23: {VCB*(lu[2]-lu[1]):.4f}, 13: {VUB*(lu[2]-lu[0]):.4f}")
print(f"   lambda Down {np.round(ld, 4).tolist()}, Up {np.round(lu, 4).tolist()}")
# --- PMNS ---
le = lam_of("e (geladene Leptonen)")
for lab, x in (("x_R", xR), ("x = 0,04478 (H176)", 0.04478), ("Baumwert der Neutrinos (x = 0, tribimaximal)", 0.0)):
    Un = K.eig_sorted(K.Nhat(np.pi / 6 - x, 1))[1]
    S13, S12, S23 = 0.02248, 0.3036, 0.470
    def build(p):
        V = std(np.sqrt(S12), np.sqrt(S23), np.sqrt(S13), p[0]) @ np.diag([1, np.exp(1j * p[1]), np.exp(1j * p[2])])
        Ue = Un @ V.conj().T
        return Ue @ np.diag(le) @ Ue.conj().T
    minimal(build, 3, f"PMNS, Brechung nur bei den geladenen Leptonen, Neutrinos bei {lab} (freie Phasen: delta_CP, zwei Majorana-Phasen)")
    for dfix in (np.pi / 2, -np.pi / 2):
        def build2(p, dfix=dfix):
            V = std(np.sqrt(S12), np.sqrt(S23), np.sqrt(S13), dfix) @ np.diag([1, np.exp(1j * p[0]), np.exp(1j * p[1])])
            Ue = Un @ V.conj().T
            return Ue @ np.diag(le) @ Ue.conj().T
        minimal(build2, 2, f"      dasselbe mit delta_CP = {'+' if dfix > 0 else '-'}90 Grad fest")
print("   Hinweis: Diese Norm ist die Frobenius-Norm (Nebendiagonalen zaehlen doppelt) und deshalb nicht direkt die Koeffizienten-Norm aus k372.")

print("\n== 3. Zahlkoerper je HS-Stufe: wie viele Eingaben gibt es ueberhaupt? ==")
print("   Stufe | Algebra | Dimension | hermitesche 3x3-Formen | davon zirkulant (a + z S + z* S^2) | Z3-brechend | imaginaere antisymmetrische Richtungen")
for n, alg in enumerate(["R", "C", "H", "O"]):
    dA = 2**n; herm = 3 + 3 * dA; circ = 1 + dA
    print(f"   HS({n}) | {alg} | {dA} | {herm} | {circ} | {herm - circ} | {3*(dA - 1)}")
print("   Reelle zirkulante Form (HS(0)): z reell, also delta = 0 oder pi (gefaltet 0 bzw. pi/3); jede andere Phase braucht mindestens C.")
