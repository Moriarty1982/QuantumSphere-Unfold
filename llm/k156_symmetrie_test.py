"""k156 (Erkundung): Kommen die Fast-Identitaeten von der Fast-Symmetrie Psi ~ D Psi* (D = diag(1, i, i, 1) je Block)?
Linkskern des prolongierten Symbols (nur J, Ordnung 4) an drei Arten von Punkten (abseits der Loesung, am Keimort):
generisch (zufaelliges Psi, dPsi), symmetrisch (Psi, dPsi exakt im C-Sektor), Keim. Aufruf: python k156_symmetrie_test.py <Ordner>"""
import sys,numpy as np
from pathlib import Path
D=Path(sys.argv[1]);src=(Path(__file__).parent/'k127_symbol_frei.py')
exec(src.read_text().split("J0=symbol(j0,psi0,p0)")[0])   # R, symbol, Daten (k127)
g={'__file__':str(D/'balanced_spencer_check.py')}
exec((D/'balanced_spencer_check.py').read_text().split('def run_variant')[0].replace("Path(__file__).resolve().parent",f"Path(r'{D}')"),g)
g['theta']=np.zeros(480)
def leftnull(J,p=4):
    g['J']=J;X=g['matrix'](p)[1];s=np.linalg.svd(X,compute_uv=False);s=s/s[0];m=int(np.sum(s>1e-14));t=np.r_[s[:m],1e-17] if m==len(s) else s[:m+1]
    r=int(np.argmax(np.log(t[:-1]/t[1:])))+1;return X.shape[0]-r,r,t[r-1],t[r]
dvec=np.array([1,1j,1j,1]*3)
rng=np.random.default_rng(11)
def sym(v): return dvec*v.real            # exakt im C-Sektor: Komponenten reell bzw. rein imaginaer nach Muster
print('Keim: |Psi - D Re(D* Psi)| / |Psi| =',f'{np.linalg.norm(psi0-dvec*(np.conj(dvec)*psi0).real)/np.linalg.norm(psi0):.1e}')
for lab in ('Keim','generisch','generisch','symmetrisch','symmetrisch','Keim symmetrisiert'):
    if lab=='Keim': psi,jv=psi0,j0
    elif lab=='generisch': psi=rng.normal(size=12)+1j*rng.normal(size=12);jv=rng.normal(size=96)
    elif lab=='symmetrisch':
        psi=sym(rng.normal(size=12));jj=[sym(rng.normal(size=12)) for m in range(4)];jv=np.concatenate([np.r_[x.real,x.imag] for x in jj])
    else:
        psi=dvec*(np.conj(dvec)*psi0).real;jj=[j0[m*24:m*24+12]+1j*j0[m*24+12:m*24+24] for m in range(4)]
        jv=np.concatenate([np.r_[(dvec*(np.conj(dvec)*x).real).real,(dvec*(np.conj(dvec)*x).real).imag] for x in jj])
    J=symbol(jv,psi,p0);k,r,a,b=leftnull(J)
    print(f'{lab:20s}: Rang Symbol Ordnung 4 = {r}, Linkskern {k}  (Luecke {a:.1e}|{b:.1e})',flush=True)
