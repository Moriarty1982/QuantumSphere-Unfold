"""k88: Test der Vorab-Notiz H32 (Commit 65c5b44): Platz-Gewichte der Abweichung Delta = J_II - J_I auf den Q-Sektoren,
Frame-Verhalten, Generationen-Maske W_q, W_l, Mischung bei schwacher Stoerung, Form in der Fourier-Basis."""
import itertools, numpy as np, os, sys
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k69_test_h17 import omul

TOL = 1e-9
E = np.eye(8)
L7 = np.array([omul(E[7], E[j]) for j in range(8)]).T
R7 = np.array([omul(E[j], E[7]) for j in range(8)]).T
Q8 = 0.5*np.eye(8) - (1j/6)*L7 - (1j/3)*R7
w8, V8 = np.linalg.eigh(Q8)
Pq = {q: V8[:, abs(w8 - q) < 1e-9]@V8[:, abs(w8 - q) < 1e-9].conj().T for q in (0, 1/3, 2/3, 1)}
B = [L7, R7, -L7 - R7]
Delta = [1j*(b - L7) for b in B]
fr = lambda x: Fraction(float(np.real(x))).limit_denominator(12)

# H32a
weights = {}; scalar_ok = True
for q, P in Pq.items():
    ws = []
    for D in Delta:
        w = np.trace(D@P)/np.trace(P)
        scalar_ok &= abs(D@P - w*P).max() < TOL
        ws.append(fr(w))
    weights[q] = tuple(ws)
want = {0: (0, 0, -3), 1/3: (0, 2, 1), 2/3: (0, -2, -1), 1: (0, 0, 3)}
ok_a = scalar_ok and all(weights[q] == tuple(Fraction(x) for x in want[q]) for q in want)
print(f"H32a: Delta auf jedem Q-Sektor skalar: {scalar_ok}; Platz-Gewichte: "
      + ", ".join(f"Q = {fr(q)}: {tuple(str(x) for x in weights[q])}" for q in weights) + f" -> {'bestaetigt' if ok_a else 'widerlegt'}")

# H32b
TDelta = max(abs(D.conj() + D).max() for D in Delta)
anti = all(weights[q] == tuple(-x for x in weights[1 - q if q in (0, 1) else (2/3 if q == 1/3 else 1/3)]) for q in weights)
Wq = np.diag([float(x) for x in weights[2/3]]); Wl = np.diag([float(x) for x in weights[0]])
# rechtshaendiger Partner im T-Frame: Gewicht -w(1-q) = w(q)
partner_q = np.diag([-float(x) for x in weights[1/3]]); partner_l = np.diag([-float(x) for x in weights[1]])
ok_b = TDelta < TOL and anti and abs(partner_q - Wq).max() < TOL and abs(partner_l - Wl).max() < TOL
print(f"\nH32b: T Delta T^-1 = -Delta: {TDelta:.0e}; Gewichte antisymmetrisch unter q <-> 1-q: {anti};"
      f" W_q = diag{tuple(np.diag(Wq))}, W_l = diag{tuple(np.diag(Wl))}, Partner im T-Frame gleich: "
      f"{abs(partner_q - Wq).max() < TOL and abs(partner_l - Wl).max() < TOL} -> {'bestaetigt' if ok_b else 'widerlegt'}")

# H32c
rng = np.random.default_rng(88)
P = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
def herm_circ(a, b): return a*np.eye(3) + b*P + np.conj(b)*P.conj().T
def rand_circ(): return herm_circ(rng.normal()*3, rng.normal() + 1j*rng.normal())
def perm_dev(V):
    best = 9
    for p in itertools.permutations(range(3)):
        Pm = np.zeros((3, 3)); Pm[range(3), p] = 1
        best = min(best, abs(V - Pm).max())
    return best
def mix(Mu, Md): return abs(np.linalg.eigh(Mu)[1].conj().T@np.linalg.eigh(Md)[1])
pert = lambda M, W, e: M + e*(W@M + M@W)
comm = min(abs(W@P - P@W).max() for W in (Wq, Wl))
nonzero = True; ratios = []
for _ in range(200):
    Mu, Md = rand_circ(), rand_circ()
    d = [perm_dev(mix(pert(Mu, Wq, e), pert(Md, Wq, e))) for e in (1e-3, 1e-4)]
    nonzero &= d[1] > 0
    ratios.append(d[0]/d[1]/10)
ratios = np.array(ratios)
ok_c = comm > 0.5 and nonzero and abs(ratios - 1).max() < 0.05
print(f"\nH32c: [W, tau] != 0 (min {comm:.2f}); Mischung bei gleicher Maske W_q fuer up und down von null verschieden: {nonzero};"
      f" Linearitaet (Abstand(1e-3)/Abstand(1e-4)/10) in [{ratios.min():.4f}, {ratios.max():.4f}] -> {'bestaetigt' if ok_c else 'widerlegt'}")

# H32d
w3 = np.exp(2j*np.pi/3)
F = np.array([[w3**(j*k) for k in range(3)] for j in range(3)])/np.sqrt(3)
assert abs(F.conj().T@P@F - np.diag(np.diag(F.conj().T@P@F))).max() < TOL
off = lambda W: [abs((F.conj().T@W@F)[i, j]) for i in range(3) for j in range(3) if i != j]
oq, ol = off(Wq), off(Wl)
ok_d = max(abs(np.array(oq) - 1/np.sqrt(3))) < TOL and max(abs(np.array(ol) - 1)) < TOL
print(f"\nH32d: Fourier-Nebendiagonale |W_q| = {np.round(oq, 6)} (1/sqrt3 = {1/np.sqrt(3):.6f}), |W_l| = {np.round(ol, 6)};"
      f" Verhaeltnis {np.mean(ol)/np.mean(oq):.6f} (sqrt3 = {np.sqrt(3):.6f}) -> {'bestaetigt' if ok_d else 'widerlegt'}")

# Nachkontrolle zu H32c (nach der Auswertung, kein Teil des Kriteriums): Liegen die nichtlinearen Faelle bei kleinen Massenabstaenden?
rng = np.random.default_rng(88)
rows = []
for _ in range(200):
    Mu, Md = rand_circ(), rand_circ()
    d = [perm_dev(mix(pert(Mu, Wq, e), pert(Md, Wq, e))) for e in (1e-3, 1e-4, 1e-6, 1e-7)]
    gap = min(min(np.diff(np.linalg.eigvalsh(Mu))), min(np.diff(np.linalg.eigvalsh(Md))))
    scale = max(abs(np.linalg.eigvalsh(Mu)).max(), abs(np.linalg.eigvalsh(Md)).max())
    rows.append((d[0]/d[1]/10, d[2]/d[3]/10, gap/scale))
rows = np.array(rows)
bad = rows[abs(rows[:, 0] - 1) > 0.05]
print(f"\nNachkontrolle H32c: {len(bad)} von 200 Faellen nichtlinear bei eps = 1e-3/1e-4; ihre relative Luecke Luecke/Skala:"
      f" max {bad[:, 2].max() if len(bad) else float('nan'):.2e} (alle Faelle: Median {np.median(rows[:, 2]):.2e});"
      f" bei eps = 1e-6/1e-7 Verhaeltnis in [{rows[:, 1].min():.4f}, {rows[:, 1].max():.4f}]")
