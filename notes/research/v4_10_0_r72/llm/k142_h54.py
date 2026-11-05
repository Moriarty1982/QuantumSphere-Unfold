"""k142: Test H54 (Vorab-Notiz Commit ec705ec). Aufruf: python k142_h54.py <Ordner> <schritt>
Schritte: lin3 | lin2 (Linearisierung mit vier Einzelschaetzungen B^(nu)) | eta | rang0 | rang1 (volles F8 mit Variante)."""
import sys,gc,time,numpy as np
from pathlib import Path
here=Path(__file__).parent;Dir=sys.argv[1];step=sys.argv[2];sys.argv=[sys.argv[0],Dir,'none']
__file__=str(here/'k140_fortsetzung_exakt.py');src=open(__file__).read().split('p,psi=T.load_germ')[0]
src=src.replace("    return A,B.mean(0)\n","    return A,B\n",1)  # hier: alle vier Schaetzungen zurueckgeben
exec(src);p,psi=T.load_germ(Dir,5);W=here/'f8_work';t0=time.time()
def AB(variant=None):
    d3=np.load(here/'k142_lin3.npz');d2=np.load(here/'k142_lin2.npz');n2=len(T.monos(2));n1=len(T.monos(1))
    A=d3['A'].copy();B=d3['B'].mean(0);A[:,:n2]=d2['A'];B[:n2]=d2['B'].mean(0)
    if variant is not None:
        kind,nu=variant
        if kind=='g3': B[n2:]=d3['B'][nu][n2:]
        if kind=='g1': B[:n1]=d2['B'][nu][:n1]
        if kind=='a3':  # Ersatz: A vom Grad 3 um die gemessene Streuung B^(nu) - Mittel (Grad 3) verschieben, fuer jedes mu
            A[:,n2:]+=(d3['B'][nu][n2:]-d3['B'].mean(0)[n2:])[None]
    return A,B
def E_raw(variant=None):
    _AB['AB']=AB(variant);E,rhs,degc=build(psi,p,4,8,wseries(psi,3));return E,degc
def worst(kind,dmax_lo,dmax_hi,key):
    d=np.load(here/key)['B'];dev=[np.max(abs(d[nu][dmax_lo:dmax_hi]-d.mean(0)[dmax_lo:dmax_hi])) for nu in range(4)]
    return list(np.argsort(dev)[::-1][:2]),dev
def norm2(M,it=60):
    v=np.random.default_rng(0).normal(size=M.shape[1]);v/=np.linalg.norm(v)
    for _ in range(it): w=M.T@(M@v);lam=np.linalg.norm(w);v=w/lam
    return float(np.sqrt(lam))
if step in('lin3','lin2'):
    dm=3 if step=='lin3' else 2;A,B=linearization(psi,p,dm,check=True);np.savez(here/f'k142_{step}.npz',A=A,B=B)
    print(step,'gespeichert, B-Schaetzungen',B.shape)
elif step=='eta':
    n2=len(T.monos(2));n1=len(T.monos(1));nM3=len(T.monos(3))
    v3,dev3=worst('g3',n2,nM3,'k142_lin3.npz');v1,dev1=worst('g1',0,n1,'k142_lin2.npz')
    print('Abweichungen B^(nu) Grad 3:',[f'{x:.1e}' for x in dev3],' -> Varianten',v3,'| Grad <= 1:',[f'{x:.1e}' for x in dev1],' -> Varianten',v1)
    E0,degc=E_raw();cn=np.linalg.norm(E0,axis=0);cn[cn==0]=1;rn=np.linalg.norm(E0/cn,axis=1);rn[rn==0]=1
    s0=np.load(W/'s.npy')[0];sr0=np.load(W/'s_ohne56.npy')[0];keep=~np.isin(degc,[5,6])
    for nu in v3:
        E1,_=E_raw(('g3',nu));dE=(E1-E0)/cn/rn[:,None];print(f'  eta (Grad 3, nu={nu}) = {norm2(dE)/s0:.2e};  auf c7,c8-Spalten: {norm2(dE[:,keep])/sr0:.2e}',flush=True);del E1,dE;gc.collect()
    for nu in v1:
        E1,_=E_raw(('g1',nu));dE=((E1-E0)/cn/rn[:,None])[:,keep];print(f'  eta_red (Grad <= 1, nu={nu}) = {norm2(dE)/sr0:.2e}',flush=True);del E1,dE;gc.collect()
elif step=='eta3':
    n2=len(T.monos(2));nM3=len(T.monos(3));v3,_=worst('g3',n2,nM3,'k142_lin3.npz')
    E0,degc=E_raw();cn=np.linalg.norm(E0,axis=0);cn[cn==0]=1;rn=np.linalg.norm(E0/cn,axis=1);rn[rn==0]=1;s0=np.load(W/'s.npy')[0]
    for nu in v3:
        E1,_=E_raw(('a3',nu));dE=(E1-E0)/cn/rn[:,None];print(f'  eta (A Grad 3 + Streuung nu={nu}) = {norm2(dE)/s0:.2e}',flush=True);del E1,dE;gc.collect()
elif step.startswith('rang'):
    n2=len(T.monos(2));nM3=len(T.monos(3));v3,_=worst('g3',n2,nM3,'k142_lin3.npz');nu=v3[int(step[-1])]
    E,degc=E_raw(('a3',nu));cn=np.linalg.norm(E,axis=0);cn[cn==0]=1;E/=cn;rn=np.linalg.norm(E,axis=1);rn[rn==0]=1;E/=rn[:,None]
    s=np.linalg.svd(E,compute_uv=False);r,a,b=rank_gap(s);s=s/s[0]
    print(f'Variante A Grad 3 + Streuung nu={nu}: Rang {r} (Luecke {a:.1e}|{b:.1e}, Verh. {a/b:.0e}); Werte um 7957: {np.array2string(s[7953:7961],precision=2)}')
print(f'   [{step}: {time.time()-t0:.0f} s]',flush=True)
