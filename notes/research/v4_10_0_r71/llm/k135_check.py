import sys,time,numpy as np
from pathlib import Path
from k135_tps import *
D=Path(sys.argv[1]);p0,psi4=load_germ(D);t0=time.time();bg=Background(p0);print('Hintergrund',round(time.time()-t0,1),'s')
t0=time.time();Rc=Rseries(psi4,bg);print('Auswertung',round(time.time()-t0,2),'s')
for d in range(4):
    idx=[i for i,a in enumerate(M3) if sum(a)==d];print('Grad',d,'max|R-Koeff| =',f'{np.max(abs(Rc[idx])):.2e}')
# Vergleich Grad 0 mit punktweisem R aus k127
exec(open('k127_symbol_frei.py').read().split("f70=json.loads")[0].replace("D=Path(sys.argv[1]);w=np.load(D/'completion-omega-witness.npz')","w=None"))
jv=np.concatenate([np.r_[psi4[I4[tuple(int(m==mu) for m in range(4))]].real,psi4[I4[tuple(int(m==mu) for m in range(4))]].imag] for mu in range(4)])
print('Abgleich Grad 0 mit k127-Auswerter:',np.max(abs(R(jv,psi4[0],p0)[0]-Rc[0])))
