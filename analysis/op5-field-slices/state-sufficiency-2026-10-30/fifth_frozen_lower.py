"""Control: keep order4 seed through degree3 fixed, calibrate degree4, recover5."""
from pathlib import Path
import importlib.util,json,numpy as np,torch as T,time,hashlib
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('frozen_model',ROOT/'recursive_calibrator.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
model=m.TaylorModel(5);rows=[];tic=time.time()
inputs=[ROOT/'recursive_calibrator.py',ROOT/'recursive-order-4-result.json',Path(__file__)]
hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
for ip in [0,1,2]:
 pos,c=model.raw_coeff(ip);bg=model.background(pos);A,topstart,rowstart=model.top_operator(c,bg)
 U,sv,Vh=np.linalg.svd(A,full_matrices=False);rank=int(sum(sv>sv[0]*1e-9));L=T.tensor(U[:,rank:]);fixed=T.tensor(c)
 start=len(m.indices(3));previous=len(m.indices(2));z0=m.pack(c[start:topstart])
 def full(z,top=None):
  return T.cat((fixed[:start],m.unpack(z),T.zeros_like(fixed[topstart:]) if top is None else m.unpack(top)),dim=0)
 def objective(z):
  F=model.evaluate(full(z),bg)
  return T.cat((F[previous:rowstart].flatten(),L.T@F[rowstart:].flatten()))
 r0=objective(T.tensor(z0)).detach().numpy();J=T.func.jacrev(objective)(T.tensor(z0)).detach().numpy()
 correction,_,jr,jsv=np.linalg.lstsq(J,-r0,rcond=1e-9);z=z0+correction
 r=objective(T.tensor(z)).detach().numpy();mid=objective(T.tensor(z0+.5*correction)).detach().numpy();afferr=np.linalg.norm(mid-r0-.5*J@correction)
 F=model.evaluate(full(T.tensor(z)),bg).detach().numpy();b=F[rowstart:].flatten();top,_,tr,_=np.linalg.lstsq(A,-b,rcond=1e-9)
 coeff=full(T.tensor(z),T.tensor(top));f=model.evaluate(coeff,bg).detach().numpy();blocks={}
 for d in range(5):
  ids=[n for n,a in enumerate(model.idx) if sum(a)==d];fac=np.array([m.factorial(model.idx[n]) for n in ids]);blocks[str(d)]=float(np.linalg.norm(f[ids]*fac[:,None]))
 cc=coeff.detach().numpy();rows.append({'point_index':ip,'point':pos.tolist(),'frozen_degrees':[0,1,2,3],'adjustable_degree':4,'initial_objective':float(np.linalg.norm(r0)),'objective_after':float(np.linalg.norm(r)),'affine_midpoint_error':float(afferr),'repair_rank':int(jr),'repair_shape':list(J.shape),'repair_singular_values':jsv.tolist(),'top_rank':int(tr),'degree4_coefficient_change':float(np.linalg.norm(correction)),'full_raw_residual_blocks':blocks,'multiindices':model.fullidx,'coefficients_real_imag':np.concatenate((cc.real,cc.imag),axis=1).tolist()})
 out={'contract':'Frozen lower0..3 coefficients of fourth-order seed; adjust fourth coefficients, recover fifth. Finite linear rank/tolerance check, no existence theorem.','inputs_sha256':hashes,'seconds':time.time()-tic,'inputs_unchanged':all(hashlib.sha256(p.read_bytes()).hexdigest()==hashes[str(p)] for p in inputs),'results':rows}
 (ROOT/'fifth-frozen-lower-result.json').write_text(json.dumps(out,indent=2))
 print(ip,'initial',np.linalg.norm(r0),'after',np.linalg.norm(r),'rank',jr,'affine',afferr,'blocks',blocks,flush=True)
