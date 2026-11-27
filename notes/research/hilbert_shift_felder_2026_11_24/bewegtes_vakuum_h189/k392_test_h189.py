"""k392 (Test H189): bewegtes Vakuum, Ableitungsterme K1 bis K4 und die Quarkmassen.
Vorab: Vorab_Notiz_H189_Bewegtes_Vakuum_und_Quarkmassen.md (Commit 017a2be).
Aufruf: python k392_test_h189.py > k392_out.txt"""
import itertools
import numpy as np
from scipy.linalg import null_space
rng = np.random.default_rng(392)
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])
e = np.eye(8); C = np.array([[mul(e[i], e[j]) for j in range(8)] for i in range(8)])
cj = np.diag([1.0] + [-1.0] * 7)
PAIRS = [(0, 1), (1, 2), (2, 0)]
def toW(v):
    v = np.asarray(v, dtype=complex); W = np.zeros((3, 3, 8), dtype=complex)
    for i in range(3): W[i, i, 0] = v[i]
    for s, (i, j) in enumerate(PAIRS):
        x = v[3 + 8 * s: 11 + 8 * s]; W[i, j] = x; W[j, i] = cj @ x
    return W
mm = lambda X, Y: np.einsum('ija,jkb,abc->ikc', X, Y, C)
jo = lambda X, Y: 0.5 * (mm(X, Y) + mm(Y, X))
tr = lambda X: X[0, 0, 0] + X[1, 1, 0] + X[2, 2, 0]
def projU(W):
    Z = np.zeros_like(W); Z[:, :, 0] = W[:, :, 0]; Z[:, :, 7] = W[:, :, 7]; return Z
N = lambda X: np.sum(np.abs(X)**2)                                      # hermitesche Norm
ip = lambda X, Y: np.sum((np.conj(X) * Y).real)
def assoc(X, Y, Z): return mm(mm(X, Y), Z) - mm(X, mm(Y, Z))
def W0(a, r, delta):
    v = np.zeros(27); v[:3] = a
    for s in range(3): v[3 + 8 * s] = r * np.cos(delta); v[3 + 8 * s + 7] = r * np.sin(delta)
    return v
colidx = [3 + 8 * s + c for s in range(3) for c in range(1, 7)]
LU8 = np.einsum('i,ijk->kj', e[7], C); LU = LU8[1:7, 1:7]
I2 = np.eye(2); J2 = np.array([[0, -1.0], [1, 0]])
Ii = np.kron(J2, np.eye(18)); LUc = np.kron(I2, np.kron(np.eye(3), LU)); Qc = 0.5 * np.eye(36) + Ii @ LUc / 6
wq, Vq = np.linalg.eigh((Qc + Qc.T) / 2); E13, E23 = Vq[:, wq < 0.5], Vq[:, wq > 0.5]
def colW(d):
    v = np.zeros(27, dtype=complex); v[colidx] = d[:18] + 1j * d[18:]; return toW(v)
ref = lambda W: tr(jo(jo(W, np.conj(W)), projU(W))).real
def hess(f, w0):
    def F(d):
        v = np.asarray(w0, dtype=complex).copy(); v[colidx] += d[:18] + 1j * d[18:]; return f(toW(v))
    def H1(h):
        Hh = np.zeros((36, 36)); E = np.eye(36) * h; f0 = F(np.zeros(36))
        for i in range(36):
            Hh[i, i] = (F(2 * E[i]) - 2 * f0 + F(-2 * E[i])) / (4 * h * h)
            for j in range(i + 1, 36):
                Hh[i, j] = Hh[j, i] = (F(E[i] + E[j]) - F(E[i] - E[j]) - F(E[j] - E[i]) + F(-E[i] - E[j])) / (4 * h * h)
        return Hh
    return (4 * H1(0.1) - H1(0.2)) / 3
def modes(Href):
    out = []
    for E in (E13, E23):
        w, V = np.linalg.eigh(E.T @ Href @ E); out.append([E @ V[:, 6 * g: 6 * g + 6] for g in range(3)])
    return out
def shifts(H, md):
    Hc = (H + Ii.T @ H @ Ii) / 2; mix = np.abs(H - Hc).max(); vals = np.zeros((2, 3)); res = 0
    for q in range(2):
        for g in range(3):
            V = md[q][g]; vals[q, g] = np.trace(V.T @ Hc @ V) / 6; res = max(res, np.abs(Hc @ V - V * vals[q, g]).max())
    return vals, res, mix
