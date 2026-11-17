"""k235 Nachtrag (nachtraeglich, nach dem Sehen von k235_stdout): wie stark haengen die beiden Ziele um 0,30 zusammen?"""
import math, runpy, io, contextlib
import numpy as np
with contextlib.redirect_stdout(io.StringIO()):
    g = runpy.run_path("k235_chance_estimate.py")
hits, T = g["hits"], [t[0] for t in g["TARGETS"]]
rng = np.random.default_rng(2351)
s = rng.uniform(1.006, 3.51, 200000)
H = hits(s); i12, iom = T.index("sin2 t12"), T.index("Omega_m DESI")
print(f"P(sin2 t12) {H[:, i12].mean():.3f}, P(Omega_m) {H[:, iom].mean():.3f}, P(beide) {(H[:, i12] & H[:, iom]).mean():.3f}, "
      f"P(Omega_m | sin2 t12) {(H[:, i12] & H[:, iom]).sum() / H[:, i12].sum():.3f}")
red = np.delete(H, iom, axis=1).sum(axis=1)
print(f"ohne Omega_m im Katalog (15 Ziele): P(n>=2) {(red >= 2).mean():.4f}, 36*P {36 * (red >= 2).mean():.3f}")
