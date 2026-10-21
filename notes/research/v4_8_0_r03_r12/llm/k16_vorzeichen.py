"""k16: Was bedeutet das negative Vorzeichen einer Triolen-Komponente? (zu K14)
v_k = t(1 + sqrt2 r cos(delta + 2 pi k/3)); r = 1 fuer Leptonen."""
import numpy as np
P = 2*np.pi/3
def v(d, r=1.0): return 1 + np.sqrt(2)*r*np.cos(d + P*np.arange(3))

# 1) Produkt-Identitaet e3 = v0 v1 v2 = cos(3d)/sqrt2 - 1/2 (r = 1, t = 1)
d = np.linspace(0, 2*np.pi, 100001)
e3 = np.array([np.prod(v(x)) for x in d])
print("max |e3 - (cos3d/sqrt2 - 1/2)| =", np.abs(e3 - (np.cos(3*d)/np.sqrt(2) - 0.5)).max())
# allgemein r: e3 = 1 - 3r^2/2 + r^3 cos(3d)/sqrt2
for r in (1.115, 1.29):
    e = np.array([np.prod(v(x, r)) for x in d[:2000]])
    print(f"r={r}: Identitaet Abw. =", np.abs(e - (1 - 1.5*r*r + r**3*np.cos(3*d[:2000])/np.sqrt(2))).max())

# 2) Hoechstens eine Komponente negativ; Anteil des Kreises mit einer negativen Komponente
neg = np.array([(v(x) < 0).sum() for x in d])
print("max. Anzahl negativer Komponenten:", neg.max(), " Anteil mit einer negativen:", (neg == 1).mean())

# 3) Grenzphase (eine Masse = 0) und Lage der Sektoren
def grenze(r):  # kleinste delta>0 mit min v = 0 im Fundamentalbereich [0, pi/3]
    return np.arccos(-1/(np.sqrt(2)*r)) - P
for name, dd, r in (("geladene Leptonen", 0.2222, 1.0), ("Down-Quarks", 0.1001, 1.115),
                    ("Up-Quarks", 0.0518, 1.290), ("Neutrinos (H2, NO)", 0.479256, 1.0)):
    vv = v(dd, r)
    print(f"{name:20s} delta={dd:.4f}  Grenze={grenze(r):.4f}  Vorzeichen={np.sign(vv).astype(int)}"
          f"  3delta={3*dd:.4f}  e3={np.prod(vv):+.4f}")

# 4) SO(3)-Invarianten des Paares (v, n=(1,1,1)/sqrt3) sind |v| und v.n -- fuer alle delta gleich
n = np.ones(3)/np.sqrt(3)
for dd in (0.2222, 0.479256):
    print(f"delta={dd}: |v|={np.linalg.norm(v(dd)):.6f}  v.n={v(dd)@n:.6f}  Winkel={np.degrees(np.arccos(v(dd)@n/np.linalg.norm(v(dd)))):.4f} Grad")
