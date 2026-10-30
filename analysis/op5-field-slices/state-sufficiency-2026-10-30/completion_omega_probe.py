"""Tableau/prolongation of F,G,dg, not an analytic existence certificate."""
from pathlib import Path
import importlib.util,json,numpy as np,torch as T,itertools,time
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('complete_model',ROOT/'recursive_calibrator.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
model=m.TaylorModel(3);data=json.loads((ROOT/'fifth-window-result.json').read_text());rows=[];tic=time.time()
def realmat(z):return np.block([[z.real,-z.imag],[z.imag,z.real]])
H=np.array([realmat(1j*k) for k in model.K.numpy()]);Hb=H.copy();Hb[0]*=-1;Hb=T.tensor(Hb)
Z=T.tensor(np.kron(np.diag([1,-1,0]),np.array(model.ns['beta'],complex)));pairs=list(itertools.combinations_with_replacement(range(4),2))
ext=m.TaylorModel(5)
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
 q0=T.tensor(np.r_[m.pack(psi),m.pack(j),pos]);JR=T.func.jacrev(R)(q0).detach().numpy()[:,24:120]
 def symbol(order):
  ri=m.indices(order-1)[len(m.indices(order-2)):] if order>1 else [(0,0,0,0)]
  ci=m.indices(order)[len(m.indices(order-1)):];lookup={a:n for n,a in enumerate(ci)};A=np.zeros((len(ri)*32,len(ci)*24))
  for rn,a in enumerate(ri):
   for mu in range(4):
    b=list(a);b[mu]+=1;cn=lookup[tuple(b)];A[rn*32:(rn+1)*32,cn*24:(cn+1)*24]+=(a[mu]+1)*JR[:,mu*24:(mu+1)*24]
  return A
 A3=symbol(3);u,s3,v3=np.linalg.svd(A3,full_matrices=True);rank3=int(sum(s3>s3[0]*1e-9));N3=T.tensor(v3[rank3:].T)
 A4=symbol(4);u4,s4,v4=np.linalg.svd(A4,full_matrices=False);rank4=int(sum(s4>s4[0]*1e-9));L=T.tensor(u4[:,rank4:])
 bgx=ext.background(pos);base=np.zeros((len(ext.fullidx),12),complex)
 for alpha,value in zip(row['multiindices'],c):
  if sum(alpha)<=3:base[ext.full[tuple(alpha)]]=value
 fixed=T.tensor(base);start=len(m.indices(2));end=len(m.indices(3));top4start=end;top4end=len(m.indices(4));idx3=[n for n,a in enumerate(ext.idx) if sum(a)==3]
 def completed_coeff(full):
  Fp=ext.evaluate(full,bgx);E=ext.evaluate(full,bgx,True);V0=T.linalg.inv(E[0]);delta=E-T.cat((E[:1],T.zeros_like(E[1:])))
  X=T.einsum('ij,kjl->kil',V0.to(T.complex128),delta.to(T.complex128));eye=T.cat((T.eye(4,dtype=T.complex128)[None],T.zeros((len(ext.idx)-1,4,4),dtype=T.complex128)));power=eye;series=eye
  for n in range(1,5):power=ext.conv(power,X,'kij,kjl->kil');series=series+(-1)**n*power
  V=T.einsum('kij,jl->kil',series,V0.to(T.complex128)).real
  ps=full[:len(ext.idx)];aa=T.einsum('ki,aij->kaj',ps.conj(),ext.Q);Am=T.cat((aa.real,-aa.imag),dim=2)
  bar=T.einsum('kma,aij->kmij',V,Hb);Kp=ext.conv(Am,bar,'kaj,kmji->kmai')
  def derivative(values):
   rr=[]
   for alpha in ext.idx:
    cols=[]
    for mu in range(4):
     beta=list(alpha);beta[mu]+=1
     cols.append((alpha[mu]+1)*values[ext.lookup[tuple(beta)]] if sum(alpha)<4 else T.zeros_like(values[0]))
    rr.append(T.stack(cols))
   return T.stack(rr)
  dFp=derivative(Fp);Gp=ext.conv(Kp,dFp,'kmai,kmi->ka')
  qpoly=ext.conv(ps.conj(),T.einsum('ij,kj->ki',Z,ps),'ki,ki->k').real
  gp=-.5*ext.conv(bgx[:,:1].real,qpoly[:,None],'ki,ki->k')+T.tensor([4.]+[0.]*(len(ext.idx)-1))
  Cp=derivative(gp);return T.cat((Fp,Gp,Cp),dim=1)
 def source(z):
  full=T.cat((fixed[:start],m.unpack(z),fixed[end:]));return completed_coeff(full)[idx3].flatten()
 z=T.tensor(m.pack(base[start:end]));b=source(z);db=T.func.jacrev(source)(z);gate=(L.T@db@N3).detach().numpy();ug,ss,vg=np.linalg.svd(gate,full_matrices=False)
 sol=np.linalg.lstsq(A4,-b.detach().numpy(),rcond=1e-9)[0];compat=A4@sol+b.detach().numpy();fullbase=completed_coeff(fixed).detach().numpy()
 controls=[]
 for col in [0,1,700]:
  change=T.zeros((top4end-top4start,24));change.flatten()[col]=.01
  full=T.cat((fixed[:top4start],fixed[top4start:top4end]+m.unpack(change.flatten()),fixed[top4end:]));diff=completed_coeff(full)[idx3].flatten().detach().numpy()-b.detach().numpy()
  controls.append(float(np.linalg.norm(diff-.01*A4[:,col])))
 d=N3[:,0]*.001;aff=float(T.linalg.norm(source(z+d)-b-db@d))
 direction=N3@T.tensor(vg[0]);lowidx=[n for n,a in enumerate(ext.idx) if sum(a)<=2];probe=[]
 theta=ug[:,0]@L.T.numpy()@db.detach().numpy()
 np.savez_compressed(ROOT/'completion-omega-witness.npz',third_direction=direction.detach().numpy(),ambient_left_witness=L.numpy()@ug[:,0],theta_normalized=theta,completed_first_symbol=JR)
 for eps in [.001,.01]:
  zz=z+eps*direction;allcoeff=T.cat((fixed[:start],m.unpack(zz),fixed[end:]));rr=completed_coeff(allcoeff).detach().numpy();bb=source(zz).detach().numpy();quart=np.linalg.lstsq(A4,-bb,rcond=1e-9)[0];res=A4@quart+bb
  scalar=float(ug[:,0]@L.T.numpy()@bb);corrected=zz-(scalar/ss[0])*direction;bc=source(corrected).detach().numpy();qc=np.linalg.lstsq(A4,-bc,rcond=1e-9)[0]
  probe.append({'third_coefficient_displacement':eps,'lower_completed_coefficient_norm':float(np.linalg.norm(rr[lowidx])),'lower_completed_change':float(np.linalg.norm(rr[lowidx]-fullbase[lowidx])),'best_completed_fourth_residual':float(np.linalg.norm(res)),'Omega_scalar':scalar,'expected_Omega_change':float(ss[0]*eps),'corrected_best_fourth_residual':float(np.linalg.norm(A4@qc+bc))})
 result={'contract':'One point: next completed projection obstruction derivative along209 thirdjet tangents, all lowerfield0..2 fixed. Series evaluation of R=(F,G,dg); coefficient conventions factorialnormalized. No allorder propagation proof.','symbol_A3_rank':rank3,'symbol_A4_rank':rank4,'source_compatibility_norm':float(np.linalg.norm(compat)),'gate_shape':list(gate.shape),'gate_norm':float(np.linalg.norm(gate)),'gate_singular_values':ss.tolist(),'top_column_controls':controls,'affine_thirdjet_control':aff,'R0_norm':float(np.linalg.norm(fullbase[0])),'perturbation_controls':probe,'thirdjet_direction':direction.detach().numpy().tolist(),'Omega_left_coordinate':ug[:,0].tolist()}
 print(result,flush=True);(ROOT/'completion-omega-probe-result.json').write_text(json.dumps(result,indent=2))
 augmented=[];betaidx=m.indices(3)[len(m.indices(2)):];rng=np.random.default_rng(301031)
 for order in range(3,7):
  aa=symbol(order);gammas=m.indices(order-3)[len(m.indices(order-4)):] if order>3 else [(0,0,0,0)]
  topidx=m.indices(order)[len(m.indices(order-1)):];toplookup={a:n for n,a in enumerate(topidx)};omega=np.zeros((len(gammas),len(topidx)*24))
  for gi,gamma in enumerate(gammas):
   for bi,beta in enumerate(betaidx):
    delta=tuple(a+b for a,b in zip(beta,gamma));ci=toplookup[delta]
    omega[gi,ci*24:(ci+1)*24]+=theta[bi*24:(bi+1)*24]*m.factorial(delta)/(m.factorial(beta)*m.factorial(gamma))
  matrix=np.vstack((aa,omega));uu,ssx,vvx=np.linalg.svd(matrix,full_matrices=True);rrank=int(sum(ssx>ssx[0]*1e-9));NN=vvx[rrank:].T;flags=[]
  loweridx=m.indices(order-1)[len(m.indices(order-2)):]
  for trial in range(2):
   flag=np.linalg.qr(rng.normal(size=(4,4)))[0];evals=[];ranks=[]
   for kk in range(4):
    blocks=[]
    for alpha in loweridx:
     block=np.zeros((24,NN.shape[1]))
     for mu in range(4):
      delta=list(alpha);delta[mu]+=1;ci=toplookup[tuple(delta)];block+=flag[mu,kk]*(alpha[mu]+1)*NN[ci*24:(ci+1)*24]
     blocks.append(block)
    evals.append(np.vstack(blocks));sss=np.linalg.svd(np.vstack(evals),compute_uv=False);ranks.append(int(sum(sss>sss[0]*1e-9)))
   chars=np.diff([0]+ranks).tolist();flags.append({'characters':chars,'bound_next_dimension':sum((k+1)*v for k,v in enumerate(chars))})
  augmented.append({'order':order,'rank':rrank,'dimension':NN.shape[1],'old_rank':int(np.linalg.matrix_rank(aa,tol=np.linalg.svd(aa,compute_uv=False)[0]*1e-9)),'omega_rows':len(gammas),'flags':flags})
  print('AUGMENTED',augmented[-1],flush=True)
  (ROOT/'omega-augmented-symbol-result.json').write_text(json.dumps({'contract':'Numerical mixed-order symbol afteraddingoneΩthirdordercondition; prolongedtheta withnormalizedcoeffweights. No nonlinearexistencecertificate.','results':augmented},indent=2))
