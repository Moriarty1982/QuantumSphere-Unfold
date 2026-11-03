"""k160 (H60): Polarisationen je Nullrichtung in g''_p (p = 6..9). Basis wie k158; q aus k160_qmat.npy.
Aufruf: QS_DPS=70 QS_HPWORK=hp_work2 python k160_polarisationen.py"""
import sys,math,numpy as np
from pathlib import Path
here=Path(__file__).parent;sys.argv=[str(here/'k158_cartan_hp.py'),'8']
exec(open(here/'k158_cartan_hp.py').read().split('for seed in (1,2,3):')[0])
Q=np.load(here/'k160_qmat.npy');rng=np.random.default_rng(60)
def nullrichtungen(n):
    out=[]
    while len(out)<n:
        sp=rng.normal(size=3);a=Q[0,0];b=2*Q[0,1:]@sp;c=sp@Q[1:,1:]@sp;d=b*b-4*a*c
        if d<0: continue
        for t in ((-b+math.sqrt(d))/(2*a),(-b-math.sqrt(d))/(2*a)): x=np.r_[t,sp];out.append(x/np.linalg.norm(x))
    return out[:n]
def wave(x,p):
    v=np.array([math.prod(x[m]**a[m] for m in range(4))/math.sqrt(fac(a)) for a in mon(p)]);return np.kron(v[:,None],np.eye(24))
def pol(x,p):
    B=basis[p];W=wave(x,p);R=W-B@(B.T@W);s=np.linalg.svd(R,compute_uv=False);s=s/np.linalg.norm(W,2)
    sm=np.sort(s);k=int(np.argmax(np.log(np.maximum(sm[1:],1e-300)/np.maximum(sm[:-1],1e-300))))+1   # Zahl der kleinen Werte
    return k,sm[k]/max(sm[k-1],1e-300),sm[0]
dirs=nullrichtungen(200);aus=[d/np.linalg.norm(d) for d in rng.normal(size=(50,4))]
for p in range(6,10):
    ks=[pol(x,p) for x in dirs];ko=[pol(x,p) for x in aus]
    kk=[k for k,_,_ in ks];gg=[g for _,g,_ in ks];ok=sum(g>=1e5 for g in gg)/len(gg)
    smin_aus=min(s for _,_,s in ko)
    print(f'p={p}: Kegel Median {int(np.median(kk))} Werte {sorted(set(kk))} Haeuf. {[kk.count(v) for v in sorted(set(kk))]}, Luecke>=1e5: {ok:.0%}, '
          f'kleinste Luecke {min(gg):.0e}; ausserhalb: kleinster Singulaerwert {smin_aus:.1e}',flush=True)
