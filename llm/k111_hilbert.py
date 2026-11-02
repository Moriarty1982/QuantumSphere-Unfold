"""k111: Hilbert-Funktion des Omega-erweiterten Symbols direkt, Grad 2..8.
Idee: H^{5,2} = dim g_7 - 722 (Euler-Charakteristik + H^{6,1}=0 fuer Prolongationen, Ausgangsrang 1024).
Also entscheidet die Dimension von g_7, ob bei Grad 5 eine neue Bedingung steckt."""
import sys,numpy as np
from pathlib import Path
SRC=Path(sys.argv[1])
g={'__file__':str(SRC/'balanced_spencer_check.py')}
exec((SRC/'balanced_spencer_check.py').read_text().split('def run_variant')[0].replace("Path(__file__).resolve().parent",f"Path(r'{SRC}')"),g)
matrix,idx=g['matrix'],g['idx']
pred=lambda p:127+81*(p-2)+19*(p-2)*(p-3)//2
for p in range(2,9):
    X=matrix(p)[1];X=X/np.maximum(np.linalg.norm(X,axis=1),1e-300)[:,None]
    s=np.linalg.svd(X,compute_uv=False);n=X.shape[1]
    dims={c:n-int(sum(s>s[0]*c)) for c in (1e-6,1e-8,1e-9,1e-10,1e-11,1e-12)}
    r=n-pred(p)  # Rang, den die quadratische Hilbert-Funktion verlangt
    print(f'p={p} Spalten {n} Zeilen {X.shape[0]} | erwartet dim {pred(p)} | dims je Schwelle {dims}')
    print(f'      Singulaerwerte um die erwartete Grenze r={r}:',np.array2string(s[r-4:r+4],precision=3))
