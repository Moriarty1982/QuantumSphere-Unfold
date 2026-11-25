"""k330 (Test H147): Spin-Zerlegung der Rest-Generation unter SO(3) subset SU(3)_Farbe (Lesart A); symmetrisches Algebrenprodukt und
Ableitungskanal; Universalitaet c o c. Vorab: Vorab_Notiz_H147_Rest_als_Graviton.md. Definitionen aus k328 (-> k326 -> k325) per exec.
Lesart B (Hauptuntergruppe SO(3) in G2, Im O = Spin 3) ist Darstellungstheorie und wird hier nicht numerisch gebaut."""
import itertools, numpy as np
src = open('k328_rest_hs0.py').read(); exec(src.split('err = 0')[0])
I8 = np.eye(8)
L8 = [np.array([mul(I8[a], I8[j]) for j in range(8)]).T for a in range(8)]     # L_{e_a} auf O
R8 = [np.array([mul(I8[j], I8[a]) for j in range(8)]).T for a in range(8)]
g2 = derivations(C8)                                                            # 14 Ableitungen von O
GV = np.array([g.ravel() for g in g2])
M = np.array([g @ I8[7] for g in g2]).T; _, sv, vt = np.linalg.svd(M)
su3 = [ (c @ GV).reshape(8, 8) for c in vt[np.sum(sv > 1e-9):] ]                 # Stabilisator von e7
print("dim g2, dim su3:", len(g2), len(su3))
J = L8[7]
# total reeller 3-Raum im Farbraum e1..e6 bzgl. J = L_e7; Lesart A: so(3) = {X in su3 : X W3 in W3}
def so3_for(W3):
    PW = W3 @ W3.T; S = np.array([((np.eye(8) - PW) @ X @ PW).ravel() for X in su3]).T
    _, s, vt = np.linalg.svd(S); co = vt[np.sum(s > 1e-9):]
    return [sum(c[i]*su3[i] for i in range(8)) for c in co]
cands = []
for tri in itertools.combinations(range(1, 7), 3):
    W3 = I8[:, list(tri)]
    if np.linalg.matrix_rank(np.hstack([W3, J @ W3]), tol=1e-9) == 6: cands.append(tri)
print("total reelle Koordinaten-Tripel im Farbraum:", cands)
def casimir_spins(gens, rep):   # rep: Funktion X -> Darstellungsmatrix; Normierung: Spin 1 auf W3 hat Casimir 2
    Cs = -sum(rep(X) @ rep(X) for X in gens)
    ev = np.linalg.eigvals(Cs).real
    return ev
