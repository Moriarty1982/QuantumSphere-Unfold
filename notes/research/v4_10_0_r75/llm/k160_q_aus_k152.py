"""k160 (Hilfsschritt): Lichtkegel-Matrix Q am Keim aus dem Koframe-Teil von k152 (q(xi) = xi^T Q xi).
Aufruf: python k160_q_aus_k152.py <Keim-Ordner>   (k152_wellen.py, k148_konsistent.py im selben Ordner)"""
import sys,os,numpy as np
from pathlib import Path
here=Path(__file__).resolve().parent;sys.path.insert(0,str(here));sys.argv=[str(here/'k152_wellen.py'),sys.argv[1],'pruef']
os.chdir(here);__file__=str(here/'k152_wellen.py')
exec(open(here/'k152_wellen.py').read().split('def wavevec')[0])
Q=V@np.diag([1,-1,-1,-1.])@V.T;np.save(here/'k160_qmat.npy',Q);print('Q',np.array2string(Q,precision=4))
