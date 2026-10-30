from pathlib import Path
import json,numpy as np,torch as T,itertools
ns={};exec(Path('OP5_Field_Residual_Diagnosis.py').read_text().split('\nbefore=')[0],ns);saved=json.loads(Path('OP5_Peak_Mixed_Check.json').read_text());ns['params'].data.copy_(T.tensor(saved['coefficients_real_imag']));old={};exec(Path('OP5_State_Second_Jet_Check.py').read_text().split('data=json.loads')[0],old)
def values(p):
 with T.no_grad():r,E,q,psi=ns['compute'](T.tensor(p[None]));psi=psi.numpy()[0];ee=E.numpy()[0]
 current=np.array([np.vdot(psi,Q@psi).real for Q in old['QQ']]);G,_,spin=old['back'](*p);G12=np.kron(np.asarray(G),np.eye(4));B=np.array([np.vdot(psi,1j*Q@G12@psi).real for Q in old['QQ']]);return ee,current,B,np.r_[0,np.asarray(spin).ravel()]
out=[]
for p in [np.array([1.,.6,0.,0.]),np.array([.99,.59,.01,-.01])]:
 E,j,B,sp=values(p);rho2=p[1]**2+p[2]**2;dphi=np.array([0,-p[2]/rho2,p[1]/rho2,0.])
 for h in [1e-4,1e-5,1e-6]:
  dj=np.empty((4,4));dE=np.empty((4,4,4))
  for mu in range(4):
   ep,jp,_,_=values(p+h*np.eye(4)[mu]);em,jm,_,_=values(p-h*np.eye(4)[mu]);dj[:,mu]=(jp-jm)/(2*h);dE[mu]=(ep-em)/(2*h)
  curl=np.array([[[dE[mu,a,nu]-dE[nu,a,mu] for nu in range(4)] for mu in range(4)] for a in range(4)])
  triple=[dphi[i]*curl[a,j,k]-dphi[j]*curl[a,i,k]+dphi[k]*curl[a,i,j] for a in range(4) for i,j,k in itertools.combinations(range(4),3)]
  out.append({'point':p.tolist(),'step':h,'coframe_current_identity_max_error':float(np.max(abs(E-(dj/2+B[:,None]*sp[None])))),'dphi_wedge_dE_max_error':float(np.max(np.abs(triple)))})
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(out)
