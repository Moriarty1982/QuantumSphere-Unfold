"""k376 (Erkundung, nicht blind): Quarks einzeln justieren. Welche Eingabe schiebt K von 2/3 weg, und zieht sie delta mit?
Aufruf: python k376_quarks_justieren.py > k376_out.txt"""
import numpy as np
from scipy.optimize import least_squares
from scipy.stats import ortho_group

rng = np.random.default_rng(20261126)
w = np.exp(2j * np.pi / 3); kk = np.arange(3); NMC = 100_000
F = np.array([[w**(j * k) for k in range(3)] for j in range(3)]) / np.sqrt(3)     # Fourier-Basis (Eigenvektoren jeder zirkulanten Form)

def cfg(m):
    """Brannen-Zerlegung von sqrt(m): K, rho, delta (gefaltet), Polwinkel theta in Grad."""
    v = np.sqrt(m); c = np.sum(v * np.conj(w**kk), axis=-1)
    d = np.mod(np.angle(c), 2 * np.pi / 3); d = np.minimum(d, 2 * np.pi / 3 - d)
    K = np.sum(m, axis=-1) / np.sum(v, axis=-1)**2
    rho = np.sqrt(3 * K - 1)
    return K, rho, d, np.degrees(np.arctan(rho))
sect = {
    "e": [(0.51099895e-3, 1.5e-13), (105.6583755e-3, 2.3e-9), (1776.93e-3, 0.09e-3)],
    "d": [(1.54e-5, 0.02e-5), (3.06e-4, 0.04e-4), (1.630e-2, 0.009e-2)],
    "u": [(7.04e-6, 0.15e-6), (3.56e-3, 0.06e-3), (0.967, 0.004)],
}
def run(typ, I):   # Top-Yukawa-Laufen aus k375: leichte zwei relativ zur schwersten
    f = {"e": 1.0, "d": np.exp(I), "u": np.exp(-I)}[typ]
    mu = np.array([a for a, _ in sect[typ]]); sd = np.array([b for _, b in sect[typ]])
    sam = np.sort(np.clip(rng.normal(mu, sd, size=(NMC, 3)), 1e-30, None), axis=1)
    g = np.array([f, f, 1.0])
    c0 = cfg(mu * g); cs = cfg(sam * g)
    return c0, [x.std() for x in cs]

print("== 1. Konfiguration je geladenem Sektor bei M_Z und an der Planck-Skala (I = 0 bzw. 0,1337) ==")
print("   Sektor | I | K | rho = tan(theta) | theta [Grad] | theta - 45 | delta")
T = {}
for typ in "edu":
    for I in (0.0, 0.13365):
        if typ == "e" and I > 0: continue
        (K, rho, d, th), (sK, sr, sd_, sth) = run(typ, I)
        T[(typ, I)] = (K, rho, d, th, sK, sr, sd_, sth)
        print(f"   {typ} | {I:.4f} | {K:.5f} +- {sK:.5f} | {rho:.5f} +- {sr:.5f} | {th:.3f} +- {sth:.3f} | {th-45:+.3f} | {d:.6f} +- {sd_:.6f}")
print("   Lesart: K = (1 + rho^2)/3. K = 2/3 heisst rho = 1, theta = 45 Grad (Fixpunkt des Frame-Tauschs J, H149).")

print("\n== 2. Zwei Wege zu K != 2/3 ==")
print("Weg A (zirkulant, Z3 bleibt, J gebrochen): rho != 1. Nur K bewegt sich, delta und Mischung bleiben. Noetig: rho - 1 =",
      ", ".join(f"{t}: {T[(t,0.0)][1]-1:+.4f}" for t in "du"))
print("Weg B (J bleibt im Baumwert, Z3 gebrochen): M = C(rho = 1, delta0) + B, B ohne zirkulanten Anteil (Diagonale in der Fourier-Basis null).")
print("   Exakt: ||B||_F^2 = Sum mu_i^2 - Sum lambda0_i^2 = 3 (rho_q^2 - 1) = 9 K - 6, unabhaengig von delta0 und von der Drehung.")
for typ in "du":
    K, rho = T[(typ, 0.0)][:2]
    print(f"   {typ}: ||B|| = sqrt(9K - 6) = {np.sqrt(9*K-6):.4f} (zum Vergleich: fuer die ganze CKM-Matrix reichen 0,157 bis 0,166; k374)")
