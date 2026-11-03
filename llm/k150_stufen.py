"""k150: stufenweise Elimination des linearisierten Fortsetzungssystems (homogen, fester Jet bis Grad Dfix).
Eliminiert c_N, c_{N-1}, ... nacheinander ueber Linkskerne der jeweiligen Spaltenbloecke; uebrig bleibt ein System auf
den niedrigen Graden, dessen Kern die Projektion ist. Nur Matrizen in Symbolgroesse.
Aufruf: python k150_stufen.py <Ordner> <Dfix> <N> <bis> [variante]   (Projektion auf Grade Dfix+1 .. bis)
variante: '' | a3_0 | a3_1 (A vom Grad 3 um die gemessene B-Streuung verschoben, wie k142)"""
import sys,math,time,numpy as np
from pathlib import Path
here=Path(__file__).parent;sys.path.insert(0,str(here));import k138_tps_d as T
Dir=sys.argv[1];Dfix,N,bis=int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]);var=sys.argv[5] if len(sys.argv)>5 else ''
p,psi=T.load_germ(Dir,5);t0=time.time()
d2=np.load(here/'k142_lin2.npz');d3=np.load(here/'k142_lin3.npz');n2=len(T.monos(2))
A=d3['A'].copy();B=d3['B'].mean(0);A[:,:n2]=d2['A'];B[:n2]=d2['B'].mean(0)
if var.startswith('a3'):
    dev=[np.max(abs(d3['B'][nu][n2:]-d3['B'].mean(0)[n2:])) for nu in range(4)];nu=list(np.argsort(dev)[::-1])[int(var[-1])]
    A[:,n2:]+=(d3['B'][nu][n2:]-d3['B'].mean(0)[n2:])[None]
dmax=3;Id=T.index(dmax);K2=T.Km[2]
w=np.einsum('ij,nj->ni',K2,psi[:len(T.monos(dmax))]);wser=np.concatenate([2*w.real,2*w.imag],axis=1)   # Eichzeilen-Reihe
mon=lambda d:[a for a in T.monos(d) if sum(a)==d];fac=lambda a:math.prod(math.factorial(k) for k in a)
sq={d:np.repeat([1/math.sqrt(fac(a)) for a in mon(d)],24) for d in range(Dfix+1,N+1)}   # c = b/sqrt(alpha!)
def Rblock(k,m):
    if m>k+1 or k+1-m>dmax: return None
    rows,cols=mon(k),mon(m);M=np.zeros((32*len(rows),24*len(cols)))
    for r,bt in enumerate(rows):
        for c,al in enumerate(cols):
            d=[x-y for x,y in zip(bt,al)];blk=np.zeros((32,24))
            if all(v>=0 for v in d) and sum(d)<=dmax: blk+=B[Id[tuple(d)]]
            for mu in range(4):
                if al[mu]==0: continue
                g=list(d);g[mu]+=1
                if all(v>=0 for v in g) and sum(g)<=dmax: blk+=al[mu]*A[mu,Id[tuple(g)]]
            M[32*r:32*r+32,24*c:24*c+24]=blk
    return M*sq[m][None,:]
def Gblock(k,m):
    if m>k or k-m>dmax: return None
    rows,cols=mon(k),mon(m);M=np.zeros((len(rows),24*len(cols)))
    for r,bt in enumerate(rows):
        for c,al in enumerate(cols):
            d=tuple(x-y for x,y in zip(bt,al))
            if all(v>=0 for v in d) and sum(d)<=dmax: M[r,24*c:24*c+24]=wser[Id[d]]
    return M*sq[m][None,:]
def rank_gap(s,floor=1e-15):
    if len(s)==0 or s[0]==0: return 0,np.inf,1.0
    s=s/s[0];m=int(np.sum(s>floor));t=np.r_[s[:m],1e-17] if m==len(s) else s[:m+1]
    k=int(np.argmax(np.log(t[:-1]/t[1:])));return k+1,t[k],t[k+1]
def normrows(rows):   # rows: dict m -> Matrix (gleiche Zeilenzahl); Zeilen auf Norm 1
    nr=np.sqrt(sum(np.sum(M**2,axis=1) for M in rows.values()));nr[nr==0]=1;return {m:M/nr[:,None] for m,M in rows.items()}
# Zeilengruppen: jede als dict {Grad: Block}
groups=[]
for k in range(Dfix,N):
    g={m:Rblock(k,m) for m in range(Dfix+1,N+1)};g={m:M for m,M in g.items() if M is not None};groups.append(normrows(g))
for k in range(Dfix+1,N+1):
    g={m:Gblock(k,m) for m in range(Dfix+1,N+1)};g={m:M for m,M in g.items() if M is not None};groups.append(normrows(g))
log=[]
for m in range(N,bis,-1):   # c_m eliminieren
    inv=[g for g in groups if m in g];rest=[g for g in groups if m not in g]
    Tm=np.vstack([g[m] for g in inv]);U,s,_=np.linalg.svd(Tm,full_matrices=True);r,a,b=rank_gap(s);L=U[:,r:]
    lower=sorted({k for g in inv for k in g if k!=m});new={}
    for k in lower:
        Mk=np.vstack([g.get(k,np.zeros((next(iter(g.values())).shape[0],24*len(mon(k))))) for g in inv]);new[k]=L.T@Mk
    log.append(f'c{m} eliminiert: Block {Tm.shape}, Rang {r} (Luecke {a:.1e}|{b:.1e}, Verh. {a/b:.0e}); abgeleitete Zeilen {L.shape[1]}')
    groups=rest+([normrows(new)] if L.shape[1] and new else [])
    print(log[-1],flush=True)
degs=list(range(Dfix+1,bis+1));X=np.vstack([np.hstack([g.get(k,np.zeros((next(iter(g.values())).shape[0],24*len(mon(k))))) for k in degs]) for g in groups])
s=np.linalg.svd(X,compute_uv=False);r,a,b=rank_gap(s);t=s/s[0]
print(f'Ergebnis Dfix={Dfix} N={N} {var or "Standard"}: Projektion auf Grade {degs}: dim {X.shape[1]-r} (Rang {r}, Luecke {a:.1e}|{b:.1e}, Verh. {a/b:.0e}); Werte um den Rang {np.array2string(t[max(r-3,0):r+3],precision=2)}  [{time.time()-t0:.0f} s]',flush=True)
