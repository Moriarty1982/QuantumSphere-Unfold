"""k352 (Test H161, ueberwiegend nicht blind): Spinor als zweigeteilter Lesekopf, XOR-Rekonstruktion (RAID5), Verbiegung der Geometrie.
Vorab-Notiz: notes/research/predictions/Vorab_Notiz_H161_Spinor_Lesekopf_XOR.md
K-a Etiketten GF(2)^2;  K-b zwei Koepfe (Qiskit);  K-c ein Kopf (Qiskit);  K-d Peres-Mermin (Abzaehlung und Qiskit);  K-e Moebius/Lorentz
Bit 0 = Eigenwert +1, Bit 1 = Eigenwert -1.
Aufruf: python k352_test_h161.py > k352_out.txt
"""
import itertools
import numpy as np
import sympy as sp
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

SHOTS = 4096
sim = AerSimulator(seed_simulator=20261126)
rng = np.random.default_rng(20261126)
I2 = np.eye(2); X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1.0, -1.0]).astype(complex)
PAULI = {"I": I2, "X": X, "Y": Y, "Z": Z}
LABEL = {"I": (0, 0), "X": (1, 0), "Z": (0, 1), "Y": (1, 1)}
INV = {v: k for k, v in LABEL.items()}

print("== K-a  Etiketten: Pauli ohne Phase = GF(2)^2 ==")
ok = True
for p, q in itertools.product("IXYZ", repeat=2):
    lab = tuple((a + b) % 2 for a, b in zip(LABEL[p], LABEL[q]))
    prod = PAULI[p] @ PAULI[q]; tgt = PAULI[INV[lab]]
    ph = [c for c in (1, -1, 1j, -1j) if np.allclose(prod, c * tgt)]
    ok &= len(ph) == 1
print("  alle 16 Produkte P·Q sind bis auf eine Phase das Etikett (x|z)(P) XOR (x|z)(Q):", ok)
print("  X xor Z =", INV[(1, 1)], ";  X xor Y =", INV[(0, 1)], ";  Y xor Z =", INV[(1, 0)], " => je zwei der drei geben das dritte (wie RAID5 mit drei Platten)")
print("  Phasen: X·Z =", "-i·Y" if np.allclose(X @ Z, -1j * Y) else "?", ";  Z·X =", "+i·Y" if np.allclose(Z @ X, 1j * Y) else "?", " => das Etikett ist eindeutig, das Vorzeichen haengt an der Reihenfolge")

def measure_string(qc, string, data, anc, cl):
    """Paritaetsmessung eines Pauli-Strings ueber einen Hilfs-Qubit (zerstoerungsfrei)."""
    qc.h(anc)
    for ch, q in zip(string, data):
        if ch == "X": qc.cx(anc, q)
        elif ch == "Y": qc.cy(anc, q)
        elif ch == "Z": qc.cz(anc, q)
    qc.h(anc); qc.measure(anc, cl)

def counts_of(qc):
    return sim.run(transpile(qc, sim), shots=SHOTS).result().get_counts()

print("\n== K-b  zwei Koepfe: XX, ZZ, YY nacheinander (Qiskit, %d Laeufe je Zustand) ==" % SHOTS)
def bell(qc, kind):
    qc.h(0); qc.cx(0, 1)
    if kind in ("Phi-", "Psi-"): qc.z(0)
    if kind in ("Psi+", "Psi-"): qc.x(1)
def kb(prep, name):
    qc = QuantumCircuit(5, 3); prep(qc)
    for k, s in enumerate(("XX", "ZZ", "YY")): measure_string(qc, s, (0, 1), 2 + k, k)
    c = counts_of(qc)
    viol = {cc: 0 for cc in (0, 1)}; outs = {}
    for bits, n in c.items():
        yy, zz, xx = (int(b) for b in bits)                      # Qiskit: hoechstes Bit zuerst
        outs[(xx, zz, yy)] = outs.get((xx, zz, yy), 0) + n
        for cc in (0, 1): viol[cc] += n * (yy != (xx ^ zz ^ cc))
    c_fit = [cc for cc in (0, 1) if viol[cc] == 0]
    print(f"  {name:22s}: (xx, zz, yy) -> Anzahl {dict(sorted(outs.items()))};  yy = xx xor zz xor c fuer alle Laeufe mit c = {c_fit}")
    return c_fit
cs = [kb(lambda qc, k=k: bell(qc, k), "Bell " + k) for k in ("Phi+", "Phi-", "Psi+", "Psi-")]
def rand2(qc):
    for q in (0, 1): qc.u(*rng.uniform(0, 2 * np.pi, 3), q)
    qc.cx(0, 1)
    for q in (0, 1): qc.u(*rng.uniform(0, 2 * np.pi, 3), q)