results = []
for tri in cands:
    W3 = I8[:, list(tri)]; so3 = so3_for(W3)
    if len(so3) != 3: results.append((tri, len(so3))); continue
    # orthonormieren bzgl. Spur und so skalieren, dass Casimir auf W3 = 2
    B3 = np.array([X.ravel() for X in so3]); Qo, _ = np.linalg.qr(B3.T); so3 = [Qo[:, i].reshape(8, 8) for i in range(3)]
    cW = -sum(W3.T @ X @ X @ W3 for X in so3); sc = 2 / np.trace(cW) * 3; so3 = [X*np.sqrt(sc) for X in so3]
    comm = max(np.linalg.norm(X @ Y - Y @ X - sum(np.trace((X @ Y - Y @ X) @ Z.T)/np.trace(Z @ Z.T)*Z for Z in so3)) for X in so3 for Y in so3)
    spins = lambda ev: sorted(np.round((-1 + np.sqrt(1 + 4*np.maximum(ev, 0)))/2, 6))
    sO = spins(casimir_spins(so3, lambda X: X))                                            # auf C O (8)
    # Sym^2(O) aeusseres Produkt
    idx = [(i, j) for i in range(8) for j in range(i, 8)]
    def sym2(X):
        Mx = np.zeros((36, 36))
        for a, (i, j) in enumerate(idx):
            T = np.zeros((8, 8)); T[i, j] = T[j, i] = (1 if i == j else 1/np.sqrt(2))
            T2 = X @ T + T @ X.T
            for b, (k, l) in enumerate(idx): Mx[b, a] = T2[k, l] * (1 if k == l else np.sqrt(2))
        return Mx
    Csym = -sum(sym2(X) @ sym2(X) for X in so3); evs, Us = np.linalg.eigh((Csym + Csym.T)/2)
    s2 = spins(evs); n_spin2 = int(np.sum(np.abs(evs - 6) < 1e-6))
    # symmetrisches Algebrenprodukt auf dem Spin-2-Teil von Sym^2
    V2 = Us[:, np.abs(evs - 6) < 1e-6]
    def prodsym(vec):
        T = np.zeros((8, 8))
        for a, (i, j) in enumerate(idx): T[i, j] = T[j, i] = vec[a] / (1 if i == j else np.sqrt(2))
        return sum(T[i, j]*(mul(I8[i], I8[j]) + mul(I8[j], I8[i]))/2 for i in range(8) for j in range(8))
    img_sym = max(np.linalg.norm(prodsym(V2[:, k])) for k in range(V2.shape[1])) if V2.shape[1] else 0.0
    # Ableitungskanal D_{x,y} und Spin-2-Teil von su3 (ad-Wirkung)
    SV = np.array([X.ravel() for X in su3]).T; Pinv = np.linalg.pinv(SV)
    ad = lambda X: Pinv @ np.array([(X @ Y - Y @ X).ravel() for Y in su3]).T
    Cad = -sum(ad(X) @ ad(X) for X in so3); eva, Ua = np.linalg.eig(Cad); eva = eva.real
    sad = spins(eva); U2 = np.real(Ua[:, np.abs(eva - 6) < 1e-6])
    Dmaps = []
    for x in range(8):
        for y in range(8):
            Lx, Ly, Rx, Ry = L8[x], L8[y], R8[x], R8[y]
            Dmaps.append(Lx @ Ly - Ly @ Lx + Lx @ Ry - Ry @ Lx + Rx @ Ry - Ry @ Rx)
    Dv = np.array([D.ravel() for D in Dmaps]).T
    der_ok = np.linalg.matrix_rank(np.hstack([GV.T, Dv]), tol=1e-8) == 14
    coef = Pinv @ Dv                                    # su3-Anteil (Projektion auf span su3)
    # Spin-2-Anteil: Komponenten entlang U2 (in su3-Koordinaten); Rang
    P2 = U2 @ np.linalg.pinv(U2)
    rank2 = np.linalg.matrix_rank(P2 @ coef, tol=1e-8)
    results.append((tri, dict(comm=comm, spins_CO=sO, sym2_spin2=n_spin2, sym2_spins=sorted(set(s2)), img_sym_spin2=img_sym,
                              su3_spins=sorted(set(sad)), su3_n_spin2=int(np.sum(np.abs(eva - 6) < 1e-6)), D_in_g2=der_ok, rank_D_spin2=int(rank2))))
for tri, r in results:
    print(f"\nLesart A, total reelles Tripel e{tri}:")
    if isinstance(r, int): print("   so(3) nicht dreidimensional:", r); continue
    print(f"   so(3) abgeschlossen (Fehler {r['comm']:.1e}); Spins auf C O (8): {r['spins_CO']}")
    print(f"   Sym^2(O) aeusseres Produkt: Spins {r['sym2_spins']}, Spin-2-Dimension {r['sym2_spin2']}")
    print(f"   symmetrisches Algebrenprodukt auf dem Spin-2-Teil: max Norm {r['img_sym_spin2']:.1e}")
    print(f"   su(3) unter ad: Spins {r['su3_spins']}, Spin-2-Dimension {r['su3_n_spin2']}; D_x,y in g2: {r['D_in_g2']}; Rang des Spin-2-Anteils von D: {r['rank_D_spin2']}")
print("\n=== H147a: c neutral und Gram-masselos (Nachrechnung) ===")
Q8 = B[0] @ Q[0] @ B[0].T
cs = []
for m in (4, 5):
    for idx_ in itertools.combinations(range(9), m):
        V = VS[list(idx_)]; R0 = null(np.vstack([V.T, np.ones((1, m))]))
        for c in R0.T: cs.append((idx_, c))
print("Generationsauswahlen (Linien):", len(cs))
gm = 0
for idx_, c in cs:
    X = np.array([B[k].T @ (I8[0] + 1j*I8[7])/np.sqrt(2) for k in idx_]); G = X.conj() @ X.T
    gm = max(gm, np.linalg.norm(G @ c))
print(f"max |G c| (Lepton-Gram, Nullvektor): {gm:.1e}; Ladung/Farbe wirken als 1 (x) Q8 bzw. 1 (x) X (H145b), auf c also trivial")
print("\n=== H147d: Universalitaet c o c ===")
uni = 0
for idx_, c in cs:
    sup = np.abs(c) > 1e-9; cc = c[sup]**2; uni = max(uni, (cc.max() - cc.min())/cc.max())
print(f"max relative Spreizung von c o c auf dem Traeger: {uni:.1e}; Traegergroessen: {sorted(set(int(np.sum(np.abs(c) > 1e-9)) for _, c in cs))}")
print("Vorzeichen von c (Beispiel):", np.round(cs[0][1]/np.abs(cs[0][1]).max(), 6))
