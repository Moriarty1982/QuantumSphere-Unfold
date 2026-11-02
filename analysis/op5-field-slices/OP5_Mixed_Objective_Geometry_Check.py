from pathlib import Path
import numpy as np,torch as T,json
ns={};exec(Path('OP5_Field_Residual_Diagnosis.py').read_text().split('\nbefore=')[0],ns);rng=np.random.default_rng(291047);pos=T.tensor(np.array([1.,.6,0.,0.])+.01*rng.uniform(-1,1,(4096,4)));out=[]
for name in ['OP5_Boundary_Fair_Balanced_Check.json','OP5_Peak_Mean_Control.json','OP5_Peak_Weighted_Check.json']:
 d=json.loads(Path(name).read_text());ns['params'].data.copy_(T.tensor(d['coefficients_real_imag']))
 with T.no_grad():
  r,E,q,psi=ns['compute'](pos);inv=T.linalg.inv(E);g=T.einsum('nai,ab,nbj->nij',E,T.diag(T.tensor([-1.,1.,1.,1.])),E);sv=T.linalg.svdvals(E);ev=T.linalg.eigvalsh(g);temporal=inv[:,0,:];rad=T.linalg.vector_norm(temporal[:,1:],dim=1);lam=T.stack([temporal[:,0]-rad,temporal[:,0]+rad],1).abs();principal=lam.max(1).values/lam.min(1).values
  out.append({'field':name,'min_E_singular_value':float(sv[:,-1].min()),'max_E_condition':float((sv[:,0]/sv[:,-1]).max()),'min_temporal_principal_abs_eigenvalue':float(lam.min()),'max_temporal_principal_condition':float(principal.max()),'all_metric_signatures_minus_plus_plus_plus':bool(T.all(ev[:,0]<0) and T.all(ev[:,1:]>0)),'max_g_inverse00':float(T.linalg.inv(g)[:,0,0].max())})
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(out)
