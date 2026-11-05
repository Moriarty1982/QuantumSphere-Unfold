"""k188: Test der Vorab-Notiz H74 (Commit b24bb08). Normaler Schwinger phi gekoppelt an Schwinger chi mit F3-Vorzeichen (Geist), linear eps*phi*chi.
Kontrolle: zwei normale Schwinger. RK4, dt = 1e-3, T = 400."""
import numpy as np, json
def run(w1s,w2s,eps,ghost,T=400.0,dt=1e-3):
    sg=-1 if ghost else 1
    # ghost: chi'' = -w2^2 chi - eps*phi ; normal: chi'' = -w2^2 chi + eps*phi
    def f(y):
        p,c,pv,cv=y;return np.array([pv,cv,-w1s*p+eps*c,-w2s*c+sg*eps*p])
    def energy(y):
        p,c,pv,cv=y;Ep=.5*pv*pv+.5*w1s*p*p;Ec=.5*cv*cv+.5*w2s*c*c;return Ep-Ec-eps*p*c if ghost else Ep+Ec-eps*p*c
    y=np.array([1e-3,0,0,0.]);E0=energy(y);n=int(T/dt);amp=[];ts=[]
    for i in range(n):
        k1=f(y);k2=f(y+dt/2*k1);k3=f(y+dt/2*k2);k4=f(y+dt*k3);y=y+dt/6*(k1+2*k2+2*k3+k4)
        if i%200==0: amp.append(abs(y[0]));ts.append((i+1)*dt)
        if abs(y[0])>1e3: break
    amp=np.array(amp);ts=np.array(ts);grow=amp.max()/1e-3
    rate=np.nan
    if grow>1e2:
        # Rate aus Einhuellender: log max in Fenstern
        W=max(5,len(ts)//20);env=[(ts[j],np.log(max(amp[j:j+W]))) for j in range(0,len(ts)-W,W)];x,yv=np.array(env).T;rate=np.polyfit(x[len(x)//2:],yv[len(x)//2:],1)[0]
    dE=abs(energy(y)-E0)/max(abs(E0),1e-30) if grow<1e5 else np.nan
    return dict(wachstum=float(grow),rate=float(rate),dE_rel=float(dE))
out={}
for eps in (1e-3,1e-2,1e-1): out[f'a gleich eps={eps}']=dict(run(1,1,eps,True),erwartet=eps/2)
for eps in (0.02,0.04,0.06,0.1): out[f'b verstimmt eps={eps}']=run(1,1.1,eps,True)
for eps in (1e-3,1e-1,0.4): out[f'c normal eps={eps}']=run(1,1,eps,False)
json.dump(out,open('k188_out.json','w'),indent=1,default=float)
for k,v in out.items(): print(f"{k:22s}",' '.join(f'{a}={b:.3g}' for a,b in v.items()))
