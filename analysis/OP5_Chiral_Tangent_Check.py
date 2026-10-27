from pathlib import Path
import json
import numpy as np
src=Path(__file__).with_name('OP5_Counterflow_Full_Residual_Check.py')
exec(src.read_text(encoding='utf-8-sig').split('results=[]')[0])
u=s.symbols('u0:3',real=True); gu=1/s.sqrt(1-sum(k*k for k in u)); au=s.sqrt((gu+1)/2)
Bu=au*(s.eye(4)+gu/(gu+1)*sum((u[j]*al[j] for j in range(3)),s.zeros(4)))/s.sqrt(gu)
dBu=[Bu.diff(ui) for ui in u]
g5=s.zeros(2).row_join(s.eye(2)).col_join(s.eye(2).row_join(s.zeros(2)))
Pmat=I*beta*g5
arr=lambda m:np.array(m.tolist(),dtype=complex)
real=lambda w:np.concatenate([w.real,w.imag])
results=[]
for pt in points:
 ev=lambda m:s.Matrix(m).subs(pt).evalf(30)
 fs=[ev(f) for f in fields]; psi=s.Matrix.vstack(*fs)
 kin=[I*ev(ds[0])+sum((I*al[k]*ev(ds[k+1]) for k in range(3)),s.zeros(4,1)) for ds in derivs]
 V=sum((s.kronecker_product(ev(G)*s.sympify(spin[k]).subs(pt),al[k]) for k in range(3)),s.zeros(12))+s.kronecker_product(Y,beta)*hm.subs(pt).evalf(30)
 vel=arr(I*(s.Matrix.vstack(*kin)-V*psi)).reshape(-1)
 internal=[]; boosts=[]; probes=[]
 for k in range(3):
  sign=1 if k<2 else -1
  uv={u[j]:sign*v[j].subs(pt) for j in range(3)}
  B=Bu.subs(uv).evalf(30)
  chi=ev(chip if k<2 else chim); rest=s.Matrix.vstack(chi,s.zeros(2,1))
  f=arr(fs[k]).reshape(-1); amplitude=np.linalg.norm(f)
  intlocal=[]
  for j in range(2):
   base=arr(B[:,j]).reshape(-1)
   for phase in [1,1j]:
    col=np.zeros(12,complex);col[4*k:4*k+4]=phase*base;internal.append(col);intlocal.append(phase*base)
  local=[]
  for j in range(3):
   vec=amplitude*arr(dBu[j].subs(uv).evalf(30)*rest).reshape(-1)
   col=np.zeros(12,complex);col[4*k:4*k+4]=vec;boosts.append(col);local.append(vec)
  w=vel[4*k:4*k+4]
  pm=arr(Pmat);ps=float(np.vdot(f,pm@f).real);der=float(2*np.vdot(f,pm@w).real)
  tangent=np.stack([real(a) for a in intlocal+local],axis=1)
  coef,_,rank,sv=np.linalg.lstsq(tangent,real(w),rcond=1e-12)
  remain=real(w)-tangent@coef
  pred=der**2/(4*np.linalg.norm(pm@f)**2)
  assert abs(np.dot(remain,remain)-pred)<1e-8
  probes.append({'probe':'ABC'[k],'rank':int(rank),'pseudoscalar':ps,'required_pseudoscalar_rate':der,'outside_all_boost_spin_phase_norm2':float(remain@remain),'pseudoscalar_predicted_norm2':pred})
 def fit(cols):
  M=np.stack([real(col) for col in cols],axis=1);w=real(vel)
  co,_,rank,sv=np.linalg.lstsq(M,w,rcond=1e-12);rvec=w-M@co
  assert np.linalg.norm(M.T@rvec)<1e-8
  return {'rank':int(rank),'residual_norm2':float(rvec@rvec),'remaining_percent_total':float(100*(rvec@rvec)/(w@w)),'singular_values':sv.tolist()}
 chiral=[]; rates=[]
 for k in range(3):
  f=arr(fs[k]).reshape(-1); col=np.zeros(12,complex); col[4*k:4*k+4]=.5j*arr(g5)@f; chiral.append(col)
  scalar=float(np.vdot(f,arr(beta)@f).real)
  rates.append(-probes[k]['required_pseudoscalar_rate']/scalar)
 pattern=chiral[0]+chiral[1]-chiral[2]
 assert abs(rates[0]-rates[1])<1e-10 and abs(rates[0]+rates[2])<1e-10
 cases={'fixed_boost_internal_only':fit(internal),'independent_boosts':fit(internal+boosts),'shared_AB_separate_C':fit(internal+[boosts[j]+boosts[3+j] for j in range(3)]+boosts[6:]),'shared_AB_opposite_C':fit(internal+[boosts[j]+boosts[3+j]-boosts[6+j] for j in range(3)])}
 cases['independent_boosts_plus_chiral_pattern']=fit(internal+boosts+[pattern])
 cases['counterflow_boosts_plus_chiral_pattern']=fit(internal+[boosts[j]+boosts[3+j]-boosts[6+j] for j in range(3)]+[pattern])
 assert cases['independent_boosts_plus_chiral_pattern']['residual_norm2']<1e-20
 results.append({'chiral_rates':rates,'point':{str(k):str(val) for k,val in pt.items()},'probes':probes,'cases':cases})
 print(json.dumps(results[-1]),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(results,indent=2))
print('PASS: boost plus one triadic chiral tangent fits sampled residual; constrained counterflow comparison retained')
