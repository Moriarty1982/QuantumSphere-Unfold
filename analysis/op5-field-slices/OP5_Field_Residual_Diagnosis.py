from pathlib import Path
import json,numpy as np,torch as T
ns={};exec(Path('OP5_Quadratic_Dense_Field_Control.py').read_text().split('before=')[0],ns);saved=json.loads(Path('OP5_Quadratic_Dense_Field_Control.json').read_text());ns['params'].data.copy_(T.tensor(saved['coefficients_real_imag']));compute=ns['compute'];params=ns['params'];train=ns['train'];center=np.array(saved['center']);rng=np.random.default_rng(291027);control=T.tensor(center+.01*rng.uniform(-1,1,(512,4)))
SS=T.tensor(np.kron(np.array(ns['S'],complex),np.eye(4)))
def describe(pos):
 with T.no_grad():
  r,E,q,psi=compute(pos);tt=pos[:,0];v2=(pos[:,1:]**2).sum(1)/tt**2;h=(1-v2).rsqrt()/(1-tt**2/4).sqrt();mass=h[:,None]*(psi@ns['MT'].T);kin=r+mass
  sq=(r.abs()**2).reshape(-1,3,4).sum((0,2));total=sq.sum();scale=T.linalg.vector_norm(kin,dim=1)+T.linalg.vector_norm(mass,dim=1);rel=T.linalg.vector_norm(r,dim=1)/scale
  projection=T.einsum('ni,ij,nj->n',psi.conj(),SS,r)
  return {'metrics':ns['metrics'](pos),'species_squared_residual_shares':(sq/total).tolist(),'relative_residual_rms':float(T.sqrt((rel**2).mean())),'relative_residual_max':float(rel.max()),'max_imaginary_S_projection':float(projection.imag.abs().max()),'max_real_S_projection':float(projection.real.abs().max())}
before={'train':describe(train),'control512':describe(control)}
r,_,_,_=compute(train);loss=(r.abs()**2).sum(1).mean();loss.backward();gradient={'loss':float(loss.detach()),'gradient_norm':float(params.grad.norm()),'gradient_max':float(params.grad.abs().max())};params.grad=None
opt=T.optim.LBFGS([params],lr=.5,max_iter=1200,tolerance_grad=1e-11,tolerance_change=1e-15,line_search_fn='strong_wolfe');calls=0
def closure():
 global calls
 opt.zero_grad();r,E,q,psi=compute(train);metric=T.einsum('nai,ab,nbj->nij',E,T.diag(T.tensor([-1.,1.,1.,1.])),E);g00=T.linalg.inv(metric)[:,0,0];loss=(r.abs()**2).sum(1).mean()+100*T.relu(g00+.05).square().mean()+100*T.relu(1e-4-q).square().mean();loss.backward();calls+=1;return loss
opt.step(closure);out={'contract':'Same quadratic amplitudes, same337 training points, same region/couplings; continued optimization1200 iterations. Diagnostic relative norm |F|/(|kinetic|+|mass|) in comparison normalization, not physical error.','before':before,'gradient_before':gradient,'after':{'train':describe(train),'control512':describe(control)},'calls':calls,'coefficients_real_imag':params.detach().tolist()};Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k!='coefficients_real_imag'},indent=2))
