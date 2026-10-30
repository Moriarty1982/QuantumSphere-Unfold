"""Finite polynomial neighbourhood and order4-to5 movement checks; no new fit."""
from pathlib import Path
import json,importlib.util,numpy as np,hashlib
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('probe_model',ROOT/'recursive_calibrator.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
model=m.TaylorModel(5)
newpath=ROOT/'recursive-order-5-result.json';oldpath=ROOT/'recursive-order-4-result.json'
new=json.loads(newpath.read_text());old=json.loads(oldpath.read_text());rows=[]
if len(new['results'])!=3:raise RuntimeError('Require complete three-point run')
directions=[*np.eye(4),np.array([1.,.2,-.3,.4]),np.array([-.3,.7,.2,-.4])]
directions=[d/np.linalg.norm(d) for d in directions]
def coeffs(row):
 v=np.array(row['coefficients_real_imag']);return v[:,:12]+1j*v[:,12:]
for row,prior in zip(new['results'],old['results']):
 pos=np.array(row['point']);idx=[tuple(a) for a in row['multiindices']];c=coeffs(row);oldidx={tuple(a):v for a,v in zip(prior['multiindices'],coeffs(prior))}
 delta=np.array([v-oldidx.get(a,np.zeros(12,complex)) for a,v in zip(idx,c)])
 def evaluate(dx):
  ps=sum((v*np.prod(dx**np.array(a)) for a,v in zip(idx,c)),np.zeros(12,complex));j=[]
  for mu in range(4):
   acc=np.zeros(12,complex)
   for a,v in zip(idx,c):
    if a[mu]:
     b=np.array(a);b[mu]-=1;acc+=v*a[mu]*np.prod(dx**b)
   j.append(acc)
  bg=model.background(pos+dx).numpy()[0];cov=np.array(j)+1j*np.einsum('mij,j->mi',bg[1:].reshape(4,12,12),ps)
  E=np.einsum('i,aij,mj->am',ps.conj(),model.Q.numpy(),cov).real;inv=np.linalg.inv(E)
  F=1j*np.einsum('ma,aij,mj->i',inv,model.K.numpy(),cov)-bg[0].real*(model.Y.numpy()@ps)
  g00=float(inv[0]@np.diag([-1,1,1,1])@inv[0]);return float(np.linalg.norm(F)),float(np.linalg.det(E)),g00
 probes=[]
 for radius in [.02,.01,.005,.0025]:
  values=[evaluate(sign*radius*d) for d in directions for sign in [-1,1]]
  bound=float(sum(np.linalg.norm(v)*radius**sum(a) for a,v in zip(idx,delta)))
  probes.append({'radius':radius,'max_full_F_norm':max(v[0] for v in values),'min_abs_detE':min(abs(v[1]) for v in values),'max_g00':max(v[2] for v in values),'sampled_displacements':len(values),'polynomial_difference_cube_bound':bound})
 changes={}
 for d in [2,3,4]:
  ids=[n for n,a in enumerate(idx) if sum(a)==d];fac=np.array([m.factorial(idx[n]) for n in ids]);oldraw=np.array([oldidx[idx[n]] for n in ids])*fac[:,None]
  rawdiff=delta[ids]*fac[:,None]
  changes[str(d)]={'raw_change':float(np.linalg.norm(rawdiff)),'relative_raw_change':float(np.linalg.norm(rawdiff)/np.linalg.norm(oldraw)),'coefficient_change':float(np.linalg.norm(delta[ids]))}
 rows.append({'point_index':row['point_index'],'degree_changes':changes,'probes':probes,'zero_and_first_coefficients_unchanged':bool(all(np.array_equal(v,oldidx[a]) for a,v in zip(idx,c) if sum(a)<=1))})
 print(rows[-1],flush=True)
out={'contract':'Actual original field residual on degree5 Taylor polynomial at12 displacements per radius, exact background, no fitting; finite neighbourhood samples and analytic polynomial-difference bound on coordinate cube only, not uniform PDE bounds.','inputs_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [newpath,oldpath,Path(__file__),ROOT/'recursive_calibrator.py',model.source]},'results':rows}
(ROOT/'fifth-local-probe-result.json').write_text(json.dumps(out,indent=2))
