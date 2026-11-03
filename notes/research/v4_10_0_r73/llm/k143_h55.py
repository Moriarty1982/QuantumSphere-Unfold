"""k143: Test H55 (Vorab-Notiz Commit 04a3950): zweiter Grundpunkt. Aufruf: python k143_h55.py <Ordner> <schritt>
Schritte: punkt | ref | pos | f7 | lin3 | f8bau | f8svd | f8proj | f8lstsq | eta"""
import sys,gc,time,numpy as np
from pathlib import Path
here=Path(__file__).parent;Dir=sys.argv[1];step=sys.argv[2];sys.argv=[sys.argv[0],Dir,'none']
__file__=str(here/'k140_fortsetzung_exakt.py');src=open(__file__).read().split('p,psi=T.load_germ')[0]
src=src.replace("    return A,B.mean(0)\n","    return A,B\n",1);exec(src)
p,psi0=T.load_germ(Dir,5);W=here/'h55_work';W.mkdir(exist_ok=True);t0=time.time();n2=len(T.monos(2));n1=len(T.monos(1))
d2=np.load(here/'k142_lin2.npz')   # A, B bis Grad 2: haengen nur vom Jet bis Grad 3 ab (gleich wie am ersten Punkt)
def setAB(variant=None):
    A=np.zeros((4,len(T.monos(3)),32,24));B=np.zeros((len(T.monos(3)),32,24))
    if (here/'k143_lin3.npz').exists(): d3=np.load(here/'k143_lin3.npz');A[:]=d3['A'];B[:]=d3['B'].mean(0)
    A[:,:n2]=d2['A'];B[:n2]=d2['B'].mean(0)
    if variant:
        kind,nu=variant;d3=np.load(here/'k143_lin3.npz')
        if kind=='a3': A[:,n2:]+=(d3['B'][nu][n2:]-d3['B'].mean(0)[n2:])[None]
        if kind=='g1': B[:n1]=d2['B'][nu][:n1]
    _AB['AB']=(A,B)
def psi_new():
    return np.load(W/'psi.npy')
def normed(E,rhs):
    cn=np.linalg.norm(E,axis=0);cn[cn==0]=1;E/=cn;rn=np.linalg.norm(E,axis=1);rn[rn==0]=1;E/=rn[:,None];return E,rhs/rn,cn,rn
def kappa_rank(E,rhs):
    s=np.linalg.svd(E,compute_uv=False);r,a,b=rank_gap(s);x=np.linalg.lstsq(E,rhs,rcond=float(np.sqrt(a*b)))[0]
    return r,a,b,np.linalg.norm(E@x-rhs)/np.linalg.norm(rhs),s
if step=='punkt':
    setAB();E,rhs,degc=build(psi0,p,3,5,wseries(psi0,1));E,rhs,cn,rn=normed(E,rhs)
    _,s,Vt=np.linalg.svd(E,full_matrices=True);r,a,b=rank_gap(s);N=Vt[r:].T
    z=N@np.random.default_rng(55).normal(size=N.shape[1]);z=z/cn
    cols=[al for al in T.monos(5) if 3<sum(al)<=5];I=T.index(5);psi=psi0.copy();z4={}
    for c,al in enumerate(cols):
        if sum(al)==4: z4[al]=z[24*c:24*c+12]+1j*z[24*c+12:24*c+24]
    c4=np.array([psi0[I[al]] for al in z4]);dz=np.array(list(z4.values()));alpha=0.5*np.linalg.norm(c4)/np.linalg.norm(dz)
    for al,v in z4.items(): psi[I[al]]=psi0[I[al]]+alpha*v
    psi[T.deg(5)==5]=0;np.save(W/'psi.npy',psi)
    print(f'F3_5: {E.shape}, Rang {r} (Verh. {a/b:.0e}), Kern {N.shape[1]}; alpha = {alpha:.3e}; |c4 neu - c4 rep|/|c4 rep| = {np.linalg.norm(alpha*dz)/np.linalg.norm(c4):.2f}')
elif step in ('ref','pos'):
    setAB();psi=psi_new()
    if step=='pos':
        rng=np.random.default_rng(56);m=T.deg(5)==4;q=rng.normal(size=(m.sum(),12))+1j*rng.normal(size=(m.sum(),12))
        psi=psi.copy();psi[m]+=1e-3*np.linalg.norm(psi[m])/np.linalg.norm(q)*q
    E,rhs,degc=build(psi,p,4,5,wseries(psi,0));E,rhs,_,_=normed(E,rhs);r,a,b,k,_=kappa_rank(E,rhs)
    print(f'{step}: {E.shape}, Rang {r} (Luecke {a:.1e}|{b:.1e}, Verh. {a/b:.0e}), kappa = {k:.2e}')
