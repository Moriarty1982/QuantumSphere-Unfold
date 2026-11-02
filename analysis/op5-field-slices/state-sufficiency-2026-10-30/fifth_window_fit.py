"""Fifth-order calibration with frozen degree0..2; vary3,4 and recover5."""
from pathlib import Path
import importlib.util,json,numpy as np,torch as T,time,hashlib,platform
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('window_model',ROOT/'recursive_calibrator.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
model=m.TaylorModel(5);rows=[];tic=time.time();started=datetime.now(timezone.utc).isoformat()
inputs=[ROOT/'recursive_calibrator.py',ROOT/'recursive-order-4-result.json',ROOT/'joint-fit-result.json',ROOT/'third-joint-fit-result.json',model.source,model.repo/'analysis/op5-field-slices/OP5_Joint_Compatibility_Lower_Data.json',Path(__file__).resolve()]
hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
for ip in [0,1,2]:
 pos,c=model.raw_coeff(ip);bg=model.background(pos);A,topstart,rowstart=model.top_operator(c,bg)
 U,sv,Vh=np.linalg.svd(A,full_matrices=False);rank=int(sum(sv>sv[0]*1e-9));L=T.tensor(U[:,rank:]);fixed=T.tensor(c)
 start=len(m.indices(2));previous=len(m.indices(1));z0=m.pack(c[start:topstart])
 def full(z,top=None):
  return T.cat((fixed[:start],m.unpack(z),T.zeros_like(fixed[topstart:]) if top is None else m.unpack(top)),dim=0)
 def objective(z):
  F=model.evaluate(full(z),bg)
  return T.cat((F[previous:rowstart].flatten(),L.T@F[rowstart:].flatten()))
 fun=lambda z:objective(T.tensor(z)).detach().numpy();jac=T.func.jacrev(objective)
 z=z0.copy();initial=fun(z);history=[];damp=1e-7
 print('START',ip,'norm',np.linalg.norm(initial),flush=True)
 for it in range(18):
  r=fun(z);J=jac(T.tensor(z)).detach().numpy();normal=J@J.T;accepted=False
  for trial in range(10):
   step=-J.T@np.linalg.solve(normal+damp*np.eye(len(r)),r);candidate=z+step;nr=fun(candidate)
   if np.linalg.norm(nr)<np.linalg.norm(r) and np.linalg.norm(candidate)<100*max(np.linalg.norm(z0),1):
    z=candidate;accepted=True;damp=max(damp/3,1e-14);break
   damp*=10
  history.append({'iteration':it,'accepted':accepted,'norm':float(np.linalg.norm(fun(z))),'step_norm':float(np.linalg.norm(step)),'damping':damp})
  print('STEP',ip,history[-1],flush=True)
  if np.linalg.norm(fun(z))<1e-9 or not accepted:break
 F=model.evaluate(full(T.tensor(z)),bg).detach().numpy();b=F[rowstart:].flatten();tests=[]
 for cut in [1e-8,1e-9,1e-11]:
  top,_,tr,tsv=np.linalg.lstsq(A,-b,rcond=cut);tests.append({'rcond':cut,'rank':int(tr),'residual_norm':float(np.linalg.norm(A@top+b))})
 top=np.linalg.lstsq(A,-b,rcond=1e-9)[0];coeff=full(T.tensor(z),T.tensor(top));f=model.evaluate(coeff,bg).detach().numpy();blocks={}
 for d in range(5):
  ids=[n for n,a in enumerate(model.idx) if sum(a)==d];fac=np.array([m.factorial(model.idx[n]) for n in ids]);blocks[str(d)]=float(np.linalg.norm(f[ids]*fac[:,None]))
 cc=coeff.detach().numpy();norms={str(d):float(np.linalg.norm(np.array([v*m.factorial(a) for a,v in zip(model.fullidx,cc) if sum(a)==d]))) for d in range(6)}
 moves={}
 for d in range(5):
  ids=[n for n,a in enumerate(model.fullidx) if sum(a)==d];diff=cc[ids]-c[ids]
  moves[str(d)]={'coefficient_change':float(np.linalg.norm(diff)),'relative_coefficient_change':float(np.linalg.norm(diff)/np.linalg.norm(c[ids])),'exactly_fixed':bool(np.array_equal(cc[ids],c[ids]))}
 rows.append({'point_index':ip,'point':pos.tolist(),'frozen_degrees':[0,1,2],'adjustable_degrees':[3,4],'recovered_degree':5,'initial_objective':float(np.linalg.norm(initial)),'final_objective':float(np.linalg.norm(fun(z))),'history':history,'highest_rank':rank,'highest_shape':list(A.shape),'highest_singular_values':sv.tolist(),'top_checks':tests,'raw_residual_blocks':blocks,'raw_jet_norms':norms,'movements':moves,'multiindices':model.fullidx,'coefficients_real_imag':np.concatenate((cc.real,cc.imag),axis=1).tolist()})
 out={'contract':'Frozen degree0..2 from successful order4 seed; jointly vary3,4 and recover5. Complete left elimination of highest jets, full retained residuals. Float64 nonlinear bounded fit, no general no-go or all-order theorem.','started_at':started,'seconds':time.time()-tic,'software':{'python':platform.python_version(),'torch':T.__version__,'numpy':np.__version__,'sympy':m.s.__version__},'inputs_sha256':hashes,'inputs_unchanged':all(hashlib.sha256(p.read_bytes()).hexdigest()==hashes[str(p)] for p in inputs),'results':rows}
 (ROOT/'fifth-window-result.json').write_text(json.dumps(out,indent=2))
 print('DONE',ip,blocks,'moves',moves,flush=True)
