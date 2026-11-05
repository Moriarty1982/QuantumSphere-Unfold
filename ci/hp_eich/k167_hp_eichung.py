"""k167 (H67): wie k159 mit waehlbarer Eichung (QS_EICHUNG) und Polarisationen im Faserraum.
k159 (H59): Faser der q-Jets hochgenau. Verallgemeinert k157 (q = 6) auf beliebiges q.
Fester Jet bis Grad q-1, Gleichungen bis Grad q+1. Elimination c_{q+2}, dann c_{q+1} (Linkskerne: float-SVD, Newton in arb).
Auf dem Kern N_q von [R_{q-1}; G_q] Gram der abgeleiteten Bedingungen; F_q = dim N_q - Rang.
Aufruf: python k159_hp_faser.py <Keim-Ordner> <q> <out.json>   (Umgebung: QS_DPS, QS_HPWORK, QS_THREADS)"""
import sys,os,time,json,math,numpy as np,flint
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent));from k154_hp_tools import *
flint.ctx.threads=int(os.environ.get('QS_THREADS','1'))
t0=time.time();D=sys.argv[1];q=int(sys.argv[2]);OUT=Path(sys.argv[3]);res={'q':q,'dps':flint.ctx.dps,'stufen':[]}
log=lambda *a:print(f'[{time.time()-t0:6.0f} s]',*a,flush=True)
mons,A,B=load();w=gauge_series(D)
Af={k:tofloat(v) for k,v in A.items()};Bf={k:tofloat(v) for k,v in B.items()};wf={k:tofloat(v) for k,v in w.items()}

def build(kind,k,m,dmax=2):
    """Block als (arb_mat, float-Array) oder None; gleiche Ordnung und Skalierung wie Rblock/Gblock in k154."""
    if kind=='R':
        if m>k+1 or k+1-m>dmax: return None
        nr,nc=32,24
    else:
        if m>k or k-m>dmax: return None
        nr,nc=1,24
    rows,cols=mon(k),mon(m);M=arb_mat(nr*len(rows),nc*len(cols));F=np.zeros((nr*len(rows),nc*len(cols)))
    for r,bt in enumerate(rows):
        for c,al in enumerate(cols):
            d=[x-y for x,y in zip(bt,al)];blk=None;bf=None
            if kind=='R':
                if all(v>=0 for v in d) and sum(d)<=dmax: blk,bf=B[tuple(d)],Bf[tuple(d)]
                for mu in range(4):
                    if al[mu]==0: continue
                    g=list(d);g[mu]+=1
                    if all(v>=0 for v in g) and sum(g)<=dmax:
                        t=A[(mu,tuple(g))]*al[mu];tf=Af[(mu,tuple(g))]*al[mu]
                        blk,bf=(t,tf) if blk is None else (blk+t,bf+tf)
            else:
                if all(v>=0 for v in d) and sum(d)<=dmax: blk,bf=w[tuple(d)],wf[tuple(d)]
            if blk is None: continue
            sc=1/arb(fac(al)).sqrt();scf=1/math.sqrt(fac(al))
            for i in range(nr):
                for j in range(nc): M[nr*r+i,nc*c+j]=blk[i,j]*sc
            F[nr*r:nr*r+nr,nc*c:nc*c+nc]=bf*scf
    return M,F

def gap_rank(t):
    m=int(np.sum(t>1e-15));tt=np.r_[t[:m],1e-17] if m==len(t) else t[:m+1]
    return int(np.argmax(np.log(tt[:-1]/tt[1:])))+1

def rows_of(L,a,b): return arb_mat([[L[i,j] for j in range(L.ncols())] for i in range(a,b)])

def leftnull(blocks):
    """blocks: Liste (arb_mat, float). Linkskern von vstack: float-SVD, Newton mit Residuum X^T T in arb."""
    Tf=np.vstack([F for _,F in blocks]);rs=np.linalg.norm(Tf,axis=1);rs[rs==0]=1;Tf=Tf/rs[:,None]
    U,s,Vt=np.linalg.svd(Tf.T,full_matrices=True);t=s/s[0];r=gap_rank(t)
    X=Vt[r:].T/rs[:,None];Ur,Sr,Vr=U[:,:r],s[:r],Vt[:r].T;del U,Vt,Tf
    Xa=arb_mat(X.tolist());offs=np.cumsum([0]+[M.nrows() for M,_ in blocks]);hist=[]
    for it in range(10):
        Res=None
        for (M,_),a,b in zip(blocks,offs[:-1],offs[1:]):
            P=rows_of(Xa,a,b).transpose()*M;Res=P if Res is None else Res+P
        rf=tofloat(Res).T;nr=float(np.max(abs(rf))/s[0]);hist.append(nr)
        if nr<1e-62: break
        Xa=Xa-arb_mat(((Vr@((Ur.T@rf)/Sr[:,None]))/rs[:,None]).tolist())
    return Xa,r,(float(t[r-1]),float(t[r]) if r<len(t) else 0.0),hist,offs

def apply_left(L,offs,blocks):
    """L^T vstack(blocks) blockweise; None-Bloecke sind Null. Rueckgabe (arb_mat, float)."""
    out=None
    for blk,a,b in zip(blocks,offs[:-1],offs[1:]):
        if blk is None: continue
        P=rows_of(L,a,b).transpose()*blk[0];out=P if out is None else out+P
    return out,tofloat(out)

def stufe(name,r,g,h,L):
    e={'stufe':name,'rang':r,'luecke':g,'verhaeltnis':g[0]/g[1] if g[1] else None,'linkskern':L.ncols(),'residuen':h}
    res['stufen'].append(e);log(f'{name}: Rang {r} (Luecke {g[0]:.1e}|{g[1]:.1e}), Linkskern {L.ncols()}, Residuen {[f"{x:.0e}" for x in h]}')

