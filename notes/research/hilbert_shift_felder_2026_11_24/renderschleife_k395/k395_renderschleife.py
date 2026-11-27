"""k395 (Erkundung, nicht blind): Renderschleife durch den HC mit Selbstjustierung, Wechsel des Traegerbands mit Schranken,
Differenzen-Statistik nach Art des Lorenz-Angriffs. Qiskit (Dichtematrix) und numpy. Kein Test, keine Vorhersage.
Aufruf: python k395_renderschleife.py > k395_out.txt"""
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import DensityMatrix, Operator, Pauli, partial_trace
from scipy.linalg import expm
rng = np.random.default_rng(395)
gL = 1.8646997646; bsym = 0.5494056410; xs = bsym**2

print("== Teil 1: eine Runde der Schleife als Schaltung (Qiskit, Dichtematrix) ==")
print("   Runde: Drehung um den Winkel alpha (Bloch-Winkel 2 alpha, RY), HC nicht selektiv (Messung entlang sigma_x, Ergebnis verworfen),")
print("   Austausch (Teil-SWAP, Winkel theta) mit einem frischen Qubit im Bezugszustand |+>. Zustand der Schleife: b = <sigma_x>.")
def runde(rho, alpha, theta):
    """rho: DensityMatrix eines Qubits. Gibt den Zustand nach einer Runde zurueck (3 Qubits: System, HC-Hilfsqubit, Reservoir)."""
    qc = QuantumCircuit(3); qc.h(2)                                             # Reservoir |+>
    full = DensityMatrix.from_label("00").tensor(rho).evolve(qc)               # Reihenfolge: q0 = System
    qc2 = QuantumCircuit(3); qc2.ry(2 * alpha, 0); qc2.h(0); qc2.cx(0, 1); qc2.h(0)   # HC: sigma_x-Wert auf das Hilfsqubit kopieren (= nicht selektive Messung)
    full = full.evolve(qc2)
    sw = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex); U = np.cos(theta) * np.eye(4) + 1j * np.sin(theta) * sw
    full = full.evolve(Operator(U), qargs=[0, 2]); return partial_trace(full, [1, 2])
bx = lambda rho: float(np.real(rho.expectation_value(Pauli("X"))))
def start(b, bz=0.0): return DensityMatrix(0.5 * (np.eye(2) + b * np.array([[0, 1], [1, 0]]) + bz * np.array([[1, 0], [0, -1]])))
SG = 1; dv = 0
for _ in range(20):
    b0, bz0, al, th = rng.uniform(-0.6, 0.6), rng.uniform(-0.6, 0.6), rng.uniform(0, np.pi / 2), rng.uniform(0, np.pi / 2); sg = SG
    out = runde(start(b0, bz0), al, th); pred = np.cos(th)**2 * (np.cos(2 * al) * b0 + sg * np.sin(2 * al) * bz0) + np.sin(th)**2   # RY(2 alpha) dreht (b_x, b_z)
    dv = max(dv, abs(bx(out) - pred), abs(float(np.real(out.expectation_value(Pauli("Z"))))), abs(float(np.real(out.expectation_value(Pauli("Y"))))))
print(f"   Kontrolle (20 Zufallsfaelle): Schaltung gegen b' = cos^2(theta) (cos(2 alpha) b_x + sin(2 alpha) b_z) + sin^2(theta), b_z' = b_y' = 0: groesste Abweichung {dv:.1e}")
print("   Auf der HC-Achse (b_z = 0) ist die Runde also die Abbildung b' = (1 - x) cos(2 alpha) b + x mit x = sin^2(theta).")

print("\n== Teil 2: vier Arten, die Schleife zu schliessen ==")
def it(f, b0, n=60):
    b = b0; tr = [b]
    for _ in range(n): b = f(b); tr.append(b)
    return np.array(tr)