def lam(rho, d): return 1 + np.sqrt(2) * rho * np.cos(d + 2 * np.pi * kk / 3)
def Uof(p):
    a, b, c, f1, f2, f3 = p
    def R(i, j, t, ph):
        M = np.eye(3, dtype=complex); M[i, i] = M[j, j] = np.cos(t); M[i, j] = np.sin(t) * np.exp(1j * ph); M[j, i] = -np.sin(t) * np.exp(-1j * ph); return M
    return R(0, 1, a, f1) @ R(0, 2, b, f2) @ R(1, 2, c, f3)
print("   Numerische Probe und noetige Drehung (kleinste groesste Drehung aus 200 Starts; Winkel zwischen Masse- und Fourier-Basis):")
for typ in "du":
    K, rho, d = T[(typ, 0.0)][:3]
    mu = np.sort(lam(rho, d))
    for name, d0 in (("delta0 = eigenes delta", d), ("delta0 = pi/12", np.pi / 12), ("delta0 = 0", 0.0)):
        l0 = np.sort(lam(1.0, d0))
        major = (mu[2] >= l0[2] - 1e-12) and (mu[0] <= l0[0] + 1e-12)
        best = None
        for _ in range(200):
            r = least_squares(lambda p: np.real(np.einsum('ij,j,ij->i', Uof(p), mu, np.conj(Uof(p)))) - l0, rng.uniform(-0.6, 0.6, 6) * np.array([1, 1, 1, 5, 5, 5]), xtol=1e-14, ftol=1e-14)
            if np.abs(r.fun).max() < 1e-9:
                U = Uof(r.x); off = np.abs(U) - np.eye(3)
                ang = np.degrees(np.arcsin(np.clip(np.abs(np.array([U[0, 1], U[1, 2], U[0, 2]])), 0, 1)))
                if best is None or ang.max() < best[0].max(): best = (ang, np.linalg.norm(U @ np.diag(mu) @ U.conj().T - np.diag(l0)))
        if best: print(f"   {typ}, {name}: loesbar (Schur-Horn {'ja' if major else 'nein'}); ||B|| numerisch {best[1]:.4f}; Drehwinkel 12/23/13 = {best[0][0]:.1f} / {best[0][1]:.1f} / {best[0][2]:.1f} Grad")
        else: print(f"   {typ}, {name}: keine Loesung gefunden (Schur-Horn {'ja' if major else 'nein'})")
print("   CKM zum Vergleich: 13,0 / 2,4 / 0,2 Grad. Weg B braeuchte also in beiden Sektoren fast dieselbe grosse Drehung, die sich in V = U_u^+ U_d aufhebt.")

print("\n== 3. Haengen J-Bruch (theta - 45) und delta zusammen? (nachtraeglich, Zahlenvergleich, kein Test) ==")
for I in (0.0, 0.13365):
    d_ = T[("d", I)]; u_ = T[("u", I)]
    a_d, a_u = np.radians(d_[3] - 45), np.radians(u_[3] - 45)
    print(f"   I = {I:.4f}: (theta-45)_u/(theta-45)_d = {a_u/a_d:.3f}; (rho-1)_u/(rho-1)_d = {(u_[1]-1)/(d_[1]-1):.3f}; (K-2/3)_u/(K-2/3)_d = {(u_[0]-2/3)/(d_[0]-2/3):.3f}; delta_d/delta_u = {d_[2]/u_[2]:.3f}; "
          f"Produkt (theta-45)*delta: d {a_d*d_[2]:.5f}, u {a_u*u_[2]:.5f}")
print("   Einfache Brueche fuer K (nachtraeglich): ", end="")
for typ, fr, nm in (("d", 3/4, "3/4"), ("u", 8/9, "8/9")):
    z = [(T[(typ, I)][0] - fr) / T[(typ, I)][4] for I in (0.0, 0.13365)]
    print(f"K_{typ} gegen {nm}: z = {z[0]:+.1f} (M_Z), {z[1]:+.1f} (Planck); ", end="")
print("\n   Einordnung: Brueche mit Nenner bis 12 liegen im Bereich 0,70 bis 0,92 im Mittel 0,008 auseinander; bei Fehler 0,001 trifft ein beliebiger Wert mit etwa 50 % einen davon auf 2 sigma.")
