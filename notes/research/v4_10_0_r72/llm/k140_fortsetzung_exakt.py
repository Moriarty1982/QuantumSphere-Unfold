"""k140: wie k139, aber mit exakter Linearisierung (symmetrische Sonden x^(m e_nu), m = 4, 5: bis Grad m+2 exakt linear).
Fortsetzungssystem des theta-geeichten OP5-Systems am Keim; fuer Test H53.
Aufruf: python k139_fortsetzung.py <state-sufficiency-Ordner> <k136_eichdaten.npy egal> [laeufe]
Laeufe: ref (Grad 4 fest, N=5, reparierter Jet), pos (alter Grad-4-Jet, N=5), e7, e8 (Grad 5 fest)."""
import sys,time,math,numpy as np
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent));import k138_tps_d as T
Dir=sys.argv[1];runs=sys.argv[2].split(',') if len(sys.argv)>2 else ['ref','pos','e7','e8']
K2=T.Km[2];h=1e-3
def linearization(psi,p,dmax=2,check=False):
    """A[mu][gamma], B[gamma] (32x24 reell) bis Grad dmax, exakt: L = (R(Psi_b + d) - R(Psi_b - d))/2 mit d = x^(m e_nu) e_i,
    m = dmax+2 und dmax+3, Basis-Jet bis Grad dmax+1. Quadratische (gerade) Terme heben sich auf; kubische beginnen
    oberhalb von Grad m + dmax."""
    m1,m2=dmax+2,dmax+3;D=m2+dmax;bg=T.Background(p,D);nP=len(T.monos(D+1));I=T.index(D+1);IR=T.index(D);Id=T.index(dmax)
    P0=np.zeros((nP,12),complex);nb=len(T.monos(dmax+1));P0[:nb]=psi[:nb]
    nM=len(T.monos(dmax));B=np.zeros((4,nM,32,24));A=np.zeros((4,nM,32,24))
    sh=lambda gam,nu,k:tuple(x+(k if j==nu else 0) for j,x in enumerate(gam))
    for nu in range(4):
        L={}
        for m in (m1,m2):
            a=[0]*4;a[nu]=m;a=tuple(a)
            for i in range(24):
                e=np.zeros(12,complex);e[i%12]=1 if i<12 else 1j
                Pp=P0.copy();Pp[I[a]]+=e;Pm=P0.copy();Pm[I[a]]-=e;L[m,i]=(T.Rseries(Pp,bg)-T.Rseries(Pm,bg))/2
        for g,gam in enumerate(T.monos(dmax)):
            for i in range(24):
                if gam[nu]==0: A[nu,g,:,i]=L[m1,i][IR[sh(gam,nu,m1-1)]]/m1
                else:
                    dl=list(gam);dl[nu]-=1;dl=tuple(dl);A[nu,g,:,i]=L[m2,i][IR[sh(dl,nu,m2)]]-L[m1,i][IR[sh(dl,nu,m1)]]
                B[nu,g,:,i]=m2*L[m1,i][IR[sh(gam,nu,m1)]]-m1*L[m2,i][IR[sh(gam,nu,m2)]]
    if check: print('Streuung der vier B-Schaetzungen:',np.max(abs(B-B.mean(0))),' |B| max',np.max(abs(B)),flush=True)
    return A,B.mean(0)
_AB={}
def build(psi,p,Dfix,N,wv):
    dmax=N-Dfix-1
    if 'AB' not in _AB:  # haengt nur vom Jet bis Grad 4 ab (gleich fuer alle F-Laeufe); Grad <= 2 aus m = 4, 5 (genauer), Grad 3 aus m = 5, 6
        cache=Path(__file__).with_name('k140_AB3.npz')
        if cache.exists(): d=np.load(cache);A3,B3=d['A'],d['B']
        else: A3,B3=linearization(psi,p,3,check=True);np.savez(cache,A=A3,B=B3)
        c2=Path(__file__).with_name('k140_AB.npz')
        if c2.exists(): d2=np.load(c2);A2,B2=d2['A'],d2['B']
        else: A2,B2=linearization(psi,p,2,check=True);np.savez(c2,A=A2,B=B2)
        n2=len(T.monos(2));A3=A3.copy();B3=B3.copy();A3[:,:n2]=A2;B3[:n2]=B2;_AB['AB']=(A3,B3)
    nm=len(T.monos(max(dmax,0)));A,B=_AB['AB'][0][:,:nm],_AB['AB'][1][:nm];Id=T.index(max(dmax,0))
    cols=[a for a in T.monos(N) if Dfix<sum(a)<=N];rowsR=[b for b in T.monos(N-1) if Dfix<=sum(b)<=N-1];rowsG=cols
    ci={a:n for n,a in enumerate(cols)};E=np.zeros((32*len(rowsR)+len(rowsG),24*len(cols)))
    for r,bt in enumerate(rowsR):
        for c,al in enumerate(cols):
            blk=np.zeros((32,24));d=[x-y for x,y in zip(bt,al)]
            if all(v>=0 for v in d) and sum(d)<=dmax: blk+=B[Id[tuple(d)]]
            for mu in range(4):
                if al[mu]==0: continue
                g=list(d);g[mu]+=1
                if all(v>=0 for v in g) and sum(g)<=dmax: blk+=al[mu]*A[mu,Id[tuple(g)]]
            E[32*r:32*r+32,24*c:24*c+24]=blk
    off=32*len(rowsR)
    for r,bt in enumerate(rowsG):
        for c,al in enumerate(cols):
            d=tuple(x-y for x,y in zip(bt,al))
            if all(v>=0 for v in d) and sum(d)<=dmax: E[off+r,24*c:24*c+24]=wv[Id[d]]
    # rechte Seite
    bg=T.Background(p,N-1);P=np.zeros((len(T.monos(N)),12),complex);P[:len(T.monos(Dfix))]=psi[:len(T.monos(Dfix))]
    Rs=T.Rseries(P,bg);IR=T.index(N-1);rhs=np.r_[np.concatenate([Rs[IR[b]] for b in rowsR]),np.zeros(len(rowsG))]
    degc=np.repeat([sum(a) for a in cols],24)
    return E,rhs,degc
