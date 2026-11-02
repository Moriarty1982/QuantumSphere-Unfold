"""k110: Woher kommt putative_H2=-1 bei Grad 5? Singulaervektoren der ein-/ausgehenden delta-Abbildung."""
import sys,numpy as np
from pathlib import Path
SRC=Path(sys.argv[1])
code=(SRC/'recursive_spencer_basis.py').read_text().split('results=[]')[0].replace("Path(__file__).resolve().parent",f"Path(r'{SRC}')")
g={'__file__':str(SRC/'recursive_spencer_basis.py')};exec(code,g)
delta=g['delta'];bases=g['bases']
p=5;A=delta(p+1,2);B=delta(p,3)
U,s,Vt=np.linalg.svd(A,full_matrices=False)
_,t,Wt=np.linalg.svd(B)
rb=int(sum(t>t[0]*1e-9));K=Wt[rb:].T   # Basis ker B
print('dim g5',bases[5].shape[1],'raum',A.shape[0],'rang aus',rb,'ker',K.shape[1],'t-Grenze',t[rb-2:rb+2])
print('B@A',np.linalg.norm(B@A),'|A|',s[0],'|B|',t[0])
for k in range(1534,1542):
  w=U[:,k];out=np.linalg.norm(B@w);inker=np.linalg.norm(K.T@w)
  print(f'k={k} sigma={s[k]:.3e}  |B w|={out:.3e}  Anteil in ker B={inker:.6f}  Abstand zu ker={np.sqrt(max(0,1-inker**2)):.3e}')
# Was bleibt im Kern uebrig, wenn das sichere Bild (sigma>1e-8) entfernt ist?
r8=int(sum(s>s[0]*1e-8));Im=U[:,:r8]
P=K-Im@(Im.T@K);u,sv,_=np.linalg.svd(P,full_matrices=False)
print('Kern minus sicheres Bild, Singulaerwerte:',sv[:4])
c=u[:,0];print('Restrichtung: Ueberlapp mit U[1537],U[1538]:',abs(U[:,r8]@c),abs(U[:,r8+1]@c))
# Konsistente Zaehlung: Bild erst auf ker B projizieren (erzwingt delta^2=0), dann zaehlen -> nie negativ
sk=np.linalg.svd(K.T@A,compute_uv=False)
print('projiziertes Bild, Grenze:',sk[1534:1540])
for cut in [1e-8,1e-9,1e-10,1e-11]:
  r=int(sum(sk>sk[0]*cut));print('cut',cut,'rang',r,'H2 =',K.shape[1]-r)
