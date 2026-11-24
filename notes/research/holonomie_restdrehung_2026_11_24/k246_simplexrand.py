# k246, Teil 2: Holonomie des Simplexrandes fuer verschiedene Massengesetze und Lagen
import numpy as np
from scipy.integrate import quad
P=2*np.pi
def hol(p):
    # Randintegral der Formverbindung A=sum w_i dg_i, w_i=l_i^p/sum, Massen in Bogenmitte
    def A(l1,l2,dx,dy):
        l3=P-l1-l2; m=np.array([l1**p,l2**p,l3**p]); w=m/m.sum()
        # dg/dl1=(1/2,1,1/2), dg/dl2=(0,1/2,1/2)
        return w@np.array([.5,1,.5])*dx + w@np.array([0,.5,.5])*dy
    s=quad(lambda t:A(t,0,1,0),0,P,epsabs=1e-13,limit=200)[0]
    s+=quad(lambda t:A(P-t,t,-1,1),0,P,epsabs=1e-13,limit=200)[0]
    s+=quad(lambda t:A(0,P-t,0,-1),0,P,epsabs=1e-13,limit=200)[0]
    return s
for p in [0,0.5,1,2,3,4,10]:
    print(f"m_i ~ l_i^{p}: Holonomie des Simplexrandes = {hol(p):+.12f}  (/pi = {hol(p)/np.pi:+.8f})")
print("-- Lage der Masse im Bogen (Anteil f), p=2 --")
def hol_f(f,p=2):
    def A(l1,l2,dx,dy):
        l3=P-l1-l2; m=np.array([l1**p,l2**p,l3**p]); w=m/m.sum()
        # g1=f l1, g2=l1+f l2, g3=l1+l2+f l3
        return w@np.array([f,1,1-f])*dx + w@np.array([0,f,1-f])*dy
    s=quad(lambda t:A(t,0,1,0),0,P,limit=200)[0]+quad(lambda t:A(P-t,t,-1,1),0,P,limit=200)[0]+quad(lambda t:A(0,P-t,0,-1),0,P,limit=200)[0]
    return s
for f in [0.0,0.3,0.5,0.7,1.0]:
    print(f"f={f}: Holonomie = {hol_f(f):+.10f}  (/pi = {hol_f(f)/np.pi:+.6f})")
