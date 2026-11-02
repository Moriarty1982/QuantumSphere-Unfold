from pathlib import Path
import numpy as np,torch as T,json
ns={};exec(Path('OP5_Quadratic_Dense_Field_Control.py').read_text().split('before=')[0],ns);saved=json.loads(Path('OP5_Quadratic_Dense_Field_Control.json').read_text());ns['params'].data.copy_(T.tensor(saved['coefficients_real_imag']));compute=ns['compute'];old={};exec(Path('OP5_State_Second_Jet_Check.py').read_text().split('data=json.loads')[0],old)
center=np.array(saved['center']);rng=np.random.default_rng(291027);pos=center+.01*rng.uniform(-1,1,(512,4));checks=[]
for p in pos[:3]:
 psi=compute(T.tensor(p[None]))[3].detach().numpy()[0];rr=compute(T.tensor(p[None]))[0].detach().numpy()[0]
 for h in [1e-5,1e-6]:
  jets=np.array([(compute(T.tensor((p+h*np.eye(4)[mu])[None]))[3].detach().numpy()[0]-compute(T.tensor((p-h*np.eye(4)[mu])[None]))[3].detach().numpy()[0])/(2*h) for mu in range(4)])
  r=old['residual'](p,psi,jets);rc=r[:12]+1j*r[12:];checks.append({'step':h,'difference':float(np.linalg.norm(rc-rr))})
out={'second_independent_sample':ns['metrics'](T.tensor(pos)),'derivative_checks':checks};Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(out)
