"""k161 (H61): Spin, Chiralitaet und komplexe Struktur des Polarisationsraums P(xi) in g''_8.
Aufruf: QS_DPS=70 QS_HPWORK=hp_work2 python k161_spin.py   (braucht k160_qmat.npy, k161_V.npy)"""
import sys,math,numpy as np
from pathlib import Path
here=Path(__file__).parent;sys.argv=[str(here/'k158_cartan_hp.py'),'7']
exec(open(here/'k158_cartan_hp.py').read().split('for seed in (1,2,3):')[0])
V=np.load(here/'k161_V.npy');Q=V@np.diag([1,-1,-1,-1.])@V.T;rng=np.random.default_rng(61)
sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1,-1]);Z2=np.zeros((2,2));I2=np.eye(2)
real=lambda M:np.block([[M.real,-M.imag],[M.imag,M.real]])
Sig=[real(np.kron(np.eye(3),np.block([[s,Z2],[Z2,s]]))) for s in (sx,sy,sz)]
G5=real(np.kron(np.eye(3),np.block([[Z2,I2],[I2,Z2]])));Jm=real(1j*np.eye(12))
def nullrichtungen(n):
    out=[]
    while len(out)<n:
        sp=rng.normal(size=3);a=Q[0,0];b=2*Q[0,1:]@sp;c=sp@Q[1:,1:]@sp;d=b*b-4*a*c
        if d<0: continue
        for t in ((-b+math.sqrt(d))/(2*a),(-b-math.sqrt(d))/(2*a)): x=np.r_[t,sp];out.append(x/np.linalg.norm(x))
    return out[:n]
def wave(x,p):
    v=np.array([math.prod(x[m]**a[m] for m in range(4))/math.sqrt(fac(a)) for a in mon(p)]);return np.kron(v[:,None],np.eye(24))
p=8;B=basis[p];res={'J':[],'g5':[],'h':[]};ev5=[];evh=[];dims=[]
for x in nullrichtungen(200):
    W=wave(x,p);R=W-B@(B.T@W);_,s,Vt=np.linalg.svd(R);P=Vt[-6:].T;dims.append(int(np.sum(s/s[0]<1e-6)))   # 24x6, orthonormal
    xh=V.T@x;xh=xh*np.sign(xh[0]);k=-xh[1:];n=k/np.linalg.norm(k);H=0.5*sum(n[i]*Sig[i] for i in range(3))
    for key,X in (('J',Jm),('g5',G5),('h',H)): Y=X@P;res[key].append(np.linalg.norm(Y-P@(P.T@Y),2))
    ev5.append(np.sort(np.linalg.eigvalsh(P.T@G5@P)));evh.append(np.sort(np.linalg.eigvalsh(P.T@H@P)))
med=lambda v:float(np.median(v))
print('Polarisationen je Richtung (Kontrolle):',sorted(set(dims)))
for key in res: print(f'r_{key}: Median {med(res[key]):.1e}, max {max(res[key]):.1e}')
print('Eigenwerte gamma5 auf P (Median je Stelle):',np.array2string(np.median(ev5,axis=0),precision=3))
print('Eigenwerte h auf P (Median je Stelle):',np.array2string(np.median(evh,axis=0),precision=3))
print('Streuung h-Eigenwerte (max |dev|):',f"{np.max(np.abs(np.array(evh)-np.median(evh,axis=0))):.1e}",' gamma5:',f"{np.max(np.abs(np.array(ev5)-np.median(ev5,axis=0))):.1e}")