def wseries(psi,dmax):
    n=len(T.monos(dmax));g=np.einsum('ij,nj->ni',K2,psi[:n]);return np.concatenate([2*g.real,2*g.imag],axis=1)
def rank_gap(s):
    s=s/s[0];m=int(np.sum(s>1e-15));t=np.r_[s[:m],1e-17] if m==len(s) else s[:m+1]
    k=int(np.argmax(np.log(t[:-1]/t[1:])));return k+1,t[k],t[k+1]
def analyse(name,psi,p,Dfix,N):
    """Speichersparend: kappa als Abstand der rechten Seite zum Bild von E (lstsq, Schnitt in der Rang-Luecke); Projektionen ueber Rangvergleiche
    P_S = dim ker E - dim ker(E ohne Spalten von S), dafuer nur Singulaerwerte."""
    import gc,scipy.linalg as sl
    t0=time.time();E,rhs,degc=build(psi,p,Dfix,N,wseries(psi,max(N-Dfix-1,0)))
    cn=np.linalg.norm(E,axis=0);cn[cn==0]=1;E/=cn;rn=np.linalg.norm(E,axis=1);rn[rn==0]=1;E/=rn[:,None];rhs=rhs/rn
    n=E.shape[1]
    s=np.linalg.svd(E,compute_uv=False);r,a,b=rank_gap(s)
    x=np.linalg.lstsq(E,rhs,rcond=float(np.sqrt(a*b)))[0]   # Abschneiden in der Mitte der Luecke (relativ zu s[0])
    kap=np.linalg.norm(E@x-rhs)/np.linalg.norm(rhs);del x;gc.collect()
    null=n-r
    out=f'{name}: Groesse {E.shape}, Rang {r} (Luecke {a:.1e}|{b:.1e}, Verh. {a/b:.0e}), kappa = {kap:.2e}, |rhs| = {np.linalg.norm(rhs):.1e}, dim ker = {null}'
    print(out,flush=True)
    for top in range(Dfix+1,N):
        degs=list(range(Dfix+1,top+1));keep=~np.isin(degc,degs)
        s2=np.linalg.svd(E[:,keep],compute_uv=False);r2,a2,b2=rank_gap(s2);null2=int(keep.sum())-r2
        print(f'   Projektion auf Grade {degs}: {null-null2} (Rang ohne diese Spalten {r2}, Luecke {a2:.1e}|{b2:.1e}, Verh. {a2/b2:.0e})',flush=True)
    print(f'   [{time.time()-t0:.0f} s]',flush=True)
p,psi=T.load_germ(Dir,5);_,psi_old=T.load_germ(Dir,5,fourth='omega')
for rn in runs:
    if rn=='ref': analyse('Referenz (Grad 4 fest, N=5, reparierter Jet)',psi,p,4,5)
    if rn=='pos': analyse('Positivkontrolle (alter Grad-4-Jet, N=5)',psi_old,p,4,5)
    if rn=='e6': analyse('E6 (Grad 5 fest)',psi,p,5,6)
    if rn=='e7': analyse('E7 (Grad 5 fest)',psi,p,5,7)
    if rn=='e8': analyse('E8 (Grad 5 fest)',psi,p,5,8)
    if rn=='e7': pass
    # H53: nur der reparierte Jet bis Grad 4 fest, Grad 5 frei
    if rn=='f7': analyse('F7 (Grad 4 fest)',psi,p,4,7)
    if rn=='f8': analyse('F8 (Grad 4 fest)',psi,p,4,8)
