"""Ein Job der parallelen OP5-Rechnung: dim g_p (ungeeicht) und dim g'_p (theta-geeicht) des eingefrorenen
Omega-Symbols fuer EINE Ordnung p. Gedacht fuer die Job-Matrix in .github/workflows/op5-parallel.yml, laeuft aber auch lokal.

Aufbau wie balanced_spencer_check.py (ausgeglichene Koordinaten, J und theta aus completion-omega-witness.npz) und
k137 (Eichzeilen kron(I, wg) mit wg = k136_eichdaten.npy[1]). Rang an der groessten Singulaerwertluecke (rank_gap wie k140).

Aufruf: python ci/op5/symbol_rang.py --p 7 [--daten <state-sufficiency-Ordner>] [--eich <k136_eichdaten.npy>] [--out x.json]
"""
import argparse, hashlib, itertools, json, math, os, platform, time
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
ap = argparse.ArgumentParser()
ap.add_argument('--p', type=int, required=True)
ap.add_argument('--daten', default=str(ROOT / 'analysis/op5-field-slices/state-sufficiency-2026-10-30'))
ap.add_argument('--eich', default=str(ROOT / 'notes/research/v4_10_0_r72/llm/k136_eichdaten.npy'))
ap.add_argument('--out', default=None)
a = ap.parse_args()
p = a.p
wit = Path(a.daten) / 'completion-omega-witness.npz'
w = np.load(wit, allow_pickle=False); J = w['completed_first_symbol']; theta = w['theta_normalized']
wg = np.load(a.eich)[1]

def idx(d): return list(itertools.combinations_with_replacement(range(4), d))
def fac(al): return math.prod(math.factorial(al.count(mu)) for mu in range(4))
def rank_gap(s):
    s = s / s[0]; m = int(np.sum(s > 1e-15)); t = np.r_[s[:m], 1e-17] if m == len(s) else s[:m + 1]
    k = int(np.argmax(np.log(t[:-1] / t[1:]))); return k + 1, float(t[k]), float(t[k + 1])

def symbol(p):
    """Ausgeglichenes Symbol der Ordnung p (direkte Assemblierung aus balanced_spencer_check.matrix)."""
    ri, ci = idx(p - 1), idx(p); look = {al: n for n, al in enumerate(ci)}
    nO = len(idx(p - 3)) if p >= 3 else 0
    M = np.zeros((len(ri) * 32 + nO, len(ci) * 24))
    for rn, al in enumerate(ri):
        for mu in range(4):
            cn = look[tuple(sorted((*al, mu)))]
            M[rn*32:(rn+1)*32, cn*24:(cn+1)*24] += math.sqrt(al.count(mu) + 1) * J[:, mu*24:(mu+1)*24]
    off = len(ri) * 32
    for rn, ga in enumerate(idx(p - 3) if p >= 3 else []):
        for bn, be in enumerate(idx(3)):
            de = tuple(sorted((*be, *ga))); cn = look[de]
            M[off+rn, cn*24:(cn+1)*24] += theta[bn*24:(bn+1)*24] * math.sqrt(fac(de)) / (fac(be) * math.sqrt(fac(ga)))
    return M

def kern_dim(M):
    M = M[np.linalg.norm(M, axis=1) > 0]; M = M / np.linalg.norm(M, axis=1)[:, None]
    t = time.time()
    try:
        import scipy.linalg as sl; s = sl.svdvals(M, overwrite_a=True, check_finite=False)
    except ImportError:
        s = np.linalg.svd(M, compute_uv=False)
    r, s1, s2 = rank_gap(s)
    return {'zeilen': int(M.shape[0]), 'spalten': int(M.shape[1]), 'rang': r, 'dim': int(M.shape[1] - r),
            'luecke_oben': s1, 'luecke_unten': s2, 'verhaeltnis': s1 / s2, 'sekunden': round(time.time() - t, 1)}

t0 = time.time()
B = symbol(p)
ungeeicht = kern_dim(B.copy())
geeicht = kern_dim(np.vstack([B, np.kron(np.eye(len(idx(p))), wg[None, :])]))
bekannt_g = dict(zip(range(2, 11), [127, 208, 308, 427, 565, 726, 910, 1118, 1351]))
bekannt_gg = dict(zip(range(2, 10), [117, 188, 273, 371, 481, 606, 745, 898]))
res = {'p': p, 'ungeeicht': ungeeicht, 'geeicht': geeicht,
       'erwartet_g': bekannt_g.get(p), 'erwartet_g_geeicht': bekannt_gg.get(p),
       'kontrolle_geeicht': ungeeicht['dim'] - math.comb(p + 3, 3),
       'witness_sha256': hashlib.sha256(wit.read_bytes()).hexdigest(),
       'numpy': np.__version__, 'python': platform.python_version(), 'kerne': os.cpu_count(),
       'sekunden_gesamt': round(time.time() - t0, 1)}
print(json.dumps(res, indent=1))
if a.out: Path(a.out).write_text(json.dumps(res, indent=1))
