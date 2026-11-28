"""k452 (Erkundung, nicht blind): Entstehung von HS(2), HS(3), HS(4) im Wand-Bild aus k449.
Jede Stufe = eine weitere Wand um das Bisherige: A_(n+1) = A_n + A_n l, Paar (a, b) = (innen, aussen),
(a, b)(c, d) = (ac + g conj(d) b, d a + b conj(c)),  g = l^2: -1 = Verdrehung ueber die Wand, +1 = Vorzeichen (Spiegel, k449).
Geprueft je Stufe und Vorzeichenfolge: kommutativ, assoziativ, alternativ, Norm multiplikativ, Nullteiler (Leck).
Aufruf aus diesem Ordner: python3 k452_innen_aussen_turm.py > k452_out.txt
"""
import itertools
import numpy as np

rng = np.random.default_rng(452)


def conj(x):
    y = -x.copy()
    y[0] = x[0]
    return y


def mul(x, y, gs):
    """Cayley-Dickson-Produkt mit Vorzeichenfolge gs (innerste Wand zuerst)"""
    n = len(x)
    if n == 1:
        return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    g = gs[-1]
    inner = gs[:-1]
    return np.concatenate([mul(a, c, inner) + g * mul(conj(d), b, inner), mul(d, a, inner) + mul(b, conj(c), inner)])


def qnorm(x, gs):
    """Normform N(x) = x conj(x) (reell)"""
    return mul(x, conj(x), gs)[0]


def props(gs, trials=200):
    dim = 2 ** len(gs)
    com = ass = alt = nm = 0.0
    for _ in range(trials):
        a, b, c = rng.normal(size=(3, dim))
        com = max(com, np.abs(mul(a, b, gs) - mul(b, a, gs)).max())
        ass = max(ass, np.abs(mul(mul(a, b, gs), c, gs) - mul(a, mul(b, c, gs), gs)).max())
        alt = max(alt, np.abs(mul(mul(a, a, gs), b, gs) - mul(a, mul(a, b, gs), gs)).max())
        nm = max(nm, abs(qnorm(mul(a, b, gs), gs) - qnorm(a, gs) * qnorm(b, gs)))
    # Nullteiler unter e_i +- e_j (und e_i allein)
    E = np.eye(dim)
    cands = [E[i] for i in range(dim)] + [E[i] + s * E[j] for i in range(dim) for j in range(i + 1, dim) for s in (1, -1)]
    zd = None
    for x in cands:
        for y in cands:
            if np.abs(mul(x, y, gs)).max() < 1e-12:
                zd = (x, y)
                break
        if zd is not None:
            break
    return com, ass, alt, nm, zd


def fmt(x):
    idx = [f"{'+' if v > 0 else '-'}e{i}" for i, v in enumerate(x) if abs(v) > 0]
    return "".join(idx)


print("=" * 100)
print("k452  Wand-Bild fuer den Turm: jede Stufe eine weitere Wand, Vorzeichen g = l^2 je Wand")
print("=" * 100)
names = {0: "HS(0) R", 1: "HS(1)", 2: "HS(2)", 3: "HS(3)", 4: "HS(4)"}
print("\nTeil 1: Verdrehung an jeder Wand (g = -1 ueberall) = Divisionsturm")
print(f"  {'Stufe':8s} {'Dim':>4s} {'kommut.':>9s} {'assoz.':>9s} {'altern.':>9s} {'|N(ab)-N(a)N(b)|':>18s}  Nullteiler (Leck)")
for n in range(1, 5):
    gs = [-1] * n
    com, ass, alt, nm, zd = props(gs)
    z = f"{fmt(zd[0])} * {fmt(zd[1])} = 0" if zd else "keiner"
    print(f"  {names[n]:8s} {2**n:4d} {com:9.1e} {ass:9.1e} {alt:9.1e} {nm:18.1e}  {z}")

