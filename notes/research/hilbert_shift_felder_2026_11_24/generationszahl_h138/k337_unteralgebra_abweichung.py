"""k337 (H154): Erzwingt die Algebra die Schleife ueber {1, U}? Woher kommt die Abweichung zwischen 2/3 und dem Messwert?

Vorab-Notiz: Vorab_Notiz_H154_Unteralgebra_und_Abweichung.md (Commit 5ef018d).
Aufruf: python -W ignore k337_unteralgebra_abweichung.py > k337_out.txt
Konvention wie k336: V = lA phi^4 + ka phi^2 B + lB B^2, B = y1^2 + y2^2, Fluss ins Infrarote dg/dt = -beta (16 pi^2 in tau).
"""
import itertools
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

lA, ka, lB, e2 = sp.symbols("lA ka lB e2", real=True)

def beta_functions(nA, nB):
    x = sp.symbols(f"x0:{nA}", real=True); y = sp.symbols(f"y0:{nB}", real=True)
    A = sum(v**2 for v in x); B = sum(v**2 for v in y)
    V = lA * A**2 + ka * A * B + lB * B**2
    H = sp.hessian(V, list(x) + list(y)); rhs = sp.expand(sp.Rational(1, 2) * (H * H).trace())
    bA, bK, bB = sp.symbols("bA bK bB")
    sol = sp.solve(sp.Poly(sp.expand(rhs - (bA * A**2 + bK * A * B + bB * B**2)), *(list(x) + list(y))).coeffs(), (bA, bK, bB), dict=True)[0]
    return [sp.factor(sol[q]) for q in (bA, bK, bB)]

b12 = beta_functions(1, 2); b11 = beta_functions(1, 1)
print("=== H154a: Schleife der zweiten Ebenenrichtung ===")
print("   beta(1,2) - beta(1,1) =", [sp.factor(p - q) for p, q in zip(b12, b11)], "(Vorhersage [2 ka^2, 8 ka lB, 8 lB^2])")
# direkt: Beitrag der y2-Schleife = 1/2 Tr ueber die y2-Zeile/Spalte der Hesseschen (Kreuzterme mit x, y1 eingeschlossen)
ph, y1, y2 = sp.symbols("phi y1 y2", real=True)
V = lA * ph**4 + ka * ph**2 * (y1**2 + y2**2) + lB * (y1**2 + y2**2)**2
H = sp.hessian(V, [ph, y1, y2]); full = sp.expand(sp.Rational(1, 2) * (H * H).trace())
Hs = H[:2, :2]; sub = sp.expand(sp.Rational(1, 2) * (Hs * Hs).trace())
print("   1/2 Tr H^2 (alle drei) - 1/2 Tr H^2 (nur phi, y1), bei y2 = 0:", sp.factor(sp.expand((full - sub).subs(y2, 0))))
print("   -> verschwindet nur fuer ka = lB = 0 (also nie im Koide-Bereich); im symmetrischen skalenfreien Bereich sind alle Massen 0, nichts entkoppelt.")

print("\n=== H154b: Ladungserhaltung, invariante Unterraeume in so(3) auf (phi, y1, y2) ===")
a1, a2, a3 = sp.symbols("a1 a2 a3", real=True)
Gen = sp.Matrix([[0, -a1, -a2], [a1, 0, -a3], [a2, a3, 0]])   # allgemeiner Erzeuger
# {1, U} = span(e_phi, e_y1) invariant <=> G e_phi, G e_y1 ohne y2-Komponente
cond = sp.solve([(Gen * sp.Matrix([1, 0, 0]))[2], (Gen * sp.Matrix([0, 1, 0]))[2]], [a2, a3], dict=True)
G1 = Gen.subs(cond[0]); print("   Erzeuger mit invariantem span{1, U}:", G1.tolist(), "-> nur die U(1) aus exp(aU) (Drehung 1 <-> U)")
print("   Ladung von U' (y2) unter diesem Erzeuger: G e_y2 =", list(G1 * sp.Matrix([0, 0, 1])), "-> U' neutral, {1, U} geladen (umgekehrt wie gebraucht)")
X = sp.Matrix([ph, y1, y2]); dV = sp.expand((sp.Matrix([V]).jacobian(X) * (G1 * X))[0])
print("   Erhaelt diese U(1) das Potential? dV =", sp.factor(dV), "-> nur fuer ka = 2 lA = 2 lB (volle Norm, H150: kein Koide-Kondensat)")
G2 = Gen.subs({a1: 0, a2: 0}); print("   Ebenen-Drehung (Erzeuger", G2.tolist(), "): mischt U und U', span{1, U} nicht invariant")
print("   Diskret: Spiegelung y2 -> -y2 (Z2 aus Z3 x| Z2): U' ungerade, {1, U} gerade. Ungerade Felder treten paarweise auf, laufen aber in der Schleife mit (H154a).")