seeds = [0.02, 0.1, 0.3, 0.5, 0.7, 0.9, 0.98]                                # x = (1 - b)/(1 + b) ist nur fuer 0 <= b <= 1 eine Austauschstaerke
c6 = np.cos(np.pi / 3)
print("   L0 (r28.2(c), festes Reservoir, alpha = pi/6, x fest): Attraktor x / (1 - (1 - x) cos(2 alpha)), unabhaengig vom Start")
for x in (0.25, 1 / 3, xs): print(f"      x = {x:.5f}: Schleife {it(lambda b: (1 - x) * c6 * b + x, 0.9)[-1]:.6f}, Formel {x / (1 - (1 - x) * c6):.6f}")
print("   L1 (dasselbe Feld wird wieder eingespeist: das Reservoir ist die Ausgabe der letzten Runde): b' = ((1 - x) cos(2 alpha) + x) b")
print(f"      x = 1/3, alpha = pi/6: nach 60 Runden von b = 0.9 aus: {it(lambda b: ((1 - 1 / 3) * c6 + 1 / 3) * b, 0.9)[-1]:.2e} (laeuft gegen 0, den Lichtpunkt; wie r28.1(c))")
print("   L2 (Staerke justiert sich: x_n = (1 - b_n)/(1 + b_n), also b = 1/gamma und x = beta^2; alpha = pi/6 fest):")
f2 = lambda b: (1 - (1 - b) / (1 + b)) * c6 * b + (1 - b) / (1 + b)
print("      Endwerte aus den Startwerten " + str(seeds) + ": " + str(np.round([it(f2, s)[-1] for s in seeds], 8).tolist()))
print("   L3 (Staerke und Drehwinkel justieren sich: x_n wie L2, tan^2(alpha_n) = x_n; keine aeussere Zahl mehr):")
f3 = lambda b: (2 * b**3 - b + 1) / (1 + b)
print("      geschlossene Form b' = (2 b^3 - b + 1)/(1 + b); Fixpunkte aus (2b - 1)(b^2 - 1) = 0: b = 1/2 und b = 1; zulaessig ist 0 <= b <= 1")
print("      Endwerte aus den Startwerten " + str(seeds) + ": " + str(np.round([it(f3, s)[-1] for s in seeds], 10).tolist()))
h = 1e-6; d_half = (f3(0.5 + h) - f3(0.5 - h)) / (2 * h); d_one = (f3(1 + h) - f3(1 - h)) / (2 * h)
print(f"      Steigung am Fixpunkt b = 1/2: {d_half:.2e} (null: der Fixpunkt zieht quadratisch an); am Fixpunkt b = 1 (Ruheframe, reiner Zustand): {d_one:.4f} (> 1: instabil)")
tr = it(f3, 0.9, 8); print("      Verlauf von b = 0.9 aus: " + " ".join(f"{v:.10f}" for v in tr))
print("      Am Fixpunkt: b = 1/2, x = 1/3, gamma = 2, beta = 1/sqrt(3) = 0.57735, alpha = pi/6 (Hopf-Punkt; dieselbe Zahl wie die Zaehlregel mit Flaeche j + 1/2).")
print(f"      Gemessen/postuliert: 1/gamma_L = {1 / gL:.6f}, beta_sym = {bsym:.7f}, x = {xs:.6f}. Die Schleife L3 landet NICHT dort.")
# L3 mit Qiskit-Schaltung, Rueckkopplung aus der letzten Runde
rho = start(0.9); qs = [0.9]
for _ in range(8):
    b = bx(rho); x = (1 - b) / (1 + b); rho = runde(rho, np.arctan(np.sqrt(x)), np.arcsin(np.sqrt(x))); qs.append(bx(rho))
print("      dieselbe Schleife als Schaltung mit Rueckkopplung (Qiskit): " + " ".join(f"{v:.10f}" for v in qs) + f"; Abweichung zur Formel {np.abs(np.array(qs) - tr).max():.1e}")
print("   Differenzen (zwei Laeufe mit leicht verschiedener Stoerung, wie beim Vergleich zweier Klartexte):")
for nm, f in (("L2", f2), ("L3", f3)):
    a, b_ = it(f, 0.30, 6), it(f, 0.31, 6); print(f"      {nm}: |Unterschied| je Runde: " + " ".join(f"{abs(u - v):.1e}" for u, v in zip(a, b_)))
print("      Lesart: Unterschiede im Startwert werden geloescht statt verbreitet. Die Schleife vergisst den Ur-Seed; sie ist das Gegenteil einer Chiffre.")
al2 = 0.5 * np.arccos((1 - xs * gL) / (1 - xs))
print(f"   Angepasst (keine Herleitung): L2 landet bei 1/gamma_L, wenn der feste Drehwinkel alpha = {np.degrees(al2):.3f} Grad ist statt 30 Grad (2 alpha = {np.degrees(2 * al2):.3f}; zum Vergleich Hoehe von M: {np.degrees(np.arccos(1 / gL)):.3f}).")
f2b = lambda b: (1 - (1 - b) / (1 + b)) * np.cos(2 * al2) * b + (1 - b) / (1 + b); print(f"      Kontrolle: Endwert {it(f2b, 0.9, 200)[-1]:.7f} gegen 1/gamma_L = {1 / gL:.7f}")

print("\n== Teil 3: HC-Stufe als Wechsel des Traegerbands; Schranken durch Wiederholen (Qiskit, 2 Qubits = 4 Baender) ==")
print("   Baender |Farbe, Sektor>: nu = |0,0>, e = |0,1>, d = |1,0>, u = |1,1>. Anfangs ist jedes Band mit jedem verbunden (vollstaendiger Graph, H = Summe aller Uebergaenge).")
X = np.array([[0, 1], [1, 0]], dtype=complex); Z = np.diag([1.0, -1.0]).astype(complex); I2 = np.eye(2, dtype=complex)
H = np.kron(I2 + X, I2 + X) - np.eye(4)                                       # Reihenfolge: (Farbe, Sektor)
def schranke(rho, P):                                                          # nicht selektive Messung mit Projektoren P
    return sum(p @ rho @ p for p in P)