print("\nTeil 2: alle Vorzeichenfolgen bis HS(3): Divisionsalgebra (kein Nullteiler, Norm definit) nur bei g = -1 an jeder Wand")
for n in range(1, 4):
    for gs in itertools.product((-1, 1), repeat=n):
        com, ass, alt, nm, zd = props(list(gs), trials=60)
        # Signatur der Normform: Diagonale von N(e_i)
        dim = 2 ** n
        sig = [int(round(qnorm(np.eye(dim)[i], list(gs)))) for i in range(dim)]
        p, m = sig.count(1), sig.count(-1)
        print(f"  n={n} g={list(gs)}: Normform-Signatur (+{p}, -{m}), Nullteiler {'ja' if zd else 'nein'},"
              f" kommutativ {com < 1e-9}, assoziativ {ass < 1e-9}, alternativ {alt < 1e-9}, Norm multiplikativ {nm < 1e-9}")

print("\nTeil 3: Reihenfolge und Klammerung der Wanddurchgaenge (Basis-Einheiten, g = -1)")
E4, E8 = np.eye(4), np.eye(8)
print(f"  HS(2): e1 e2 = {fmt(mul(E4[1], E4[2], [-1, -1]))}, e2 e1 = {fmt(mul(E4[2], E4[1], [-1, -1]))}"
      "  -> Reihenfolge zweier Wanddurchgaenge zaehlt (Vorzeichen)")
g3 = [-1, -1, -1]
print(f"  HS(3): (e1 e2) e4 = {fmt(mul(mul(E8[1], E8[2], g3), E8[4], g3))}, e1 (e2 e4) = {fmt(mul(E8[1], mul(E8[2], E8[4], g3), g3))}"
      "  -> Klammerung dreier Durchgaenge zaehlt")
g4 = [-1] * 4
E16 = np.eye(16)
x = E16[1] + E16[10]; y = E16[4] - E16[15]
print(f"  HS(4): N(x) = {qnorm(x, g4):.0f}, N(y) = {qnorm(y, g4):.0f}, N(xy) = {qnorm(mul(x, y, g4), g4):.0f}"
      "  -> zwei Felder endlicher Intensitaet loeschen sich nach vier Waenden aus (Leck)")

