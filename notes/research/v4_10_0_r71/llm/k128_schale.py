"""k128: Gilt die z-Freiheit fuer alle Loesungen R=0 am Punkt (andere erste Ableitungen, gleiches Psi), oder nur fuer diesen Keim?"""
import sys,numpy as np
exec(open('k127_symbol_frei.py').read().split("rng=np.random.default_rng(0)")[0])
def ztest_val(jv,psi,p):
    J=symbol(jv,psi,p);cov=R(jv,psi,p)[1];vz=rv(cov[3])
    return max(np.linalg.norm(J[24:,m*24:(m+1)*24]@vz) for m in range(4))
def project(jv,psi,p):
    for it in range(30):
        r=R(jv,psi,p)[0]
        if np.max(abs(r))<1e-11: break
        J=symbol(jv,psi,p);jv=jv-np.linalg.lstsq(J,r,rcond=1e-10)[0]
    return jv,np.max(abs(R(jv,psi,p)[0]))
rng=np.random.default_rng(5);Kn=np.linalg.svd(J0)[2][31:].T   # Tangentialrichtungen der Loesungsmenge
print('Ausgang: Residuum',np.max(abs(R(j0,psi0,p0)[0])),' z-Wert',ztest_val(j0,psi0,p0))
for step in [0.05,0.2,0.5]:
    jv=j0+step*Kn@rng.normal(size=Kn.shape[1])/np.sqrt(Kn.shape[1])
    jv,res=project(jv,psi0,p0)
    print(f'Schritt {step}: |Aenderung|={np.linalg.norm(jv-j0):.3f}  Residuum={res:.1e}  z-Wert={ztest_val(jv,psi0,p0):.2e}')
