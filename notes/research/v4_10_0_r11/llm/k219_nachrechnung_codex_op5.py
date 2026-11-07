"""k219: Nachrechnung der tragenden Aussagen der Codex-OP5-Rekonstruktion (GitHub 4ae32c9, 6./7.11.2026).

Runde v4.10.0-r11. Unabhaengige Pruefung mit eigenem Code (SymPy/NumPy), keine Vorab-Notiz, kein Test.
Geprueft werden die Formeln, auf die sich die Einordnung stuetzt:
  A  Zustandsfamilie gleicher Skala/Orientierung mit beliebigem Eigenwertverhaeltnis q (op5_state_selection_exploration)
  B  Energiegewichte: Anteil f_- = w_- q/(w_+ + w_- q) (ebd.)
  C  Saettigung (j-|m|)(j+|m|+1); |1,1> saettigt; endliche Spinmengen geben verschiedene gamma (op5_spin_selection_audit)
  D  Markov-Kaskade r31: Ausflussanteil = eingesetztes q, Besetzungsverhaeltnis q r (op5_denominator_audit)
  E  Scherungs-Gegenbeispiel zum Rueckweg-Mittel (qam_quelle_rueckweg_auslesung)
  F  r27-Richtungsauslesung: m, d, quadratisches Register, Portkollision (qam_r27_richtungsreadout)
  G  s-Schalen: Dualitaet erhaelt |s|, Kompensatorbild nicht null (qsc_back_to_basic_idea)
  H  doppelte Rapiditaet: gamma_L = 1/r = cosh 2 eta_ref ist Lorentzfaktor zwischen zwei Profilen mit Gegenfluss
Aufruf: python llm/k219_nachrechnung_codex_op5.py > llm/k219_out.txt
"""
import math

import numpy as np
import sympy as sp

out = []


def ok(name, cond, info=""):
    out.append(f"[{'OK' if cond else 'FEHLER'}] {name}" + (f"  ({info})" if info else ""))
    return cond


# ---------- A: Zustandsfamilie ----------
q = sp.symbols("q", positive=True)
E = sp.Matrix([1 / sp.sqrt(1 + q), 0, 0])
B = sp.Matrix([0, sp.sqrt(q / (1 + q)), 0])
F = E.row_join(B)
G = sp.simplify(F.T * F)
ok("A1 G_q = diag(1/(1+q), q/(1+q))", sp.simplify(G - sp.diag(1 / (1 + q), q / (1 + q))) == sp.zeros(2))
ok("A2 tr G = 1, E.B = 0", sp.simplify(G.trace() - 1) == 0 and sp.simplify(E.dot(B)) == 0)
ok("A3 s_q = (1-q)/(1+q)", sp.simplify(E.dot(E) - B.dot(B) - (1 - q) / (1 + q)) == 0)
ok("A4 Eigenwertverhaeltnis = q", sp.simplify(G[1, 1] / G[0, 0] - q) == 0)
p_plus = sp.Rational(1, 2) + E.dot(B) / G.trace()
ok("A5 sigma_x-Port p+ = 1/2 fuer alle q", sp.simplify(p_plus - sp.Rational(1, 2)) == 0)

# ---------- B: Energiegewichte ----------
wp, wm = sp.symbols("w_p w_m", positive=True)
lp, lm = 1 / (1 + q), q / (1 + q)
fm = sp.simplify(wm * lm / (wp * lp + wm * lm))
ok("B1 f_- = w_- q/(w_+ + w_- q)", sp.simplify(fm - wm * q / (wp + wm * q)) == 0)
sol = sp.solve(sp.Eq(fm.subs(wp, 1), q), wm)
ok("B2 f_- = q verlangt w_-/w_+ = 1/(1-q)", len(sol) == 1 and sp.simplify(sol[0] - 1 / (1 - q)) == 0, str(sol))
qv = 0.30185
ok("B3 Beispiel q = beta^2: Gewichte (1,1) und (1,2) geben verschiedene Anteile",
   abs(qv / (1 + qv) - 2 * qv / (1 + 2 * qv)) > 0.1, f"{qv/(1+qv):.5f} vs {2*qv/(1+2*qv):.5f}")

