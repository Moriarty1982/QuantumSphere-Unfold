"""Erzeugt die ersten N Zeta-Nullstellen-Ordinaten parallel und speichert sie in zeros.npy."""
import sys, os, numpy as np, mpmath as mp
from multiprocessing import Pool
def z(k):
    mp.mp.dps = 15
    return float(mp.zetazero(k).imag)
if __name__ == "__main__":
    N = int(sys.argv[1])
    with Pool() as p:
        g = np.array(p.map(z, range(1, N + 1), chunksize=20))
    np.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "zeros.npy"), g)
    print(N, g[:3], g[-1])
