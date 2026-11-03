"""k144 (Erkundung): die vier versteckten Bedingungen an 6-Jets ausdruecklich bestimmen.
Aufruf: python k144_vier_bedingungen.py <Ordner> <punkt 1|2> <schritt: k7 | k8 | w>
K7 = Projektion von ker F7 auf (c5, c6), K8 = dasselbe fuer F8 (fester 4-Jet). Bedingungen = K7 ∩ K8^⊥ (ausgeglichene
Koordinaten b_alpha = c_alpha * sqrt(alpha!)). Projektion ohne volle SVD: ker((I - QQ^T) E_56), Q = Bild von E_78."""
import sys,gc,math,time,numpy as np
from pathlib import Path
here=Path(__file__).parent;Dir=sys.argv[1];pt=sys.argv[2];step=sys.argv[3];sys.argv=[sys.argv[0],Dir,'none']
__file__=str(here/'k140_fortsetzung_exakt.py');src=open(__file__).read().split('p,psi=T.load_germ')[0]
src=src.replace("    return A,B.mean(0)\n","    return A,B\n",1);exec(src)
p,psi0=T.load_germ(Dir,5);t0=time.time();W=here/f'k144_p{pt}';W.mkdir(exist_ok=True)
psi=psi0 if pt=='1' else np.load(here/'h55_work'/'psi.npy');lin3=here/('k142_lin3.npz' if pt=='1' else 'k143_lin3.npz')
d2=np.load(here/'k142_lin2.npz');d3=np.load(lin3);n2=len(T.monos(2))
A=d3['A'].copy();B=d3['B'].mean(0);A[:,:n2]=d2['A'];B[:n2]=d2['B'].mean(0);_AB['AB']=(A,B)
def proj_basis(N):
    E,rhs,degc=build(psi,p,4,N,wseries(psi,N-5));cols=[a for a in T.monos(N) if 4<sum(a)<=N]
    cn=np.linalg.norm(E,axis=0);cn[cn==0]=1;E/=cn;rn=np.linalg.norm(E,axis=1);rn[rn==0]=1;E/=rn[:,None]
    s56=np.isin(degc,[5,6]);E56=E[:,s56];E78=np.ascontiguousarray(E[:,~s56]);del E;gc.collect()
    U,s,_=np.linalg.svd(E78,full_matrices=False);r,a,b=rank_gap(s);Q=U[:,:r];del U,E78;gc.collect()
    M=E56-Q@(Q.T@E56);_,sm,Vt=np.linalg.svd(M,full_matrices=True);rm,am,bm=rank_gap(sm);K=Vt[rm:].T
    sf=np.repeat([math.sqrt(math.prod(math.factorial(k) for k in a)) for a in cols if sum(a) in (5,6)],24)
    K=K/cn[s56][:,None]*sf[:,None];K,_=np.linalg.qr(K)
    print(f'F{N}: Rang E78 {r} (Verh. {a/b:.0e}); dim Projektion = {K.shape[1]} (Rang M {rm}, Verh. {am/bm:.0e})',flush=True);return K
if step in ('k7','k8'):
    np.save(W/f'{step}.npy',proj_basis(7 if step=='k7' else 8))
else:
    K7=np.load(W/'k7.npy');K8=np.load(W/'k8.npy')
    print('K8 in K7? Rest',f'{np.linalg.norm(K8-K7@(K7.T@K8)):.1e}')
    C=K7.T@K8;U,s,_=np.linalg.svd(C,full_matrices=True);print('Winkel-Cosinusse (kleinste 6):',np.array2string(s[-6:],precision=3))
    Wc=U[:,K8.shape[1]:];w=K7@Wc;np.save(W/'w.npy',w)   # vier Bedingungs-Richtungen (ausgeglichene Koordinaten)
    n5=len([a for a in T.monos(5) if sum(a)==5])*24
    print('Anteil auf c6 je Bedingung:',np.array2string(np.linalg.norm(w[n5:],axis=0),precision=3))
    # Symbolteil: Faser {c5 = 0} in K7 (= g'_6) und Rang der Bedingungen darauf
    sel=np.zeros(K7.shape[0],bool);sel[:n5]=True;_,s5,Vt5=np.linalg.svd(K7[sel],full_matrices=True);r5,_,_=rank_gap(s5)
    G6=K7@Vt5[r5:].T;sg=np.linalg.svd(w.T@G6,compute_uv=False)
    print(f'Faser c5=0 in K7: dim {G6.shape[1]}; Singulaerwerte der Bedingungen darauf: {np.array2string(sg,precision=3)}')
    np.save(W/'G6.npy',G6)
print(f'   [{step}: {time.time()-t0:.0f} s]',flush=True)