# ---------- C: Saettigung und Spinmengen ----------
j, m = sp.symbols("j m", nonnegative=True)
ok("C1 j(j+1)-m^2-m = (j-m)(j+m+1)", sp.expand(j * (j + 1) - m**2 - m - (j - m) * (j + m + 1)) == 0)
sat = all(sp.Rational(jj * (jj + 1) - jj**2, 2) == sp.Rational(jj, 2) for jj in [sp.Rational(1, 2), 1, sp.Rational(3, 2), 2])
ok("C2 |j,j> saettigt fuer j = 1/2, 1, 3/2, 2", sat)


def gamma_of(Jset):
    f = lambda g: sum(2 * math.exp(-2 * math.pi * g * math.sqrt(jj * (jj + 1))) for jj in Jset) - 1
    lo, hi = 1e-6, 5.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if f(mid) > 0 else (lo, mid)
    return 0.5 * (lo + hi)


g1, g2 = gamma_of([0.5]), gamma_of([0.5, 1.0])
ok("C3 J1 = {1/2}: gamma = ln2/(pi sqrt3) (ABCK-Wert)", abs(g1 - math.log(2) / (math.pi * math.sqrt(3))) < 1e-10, f"{g1:.6f}")
ok("C4 J2 = {1/2, 1}: gamma strikt groesser", g2 > g1 + 1e-3, f"{g2:.6f}")

# ---------- D: Markov-Kaskade r31 ----------
r_ = sp.symbols("r", positive=True)
p8 = 1
f4, f2 = p8 * q, p8 * (1 - q)
ok("D1 Ausflussanteil f4/(f4+f2) = q (Eingabe)", sp.simplify(f4 / (f4 + f2) - q) == 0)
# r31.1(b): stationaer (p2, p4, p8) ~ (1, q r, r) mit Uebergaengen S8->S4 (q), S8->S2 (1-q), S4->S2 (1), S2->S8 (r)
P = sp.Matrix([[1 - r_, 0, r_], [1, 0, 0], [1 - q, q, 0]])  # Zeilen/Spalten: S2, S4, S8
pi = sp.Matrix([[1, q * r_, r_]])
ok("D2 (1, q r, r) ist stationaer (Reihenfolge p2, p4, p8)", sp.simplify(pi * P - pi) == sp.zeros(1, 3))
ok("D3 Besetzungsverhaeltnis p4/p2 = q r haengt am Rueckweg r", sp.simplify(pi[1] / pi[0] - q * r_) == 0)

# ---------- E: Scherung ----------
def A2(v):
    u, z, y = v
    return np.array([u, z + y, y])


def A2inv(v):
    u, z, y = v
    return np.array([u, z - y, y])


def readout(v):
    return np.array([v[0], v[1]])


res = []
for c in (np.array([1.0, 2.0, 1.0]), np.array([1.0, 2.0, -1.0])):
    f_, b_ = readout(A2(c)), readout(A2inv(c))
    res.append(((f_ + b_) / 2, f_, b_))
ok("E1 gleiches Mittel m = (1,2)", np.allclose(res[0][0], res[1][0]) and np.allclose(res[0][0], [1, 2]))
ok("E2 verschiedene Vorwaertswerte f = (1,3) bzw. (1,1)", np.allclose(res[0][1], [1, 3]) and np.allclose(res[1][1], [1, 1]))
ok("E3 Klasse u erhalten", all(np.isclose(rr[1][0], 1) and np.isclose(rr[2][0], 1) for rr in res))

# ---------- F: r27-Richtungsauslesung ----------
al = math.pi / 6
c2, s2 = math.cos(2 * al), math.sin(2 * al)
Rp = np.array([[c2, s2], [-s2, c2]])
Rm = np.array([[c2, -s2], [s2, c2]])
v = np.array([1.0, 0.0])
f_, b_ = Rp @ v, Rm @ v
mm, dd = (f_ + b_) / 2, (f_ - b_) / 2
Q = lambda w: np.outer(w, w)
ok("F1 (Q(f)+Q(b))/2 = Q(m)+Q(d)", np.allclose((Q(f_) + Q(b_)) / 2, Q(mm) + Q(dd)))
ok("F2 Spur vor Mittelung 1, Quadrat des Mittels 1/4", np.isclose(np.trace((Q(f_) + Q(b_)) / 2), 1) and np.isclose(mm @ mm, 0.25))
ok("F3 Differenz |d|^2 = sin^2(2 alpha) = 3/4", np.isclose(dd @ dd, 0.75))
port = lambda w: (1 + w[0]) / 2
pa = (port(Rp @ np.array([0, 1.0])), port(Rm @ np.array([0, 1.0])))
pb = (port(Rp @ np.array([0, -1.0])), port(Rm @ np.array([0, -1.0])))
ok("F4 Portkollision: Eingaben (0,+-1) gleiche Vorab- und Mittelwerte, vertauschte Richtungssignale",
   np.isclose(sum(pa) / 2, 0.5) and np.isclose(sum(pb) / 2, 0.5) and np.allclose(pa, pb[::-1]) and not np.allclose(pa, pb),
   f"{pa[0]:.6f}, {pa[1]:.6f}")
