"""k409 (Test H199): Entsteht D/B ~ 1 (Down linear) aus dem Lauf der Kopplungen?
1-Schleifen-SM-RGEs fuer g1,g2,g3 und die sechs Quark-Yukawas von M_Z bis zur Planck-Skala;
an jeder Skala die vier Koeffizienten (A,B,C,D) an die sechs laufenden Massen fitten, D/B(mu) verfolgen.
Aufruf: python k409_test_h199.py > k409_out.txt
"""
import numpy as np
from scipy.integrate import solve_ivp

# ---- Vakuum (laeuft nicht): l_k, Nenner z, Zuordnung B ----
l = np.sort([1 + np.sqrt(2) * np.cos(2/9 + 2*np.pi*k/3) for k in range(3)])
PRS = [(0,1,2),(0,2,1),(1,2,0)]; PERM_B = [2,1,0]
lk = np.array([l[k] for (i,j,k) in PRS])[PERM_B]
z  = np.array([(l[i]+l[j])**2 for (i,j,k) in PRS])[PERM_B]

# ---- Daten bei M_Z: Yukawas y = m/v (v=174), rel. Fehler fest ----
mu = np.array([7.04e-6, 3.56e-3, 0.967]);   su = np.array([0.15e-6, 0.06e-3, 0.004])
md = np.array([1.54e-5, 3.06e-4, 1.630e-2]); sd = np.array([0.02e-5, 0.04e-4, 0.009e-2])
rel = np.concatenate([su/mu, sd/md])        # feste relative Fehler fuer den Fit

# ---- Fit (A,B,C,D) an sechs Massen; D/B ----
def fitDB(m6):
    s = rel * m6
    X = np.vstack([np.stack([lk/z, lk**2/z,  lk/z,  lk**2/z],1),
                   np.stack([lk/z, lk**2/z, -lk/z, -lk**2/z],1)])
    W = 1/s; co,*_ = np.linalg.lstsq(X*W[:,None], m6*W, rcond=None)
    A,B,Cc,D = co; chi2 = float(np.sum(((X@co - m6)/s)**2))
    return D/B, co, chi2

DB0, co0, chi0 = fitDB(np.concatenate([mu, md]))
print(f"Bei M_Z: D/B = {DB0:+.4f}, chi2 = {chi0:.2f}  (A={co0[0]:.3e} B={co0[1]:.3e} C={co0[2]:.3e} D={co0[3]:.3e})")

# ---- 1-Schleifen-SM-RGEs (GUT-Norm g1^2 = 5/3 g_Y^2) ----
# Zustand: [g1,g2,g3, yu,yc,yt, yd,ys,yb]  (Leptonen: nur y_tau fuer Y2, laeuft naeherungsweise mit)
g1=0.462; g2=0.651; g3=1.220                 # bei M_Z
ytau = 0.0102
y0 = np.array([g1,g2,g3, *mu, *md])
k = 1/(16*np.pi**2)
bg = np.array([41/10, -19/6, -7.0])
# Hyperladungs-Koeffizienten (up, down) fuer den g1-Term
cU = np.array([17/20, 9/4, 8.0]); cD = np.array([1/4, 9/4, 8.0])
def rhs(t, y):
    g = y[:3]; yu = y[3:6]; yd = y[6:9]
    Y2 = 3*np.sum(yu**2) + 3*np.sum(yd**2) + ytau**2
    gterm = g**2
    dyu = yu*( 1.5*(yu**2 - yd**2) + Y2 - (cU[0]*gterm[0] + cU[1]*gterm[1] + cU[2]*gterm[2]) )
    dyd = yd*( 1.5*(yd**2 - yu**2) + Y2 - (cD[0]*gterm[0] + cD[1]*gterm[1] + cD[2]*gterm[2]) )
    dg  = bg * g**3
    return k*np.concatenate([dg, dyu, dyd])

tmax = np.log(1e19/91.1876)
sol = solve_ivp(rhs, [0, tmax], y0, dense_output=True, rtol=1e-9, atol=1e-12, max_step=0.2)
print(f"\nIntegration M_Z -> 10^19 GeV ok: {sol.success}; y_t(M_Z)={y0[5]:.3f} -> y_t(Pl)={sol.y[5,-1]:.3f}")

# ---- D/B(mu) ueber die Skalen ----
print("\n  mu [GeV]      y_t     y_b/y_s   D/B      chi2    (Symmetriewerte: 0, 1/3, -1)")
sym = {0.0:0, 1/3:0, -1.0:0}; DBs = []
for tt in np.linspace(0, tmax, 18):
    yv = sol.sol(tt); m6 = np.concatenate([yv[3:6], yv[6:9]])
    DB, co, chi2 = fitDB(m6); DBs.append((91.1876*np.exp(tt), DB))
    mu_scale = 91.1876*np.exp(tt)
    print(f"  {mu_scale:.3e}  {yv[5]:.4f}  {yv[8]/yv[7]:7.2f}  {DB:+.4f}  {chi2:7.2f}")
DBmin = min(db for _,db in DBs); DBmax = max(db for _,db in DBs)
print(f"\n  D/B-Bereich ueber 17 Dekaden: [{DBmin:+.4f}, {DBmax:+.4f}]  (Bewegung {abs(DBmax-DBmin):.4f} = {100*abs(DBmax-DBmin)/abs(DB0):.1f}%)")
# Naehe zu Symmetriewerten
near = min([(abs(db-s), s, mu_) for mu_,db in DBs for s in (0.0,1/3,-1.0)])
print(f"  naechster Symmetriewert: D/B kommt {sym and ''}{near[1]:+.3f} bis auf {near[0]:.3f} nahe (bei mu~{near[2]:.1e} GeV)")

print("\n" + "="*72)
print("Urteil H199:")
moved = 100*abs(DBmax-DBmin)/abs(DB0)
reaches = near[0] < 0.1            # erreicht Symmetriewert innerhalb ~2sigma-Fensterbreite?
if reaches:
    print(f"    D/B erreicht einen Symmetriewert ({near[1]:+.3f}) -> Lauf koennte D=B erklaeren (siehe Skala).")
elif moved > 10:
    print(f"    D/B bewegt sich {moved:.1f}% in {17} Dekaden, erreicht aber keinen Symmetriewert -> teilweise.")
else:
    print(f"    D/B bleibt ueber 17 Dekaden nahe 1 (Bewegung {moved:.2f}%), fern von 0, 1/3, -1.")
    print("    -> NEIN: der Lauf der Kopplungen ist nicht die Quelle von D=B.")