print("\n=== H154c: Massen am GW-Punkt des (1,2)-Flusses ===")
fb12 = sp.lambdify([[lA, ka, lB]], [-q for q in b12], "numpy")
def flow(fb, g0, n=3, tmax=1e4):
    ev = lambda t, y: y[1] + 2 * np.sqrt(max(y[0] * y[2], 0.0)); ev.terminal = True; ev.direction = -1
    neg = lambda t, y: min(y[0], y[2]); neg.terminal = True; neg.direction = -1
    r = solve_ivp(lambda t, y: fb(y), (0, tmax), g0, method="LSODA", rtol=1e-12, atol=1e-15, events=[ev, neg])
    if len(r.t_events[0]):
        return r.t_events[0][0], r.y_events[0][0]
    return None
tg, gv = flow(fb12, [0.2, -0.2, 0.2])
x = gv[0] / gv[2]; th = np.arctan(x**0.25)
Hn = np.array(sp.hessian(V, [ph, y1, y2]).subs({lA: gv[0], ka: gv[1], lB: gv[2], ph: np.cos(th), y1: np.sin(th), y2: 0}).evalf(), dtype=float)
print(f"   Start (0.2, -0.2, 0.2): tau = {tg:.6f}, K = {(1 + np.sqrt(x)) / 3:.6f}; Massenquadrate (v = 1): {np.round(np.linalg.eigvalsh(Hn), 12).tolist()}")
print("   y2-Eintrag der Hesseschen:", Hn[2, 2], "(Goldstone, m = 0); flache Richtung ebenfalls 0 (Dilaton).")
print("   Coleman-Weinberg laengs der flachen Richtung: Beitrag m^4 ln m^2 der Goldstone-Richtung = 0; der Ort des GW-Punkts (K) kommt aber aus dem Fluss davor,")
print("   in dem y2 masselos mitlaeuft. K unveraendert = H150/H153-Kontrolle 0.671941.")

print("\n=== H154d: geeichte Ebenen-Drehung (skalare QED, phi neutral) ===")
bg = [b12[0], b12[1] - 6 * e2 * ka, b12[2] - 12 * e2 * lB + sp.Rational(3, 2) * e2**2, 2 * e2**2 / 3]   # beta von e^2: 2 e beta_e = 2 e^4/3
fbg = sp.lambdify([[lA, ka, lB, e2]], [-q for q in bg], "numpy")
rows = []
for E, L, kr in itertools.product([0.05, 0.1, 0.2, 0.5, 1.0], [0.1, 0.2], [-1.5, -1.0, -0.5, -0.2]):
    out = flow(fbg, [L, kr * L, L, E])
    if out is None:
        rows.append((E, L, kr, None)); continue
    g = out[1]; rows.append((E, L, kr, (1 + np.sqrt(g[0] / g[2])) / 3))
ok = [r for r in rows if r[3] is not None]; Ks = np.array([r[3] for r in ok])
for E in [0.05, 0.1, 0.2, 0.5, 1.0]:
    ks = [r[3] for r in ok if r[0] == E]
    print(f"   e0^2 = {E}: GW {len(ks)}/8, K = {np.round(ks, 6).tolist()}")
print(f"   gesamt: GW {len(ok)}/{len(rows)}; K {Ks.min():.6f} ... {Ks.max():.6f}, Std {Ks.std():.2e} -> {'startunabhaengig' if Ks.std() < 1e-3 else 'startabhaengig'};"
      f" Treffer |K - 2/3| < 1,5e-5: {int(np.sum(np.abs(Ks - 2 / 3) < 1.5e-5))}")
