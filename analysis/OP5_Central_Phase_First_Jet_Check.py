from pathlib import Path
import json,numpy as np
source=Path(__file__).with_name('OP5_Sector_Traceless_Check.py').read_text()
prefix=source.split('\nout=[]')[0]
exec(prefix)
body=source.split('for pt in points:\n',1)[1].split(' summaries={}')[0]
# Preserve original matrix assembly; replace only evaluator with cached analytic lambdas.
cache={}
def value(mat,pos):
 key=s.ImmutableMatrix(mat)
 if key not in cache:cache[key]=s.lambdify((t,x,y,z),key,modules='numpy',cse=True)
 return s.Matrix(cache[key](*pos))
body=body.replace(' ev=lambda m:s.Matrix(m).subs(pt).evalf(30)',' ev=lambda m:value(m,pos)')
tail="""
 Mt=M@Zt
 P=np.eye(24)-Mt@np.linalg.pinv(Mt,rcond=1e-12)
 Central=np.zeros((20,4))
 for mu in range(4):Central[5*mu:5*mu+3,mu]=1
 return P@M@Central,-P@pack(res)
"""
exec('def evaluate(pos):\n pt=dict(zip((t,x,y,z),pos))\n'+body+tail)
pairs=[(i,j) for i in range(4) for j in range(i,4)]
def run(pos,h,symmetric):
 F,b=evaluate(pos)
 deriv=[tuple((vp-vm)/(2*h) for vp,vm in zip(evaluate(pos+np.eye(4)[k]*h),evaluate(pos-np.eye(4)[k]*h))) for k in range(4)]
 entries=pairs if symmetric else [(i,j) for i in range(4) for j in range(4)]
 A=np.zeros((120,4+len(entries)));rhs=np.zeros(120)
 A[:24,:4]=F;rhs[:24]=b
 for k,(dF,db) in enumerate(deriv):
  rows=slice(24*(k+1),24*(k+2))
  A[rows,:4]=dF;rhs[rows]=db
  for j,(a,bb) in enumerate(entries):
   if bb==k:A[rows,4+j]+=F[:,a]
   if symmetric and a==k and bb!=a:A[rows,4+j]+=F[:,bb]
 coef,_,rank,sv=np.linalg.lstsq(A,rhs,rcond=1e-5)
 rem=A@coef-rhs
 return {'symmetric':symmetric,'step':h,'rank':int(rank),'singular_values':sv.tolist(),'residual_norm':float(np.linalg.norm(rem)),'rhs_norm':float(np.linalg.norm(rhs)),'coefficients':coef.tolist()}
out=[]
for pos in [np.array([1.,.6,0,0]),np.array([1.,.4,.2,.2])]:
 checks=[run(pos,h,sy) for h in [1e-3,5e-4,2.5e-4] for sy in [False,True]]
 out.append({'point':pos.tolist(),'checks':checks})
 print(json.dumps({'point':pos.tolist(),'checks':[{k:v for k,v in ch.items() if k not in ['coefficients','singular_values']} for ch in checks]}),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
