"""k359 (H166): Phase der Nebendiagonale: Zielwert, notwendige Bedingungen, Maske mit festem eps.
Vorab-Notiz Vorab_Notiz_H166_Phase_der_Nebendiagonale.md (Commit c0e9142).
Aufruf: python3 k359_test_h166.py > k359_out.txt
"""
import itertools
import numpy as np
import sympy as sp
from mpmath import mp, mpf, sqrt, cos, pi, findroot, atanh, acos
from scipy.optimize import fsolve

mp.dps = 30
ME, MMU, MTAU, DTAU = mpf('0.51099895000'), mpf('105.6583755'), mpf('1776.93'), mpf('0.09')
RATIO, DRATIO = mpf('206.7682827'), mpf('0.0000046')   # m_mu/m_e (CODATA 2022)
ALPHA = mpf(1) / mpf('137.035999177')


def lam(rho, d):
    """Wurzeln (e, mu, tau) der Brannen-Form 1 + 2 rho cos(d + 2 pi k/3)."""
    return [1 + 2 * rho * cos(d + 2 * pi * k / 3) for k in (1, 2, 0)]


print("== H166a: Zielwert allein aus m_mu/m_e ==")
R = 1 / sqrt(RATIO)
rk = 1 / sqrt(mpf(2))
d_star = findroot(lambda d: lam(rk, d)[0] / lam(rk, d)[1] - R, 0.222)
dd = abs(findroot(lambda d: lam(rk, d)[0] / lam(rk, d)[1] - 1 / sqrt(RATIO + DRATIO), 0.222) - d_star)
l = lam(rk, d_star)
mt1 = MMU * (l[2] / l[1]) ** 2
print(f"(i)  K = 2/3 exakt: delta* = {mp.nstr(d_star, 13)} +- {mp.nstr(dd, 2)}; delta* - 2/9 = {mp.nstr(d_star - mpf(2)/9, 4)}"
      f" (relativ {mp.nstr((d_star - mpf(2)/9) / (mpf(2)/9), 3)}; {mp.nstr((d_star - mpf(2)/9) / dd, 4)} sigma); m_tau = {mp.nstr(mt1, 9)} MeV")
rho2 = findroot(lambda r: lam(r, mpf(2) / 9)[0] / lam(r, mpf(2) / 9)[1] - R, 0.707)
l = lam(rho2, mpf(2) / 9)
K2 = (1 + 2 * rho2 ** 2) / 3
mt2 = MMU * (l[2] / l[1]) ** 2
print(f"(ii) delta = 2/9 exakt: K = {mp.nstr(K2, 13)}; K - 2/3 = {mp.nstr(K2 - mpf(2)/3, 4)}; m_tau = {mp.nstr(mt2, 9)} MeV")
l = lam(rk, mpf(2) / 9)
rb = (l[1] / l[0]) ** 2
print(f"(iii) beide exakt: m_mu/m_e = {mp.nstr(rb, 12)}; gemessen {mp.nstr(RATIO, 12)} +- {mp.nstr(DRATIO, 2)}; "
      f"Abstand {mp.nstr((rb - RATIO) / DRATIO, 5)} sigma (relativ {mp.nstr((rb - RATIO) / RATIO, 3)})")
# 3 delta = K (Selbstbezug, H1)
sol = findroot(lambda r, d: (lam(r, d)[0] / lam(r, d)[1] - R, 3 * d - (1 + 2 * r * r) / 3), (0.707, 0.222))
l = lam(sol[0], sol[1])
mt3 = MMU * (l[2] / l[1]) ** 2
print(f"(iv) 3 delta = K: delta = {mp.nstr(sol[1], 13)}, K = {mp.nstr(3 * sol[1], 13)}; m_tau = {mp.nstr(mt3, 9)} MeV")
gM = mpf('0.237533')
th = (pi / 4 - gM / 2) / 3
r4 = findroot(lambda r: lam(r, th)[0] / lam(r, th)[1] - R, 0.707)
l = lam(r4, th)
mt4 = MMU * (l[2] / l[1]) ** 2
print(f"(v)  H102, 3 delta = pi/4 - gamma_M/2: delta = {mp.nstr(th, 10)}; m_tau = {mp.nstr(mt4, 8)} MeV")
for nm, m in (("K = 2/3", mt1), ("delta = 2/9", mt2), ("3 delta = K", mt3), ("H102", mt4)):
    print(f"   {nm:12s}: (m_tau - 1776.93)/0.09 = {mp.nstr((m - MTAU) / DTAU, 3)} sigma")
