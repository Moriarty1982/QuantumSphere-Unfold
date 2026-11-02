from pathlib import Path
import numpy as np,torch as T,json,itertools
ns={};exec(Path('OP5_Field_Residual_Diagnosis.py').read_text().split('\nbefore=')[0],ns)
saved=json.loads(Path('OP5_Gauss_Newton_Third_Block_Check.json').read_text());ns['params'].data.copy_(T.tensor(saved['coefficients_real_imag']));center=np.array([1.,.6,0.,0.]);grid=np.array(list(itertools.product(np.linspace(-1,1,5),repeat=4)));boundary=np.any(abs(grid)==1,axis=1);rng=np.random.default_rng(291038)
reports={}
for name,offset in [('grid625',grid),('boundary544',grid[boundary]),('fresh4096',rng.uniform(-1,1,(4096,4)))]:
 pos=T.tensor(center+.01*offset);report=ns['describe'](pos)
 with T.no_grad():
  r,E,q,psi=ns['compute'](pos);sv=T.linalg.svdvals(E);norm=T.linalg.vector_norm(r,dim=1);idx=int(T.argmax(norm));report.update({'points':len(offset),'worst_point':pos[idx].tolist(),'min_coframe_singular_value':float(sv[:,-1].min()),'max_coframe_condition_number':float((sv[:,0]/sv[:,-1]).max()),'max_field_norm':float(T.linalg.vector_norm(psi,dim=1).max())})
 reports[name]=report
Path(__file__).with_suffix('.json').write_text(json.dumps(reports,indent=2));print(json.dumps(reports,indent=2))
