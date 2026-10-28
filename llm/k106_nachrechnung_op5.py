# Unabhaengige Nachrechnung ausgewaehlter OP5-Aussagen (analysis/, 3fa5ba9..337d9cb)
import sympy as sp
t,x,y,z=sp.symbols('t x y z',real=True)
out={}
# 1) Regularisierung: R(t) = -e^{-t/2}/(e^t-1)
R=-sp.exp(-t/2)/(sp.exp(t)-1)
out['R_series']=str(sp.series(R,t,0,4).removeO())
# 2) Ward-No-Go: b+3tb'=1, (h b^2)'=0, h=(b+1/3)/t
b=sp.Function('b')(t)
h=(b+sp.Rational(1,3))/t
expr=sp.diff(h*b**2,t).subs(sp.diff(b,t),(1-b)/(3*t))
out['ward_factor']=str(sp.factor(sp.simplify(expr)))
out['ward_roots']=[str(r) for r in sp.solve(9*sp.Symbol('B')**2-2*sp.Symbol('B')-1,sp.Symbol('B'))]
# 3) Torsions-Zeuge: E=dt,dx_i; j=(2t,0,0,0); omega^i_0=omega^0_i=dx_i/t
X=[t,x,y,z]; eta=sp.diag(-1,1,1,1)
# connection 1-forms omega[a][b] as coefficient vectors over dX
om=[[[0]*4 for _ in range(4)] for _ in range(4)]
for i in (1,2,3):
    om[i][0][i]=1/t; om[0][i][i]=1/t
E=[[1 if a==m else 0 for m in range(4)] for a in range(4)]
j=[2*t,0,0,0]
Dj=[[sp.diff(j[a],X[m])+sum(om[a][c][m]*j[c] for c in range(4)) for m in range(4)] for a in range(4)]
out['E_eq_half_Dj']=all(sp.simplify(Dj[a][m]/2-E[a][m])==0 for a in range(4) for m in range(4))
def wedge2(f,g): # 1-forms -> 2-form components [m][n]
    return [[f[m]*g[n]-f[n]*g[m] for n in range(4)] for m in range(4)]
def d1(f): return [[sp.diff(f[n],X[m])-sp.diff(f[m],X[n]) for n in range(4)] for m in range(4)]
Tor=[]
for a in range(4):
    T=d1(E[a])
    for c in range(4):
        w=wedge2(om[a][c],E[c]); T=[[T[m][n]+w[m][n] for n in range(4)] for m in range(4)]
    Tor.append(T)
Rc=[[None]*4 for _ in range(4)]
for a in range(4):
    for c in range(4):
        Rm=d1(om[a][c])
        for e in range(4):
            w=wedge2(om[a][e],om[e][c]); Rm=[[Rm[m][n]+w[m][n] for n in range(4)] for m in range(4)]
        Rc[a][c]=Rm
ok=True
for a in range(4):
    for m in range(4):
        for n in range(4):
            if sp.simplify(Tor[a][m][n]-sum(Rc[a][c][m][n]*j[c] for c in range(4))/2)!=0: ok=False
out['T_eq_half_Rj']=ok
out['T1_tx']=str(sp.simplify(Tor[1][0][1]))
# 4) Zwei-Sonden-Austausch: R_B Koeffizient auf der Zeitachse, g=8
g=8; d=sp.cos(16*t); f=1-sp.Rational(3,4)*sp.sin(8*t)**2; hh=1-sp.Rational(6,g)
RB=sp.cos(8*t)*(g*hh/d+6/f-g)
out['RB_series']=str(sp.series(RB,t,0,5).removeO())
out['v_series']=str(sp.series(d/f,t,0,3).removeO())
# 5) Zwei komplexe Sonden: Spur-Hindernis e_a^mu E^a_mu = 4 vs 0 -> Residuum 8 (aus Skript), hier E=diag(3,-1,-1,-1)
Em=sp.diag(3,-1,-1,-1); out['g_two_probes']=str(Em.T*eta*Em)
# 6) Neutraler Mittelpunkt: Mischung rho und sigma_y rho sigma_y
bz,bx=sp.symbols('bz bx',real=True)
sx=sp.Matrix([[0,1],[1,0]]); sy=sp.Matrix([[0,-sp.I],[sp.I,0]]); sz=sp.diag(1,-1)
rho=(sp.eye(2)+bz*sz+bx*sx)/2
out['mix_sigma_y']=str(sp.simplify((rho+sy*rho*sy)/2))
out['mix_sigma_x']=str(sp.simplify((rho+sx*rho*sx)/2))
# 7) q_rel = tanh^2(eta) = (cosh2eta-1)/(cosh2eta+1)
e=sp.symbols('eta',positive=True)
out['qrel_identity']=sp.simplify(sp.tanh(e)**2-(sp.cosh(2*e)-1)/(sp.cosh(2*e)+1))==0
# 8) Vergleichspotential V=M^4 tanh^2(chi/2) bei historischer Trennung tanh^2(chi/2)=beta^2
import mpmath as mp
mp.mp.dps=30
beta2=mp.mpf('0.301783497976057'); beta=mp.sqrt(beta2)
out['Vprime_over_M4']=mp.nstr(beta*(1-beta2),8)
# 9) Regularisierter Wert: lim [int_eps^T (1+R) dtau - log eps], T=0.393, mu=1
T=mp.mpf('0.393')
Rf=lambda u: -mp.e**(-u/2)/(mp.e**u-1)
out['pv_korrekt_T0393']=mp.nstr(mp.quad(lambda u:1+Rf(u)+1/u,[0,T])-mp.log(T),10)
out['pv_gedruckt_T0393']=mp.nstr(3*T/2-mp.log(T)-T**2/24-mp.euler,10)
for k,v in out.items(): print(f"{k}: {v}")
