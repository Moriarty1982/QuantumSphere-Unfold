"""k437 (Test H223): Bindet ein Elternterm u^2 (u kubische Invariante) das Vorzeichen des Zweigwahl-Terms?
Vorab-Notiz Vorab_H223_Elternterm_Vorzeichen.md (vor der Rechnung committet).
Zirkulante: Eigenwerte phi + 2 r cos(delta + 2 pi k/3); K = 2/3 <=> r = phi/sqrt2.
Aufruf aus diesem Ordner: python3 k437_test_h223.py > k437_out.txt
"""
import numpy as np
import sympy as sp

ph, r, d, C, x, y, z = sp.symbols('phi r delta C x y z', real=True)
lam = [ph + 2 * r * sp.cos(d + 2 * sp.pi * k / 3) for k in range(3)]


def red(e):
    """auf Polynom in phi, r, C = cos 3 delta reduzieren"""
    e = sp.expand(sp.expand_trig(sp.expand(e)))
    e = sp.simplify(sp.expand(sp.fu(e)))
    e = sp.expand(e.subs(sp.cos(3 * d), C))
    return sp.expand(sp.simplify(e))


e1 = red(sum(lam)); e2 = red(lam[0] * lam[1] + lam[1] * lam[2] + lam[0] * lam[2]); e3 = red(lam[0] * lam[1] * lam[2])
T2 = red(sum(l**2 for l in lam)); T3 = red(sum(l**3 for l in lam))
print("Zirkulante: e1 =", e1, "; e2 =", e2, "; e3 = det =", e3, "; Tr W^2 =", T2, "; Tr W^3 =", T3)
DSTAR = 0.2222220470731; P = np.pi / 12 - DSTAR
BR = {"Im (alphap=+1)": (5 * np.pi / 4 + P, np.pi / 4 + P), "Re (alphap=-1)": (np.pi / 2 + P, 3 * np.pi / 2 + P)}


def choose(f, label):
    """f: Funktion von delta (phi=1, r=1/sqrt2); kleinerer Wert = gewaehlter Zweig; Daten-Zweig zuerst in BR"""
    out = []
    for s, (D, O) in BR.items():
        fd, fo = f(D), f(O)
        out.append((s, fd - fo))
    ok = all(v < 0 for _, v in out)
    txt = "; ".join(f"{s}: V(Daten)-V(andere) = {v:+.5f}" for s, v in out)
    return ok, txt


print("\n" + "=" * 86)
print("a (nicht blind)  beta3 = kappa * alphap mit sektorunabhaengigem kappa")
print("=" * 86)
for kap in (+1, -1):
    res = []
    for s, (D, O), ap in ((k, v, (+1 if k.startswith("Im") else -1)) for k, v in BR.items()):
        b3 = kap * ap
        dv = b3 * (np.cos(3 * D) - np.cos(3 * O))
        res.append(f"{s}: beta3 = {b3:+d}, V(Daten)-V(andere) = {dv:+.4f} {'Daten' if dv < 0 else 'FALSCH'}")
    print(f"  kappa = {kap:+d}: " + " | ".join(res))
print("  -> in jedem Fall genau ein Sektor falsch: Bindung an alphap mit festem kappa ausgeschlossen")

print("\n" + "=" * 86)
print("b/c  Bausteine u = x e1^3 + y e1 Tr W^2 + z det W; J-Projektion von u^2: beta3 = Koeffizient von phi^3 r^3 C")
print("=" * 86)
cands = {"(i) det W": e3, "(ii) Tr W^3": T3, "(iii) (Tr W)^3": e1**3, "(iv) det(W - TrW/3)": None, "(v) Tr W * Tr W^2": e1 * T2,
         "(vi) Tr W^3 - (Tr W)^3/9": T3 - e1**3 / 9, "(vii) e1 e2 - 9 e3": e1 * e2 - 9 * e3}
# (iv): Eigenwerte der spurfreien Matrix
lam0 = [2 * r * sp.cos(d + 2 * sp.pi * k / 3) for k in range(3)]
cands["(iv) det(W - TrW/3)"] = red(lam0[0] * lam0[1] * lam0[2])
anyok = False
for nm, u in cands.items():
    u = sp.expand(red(u))
    X = u.coeff(ph, 3).subs({r: 0, C: 0}); Z = sp.expand(u).coeff(r, 3).coeff(C, 1).subs(ph, 0)
    u2 = sp.expand(u**2)
    b3 = u2.coeff(ph, 3).coeff(r, 3).coeff(C, 1)
    fJ = lambda dd, b=float(b3): b * np.cos(3 * dd)                       # J-projizierter delta-Teil
    ufun = sp.lambdify(d, u.subs({ph: 1, r: 1 / sp.sqrt(2), C: sp.cos(3 * d)}), 'numpy')
    fF = lambda dd: ufun(dd) ** 2                                          # volles u^2 bei K = 2/3
    okJ, tJ = choose(fJ, nm) if b3 != 0 else (False, "beta3 = 0: keine Wahl")
    okF, tF = choose(fF, nm)
    anyok |= okJ
    print(f"  {nm:26s}: u = {u};  X = {X}, Z = {Z}, beta3(J) = {b3}")
    print(f"      J-projiziert: {'DATEN-Zweig in beiden' if okJ else 'nicht beide'} ({tJ})")
    print(f"      volles u^2:   {'DATEN-Zweig in beiden' if okF else 'nicht beide'} ({tF})")
print(f"  Kriterium c: benannter Kandidat mit beta3 < 0 nach J-Projektion: {'JA' if anyok else 'keiner'}")

ug = sp.expand(x * red(e1**3) + y * red(e1 * T2) + z * e3)
Xg = ug.coeff(ph, 3).subs({r: 0, C: 0}); Zg = ug.coeff(r, 3).coeff(C, 1).subs(ph, 0)
b3g = sp.factor(sp.expand(ug**2).coeff(ph, 3).coeff(r, 3).coeff(C, 1))
print(f"  allgemein: X = {sp.expand(Xg)}, Z = {Zg}, beta3(J) = {b3g}")
rng = np.random.default_rng(223); v = rng.normal(size=(400000, 3)); v /= np.linalg.norm(v, axis=1)[:, None]
fb = sp.lambdify((x, y, z), b3g, 'numpy')
print(f"  Anteil der Richtungen (x, y, z) mit beta3 < 0: {np.mean(fb(v[:,0], v[:,1], v[:,2]) < 0):.4f}  (Bedingung: z (27 x + 9 y + z) < 0)")

print("\n" + "=" * 86)
print("d (blind)  liefern Spur-/Determinanten-Bausteine cos delta oder den Spin-1-Term?")
print("=" * 86)
for nm, e in (("e1", e1), ("e2", e2), ("e3", e3), ("Tr W^2", T2), ("Tr W^3", T3)):
    print(f"  {nm}: freie Symbole nach Reduktion {sorted(map(str, e.free_symbols))}  (delta nur ueber C = cos 3 delta)")
print("  -> jede Funktion von Spur und Determinante haengt von delta nur ueber cos 3 delta ab: c4 = 0, kein cos 2(delta - chi), keine Bindung an alphap")
