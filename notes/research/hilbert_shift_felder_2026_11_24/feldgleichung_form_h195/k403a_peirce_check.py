import numpy as np
rng = np.random.default_rng(1)
# Oktonion-Multiplikation (Cayley-Dickson), wie k387
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])
e = np.eye(8); C = np.array([[mul(e[i], e[j]) for j in range(8)] for i in range(8)])
cj = np.diag([1.0] + [-1.0] * 7)
# W als (3,3,8); Jordan-Produkt
mm = lambda X, Y: np.einsum('ija,jkb,abc->ikc', X, Y, C)
jo = lambda X, Y: 0.5 * (mm(X, Y) + mm(Y, X))
# diagonales Vakuum mit Eigenwerten l (in der Eigenbasis)
l = np.sort([1 + np.sqrt(2) * np.cos(2/9 + 2*np.pi*k/3) for k in range(3)])
W0 = np.zeros((3,3,8));
for i in range(3): W0[i,i,0] = l[i]
# Off-Diagonal-Mode X_ij: Oktonion x in Position (i,j), hermitesch gespiegelt
def Xmode(i, j, x):
    X = np.zeros((3,3,8)); X[i,j] = x; X[j,i] = cj @ x; return X
print("Peirce-Eigenwert: W0 o X_ij = ? * X_ij  (erwartet (l_i+l_j)/2)")
for (i,j) in [(0,1),(0,2),(1,2)]:
    x = rng.normal(size=8)
    X = Xmode(i,j,x); WX = jo(W0, X)
    # Verhaeltnis WX / X auf der (i,j)-Komponente
    ratio = WX[i,j] / X[i,j]
    print(f"  (i,j)=({i},{j}): Faktor = {ratio[0]:.6f}, erwartet (l_i+l_j)/2 = {(l[i]+l[j])/2:.6f}, "
          f"konstant ueber Komponenten: {np.allclose(ratio, ratio[0])}")
print("\nKinetische Normen der Mode (i,j), |x|^2 = 1:")
print("  N0 = Tr(X o X)       (flach)         -> erwartet const")
print("  N1 = Tr(X o (W0 o X))                -> erwartet (l_i+l_j)/2")
print("  N2 = Tr((W0 o X) o (W0 o X))         -> erwartet ((l_i+l_j)/2)^2")
tr = lambda X: X[0,0,0] + X[1,1,0] + X[2,2,0]
for (i,j) in [(0,1),(0,2),(1,2)]:
    x = rng.normal(size=8); x = x/np.linalg.norm(x)
    X = Xmode(i,j,x); WX = jo(W0,X)
    N0 = tr(jo(X,X)); N1 = tr(jo(X, WX)); N2 = tr(jo(WX,WX))
    s = (l[i]+l[j])/2
    print(f"  ({i},{j}): N0={N0:.4f}  N1={N1:.4f} (s={s:.4f})  N2={N2:.4f} (s^2={s**2:.4f})")