# volle Anpassung an drei Massen
def fit(mt):
    s = [sqrt(ME), sqrt(MMU), sqrt(mt)]
    return findroot(lambda r, d: (lam(r, d)[0] / lam(r, d)[1] - s[0] / s[1], lam(r, d)[2] / lam(r, d)[1] - s[2] / s[1]), (0.707, 0.222))
for m in (MTAU - DTAU, MTAU, MTAU + DTAU):
    r, d = fit(m)
    print(f"   drei Massen, m_tau = {mp.nstr(m, 6)}: K = {mp.nstr((1 + 2 * r * r) / 3, 9)}, delta = {mp.nstr(d, 9)}")
print(f"Groessenvergleich: |delta*/(2/9) - 1| = {mp.nstr(abs(d_star * 9 / 2 - 1), 3)}; alpha/pi = {mp.nstr(ALPHA / pi, 3)}; "
      f"(alpha/pi)^2 = {mp.nstr((ALPHA / pi) ** 2, 3)}; (alpha/pi)^3 = {mp.nstr((ALPHA / pi) ** 3, 3)}")

print("\n== H166b: Stationaritaet ist algebraisch ==")
x, q = sp.symbols('x q')            # x = cos delta, q = beta/alpha
d = sp.symbols('delta', real=True)
for name, n in (("cos 2d + q cos 3d", 3), ("cos 2d + q cos d", 1)):
    V = sp.cos(2 * d) + q * sp.cos(n * d)
    dV = sp.diff(V, d)
    red = sp.simplify(sp.expand_trig(dV) / sp.sin(d))
    poly = sp.Poly(sp.expand(red.subs(sp.cos(d), x).subs(sp.sin(d) ** 2, 1 - x ** 2)), x)
    print(f"V = {name}: dV/d(delta) = sin(delta) * ({poly.as_expr()}); Polynom in x = cos delta vom Grad {poly.degree()}, Koeffizienten in Q(q)")
    qneed = sp.solve(poly.as_expr(), q)[0]
    print(f"   noetiges q bei delta: q = {qneed}; bei cos(2/9): {float(qneed.subs(x, sp.cos(sp.Rational(2, 9)))):+.9f}; "
          f"bei cos(2 pi/3 - 2/9): {float(qneed.subs(x, sp.cos(2 * sp.pi / 3 - sp.Rational(2, 9)))):+.9f}")
print("Satz: q algebraisch => x = cos delta algebraisch (Nullstelle eines Polynoms ueber den algebraischen Zahlen).")
print("Lindemann-Weierstrass: fuer algebraisches t != 0 ist cos t transzendent; also ist delta = 2/9 fuer algebraisches q ausgeschlossen.")
print("sympy: cos(2/9) algebraisch?", sp.cos(sp.Rational(2, 9)).is_algebraic, "; tan(2/9) algebraisch?", sp.tan(sp.Rational(2, 9)).is_algebraic)

print("\n== H166c: Bedeutung der Phase ==")
a, r, s, v = sp.symbols('a r s v', real=True)
S = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
b = s + sp.I * v
W = a * sp.eye(3) + b * S + sp.conjugate(b) * S.T
n = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
Lx = sp.Matrix([[0, 0, 0], [0, 0, -sp.I], [0, sp.I, 0]])
Ly = sp.Matrix([[0, 0, sp.I], [0, 0, 0], [-sp.I, 0, 0]])
Lz = sp.Matrix([[0, -sp.I, 0], [sp.I, 0, 0], [0, 0, 0]])
Ln = (Lx + Ly + Lz) / sp.sqrt(3)
print("L_n^3 - L_n = 0:", sp.simplify(Ln ** 3 - Ln).is_zero_matrix, "; L_n^2 = 1 - n n^T:", sp.simplify(Ln ** 2 - sp.eye(3) + n * n.T).is_zero_matrix)
# exp(i t L_n) = 1 + i sin t L_n + (cos t - 1) L_n^2
t = 2 * sp.pi / 3
E = sp.eye(3) + sp.I * sp.sin(t) * Ln + (sp.cos(t) - 1) * Ln ** 2
sgn = None
for sg in (1, -1):
    Esg = sp.eye(3) + sp.I * sp.sin(sg * t) * Ln + (sp.cos(t) - 1) * Ln ** 2
    if sp.simplify(Esg - S).is_zero_matrix:
        sgn = sg
