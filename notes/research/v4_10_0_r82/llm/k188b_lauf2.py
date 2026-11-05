"""k188b: Lauf 2 zu H74 (nach dem Lauf 1, offen als zweiter Lauf). Laufzeit an die erwartete Rate angepasst (T ~ 2 ln(1e4)/rate), dt = 0.02.
Vergleich der gemessenen Rate mit der exakten Rate Im(Omega) aus den Eigenwerten von M."""
import numpy as np, json, importlib.util, io, contextlib
spec=importlib.util.spec_from_file_location('k','k188_test_h74.py');src=open('k188_test_h74.py').read().split('out={}')[0];g={}
exec(src,g);run=g['run']
def exact_rate(w1s,w2s,eps):
    M=np.array([[w1s,-eps],[eps,w2s]]);ev=np.linalg.eigvals(M);return float(max(abs(np.sqrt(complex(e)).imag) for e in ev))
out={}
for (lab,w2s,eps) in (('a gleich',1,1e-3),('a gleich',1,1e-2),('b verstimmt',1.1,0.06)):
    r=exact_rate(1,w2s,eps);T=2*np.log(1e4)/r
    res=run(1,w2s,eps,True,T=T,dt=0.02);res.update(exakte_rate=r,T=T);out[f'{lab} eps={eps}']=res
    print(f"{lab} eps={eps}: T={T:.0f} wachstum={res['wachstum']:.3g} rate={res['rate']:.4g} exakt={r:.4g}")
json.dump(out,open('k188b_out.json','w'),indent=1,default=float)