cs += [kb(rand2, f"Zufallszustand {k + 1}") for k in range(3)]
print("  K-b: festes c in allen Faellen:", all(c == [1] for c in cs), " (c = 1: (XX)(ZZ) = -YY; die Paritaet der drei Platten ist immer ungerade)")
print("  Matrixprobe: (XX)(ZZ) + YY =", np.abs(np.kron(X, X) @ np.kron(Z, Z) + np.kron(Y, Y)).max())

print("\n== K-c  ein Kopf: X, dann Z, dann Y auf einem Qubit (Qiskit, 20 Zufallszustaende, %d Laeufe) ==" % SHOTS)
rates = []
for k in range(20):
    qc = QuantumCircuit(1, 3); qc.u(*rng.uniform(0, 2 * np.pi, 3), 0)
    qc.h(0); qc.measure(0, 0); qc.h(0)                             # X
    qc.measure(0, 1)                                               # Z
    qc.sdg(0); qc.h(0); qc.measure(0, 2)                           # Y
    c = counts_of(qc); hit = 0
    for bits, n in c.items():
        y, z, x = (int(b) for b in bits); hit += n * (y == (x ^ z))
    rates.append(hit / SHOTS)
rates = np.array(rates)
print(f"  Trefferquote von y = x xor z: min {rates.min():.4f}, Mittel {rates.mean():.4f}, max {rates.max():.4f};  mit c = 1: Mittel {1 - rates.mean():.4f}")
print(f"  erwartete Streuung bei reinem Zufall: +-{0.5/np.sqrt(SHOTS):.4f};  groesste Abweichung von 0.5: {np.abs(rates - 0.5).max():.4f}")
print("  Vergleich ohne Messung: Bloch-Komponenten erfuellen x^2 + y^2 + z^2 = 1; |y| folgt aus x und z, das Vorzeichen von y nicht (ein Bit fehlt)")

print("\n== K-d  Datenstrom: Peres-Mermin-Quadrat ==")
SQ = [["XI", "IX", "XX"], ["IZ", "ZI", "ZZ"], ["XZ", "ZX", "YY"]]
kron = lambda s: np.kron(PAULI[s[0]], PAULI[s[1]])
ctx = [("Zeile %d" % (i + 1), SQ[i]) for i in range(3)] + [("Spalte %d" % (j + 1), [SQ[i][j] for i in range(3)]) for j in range(3)]
signs = {}
for name, obs in ctx:
    prod = kron(obs[0]) @ kron(obs[1]) @ kron(obs[2])
    signs[name] = 1 if np.allclose(prod, np.eye(4)) else (-1 if np.allclose(prod, -np.eye(4)) else None)
    comm = all(np.allclose(kron(a) @ kron(b), kron(b) @ kron(a)) for a, b in itertools.combinations(obs, 2))
    print(f"  {name}: {obs}, Produkt = {signs[name]:+d}·1, vertauschen paarweise: {comm}")
best, nbest = 0, 0
for vals in itertools.product((1, -1), repeat=9):
    v = np.array(vals).reshape(3, 3)
    sat = sum(int(np.prod(v[i, :]) == signs["Zeile %d" % (i + 1)]) for i in range(3)) + sum(int(np.prod(v[:, j]) == signs["Spalte %d" % (j + 1)]) for j in range(3))
    if sat > best: best, nbest = sat, 1
    elif sat == best: nbest += 1
print(f"  512 klassische Belegungen: hoechstens {best} von 6 Pruefungen erfuellt ({nbest} Belegungen erreichen das); alle 6: {'ja' if best == 6 else 'keine'}")
for name, obs in ctx:
    qc = QuantumCircuit(5, 3); rand2(qc)
    for k, s in enumerate(obs): measure_string(qc, s, (0, 1), 2 + k, k)
    c = counts_of(qc); par = {0: 0, 1: 0}
    for bits, n in c.items(): par[sum(int(b) for b in bits) % 2] += n
    print(f"  Qiskit, {name} auf Zufallszustand: Paritaet der drei Bits gerade {par[0]}, ungerade {par[1]}  (erwartet: {'gerade' if signs[name] == 1 else 'ungerade'})")