ok("F5 (2+sqrt3)/4 = Portsignal", np.isclose(max(pa), (2 + math.sqrt(3)) / 4))

# ---------- G: s-Schalen ----------
rng = np.random.default_rng(219)
Ev, Bv = rng.normal(size=3), rng.normal(size=3)
z = Ev + 1j * Bv
s = z @ z
a = 0.7
zr = np.exp(1j * a) * z
ok("G1 Dualitaet: s -> e^{2ia} s, |s| erhalten", np.isclose(zr @ zr, np.exp(2j * a) * s) and np.isclose(abs(zr @ zr), abs(s)))
ok("G2 Viertel-Drehung z -> iz: s -> -s", np.isclose((1j * z) @ (1j * z), -s))
zc = (Ev + Bv) * (1 + 1j) / 2  # C(z) = (z + J_B z)/2 mit J_B z = i conj(z)
ok("G3 Kompensatorbild C(z) = (z + i conj z)/2", np.allclose(zc, (z + 1j * np.conj(z)) / 2))
Ep = (Ev + Bv) / 2
ok("G4 s' = 2i|E'|^2 != 0 (nicht nullartig)", np.isclose(zc @ zc, 2j * (Ep @ Ep)) and abs(zc @ zc) > 1e-9)

# ---------- H: doppelte Rapiditaet ----------
def boost_fields(Ev, Bv, v):
    """Boost mit Geschwindigkeit v entlang e_z (c = 1), Felder senkrecht zu e_z."""
    g = 1 / math.sqrt(1 - v * v)
    vv = np.array([0, 0, v])
    Ep = g * (Ev + np.cross(vv, Bv))
    Bp = g * (Bv - np.cross(vv, Ev))
    return Ep, Bp


E0, B0 = np.array([2.0, 0, 0]), np.array([0, 1.0, 0])
E1, B1 = boost_fields(E0, B0, 0.5)
E2, B2 = boost_fields(E0, B0, 0.8)
ok("H1 v = 1/2: flussfreies Profil (E x B = 0)", np.allclose(np.cross(E1, B1), 0), f"E'={E1}, B'={B1}")
ok("H2 v = 4/5: E' = 2 e_x, B' = -e_y (Gegenfluss, gleiche Skala)", np.allclose(E2, [2, 0, 0]) and np.allclose(B2, [0, -1, 0]))
n0, s0 = E0 @ E0 + B0 @ B0, E0 @ E0 - B0 @ B0
rr = s0 / n0
ok("H3 1/r = cosh(2 artanh(1/2)) = Lorentzfaktor von v = 4/5", np.isclose(1 / rr, math.cosh(2 * math.atanh(0.5))) and np.isclose(1 / rr, 1 / math.sqrt(1 - 0.64)),
   f"1/r = {1/rr:.6f}")
beta = math.sqrt(0.30185)
gL = (1 + beta**2) / (1 - beta**2)
ok("H4 mit beta_sym: Register r = 1/gamma_L, Boost ins flussfreie Profil v = beta_sym (r17-Parametrisierung)",
   np.isclose(math.cosh(2 * math.atanh(beta)), gL), f"gamma_L = {gL:.6f}, beta_sym = {beta:.6f}")

print("k219 Nachrechnung Codex-OP5-Rekonstruktion (GitHub 4ae32c9)")
print("\n".join(out))
nf = sum(1 for o in out if o.startswith("[FEHLER]"))
print(f"\n{sum(1 for o in out if o.startswith('[OK]'))} OK, {nf} FEHLER")
