from pathlib import Path
import json,numpy as np
exec(Path('OP5_Full_Time_Symbol_Check.py').read_text().split('out=[]')[0])
gg,hh,spin=old['back'](*p);cov=jets.copy()
for mu in range(1,4):cov[mu]+=1j*np.kron(np.asarray(gg)*np.asarray(spin).ravel()[mu-1],np.eye(4))@psi
base=old['residual'](p,psi,jets);checks=[]
for mu in range(4):
 changed=jets.copy();changed[0]+=.1*cov[mu];err=float(np.linalg.norm(old['residual'](p,psi,changed)-base));assert err<1e-8;checks.append({'direction':mu,'finite_change_residual_difference':err})
Path(__file__).with_suffix('.json').write_text(json.dumps({'checks':checks,'scope':'Pointwise coframe/derivative shear invariance; no regional gauge invariance claimed'},indent=2));print(checks)
