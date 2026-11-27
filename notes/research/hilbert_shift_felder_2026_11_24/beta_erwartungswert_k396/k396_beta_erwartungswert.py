"""k396 (Erkundung, kein Test): Kann beta_sym ein Erwartungswert sein, der leicht von 1/2 abweicht?
Aufruf: python k396_beta_erwartungswert.py   (keine Eingabedateien)"""
import numpy as np
from scipy.optimize import brentq
from qiskit.quantum_info import DensityMatrix, Operator, Pauli
from qiskit import QuantumCircuit

K = np.arange(1, 400)
aC = np.sqrt(K * (K + 2) / 3.0)      # Casimir-Flaeche, 1 Bit bei j = 1/2 (r67)
aH = (K + 1) / 2.0                   # Flaeche j + 1/2, gleich normiert
def gam(a): return brentq(lambda g: np.sum(2.0 ** (1 - g * a)) - 1, 1.01, 5)
def beta(g): return np.sqrt((g - 1) / (g + 1))
gL, gH = gam(aC), gam(aH)
print("== Teil 1: Welche Groesse liegt nahe 1/2? ==")
print(f"   Zaehlregel (r67): Summe_k 2^(1 - gamma a_k) = 1.  Casimir: gamma_L = {gL:.10f}, beta_sym = {beta(gL):.10f}.  Flaeche j+1/2: gamma = {gH:.10f}, beta = {beta(gH):.10f}")
rows = [("b_C = 1/gamma (Erwartungswert der HC-Messung, <sigma_x>)", 1 / gH, 1 / gL),
        ("p_1 = 2^(1-gamma) (Anteil der Spin-1/2-Durchstosspunkte)", 2 ** (1 - gH), 2 ** (1 - gL)),
        ("beta = sqrt((gamma-1)/(gamma+1))", beta(gH), beta(gL)),
        ("x = beta^2 (Gewichtsverhaeltnis)", beta(gH) ** 2, beta(gL) ** 2),
        ("p_+ = (1 + 1/gamma)/2 (Wahrscheinlichkeit HC-Ausgang +)", (1 + 1 / gH) / 2, (1 + 1 / gL) / 2)]
print(f"   {'Groesse':58s} {'glatt (j+1/2)':>14s} {'Casimir':>12s} {'Abstand':>10s}")
for n, h, c in rows: print(f"   {n:58s} {h:14.7f} {c:12.7f} {c - h:+10.7f}")
print(f"   beta_sym - 1/2 = {beta(gL) - 0.5:+.7f}; beta_sym - 1/sqrt(3) = {beta(gL) - 1 / np.sqrt(3):+.7f}")
print("   Befund: Glatt 1/2 sind im Vergleichsfall (Flaeche j+1/2, zugleich Fixpunkt der Schleife L3 aus k395) der Erwartungswert 1/gamma und der Anteil p_1,")
print("   nicht beta. Der glatte Wert von beta ist 1/sqrt(3).")

print("\n== Teil 2: Die Abweichung von 1/2 als Erwartungswert (innerhalb der Zaehlregel hergeleitet) ==")
pH = 2.0 ** (1 - gH * aH); pC = 2.0 ** (1 - gL * aC)
print(f"   Verteilung der Spins k = 2j: glatt p_k = 2^-k: {np.round(pH[:5], 5)}; Casimir: {np.round(pC[:5], 5)}; Summen {pH.sum():.12f}, {pC.sum():.12f}")
d = aC - aH
print(f"   Flaechenueberschuss a_C - a_H fuer k = 1..6: {np.round(d[:6], 5)} (null bei j = 1/2, waechst mit dem Spin)")
lin = -gH * np.sum(pH * d) / np.sum(pH * aH)
print(f"   erste Ordnung: delta gamma = -gamma <delta a>/<a> = {lin:+.6f}  (<delta a> = {np.sum(pH * d):.6f}, <a> = {np.sum(pH * aH):.6f}); voll: {gL - gH:+.6f}")
print(f"   also 1/gamma - 1/2: erste Ordnung {-lin / gH**2:+.6f}, voll {1 / gL - 0.5:+.6f}")
# exakte Mittelwertform: gamma_L = Loesung; Interpolation a(t)
ts = np.linspace(0, 1, 6); print("   Interpolation a(t) = (1-t) a_H + t a_C:  t, gamma, 1/gamma, beta:")
for t in ts:
    g = gam((1 - t) * aH + t * aC); print(f"      {t:.1f}  {g:.7f}  {1 / g:.7f}  {beta(g):.7f}")
