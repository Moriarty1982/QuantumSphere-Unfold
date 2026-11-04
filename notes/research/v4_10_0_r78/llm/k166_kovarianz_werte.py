"""k166 (H66): Verfahren von k165b (C aus Werten, 80 Bestimmung / 20 Pruefung), Saat 66, fuenf Paare (M,S) und Negativkontrolle.
Aufruf: python k166_kovarianz_werte.py <Keim-Ordner> <k127_symbol_frei.py> <k164_kovarianz.py>"""
import sys,numpy as np
from pathlib import Path
D,P127,P164=sys.argv[1:4];src=open(Path(__file__).parent/'k165_kovarianz_rest.py').read().split("blocks=(")[0];exec(src)
rng=np.random.default_rng(66);blocks=(('F',slice(0,24)),('G',slice(24,28)),('dg',slice(28,32)))
fmt=lambda d:'  '.join(f'{k} {v:.1e}' for k,v in d.items())
def run(M,S4,label,tbg=True):
    R1=[];R2=[]
    for i in range(100):
        psi=rng.normal(size=12)+1j*rng.normal(size=12);jv=rng.normal(size=96);bg=rand_bg()
        p2,j2,bg2,_=tf(M,S4,psi,jv,bg)
        if not tbg: bg2=(bg[0],bg[1],bg[2],bg[3])
        R1.append(Rb(jv,psi,bg));R2.append(Rb(j2,p2,bg2))
    R1=np.array(R1).T;R2=np.array(R2).T;C=R2[:,:80]@np.linalg.pinv(R1[:,:80],rcond=1e-12)
    out={n:max(np.linalg.norm(R2[r,k]-(C@R1[:,k])[r])/np.linalg.norm(R2[r,k]) for k in range(80,100)) for n,r in blocks}
    off=np.linalg.norm(C[:24,24:])+np.linalg.norm(C[24:28,np.r_[0:24,28:32]])+np.linalg.norm(C[28:,:28])
    print(f'{label:28s}',fmt(out),f'| Mischung {off:.1e}',flush=True);return out
I=np.eye(4);run(I,I,'Kontrolle positiv')
Mg=I+0.3*rng.normal(size=(4,4));Sg=spinor(0.6*rng.normal(size=6))
run(Mg,Sg,'Kontrolle negativ',tbg=False)
run(I,spinor(np.r_[0.8*rng.normal(size=3),0,0,0]),'reine Drehung')
run(I,spinor(np.r_[0,0,0,0.6*rng.normal(size=3)]),'reiner Boost')
run(I+0.3*rng.normal(size=(4,4)),I,'reine Koordinatenaenderung')
run(Mg,Sg,'gemischt 1')
run(I+0.3*rng.normal(size=(4,4)),spinor(0.6*rng.normal(size=6)),'gemischt 2')