print("\nTeil 4: die Verdrehung der neuen Wand steht senkrecht auf allen inneren (l antikommutiert mit allen Imaginaereinheiten von A_n)")
for n in (2, 3, 4):
    gs = [-1] * n
    dim = 2 ** n
    E = np.eye(dim)
    l = E[dim // 2]
    worst = max(np.abs(mul(l, E[i], gs) + mul(E[i], l, gs)).max() for i in range(1, dim // 2))
    print(f"  {names[n]}: max |l e_i + e_i l| ueber i = 1..{dim//2 - 1}: {worst:.1e}")

print("\nTeil 5: Warum es anhaelt, physikalisch: die Wand zwischen innen und aussen ist eine Sphaere S^(N-1) im Feldraum (N = 2^n).")
print("  Eine Verdrehung in jede Richtung braucht auf der Wand N-1 ueberall von null verschiedene, orthonormale Tangentialfelder")
print("  (ein Rahmen). Kandidat: v_i(x) = e_i x (Linksmultiplikation mit den Imaginaereinheiten). Pruefung auf zufaelligen x der Wand:")
for n in (1, 2, 3, 4):
    gs = [-1] * n
    N = 2 ** n
    E = np.eye(N)
    worst_t = worst_o = 0.0
    for _ in range(300):
        x = rng.normal(size=N); x /= np.linalg.norm(x)
        V = np.array([mul(E[i], x, gs) for i in range(1, N)])
        worst_t = max(worst_t, np.abs(V @ x).max())                     # tangential?
        G = V @ V.T
        worst_o = max(worst_o, np.abs(G - np.eye(N - 1)).max())         # orthonormal?
    print(f"  {names[n]}: Wand S^{N-1}: max |<v_i, x>| = {worst_t:.1e}, max |Gram - 1| = {worst_o:.1e}"
          f"  -> {'voller Verdrehungsrahmen' if worst_o < 1e-9 else 'KEIN Rahmen (Richtungen fallen zusammen)'}")


def rho(N):
    """Radon-Hurwitz-Zahl: N = 2^(4a+b) * ungerade, rho = 8a + 2^b; S^(N-1) traegt genau rho(N) - 1 unabhaengige Vektorfelder"""
    k = 0
    while N % 2 == 0:
        N //= 2; k += 1
    a, b = divmod(k, 4)
    return 8 * a + 2 ** b


print("\n  Radon-Hurwitz: Zahl unabhaengiger, nirgends verschwindender Verdrehungsfelder auf der Wand S^(N-1) = rho(N) - 1")
for n in range(0, 7):
    N = 2 ** n
    r = rho(N) - 1
    print(f"    HS({n}): N = {N:3d}, Wand S^{N-1:<3d}: {r:2d} Felder von {N-1:2d} noetigen -> {'voller Rahmen' if r == N - 1 else 'Rahmen fehlt ' + str(N - 1 - r)}")
print("  Voller Rahmen nur fuer N = 1, 2, 4, 8 (Adams 1960: Hopf-Invariante 1 nur in diesen Dimensionen).")

print("\nTeil 6: Was jede Stufe neu zeigt (Ableitungsalgebra Der, aus k253/k254; hier nur die Dimensionen nachgerechnet)")


def der_dim(n):
    """dim der Loesungen D linear mit D(xy) = D(x)y + xD(y) auf der Basis"""
    gs = [-1] * n
    N = 2 ** n
    E = np.eye(N)
    T = np.array([[mul(E[i], E[j], gs) for j in range(N)] for i in range(N)])  # T[i,j] = e_i e_j
    # direkte Konstruktion
    M = []
    for i in range(N):
        for j in range(N):
            for c in range(N):
                r = np.zeros(N * N)
                for k in range(N):
                    r[c * N + k] += T[i, j][k]                         # D(e_i e_j)_c
                for k in range(N):
                    # (D(e_i) e_j)_c = sum_m D[m,i] (e_m e_j)_c
                    r[k * N + i] -= T[k, j][c]
                    # (e_i D(e_j))_c = sum_m D[m,j] (e_i e_m)_c
                    r[k * N + j] -= T[i, k][c]
                M.append(r)
    M = np.array(M)
    return N * N - np.linalg.matrix_rank(M, tol=1e-9)


for n in range(0, 5):
    print(f"  HS({n}): dim Der = {der_dim(n)}")

print("\nTeil 7: Feldgleichung je Stufe: D = d_0 + sum_i e_i d_i (Cauchy-Riemann / Fueter / Dirac der Stufe), D f = 0.")
print("  Sie ist nur dann eine Wurzel der Wellen-/Laplace-Gleichung (Dbar D f = Laplace f fuer JEDES Feld f), wenn die Linksmultiplikationen")
print("  L_i eine Clifford-Darstellung bilden: L_i L_j + L_j L_i = -2 delta_ij. Pruefung als Matrizen:")
for n in range(1, 5):
    gs = [-1] * n
    N = 2 ** n
    E = np.eye(N)
    L = [np.array([mul(E[i], E[k], gs) for k in range(N)]).T for i in range(1, N)]   # L_i als Matrix (Spalte k = e_i e_k)
    worst = 0.0
    for a_ in range(N - 1):
        for b_ in range(N - 1):
            A = L[a_] @ L[b_] + L[b_] @ L[a_] + 2 * (a_ == b_) * np.eye(N)
            worst = max(worst, np.abs(A).max())
    # direkt am Feld: Dbar D f - Laplace f fuer ein Polynomfeld, numerisch ueber Differenzen ist unnoetig: Dbar D = d0^2 + sum_ij L_i L_j d_i d_j (symm.)
    print(f"  {names[n]}: max |L_i L_j + L_j L_i + 2 delta_ij| = {worst:.1e}  -> {'Dbar D = Laplace, Feldgleichung erster Ordnung wohlgestellt' if worst < 1e-9 else 'Dbar D != Laplace: keine Wurzel der Wellengleichung'}")
