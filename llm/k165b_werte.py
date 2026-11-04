"""k165b (H65, Lauf 2): Zeilentransformation C aus Werten (80 Datensaetze, fuer festes (M,S)), Pruefung an 20 weiteren.
Aufruf wie k165_kovarianz_rest.py."""
import sys,numpy as np
D,P127,P164=sys.argv[1:4];here=__file__;src=open(here.replace('k165b_werte.py','k165_kovarianz_rest.py')).read().split("blocks=(")[0];exec(src)
fmt=lambda d:'  '.join(f'{k} {v:.1e}' for k,v in d.items())
blocks=(('F',slice(0,24)),('G',slice(24,28)),('dg',slice(28,32)))
def run(M,S4,label):
    R1=[];R2=[]
    for i in range(100):
        psi=rng.normal(size=12)+1j*rng.normal(size=12);jv=rng.normal(size=96);bg=rand_bg()
        p2,j2,bg2,_=tf(M,S4,psi,jv,bg);R1.append(Rb(jv,psi,bg));R2.append(Rb(j2,p2,bg2))
    R1=np.array(R1).T;R2=np.array(R2).T;C=R2[:,:80]@np.linalg.pinv(R1[:,:80],rcond=1e-12)
    out={n:max(np.linalg.norm(R2[r,k]-(C@R1[:,k])[r])/np.linalg.norm(R2[r,k]) for k in range(80,100)) for n,r in blocks}
    off=np.linalg.norm(C[:24,24:])+np.linalg.norm(C[24:28,np.r_[0:24,28:32]])+np.linalg.norm(C[28:,:28])
    print(f'{label}:',fmt(out),f'| Mischung zwischen Bloecken {off:.1e}',flush=True)
run(np.eye(4),np.eye(4),'Kontrolle positiv')
for t in range(2):
    run(np.eye(4)+0.3*rng.normal(size=(4,4)),spinor(0.6*rng.normal(size=6)),f'(M,S) Paar {t}')
