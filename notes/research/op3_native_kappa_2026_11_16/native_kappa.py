"""OP3: native Kohaerenzfaktor kappa fuer die Querdephasierung um die Zyklusachse (Erkundung, NICHT BLIND).

Ziel (aus der Betrachter-Erkundung): kappa^2 = 0.880706, dann K = 2/3 exakt und phi = arctan(kappa^2/(2-kappa^2)) = 0.666665.
Der Zielwert ist bekannt, und jeder Kandidat ist im Kopf auswertbar; deshalb Erkundung ohne H-Nummer.  Liste vor dem Lauf festgelegt:

Strukturteil
 S1  Welche Kanaele dephasieren nur quer zur Zyklusachse?  (a) Zwirbeln mit n.sigma = (R+T+J_B)/sqrt3;  (b) gleichgewichtetes
     Mischen der drei Frame-Abbildungen (Pauli-Kanal);  (c) Mittel ueber den Generationszyklus (Drehung um n um 0, 2pi/3, 4pi/3).
 S2  Noetiger Winkel zwischen den zwei Aufzeichnungszustaenden des Betrachters: cos(theta) = 2 kappa^2 - 1.
Kandidaten aus dem Bestand (kappa bzw. kappa^2 aus einer nativen Groesse)
 N1  Dephasierung ueber N Frequenzen (r28.2(b)): kappa^2 = 1/N, N >= 2.
 N2  Sichtbarkeit |b| = 1/gamma_M (r03, r22) als kappa.
 N3  Zeitmittel ueber ein Drittel der Periode (r16.9) auf den Anteilen e^{+-2 i omega t}: kappa = sinc(pi/3).
 N4  Aufzeichnung o, F o (Betrachter ohne / mit Frame-Abbildung): kappa = |n.f| = 1/sqrt3.
 N5  Aufzeichnung in zwei Oktantenzustaenden: kappa = 1/sqrt2.
 N6  Autokorrelation nach einem Drittel der Periode bei Koide (r16.9(b)): kappa = 1/sqrt2 (wie N5, eigene Herkunft).
 N7  Kick-Lesart des C5-Faktors cos^2(pi/6) = 3/4 (r10): kappa^2 = 3/4 und kappa = 3/4.
 N8  Kompensator-Eigenwert p_+ (r17, Frame M): kappa = p_+ und kappa^2 = p_+.
 N9  Spin-1-Aufzeichnung: zwei Kopien je Aufzeichnung (r25), kappa = (Ueberlappung einer Kopie)^2 fuer N4 und N5.
"""
import numpy as np

T = 0.666665
K2_TARGET = 2 * np.tan(T) / (1 + np.tan(T))
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1]).astype(complex)
sig = lambda r: r[0] * X + r[1] * Y + r[2] * Z
n = np.ones(3) / np.sqrt(3)
E = [np.array(v, float) for v in ([0, 0, 1], [1, 0, 0], [0, 1, 0])]
bloch = lambda rho: np.real([np.trace(rho @ X), np.trace(rho @ Y), np.trace(rho @ Z)])
phase_of = lambda k2: np.arctan(k2 / (2 - k2))

print(f"Ziel: kappa^2 = {K2_TARGET:.6f}, kappa = {np.sqrt(K2_TARGET):.6f}")
e = E[0]; rho = (I2 + sig(e)) / 2; Zn = sig(n)
for name, ch in (
    ("S1a Zwirbeln mit n.sigma, p = 0.1", lambda r: 0.9 * r + 0.1 * Zn @ r @ Zn),
    ("S1b Frame-Abbildungen gleich gemischt, q = 0.05", lambda r: 0.85 * r + 0.05 * (X @ r @ X + Y @ r @ Y + Z @ r @ Z)),
    ("S1c Mittel ueber den Generationszyklus", None),
):
    if ch is None:
        th = 2 * np.pi / 3; U = np.cos(th / 2) * I2 - 1j * np.sin(th / 2) * Zn
        out = sum(np.linalg.matrix_power(U, j) @ rho @ np.linalg.matrix_power(U, j).conj().T for j in range(3)) / 3
    else:
        out = ch(rho)
    r = bloch(out); lon = r @ n; tr = np.linalg.norm(r - lon * n)
    print(f"{name}: Laengsanteil {lon:.4f} (vorher {e @ n:.4f}), Queranteil {tr:.4f} (vorher {np.linalg.norm(e - (e @ n) * n):.4f})")
print(f"S2 noetiger Winkel der Aufzeichnungszustaende: cos theta = {2 * K2_TARGET - 1:.6f}, theta = {np.degrees(np.arccos(2 * K2_TARGET - 1)):.3f} Grad")

x = None
gamma_M = 1.864  # r22-Tabelle; genauer aus beta_sym:
p_plus = 0.768
try:
    # gamma = (1+x)/(1-x) mit x = beta_sym^2; aus der r22-Tabelle p_+ = 1/(1+x) = 0.768 -> x
    x = 1 / p_plus - 1; gamma_M = (1 + x) / (1 - x)
except Exception:
    pass
cands = [
    ("N1 1/N, N = 2 (Obergrenze)", 0.5),
    ("N2 kappa = |b| = 1/gamma_M", (1 / gamma_M) ** 2),
    ("N3 kappa = sinc(pi/3)", (np.sin(np.pi / 3) / (np.pi / 3)) ** 2),
    ("N4 kappa = 1/sqrt3", 1 / 3),
    ("N5/N6 kappa = 1/sqrt2", 1 / 2),
    ("N7 kappa^2 = 3/4", 3 / 4),
    ("N7 kappa = 3/4", 9 / 16),
    ("N8 kappa = p_+", p_plus ** 2),
    ("N8 kappa^2 = p_+", p_plus),
    ("N9 kappa = (1/sqrt3)^2", 1 / 9),
    ("N9 kappa = (1/sqrt2)^2", 1 / 4),
]
print(f"Kandidaten (x = beta_sym^2 = {x:.4f} aus p_+ = {p_plus}, gamma_M = {gamma_M:.4f}):")
for name, k2 in cands:
    print(f"   {name:28s} kappa^2 = {k2:.6f}  phi = {phase_of(k2):.6f}  phi - Ziel = {phase_of(k2) - T:+.6f}")
