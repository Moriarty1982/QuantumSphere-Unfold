"""Zeitabhaengige Verbindung: Flussumverteilung auf der Generationskugel (Methoden_Notiz_Verbindung.md, Nachtrag N2, Commit e4f7b30).

Start: Berry-Fluss gleichmaessig 1/2 je sr; T = Oktant (x, y, z >= 0); Ziel: Fluss(T) um Delta = pi/4 - 0.666674 senken.
V0: statischer W2-Transport (gleichwertig zu Benamou-Brenier), freier Endzustand -> gierige Randloesung, Gitter 3, 4, 5.
V1: Stromnorm ohne Gewichtung -> Strom nur auf Randkanten, Kosten Delta^2 / Zahl der Randkanten.
K-A, K-B: exakter W2 zwischen Start und festem Endzustand (LP, HiGHS); Gitter 3 dicht, Gitter 3 und 4 mit Abstandsschranke 0.6 rad.
"""
import json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

DELTA = np.pi / 4 - 0.666674
ZC = np.ones(3) / np.sqrt(3)


def icosphere(k):
    t = (1 + 5 ** 0.5) / 2
    V = [(-1, t, 0), (1, t, 0), (-1, -t, 0), (1, -t, 0), (0, -1, t), (0, 1, t), (0, -1, -t), (0, 1, -t), (t, 0, -1), (t, 0, 1), (-t, 0, -1), (-t, 0, 1)]
    F = [(0, 11, 5), (0, 5, 1), (0, 1, 7), (0, 7, 10), (0, 10, 11), (1, 5, 9), (5, 11, 4), (11, 10, 2), (10, 7, 6), (7, 1, 8),
         (3, 9, 4), (3, 4, 2), (3, 2, 6), (3, 6, 8), (3, 8, 9), (4, 9, 5), (2, 4, 11), (6, 2, 10), (8, 6, 7), (9, 8, 1)]
    V = [np.array(v, float) / np.linalg.norm(v) for v in V]
    for _ in range(k):
        cache, F2 = {}, []
        def mid(a, b):
            key = (min(a, b), max(a, b))
            if key not in cache:
                m = V[a] + V[b]; V.append(m / np.linalg.norm(m)); cache[key] = len(V) - 1
            return cache[key]
        for a, b, c in F:
            ab, bc, ca = mid(a, b), mid(b, c), mid(c, a)
            F2 += [(a, ab, ca), (b, bc, ab), (c, ca, bc), (ab, bc, ca)]
        F = F2
    V = np.array(V); F = np.array(F)
    # Knotenflaechen: ein Drittel der angrenzenden Dreiecke (sphaerischer Exzess), Summe 4 pi
    def sph_area(a, b, c):
        num = abs(np.dot(a, np.cross(b, c))); den = 1 + a @ b + b @ c + c @ a
        return 2 * np.arctan2(num, den)
    area = np.zeros(len(V))
    for a, b, c in F:
        s = sph_area(V[a], V[b], V[c]); area[[a, b, c]] += s / 3
    edges = set()
    for a, b, c in F:
        for u, v in ((a, b), (b, c), (c, a)):
            edges.add((min(u, v), max(u, v)))
    return V, area, np.array(sorted(edges))


def octant_weight(V, tol=1e-9):
    w = np.ones(len(V))
    for k in range(3):
        w[V[:, k] < -tol] = 0
        w[np.abs(V[:, k]) <= tol] *= 0.5
    return w


def rim_solution(V, area):
    w = octant_weight(V); m = 0.5 * area * w
    d = np.arcsin(np.clip(np.min(V, axis=1), 0, 1))           # Abstand zum Rand des Oktanten (innen)
    idx = np.argsort(d); idx = idx[m[idx] > 0]
    moved, cost, width, emptied = 0.0, 0.0, 0.0, []
    for i in idx:
        take = min(m[i], DELTA - moved)
        if take <= 0: break
        moved += take; cost += take * d[i] ** 2; width = d[i]; emptied.append(i)
    full = [i for i in emptied if abs(m[i] - 0) > 0]
    ang_centroid = np.degrees(np.arccos(np.clip(V[emptied] @ ZC, -1, 1)))
    return {"Masse T (Gitter)": float(m.sum()), "Breite des geleerten Saums (rad)": float(width), "Kosten W2": float(cost),
            "geleerte Knoten": len(emptied), "Winkel zur Zyklusachse der geleerten Knoten (min, max, Grad)": [float(ang_centroid.min()), float(ang_centroid.max())],
            "Ablageabstand (gleich Randabstand)": "gleich d_i, direkt jenseits des Randes"}


