from pathlib import Path
import sympy as s,json
T,w,a,b=s.symbols('t omega a b',real=True);I=s.I;sigz=s.diag(1,-1);rho=s.Matrix([[1,1],[1,1]])/2;clock0=s.diag(1,0);clock1=s.diag(0,1);H=s.kronecker_product(s.diag(a,b),w*sigz/2)
def ptrace_clock(M):return M[:2,:2]+M[2:,2:]
full0=s.kronecker_product(clock0,rho);full1=s.kronecker_product(clock1,rho);assert ptrace_clock(full0)==ptrace_clock(full1)
vel0=ptrace_clock(-I*(H*full0-full0*H));vel1=ptrace_clock(-I*(H*full1-full1*H));assert vel0!=vel1
v=s.symbols('v',real=True);gp=s.diag((2-v)**2,(1-2*v)**2);gm=s.diag((2+v)**2,(1+2*v)**2);rp=gp/s.trace(gp);rm=gm/s.trace(gm);vp=rp.diff(v).subs(v,0);vm=rm.diff(v).subs(v,0);assert rp.subs(v,0)==rm.subs(v,0);assert vp==-vm and vp!=s.zeros(2)
# Closed mediator records rate and orientation; suppressing them loses autonomy.
out={'clock_controlled_example':{'same_reduced_initial_state':str(rho),'same_full_Hamiltonian':str(H),'first_velocity':str(vel0),'second_velocity':str(vel1),'difference':str(s.simplify(vel0-vel1))},'native_Gram_observer_example':{'full_fields':'E=(2,0,0), B_plus=(0,1,0), B_minus=(0,-1,0)','common_initial_Gram_state':str(rp.subs(v,0)),'derivative_wrt_common_boost_speed_plus':str(vp),'derivative_minus':str(vm),'invariants':'E^2-B^2=3, E dot B=0 in both cases'},'scope':'Exact finite controlled examples. Clock Hamiltonian is a comparison choice, not the derived native QSC dynamics. Observer change is not physical time evolution of a closed qubit.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(out)
