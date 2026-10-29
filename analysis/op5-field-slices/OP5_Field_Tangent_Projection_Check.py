from pathlib import Path
import torch as T,numpy as np,json,time
ns={};exec(Path('OP5_Quadratic_Dense_Field_Control.py').read_text().split('\nbefore=')[0],ns);saved=json.loads(Path('OP5_Field_Residual_Diagnosis.json').read_text());initial=T.tensor(saved['coefficients_real_imag']);shape=initial.shape
rng=np.random.default_rng(291031);control=T.tensor(np.array([1.,.6,0.,0.])+.01*rng.uniform(-1,1,(512,4)))
# Use all337 training points; vectorized forward-mode differentiates720 real parameters.
pos=ns['train'];compute=ns['compute']
def vec(flat):
 ns['params']=flat.reshape(shape);r,E,q,psi=compute(pos);return T.cat([r.real.flatten(),r.imag.flatten()])
a=initial.flatten();start=time.time();r=vec(a).detach().numpy()
# Exact autograd columns, no finite differences. Chunked forward JVP keeps memory bounded.
cols=[]
for k in range(a.numel()):
 direction=T.zeros_like(a);direction[k]=1
 _,v=T.autograd.functional.jvp(vec,a,direction,create_graph=False,strict=False);cols.append(v.detach().numpy())
J=np.column_stack(cols);u,sv,vh=np.linalg.svd(J,full_matrices=False);rows=[]
for cutoff in [1e-6,1e-8,1e-10]:
 rank=int(np.sum(sv>sv[0]*cutoff));proj=u[:,:rank]@(u[:,:rank].T@r);step=-(vh[:rank].T@((u[:,:rank].T@r)/sv[:rank]));trials=[]
 for factor in [1e-3,1e-2,.1,1.]:
  ns['params']=(a+T.tensor(step)*factor).reshape(shape)
  try:
   tr=ns['metrics'](pos);ct=ns['metrics'](control);trials.append({'factor':factor,'train':tr,'control':ct})
  except Exception as e:trials.append({'factor':factor,'error':str(e)})
 rows.append({'relative_cutoff':cutoff,'rank':rank,'residual_norm':float(np.linalg.norm(r)),'linear_correctable_norm':float(np.linalg.norm(proj)),'linear_remaining_norm':float(np.linalg.norm(r-proj)),'step_norm':float(np.linalg.norm(step)),'trials':trials})
ns['params']=initial
out={'contract':'Full parameter Jacobian of quadratic family at saved field; all337 training points; no extra physics; first-order tangent only; unconstrained linear correction with causal checks after reinsertion.','dimensions':list(J.shape),'singular_values':sv.tolist(),'baseline':{'train':ns['metrics'](pos),'control':ns['metrics'](control)},'tests':rows,'seconds':time.time()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k!='singular_values'},indent=2))
