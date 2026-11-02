from pathlib import Path
import numpy as np,torch as T,json,time
ns={};exec(Path('OP5_Field_Tangent_Projection_Check.py').read_text().split('\na=initial.flatten()')[0],ns)
a=T.tensor(json.loads(Path('OP5_Boundary_Fair_Balanced_Check.json').read_text())['coefficients_real_imag']).flatten();rngedge=np.random.default_rng(291043);edge=rngedge.uniform(-1,1,(64,4));edge[np.arange(64),np.arange(64)%4]=np.where((np.arange(64)//4)%2,1.,-1.);pos=T.cat([ns['pos'],T.tensor(np.array([1.,.6,0.,0.])+.01*edge)]);ns['pos']=pos;shape=ns['shape'];vec=ns['vec'];rng=np.random.default_rng(291045);control=T.tensor(np.array([1.,.6,0.,0.])+.01*rng.uniform(-1,1,(1024,4)));history=[];damping=1e-6;start=time.time()
ns['ns']['params']=a.reshape(shape);before={'train':ns['ns']['metrics'](pos),'control':ns['ns']['metrics'](control)}
for iteration in range(3):
 r=vec(a).detach().numpy();cols=[]
 for k in range(a.numel()):
  v=T.zeros_like(a);v[k]=1;_,jv=T.autograd.functional.jvp(vec,a,v);cols.append(jv.detach().numpy())
 J=np.column_stack(cols);u,sv,vh=np.linalg.svd(J,full_matrices=False);g=u.T@r;accepted=False;trials=[]
 for attempt in range(10):
  lam=damping*sv[0]**2;step=-(vh.T@(sv*g/(sv**2+lam)));pred=np.dot(r,r)-np.linalg.norm(r+J@step)**2
  candidate=a+T.tensor(step)
  try:
   rr=vec(candidate).detach().numpy();tm=ns['ns']['metrics'](pos);cm=ns['ns']['metrics'](control);actual=np.dot(r,r)-np.dot(rr,rr);ratio=actual/pred if pred>0 else -1
   regular=tm['max_inverse_g00']<-.05 and cm['max_inverse_g00']<-.05 and tm['min_q']>1e-4 and cm['min_q']>1e-4 and tm['min_abs_detE']>1e-5 and cm['min_abs_detE']>1e-5
  except Exception as e:ratio=-1;regular=False;tm={};cm={}
  trials.append({'damping_relative':damping,'step_norm':float(np.linalg.norm(step)),'prediction_ratio':float(ratio),'train':tm,'control':cm,'regular':regular})
  if ratio>.1 and regular:
   a=candidate.detach();accepted=True
   if ratio>.75:damping/=3
   elif ratio<.25:damping*=3
   break
  damping*=10
 history.append({'iteration':iteration,'accepted':accepted,'trials':trials});print(iteration,accepted,tm.get('rms_residual'),cm.get('rms_residual'),damping,flush=True)
 if not accepted:break
ns['ns']['params']=a.reshape(shape);out={'contract':'Five damped Gauss Newton outer steps; all720 parameters and337 training points, fixed region/model. Damping accepted by actual/predicted reduction and geometry checks. Control points participate in geometric regularity acceptance, not residual minimization.','before':before,'after':{'train':ns['ns']['metrics'](pos),'control':ns['ns']['metrics'](control)},'history':history,'coefficients_real_imag':a.reshape(shape).tolist(),'seconds':time.time()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