print("   Befund: Die Abweichung von 1/2 ist ein Mittelwert: der mittlere Flaechenueberschuss der hoeheren Spins (j >= 1), gewichtet mit ihrer Haeufigkeit.")
print("   Spin 1/2 allein gaebe exakt 1/2; die selteneren hoeheren Spins (zusammen 45 % der Durchstosspunkte) verschieben den Wert. Das ist die Zaehlregel, anders gelesen.")
for kmax in (1, 2, 3, 4, 6, 10, 400):
    kk = np.arange(1, kmax + 1); a = np.where(kk <= kmax, np.sqrt(kk * (kk + 2) / 3.0), 0)
    # hoehere Spins > kmax glatt lassen
    full = aH.copy(); full[:len(kk)] = a[:len(full[:len(kk)])]
    g = gam(full); print(f"      Casimir nur bis k = {kmax:3d}, darueber glatt: 1/gamma = {1 / g:.7f}, beta = {beta(g):.7f}")

print("\n== Teil 3: Schleife L3 (k395) mit kleinen Stoerungen: welche Eingabe verschiebt den Fixpunkt 1/2 wohin? ==")
def fix(step, b0=0.6, s0=0.0, n=4000):
    b, s = b0, s0
    for _ in range(n): b, s = step(b, s)
    return b
def make(res=1.0, mem=0.0, kap=0.0, lam=0.0, eta=1.0):
    """res: Polarisation des frischen Bands; mem: Anteil der letzten Ausgabe im Reservoir; kap: tan^2 alpha = x(1+kap);
    lam: x = (1-b)/(1+b) (1+lam); eta: Staerke der HC-Messung (1 = voll, loescht b_S ganz)"""
    def step(b, s):
        r = np.hypot(b, s); x = min(1.0, (1 - r) / (1 + r) * (1 + lam)) if eta < 1 else min(1.0, (1 - b) / (1 + b) * (1 + lam))
        al = np.arctan(np.sqrt(x * (1 + kap))); c, sn = np.cos(2 * al), np.sin(2 * al)
        b2, s2 = c * b - sn * s, sn * b + c * s
        s2 *= (1 - eta)
        R = res * (1 - mem) + mem * b
        return (1 - x) * b2 + x * R, (1 - x) * s2
    return step
target = 1 / gL
print(f"   ungestoert: Fixpunkt {fix(make()):.7f}; Ziel 1/gamma_L = {target:.7f}")
knobs = {"res (Reservoir unrein, 1 - eps)": ("res", [0.99, 0.95, 0.9], (0.5, 1.0)),
         "mem (Reservoir enthaelt Anteil m der letzten Ausgabe)": ("mem", [0.05, 0.1, 0.2, -0.1, -0.2], (-0.6, 0.6)),
         "kap (Drehwinkel-Regel tan^2 alpha = x (1 + kap))": ("kap", [-0.1, -0.05, 0.05, 0.1], (-0.9, 0.9)),
         "lam (Staerke-Regel x = (1-b)/(1+b) (1 + lam))": ("lam", [-0.1, -0.05, 0.05, 0.1], (-0.9, 0.9)),
         "eta (HC-Messung nur mit Staerke eta)": ("eta", [0.99, 0.9, 0.7, 0.5], (0.05, 1.0))}
for name, (key, vals, br) in knobs.items():
    out = "  ".join(f"{v:+.2f}: {fix(make(**{key: v})):.5f}" for v in vals)
    g = lambda v: fix(make(**{key: v})) - target
    try:
        lo, hi = br; grid = np.linspace(lo, hi, 61); gv = [g(v) for v in grid]; root = None
        for i in range(60):
            if np.isfinite(gv[i]) and np.isfinite(gv[i + 1]) and gv[i] * gv[i + 1] < 0: root = brentq(g, grid[i], grid[i + 1], xtol=1e-10); break
        need = f"trifft 1/gamma_L bei {key} = {root:+.5f}" if root is not None else "erreicht 1/gamma_L im Bereich nicht"
    except Exception as e: need = f"Fehler {e}"
    print(f"   {name}\n      Fixpunkt bei {out}\n      {need}")
print("   Lesart: Jede Stellgroesse ist eine Zahl fuer eine Zahl (angepasst, nichts hergeleitet). Die Tabelle sagt nur, in welche Richtung welche Stoerung zieht.")

print("\n== Teil 4: Restkorrelation gekoppelter Baender (Lorenz-artig), Qiskit ==")
def state(b):  # Bloch-Vektor (b, 0, 0)
    return DensityMatrix(0.5 * (np.eye(2) + b * np.array([[0, 1], [1, 0]])))
XX = Pauli("XX")
for b1, b2 in [(0.5, 0.5), (target, target), (0.2, 0.3)]:
    rho = state(b1).tensor(state(b2)); e = np.real(rho.expectation_value(XX)); print(f"   unabhaengige Baender b = ({b1:.4f}, {b2:.4f}): <X X> = {e:.6f} = Produkt {b1 * b2:.6f}; P(gleich) = {(1 + e) / 2:.6f}")
