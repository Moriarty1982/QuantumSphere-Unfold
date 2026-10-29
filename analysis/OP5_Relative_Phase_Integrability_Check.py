from pathlib import Path
import numpy as np,json
src=Path(__file__).with_name('OP5_Counterflow_Full_Residual_Check.py')
exec(src.read_text(encoding='utf-8-sig').split('results=[]')[0])
g5=s.zeros(2).row_join(s.eye(2)).col_join(s.eye(2).row_join(s.zeros(2)))
# No finite differences of spinor derivatives needed: gate uses field values.
fun=s.lambdify((t,x,y,z),[U,W,c,d,th.diff(t),hm,d*p-c*q]+spin,modules='numpy',cse=True)
K=[np.eye(4)]+[np.array(a.tolist(),complex) for a in al]
bm=np.array(beta.tolist(),complex)
pack=lambda v:np.r_[v.real,v.imag]
def evaluate(pos):
 vals=fun(*pos)
 uu=np.asarray(vals[0],complex).reshape(-1);ww=np.asarray(vals[1],complex).reshape(-1)
 cv,dv,q0,h,kap=map(float,vals[2:7]);spinvec=np.array(vals[7:],float)
 als=sum(spinvec[j]*K[j+1] for j in range(3))
 b0=q0*uu-h*bm@uu-1j*kap*als@ww
 M=np.column_stack([pack(1j*k@uu) for k in K])
 l,_,rank,sv=np.linalg.lstsq(M,-pack(b0),rcond=1e-12)
 error=np.linalg.norm(pack(b0)+M@l)
 return {'l':l,'relative':l/(cv*dv),'A':-dv/cv*l,'B':cv/dv*l,'fit_residual':error,'rank':int(rank)}
def derivative(pos,h,key):
 return np.column_stack([(evaluate(pos+np.eye(4)[j]*h)[key]-evaluate(pos-np.eye(4)[j]*h)[key])/(2*h) for j in range(4)])
out=[]
for pos in [np.array([1.,.6,0,0]),np.array([1.,.4,.2,.2]),np.array([.9,.3,.2,.1])]:
 v=evaluate(pos);checks=[]
 for hstep in [1e-3,5e-4,2.5e-4,1e-4]:
  J=derivative(pos,hstep,'relative'); curl=J.T-J
  checks.append({'step':hstep,'d_relative_phase':curl.tolist(),'max_abs':float(np.max(abs(curl)))})
 out.append({'point':pos.tolist(),'l':v['l'].tolist(),'relative_phase_covector':v['relative'].tolist(),'fit_residual':v['fit_residual'],'rank':v['rank'],'checks':checks})
 assert checks[-1]['max_abs']>1
 assert np.max(abs(np.array(checks[-1]['d_relative_phase'])-np.array(checks[-2]['d_relative_phase'])))<1e-3
 print(json.dumps(out[-1]),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
