"""H47 (Vorab-Notiz df0c788): beta_sym als Verhaeltnis zweier Horizontzaehlungen."""
from mpmath import mp, mpf, sqrt, exp, pi, log, findroot, atanh
mp.dps = 30
JMAX = 4000  # k = 2j bis 8000
def a(k): j = mpf(k)/2; return sqrt(j*(j+1))
def Z(g, w):  # w(k) Gewicht, k = 2j
    return sum(w(k)*exp(-2*pi*g*a(k)) for k in range(1, 2*JMAX+1)) - 1
def rest(g, w): k=2*JMAX+1; return w(k)*exp(-2*pi*g*a(k))  # grobe Restgroesse (erstes ausgelassenes Glied)
g_min = log(2)/(pi*sqrt(3))
g_dlm = findroot(lambda g: Z(g, lambda k: 2), 0.24)
g_gm  = findroot(lambda g: Z(g, lambda k: k+1), 0.27)
lo, hi = mpf('0.545'), mpf('0.570')
print(f"gamma_min (ABCK) = {g_min}")
for name, g, w in [("DL/M", g_dlm, lambda k: 2), ("GM", g_gm, lambda k: k+1)]:
    gl = g/g_min; b = sqrt((gl-1)/(gl+1))
    print(f"{name}: gamma = {mp.nstr(g,12)}  Rest {mp.nstr(rest(g,w),3)}  gamma_L = {mp.nstr(gl,8)}  beta = {mp.nstr(b,8)}  eta = {mp.nstr(atanh(b),6)}  im Fenster: {lo<=b<=hi}")
print("A: |g_dlm - 0.237532957966| =", mp.nstr(abs(g_dlm-mpf('0.237532957966')),3), " gamma_L Ziel 1.86444")
