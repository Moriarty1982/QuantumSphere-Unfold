"""k151 (Methodenpruefung): Woher kommt der kleinste echte Singulaerwert (~1e-8) des Symbols? Skalierung der 32 Zeilen
und 24 Spalten von J, Zeilengruppen F/G/dg, und das prolongierte Symbol bei p = 4, 6."""
import sys,math,numpy as np
from pathlib import Path
here=Path(__file__).parent;D=Path(sys.argv[1])
d2=np.load(here/'k142_lin2.npz');J=np.hstack([d2['A'][m,0] for m in range(4)])
g={'__file__':str(D/'balanced_spencer_check.py')}
exec((D/'balanced_spencer_check.py').read_text().split('def run_variant')[0].replace("Path(__file__).resolve().parent",f"Path(r'{D}')"),g)
idx=g['idx'];g['theta']=np.zeros(480)
print('Zeilennormen J (F 24, G 4, dg 4):',np.array2string(np.linalg.norm(J,axis=1),precision=1))
print('Spaltennormen J je Komponente (24, ueber mu gemittelt):',np.array2string(np.linalg.norm(J.reshape(32,4,24),axis=(0,1)),precision=1))
def symb_sv(Jm,p):
    g['J']=Jm;X=g['matrix'](p)[1];X=X[np.linalg.norm(X,axis=1)>0];X=X/np.linalg.norm(X,axis=1)[:,None];s=np.linalg.svd(X,compute_uv=False);s=s/s[0]
    r=int(np.argmax(np.log(s[:-1]/np.maximum(s[1:],1e-300))*(s[1:]>0)))+1;return r,s[r-3:r+2]
def ruiz(Jm,it=30):
    Jm=Jm.copy();R=np.ones(32);C=np.ones(24)
    for _ in range(it):
        r=np.sqrt(np.linalg.norm(Jm,axis=1));Jm/=r[:,None];R/=r
        c=np.sqrt(np.linalg.norm(Jm.reshape(32,4,24),axis=(0,1)));Jm=(Jm.reshape(32,4,24)/c[None,None,:]).reshape(32,96);C/=c
    return Jm,R,C
for lab,Jm in [('roh',J),('Ruiz (Zeilen + Komponenten)',ruiz(J)[0])]:
    for p in (4,6):
        r,v=symb_sv(Jm,p);print(f'{lab:28s} p={p}: Rang {r}; Werte um den Rang {np.array2string(v,precision=2)}')
# Welche Richtungen tragen den kleinen Wert? (p=4, roh): rechter Singulaervektor nach Komponenten
g['J']=J;X=g['matrix'](4)[1];X=X[np.linalg.norm(X,axis=1)>0];X=X/np.linalg.norm(X,axis=1)[:,None];U,s,Vt=np.linalg.svd(X);s=s/s[0]
r=int(np.argmax(np.log(s[:-1]/np.maximum(s[1:],1e-300))*(s[1:]>0)))+1;v=Vt[r-1].reshape(-1,24)
print('kleinster echter Wert p=4:',f'{s[r-1]:.1e}','; Gewicht je Komponente:',np.array2string(np.linalg.norm(v,axis=0),precision=2))
u=U[:,r-1];print('Gewicht der Zeilen nach Gruppe F/G/dg:',[f'{np.linalg.norm(u.reshape(-1,32)[:,a:b]):.2f}' for a,b in ((0,24),(24,28),(28,32))])
