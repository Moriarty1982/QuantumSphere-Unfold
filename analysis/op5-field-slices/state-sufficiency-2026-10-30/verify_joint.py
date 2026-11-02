from pathlib import Path
import json,numpy as np
p=Path(__file__).resolve().parent
ns={'__file__':str(p/'joint_fit.py')};exec((p/'joint_fit.py').read_text().split('rows=[];start=')[0],ns)
d=json.loads((p/'joint-fit-result.json').read_text());checks=[]
Z=np.kron(np.diag([1,-1,0]),np.array(ns['ns']['beta'],complex))
for row,old in zip(d['results'],ns['data']['results']):
 pos=np.array(row['point']);psi=np.array([complex(*v) for v in old['field_values_real_imag']]);v=np.array(row['first_jets_packed']);j=(v[:48]+1j*v[48:]).reshape(4,12)
 bg=np.asarray(ns['bgfun'](*pos),complex).ravel();db=np.asarray(ns['bgjac'](*pos),complex)
 q=np.vdot(psi,Z@psi).real;g=4-bg[0].real*q/2
 dg=-db[0].real*q/2-bg[0].real*np.real(np.einsum('i,ij,mj->m',psi.conj(),Z,j))
 checks.append({'point':row['point'],'g':float(g),'dg':dg.tolist(),'dg_norm':float(np.linalg.norm(dg))})
 print({k:row[k] for k in ['point','initial_prolongation_norm','F_norm','AD_prolongation_norm','E0_fix_norm','detE','g00','first_jet_change','second_jet_norm']});print(checks[-1])
(p/'joint-fit-scalar-controls.json').write_text(json.dumps(checks,indent=2))
assert max(abs(c['g']) for c in checks)<1e-10
assert max(c['dg_norm'] for c in checks)<1e-9
