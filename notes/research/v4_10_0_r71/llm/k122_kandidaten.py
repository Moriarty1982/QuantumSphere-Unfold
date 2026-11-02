import json,sys,itertools,numpy as np
from pathlib import Path
exec(open('k121_rahmen.py').read().split("print('det E")[0].replace("D=Path(sys.argv[1])","D=Path(sys.argv[1])"))
Pl=np.load('ebenen.npy');eta=np.diag([1.,-1,-1,-1])
planes_f=[np.linalg.qr(V.T@np.linalg.svd(np.hstack([Pl[k].real,Pl[k].imag]))[0][:,:2])[0] for k in range(2)]  # Kovektor-Ebenen im Rahmen
sx_=np.array([[0,1],[1,0]]);Z2=np.zeros((2,2));gamma=[beta]+[beta@a for a in al];g5=np.block([[Z2,np.eye(2)],[np.eye(2),Z2]])
P3=psi.reshape(3,4);W={}
for n in range(3):
    u=P3[n];ub=u.conj()@beta
    W[f'j{n}']=np.array([np.real(ub@gamma[a]@u) for a in range(4)]);W[f's{n}']=np.array([np.real(ub@gamma[a]@g5@u) for a in range(4)])
    # Tensor-Bilinear (Spin-Ebene): Re/Im von u^T C gamma u (Majorana-artig) -> zwei weitere Vektoren
    C=1j*gamma[2]@gamma[0]
    m=np.array([u@ (C@gamma[a]) @ u for a in range(4)]);W[f'mR{n}']=m.real;W[f'mI{n}']=m.imag
for a in range(4): W[f'e{a}']=np.eye(4)[a]
for n in range(3): W[f'j{n}+s{n}']=W[f'j{n}']+W[f's{n}'];W[f'j{n}-s{n}']=W[f'j{n}']-W[f's{n}']
# Mischungen ueber Farben (Matrix S3 koppelt Farbe 0 und 1)
print({k:np.round(v,3) for k,v in W.items() if k.startswith(('mR','mI'))})
def angle(A,B):
    A=np.linalg.qr(A)[0];B=np.linalg.qr(B)[0];c=np.linalg.svd(A.T@B,compute_uv=False);return np.degrees(np.arccos(np.clip(c.min(),0,1)))
res=[]
for (n1,v1),(n2,v2) in itertools.combinations([(k,v) for k,v in W.items() if np.linalg.norm(v)>1e-6],2):
    M=np.column_stack([v1,v2])
    if np.linalg.matrix_rank(M,1e-6*np.linalg.norm(M))<2: continue
    cov=eta@M   # Vektoren -> Kovektoren
    for k in range(2):
        res.append((angle(cov,planes_f[k]),f'Ebene {k} = span({n1},{n2}) (gesenkt)'))
        ann=np.linalg.svd(planes_f[k].T)[2][2:].T   # Annihilator als Vektor-Ebene
        res.append((angle(M,ann),f'Querrichtungen {k} = span({n1},{n2})'))
res.sort();[print(f'{a:7.3f} Grad  {s}') for a,s in res[:12]]
