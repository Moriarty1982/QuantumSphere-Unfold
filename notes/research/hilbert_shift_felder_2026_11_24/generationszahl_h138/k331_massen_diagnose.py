"""k331 (Test H148): Warum liegen die Massen aus H146 daneben? Gram-Auslesung mit Mischwinkel e0/e7, Amplituden-Auslesung (r13/k255),
komplexer Ladungszustand. Vorab: Vorab_Notiz_H148_Warum_Massen_daneben.md. Gram-Teil mit den echten Kopien aus k326 (per exec)."""
import numpy as np, io, contextlib
from scipy.optimize import brentq
src = open('k326_fuenf_kopien.py').read().split('TR = (1, 1, 1, 1, 1)')[0]
with contextlib.redirect_stdout(io.StringIO()): exec(src)
I8 = np.eye(8); SED = (0, 1, 2)
mlep = np.array([0.51099895, 105.6583755, 1776.93])
K = lambda r: float(np.sum(r**2) / np.sum(np.abs(r))**2)
def gram(idx, y):
    X = np.array([B[k].T @ y for k in idx]); return X.conj() @ X.T
print("=== H148a: Gram-Auslesung, Sedenion-Tripel ===")
for name, y in (("Lepton (e0+i e7)/sqrt2", (I8[0] + 1j*I8[7])/np.sqrt(2)), ("Farbe e1", I8[1])):
    G = gram(SED, y); a = G[0, 1]
    print(f"   {name}: Ueberlappung {np.round(a, 6)}, |a|^2 = {abs(a)**2:.6f}, K = {K(np.linalg.eigvalsh(G)):.6f}, Formel (3+6|a|^2)/9 = {(3+6*abs(a)**2)/9:.6f}")
print("   benoetigt fuer K = 2/3: |a|^2 = 1/2 (Ueberlappung 1/sqrt2 = cos(pi/4))")
print("\n=== H148b: Gram-Auslesung mit y = cos t e0 + sin t e7 ===")
Kt = lambda t: K(np.linalg.eigvalsh(gram(SED, np.cos(t)*I8[0] + np.sin(t)*I8[7])))
grid = np.linspace(1e-4, np.pi/2 - 1e-4, 2001); vals = np.array([Kt(t) for t in grid])
roots = [brentq(lambda t: Kt(t) - 2/3, grid[i], grid[i+1]) for i in range(len(grid)-1) if (vals[i] - 2/3)*(vals[i+1] - 2/3) < 0]
print("   Nullstellen K = 2/3 in (0, pi/2):", [f"{r:.6f} rad = {np.degrees(r):.4f} Grad" for r in roots])
ts = np.arcsin(np.sqrt(2/3*(1 - 1/np.sqrt(2))))
print(f"   Formel sin^2 t* = 2/3 (1 - 1/sqrt2): t* = {ts:.6f} rad = {np.degrees(ts):.4f} Grad")
lam = np.sort(np.linalg.eigvalsh(gram(SED, np.cos(ts)*I8[0] + np.sin(ts)*I8[7])))
print(f"   sqrt m bei t*: {np.round(lam, 6)} (zwei gleich: {abs(lam[0]-lam[1]) < 1e-9}), m_max/m_min = {lam[2]**2/lam[0]**2:.3f}")
bs = 0.5493; consts = {"beta_sym": bs, "artanh beta_sym": np.arctanh(bs), "pi/4": np.pi/4, "pi/12": np.pi/12,
          "halber magischer Winkel": np.arccos(1/np.sqrt(3))/2, "arcsin(1/sqrt3)": np.arcsin(1/np.sqrt(3)), "magischer Winkel": np.arccos(1/np.sqrt(3)),
          "2/9": 2/9, "arctan(beta_sym)": np.arctan(bs)}
print("   Abstand zu Projektgroessen (rad):", {k: round(abs(ts - v), 4) for k, v in consts.items()})
print("   naechste:", min(consts, key=lambda k: abs(ts - consts[k])), f"{min(abs(ts - v) for v in consts.values()):.4f}")
print("\n=== H148c: Amplituden-Auslesung (r13/k255) ===")
f = [np.array([np.cos(t), np.sin(t)]) for t in (0, 2*np.pi/3, 4*np.pi/3)]
g = [np.concatenate([[1/np.sqrt(3)], np.sqrt(2/3)*fk]) for fk in f]
print("   Gram der g_k:", np.round(np.array([[gi @ gj for gj in g] for gi in g]), 12).tolist())
def amp(t, d, beta_phase=1.0):
    Psi = np.concatenate([[np.cos(t)], beta_phase*np.sin(t)*np.array([np.cos(d), np.sin(d)])])
    return np.array([gk @ Psi for gk in g])
for t in (np.pi/8, np.pi/6, np.pi/4, np.pi/3):
    ks = [K(np.abs(amp(t, d))) for d in np.linspace(0, 2*np.pi, 13)]
    print(f"   t = {np.degrees(t):.1f} Grad: K ueber delta {min(ks):.6f} .. {max(ks):.6f}, Formel 1/(3 cos^2 t) = {1/(3*np.cos(t)**2):.6f}")
c = np.sort(np.abs(amp(np.pi/4, 2/9)))**2
print(f"   t = pi/4, delta = 2/9 (eingesetzt): m-Verhaeltnisse mu/e = {c[1]/c[0]:.3f} (Messung {mlep[1]/mlep[0]:.3f}), tau/mu = {c[2]/c[1]:.4f} (Messung {mlep[2]/mlep[1]:.4f})")
print(f"      relative Abweichung: {abs(c[1]/c[0]/(mlep[1]/mlep[0]) - 1):.2e}, {abs(c[2]/c[1]/(mlep[2]/mlep[1]) - 1):.2e}; K = {K(np.sqrt(c)):.6f}")
d_fit = brentq(lambda d: (lambda c: c[1]/c[0])(np.sort(np.abs(amp(np.pi/4, d)))**2) - mlep[1]/mlep[0], 0.15, 0.3)
print(f"   delta aus m_mu/m_e angepasst: {d_fit:.6f} (2/9 = {2/9:.6f})")
print("\n=== H148d: komplexer Ladungszustand (e0 + i e7)/sqrt2 ===")
Ks = [K(np.abs(amp(np.pi/4, d, 1j))) for d in np.radians(np.arange(0, 360, 1))]
print(f"   K ueber delta (1-Grad-Raster): min {min(Ks):.6f}, max {max(Ks):.6f}; min |K - 2/3| = {min(abs(k - 2/3) for k in Ks):.6f}")
print("\n=== Nachtrag zur Auswertung von H148c: K mit vorzeichenbehafteten Amplituden (sqrt m = c_k, Brannen-Konvention) ===")
Ks_signed = lambda c: float(np.sum(c**2) / np.sum(c)**2)
for t in (np.pi/8, np.pi/4, np.pi/3):
    ks = [Ks_signed(amp(t, d)) for d in np.linspace(0, 2*np.pi, 13)]
    print(f"   t = {np.degrees(t):.1f} Grad: K (signiert) ueber delta {min(ks):.6f} .. {max(ks):.6f}")
pos = [d for d in np.radians(np.arange(0, 360, 1)) if np.all(amp(np.pi/4, d) >= 0)]
print(f"   bei t = pi/4 alle Amplituden >= 0 fuer {len(pos)} von 360 Rasterwerten von delta; bei delta = 2/9 rad ({np.degrees(2/9):.2f} Grad): {np.all(amp(np.pi/4, 2/9) >= 0)}")
