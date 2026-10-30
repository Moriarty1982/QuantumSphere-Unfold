"""Tableau/prolongation of F,G,dg, not an analytic existence certificate."""
from pathlib import Path
import importlib.util,json,numpy as np,torch as T,itertools,time
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('complete_model',ROOT/'recursive_calibrator.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
model=m.TaylorModel(3);data=json.loads((ROOT/'fifth-window-result.json').read_text());rows=[];tic=time.time()
def realmat(z):return np.block([[z.real,-z.imag],[z.imag,z.real]])
H=np.array([realmat(1j*k) for k in model.K.numpy()]);Hb=H.copy();Hb[0]*=-1;Hb=T.tensor(Hb)
Z=T.tensor(np.kron(np.diag([1,-1,0]),np.array(model.ns['beta'],complex)));pairs=list(itertools.combinations_with_replacement(range(4),2))
for row in data['results'][:1]:
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
 q=T.tensor(np.r_[m.pack(psi),m.pack(j),pos]);D=T.func.jacrev(R)(q).detach().numpy();J=D[:,24:120]
 previous=None;series=[];rng=np.random.default_rng(301027)
 for order in range(1,7):
  ridx=list(itertools.combinations_with_replacement(range(4),order-1));cidx=list(itertools.combinations_with_replacement(range(4),order));lookup={a:n for n,a in enumerate(cidx)}
  matrix=np.zeros((len(ridx)*32,len(cidx)*24))
  for rn,alpha in enumerate(ridx):
   for mu in range(4):
    cn=lookup[tuple(sorted((*alpha,mu)))];matrix[rn*32:(rn+1)*32,cn*24:(cn+1)*24]+=J[:,mu*24:(mu+1)*24]
  u,sv,vh=np.linalg.svd(matrix,full_matrices=True);rank=int(sum(sv>sv[0]*1e-9));N=vh[rank:].T;flags=[]
  for trial in range(2):
   flag=np.eye(4) if trial==0 else np.linalg.qr(rng.normal(size=(4,4)))[0];ev=[];ranks=[]
   for k in range(4):
    blocks=[]
    for alpha in ridx:
     block=np.zeros((24,N.shape[1]))
     for mu in range(4):
      cn=lookup[tuple(sorted((*alpha,mu)))];block+=flag[mu,k]*N[cn*24:(cn+1)*24]
     blocks.append(block)
    block=np.vstack(blocks)
    ev.append(block);ss=np.linalg.svd(np.vstack(ev),compute_uv=False);ranks.append(int(sum(ss>ss[0]*1e-9)))
   chars=np.diff([0]+ranks).tolist();flags.append({'characters':chars,'bound_next_dimension':sum((k+1)*v for k,v in enumerate(chars))})
  series.append({'symbol_order':order,'shape':list(matrix.shape),'rank':rank,'dimension':N.shape[1],'flags':flags,'gap_against_previous':None if previous is None else previous-N.shape[1]})
  previous=flags[-1]['bound_next_dimension'];print(series[-1],flush=True)
  (ROOT/'completed-symbol-tower-result.json').write_text(json.dumps({'contract':'Frozen completedfirstsymbol only, not nonlinear formalintegrability. Genericflag numerical Cartan tests atone germ.','results':series},indent=2))
