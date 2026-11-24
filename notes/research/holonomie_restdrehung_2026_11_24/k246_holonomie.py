"""k246. Erkundung (nicht blind): Restdrehung der Drei-Sektor-Scheibe als Holonomie.
Modelle: A feste Radien/Massen, B Wanderwelle radial+tangential, C Bogenmassen m_i ~ l_i^2."""
import sympy as sp, numpy as np
from scipy.integrate import solve_ivp
print("== Modell A: Punkte auf festem Kreis, feste Massen ==")
th=sp.symbols('th1:4'); mm=sp.symbols('m1:4',positive=True)
A=[mi/sum(mm) for mi in mm]   # A = sum m_i dth_i / M, Koeffizienten konstant
F=[[sp.diff(A[j],th[i])-sp.diff(A[i],th[j]) for j in range(3)] for i in range(3)]
print("Kruemmung dA (alle Komponenten):",set(sp.simplify(x) for r in F for x in r))
print("== Modell B: r_i=R(1+a cos(d+2pi i/3)), th_i=phi+2pi i/3+b sin(d+2pi i/3), J=0 ==")
a,b,d=sp.symbols('a b delta',real=True)
c=[sp.cos(d+2*sp.pi*i/3) for i in range(3)]
r2=[(1+a*ci)**2 for ci in c]
I=sp.simplify(sp.expand_trig(sum(r2)))
N=sp.simplify(sp.expand_trig(sum(r2[i]*c[i] for i in range(3))))
print("Sum r^2 =",I,"  Sum r^2 cos =",N)
dphi=-b*N/I
hol=sp.simplify(sp.integrate(sp.expand_trig(dphi),(d,0,2*sp.pi)))
print("Holonomie je Zyklus Delta phi =",hol)
k=sp.simplify(hol/(-2*sp.pi*b)); print("Kopplung k(a)=",k," Maximum bei a=",sp.solve(sp.diff(k,a),a)," k_max=",sp.simplify(k.subs(a,sp.sqrt(2))))
K=sp.simplify(sum(r2)/sum(1+a*ci for ci in c)**2); print("Koide K(a)=",sp.simplify(sp.expand_trig(K)),"  K(sqrt2)=",sp.simplify(sp.expand_trig(K.subs(a,sp.sqrt(2)))))
# numerische Kontrolle: J=0 direkt integrieren
for av,bv in [(np.sqrt(2),0.1),(0.5,0.3),(np.sqrt(2),1.0)]:
    def f(t,y):
        cc=np.cos(t+2*np.pi*np.arange(3)/3); rr=(1+av*cc)**2
        return [-bv*np.sum(rr*cc)/np.sum(rr)]
    s=solve_ivp(f,(0,2*np.pi),[0.0],rtol=1e-12,atol=1e-14)
    print(f"  numerisch a={av:.4f} b={bv}: {s.y[0][-1]:.10f}  exakt {-2*np.pi*bv*av/(1+av**2/2):.10f}")
print("== Modell C: Bogenmassen m_i=l_i^2 im Bogenmittelpunkt, fester Radius ==")
l1,l2=sp.symbols('l1 l2',positive=True); L=2*sp.pi; l3=L-l1-l2
m=[l1**2,l2**2,l3**2]; M=sum(m); g=[l1/2,l1+l2/2,l1+l2+l3/2]; w=[x/M for x in m]
Fc=sp.simplify(sum(sp.diff(w[i],l1)*sp.diff(g[i],l2)-sp.diff(w[i],l2)*sp.diff(g[i],l1) for i in range(3)))
print("F(l1,l2) =",sp.factor(Fc))
print("F bei gleichen Boegen:",sp.simplify(Fc.subs({l1:L/3,l2:L/3})))
q=4+3*sp.sqrt(2)  # Koide-Boegen q:1:1 aus op3_string_length (2026-11-12)
Lk=[L*q/(q+2),L/(q+2)]
print("F am Koide-Punkt (q:1:1):",sp.N(Fc.subs({l1:Lk[0],l2:Lk[1]})))
# Gesamtfluss numerisch (die symbolische sympy-Integration lieferte -1.2589, falsch; Wolfram und Randintegral geben -pi)
from scipy.integrate import dblquad
Ff=sp.lambdify((l1,l2),Fc)
v,e=dblquad(lambda y,x:Ff(x,y),0,2*np.pi,0,lambda x:2*np.pi-x,epsabs=1e-12,epsrel=1e-12)
print("Gesamtfluss ueber Formsimplex (numerisch):",v," -pi =",-np.pi)
# Normierte Formflaeche einer Schleife und Holonomie: kleine Kreisschleife um gleiche Boegen
eps=sp.symbols('eps',positive=True)
print("Kleine Schleife um Gleichverteilung: Holonomie = F*Flaeche =",sp.simplify(Fc.subs({l1:L/3,l2:L/3}))," * pi eps^2")
print("== Vergleichszahlen ==")
gM=0.237533; print("gamma_M =",gM," gamma_M/2 =",gM/2," ΔΦ Daten 0.118724")
