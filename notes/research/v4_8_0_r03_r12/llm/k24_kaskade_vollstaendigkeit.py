"""k24: Traegt die Kaskade die Fano-Struktur so, dass Vollstaendigkeit (TM1) erzwungen wird? (zu K19)
Reine Algebra. Vermutung aus K19.2: TM1 <=> Triole und Restspiegelung erzeugen den ganzen Fano-Punkt-Stabilisator."""
import numpy as np, contextlib, io, os
from collections import Counter
here = os.path.dirname(os.path.abspath(__file__))
with contextlib.redirect_stdout(io.StringIO()):
    exec(open(os.path.join(here, "k23_test_h6.py")).read())

def fano_img(M): return perm_of(M)
def elems(gens): return gen_elems(gens)
V = [np.eye(7)] + kernel                         # Vorzeichen-Kern in Stab(+e7)
key = lambda M: tuple(np.round(M).flatten())
Vk = {key(x) for x in V}
g3 = lifts3[3]
print("Vorzeichen-Kern in Stab(+e7):", len(V), "Elemente")

# 1) Woraus besteht <g3, h>?  Fano-Bild und Schnitt mit dem Vorzeichen-Kern
w, Vv = np.linalg.eig(cmat(g3)); i1 = int(np.argmin(abs(w - 1)))
types = {}
for M, C in zip(H, R):
    if ordn(C) != 2: continue
    ev, EV = np.linalg.eig(C); vals = np.round(ev.real).astype(int)
    s = [i for i in range(3) if list(vals).count(vals[i]) == 1][0]
    coef = np.linalg.solve(Vv, EV[:, s]); mod = np.abs(coef)**2/np.sum(np.abs(coef)**2)
    t = ("TM2" if np.allclose(mod, 1/3, atol=1e-6) else "TM1" if np.isclose(mod[i1], 2/3)
         else "TBM3" if np.isclose(mod[i1], 0) else "D96")
    types.setdefault(t, []).append(M)
print("\n1) Erzeugte Gruppe <g3, h>:")
for t, Ms in types.items():
    for M in Ms[:1]:
        E = elems([g3, M])
        img = {fano_img(x) for x in E}
        nV = sum(key(x) in Vk for x in E)
        print(f"  h = {t:4s}: |<g3,h>| = {len(E):3d}, Fano-Bild hat {len(img):2d} Elemente, enthaelt {nV} der 4 Kern-Elemente (inkl. Identitaet)")
fimg_stab = {fano_img(x) for x in H}
print(f"  zum Vergleich: Fano-Bild von ganz Stab(+e7) = {len(fimg_stab)} Elemente (S4)")
same = fano_img(types['TM1'][0]) in {fano_img(x) for x in types['TBM3']}
print("  Haben TM1- und TBM3-Lifts gleiche Fano-Bilder (je Zentrum)?", same)

# 2) Kern-Elemente als partielle e7-Konjugation auf den drei quaternionischen Linien durch e7
lines7 = [l for l in tri if 7 in l]
print("\n2) Linien durch e7:", lines7)
for K in kernel:
    d = np.diag(K).astype(int)
    desc = []
    for l in lines7:
        a, b = [u for u in l if u != 7]
        desc.append(f"{l}: {'Identitaet' if d[a-1] == 1 and d[b-1] == 1 else 'e7-Konjugation' if d[a-1] == -1 and d[b-1] == -1 else 'anders'}")
    print("  Kern-Element", d.tolist(), "->", "; ".join(desc))

# 3) Was sieht die Kaskade? Orthogonale Projektionen auf H_L = span(1, L) fuer L durch e7, und auf C = span(1, e7)
def proj(units):
    Pm = np.zeros((7, 7))
    for u in units: Pm[u-1, u-1] = 1
    return Pm
PL = [proj(l) for l in lines7]; PC = proj((7,))
comm_all = [M for M in H if all(np.allclose(M @ Pm, Pm @ M) for Pm in PL + [PC])]
set_pres = [M for M in H if all(any(np.allclose(M @ Pm @ M.T, Q) for Q in PL) for Pm in PL)]
print(f"\n3) Elemente von Stab(+e7), die mit jeder Kaskaden-Projektion kommutieren: {len(comm_all)}"
      f" (davon Vorzeichen-Kern: {sum(key(M) in Vk for M in comm_all)})")
print(f"   Elemente, die die Menge der drei Projektionen erhalten: {len(set_pres)} von {len(H)}")
print("   Kommutieren die Vorzeichen-Elemente mit allen Projektionen?",
      all(np.allclose(K @ Pm, Pm @ K) for K in kernel for Pm in PL + [PC]))
# Unterscheidet die Kaskade TM1- und TBM3-Lift? Paare mit gleichem Fano-Bild vergleichen
pairs = [(a, b) for a in types["TM1"] for b in types["TBM3"] if fano_img(a) == fano_img(b)]
print(f"   Paare (TM1, TBM3) mit gleichem Fano-Bild: {len(pairs)}")
for a, b in pairs:
    q = a @ b.T
    same_proj = all(np.allclose(a @ Pm @ a.T, b @ Pm @ b.T) for Pm in PL + [PC])
    print(f"   h_TM1 = Kern-Element * h_TBM3: {key(q) in Vk};  gleiche Wirkung auf alle Projektionen: {same_proj}")