print("   (Das ist die Regel hinter Tuttes 1+2-Angriff: Korrelationen multiplizieren sich, kleine Abweichungen von 50 % ueberleben die Summe zweier Baender.)")
print("   Zwei Schleifen L3, deren Baender je Runde teilweise getauscht werden (Kopplung y) und deren Reservoir |+> ist:")
def partial_swap(th):
    S = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], complex); return Operator(np.cos(th) * np.eye(4) - 1j * np.sin(th) * S)
for y in (0.0, 0.1, 0.3):
    b = np.array([0.9, 0.2]); th = np.arcsin(np.sqrt(y))
    for _ in range(300):
        nb = []
        for bi in b:
            x = (1 - bi) / (1 + bi); nb.append((2 * bi ** 3 - bi + 1) / (1 + bi))
        rho = state(nb[0]).tensor(state(nb[1])).evolve(partial_swap(th))
        b = np.array([np.real(rho.expectation_value(Pauli("XI"))), np.real(rho.expectation_value(Pauli("IX")))]); exx = np.real(rho.expectation_value(XX))
    print(f"      y = {y:.1f}: Endwerte b = ({b[0]:.7f}, {b[1]:.7f}), <X X> = {exx:.7f} (Produkt {b[0] * b[1]:.7f})")
print("   Befund: Zwei gleiche gekoppelte Schleifen bleiben bei 1/2; der Tausch gleicher Zustaende erzeugt keine Restkorrelation. Eine Abweichung braucht ein Band,")
print("   das anders ist (andere Flaeche, anderer Spin). Genau das leistet in der Zaehlregel der Flaechenueberschuss der hoeheren Spins (Teil 2).")

print("\n== Teil 5: Nachtraegliche Beobachtung (kein Test) ==")
p1 = 2 ** (1 - gL); bs = beta(gL)
print(f"   p_1 = 2^(1 - gamma_L) = {p1:.7f}; beta_sym = {bs:.7f}; Unterschied {p1 - bs:+.7f} ({(p1 - bs) / bs * 100:+.3f} %). Im glatten Fall: p_1 = 0.5, beta = 0.57735 (dort NICHT gleich).")
print(f"   2-sigma-Fenster aus m_W (k358): beta in [0.54907, 0.54978]: p_1 liegt {'darin' if 0.54907 <= p1 <= 0.54978 else 'nicht darin'}.")
gs = brentq(lambda g: 2 ** (1 - g) - beta(g), 1.5, 2.5); print(f"   Beide gleich waeren sie bei gamma = {gs:.7f} (beta = {beta(gs):.7f}); die Zaehlregel gibt {gL:.7f}.")
cands = {"1/gamma": 1 / gL, "p_1": p1, "p_+": (1 + 1 / gL) / 2, "x": bs ** 2, "1 - p_1": 1 - p1, "p_2/p_1": pC[1] / pC[0], "<a>/2": np.sum(pC * aC) / 2, "1/<a>": 1 / np.sum(pC * aC),
         "<k>/2 = <j>": np.sum(pC * K) / 2, "1/<k>": 1 / np.sum(pC * K), "Entropie/2 (bit)": -np.sum(pC * np.log2(pC)) / 2, "sqrt(2 p_2)": np.sqrt(pC[1] * 2), "1/(gamma ln 2)": 1 / (gL * np.log(2))}
print("   Durchgesehene einfache Kenngroessen der Spinverteilung (alle, nicht nur die naechste):")
for n, v in sorted(cands.items(), key=lambda t: abs(t[1] - bs)): print(f"      {n:34s} {v:.7f}  Abstand zu beta_sym {v - bs:+.7f}")
n = len(cands); win = abs(p1 - bs); span = 1.0
tc = brentq(lambda t: 2 ** (1 - gam((1 - t) * aH + t * aC)) - beta(gam((1 - t) * aH + t * aC)), 0.5, 1.5)
print(f"   Entlang der Interpolation aus Teil 2 schneiden sich p_1(t) und beta(t) bei t = {tc:.5f} (t = 1 ist die Casimir-Flaeche). Bei t gleichverteilt in [0, 2] laege ein Schnitt so nah an 1 mit {abs(tc - 1) * 100:.2f} %.")
print(f"   Grobe Zufallsabschaetzung: {n} Kenngroessen, Fenster +-{win:.5f} in einem Bereich der Breite ~{span:.0f}: Erwartung {n * 2 * win / span:.4f} Treffer. Selten, aber nachtraeglich gefunden.")
