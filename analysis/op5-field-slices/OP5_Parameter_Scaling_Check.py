from pathlib import Path
import numpy as np,json,torch as T,time
base={};exec(Path('OP5_Quadratic_Dense_Field_Control.py').read_text().split('\nbefore=')[0],base)
saved=json.loads(Path('OP5_Field_Residual_Diagnosis.json').read_text());initial=T.tensor(saved['coefficients_real_imag']); train=base['train'];rng=np.random.default_rng(291030);control=T.tensor(np.array([1.,.6,0.,0.])+.01*rng.uniform(-1,1,(4096,4)))
# Independent final controls. No control point enters the optimizer.
results=[]
for scaled in [False,True]:
 ns={};exec(Path('OP5_Quadratic_Dense_Field_Control.py').read_text().split('\nbefore=')[0],ns)
 # Normalize coordinates in parameter space by polynomial degree; keep same field family.
 scales=T.ones_like(initial)
 if scaled:
  scales[:,1:5]*=.01;scales[:,5:]*=.0001
 theta=T.nn.Parameter((initial/scales).clone());opt=T.optim.LBFGS([theta],lr=.5,max_iter=1200,tolerance_grad=1e-12,tolerance_change=1e-16,line_search_fn='strong_wolfe');calls=0
 def closure():
  global calls
  opt.zero_grad();ns['params']=theta*scales;r,E,q,psi=ns['compute'](train);g=T.einsum('nai,ab,nbj->nij',E,T.diag(T.tensor([-1.,1.,1.,1.])),E);g00=T.linalg.inv(g)[:,0,0];loss=(r.abs()**2).sum(1).mean()+100*T.relu(g00+.05).square().mean()+100*T.relu(1e-4-q).square().mean();loss.backward();calls+=1;return loss
 start=time.time();opt.step(closure);ns['params']=theta*scales
 results.append({'scaled':scaled,'train':ns['metrics'](train),'fresh4096':ns['metrics'](control),'calls':calls,'seconds':time.time()-start,'coefficients_real_imag':ns['params'].detach().tolist()})
 print({k:v for k,v in results[-1].items() if k!='coefficients_real_imag'},flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps({'contract':'Same quadratic family/337 training points/region .01. Two branches from same saved initial field;1200 LBFGS iterations each. Degree scales 1,.01,.0001 vs unscaled. New4096 controls seed291030.','results':results},indent=2))
