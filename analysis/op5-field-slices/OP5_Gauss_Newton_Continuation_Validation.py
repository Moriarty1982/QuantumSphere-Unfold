from pathlib import Path
import json,numpy as np,torch as T
ns={};exec(Path('OP5_Field_Residual_Diagnosis.py').read_text().split('\nbefore=')[0],ns)
saved=json.loads(Path('OP5_Gauss_Newton_Continuation_Check.json').read_text());ns['params'].data.copy_(T.tensor(saved['coefficients_real_imag']));rng=np.random.default_rng(291036);pos=T.tensor(np.array([1.,.6,0.,0.])+.01*rng.uniform(-1,1,(4096,4)))
with T.no_grad():
 r,E,q,psi=ns['compute'](pos);sv=T.linalg.svdvals(E);out=ns['describe'](pos);out['min_coframe_singular_value']=float(sv[:,-1].min());out['max_coframe_condition_number']=float((sv[:,0]/sv[:,-1]).max());out['max_field_norm']=float(T.linalg.vector_norm(psi,dim=1).max())
Path(__file__).with_suffix('.json').write_text(json.dumps({'seed':291036,'new_independent_points':4096,'diagnostics':out},indent=2));print(out)
