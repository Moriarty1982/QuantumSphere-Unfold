from pathlib import Path
import json,numpy as np,torch as T
ns={};exec(Path('OP5_Field_Residual_Diagnosis.py').read_text().split('\nbefore=')[0],ns);d=json.loads(Path('OP5_Peak_Mean_Control.json').read_text());ns['params'].data.copy_(T.tensor(d['coefficients_real_imag']));old={};exec(Path('OP5_State_Second_Jet_Check.py').read_text().split('data=json.loads')[0],old)
p=np.array([1.,.6,0.,0.]);psi=ns['compute'](T.tensor(p[None]))[3].detach().numpy()[0];hf=1e-6;jets=np.array([(ns['compute'](T.tensor((p+hf*np.eye(4)[mu])[None]))[3].detach().numpy()[0]-ns['compute'](T.tensor((p-hf*np.eye(4)[mu])[None]))[3].detach().numpy()[0])/(2*hf) for mu in range(4)])
out=[]
for h in [1e-4,1e-5,1e-6]:
 cols=[]
 for k in range(24):
  delta=np.zeros((4,12),complex);delta[0,k%12]=1 if k<12 else 1j
  cols.append((old['residual'](p,psi,jets+h*delta)-old['residual'](p,psi,jets-h*delta))/(2*h))
 sv=np.linalg.svd(np.column_stack(cols),compute_uv=False);out.append({'step':h,'rank_relative1e-8':int(sum(sv>sv[0]*1e-8)),'singular_values':sv.tolist()})
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print([(r['step'],r['rank_relative1e-8'],r['singular_values'][-3:]) for r in out])
