"""F8 aus k140 in Einzelschritten mit Zwischenspeicherung (Speicher < 8 GB). Aufruf: python k140_f8_schritte.py <Ordner> <schritt>
schritt: bauen | svd | lstsq | proj5 | proj56 | proj567"""
import sys,gc,time,numpy as np
from pathlib import Path
here=Path(__file__).parent;sys.argv=[sys.argv[0],sys.argv[1],'none',sys.argv[2]];step=sys.argv[3]
__file__=str(here/'k140_fortsetzung_exakt.py');exec(open(__file__).read().split('p,psi=T.load_germ')[0])
p,psi=T.load_germ(sys.argv[1],5);W=here/'f8_work';W.mkdir(exist_ok=True);t0=time.time()
if step=='bauen':
    E,rhs,degc=build(psi,p,4,8,wseries(psi,3))
    cn=np.linalg.norm(E,axis=0);cn[cn==0]=1;E/=cn;rn=np.linalg.norm(E,axis=1);rn[rn==0]=1;E/=rn[:,None];rhs=rhs/rn
    np.save(W/'E.npy',E);np.save(W/'rhs.npy',rhs);np.save(W/'degc.npy',degc);print('gebaut',E.shape)
elif step=='svd':
    E=np.load(W/'E.npy');s=np.linalg.svd(E,compute_uv=False);np.save(W/'s.npy',s);r,a,b=rank_gap(s)
    print(f'F8: Groesse {E.shape}, Rang {r} (Luecke {a:.1e}|{b:.1e}, Verh. {a/b:.0e}), dim ker = {E.shape[1]-r}')
elif step=='lstsq':
    E=np.load(W/'E.npy');rhs=np.load(W/'rhs.npy');r,a,b=rank_gap(np.load(W/'s.npy'))
    x=np.linalg.lstsq(E,rhs,rcond=float(np.sqrt(a*b)))[0];print(f'F8: kappa = {np.linalg.norm(E@x-rhs)/np.linalg.norm(rhs):.2e}, |rhs| = {np.linalg.norm(rhs):.1e}')
else:
    degs={'proj5':[5],'proj56':[5,6],'proj567':[5,6,7]}[step];degc=np.load(W/'degc.npy');keep=~np.isin(degc,degs)
    E=np.load(W/'E.npy',mmap_mode='r');X=np.ascontiguousarray(E[:,keep]);del E;gc.collect()
    r,a,b=rank_gap(np.load(W/'s.npy'));null=len(degc)-r
    s2=np.linalg.svd(X,compute_uv=False);r2,a2,b2=rank_gap(s2)
    print(f'   F8 Projektion auf Grade {degs}: {null-(int(keep.sum())-r2)} (Rang ohne diese Spalten {r2}, Luecke {a2:.1e}|{b2:.1e}, Verh. {a2/b2:.0e})')
print(f'   [{step}: {time.time()-t0:.0f} s]',flush=True)