print("\n== K-e  Verbiegung: Moebius/Lorentz macht zwei Punkte zu Gegenpunkten ==")
th, be = sp.symbols("theta beta", positive=True)
nx, nz = sp.sin(th / 2), sp.cos(th / 2)                            # zwei Punkte (+-sin, 0, cos), Winkel theta, Winkelhalbierende z
gam = 1 / sp.sqrt(1 - be ** 2)
nzp = (nz - be) / (1 - be * nz); nxp = nx / (gam * (1 - be * nz))
print("  symmetrischer Fall, Boost laengs der Winkelhalbierenden: n_z' =", sp.simplify(nzp), ";  null fuer beta =", sp.solve(sp.Eq(nz - be, 0), be))
print("  dann n_x' =", sp.simplify(nxp.subs(be, sp.cos(th / 2))), "(Gegenpunkte +-x);  gamma =", sp.simplify(gam.subs(be, sp.cos(th / 2))), "= 1/sin(theta/2)")
print("  Spinor-Ueberlapp |<psi1|psi2>|^2 = (1 + n1·n2)/2 =", sp.simplify((1 + sp.cos(th)) / 2 - sp.cos(th / 2) ** 2) == 0 and "cos^2(theta/2) = beta^2")
print("  invariante Masse: M^2 = 2 E1 E2 (1 - cos theta); im Gegenpunkt-System E1' = E2' = M/2")
def boost(bvec):
    b = np.linalg.norm(bvec); g = 1 / np.sqrt(1 - b * b); n = bvec / b
    Lm = np.eye(4); Lm[0, 0] = g; Lm[0, 1:] = -g * bvec; Lm[1:, 0] = -g * bvec; Lm[1:, 1:] += (g - 1) * np.outer(n, n)
    return Lm
def spinor(n):
    t, p = np.arccos(n[2]), np.arctan2(n[1], n[0]); return np.array([np.cos(t / 2), np.exp(1j * p) * np.sin(t / 2)])
mink = lambda a, b: a[0] * b[0] - np.dot(a[1:], b[1:])
worst = dict(anti=0, mass=0, circ=0, spin=0, beta=0)
for k in range(1000):
    n1, n2 = (v / np.linalg.norm(v) for v in rng.normal(size=(2, 3)))
    cth = float(np.dot(n1, n2)); bis = (n1 + n2) / np.linalg.norm(n1 + n2); bet = np.sqrt((1 + cth) / 2)
    Lm = boost(bet * bis); E1, E2 = 1.0, 1.0
    k1, k2 = Lm @ np.r_[E1, E1 * n1], Lm @ np.r_[E2, E2 * n2]
    m1, m2 = k1[1:] / k1[0], k2[1:] / k2[0]
    worst["anti"] = max(worst["anti"], np.linalg.norm(m1 + m2))
    worst["mass"] = max(worst["mass"], abs(mink(k1 + k2, k1 + k2) - 2 * E1 * E2 * (1 - cth)), abs(k1[0] - np.sqrt(2 * (1 - cth)) / 2))
    # Kreis auf der Kugel: Achse c, Oeffnungswinkel al; 12 Punkte, Bildpunkte muessen in einer Ebene liegen
    c = rng.normal(size=3); c /= np.linalg.norm(c); al = rng.uniform(0.2, 2.9)
    u = np.cross(c, [1, 0, 0]); u /= np.linalg.norm(u); w = np.cross(c, u)
    pts = np.array([np.cos(al) * c + np.sin(al) * (np.cos(s) * u + np.sin(s) * w) for s in np.linspace(0, 2 * np.pi, 12, endpoint=False)])
    img = np.array([(Lm @ np.r_[1, p])[1:] / (Lm @ np.r_[1, p])[0] for p in pts])
    nrm = np.cross(img[1] - img[0], img[2] - img[0]); nrm /= np.linalg.norm(nrm)
    worst["circ"] = max(worst["circ"], np.abs((img - img[0]) @ nrm).max())
    # Spinoren: SL(2,C)-Element zum Boost, beide Vorzeichen probieren
    s1, s2 = spinor(n1), spinor(n2); sig = bis[0] * X + bis[1] * Y + bis[2] * Z; eta = np.arctanh(bet)
    ov = min(abs(np.vdot(A @ s1, A @ s2)) / (np.linalg.norm(A @ s1) * np.linalg.norm(A @ s2)) for A in
             [np.cosh(sg * eta / 2) * I2 + np.sinh(sg * eta / 2) * sig for sg in (1, -1)])
    worst["spin"] = max(worst["spin"], ov); worst["beta"] = max(worst["beta"], abs(abs(np.vdot(s1, s2)) - bet))
print(f"  1000 Zufallspaare, Boost beta = cos(theta/2) laengs der Winkelhalbierenden: groesste Abweichung von Gegenpunkten {worst['anti']:.2e};")
print(f"    invariante Masse und E' = M/2: {worst['mass']:.2e};  Kreis -> Kreis (Abstand der Bildpunkte von einer Ebene): {worst['circ']:.2e};")
print(f"    Spinoren nach der SL(2,C)-Abbildung orthogonal (Rest-Ueberlapp): {worst['spin']:.2e};  |<psi1|psi2>| - beta: {worst['beta']:.2e}")
bs = 0.5494; gL = 1.86444
print(f"  Zahlen ohne Zuordnung: beta = beta_sym = {bs} entspricht theta = {np.degrees(2*np.arccos(bs)):.2f} Grad, Lorentz-gamma {1/np.sqrt(1-bs**2):.4f} (gamma_L = {gL} ist cosh der doppelten Rapiditaet: {np.cosh(2*np.arctanh(bs)):.4f})")