print("   Tausch bei lA = lB: beta_lA - beta_lB =", sp.factor((bg[0] - bg[2]).subs(lB, lA)), "(Eichanteil bricht ihn zusaetzlich)")

print("\n=== H154e: Messrauschen (Polmassen) ===")
def K(m): return m.sum() / np.sqrt(m).sum()**2
for lab, tau, st in [("PDG aktuell (wie H146)", 1776.93, 0.09), ("aelterer Wert (Basis von 0,666661 +- 7e-6)", 1776.86, 0.12)]:
    m = np.array([0.51099895000, 105.6583755, tau]); s = np.array([1.5e-10, 2.3e-6, st]); k0 = K(m)
    gr = np.array([(K(m + np.eye(3)[i] * 1e-7 * m[i]) - K(m - np.eye(3)[i] * 1e-7 * m[i])) / (2e-7 * m[i]) for i in range(3)])
    contrib = (gr * s)**2; sk = np.sqrt(contrib.sum())
    print(f"   {lab}: m_tau = {tau} +- {st}: K = {k0:.8f} +- {sk:.2e}; (2/3 - K)/sigma = {(2 / 3 - k0) / sk:.3f}; Fehleranteile e, mu, tau: {np.round(contrib / contrib.sum(), 8).tolist()}")
from scipy.optimize import brentq
print(f"   m_tau fuer K = 2/3 exakt: {brentq(lambda t: K(np.array([0.51099895, 105.6583755, t])) - 2 / 3, 1700, 1800):.4f} MeV")

print("\n=== H154f: Laufen der Massen (QED einschleifig) ===")
al = 1 / 137.035999; M = np.array([0.51099895, 105.6583755, 1776.93]); MZ = 91187.6
k_pole = K(M); sig = 5.08e-6
run = lambda mu: M * (1 - al / np.pi * (1 + 0.75 * np.log(mu**2 / M**2)))
for nm, mu in [("m_e", M[0]), ("m_mu", M[1]), ("m_tau", M[2]), ("M_Z", MZ)]:
    kk = K(run(mu)); print(f"   gemeinsame Skala mu = {nm}: K = {kk:.6f}, K - K_pol = {kk - k_pole:+.2e} = {(kk - k_pole) / sig:+.0f} sigma")
own = M * (1 - al / np.pi)
print(f"   je eigene Skala m(M): K - K_pol = {K(own) - k_pole:+.1e} (gemeinsamer Faktor faellt heraus)")
print("   Vergleich H1 (laufende MS-bar-Massen bei M_Z, Antusch-Hinze-Saad 2025): K = 0,6678")

print("\n=== H154g/h: Frame (Form S) und delta ===")
m1, m2, m3 = sp.symbols("m1 m2 m3", positive=True)
G = sp.diag(m1, m2, m3); S = sp.Matrix([[2, 1, 0], [1, 3, 1], [0, 1, 4]])     # beliebige invertierbare Matrix
Gp = S * G * S.inv()
Kf = lambda Gm: Gm.trace() and (Gm * Gm).trace() / Gm.trace()**2
print("   Form S: K(S G S^-1) - K(G) =", sp.simplify(Kf(Gp) - Kf(G)), "(Spuren invariant) -> Frame-Beitrag 0")
t, d = sp.symbols("theta delta", real=True)
c = [sp.cos(t) / sp.sqrt(3) + sp.sqrt(sp.Rational(2, 3)) * sp.sin(t) * sp.cos(d + 2 * sp.pi * k / 3) for k in range(3)]
Kc = sp.simplify(sp.expand_trig(sum(ci**2 for ci in c)) / sp.expand_trig(sum(c))**2)
print("   K(theta, delta) =", sp.simplify(sp.trigsimp(Kc)), "; dK/ddelta =", sp.simplify(sp.diff(Kc, d)))
print("   dK/dtheta bei pi/4 =", sp.simplify(sp.diff(1 / (3 * sp.cos(t)**2), t).subs(t, sp.pi / 4)), "-> noetiges Dtheta = 3 DK/4 =", 0.75 * (k_pole - 2 / 3))