PZc = [np.kron(np.diag([1.0, 0]), I2), np.kron(np.diag([0, 1.0]), I2)]; PZs = [np.kron(I2, np.diag([1.0, 0])), np.kron(I2, np.diag([0, 1.0]))]
PXs = [np.kron(I2, (I2 + X) / 2), np.kron(I2, (I2 - X) / 2)]
names = ["nu", "e", "d", "u"]; Tt = 1.0
def lauf(N, schr, psi0=0):
    U = expm(-1j * H * Tt / N); rho = np.zeros((4, 4), dtype=complex); rho[psi0, psi0] = 1
    for _ in range(N):
        rho = U @ rho @ U.conj().T
        for P in schr: rho = schranke(rho, P)
    return DensityMatrix(rho)                                                  # Qiskit-Objekt fuer die Auswertung
for lab, schr in (("ohne Schranke", []), ("Schranke Farbe (Z auf dem Farb-Qubit)", [PZc]), ("Schranken Farbe und Sektor (Z, Z)", [PZc, PZs]), ("Schranke Farbe (Z) und HC auf dem Sektor (X)", [PZc, PXs])):
    print(f"   {lab}: Start auf Band nu, Gesamtzeit {Tt}; Aufenthalt (nu, e, d, u) nach N Wiederholungen")
    for N in (1, 4, 16, 64, 256, 1024):
        p = lauf(N, schr).probabilities(); print(f"      N = {N:5d}: " + " ".join(f"{v:.4f}" for v in p) + f"   (in die Quark-Baender: {p[2] + p[3]:.4f})")
r = lauf(1024, [PZc, PXs]).data; print(f"   HC als Schranke: Kohaerenz nu-e nach 1024 Runden = {abs(r[0, 1]):.4f}; Gewicht auf (nu + e)/sqrt(2): {np.real(0.5 * (r[0, 0] + r[1, 1] + r[0, 1] + r[1, 0])):.4f}, auf (nu - e)/sqrt(2): {np.real(0.5 * (r[0, 0] + r[1, 1] - r[0, 1] - r[1, 0])):.4f}")
print("   Lesart: Eine oft wiederholte Schranke loescht die Uebergaenge, die sie unterscheidet (Rate ~ 1/N). Der HC (Messung entlang sigma_x) unterscheidet die zwei")
print("   farblosen Baender nicht; er laesst ihren Uebergang offen und besetzt beide gleich stark. Das Ergebnis ist ein Gemisch zu gleichen Teilen, keine ausgewaehlte Ueberlagerung.")

print("\n== Teil 4: Differenzen nach Art des Lorenz-Angriffs auf die sechs Quarkmassen (nachtraeglich, kein Test) ==")
md = np.array([1.54e-5, 3.06e-4, 1.630e-2]); sd = np.array([0.02e-5, 0.04e-4, 0.009e-2]); mu = np.array([7.04e-6, 3.56e-3, 0.967]); su = np.array([0.15e-6, 0.06e-3, 0.004])
print("   Idee: Was beiden Sektoren gemeinsam ist (Skala, gemeinsame Funktion, Laufen der starken Kopplung), faellt in Delta_g = ln(m_u,g / m_d,g) heraus;")
print("   die zweite Differenz loescht zusaetzlich einen in g linearen Anteil.")
D = np.log(mu / md); sD = np.sqrt((su / mu)**2 + (sd / md)**2); d1, d2 = D[1] - D[0], D[2] - D[1]; s1, s2 = np.hypot(sD[1], sD[0]), np.hypot(sD[2], sD[1])
q = d1 / d2; sq = q * np.sqrt((sD[0] / d1)**2 + (sD[2] / d2)**2 + (sD[1] * (1 / d1 + 1 / d2))**2)
print(f"   Delta = {np.round(D, 4)} +- {np.round(sD, 4)}; erste Differenzen {d1:.4f} +- {s1:.4f}, {d2:.4f} +- {s2:.4f}; Verhaeltnis {q:.4f} +- {sq:.4f}")
lhs = (mu[1] / md[1])**3; rhs = (mu[0] / md[0]) * (mu[2] / md[2])**2
print(f"   Verhaeltnis 2 hiesse (m_c/m_s)^3 = (m_u/m_d) (m_t/m_b)^2: links {lhs:.1f}, rechts {rhs:.1f}, Abstand {(q - 2) / sq:+.2f} sigma")
NF = 20000; hit = 0; simple = np.array([1 / 3, 0.5, 1, 2, 3])
for _ in range(NF):
    fk = []
    for m in (mu, md):
        m2 = 10 ** rng.uniform(-3.5, -0.5); m1 = m2 * 10 ** rng.uniform(-3.5, -0.5); fk.append(np.array([m1, m2, 1.0]))
    Df = np.log(fk[0] / fk[1]); qf = (Df[1] - Df[0]) / (Df[2] - Df[1]) if Df[2] != Df[1] else np.inf; hit += np.any(np.abs(qf - simple) < max(abs(q - 2), sq))
print(f"   Zufall: {hit / NF:.2%} von {NF} erfundenen Datensaetzen haben ein Verhaeltnis so nah an einer der einfachen Zahlen 1/3, 1/2, 1, 2, 3 (Fenster {max(abs(q - 2), sq):.3f}).")
