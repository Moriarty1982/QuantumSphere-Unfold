"""Frozen successful two-jets, free fully symmetric third jets; python third_check.py."""
from pathlib import Path
import os
os.environ['OMP_NUM_THREADS']='2';os.environ['OPENBLAS_NUM_THREADS']='2'
import numpy as np,torch as T,sympy as s,json,itertools,time,hashlib,sys,platform
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parent
ns={'__file__':str(ROOT/'joint_fit.py')};exec((ROOT/'joint_fit.py').read_text().split('rows=[];start=')[0],ns)
T.set_num_threads(2)
bg,coords=ns['bg'],ns['coords'];pairs=ns['pairs'];pick=ns['picker']
bg2=s.Matrix.hstack(*[bg.diff(coords[i],coords[j]) for i,j in pairs])
bg2fun=s.lambdify(coords,bg2,'numpy',cse=True)
triples=list(itertools.combinations_with_replacement(range(4),3));ti={v:i for i,v in enumerate(triples)}
fixed=json.loads((ROOT/'joint-fit-result.json').read_text());start=time.time();rows=[]
inputs=[ROOT/'third_check.py',ROOT/'joint_fit.py',ROOT/'joint-fit-result.json',ns['paths'][0],ns['paths'][1],ns['paths'][2]]
hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
started=datetime.now(timezone.utc).isoformat()
Q,K,Y=ns['Q'],ns['Kt'],ns['Y'];c24,c96,pack=ns['c24'],ns['c96'],ns['pack']
for ip,(row,old) in enumerate(zip(fixed['results'],ns['data']['results'])):
 pos=np.array(row['point']);psi=np.array([complex(*v) for v in old['field_values_real_imag']]);jp=np.array(row['first_jets_packed']);j=(jp[:48]+1j*jp[48:]).reshape(4,12)
 hp=np.array(row['symmetric_second_jets']).reshape(10,24);h=(hp[:,:12]+1j*hp[:,12:])[pick]
 bt=T.tensor(np.asarray(ns['bgfun'](*pos),complex).ravel());db=T.tensor(np.asarray(ns['bgjac'](*pos),complex));bp=np.asarray(bg2fun(*pos),complex);bfull=np.empty((577,4,4),complex)
 for n,(mu,nu) in enumerate(pairs):bfull[:,mu,nu]=bfull[:,nu,mu]=bp[:,n]
 ddb=T.tensor(bfull);pt=T.tensor(pos)
 def fun(q):
  ps=c24(q[:24]);js=c96(q[24:120]);dx=(q[120:]-pt).to(T.complex128)
  b=bt+db@dx+.5*T.einsum('aij,i,j->a',ddb,dx,dx)
  cov=js+1j*T.einsum('mij,j->mi',b[1:].reshape(4,12,12),ps)
  ee=T.einsum('i,aij,mj->am',ps.conj(),Q,cov).real
  f=1j*T.einsum('ma,aij,mj->i',T.linalg.inv(ee).to(T.complex128),K,cov)-b[0].real*(Y@ps)
  return T.cat((f.real,f.imag))
 q=T.tensor(np.r_[pack(psi),jp,pos]);D=T.func.jacrev(fun)(q).detach().numpy();DD=T.func.jacrev(T.func.jacrev(fun))(q).detach().numpy()
 tangent=np.vstack((np.r_[j.real.T,j.imag.T],np.r_[h.real.transpose(1,2,0).reshape(48,4),h.imag.transpose(1,2,0).reshape(48,4)],np.eye(4)))
 b=np.concatenate([tangent[:,mu]@DD@tangent[:,nu]+D[:,:24]@pack(h[mu,nu]) for mu,nu in pairs])
 A=np.zeros((240,480))
 for pn,(mu,nu) in enumerate(pairs):
  for lam in range(4):
   n=ti[tuple(sorted((mu,nu,lam)))]
   for r in range(24):
    col=24*n+r;idx=24+48*(r//12)+12*lam+(r%12)
    A[pn*24:(pn+1)*24,col]+=D[:,idx]
 tests=[]
 for cut in [1e-8,1e-9,1e-11]:
  sol,_,rank,sv=np.linalg.lstsq(A,-b,rcond=cut);res=A@sol+b
  tests.append({'rcond':cut,'rank':int(rank),'residual_norm':float(np.linalg.norm(res)),'third_jet_norm':float(np.linalg.norm(sol)),'singular_values':sv.tolist(),'third_jets':sol.tolist()})
 sol=np.array(tests[1]['third_jets']);tp=sol.reshape(20,24);tc=tp[:,:12]+1j*tp[:,12:];third=np.empty((4,4,4,12),complex)
 for ii in itertools.product(range(4),repeat=3):third[ii]=tc[ti[tuple(sorted(ii))]]
 # Unrestricted third jets: one independent jet-gradient per differentiated pair.
 Ju=D[:,24:120];unres=[]
 for pn in range(10):
  zz,_,ur,us=np.linalg.lstsq(Ju,-b[pn*24:(pn+1)*24],rcond=1e-9);unres.extend(Ju@zz+b[pn*24:(pn+1)*24])
 # Independent direct NumPy evaluation on a shared cubic Taylor field.
 def direct(dx):
  ps=psi+np.einsum('m,mi->i',dx,j)+.5*np.einsum('m,n,mni->i',dx,dx,h)+np.einsum('m,n,l,mnli->i',dx,dx,dx,third)/6
  js=j+np.einsum('n,mni->mi',dx,h)+.5*np.einsum('n,l,mnli->mi',dx,dx,third)
  bgv=np.asarray(ns['bgfun'](*(pos+dx)),complex).ravel();cov=js+1j*np.einsum('mij,j->mi',bgv[1:].reshape(4,12,12),ps)
  ee=np.einsum('i,aij,mj->am',ps.conj(),ns['QQ'],cov).real
  f=1j*np.einsum('ma,aij,mj->i',np.linalg.inv(ee),ns['KK'],cov)-bgv[0].real*(ns['YY']@ps)
  return pack(f)
 controls=[];f0=direct(np.zeros(4));expected=A@sol+b
 for eps in [1e-3,3e-4,1e-4]:
  sec=[]
  for mu,nu in pairs:
   u=np.eye(4)[mu]*eps;v=np.eye(4)[nu]*eps
   if mu==nu:val=(direct(u)-2*f0+direct(-u))/eps**2
   else:val=(direct(u+v)-direct(u-v)-direct(-u+v)+direct(-u-v))/(4*eps**2)
   sec.extend(val)
  controls.append({'step':eps,'ddF_norm':float(np.linalg.norm(sec)),'difference_from_AD':float(np.linalg.norm(np.array(sec)-expected))})
 f=fun(q).detach().numpy();first=(D@tangent).T.ravel()
 rows.append({'point':pos.tolist(),'F_norm':float(np.linalg.norm(f)),'dF_norm':float(np.linalg.norm(first)),'source_norm':float(np.linalg.norm(b)),'matrix_shape':list(A.shape),'tests':tests,'unrestricted_residual':float(np.linalg.norm(unres)),'unrestricted_block_rank':int(ur),'controls':controls})
 out={'contract':'Fixed successful field values/first/second jets. Free480 real fully symmetric third derivatives. Solve240 real second total derivatives of F; exact symbolic background derivatives to order2 and AD field derivatives. Float64, no regional existence.','started_at':started,'seconds':time.time()-start,'inputs_sha256':hashes,'inputs_unchanged':all(hashlib.sha256(p.read_bytes()).hexdigest()==hashes[str(p)] for p in inputs),'software':{'python':platform.python_version(),'numpy':np.__version__,'torch':T.__version__,'sympy':s.__version__},'results':rows}
 (ROOT/'third-check-result.json').write_text(json.dumps(out,indent=2))
 print('POINT',ip,'F,dF',np.linalg.norm(f),np.linalg.norm(first),'symmetric',[(v['rcond'],v['rank'],v['residual_norm']) for v in tests],'unsym',np.linalg.norm(unres),'controls',controls,flush=True)
