from pathlib import Path
import numpy as np,torch as T,json
ns={};exec(Path('OP5_Field_Tangent_Projection_Check.py').read_text().split('\na=initial.flatten()')[0],ns);a=ns['initial'].flatten();v=T.tensor(np.random.default_rng(291032).normal(size=len(a)));v=v/T.linalg.vector_norm(v)
_,jv=T.autograd.functional.jvp(ns['vec'],a,v);checks=[]
for h in [1e-5,1e-6,1e-7]:
 fd=(ns['vec'](a+h*v)-ns['vec'](a-h*v))/(2*h);checks.append({'step':h,'relative_error':float(T.linalg.vector_norm(fd-jv)/T.linalg.vector_norm(jv))})
Path(__file__).with_suffix('.json').write_text(json.dumps(checks,indent=2));print(checks)
