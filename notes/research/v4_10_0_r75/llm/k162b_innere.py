"""k162b (Erkundung nach H62): Struktur der inneren Symmetrie-Algebra (A = 0) von g''_8 aus k162_G8.npy."""
import numpy as np
from pathlib import Path
here=Path(__file__).parent;G=np.load(here/'k162_G8.npy')
GB=G[16:,16:];w,U=np.linalg.eigh(GB);w=np.abs(w)/np.abs(w).max();o=np.argsort(w);w,U=w[o],U[:,o]
lg=np.log10(np.maximum(w,1e-300));j=int(np.argmax(lg[1:]-lg[:-1]))+1;print('innere Algebra: dim',j,f'(Luecke {w[j-1]:.0e}|{w[j]:.0e})')
Bs=[U[:,k].reshape(24,24) for k in range(j)];Bm=np.array([b.ravel() for b in Bs]).T   # 576 x j, orthonormal
coef=lambda X:Bm.T@X.ravel()
C=np.zeros((j,j,j));cl=0
for a in range(j):
    for b in range(j):
        X=Bs[a]@Bs[b]-Bs[b]@Bs[a];c=coef(X);C[a,b]=c;cl=max(cl,np.linalg.norm(X.ravel()-Bm@c))
print(f'Abgeschlossenheit unter Kommutator: Rest {cl:.1e}')
ad=np.transpose(C,(0,2,1))            # ad(a)[c,b]
K=np.einsum('acb,dbc->ad',ad,ad);ev=np.linalg.eigvalsh((K+K.T)/2);ev=ev/np.abs(ev).max()
print('Killing-Form: positiv',int(np.sum(ev>1e-8)),' negativ',int(np.sum(ev<-1e-8)),' null',int(np.sum(abs(ev)<=1e-8)))
D=np.array([C[a,b] for a in range(j) for b in range(j)]);sd=np.linalg.svd(D,compute_uv=False);print('Dimension der abgeleiteten Algebra [s,s]:',int(np.sum(sd/sd[0]>1e-8)))
Z=np.vstack([ad[a] for a in range(j)]) if False else np.vstack([C[:,b,:].T for b in range(j)]);sz=np.linalg.svd(np.vstack([C[a] for a in range(j)]).reshape(j*j,j) if False else np.concatenate([C[:,b,:] for b in range(j)],axis=0),compute_uv=False)
# Zentrum: z mit [z,b]=0 fuer alle b  <=> sum_a z_a C[a,b,:] = 0
Mz=np.concatenate([C[:,b,:].T for b in range(j)],axis=0);s=np.linalg.svd(Mz,compute_uv=False);print('Dimension des Zentrums:',int(np.sum(s/s[0]<1e-8))+max(0,j-len(s)))
# Wirkung auf C^24: Eigenwerte eines generischen Elements
x=sum(np.random.default_rng(1).normal()*b for b in Bs);print('Eigenwerte eines generischen Elements (Betraege der Imaginaerteile, gerundet):',np.round(np.sort(np.abs(np.linalg.eigvals(x).imag)),2)[::2])
print('Realteile (gerundet):',np.round(np.sort(np.linalg.eigvals(x).real),2))
