from pathlib import Path
import sympy as s,json
a,b,w,t,tau=s.symbols('a b omega t tau',positive=True,real=True)
def rho(rate,time):return s.Matrix([[1,s.exp(-s.I*w*rate*time)],[s.exp(s.I*w*rate*time),1]])/2
synced=(rho(a,tau/a)-rho(b,tau/b)).applyfunc(s.simplify);assert synced==s.zeros(2)
unsynced=(rho(a,t)-rho(b,t)).diff(t).subs(t,0).applyfunc(s.simplify);assert unsynced!=s.zeros(2)
v=s.symbols('v',real=True);gp=s.diag((2-v)**2,(1-2*v)**2);gm=s.diag((2+v)**2,(1+2*v)**2);orientation=((gp/s.trace(gp))-(gm/s.trace(gm))).diff(v).subs(v,0);assert orientation==s.diag(s.Rational(24,25),-s.Rational(24,25))
out={'same_initial_clock_reading_only_velocity_difference':str(unsynced),'after_positive_rate_calibration':str(synced),'common_tau_orientation_velocity_difference_per_dv_dtau':str(orientation),'scope':'Exact constant positive clock rates and common initial phase. No native QSC clock or global GR synchronization derived.'};Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(out)
