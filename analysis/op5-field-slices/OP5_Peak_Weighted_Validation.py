from pathlib import Path
import json,numpy as np,torch as T
ns={};exec(Path('OP5_Field_Residual_Diagnosis.py').read_text().split('\nbefore=')[0],ns);center=np.array([1.,.6,0.,0.]);rng=np.random.default_rng(291046);edge=rng.uniform(-1,1,(1024,4));edge[np.arange(1024),np.arange(1024)%4]=np.where((np.arange(1024)//4)%2,1.,-1.);inside=rng.uniform(-1,1,(4096,4));reports=[]
for filename in ['OP5_Boundary_Fair_Balanced_Check.json','OP5_Peak_Mean_Control.json','OP5_Peak_Weighted_Check.json']:
 data=json.loads(Path(filename).read_text());ns['params'].data.copy_(T.tensor(data['coefficients_real_imag']));groups={}
 for name,off in [('fresh_boundary1024',edge),('fresh_inside4096',inside)]:
  pos=T.tensor(center+.01*off);groups[name]=ns['describe'](pos)
  with T.no_grad():r,E,q,psi=ns['compute'](pos);groups[name]['smallest_E_singular_value']=float(T.linalg.svdvals(E)[:,-1].min())
 if 'Boundary' in filename:
  groups['faces']=[ns['describe'](T.tensor(center+.01*edge[np.arange(1024)%8==k])) for k in range(8)]
 reports.append({'field':filename,'groups':groups})
Path(__file__).with_suffix('.json').write_text(json.dumps(reports,indent=2));print([(r['field'],{k:v['metrics'] for k,v in r['groups'].items() if k!='faces'}) for r in reports])
