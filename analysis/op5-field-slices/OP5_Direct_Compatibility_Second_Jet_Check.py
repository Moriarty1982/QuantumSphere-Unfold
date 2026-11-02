from pathlib import Path
import numpy as np,sympy as s,json
src=Path(__file__).resolve().parents[1] / 'OP5_Counterflow_Full_Residual_Check.py'
exec(src.read_text(encoding='utf-8-sig').split('results=[]')[0])
K=np.array([np.eye(4)]+[np.array(a,complex) for a in al]); QQ=np.array([np.kron(np.array(S,complex),k) for k in K]); YY=np.kron(np.array(Y,complex),np.array(beta,complex)); KK=[np.kron(np.eye(3),k) for k in K]
back=s.lambdify((t,x,y,z),(G,hm,s.Matrix(spin)),modules='numpy',cse=True)
pack=lambda a:np.r_[a.real.ravel(),a.imag.ravel()]
def unpack(a):return (a[:48]+1j*a[48:]).reshape(4,12)
def residual(pos,psi,jets):
 gg,hh,ss=back(*pos); ss=np.asarray(ss).ravel()
 cov=jets.copy()
 for mu in range(1,4):cov[mu]+=1j*np.kron(np.asarray(gg)*ss[mu-1],np.eye(4))@psi
 E=np.array([[np.vdot(psi,Q@cov[mu]).real for mu in range(4)] for Q in QQ]); inv=np.linalg.inv(E)
 return pack(sum((1j*sum(inv[mu,a]*KK[a] for a in range(4))@cov[mu] for mu in range(4)),np.zeros(12,complex))-float(hh)*YY@psi)
data=json.loads(Path('OP5_Direct_Compatibility_Lower_Data.json').read_text()); rows=[]
for ip,row in enumerate(data['results']):
 pos=np.array([float(s.sympify(row['point'][str(k)])) for k in (t,x,y,z)])
 sub=dict(zip((t,x,y,z),pos));psi=np.concatenate([np.array(f.subs(sub).evalf(),complex).ravel() for f in fields])
 psi=np.array([complex(*v) for v in row['field_values_real_imag']])
 for ia,attempt in enumerate(row['attempts']):
  jets=np.array([complex(*v) for v in attempt['all_jets']]).reshape(4,12); v0=pack(jets); tests=[]
  for h in [1e-4,1e-5,1e-6]:
   J=np.column_stack([(residual(pos,psi,unpack(v0+np.eye(96)[i]*h))-residual(pos,psi,unpack(v0-np.eye(96)[i]*h)))/(2*h) for i in range(96)])
   b=np.concatenate([(residual(pos+np.eye(4)[k]*h,psi+h*jets[k],jets)-residual(pos-np.eye(4)[k]*h,psi-h*jets[k],jets))/(2*h) for k in range(4)])
   A=np.zeros((96,240));pairs=[(i,j) for i in range(4) for j in range(i,4)]
   for pidx,(i,j) in enumerate(pairs):
    for zidx in range(24):
     comp=zidx%12;imag=zidx//12; col=pidx*24+zidx
     A[i*24:(i+1)*24,col]=J[:,imag*48+j*12+comp]
     if i!=j:A[j*24:(j+1)*24,col]=J[:,imag*48+i*12+comp]
   sol,_,rank,sv=np.linalg.lstsq(A,-b,rcond=1e-9)
   Au=np.kron(np.eye(4),J); zu,_,ru,_=np.linalg.lstsq(Au,-b,rcond=1e-9)
   tests.append({'step':h,'unrestricted_second_rank':int(ru),'unrestricted_second_residual':float(np.linalg.norm(Au@zu+b)),'rank':int(rank),'source_norm':float(np.linalg.norm(b)),'residual_norm':float(np.linalg.norm(A@sol+b)),'second_jet_norm':float(np.linalg.norm(sol)),'singular_values':sv.tolist(),'symmetric_second_jets':sol.tolist()})
  rows.append({'point_index':ip,'attempt':ia,'lower_residual':float(np.linalg.norm(residual(pos,psi,jets))),'tests':tests})
result={'contract':'Fixed field values and fitted first jets; free symmetric second derivatives (240 real); differentiated full spinor equation (96 real), including position-dependent original couplings and induced coframe. Numerical central differences, not regional existence.','results':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
print([(r['point_index'],r['attempt'],[(v['step'],v['rank'],v['residual_norm']) for v in r['tests']]) for r in rows])
