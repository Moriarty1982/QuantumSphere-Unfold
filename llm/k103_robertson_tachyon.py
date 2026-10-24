"""r63: (a) Robertson-Saettigung fuer |j,m>, (b) Tachyon am Boden im bewegten Frame. Reine Mathematik/Kinematik, keine Vorhersage."""
import sympy as sp
def J(j):
    j = sp.Rational(j); ms = [j - k for k in range(int(2*j)+1)]; n = len(ms)
    Jp = sp.zeros(n)
    for a in range(1, n):  # J+ |m> = sqrt(j(j+1)-m(m+1)) |m+1>
        m = ms[a]; Jp[a-1, a] = sp.sqrt(j*(j+1) - m*(m+1))
    Jm = Jp.T; Jx = (Jp + Jm)/2; Jy = (Jp - Jm)/(2*sp.I); Jz = sp.diag(*ms)
    return ms, Jx, Jy, Jz
print("(a) Delta Jx * Delta Jy gegen |<Jz>|/2  (hbar = 1)")
fehler = 0
for twoj in range(1, 13):
    ms, Jx, Jy, Jz = J(sp.Rational(twoj, 2))
    for i, m in enumerate(ms):
        e = sp.zeros(len(ms), 1); e[i] = 1
        ev = lambda A: sp.simplify((e.T*A*e)[0])
        vx = ev(Jx*Jx) - ev(Jx)**2; vy = ev(Jy*Jy) - ev(Jy)**2
        prod = sp.sqrt(sp.simplify(vx*vy)); bound = abs(m)/2
        formel = (sp.Rational(twoj,2)*(sp.Rational(twoj,2)+1) - m**2)/2
        satt = sp.simplify(prod - bound) == 0
        if sp.simplify(prod - formel) != 0 or satt != (abs(m) == sp.Rational(twoj,2)) or prod < bound: fehler += 1
    if twoj <= 4: print(f"  j = {sp.Rational(twoj,2)}: saettigend m =", [m for m in ms if abs(m) == sp.Rational(twoj,2)])
print("  j = 1/2 ... 6 geprueft, Abweichungen:", fehler)
_, Jx, _, _ = J(sp.Rational(1,2)); print("  Spin 1/2: Delta Jx =", sp.sqrt((Jx*Jx)[0,0]))
print("(b) Tachyon am Boden E = 0, p = mu, Boost mit u = beta_sym")
u, mu = sp.symbols('u mu', positive=True); g = 1/sp.sqrt(1-u**2)
E2, p2 = g*(0 - u*mu), g*(mu - u*0)
print("  E' =", sp.simplify(E2), "  p' =", sp.simplify(p2), "  v' = p'/E' =", sp.simplify(p2/E2), "  E'^2-p'^2 =", sp.simplify(E2**2-p2**2))
b = 0.549406; print(f"  bei beta_sym = {b}: |v'| = {1/b:.5f}, E'/mu = {-b/(1-b*b)**0.5:.5f}")
v = sp.symbols('v'); print("  E(v) = mu/sqrt(v^2-1): dE/dv =", sp.simplify(sp.diff(mu/sp.sqrt(v**2-1), v)), ", Grenzwert v->oo:", sp.limit(mu/sp.sqrt(v**2-1), v, sp.oo))
print("(c) Wo sitzt der Tachyon-Boden? Boden in Frame X: Rapiditaet eta_X + i*pi/2 relativ R; Geschwindigkeit in Frame Y = coth(eta_X - eta_Y), unendlich bei eta_X = eta_Y")
import mpmath as m
eta = m.atanh(m.mpf('0.549406'))
v = lambda d: "unendlich" if d == 0 else m.nstr(1/m.tanh(d), 6)
for name, eX in [("Boden in R (Photon)", m.mpf(0)), ("Boden in M (+eta)", eta), ("Boden im Spiegel -eta", -eta)]:
    print(f"  {name:22s}: v in R = {v(eX):>9s}  v in M = {v(eX-eta):>9s}  Realteil-Abstand zu M = {m.nstr(abs(eX-eta),5)}  cosh(Abstand) = {m.nstr(m.cosh(eX-eta),6)}")
print("  gamma_L (H47, exakt) =", m.nstr(m.mpf('0.237532957966')/(m.log(2)/(m.pi*m.sqrt(3))),6), "  cosh 2 eta =", m.nstr(m.cosh(2*eta),6))