# --- Stufe 1: c_{q+2}
top=[build('R',q+1,q+2),build('G',q+2,q+2)];log('Bloecke c%d gebaut'%(q+2),top[0][0].nrows(),top[0][0].ncols())
L1,r1,g1,h1,o1=leftnull(top);stufe(f'c{q+2}',r1,g1,h1,L1);del top
D11=apply_left(L1,o1,[build('R',q+1,q+1),build('G',q+2,q+1)])
D10=apply_left(L1,o1,[build('R',q+1,q),build('G',q+2,q)]);del L1;log('abgeleitete Zeilen',D11[0].nrows())
# --- Stufe 2: c_{q+1}
mid=[build('R',q,q+1),build('G',q+1,q+1),D11]
L2,r2,g2,h2,o2=leftnull(mid);stufe(f'c{q+1}',r2,g2,h2,L2);del mid,D11
Dq,_=apply_left(L2,o2,[build('R',q,q),build('G',q+1,q),D10]);del L2,D10;log('abgeleitete Zeilen auf c%d'%q,Dq.nrows())
# --- Stufe 3: Faser c_q
bl=[build('R',q-1,q),build('G',q,q)];Tf=np.vstack([F for _,F in bl]);U,s,Vt=np.linalg.svd(Tf,full_matrices=True);t=s/s[0];r=gap_rank(t)
N=Vt[r:].T;Ur,Sr,Vr=U[:,:r],s[:r],Vt[:r].T;Na=arb_mat(N.tolist());hN=[]
for it in range(8):
    rf=np.vstack([tofloat(M*Na) for M,_ in bl]);nr=float(np.max(abs(rf))/s[0]);hN.append(nr)
    if nr<1e-62: break
    Na=Na-arb_mat((Vr@((Ur.T@rf)/Sr[:,None])).tolist())
res['dim_N']=Na.ncols();res['residuen_N']=hN;log(f'Kern N_{q}: dim {Na.ncols()} (Residuen {[f"{x:.0e}" for x in hN]})')
C=Dq*Na;cn=np.linalg.norm(tofloat(Dq),axis=1);cn[cn==0]=1
C=arb_mat([[C[i,j]/cn[i] for j in range(C.ncols())] for i in range(C.nrows())]);Gm=C.transpose()*C
ev=np.array([abs(float(v.real.mid())) for v in flint.acb_mat(Gm).eig(algorithm='approx')]);ev=np.sort(ev)[::-1];ev=ev/ev[0]
lg=np.log10(np.maximum(ev,1e-300));j=int(np.argmax(lg[:-1]-lg[1:]));rank=j+1
res.update(rang_C=rank,luecke_gram=[float(ev[j]),float(ev[j+1])],verhaeltnis_gram=float(ev[j]/max(ev[j+1],1e-300)),
           F=Na.ncols()-rank,gram_um_luecke=[float(x) for x in ev[max(0,j-6):j+7]],sekunden=time.time()-t0)
log(f'Gram: Rang {rank}, Luecke {ev[j]:.1e}|{ev[j+1]:.1e}; F_{q} = {Na.ncols()} - {rank} = {Na.ncols()-rank}')
print(np.array2string(ev[max(0,j-6):j+7],precision=1),flush=True)
OUT.write_text(json.dumps(res,indent=1));log('geschrieben',OUT)

# --- H67: Polarisationen im Faserraum (float)
import math as _m
Cf=tofloat(C);_,sc,Vc=np.linalg.svd(Cf);Kf=Vc[rank:].T;Nf=tofloat(Na);Bf=np.linalg.qr(Nf@Kf)[0]
Qm=np.load(Path(__file__).parent/'k160_qmat.npy');rg=np.random.default_rng(67)
def nullr():
    while True:
        sp=rg.normal(size=3);a=Qm[0,0];b=2*Qm[0,1:]@sp;c=sp@Qm[1:,1:]@sp;d=b*b-4*a*c
        if d>=0: x=np.r_[(-b+_m.sqrt(d))/(2*a),sp];return x/np.linalg.norm(x)
def wave(x):
    v=np.array([_m.prod(x[m]**al[m] for m in range(4))/_m.sqrt(fac(al)) for al in mon(q)]);return np.kron(v[:,None],np.eye(24))
def pol(x):
    W=wave(x);R_=W-Bf@(Bf.T@W);s=np.sort(np.linalg.svd(R_,compute_uv=False)/np.linalg.norm(W,2))
    k=int(np.argmax(np.log(np.maximum(s[1:],1e-300)/np.maximum(s[:-1],1e-300))))+1;return k,s[k]/max(s[k-1],1e-300),s[0]
pk=[pol(nullr()) for _ in range(100)];po=[pol((lambda v:v/np.linalg.norm(v))(rg.normal(size=4))) for _ in range(30)]
kk=[a for a,_,_ in pk];res['polarisationen_kegel']=sorted(set(kk));res['polarisationen_median']=int(np.median(kk))
res['pol_luecke_min']=float(min(g for _,g,_ in pk));res['ausserhalb_kleinster_sw']=float(min(s for _,_,s in po))
res['eichung']=os.environ.get('QS_EICHUNG','K2')
log(f"Eichung {res['eichung']}: Polarisationen auf dem Kegel {res['polarisationen_kegel']} (Median {res['polarisationen_median']}, kleinste Luecke {res['pol_luecke_min']:.0e}); ausserhalb kleinster Singulaerwert {res['ausserhalb_kleinster_sw']:.1e}")
OUT.write_text(json.dumps(res,indent=1));log('geschrieben',OUT)
