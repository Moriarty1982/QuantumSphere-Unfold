"""k383 (Test H181): zwei Lesarten des M-Zustands, b/a = beta_sym (W) gegen b/a = beta_sym^2 (A).

Vorab-Notiz: notes/research/predictions/Vorab_Notiz_H181_Zwei_Lesarten_des_M_Zustands.md
Teil 1 (nicht blind): Woerterbuch D an beiden Zustaenden. Teil 1b (Erkundung): Woerterbuch D' und Zaehlung der kappa-Kandidaten.
Teil 2 (blind): Maskenscan mit dem unveraenderten Code von k105 bei drei Werten von eps.
Aufruf: python k383_test_h181.py [--ohne-maske]
"""
import pathlib, sys
from mpmath import mp, mpf, atanh, tanh, cosh, sinh, exp, sqrt, log

mp.dps = 30
B = mpf("0.5494056410")
GL = (1 + B**2) / (1 - B**2)
MZ, DMZ = mpf("91.1876"), mpf("0.0018")       # 1,8 MeV aus m_Z auf m_W (k358)
S13 = mpf("0.02215")
KSTAR = mpf("1.2039")

def mh(k):
    r = (16 * k**2 - mpf("2.77")) / mpf("20.42")
    return mpf("125.20") * sqrt(r) if r > 0 else None

def z(v, m, s):
    return (v - m) / s

def urteil(zz):
    a = abs(zz)
    return "traegt" if a < 2 else ("widerlegt" if a > 3 else "offen")

ETA = {"W (b/a = beta_sym)": atanh(B), "A (b/a = beta_sym^2)": atanh(B**2)}
print(f"beta_sym = {B}, gamma_L = {mp.nstr(GL, 12)}")
for n, e in ETA.items():
    print(f"  {n}: eta = {mp.nstr(e, 9)}, cosh 2eta = {mp.nstr(cosh(2*e), 9)}, e^(2eta) = {mp.nstr(exp(2*e), 9)}, tanh^2 = {mp.nstr(tanh(e)**2, 9)}")
print(f"  Identitaeten: cosh 2eta_A - (gamma_L + 1/gamma_L)/2 = {mp.nstr(cosh(2*ETA['A (b/a = beta_sym^2)']) - (GL + 1/GL)/2, 3)};"
      f"  e^(2eta_A) - gamma_L = {mp.nstr(exp(2*ETA['A (b/a = beta_sym^2)']) - GL, 3)};  cosh 2eta_W - gamma_L = {mp.nstr(cosh(2*ETA['W (b/a = beta_sym)']) - GL, 3)}")

def woerterbuch(name, c, om, eps, kap):
    print(f"\n--- {name} ---")
    fehl = 0
    mw = MZ * c / sqrt(1 + c**2)
    zz = z(mw, mpf("80.3625"), sqrt(mpf("0.0077")**2 + DMZ**2))
    print(f"  Q1 m_W = {mp.nstr(mw, 7)} GeV (cot theta_W = {mp.nstr(c, 7)}, sin^2 theta_W = {mp.nstr(1/(1+c**2), 5)}); z = {mp.nstr(zz, 4)} -> {urteil(zz)}")
    fehl += urteil(zz) == "widerlegt"
    z1, z2 = z(om, mpf("0.2975"), mpf("0.0086")), z(om, mpf("0.315"), mpf("0.007"))
    u = "widerlegt" if min(abs(z1), abs(z2)) > 3 else ("traegt" if max(abs(z1), abs(z2)) < 2 else "offen")
    print(f"  Q2 Omega_M = {mp.nstr(om, 6)}; z(DESI) = {mp.nstr(z1, 4)}, z(Planck) = {mp.nstr(z2, 4)} -> {u}")
    fehl += u == "widerlegt"
    s12 = om / (1 - S13); zz = z(s12, mpf("0.3036"), mpf("0.0064"))
    print(f"  Q3 sin^2 theta_12 = {mp.nstr(s12, 6)}; z(JUNO) = {mp.nstr(zz, 4)} -> {urteil(zz)}")
    fehl += urteil(zz) == "widerlegt"
    inn = mpf("0.611") <= eps <= mpf("0.647")
    print(f"  Q4 Maske eps = {mp.nstr(eps, 7)}; Fenster 0,611 bis 0,647 -> {'im Fenster' if inn else 'ausserhalb'}")
    fehl += not inn
    m = mh(kap); ab = (m / mpf("125.20") - 1) * 100
    print(f"  Q5 kappa = {mp.nstr(kap, 7)} -> m_h = {mp.nstr(m, 6)} GeV ({mp.nstr(ab, 3)} %) -> {'traegt (kein Beleg)' if abs(ab) < 5 else ('widerlegt' if abs(ab) > 10 else 'offen')}")
    print(f"  verfehlt von Q1 bis Q4: {int(fehl)}")
    return int(fehl)