def quadform(g):
    """Matrix einer exakt quadratischen Form auf den 36 Farbrichtungen (Polarisation)."""
    E = np.eye(36); d = np.array([g(colW(E[a])) for a in range(36)]); M = np.diag(d)
    for a in range(36):
        for b in range(a + 1, 36): M[a, b] = M[b, a] = (g(colW(E[a] + E[b])) - d[a] - d[b]) / 2
    return M
vac = [(1.0, 1 / np.sqrt(2), 2.0 / 9.0), (1.3, 0.55, 0.31), (0.8, 0.7, 0.12), (1.1, 0.4, 0.45)]
def ls(a, r, d): return np.sort([a + 2 * r * np.cos(d + 2 * np.pi * k / 3) for k in range(3)])
def bg(vc, var):
    """Hintergrund B0 = d_t W fuer omega = 1. Variante 1: i W0. Variante 2: U auf den Nebendiagonal-Eintraegen."""
    w = W0(*vc)
    if var == 1: return toW(1j * w)
    v = np.zeros(27)
    for s in range(3): v[3 + 8 * s: 11 + 8 * s] = LU8 @ w[3 + 8 * s: 11 + 8 * s]
    return toW(v)
K1 = lambda X, Y: N(X) * N(Y) - ip(X, Y)**2
K2 = lambda X, Y: N(mm(X, Y) - mm(Y, X))
K4 = lambda X, Y: N(mm(X, Y)) + N(mm(Y, X)) - 2 * N(X) * N(Y)
K3 = lambda X, Y, Z: N(assoc(X, Y, Z) - assoc(X, Z, Y))

print("== H189a: Ruhefrequenzen (k = 0) bei rein zeitlich bewegtem Vakuum ==")
B0 = bg(vac[0], 1); B0b = bg(vac[0], 2); A = colW(rng.normal(size=36)); Bx = colW(rng.normal(size=36)); By = colW(rng.normal(size=36)); Zr = np.zeros_like(A)
za = max(abs(K(B + 0.3 * A, Zr)) for K in (K1, K2, K4) for B in (B0, B0b))
print(f"   K1, K2, K4 mit X_t = B0 + eps d_t dW, X_x = 0 (beide Varianten): groesster Betrag {za:.1e}")
k3 = [K3(B, ep * Bx, ep * By) for ep in (1.0, 0.5) for B in (B0, B0b)]
print(f"   K3(B0, eps a, eps b): Verhaeltnis der Werte bei eps = 1 und eps = 1/2: {k3[0] / k3[2]:.6f}, {k3[1] / k3[3]:.6f} (16 = Ordnung eps^4, kein Beitrag in eps^2)")
ok_a = za == 0 and all(abs(r - 16) < 1e-9 for r in (k3[0] / k3[2], k3[1] / k3[3]))
print("   Urteil H189a:", "BESTAETIGT (nicht blind): die Ableitungsterme aendern die Ruhefrequenzen nicht" if ok_a else "WIDERLEGT")

print("\n== Moden der Generationen je Vakuum (Referenzform wie k390) ==", flush=True)
mds = [modes(hess(ref, W0(*vc))) for vc in vac]; l0 = ls(*vac[0]); print(f"   Eigenwerte des Vakuums l = {np.round(l0, 6)}")

print("\n== H189b: gewoehnlicher kinetischer Term um W = exp(i omega t) (W0 + dW) ==")
print("   Bewegungsgleichung: d'' + 2 omega I d' - omega^2 d + H d = 0 (I = Multiplikation mit i; H = zweite Variation eines phaseninvarianten Potentials)")
md0 = mds[0]; om = 0.37; hq = np.array([[0.9, 2.3, 4.1], [1.4, 2.9, 5.2]]); H = sum(hq[q, g] * md0[q][g] @ md0[q][g].T for q in range(2) for g in range(3))
print(f"   Beispiel: omega = {om}, H diagonal in den Moden mit h = {hq.tolist()} (Zeilen: Ladung 1/3, 2/3); [H, I] = {np.abs(H @ Ii - Ii @ H).max():.1e}")
Msys = np.block([[np.zeros((36, 36)), np.eye(36)], [om**2 * np.eye(36) - H, -2 * om * Ii]]); ev = np.sort(np.abs(np.linalg.eigvals(Msys).imag))
pred = np.sort(np.concatenate([np.repeat(np.abs(np.sqrt(hq.ravel()) + s * om), 6) for s in (1, -1)]))
dv = np.abs(ev - pred).max(); print(f"   Eigenfrequenzen gegen sqrt(h) +- omega: groesste Abweichung {dv:.1e}; Aufspaltung je Mode 2 omega = {2 * om}, unabhaengig von Generation und Ladung")
print("   (In der Vorab-Notiz steht sqrt(h + omega^2) +- omega; dort ist h die Kruemmung im mitdrehenden Bild, hier die des Potentials: h_Vorab = h - omega^2.)")
print("   Urteil H189b:", "BESTAETIGT (nicht blind): die Drehung allein trennt Up und Down nicht und gibt keine Hierarchie" if dv < 1e-8 else "WIDERLEGT")

