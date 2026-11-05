"""k177 (Erkundung): M-T-Paar mit Frame-Gewichten p_+ (M) und p_- (T) nach Konvention F, flach, Delta omega * delta = pi.
Gewichte: P (1/2, 1/2), M (1/(1+x), x/(1+x)) mit x = beta_sym^2, T (vertauscht). Gemessen: Strombilanz (K), Energierest,
dessen raeumliches Mittel und Spur (Lambda-artig waere T ~ g, Spur != 0)."""
import numpy as np, importlib.util, io, contextlib
spec=importlib.util.spec_from_file_location('k','k175_test_h69.py');k=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(k)
x=0.5493**2;dw=k.w1-k.w2;delta=np.pi/dw;Lz=2*np.pi/(k.w1+k.w2);eta=np.diag([1.,-1,-1,-1])
for name,(pp,pm) in {'P (1/2,1/2)':(0.5,0.5),'M':(1/(1+x),x/(1+x)),'T':(x/(1+x),1/(1+x))}.items():
    J=[];Tr=[];Tm=[]
    for z in np.arange(64)*Lz/64:
        X=np.array([0.3,0.,0.,z]);pM,dM,pT,dT=k.MT(X,delta)
        J.append(pp*k.cur(pM)-pm*k.cur(pT));Tr.append(pp*k.Tmn(pM,dM)-pm*k.Tmn(pT,dT));Tm.append(np.abs(k.Tmn(pM,dM)).max())
    J=np.array(J);Tr=np.array(Tr);m=Tr.mean(0)
    print(f'{name:12s} p+-p- = {pp-pm:+.4f} | max|j_ges| = {np.abs(J).max():.3e} | max|T_rest|/|T^M| = {np.abs(Tr).max()/max(Tm):.3e} | Mittel T_rest: tt={m[0,0]:+.3f} zz={m[3,3]:+.3f} xx={m[1,1]:+.3f} Spur={np.trace(eta@m):+.1e}')
print('Vergleich: |b| = 1/gamma = (1-x)/(1+x) =',round((1-x)/(1+x),4))
