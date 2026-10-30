from pathlib import Path
import numpy as np,torch as T,json
ns={};exec(Path('OP5_Field_Residual_Diagnosis.py').read_text().split('\nbefore=')[0],ns);d=json.loads(Path('OP5_Peak_Mixed_Check.json').read_text());ns['params'].data.copy_(T.tensor(d['coefficients_real_imag']));old={};exec(Path('OP5_State_Second_Jet_Check.py').read_text().split('data=json.loads')[0],old)
points=[np.array([1.,.6,0.,0.]),np.array([.99,.59,.01,-.01]),np.array([1.005,.605,-.005,.005])];out=[]
for p in points:
 psi=ns['compute'](T.tensor(p[None]))[3].detach().numpy()[0];hf=1e-6;jets=np.array([(ns['compute'](T.tensor((p+hf*np.eye(4)[mu])[None]))[3].detach().numpy()[0]-ns['compute'](T.tensor((p-hf*np.eye(4)[mu])[None]))[3].detach().numpy()[0])/(2*hf) for mu in range(4)])
 gg,hh,spin=old['back'](*p);cov=jets.copy()
 for mu in range(1,4):cov[mu]+=1j*np.kron(np.asarray(gg)*np.asarray(spin).ravel()[mu-1],np.eye(4))@psi
 pack=lambda z:np.r_[z.real,z.imag]
 B=np.column_stack([pack(v) for v in cov]);Q=old['QQ'];A=np.column_stack([[np.vdot(psi,q@(np.eye(12,dtype=complex)[k%12]*(1 if k<12 else 1j))).real for q in Q] for k in range(24)])
 E=np.array([[np.vdot(psi,q@cov[mu]).real for mu in range(4)] for q in Q]);assert np.linalg.norm(A@B-E)<1e-9
 _,_,vh=np.linalg.svd(A,full_matrices=True);N=vh[4:].T;tests=[]
 for h in [1e-4,1e-5,1e-6]:
  cols=[]
  for k in range(24):
   delta=np.zeros((4,12),complex);delta[0,k%12]=1 if k<12 else 1j
   cols.append((old['residual'](p,psi,jets+h*delta)-old['residual'](p,psi,jets-h*delta))/(2*h))
  J=np.column_stack(cols);sv=np.linalg.svd(J,compute_uv=False);red=np.linalg.svd(J@N,compute_uv=False);aug=np.linalg.svd(np.vstack([J,A]),compute_uv=False)
  tests.append({'step':h,'full_rank':int(sum(sv>sv[0]*1e-8)),'fixed_coframe_reduced_rank':int(sum(red>red[0]*1e-8)),'augmented_rank':int(sum(aug>aug[0]*1e-8)),'reduced_min_sv':float(red[-1]),'reduced_condition':float(red[0]/red[-1]),'gauge_null_relative_error':float(np.linalg.norm(J@B)/(np.linalg.norm(J)*np.linalg.norm(B)))})
 P=np.eye(24)-B@np.linalg.solve(E,A)
 assert np.linalg.norm(P@P-P)<1e-9 and np.linalg.norm(A@P)<1e-9 and np.linalg.norm(P@B)<1e-9
 out.append({'projector_idempotence_error':float(np.linalg.norm(P@P-P)),'projector_rank':int(np.linalg.matrix_rank(P)),'point':p.tolist(),'coframe_gauge_rank':int(np.linalg.matrix_rank(A)),'pointwise_gauge_dimension':int(np.linalg.matrix_rank(B)),'AB_minus_E_norm':float(np.linalg.norm(A@B-E)),'tests':tests})
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(out)
