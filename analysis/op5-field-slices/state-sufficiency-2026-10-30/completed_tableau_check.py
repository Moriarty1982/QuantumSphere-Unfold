"""Tableau/prolongation of F,G,dg, not an analytic existence certificate."""
from pathlib import Path
import importlib.util,json,numpy as np,torch as T,itertools,time
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('complete_model',ROOT/'recursive_calibrator.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
model=m.TaylorModel(3);data=json.loads((ROOT/'fifth-window-result.json').read_text());rows=[];tic=time.time()
def realmat(z):return np.block([[z.real,-z.imag],[z.imag,z.real]])
H=np.array([realmat(1j*k) for k in model.K.numpy()]);Hb=H.copy();Hb[0]*=-1;Hb=T.tensor(Hb)
Z=T.tensor(np.kron(np.diag([1,-1,0]),np.array(model.ns['beta'],complex)));pairs=list(itertools.combinations_with_replacement(range(4),2))
for row in data['results']:
 pos=np.array(row['point']);pp=np.array(row['coefficients_real_imag']);c=pp[:,:12]+1j*pp[:,12:];psi=c[0];j=c[1:5]
 bg=model.background(pos);pt=T.tensor(pos)
 def back(q):
  dx=q[120:]-pt
  terms=[]
  for alpha in model.idx:
   term=T.ones(())
   for mu,n in enumerate(alpha):
    for _ in range(n):term=term*dx[mu]
   terms.append(term)
  mon=T.stack(terms)
  return mon.to(T.complex128)@bg
 def pieces(q):
  ps=m.unpack(q[:24])[0];js=m.unpack(q[24:120]);b=back(q);cov=js+1j*T.einsum('mij,j->mi',b[1:].reshape(4,12,12),ps)
  E=T.einsum('i,aij,mj->am',ps.conj(),model.Q,cov).real;V=T.linalg.inv(E)
  f=1j*T.einsum('ma,aij,mj->i',V.to(T.complex128),model.K,cov)-b[0].real*(model.Y@ps)
  return ps,js,b,V,T.cat((f.real,f.imag))
 def F(q):return pieces(q)[4]
 DF=T.func.jacrev(F)
 def g(q):
  ps,js,b,V,f=pieces(q);return 4-.5*b[0].real*T.vdot(ps,Z@ps).real
 Dg=T.func.jacrev(g)
 def R(q):
  ps,js,b,V,f=pieces(q);D=DF(q)
  aa=T.einsum('i,aij->aj',ps.conj(),model.Q);A=T.cat((aa.real,-aa.imag),dim=1)
  K=T.einsum('ai,mij->maj',A,T.einsum('ma,aij->mij',V,Hb))
  bmu=T.stack([D[:,120+mu]+D[:,:24]@T.cat((js[mu].real,js[mu].imag)) for mu in range(4)])
  G=T.einsum('mai,mi->a',K,bmu);gg=Dg(q)
  dg=T.stack([gg[120+mu]+gg[:24]@T.cat((js[mu].real,js[mu].imag)) for mu in range(4)])
  return T.cat((f,G,dg))
 q=T.tensor(np.r_[m.pack(psi),m.pack(j),pos]);rr=R(q).detach().numpy();D=T.func.jacrev(R)(q).detach().numpy();J=D[:,24:120]
 U,sv,Vh=np.linalg.svd(J,full_matrices=True);rank=int(sum(sv>sv[0]*1e-9));N=Vh[rank:].T
 A2=np.zeros((128,240))
 for pn,(mu,nu) in enumerate(pairs):
  A2[mu*32:(mu+1)*32,pn*24:(pn+1)*24]=J[:,nu*24:(nu+1)*24]
  if mu!=nu:A2[nu*32:(nu+1)*32,pn*24:(pn+1)*24]=J[:,mu*24:(mu+1)*24]
 ss=np.linalg.svd(A2,compute_uv=False);r2=int(sum(ss>ss[0]*1e-9));g1=96-rank;g2=240-r2
 flags=[];rng=np.random.default_rng(301026)
 for trial in range(4):
  flag=np.eye(4) if trial==0 else np.linalg.qr(rng.normal(size=(4,4)))[0]
  evals=[];ranks=[]
  for mu in range(4):
   block=sum((flag[nu,mu]*N[nu*24:(nu+1)*24] for nu in range(4)),np.zeros((24,N.shape[1])))
   evals.append(block);svv=np.linalg.svd(np.vstack(evals),compute_uv=False);ranks.append(int(sum(svv>svv[0]*1e-9)))
  chars=np.diff([0]+ranks).tolist();bound=sum((i+1)*v for i,v in enumerate(chars))
  flags.append({'characters':chars,'Cartan_bound':bound,'g2_dimension':g2,'equality':bound==g2})
 triples=list(itertools.combinations_with_replacement(range(4),3));A3=np.zeros((320,480))
 for pn,alpha in enumerate(pairs):
  for mu in range(4):
   col=triples.index(tuple(sorted((*alpha,mu))))
   A3[pn*32:(pn+1)*32,col*24:(col+1)*24]+=J[:,mu*24:(mu+1)*24]
 s3=np.linalg.svd(A3,compute_uv=False);rank3=int(sum(s3>s3[0]*1e-9));g3=480-rank3
 u2,s2,v2=np.linalg.svd(A2,full_matrices=True);N2=v2[r2:].T;flags2=[]
 for trial in range(4):
  flag=np.eye(4) if trial==0 else np.linalg.qr(rng.normal(size=(4,4)))[0];ev=[];evrank=[]
  for k in range(4):
   block=np.vstack([sum((flag[mu,k]*N2[pairs.index(tuple(sorted((mu,nu))))*24:(pairs.index(tuple(sorted((mu,nu))))+1)*24] for mu in range(4)),np.zeros((24,N2.shape[1]))) for nu in range(4)])
   ev.append(block);sx=np.linalg.svd(np.vstack(ev),compute_uv=False);evrank.append(int(sum(sx>sx[0]*1e-9)))
  chars=np.diff([0]+evrank).tolist();bound=sum((k+1)*v for k,v in enumerate(chars));flags2.append({'characters':chars,'Cartan_bound':bound,'g3_dimension':g3,'equality':bound==g3})
 # Test first prolongation of completed constraints at the same lower germ.
 source=np.concatenate([D[:,120+mu]+D[:,:24]@m.pack(j[mu]) for mu in range(4)])
 sol,_,pr,_=np.linalg.lstsq(A2,-source,rcond=1e-9);res=A2@sol+source
 rows.append({'point_index':row['point_index'],'R_norm':float(np.linalg.norm(rr)),'first_symbol_rank':rank,'first_symbol_singular_values':sv.tolist(),'g1_dimension':g1,'second_symbol_rank':r2,'g2_dimension':g2,'flags':flags,'third_symbol_rank':rank3,'g3_dimension':g3,'prolonged_flags':flags2,'completed_prolongation_residual':float(np.linalg.norm(res)),'source_norm':float(np.linalg.norm(source))})
 print(rows[-1],flush=True)
 (ROOT/'completed-tableau-result.json').write_text(json.dumps({'contract':'Finite numerical tableau of R=(F24,G4,dg4) at fixedpsi satisfyingg0; symmetric2jet completion and4flagcharacterchecks. No constant-rank analyticneighborhood or existencecertification.','seconds':time.time()-tic,'results':rows},indent=2))
