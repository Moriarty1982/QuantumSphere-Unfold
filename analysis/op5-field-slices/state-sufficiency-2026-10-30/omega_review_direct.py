"""Direct one-variable AD crosscheck of completed R coefficient series; no fitting."""
from pathlib import Path
import json,textwrap,hashlib,time,numpy as np,torch as T
ROOT=Path(__file__).resolve().parent;path=ROOT/'completion_omega_probe.py';text=path.read_text();tic=time.time()
prefix=text.split("for row in data['results'][:1]:")[0].replace('model=m.TaylorModel(3)','model=m.TaylorModel(5)').replace('ext=m.TaylorModel(5)','ext=model')
ns={'__file__':str(path)};exec(prefix,ns);ns['row']=ns['data']['results'][0]
body=text.split("for row in data['results'][:1]:")[1]
exec(textwrap.dedent(body.split(' q0=T.tensor')[0]),ns)
ext=ns['ext'];row=ns['row'];pos=ns['pos'];R=ns['R'];base=np.zeros((len(ext.fullidx),12),complex)
for alpha,value in zip(row['multiindices'],ns['c']):
    if sum(alpha)<=3:base[ext.full[tuple(alpha)]]=value
ns['bgx']=ext.background(pos)
definition=' def completed_coeff(full):'+body.split(' def completed_coeff(full):')[1].split(' def source(z):')[0]
exec(textwrap.dedent(definition),ns);series=ns['completed_coeff'](T.tensor(base)).detach().numpy()
rows=[]
for direction in [np.array([1.,0.,0.,0.]),np.array([1.,.2,-.3,.4])]:
    psi=np.zeros((4,12),complex);jets=np.zeros((4,4,12),complex)
    for alpha,value in zip(ext.fullidx,base):
        d=sum(alpha)
        if d<=3:psi[d]+=value*np.prod(direction**np.array(alpha))
    for alpha in ext.idx:
        d=sum(alpha)
        if d>3:continue
        weight=np.prod(direction**np.array(alpha))
        for mu in range(4):
            beta=list(alpha);beta[mu]+=1;jets[d,mu]+=(alpha[mu]+1)*base[ext.full[tuple(beta)]]*weight
    psi=T.tensor(psi);jets=T.tensor(jets);v=T.tensor(direction);pt=T.tensor(pos)
    def along(lam):
        powers=[T.ones(())]
        for _ in range(3):powers.append(powers[-1]*lam)
        ps=sum((powers[d]*psi[d] for d in range(4)),T.zeros(12,dtype=T.complex128));js=sum((powers[d]*jets[d] for d in range(4)),T.zeros((4,12),dtype=T.complex128))
        packed=T.cat((ps.real,ps.imag,T.cat((js.real,js.imag),dim=1).ravel(),pt+lam*v))
        return R(packed)
    zero=T.zeros(());target=np.zeros((4,32))
    for n,alpha in enumerate(ext.idx):
        if sum(alpha)<=3:target[sum(alpha)]+=series[n]*np.prod(direction**np.array(alpha))
    errors=[];current=along
    for degree in range(4):
        val=current(zero).detach().numpy()/np.math.factorial(degree) if hasattr(np,'math') else None
        if val is None:
            import math
            val=current(zero).detach().numpy()/math.factorial(degree)
        errors.append(float(np.linalg.norm(val-target[degree])))
        if degree<3:current=T.func.jacrev(current)
    rows.append({'direction':direction.tolist(),'coefficient_difference_degrees0to3':errors,'target_coefficient_norms':[float(np.linalg.norm(v)) for v in target]});print(rows[-1],flush=True)
inputs=[Path(__file__),path,ROOT/'recursive_calibrator.py',ROOT/'fifth-window-result.json',ext.source]
out={'contract':'Independent 1D automatic derivatives of declared pointwise R versus completed coefficient series throughdegree3. Backgroundthrough4, spinor polynomialthrough3, highest4/5zero. Two directions, no fitting orOmegaSVD rerun.','seconds':time.time()-tic,'inputs_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},'results':rows}
(ROOT/'omega_review_direct_result.json').write_text(json.dumps(out,indent=2))
