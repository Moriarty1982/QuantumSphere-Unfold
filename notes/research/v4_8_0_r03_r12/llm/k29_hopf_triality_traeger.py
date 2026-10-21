"""k29: Traeger der drei Triality-Plaetze in der oktonionischen Hopf-Faserung S7 -> S15 -> S8 (thm:hopf). Reine Algebra."""
import numpy as np, contextlib, io, os
from scipy.linalg import expm
here = os.path.dirname(os.path.abspath(__file__))
with contextlib.redirect_stdout(io.StringIO()):
    exec(open(os.path.join(here, "k28_sedenion_generationen.py")).read())
rng = np.random.default_rng(29)
cj = lambda a: a*np.array([1] + [-1]*7)
nrm = lambda a: np.sqrt(a @ a)
one = np.eye(8)[0]
def unit(): v = rng.normal(size=8); return v/nrm(v)

# 1) Hopf-Abbildung h(x,y) = (|x|^2 - |y|^2, 2 x conj(y)) bildet S15 auf S8 ab
ok = True
for _ in range(200):
    z = rng.normal(size=16); z /= nrm(z); x, y = z[:8], z[8:]
    v = 2*omul(x, cj(y)); ok &= np.isclose((x@x - y@y)**2 + v@v, 1)
print("1) Hopf-Abbildung S15 -> S8 (Normtreue):", ok)

# 2) Einheits-Tripel (a,b,c) mit (ab)c = 1: zyklisch invariant und unter (a,b,c) -> (conj a, conj c, conj b)
okc = okr = True
for _ in range(200):
    a, b = unit(), unit(); c = cj(omul(a, b))
    okc &= np.allclose(omul(omul(a, b), c), one) and np.allclose(omul(omul(b, c), a), one) and np.allclose(omul(omul(c, a), b), one)
    okr &= np.allclose(omul(omul(cj(a), cj(c)), cj(b)), one)
print("2) Tripel (ab)c = 1 ist zyklisch abgeschlossen:", okc, "| unter (a,b,c) -> (conj a, conj c, conj b):", okr)

# 3) Verbindung zur Hopf-Faserung: auf dem Aequator |x| = |y| = 1/sqrt2 ist a = sqrt2 x, b = sqrt2 conj(y),
#    Basis-Punkt v = 2 x conj(y) = ab, dritter Platz c = conj(v). Faser ueber v: alle a, b = conj(a) v.
okh = okf = True
for _ in range(200):
    x, y = unit()/np.sqrt(2), unit()/np.sqrt(2)
    a, b = np.sqrt(2)*x, np.sqrt(2)*cj(y); v = 2*omul(x, cj(y))
    okh &= np.allclose(omul(a, b), v) and np.allclose(omul(omul(a, b), cj(v)), one)
    a2 = unit(); b2 = omul(cj(a2), v)
    okf &= np.allclose(omul(a2, b2), v)
print("3) Aequator-Faser: (a, b, c) = (sqrt2 x, sqrt2 conj y, conj v) ist Einheits-Tripel:", okh,
      "| Faser ueber v = {(a, conj(a) v)} (S7):", okf)

# 4) G2 diagonal: erhaelt Tripel und vertauscht mit der Hopf-Abbildung
okg = True
for _ in range(10):
    g = expm((Dsp @ rng.normal(size=Dsp.shape[1])).reshape(8, 8))
    a, b = unit(), unit(); c = cj(omul(a, b))
    okg &= np.allclose(omul(omul(g @ a, g @ b), g @ c), one)
    x, y = rng.normal(size=8), rng.normal(size=8)
    okg &= np.allclose(g @ omul(x, cj(y)), omul(g @ x, cj(g @ y)))
print("4) G2 (diagonal) erhaelt Tripel und ist mit der Hopf-Abbildung vertraeglich:", okg)

# 5) Wo liegen Farbe und Generation? Farbtriplett e4,e5,e6 in jedem Platz; der ganze Generationen-Raum ist
#    der Tripel-Raum S7 x S7 (Dimension 14), die Generationen-S3 permutiert die Plaetze.
print("5) Dimension des Tripel-Raums {(a,b,c) : (ab)c = 1, |a|=|b|=|c|=1}: 7 + 7 = 14 (a, b frei, c bestimmt)")
# 6) Symmetrischer Punkt der Triole: a = b = c mit a^3 = 1 -> a = cos(2pi/3) + sin(2pi/3) u, u imaginaere Einheit
u = np.eye(8)[7]; w = np.cos(2*np.pi/3)*one + np.sin(2*np.pi/3)*u
print("6) Symmetrisches Tripel a = b = c = exp(2pi/3 e7): (aa)a = 1:", np.allclose(omul(omul(w, w), w), one),
      "| a liegt in span(1, e7), der komplexen Ebene des Kaskaden-Endes")

# 7) Stabilisator des symmetrischen Tripels in g2: Derivationen D mit D(a) = 0 fuer a = exp(2pi/3 e7)
St = null_space(np.array([(Dsp[:, k].reshape(8, 8) @ w) for k in range(Dsp.shape[1])]).T)
print("7) Dimension des Stabilisators von a = exp(2pi/3 e7) in g2:", St.shape[1], "(su(3) = 8, also die Farbgruppe)")
# 8) Einfache Probe: Tripel in der komplexen Ebene span(1,e7) haben Phasen alpha_k mit Summe 0 mod 2pi.
#    Koide-Phasen delta + 2pi k/3 erfuellen das nur fuer 3 delta = 0 mod 2pi.
d_lep = 0.2222
print(f"8) Koide-Phasen als Tripel-Phasen verlangen delta in (2pi/3)Z; gemessen delta = {d_lep}"
      f" -> Summe der Phasen = {3*d_lep:.4f} statt 0 mod 2pi: direkte Lesart scheitert")
