"""k109: unabhaengige Gegenpruefung des reparierten OP5-Feldkeims (Stand cf48496).

Eigene Implementierung: Vergleichsmodell aus den Formeln neu aufgeschrieben, Feld als Polynom bis Grad 5 aus den
gespeicherten Koeffizienten, Auswertung entlang Geraden x = p + t d mit exakter Potenzreihen-Arithmetik in t
(keine numerische Differentiation, kein Code des anderen Modells). Geprueft werden F (Feldgleichung) bis Ordnung 4
und g (skalare Zustandsbedingung) bis Ordnung 5 -- das sind die Teile von R = (F, G, dg), die ohne die
Kompatibilitaetsfunktionen G auskommen.

Modell (OP5_Counterflow_Full_Residual_Check.py, v410-Abschnitt):
  F = i sum_{mu,a} V^mu_a K_a D_mu Psi - h (Y x beta) Psi,  D_mu = d_mu + i A_mu,  V = E^{-1}
  E^a_mu = Re(Psi^dagger Q_a D_mu Psi),  K_a = I3 x (I, alpha_i),  Q_a = S x (I, alpha_i)
  A_0 = 0, A_k = G(x) spin_k(x) x I4;  g = 4 - h Psi^dagger (Z x beta) Psi / 2
"""
import json, itertools, sys
from pathlib import Path
import mpmath as mp
import sympy as s

mp.mp.dps = 80
ORD = 5
D = Path(sys.argv[1])

# ---------- Hintergrund, unabhaengig aufgeschrieben ----------
t, x, y, z, tau = s.symbols('t x y z tau', real=True)
N = s.Integer(16); I = s.I
rho = s.sqrt(x**2 + y**2)
vv = s.Matrix([x, y, z]) / t
gam = 1 / s.sqrt(1 - vv.dot(vv))
th = s.asin(8 * t / N) / 2
c, d_, Del = s.cos(th), s.sin(th), s.cos(2 * th)
pp = 3 * c / (2 * rho * Del); qq = -3 * d_ / (2 * rho * Del)
Gm = s.Matrix([[0, 0, pp], [0, 0, qq], [pp, qq, 0]])
spin = [-y / rho, x / rho, 0]
hm = 16 * gam / (N * Del)
sx = s.Matrix([[0, 1], [1, 0]]); sy = s.Matrix([[0, -I], [I, 0]]); sz = s.diag(1, -1)
def blk(p_):
    z2 = s.zeros(2); return s.Matrix(s.BlockMatrix([[z2, p_], [p_, z2]]))
al = [blk(sx), blk(sy), blk(sz)]
beta = s.diag(1, 1, -1, -1)
Y3 = s.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]])
S3 = s.Matrix([[0, s.Rational(1, 2), 0], [s.Rational(1, 2), 0, 0], [0, 0, 0]])
Z3 = s.diag(1, -1, 0)
kron = s.kronecker_product
Kmats = [kron(s.eye(3), m) for m in [s.eye(4)] + al]
Qmats = [kron(S3, m) for m in [s.eye(4)] + al]
YB = kron(Y3, beta); ZB = kron(Z3, beta)

def mpmat(M):
    return mp.matrix([[mp.mpc(complex(M[i, j])) if M[i, j].is_number and M[i, j].is_Rational is False and False else
                       mp.mpc(str(s.re(s.N(M[i, j], 90))), str(s.im(s.N(M[i, j], 90)))) for j in range(M.cols)] for i in range(M.rows)])
K = [mpmat(m) for m in Kmats]; Q = [mpmat(m) for m in Qmats]; YBm = mpmat(YB); ZBm = mpmat(ZB)

# ---------- Feldkoeffizienten ----------
first70 = json.loads((D / 'precision-first-jet-70.json').read_text())
p0 = [s.Rational(v) for v in first70['point']]
psi0 = mp.matrix([mp.mpc(*v) for v in first70['psi']])
root = json.loads((D / 'precision-completed-root-result.json').read_text())
second = json.loads((D / 'precision-second-jet-result.json').read_text())
omega = json.loads((D / 'precision-omega-repair-result.json').read_text())
fifth = json.loads((D / 'precision-fifth-gate-repair-result.json').read_text())
def unpack(packed, deg):
    vals = [mp.mpf(v) for v in packed]; out = {}
    for i, a in enumerate(itertools.combinations_with_replacement(range(4), deg)):
        alpha = tuple(a.count(m) for m in range(4))
        out[alpha] = mp.matrix([mp.mpc(vals[i * 24 + k], vals[i * 24 + k + 12]) for k in range(12)])
    return out
coef = {(0, 0, 0, 0): psi0}
coef.update(unpack(root['first_derivatives_real_packed'], 1))   # Taylor-Koeffizient = erste Ableitung
coef.update(unpack(second['second_coefficients_real_packed'], 2))
coef.update(unpack(omega['third_coefficients_real_packed'], 3))
coef.update(unpack(fifth['fourth_coefficients_real_packed'], 4))
coef.update(unpack(fifth['fifth_coefficients_real_packed'], 5))
assert len(coef) == 1 + 4 + 10 + 20 + 35 + 56