elif step=='f7':
    setAB();psi=psi_new();E,rhs,degc=build(psi,p,4,7,wseries(psi,2));E,rhs,_,_=normed(E,rhs);r,a,b,k,_=kappa_rank(E,rhs)
    keep=~np.isin(degc,[5,6]);s2=np.linalg.svd(E[:,keep],compute_uv=False);r2,a2,b2=rank_gap(s2)
    print(f'F7: {E.shape}, Rang {r} (Luecke {a:.1e}|{b:.1e}, Verh. {a/b:.0e}), kappa = {k:.2e}; ohne c5,c6: Rang {r2} (Luecke {a2:.1e}|{b2:.1e}, Verh. {a2/b2:.0e}); P56 = {(E.shape[1]-r)-(int(keep.sum())-r2)}')
elif step=='lin3':
    A,B=linearization(psi_new(),p,3,check=True);np.savez(here/'k143_lin3.npz',A=A,B=B);print('lin3 gespeichert')
elif step=='f8bau':
    setAB();psi=psi_new();E,rhs,degc=build(psi,p,4,8,wseries(psi,3));E,rhs,cn,rn=normed(E,rhs)
    np.save(W/'E.npy',E);np.save(W/'rhs.npy',rhs);np.save(W/'degc.npy',degc);np.save(W/'cn.npy',cn);np.save(W/'rn.npy',rn);print('F8 gebaut',E.shape)
elif step=='f8svd':
    E=np.load(W/'E.npy');s=np.linalg.svd(E,compute_uv=False);np.save(W/'s.npy',s);r,a,b=rank_gap(s);t=s/s[0]
    print(f'F8: Rang {r} (Luecke {a:.1e}|{b:.1e}, Verh. {a/b:.0e}); Werte um den Rang: {np.array2string(t[r-4:r+3],precision=2)}')
elif step=='f8proj':
    degc=np.load(W/'degc.npy');keep=~np.isin(degc,[5,6]);E=np.load(W/'E.npy',mmap_mode='r');X=np.ascontiguousarray(E[:,keep]);del E
    s2=np.linalg.svd(X,compute_uv=False);np.save(W/'s_ohne56.npy',s2);r2,a2,b2=rank_gap(s2);t=s2/s2[0];r,_,_=rank_gap(np.load(W/'s.npy'))
    print(f'F8 ohne c5,c6: Rang {r2} (Luecke {a2:.1e}|{b2:.1e}, Verh. {a2/b2:.0e}); Werte: {np.array2string(t[r2-4:r2+3],precision=2)}; P56 = {(len(degc)-r)-(int(keep.sum())-r2)}')
elif step=='f8lstsq':
    E=np.load(W/'E.npy');rhs=np.load(W/'rhs.npy');r,a,b=rank_gap(np.load(W/'s.npy'))
    x=np.linalg.lstsq(E,rhs,rcond=float(np.sqrt(a*b)))[0];print(f'F8: kappa = {np.linalg.norm(E@x-rhs)/np.linalg.norm(rhs):.2e}')
elif step=='eta':
    psi=psi_new();d3=np.load(here/'k143_lin3.npz');dev3=[np.max(abs(d3['B'][nu][n2:]-d3['B'].mean(0)[n2:])) for nu in range(4)];v3=list(np.argsort(dev3)[::-1][:2])
    dev1=[np.max(abs(d2['B'][nu][:n1]-d2['B'].mean(0)[:n1])) for nu in range(4)];v1=list(np.argsort(dev1)[::-1][:2])
    def Eraw(var=None): setAB(var);return build(psi,p,4,8,wseries(psi,3))[0]
    cn=np.load(W/'cn.npy');rn=np.load(W/'rn.npy');s0=np.load(W/'s.npy')[0];sr0=np.load(W/'s_ohne56.npy')[0];keep=~np.isin(np.load(W/'degc.npy'),[5,6])
    def norm2(M,it=60):
        v=np.random.default_rng(0).normal(size=M.shape[1]);v/=np.linalg.norm(v)
        for _ in range(it): w=M.T@(M@v);lam=np.linalg.norm(w);v=w/max(lam,1e-300)
        return float(np.sqrt(lam))
    E0=Eraw()
    for nu in v3: dE=(Eraw(('a3',nu))-E0)/cn/rn[:,None];print(f'  eta (A Grad 3 + Streuung nu={nu}) = {norm2(dE)/s0:.2e}',flush=True)
    for nu in v1: dE=((Eraw(('g1',nu))-E0)/cn/rn[:,None])[:,keep];print(f'  eta_red (Grad <= 1, nu={nu}) = {norm2(dE)/sr0:.2e}',flush=True)
print(f'   [{step}: {time.time()-t0:.0f} s]',flush=True)