print("\n== H189c (ohne Daten): Gradientenformen aus K1, K2, K4 in zweiter Ordnung, X_t = B0, X_x = d_x dW ==", flush=True)
prs = [(0, 1, 2), (0, 2, 1), (1, 2, 0)]; fnames = ["1", "(l_i + l_j)", "l_k", "(l_i^2 + l_j^2)", "l_i l_j", "l_k (l_i + l_j)", "l_k^2"]
def feats(l): return np.array([[1.0, l[i] + l[j], l[k], l[i]**2 + l[j]**2, l[i] * l[j], l[k] * (l[i] + l[j]), l[k]**2] for (i, j, k) in prs])
A7 = np.vstack([feats(ls(*vc)) for vc in vac])
def show(co): return " ".join(f"{c:+.4f} {n}" for c, n in zip(co, fnames) if abs(c) > 1e-8) or "0"
G = {}; ok_c = True
for var in (1, 2):
    for kn, K in (("g1 (K1)", K1), ("g2 (K2)", K2), ("g4 (K4)", K4)):
        ev_, od_, rs_, mx_, v0 = [], [], 0, 0, None
        for n_, (vc, md) in enumerate(zip(vac, mds)):
            Bv = bg(vc, var); vals, rs, mx = shifts(quadform(lambda a: K(Bv, a)), md); ev_.append((vals[1] + vals[0]) / 2); od_.append((vals[1] - vals[0]) / 2); rs_ = max(rs_, rs); mx_ = max(mx_, mx)
            if n_ == 0: v0 = vals
        G[(var, kn[:2])] = v0; line = f"   Variante {var}, {kn}: Eigenrest {rs_:.1e}, ladungsmischend {mx_:.1e}"; good = rs_ < 1e-8 and mx_ < 1e-8
        for lab, y in (("gerade", np.concatenate(ev_)), ("ungerade (Up - Down)/2", np.concatenate(od_))):
            if np.abs(y).max() < 1e-10: continue
            co, *_ = np.linalg.lstsq(A7, y, rcond=None); co[np.abs(co) < 1e-9] = 0; rr = np.abs(A7 @ co - y).max(); good &= rr < 1e-8
            line += f"\n        {lab}: {show(co)}   (Rest {rr:.1e})"
        print(line + f"\n        Werte am Vakuum (Down; Up): {np.round(v0[0], 6)}; {np.round(v0[1], 6)}   -> {'Funktion des Paars' if good else 'KEINE Funktion des Paars in diesem Raum'}", flush=True); ok_c &= good
print("   Urteil H189c:", "BESTAETIGT (alle Formen diagonal und Funktionen des Paars)" if ok_c else "WIDERLEGT (mindestens eine Form ist nicht diagonal oder keine Funktion des Paars)")

print("\n== H189d: traege Masse m_g = A sqrt(f_g) / (1 + kappa2 g2 + kappa4 g4), kappa fuer beide Sektoren gleich ==", flush=True)
Rdef = [("l_k", lambda i, j, k: k), ("l_k^2", lambda i, j, k: k * k), ("l_i l_j", lambda i, j, k: i * j), ("l_i l_j - l_k^2/2", lambda i, j, k: i * j - k * k / 2),
        ("1", lambda i, j, k: 1.0), ("l_i + l_j", lambda i, j, k: i + j), ("l_i^2 + l_j^2", lambda i, j, k: i * i + j * j),
        ("(l_i^2 + l_j^2)/2 + l_i l_j", lambda i, j, k: (i * i + j * j) / 2 + i * j), ("l_k (l_i + l_j)", lambda i, j, k: k * (i + j))]