# ---------- Potenzreihen in tau bis Ordnung ORD ----------
def ser_bg(expr, dvec):
    e = expr.subs({t: p0[0] + tau * dvec[0], x: p0[1] + tau * dvec[1], y: p0[2] + tau * dvec[2], z: p0[3] + tau * dvec[3]}, simultaneous=True)
    out = []; cur = e
    for k in range(ORD + 1):
        val = s.N(cur.subs(tau, 0), 90)
        out.append(mp.mpc(str(s.re(val)), str(s.im(val))))
        cur = s.diff(cur, tau) / (k + 1)
    return out

def poly_series(dvec):
    """Psi(p + tau d) und d_mu Psi(p + tau d) als Reihen: Liste von 12-Vektoren je Ordnung."""
    psi = [mp.zeros(12, 1) for _ in range(ORD + 1)]
    dpsi = [[mp.zeros(12, 1) for _ in range(ORD + 1)] for _ in range(4)]
    for alpha, cvec in coef.items():
        deg = sum(alpha)
        mono = mp.mpf(1)
        for m in range(4): mono *= mp.mpf(dvec[m]) ** alpha[m]
        psi[deg] += mono * cvec
        for mu in range(4):
            if alpha[mu]:
                beta_ = list(alpha); beta_[mu] -= 1
                m2 = alpha[mu] * mp.fprod(mp.mpf(dvec[n]) ** beta_[n] for n in range(4))
                if deg - 1 <= ORD: dpsi[mu][deg - 1] += m2 * cvec
    return psi, dpsi

def mul(a, b):  # Reihenprodukt von Listen (Matrizen/Skalare)
    return [sum((a[i] * b[k - i] for i in range(k + 1)), a[0] * 0 if not isinstance(a[0], mp.matrix) else None) if False else
            _acc([a[i] * b[k - i] for i in range(k + 1)]) for k in range(ORD + 1)]
def _acc(lst):
    r = lst[0]
    for v in lst[1:]: r = r + v
    return r

def check(dvec):
    psi, dpsi = poly_series(dvec)
    hS = ser_bg(hm, dvec)
    Gs = [[ser_bg(Gm[i, j], dvec) if Gm[i, j] != 0 else None for j in range(3)] for i in range(3)]
    spS = [ser_bg(sp, dvec) if sp != 0 else None for sp in spin]
    # A_mu als 12x12-Reihe
    A = [[mp.zeros(12) for _ in range(ORD + 1)]]
    for k in range(3):
        ser = []
        for o in range(ORD + 1):
            M = mp.zeros(12)
            if spS[k] is not None:
                for i in range(3):
                    for j in range(3):
                        if Gs[i][j] is None: continue
                        val = sum(Gs[i][j][a] * spS[k][o - a] for a in range(o + 1))
                        for r in range(4): M[4 * i + r, 4 * j + r] = val
            ser.append(M)
        A.append(ser)
    cov = [[dpsi[mu][o] + mp.j * _acc([A[mu][a] * psi[o - a] for a in range(o + 1)]) for o in range(ORD + 1)] for mu in range(4)]
    psiH = [v.H for v in psi]
    E = []
    for o in range(ORD + 1):
        M = mp.zeros(4)
        for a in range(4):
            for mu in range(4):
                M[a, mu] = mp.re(_acc([(psiH[i] * Q[a] * cov[mu][o - i])[0] for i in range(o + 1)]))
        E.append(M)
    V0 = E[0] ** -1; V = [V0]
    for o in range(1, ORD + 1):
        V.append(-V0 * _acc([E[j] * V[o - j] for j in range(1, o + 1)]))
    F = []
    for o in range(ORD + 1):
        acc = mp.zeros(12, 1)
        for i in range(o + 1):
            for mu in range(4):
                for a in range(4):
                    acc += mp.j * V[i][mu, a] * (K[a] * cov[mu][o - i])
        acc -= _acc([hS[i] * (YBm * psi[o - i]) for i in range(o + 1)])
        F.append(acc)
    g = []
    for o in range(ORD + 1):
        quad = _acc([(psiH[i] * ZBm * psi[o - i])[0] for i in range(o + 1)])
        hq = _acc([hS[i] * _acc([(psiH[j] * ZBm * psi[o - i - j])[0] for j in range(o - i + 1)]) for i in range(o + 1)])
        g.append((4 if o == 0 else 0) - hq / 2)
    nF = [max(abs(v) for v in F[o]) for o in range(ORD)]       # F bis Ordnung 4
    ng = [abs(g[o]) for o in range(ORD + 1)]                    # g bis Ordnung 5
    return nF, ng, float(abs(mp.det(E[0])))

out = []
for dvec in [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, -2, 3, -1], [2, 1, -1, 3], [-1, 1, 1, 2]]:
    nF, ng, det = check(dvec)
    row = {'direction': dvec, 'F_orders0_4_max': [mp.nstr(v, 6) for v in nF], 'g_orders0_5': [mp.nstr(v, 6) for v in ng], 'detE0': det}
    out.append(row); print(json.dumps(row), flush=True)
Path(sys.argv[2]).write_text(json.dumps({'contract': 'Unabhaengige Reihen-Auswertung von F (bis Ordnung 4) und g (bis Ordnung 5) am reparierten Keim; eigene Modell- und Reihenimplementierung, 80 Stellen.', 'checks': out}, indent=2))
