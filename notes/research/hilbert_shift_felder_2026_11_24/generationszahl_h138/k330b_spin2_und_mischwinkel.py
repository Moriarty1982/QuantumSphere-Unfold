"""k330b (zu H147): (1) Berichtigte Auswertung des Ableitungskanals: k330 projizierte den su(3)-Anteil von D_{x,y} mit einem nicht
spektralen Projektor (Rang 3-5 je Tripel, Rechenfehler der Auswertung, nicht der Algebra). Hier: Spannweite der D_{x,y} und Spin-2-Anteil
ueber die Eigenbasis der ad-Casimir-Matrix. (2) Nachtraeglich, Erkundung (nicht in der Vorab-Notiz): Teilfrage des Autors 25.11. 20:45,
zwei skalare Richtungen c(x)e0 und c(x)e7 im Rest und ihr Mischwinkel. Definitionen aus k330 per exec (ohne Ausgabe)."""
import itertools, numpy as np, io, contextlib
src = open('k330_rest_graviton.py').read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(src.split('print("\\n=== H147a')[0])
Dv = np.array([D.ravel() for D in Dmaps]).T
print("(1) Rang der Spannweite aller D_x,y:", np.linalg.matrix_rank(Dv, tol=1e-8), "(dim g2 = 14)")
for tri in cands:
    W3 = I8[:, list(tri)]; so3 = so3_for(W3)
    SV = np.array([X.ravel() for X in su3]).T; Pinv = np.linalg.pinv(SV)
    ad = lambda X: Pinv @ np.array([(X @ Y - Y @ X).ravel() for Y in su3]).T
    Cad = -sum(ad(X) @ ad(X) for X in so3); eva, Ua = np.linalg.eig(Cad)
    # g2 = su3 (+) Komplement; su3-Anteil der D ueber orthogonale Projektion auf span su3, dann Spektralkoordinaten
    coef = Pinv @ Dv; spec = np.linalg.solve(Ua, coef)
    sel = np.abs(eva.real - np.min(eva.real[np.abs(eva.real - 6) < 1]) ) < 1e-6 if np.any(np.abs(eva.real - 6) < 1) else None
    n2 = int(np.sum(np.abs(eva.real - 6*np.mean(eva.real[np.argsort(-eva.real)[:5]])/6) < 1e-6))
    top = np.argsort(-eva.real)[:5]
    print(f"   Tripel e{tri}: ad-Casimir-Eigenwerte (Spin 2 erwartet 5x gleich) {np.round(np.sort(eva.real)[::-1], 4)}; Rang des Spin-2-Anteils der D: {np.linalg.matrix_rank(spec[top], tol=1e-8)}")
print("\n(2) Zwei Skalare c(x)e0, c(x)e7 (Erkundung, nachtraeglich)")
Q8 = B[0] @ Q[0] @ B[0].T
w, U = np.linalg.eigh(Q8)
for phi in (0.0, np.pi/3, np.pi/2, np.pi):
    x = (np.eye(8)[:, :8] @ np.eye(8))[:, 0]
    y = U @ np.diag(np.exp(1j*phi*w)) @ U.conj().T @ x          # exp(i phi Q) e0
    y = y / np.exp(1j*np.angle(y[0])) if abs(y[0]) > 1e-12 else y / np.exp(1j*np.angle(y[7]))
    print(f"   exp(i*{phi:.4f}*Q) e0 = {np.round(y, 6)}  (nur e0, e7 besetzt, reell bis auf Phase: {np.allclose(y[1:7], 0) and np.allclose(y.imag, 0, atol=1e-12)})")
# Automorphismen (g2) fixieren e0: kein Automorphismus mischt e0 und e7
print("   max |D e0| ueber g2:", max(np.abs(g @ I8[0]).max() for g in g2))
# algebraische Unterscheidung: e0 Einheit (e0^2 = e0), e7^2 = -e0; s (nur Imaginaerteil) und N
for name, v in (("e0", I8[0]), ("e7", I8[7])):
    print(f"   {name}: Quadrat {np.round(mul(v, v), 6)[[0, 7]]}, N = {v @ v:.0f}, s (Im) = {v[1:] @ v[1:]:.0f}")