print(f"(i) S = exp({'+' if sgn == 1 else '-'}i (2 pi/3) L_n):", sgn is not None)
c0, D, B = a + 2 * s, -3 * s, -sgn * sp.sqrt(3) * v
print("(ii) W - (c0 + D L_n^2 + B L_n) = 0 mit c0 = a + 2s, D = -3s, B =", B, ":",
      sp.simplify(W - (c0 * sp.eye(3) + D * Ln ** 2 + B * Ln)).is_zero_matrix, "; tan delta = v/s = -sqrt3 B/D * (", sgn, ")")
print("     Konjugation sigma (W -> W*): L_n -> -L_n, L_n^2 fest; der v-Anteil ist der sigma-ungerade Dipol:",
      sp.simplify(sp.conjugate(Ln) + Ln).is_zero_matrix)
al = sp.symbols('alpha1:4', real=True)
G = sp.diag(*[sp.exp(sp.I * x_) for x_ in al])
Wg = G * W * G.H
prod = sp.simplify(Wg[0, 1] * Wg[1, 2] * Wg[2, 0])
print("(iii) Torus: w12 w23 w31 nach Umeichung - b^3 =", sp.simplify(sp.expand(prod - b ** 3)), "; einzelne Phase w12 ->", sp.simplify(Wg[0, 1] / W[0, 1]))
de = sp.symbols('delta', real=True)
lam_s = [a + 2 * r * sp.cos(de + 2 * sp.pi * k / 3) for k in (0, 1, 2)]   # tau, e, mu
expr = sp.sqrt(3) * (lam_s[2] - lam_s[1]) / (2 * lam_s[0] - lam_s[1] - lam_s[2])
print("(iv) sqrt3 (sqrt m_mu - sqrt m_e)/(2 sqrt m_tau - sqrt m_mu - sqrt m_e) - tan delta =", sp.simplify(sp.expand_trig(expr) - sp.tan(de)))

print("\n== H166d: Maske mit festem eps0 = artanh(beta_sym) (blind) ==")
EPS0 = float(atanh(mpf('0.5494056410')))
PHI1 = float(3 * acos(1 - 1 / sqrt(mpf(2))) - pi)
P = np.roll(np.eye(3), 1, axis=0)
print(f"eps0 = {EPS0:.10f}; phi_1 = {PHI1:.7f}, phi_1/3 = {PHI1 / 3:.7f}")


def Cmat(rho, d0):
    z = rho * np.exp(1j * d0)
    return np.eye(3) + z * P + np.conj(z) * P.T


def form_K(C, eps, slot=2):
    w = np.zeros(3); w[slot] = -3.0
    Dm = np.diag(np.exp(eps * w))
    return Dm @ C @ Dm


def form_lin(C, eps, slot=2):
    Wm = np.zeros((3, 3)); Wm[slot, slot] = -3.0
    return C + eps * (Wm @ C + C @ Wm)


def K_delta(M):
    ev = np.sort(np.linalg.eigvalsh((M + M.conj().T) / 2))
    neg = int((ev < 0).sum())
    K = (ev ** 2).sum() / ev.sum() ** 2
    aa = ev.sum() / 3
    # ev = aa (1 + 2 rho cos(delta + 2 pi k/3)), groesster bei k = 0, delta in [0, pi/3]
    td = np.sqrt(3) * (ev[1] - ev[0]) / (2 * ev[2] - ev[1] - ev[0])
    return K, np.arctan(td), neg, ev


FORMS = {"K": form_K, "lin": form_lin}
rk_ = 1 / np.sqrt(2)
print("Kontrollen:")
c1 = max(abs(np.array(K_delta(f(Cmat(rk_, d0), 0.0))[:2]) - np.array([2 / 3, d0])).max() for f in FORMS.values() for d0 in (0.1, 0.2222, 0.7))
print(f"  eps = 0: max |(K', delta') - (2/3, delta0)| = {c1:.1e}")
c2 = 0.0
for f in FORMS.values():
    for d0 in (0.1, 0.2222, 0.7):
        ref = K_delta(f(Cmat(rk_, d0), EPS0))[3]
        for sl in (0, 1):
            c2 = max(c2, abs(K_delta(f(Cmat(rk_, d0), EPS0, sl))[3] - ref).max())
        for d1 in (-d0, d0 + 2 * np.pi / 3):
            c2 = max(c2, abs(K_delta(f(Cmat(rk_, d1), EPS0))[3] - ref).max())