FR = np.array([[f(l0[i], l0[j], l0[k]) for (i, j, k) in prs] for _, f in Rdef]); pos = [n for n in range(9) if FR[n].min() > 0]
print(f"   Funktionen aus R mit positiven Werten (fuer die Wurzel noetig): {['f%d' % (n + 1) for n in pos]} von 9")
md_ = np.array([1.54e-5, 3.06e-4, 1.630e-2]); sd_ = np.array([0.02e-5, 0.04e-4, 0.009e-2]); mu_ = np.array([7.04e-6, 3.56e-3, 0.967]); su_ = np.array([0.15e-6, 0.06e-3, 0.004])
zu = {"A": [0, 1, 2], "B": [2, 1, 0]}; BOX = 1e6
rr_ = np.arange(18); P1, P2 = np.array([(a, b) for a in rr_ for b in rr_ if a < b]).T
def sector(m, s, Fm, g2, g4, nsig):
    """Nenner auf die dritte Generation normiert: D_j = 1 + a (g2_j - g2_3) + b (g4_j - g4_3), D_3 = 1 (gleichwertig zu 1 + kappa2 g2 + kappa4 g4
    bis auf den Faktor A). Lineare Ungleichungen in (a, b) je Funktion: zwei Verhaeltnisse (oben, unten) und zwei positive Nenner."""
    r = m[:2] / m[2]; sr = r * np.sqrt((s[:2] / m[:2])**2 + (s[2] / m[2])**2); hi = r + nsig * sr; lo = np.maximum(r - nsig * sr, 0); out = []; h2 = g2 - g2[2]; h4 = g4 - g4[2]
    for j in range(2):
        out.append(np.stack([-hi[j] * Fm[:, 2] * h2[j], -hi[j] * Fm[:, 2] * h4[j], hi[j] * Fm[:, 2] - Fm[:, j]], axis=1))
        out.append(np.stack([lo[j] * Fm[:, 2] * h2[j], lo[j] * Fm[:, 2] * h4[j], Fm[:, j] - lo[j] * Fm[:, 2]], axis=1))
        out.append(np.tile([-h2[j], -h4[j], 1 - 1e-9], (len(Fm), 1)))
    return np.stack(out, axis=1)                                                   # (nF, 6, 3)
box = np.array([[1, 0, BOX], [-1, 0, BOX], [0, 1, BOX], [0, -1, BOX]], float)
case = {"nur kappa2": np.array([[0, 1, 0], [0, -1, 0.0]]), "nur kappa4": np.array([[1, 0, 0], [-1, 0, 0.0]]), "kappa2 und kappa4": box[:2]}   # in (a, b): b = 0 <=> kappa4 = 0, a = 0 <=> kappa2 = 0
def feasible(Su, Sd, extra):
    """je Paar (f_u, f_d): gibt es (kappa2, kappa4), das alle Ungleichungen erfuellt? Ecken des zulaessigen Gebiets aufzaehlen."""
    nu, nd = len(Su), len(Sd); Cs = np.concatenate([np.repeat(Su, nd, axis=0), np.tile(Sd, (nu, 1, 1)), np.tile(box, (nu * nd, 1, 1)), np.tile(extra, (nu * nd, 1, 1))], axis=1)
    sc = np.linalg.norm(Cs[:, :, :2], axis=2, keepdims=True); sc[sc == 0] = 1; Cs = Cs / sc
    a1, a2 = Cs[:, P1], Cs[:, P2]; det = a1[..., 0] * a2[..., 1] - a1[..., 1] * a2[..., 0]; okd = np.abs(det) > 1e-12; det = np.where(okd, det, 1)
    vx = (a1[..., 2] * a2[..., 1] - a1[..., 1] * a2[..., 2]) / det; vy = (a1[..., 0] * a2[..., 2] - a1[..., 2] * a2[..., 0]) / det
    lhs = Cs[:, None, :, 0] * vx[..., None] + Cs[:, None, :, 1] * vy[..., None]; tol = 1e-9 * (1 + np.abs(vx) + np.abs(vy))[..., None]
    good = okd & np.all(lhs <= Cs[:, None, :, 2] + tol, axis=2); idx = np.argmax(good, axis=1); has = good.any(axis=1)
    return has.reshape(nu, nd), vx[np.arange(len(vx)), idx].reshape(nu, nd), vy[np.arange(len(vy)), idx].reshape(nu, nd)
def combos():
    for var in (1, 2):
        for ln, tf in (("m = A sqrt(f)/c^2", np.sqrt), ("m = A f/c^2 (Kontrolle)", lambda x: x)):
            for zn, perm in zu.items():
                yield var, ln, zn, tf(FR[pos][:, perm]), Gv[var - 1][1][perm], Gv[var - 1][2][perm]
