"""k120: Punkte von V(d_1..d_4) per Gauss-Newton (komplex), Gruppierung in 2-Ebenen, Lage zum Kegel q."""
import numpy as np
d=np.load('kofaktoren.npy');Q=np.load('quadrik.npy')
import itertools
g2=list(itertools.combinations_with_replacement(range(4),2))
def mat(c):
    M=np.zeros((4,4))
    for i,a in enumerate(g2):
        if a[0]==a[1]: M[a[0],a[0]]+=c[i]
        else: M[a[0],a[1]]+=c[i]/2;M[a[1],a[0]]+=c[i]/2
    return M
Ms=[mat(c)/np.linalg.norm(mat(c)) for c in d]
rng=np.random.default_rng(4);pts=[]
for _ in range(60):
    v=rng.normal(size=4)+1j*rng.normal(size=4);v/=np.linalg.norm(v)
    for it in range(80):
        F=np.array([v@M@v for M in Ms]+[v.conj()@v-1]);Jm=np.array([2*M@v for M in Ms]+[v.conj()])
        dv=np.linalg.lstsq(Jm,-F,rcond=None)[0];v=v+dv
        if np.linalg.norm(dv)<1e-15: break
    v/=np.linalg.norm(v)
    if max(abs(v@M@v) for M in Ms)<1e-12: pts.append(v)
print('Punkte auf V:',len(pts))
groups=[]
for v in pts:
    for gr in groups:
        if np.linalg.svd(np.array(gr[:2]+[v]).T,compute_uv=False)[2]<1e-8: gr.append(v);break
    else:
        # neue Gruppe nur, wenn v mit einem bisherigen Einzelpunkt keine Ebene in V bildet
        placed=False
        for gr in groups:
            if len(gr)==1:
                w=gr[0]+0.613*v
                if max(abs(w@M@w) for M in Ms)<1e-10: gr.append(v);placed=True;break
        if not placed: groups.append([v])
print('Gruppen:',[len(g) for g in groups])
planes=[]
for gr in groups:
    if len(gr)<2: continue
    u,s,_=np.linalg.svd(np.array(gr).T);P=u[:,:2];planes.append(P)
    print(f'Ebene: Dim-Test {np.array2string(s[:3],precision=1)} | im Kegel? |PtQP|={np.linalg.norm(P.T@Q@P)/np.linalg.norm(Q):.1e} | reell? Rang[P,conjP]={np.linalg.matrix_rank(np.hstack([P,P.conj()]),1e-8)}')
if len(planes)>=2:
    P0,P1=planes[:2]
    print('Ebene1 = conj(Ebene0)? Rang[P0,conj P1] =',np.linalg.matrix_rank(np.hstack([P0,P1.conj()]),1e-8),'| windschief? Rang[P0,P1] =',np.linalg.matrix_rank(np.hstack([P0,P1]),1e-8))
    # Kegel-Familien: alpha/beta (Selbst-/Antiselbstdual) - Schnitt zweier Ebenen derselben Familie ist gerade-dimensional
    np.save('ebenen.npy',np.array([P0,P1]))
