"""k212: Test H95 - Machbarkeit von I3 mit dynamischem Zweig-Gas (Variante A) auf FRW.
Vorab-Notiz llm/Vorab_Notiz_H95_Zweiggas_FRW.md (Commit 9eb4e40).
Aufruf (aus llm/): python k212_zweiggas_frw.py [ausgabe.json]
"""
import json, sys
import numpy as np

Om_r, Om_b, z_rec = 9.1e-5, 0.049, 1090.0
a_rec = 1/(1 + z_rec)
rs = np.linspace(0.1, 5, 60)
aths = np.exp(np.linspace(np.log(1 + 1e-6), np.log(100), 60))
qs = np.linspace(0, 0.999, 40)                     # kappa1 / a_th
agrid = np.exp(np.linspace(np.log(1e-8), 0, 400))


def fM(a, k1): return np.sqrt(1 + (k1/a)**2)
def fT(a, ath): return np.sqrt(np.maximum((ath/a)**2 - 1, 0))


hits, best, n_tot, n_pos = [], None, 0, 0
for r in rs:
    for ath in aths:
        for q in qs:
            n_tot += 1
            k1 = q*ath
            den = fM(1.0, k1) - r*fT(1.0, ath)
            if den <= 0:
                continue
            OD = (1 - Om_r - Om_b)/den
            rho = Om_r*agrid**-4 + Om_b*agrid**-3 + OD*agrid**-3*(fM(agrid, k1) - r*fT(agrid, ath))
            if np.any(rho <= 0):
                continue
            n_pos += 1
            ratio = OD*(fM(a_rec, k1) - r*fT(a_rec, ath))/Om_b
            p0 = Om_r/3 + OD*(k1**2/(3*fM(1.0, k1)) - r*ath**2/(3*max(fT(1.0, ath), 1e-300)))
            w0 = p0/1.0
            ok = (4.32 <= ratio <= 6.48) and (-0.8 <= w0 <= -0.6)
            d = abs(np.log(max(ratio, 1e-30)/5.4)) + abs(w0 + 0.7)
            rec = dict(r=float(r), a_th=float(ath), q=float(q), Omega_D=float(OD), ratio_rec=float(ratio), w0=float(w0), dist=float(d))
            if ok:
                hits.append(rec)
            if best is None or d < best['dist']:
                best = rec
out = dict(grid=[len(rs), len(aths), len(qs)], n_total=n_tot, n_positive=n_pos, n_hits=len(hits), hits=hits[:50], best=best)
# Zusatz: bester Punkt unter den positiven mit w0 in [-0.8,-0.6] (ohne Rekombinationskriterium) und umgekehrt
print(f'Gitter {out["grid"]}, Punkte {n_tot}, positiv {n_pos}, Treffer {len(hits)}')
print('naechster Punkt:', best)
if len(sys.argv) > 1:
    json.dump(out, open(sys.argv[1], 'w'), indent=1)