def v1_solution(V, edges):
    inn = np.min(V, axis=1) >= -1e-9
    cross = [(a, b) for a, b in edges if inn[a] != inn[b]]
    L = np.mean([np.arccos(np.clip(V[a] @ V[b], -1, 1)) for a, b in cross])
    return {"Randkanten": len(cross), "Kosten (Einheitsgewichte)": float(DELTA ** 2 / len(cross)), "mittlere Kantenlaenge": float(L),
            "Kosten mit Kantenlaenge^2": float(DELTA ** 2 / len(cross) * L ** 2)}


def core_targets(V, area):
    m0 = 0.5 * area
    ang = np.arccos(np.clip(V @ ZC, -1, 1))
    m1 = m0.copy(); removed = 0.0
    for i in np.argsort(ang):
        take = min(m1[i], DELTA - removed); m1[i] -= take; removed += take
        if removed >= DELTA - 1e-15: break
    capmask = m1 < m0 - 1e-15
    capA = float(area[capmask].sum())
    mA = m1.copy(); anti = np.argsort(np.arccos(np.clip(-V @ ZC, -1, 1)))
    sel, acc = [], 0.0
    for i in anti:
        sel.append(i); acc += area[i]
        if acc >= capA: break
    sel = np.array(sel); mA[sel] += DELTA * area[sel] / area[sel].sum()
    mB = m1.copy(); rest = ~capmask; mB[rest] += DELTA * area[rest] / area[rest].sum()
    return m0, mA, mB


def w2_lp(V, m0, m1, cutoff=None):
    n = len(V)
    D = np.arccos(np.clip(V @ V.T, -1, 1))
    if cutoff is None:
        I, J = np.meshgrid(np.arange(n), np.arange(n), indexing="ij"); I, J = I.ravel(), J.ravel()
    else:
        I, J = np.nonzero(D <= cutoff)
    c = D[I, J] ** 2
    k = len(c)
    rows = np.concatenate([I, n + J]); cols = np.concatenate([np.arange(k), np.arange(k)])
    A = coo_matrix((np.ones(2 * k), (rows, cols)), shape=(2 * n, k)).tocsr()
    b = np.concatenate([m0, m1])
    r = linprog(c, A_eq=A, b_eq=b, bounds=(0, None), method="highs")
    return float(r.fun) if r.status == 0 else None, r.status, k


if __name__ == "__main__":
    out = {"Delta": DELTA}
    for k in (3, 4, 5):
        V, area, edges = icosphere(k)
        out[f"Gitter {k}"] = {"Knoten": len(V), "V0 Randloesung": rim_solution(V, area), "V1 Stromnorm": v1_solution(V, edges)}
        print(k, json.dumps(out[f"Gitter {k}"], ensure_ascii=False))
    for k, cut in ((3, None), (3, 0.6), (4, 0.6)):
        V, area, edges = icosphere(k)
        m0, mA, mB = core_targets(V, area)
        resA = w2_lp(V, m0, mA, cut); resB = w2_lp(V, m0, mB, cut)
        rim = rim_solution(V, area)["Kosten W2"]
        key = f"Kern-Konfigurationen Gitter {k}, Schranke {cut}"
        out[key] = {"K-A (Gegenpol) W2": resA[0], "K-B (gleichmaessig) W2": resB[0], "Variablen": resA[2],
                    "Verhaeltnis K-A / Rand": resA[0] / rim if resA[0] else None, "Verhaeltnis K-B / Rand": resB[0] / rim if resB[0] else None}
        print(key, json.dumps(out[key], ensure_ascii=False))
    with open("run/connection_flow.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
