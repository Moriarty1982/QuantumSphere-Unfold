"""k326 (Test H143): fuenf Oktonion-Kopien auf HS(5) als getrennte Traeger; alle 126 Fuenferauswahlen der 9 Kopien,
transportierte Orientierung (gewertet) und alle 2^4 relativen Orientierungen (offengelegt). Vorab: Vorab_Notiz_H143_Fuenf_Kopien_HS5.md.
Uebernimmt die Definitionen aus k325_vier_kopien.py (per exec, ohne dessen Ausgabe-Teil)."""
import itertools, numpy as np
src = open('k325_vier_kopien.py').read().split('print("=== H142a ===")')[0]
exec(src)
_full = open('k325_vier_kopien.py').read()
exec(_full[_full.index('# Leck-Gram'):_full.index('# Casimir auf V')])   # gram, common_charge
rng = np.random.default_rng(326)
lab = lambda k: f"f{120*(k//3)}(x)f{120*(k%3)}"

def ops(idx, sg):
    m = len(idx)
    Qs = [Qof(s*VS[k]) for k, s in zip(idx, sg)]
    Phi = np.hstack([B[k].T for k in idx])
    _, s_, vt_ = np.linalg.svd(Phi); r = int(np.sum(s_ > 1e-10)); Kb = vt_[r:]
    blk = lambda Ms: np.block([[Ms[a] if a == b else np.zeros((8, 8)) for b in range(m)] for a in range(m)])
    QV = blk([B[k] @ q @ B[k].T for k, q in zip(idx, Qs)])
    return Kb, QV, blk

def stable_part(Kb, QV):
    """groesster Q-invarianter Teilraum W von K (QV hermitesch): W <- {x in W : QV x in W} bis stabil."""
    Wb = Kb.T.astype(complex)               # Spalten = ONB
    while Wb.shape[1]:
        PW = Wb @ Wb.conj().T
        M = (np.eye(len(PW)) - PW) @ QV @ Wb
        _, s, vh = np.linalg.svd(M)
        nk = Wb.shape[1] - int(np.sum(s > 1e-9))
        if nk == Wb.shape[1]: break
        Wb = Wb @ vh[Wb.shape[1]-nk:].conj().T
    return Wb

def R0(idx, sg):
    A = np.vstack([(np.array(sg)[:, None]*VS[list(idx)]).T, np.ones(len(idx))])
    return len(idx) - np.linalg.matrix_rank(A, tol=1e-10)

def run(idx, sg, full=False):
    Kb, QV, blk = ops(idx, sg)
    Wb = stable_part(Kb, QV)
    w = np.sort(np.linalg.eigvalsh(Wb.conj().T @ QV @ Wb)) if Wb.shape[1] else np.array([])
    res = dict(dimK=len(Kb), dimW=Wb.shape[1], n0=int(np.sum(np.abs(w) < 1e-6)), n1=int(np.sum(np.abs(w-1) < 1e-6)),
               R0=R0(idx, sg), specW=tuple(np.round(w, 6)), rank_v=int(np.linalg.matrix_rank(VS[list(idx)], tol=1e-10)))
    if full:
        # Rest ausserhalb W: Spektrum der gestauchten Ladung und Leck
        PK = Kb.T @ Kb; PW = (Wb @ Wb.conj().T).real if Wb.shape[1] else 0*PK
        PR = PK - PW
        U = np.linalg.svd(PR)[0][:, :len(Kb) - Wb.shape[1]]
        res['specR'] = tuple(np.round(np.linalg.eigvalsh(U.conj().T @ QV @ U), 6))
        res['leakR'] = round(float(np.linalg.norm(QV @ U - U @ (U.conj().T @ QV @ U), 2)), 6) if U.shape[1] else 0.0
        # su(3) im W-Teil
        SV = [blk([B[k] @ g @ B[k].T for k in idx]) for g in Sg]
        Km = np.array([[np.trace(a @ b) for b in SV] for a in SV]); Ki = np.linalg.inv(Km)
        Cas = -sum(Ki[i, j] * SV[i] @ SV[j] for i in range(8) for j in range(8))
        if Wb.shape[1]:
            cw = np.linalg.eigvalsh(Wb.conj().T @ Cas @ Wb)
            res['casW'] = (int(np.sum(np.abs(cw) < 1e-6)), int(np.sum(np.abs(cw) > 1e-6)))
        # Nullteiler-Probe: Komponenten zufaelliger (komplexer) Kernelemente
        smin = np.inf
        for _ in range(40):
            c = rng.normal(size=len(Kb)) + 1j*rng.normal(size=len(Kb)); x = Kb.T @ c
            for j, k in enumerate(idx):
                y = B[k].T @ x[8*j:8*j+8]
                if np.linalg.norm(y) < 1e-9: continue
                smin = min(smin, np.linalg.svd(Lm(y/np.linalg.norm(y)), compute_uv=False).min())
        res['smin'] = round(float(smin), 6)
    return res

