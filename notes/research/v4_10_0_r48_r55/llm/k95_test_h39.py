"""k95: Test der Vorab-Notiz H39 (Commit 5c916b8): Lesart je Teilchenart als Untergruppe der A4 der Ablage; Dirac-Sektoren mit <tau>,
Neutrinos (Majorana) mit einer anderen Untergruppe G_M."""
import itertools, numpy as np

RNG = np.array([(0.275, 0.345), (0.430, 0.596), (0.02023, 0.02376)])
# A4: gerade Permutationen x Vorzeichen mit gerader Zahl von -1 (wie Dixon.a4)
perms = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
signs = [s for s in itertools.product((1, -1), repeat=3) if np.prod(s) == 1]
def mat(p, s):
    M = np.zeros((3, 3), int)
    for i in range(3): M[p[i], i] = s[i]
    return M
A4 = [mat(p, s) for p in perms for s in signs]
key = lambda M: tuple(M.flatten())
assert len({key(g) for g in A4}) == 12
def closure(gens):
    G = {key(np.eye(3, dtype=int)): np.eye(3, dtype=int)}
    frontier = list(G.values())
    while frontier:
        new = []
        for a in frontier:
            for g in gens:
                b = a@g
                if key(b) not in G: G[key(b)] = b; new.append(b)
        frontier = new
    return G
subs = {}
for a in A4:
    for b in A4:
        G = closure([a, b]); subs[frozenset(G)] = list(G.values())
subs = list(subs.values())
tau = mat((1, 2, 0), (1, 1, 1))
print("Untergruppen von A4 (Ordnung: Anzahl):", {o: sum(len(s) == o for s in subs) for o in sorted({len(s) for s in subs})})

def joint_eig(G):
    rng = np.random.default_rng(7)
    H = sum(rng.normal()*(g + g.T)/2 + 1j*rng.normal()*(g - g.T)/2 for g in G)
    w, V = np.linalg.eigh(H)
    groups = []; i = 0
    while i < 3:
        j = i
        while j + 1 < 3 and abs(w[j + 1] - w[i]) < 1e-9: j += 1
        groups.append(V[:, i:j + 1]); i = j + 1
    return groups

Ue = np.hstack(joint_eig(closure([tau]).values()))          # Fourier-Spalten
TH = np.linspace(0, np.pi, 721); PH = np.linspace(0, 2*np.pi, 73)
def candidates(G):
    gr = joint_eig(G); dims = sorted(g.shape[1] for g in gr)
    if dims == [1, 1, 1]: return [np.hstack(gr)], "fest"
    if dims == [1, 2]:
        one = [g for g in gr if g.shape[1] == 1][0]; two = [g for g in gr if g.shape[1] == 2][0]
        a, b = two[:, 0], two[:, 1]; out = []
        for t in TH:
            for f in PH:
                c, s = np.cos(t), np.sin(t)*np.exp(1j*f)
                out.append(np.column_stack([one[:, 0], c*a + s*b, -np.conj(s)*a + c*b]))
        return out, "ein Winkel"
    return [], "keine Vorhersage"
def pmns(U):
    a = abs(U)**2; s13 = a[0, 2]
    return np.array([a[0, 1]/(1 - s13), a[1, 2]/(1 - s13), s13]) if s13 < 1 - 1e-12 else None
inside = lambda v: v is not None and all(R[0] <= x <= R[1] for x, R in zip(v, RNG))

res = {}
for G in subs:
    o = len(G)
    if o in (12,) or {key(g) for g in G} == set(closure([tau]).keys()): continue
    kind = {1: "trivial", 2: "Z2", 3: "Z3", 4: "Klein"}[o]
    Us, how = candidates(G)
    hits = []; s13hit = []
    for Un in Us:
        for pe in itertools.permutations(range(3)):
            for pn in itertools.permutations(range(3)):
                v = pmns(Ue[:, pe].conj().T@Un[:, pn])
                if v is None: continue
                if RNG[2, 0] <= v[2] <= RNG[2, 1]: s13hit.append(v)
                if inside(v): hits.append(v)
    res.setdefault(kind, []).append((how, len(hits), np.array(s13hit), np.array(hits)))