Gv = [[G[(var, k)][0] for k in ("g1", "g2", "g4")] for var in (1, 2)]            # Formen sind ladungsgerade: Werte fuer beide Sektoren gleich
def search(mu, su, md, sd, verbose=False):
    hits = {}
    for var, ln, zn, Fm, g2, g4 in combos():
        for cn, extra in case.items():
            has, kx, ky = feasible(sector(mu, su, Fm, g2, g4, 3.0), sector(md, sd, Fm, g2, g4, 3.0), extra); key = (ln, cn); hits[key] = hits.get(key, False) or bool(has.any())
            if verbose:
                lo_, hi_ = 0.0, 3000.0
                for _ in range(40):
                    mid = (lo_ + hi_) / 2; h2, *_ = feasible(sector(mu, su, Fm, g2, g4, mid), sector(md, sd, Fm, g2, g4, mid), extra)
                    if h2.any(): hi_ = mid
                    else: lo_ = mid
                h2, kx2, ky2 = feasible(sector(mu, su, Fm, g2, g4, hi_), sector(md, sd, Fm, g2, g4, hi_), extra); iu, id_ = np.unravel_index(np.argmax(h2), h2.shape)
                a_, b_ = kx2[iu, id_], ky2[iu, id_]; den = 1 + a_ * (g2 - g2[2]) + b_ * (g4 - g4[2]); nn_ = 1 - a_ * g2[2] - b_ * g4[2]; k2_, k4_ = (a_ / nn_, b_ / nn_) if abs(nn_) > 1e-12 else (np.inf, np.inf)
                if hi_ > 2999: print(f"   Variante {var}, {ln}, Zuordnung {zn}, {cn}: nicht erreichbar (kein Paar unter 3000 sigma)", flush=True); continue
                dev = []
                for m_, s_, F_ in ((mu, su, Fm[iu]), (md, sd, Fm[id_])):
                    r = m_[:2] / m_[2]; sr = r * np.sqrt((s_[:2] / m_[:2])**2 + (s_[2] / m_[2])**2); mod = F_ / den; dev += list((mod[:2] / mod[2] - r) / sr)
                print(f"   Variante {var}, {ln}, Zuordnung {zn}, {cn}: bester Abstand {hi_:.2f} sigma mit Up f{pos[iu] + 1}, Down f{pos[id_] + 1}, kappa2 = {k2_:+.5g}, kappa4 = {k4_:+.5g}, Nenner (dritte Generation = 1) {np.array2string(den, precision=5)}; nachgerechnete Abstaende {np.round(dev, 2)}; Paare (f_u, f_d) unter 3 sigma: {int(has.sum())} von {has.size}", flush=True)
    return hits
hits = search(mu_, su_, md_, sd_, verbose=True)
nc = sum(1 for _ in combos()) * len(case); print(f"   verglichen: {nc} Faelle (2 Varianten, 2 Lesarten, 2 Zuordnungen, 3 Wahlen der kappa), je {len(pos)**2} Paare von Potentialfunktionen")
import sys
NF = int(sys.argv[1]) if len(sys.argv) > 1 else 2000; cnt = {k: 0 for k in hits}; anyp = anyk = 0
for it in range(NF):
    fake = []
    for s, m in ((su_, mu_), (sd_, md_)):
        m2 = 10 ** rng.uniform(-3.5, -0.5); m1 = m2 * 10 ** rng.uniform(-3.5, -0.5); mf = np.array([m1, m2, 1.0]); fake += [mf, mf * s / m]
    h = search(fake[0], fake[1], fake[2], fake[3])
    for k in h: cnt[k] += h[k]
    anyp += any(v for k, v in h.items() if "Kontrolle" not in k[0]); anyk += any(v for k, v in h.items() if "Kontrolle" in k[0])
    if it % 500 == 499: print(f"   ... {it + 1} erfundene Datensaetze gerechnet", flush=True)
print(f"   Zufallskontrolle ({NF} erfundene Datensaetze), Trefferquote je Lesart und Wahl:")
for k in hits: print(f"      {k[0]}, {k[1]}: echte Daten {'Treffer' if hits[k] else 'kein Treffer'}; erfunden {cnt[k] / NF:.2%}")
for lab, sel, q in (("H189d (Lesart m = A sqrt(f)/c^2)", lambda k: "Kontrolle" not in k[0], anyp / NF), ("Kontroll-Lesart m = A f/c^2", lambda k: "Kontrolle" in k[0], anyk / NF)):
    h = any(v for k, v in hits.items() if sel(k))
    if not h: print(f"   Urteil {lab}: WIDERLEGT (kein Fall trifft alle vier Verhaeltnisse innerhalb von 3 sigma); Zufallsquote ueber alle Faelle {q:.2%}")
    elif q < 0.05: print(f"   Urteil {lab}: BESTAETIGT als Kandidat (Treffer, Zufallsquote {q:.2%}); eigener Vorab-Test noetig")
    else: print(f"   Urteil {lab}: OHNE URTEIL (Treffer, aber Zufallsquote {q:.2%})")