TR = (1, 1, 1, 1, 1)
print("=== Kontrolle: Vierer-Teilauswahlen (transportierte Orientierung) ===")
c4 = [(idx, run(idx, (1,)*4)) for idx in itertools.combinations(range(9), 4)]
print("Auswahlen mit n_gen >= 1:", sum(r['n0'] >= 1 for _, r in c4), "; Regel n_gen = dim R0 in allen 126:", all(r['n0'] == r['R0'] for _, r in c4))
print("Spektrum W bei n_gen = 1 (Beispiel):", next(r['specW'] for _, r in c4 if r['n0'] == 1))

print("\n=== H143b/c/d: alle 126 Fuenferauswahlen, transportierte Orientierung ===")
classes = {}
for idx in itertools.combinations(range(9), 5):
    r = run(idx, TR, full=True)
    key = (r['rank_v'], r['dimK'], r['dimW'], r['n0'], r['n1'], r['R0'], r['specW'], r['specR'], r['leakR'], r.get('casW'))
    classes.setdefault(key, []).append((idx, r['smin']))
for key, lst in sorted(classes.items(), key=lambda t: -t[0][3]):
    cc = common_charge(lst[0][0])
    print(f"Rang v {key[0]}, dim K {key[1]}, dim W {key[2]}, n_gen (EW 0) {key[3]}, EW 1 {key[4]}, dim R0 {key[5]}")
    print(f"   Spektrum W {key[6]}")
    print(f"   su(3) in W (Singulett, Farbe) {key[9]}; Rest K/W: Spektrum {key[7]}, Leck {key[8]}")
    print(f"   {len(lst)} Auswahlen, z. B. {[lab(k) for k in lst[0][0]]}; min smin Kern-Komponenten {min(s for _, s in lst):.4f}; min Leck^2 gemeinsame Ladung {cc:.4f}")
nmax = max(k[3] for k in classes)
print("H143b: Auswahlen mit n_gen >= 1:", sum(len(l) for k, l in classes.items() if k[3] >= 1), "; mit n_gen >= 2:", sum(len(l) for k, l in classes.items() if k[3] >= 2), "; max n_gen:", nmax)

print("\n=== H143a: Regel n_gen = dim R0, alle 126 x 16 Orientierungen ===")
bad = []; hist = {}; viol01 = 0
for idx in itertools.combinations(range(9), 5):
    for sg in itertools.product([1, -1], repeat=4):
        r = run(idx, (1,) + sg)
        if r['n0'] != r['R0']: bad.append((idx, (1,) + sg, r['n0'], r['R0']))
        if r['n0'] != r['n1']: viol01 += 1
        hist[r['n0']] = hist.get(r['n0'], 0) + 1
print("Abweichungen:", len(bad), bad[:5])
print("Faelle mit #EW0 != #EW1:", viol01)
print("Verteilung n_gen ueber 2016 Faelle:", dict(sorted(hist.items())))
