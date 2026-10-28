from pathlib import Path
import json, math
src=Path(__file__).with_name('OP5_Counterflow_Full_Residual_Check.py')
exec(src.read_text(encoding='utf-8-sig').split('results=[]')[0])
rows=[]
num=lambda z:complex(s.N(z,18))
dot=lambda a,b:sum(u.conjugate()*v for u,v in zip(a,b))
norm=lambda a:sum(abs(v)**2 for v in a)
for pt in points:
 ev=lambda m:s.Matrix(m).subs(pt).evalf(30)
 fs=[ev(f) for f in fields]; psi=s.Matrix.vstack(*fs)
 kin=[I*ev(ds[0])+sum((I*al[k]*ev(ds[k+1]) for k in range(3)),s.zeros(4,1)) for ds in derivs]
 V=sum((s.kronecker_product(ev(G)*s.sympify(spin[k]).subs(pt),al[k]) for k in range(3)),s.zeros(12))+s.kronecker_product(Y,beta)*hm.subs(pt).evalf(30)
 res=s.Matrix.vstack(*kin)-V*psi
 vel=I*res
 ch=[ev(chip),ev(chim)]
 detail=[]; amps=[]; total=[0.,0.,0.]
 for k in range(3):
  sign=1 if k<2 else -1
  spinindex=0 if k<2 else 1
  boost=ev(a*(s.eye(4)+sign*gam/(gam+1)*sum((v[j]*al[j] for j in range(3)),s.zeros(4))))
  basis=[]
  for j in [spinindex,1-spinindex]:
   basis.append([num(u) for u in boost*s.Matrix.vstack(ch[j],s.zeros(2,1))/s.sqrt(gam.subs(pt))])
  w=[num(u) for u in vel[4*k:4*k+4,0]]
  coeff=[dot(e,w) for e in basis]
  perp=[w[j]-sum(coeff[l]*basis[l][j] for l in range(2)) for j in range(4)]
  parts=[abs(coeff[0])**2,abs(coeff[1])**2,norm(perp)]
  assert abs(sum(parts)-norm(w))<1e-9
  total=[total[j]+parts[j] for j in range(3)]
  fvec=[num(u) for u in fs[k]]; amp=math.sqrt(norm(fvec))
  dc=(coeff[0]*ch[spinindex]+coeff[1]*ch[1-spinindex])/amp
  ds=[float(s.re(2*(ch[spinindex].conjugate().T*P*dc)[0])) for P in pa]
  detail.append({'probe':'ABC'[k],'norm2_components':parts,'percent':[100*x/sum(parts) for x in parts],'spin_bloch':[float(s.re((ch[spinindex].conjugate().T*P*ch[spinindex])[0])) for P in pa],'missing_spin_velocity':ds})
  if k<2: amps.append(coeff[0]/math.sqrt(float(N/2)))
 mix=ev(s.Matrix([c,d])); dm=s.Matrix(amps)
 bv=[float(s.re((mix.conjugate().T*P*mix)[0])) for P in pa]
 db=[float(s.re(2*(mix.conjugate().T*P*dm)[0])) for P in pa]
 rows.append({'point':{str(k):str(val) for k,val in pt.items()},'probes':detail,'total_percent':[100*x/sum(total) for x in total],'mixture_bloch':bv,'missing_mixture_velocity':db})
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2))
print(json.dumps(rows,indent=2))
