from pathlib import Path
import numpy as np,torch as T,json,time
source=Path('OP5_Quadratic_Dense_Field_Control.py').read_text().split('\nbefore=')[0];saved=json.loads(Path('OP5_Peak_Mixed_Check.json').read_text());initial=T.tensor(saved['coefficients_real_imag']);rng=np.random.default_rng(291043);edge=rng.uniform(-1,1,(64,4));edge[np.arange(64),np.arange(64)%4]=np.where((np.arange(64)//4)%2,1.,-1.)
controlrng=np.random.default_rng(291048);control=T.tensor(np.array([1.,.6,0.,0.])+.01*controlrng.uniform(-1,1,(1024,4)));out=[]
for weight in [0.,4.]:
 ns={};exec(source,ns);params=ns['params'];params.data.copy_(initial);train=T.cat([ns['train'],T.tensor(np.array([1.,.6,0.,0.])+.01*edge)]);K4=T.tensor(np.array([np.eye(4)]+[np.array(v,complex) for v in ns['al']]));Q=ns['QT']
 def evaluate(pos):
  r,E,q,psi=ns['compute'](pos);inv=T.linalg.inv(E);H=1j*T.einsum('na,aij->nij',inv[:,0].to(T.complex128),K4);Hi=T.linalg.inv(H)
  # Inverse frozen time operator repeated on three species.
  H12=T.stack([T.kron(T.eye(3,dtype=T.complex128),hi.contiguous()) for hi in Hi]);left=T.einsum('ni,aij,njk->nak',psi.conj(),Q,H12);C=T.einsum('nai,ni->na',left,r).real;gram=T.einsum('nai,nbi->nab',left,left.conj()).real
  coeff=T.linalg.solve(gram,C[:,:,None]).squeeze(-1);orth=(C*coeff).sum(1)
  return r,E,q,orth
 def metrics(pos):
  with T.no_grad():
   r,E,q,orth=evaluate(pos);return {'full_RMS':float(T.sqrt((r.abs()**2).sum(1).mean())),'full_max':float(T.linalg.vector_norm(r,dim=1).max()),'compatibility_RMS':float(T.sqrt(T.clamp(orth,min=0).mean())),'geometry':ns['metrics'](pos)}
 before=metrics(control);opt=T.optim.LBFGS([params],lr=.5,max_iter=400,tolerance_grad=1e-11,tolerance_change=1e-15,line_search_fn='strong_wolfe');calls=0
 def closure():
  global calls
  opt.zero_grad();r,E,q,orth=evaluate(train);g=T.einsum('nai,ab,nbj->nij',E,T.diag(T.tensor([-1.,1.,1.,1.])),E);g00=T.linalg.inv(g)[:,0,0];loss=(r.abs()**2).sum(1).mean()+weight*orth.mean()+100*T.relu(g00+.05).square().mean()+100*T.relu(1e-4-q).square().mean();loss.backward();calls+=1;return loss
 start=time.time();opt.step(closure);result={'constraint_weight':weight,'before_control':before,'after_train':metrics(train),'after_control':metrics(control),'calls':calls,'seconds':time.time()-start,'coefficients_real_imag':params.detach().tolist()};out.append(result);print({k:v for k,v in result.items() if k!='coefficients_real_imag'},flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