print("\n=== Teil 1: Woerterbuch D (cot theta_W = cosh 2eta, Omega_M = tanh^2 eta, eps = eta, kappa = cosh 2eta) ===")
F = {}
for n, e in ETA.items():
    F[n] = woerterbuch("Lesart " + n + ", Woerterbuch D", cosh(2*e), tanh(e)**2, e, cosh(2*e))
fa = F["A (b/a = beta_sym^2)"]
print(f"\nUrteil H181 (Teil 1): Lesart A verfehlt {fa} von Q1 bis Q4 -> {'widerlegt' if fa >= 2 else ('bestaetigt' if fa == 0 else 'offen')}")

print("\n=== Teil 1b (Erkundung): Woerterbuch D' fuer A (cot theta_W = e^(2eta), Omega_M = tanh eta, eps = 2eta, kappa = cosh 2eta) ===")
eA = ETA["A (b/a = beta_sym^2)"]
woerterbuch("Lesart A, Woerterbuch D'", exp(2*eA), tanh(eA), 2*eA, cosh(2*eA))
print(f"  Portgewichte unter D' (Gewicht = Amplitude^2): {mp.nstr(1/(1+B**4), 5)} : {mp.nstr(B**4/(1+B**4), 5)};"
      f" Konvention F verlangt {mp.nstr(1/(1+B**2), 5)} : {mp.nstr(B**2/(1+B**2), 5)}")
print(f"  eps: 2 eta_A = ln gamma_L = {mp.nstr(2*eA, 9)} gegen eta_W = {mp.nstr(ETA['W (b/a = beta_sym)'], 9)}; Unterschied {mp.nstr((2*eA/ETA['W (b/a = beta_sym)'] - 1)*100, 3)} %")

print("\n=== Teil 1b: feste Liste einfacher Funktionen als kappa (Fenster 5 % um kappa* = 1,2039) ===")
def liste(e):
    out = {}
    for lab, x in (("eta", e), ("2eta", 2*e)):
        for fn, f in (("tanh", tanh), ("sinh", sinh), ("cosh", cosh), ("exp", exp), ("exp-", lambda t: exp(-t))):
            v = f(x); out[f"{fn}({lab})"] = v; out[f"1/{fn}({lab})"] = 1 / v
    return out
for n, e in ETA.items():
    L = liste(e)
    tr = {k: v for k, v in L.items() if abs(v / KSTAR - 1) < mpf("0.05")}
    print(f"  Lesart {n}: {len(L)} Kandidaten, {len(tr)} im Fenster")
    for k, v in sorted(tr.items(), key=lambda kv: abs(kv[1] / KSTAR - 1)):
        print(f"    kappa = {k} = {mp.nstr(v, 7)} ({mp.nstr((v/KSTAR - 1)*100, 3)} %), m_h = {mp.nstr(mh(v), 6)} GeV")

if "--ohne-maske" not in sys.argv:
    print("\n=== Teil 2 (blind): Maskenscan, unveraenderter Code k105 mit drei Werten von eps ===", flush=True)
    REPO = pathlib.Path(__file__).resolve().parents[4]
    src = (REPO / "notes/research/v4_10_0_r63_r64/llm/k105_h46_exakt.py").read_text()
    old = 'K = {"artanh(beta exakt)": float(np.arctanh(0.549406)), "artanh(0.5493)": float(np.arctanh(0.5493))}'
    new = ('K = {"eta_W = artanh(beta_sym)": float(np.arctanh(0.5494056410)), "eta_A = artanh(beta_sym^2)": float(np.arctanh(0.5494056410**2)), '
           '"2 eta_A = ln gamma_L": float(2*np.arctanh(0.5494056410**2))}')
    assert src.count(old) == 1, "Kandidatenzeile in k105 nicht gefunden"
    exec(compile(src.replace(old, new), "k105_mit_drei_eps", "exec"), {"__name__": "__main__"})