print(f"  Maskenplatz, delta0 -> -delta0, delta0 -> delta0 + 2 pi/3: max Aenderung des Spektrums = {c2:.1e}")
Sg = np.diag(np.exp(EPS0 * np.array([0, 0, -3.0])))
C0 = Cmat(rk_, 0.2222)
evS = np.sort(np.linalg.eigvals(Sg @ C0 @ np.linalg.inv(Sg)).real)
print(f"  Form S (Aehnlichkeit): max Aenderung des Spektrums = {abs(evS - np.sort(np.linalg.eigvalsh(C0))).max():.1e}")

KT, DT, TOL = 0.666664, 0.222222, 1e-4
NSET = {"0": 0.0, "pi/12": np.pi / 12, "pi/6": np.pi / 6, "pi/4": np.pi / 4, "pi/3": np.pi / 3, "phi1/3": PHI1 / 3}
print("\nVorwaerts (rho^2 = 1/2): Kandidat -> (K', delta'), Anzahl negativer Eigenwerte")
hits = 0; best = (9, None)
for fn, f in FORMS.items():
    for sg in (+1, -1):
        for nm, d0 in NSET.items():
            K, dl, neg, ev = K_delta(f(Cmat(rk_, d0), sg * EPS0))
            hit = abs(K - KT) <= TOL and abs(dl - DT) <= TOL
            hits += hit
            dist = max(abs(K - KT), abs(dl - DT))
            if dist < best[0]:
                best = (dist, (fn, sg, nm))
            print(f"  Form {fn:3s} eps {'+' if sg > 0 else '-'}eps0, delta0 = {nm:7s}: K' = {K:.6f}, delta' = {dl:.6f}, neg = {neg}{'  TREFFER' if hit else ''}")
print(f"Treffer vorwaerts: {hits} von 24; naechster Kandidat {best[1]} mit Abstand {best[0]:.4f}")

print("\nRueckwaerts: unmaskiertes (K0, delta0), dessen maskiertes Spektrum die Lepton-Wurzeln gibt")
bhits = 0
for mt in (1776.84, 1776.93, 1777.02):
    sq = np.sqrt(np.array([0.51099895, 105.6583755, mt]))
    tgt = (sq[0] / sq[2], sq[1] / sq[2])
    for fn, f in FORMS.items():
        for sg in (+1, -1):
            found = {}
            for r0, d0 in itertools.product(np.linspace(0.05, 3.0, 25), np.linspace(-np.pi, np.pi, 37)):
                def eq(p, f=f, sg=sg):
                    ev = np.sort(np.abs(np.linalg.eigvalsh(f(Cmat(p[0], p[1]), sg * EPS0))))
                    return [ev[0] / ev[2] - tgt[0], ev[1] / ev[2] - tgt[1]]
                p, info, ier, _ = fsolve(eq, [r0, d0], full_output=True, xtol=1e-14)
                if ier == 1 and max(abs(np.array(eq(p)))) < 1e-11 and p[0] > 0:
                    dfold = abs(((p[1] + np.pi / 3) % (2 * np.pi / 3)) - np.pi / 3)
                    ev = np.linalg.eigvalsh(f(Cmat(p[0], p[1]), sg * EPS0))
                    key = (round(p[0], 7), round(dfold, 7))
                    found[key] = int((ev < 0).sum())
            for (r0, d0), neg in sorted(found.items()):
                K0 = (1 + 2 * r0 ** 2) / 3
                near = min(NSET.items(), key=lambda kv: abs(kv[1] - d0))
                hit = abs(K0 - 2 / 3) <= TOL and abs(near[1] - d0) <= TOL
                bhits += hit
                if mt == 1776.93 or hit:
                    print(f"  m_tau {mt}: Form {fn:3s} eps {'+' if sg > 0 else '-'}eps0: rho0 = {r0:.7f}, K0 = {K0:.6f}, delta0 = {d0:.7f} "
                          f"(naechstes N: {near[0]}, Abstand {abs(near[1] - d0):.4f}), neg. Eigenwerte {neg}{'  TREFFER' if hit else ''}")
            if not found and mt == 1776.93:
                print(f"  m_tau {mt}: Form {fn:3s} eps {'+' if sg > 0 else '-'}eps0: keine Loesung")
print(f"Treffer rueckwaerts (alle drei m_tau): {bhits}")
print(f"\nH166d: {'bestaetigt (kein Treffer)' if hits == 0 and bhits == 0 else 'widerlegt (Treffer)'}")