for kind in ("trivial", "Klein", "Z2", "Z3"):
    for how, nh, s13h, hh in res.get(kind, []):
        line = f"G_M = {kind} ({how}): Treffer in allen drei 3sigma-Bereichen: {nh}"
        if len(s13h): line += (f"; bei sin^2 13 im Bereich ({len(s13h)} Faelle): sin^2 12 in [{s13h[:,0].min():.4f}, {s13h[:,0].max():.4f}],"
                               f" sin^2 23 in [{s13h[:,1].min():.4f}, {s13h[:,1].max():.4f}]")
        if nh: line += f"; Treffer: sin^2 12 in [{hh[:,0].min():.4f}, {hh[:,0].max():.4f}], sin^2 23 in [{hh[:,1].min():.4f}, {hh[:,1].max():.4f}]"
        print(line)
ok_a = all(nh == 0 for _, nh, _, _ in res["Klein"])
ok_b = any(nh > 0 for _, nh, _, _ in res["Z2"])
ok_c = all(nh == 0 for _, nh, _, _ in res["Z3"])
print(f"\nH39a (Klein: kein Treffer) -> {'bestaetigt' if ok_a else 'widerlegt'}")
print(f"H39b (Z2: Treffer) -> {'bestaetigt' if ok_b else 'widerlegt'}")
if ok_b:
    allh = np.vstack([hh for _, nh, _, hh in res["Z2"] if nh]); s13all = np.vstack([s for _, _, s, _ in res["Z2"] if len(s)])
    w12 = s13all[:, 0].max() - s13all[:, 0].min()
    # Schaerfe nur ueber die Zuordnungen, die ueberhaupt einen Treffer haben (TM2-Zuordnung)
    print(f"  Treffer insgesamt {len(allh)}: sin^2 12 in [{allh[:,0].min():.4f}, {allh[:,0].max():.4f}], sin^2 23 in [{allh[:,1].min():.4f}, {allh[:,1].max():.4f}]")
print(f"H39c (andere Z3: kein Treffer) -> {'bestaetigt' if ok_c else 'widerlegt'}")
print("H39d: u und d mit derselben Lesart <tau>: V = U_u^dagger U_d ist eine Permutationsmatrix; bei gleicher Zuordnung die Einheitsmatrix (qualitativ, kein Kriterium).")

# Nachkontrolle (nach der Auswertung, kein Teil des Kriteriums): Spannweiten je Zuordnung fuer G_M = Z2. Die Zuordnung, die trifft, ist die mit der
# festen Spalte an der Stelle von nu2 (TM2); andere Zuordnungen treffen nie und weiten die Spannweite im Kriterium auf.
G = [g for g in subs if len(g) == 2][0]
Us, _ = candidates(G)
by = {}
for Un in Us:
    for pe in itertools.permutations(range(3)):
        for pn in itertools.permutations(range(3)):
            v = pmns(Ue[:, pe].conj().T@Un[:, pn])
            if v is None or not (RNG[2, 0] <= v[2] <= RNG[2, 1]): continue
            by.setdefault(pn.index(0), []).append(v)          # Position der festen Spalte unter nu1, nu2, nu3
for pos, vs in sorted(by.items()):
    vs = np.array(vs)
    print(f"Nachkontrolle Z2, feste Spalte als nu{pos+1}: {len(vs)} Faelle mit sin^2 13 im Bereich; sin^2 12 in [{vs[:,0].min():.4f}, {vs[:,0].max():.4f}],"
          f" sin^2 23 in [{vs[:,1].min():.4f}, {vs[:,1].max():.4f}]; Treffer {sum(inside(v) for v in vs)}")
print("Vergleich: NuFIT 6.0 Bestwert sin^2 12 = 0.307 (3sigma bis 0.345); TM2-Wert 1/(3 cos^2 theta13) bei sin^2 13 = 0.02195:", round(1/(3*(1 - 0.02195)), 4))
