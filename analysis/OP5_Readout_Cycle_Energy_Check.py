"""Explicit readout-order/delay cycle with energy-accounted thermal collisions.

The full Bloch ball, axes, Hamiltonian, reservoir temperature and protocol are
comparison INPUTS, not native assignments of the QSC frame labels.
"""
import argparse
import json
import platform
from pathlib import Path

import sympy as s


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    I=s.I; eye=s.eye(2)
    sig=(s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1))
    H=sig[2]/2  # gap=1, hbar=1; not an absolute vacuum-energy choice.
    bath=s.diag(s.Rational(1,4),s.Rational(3,4))  # beta*gap=log3
    axes={"A":s.Matrix([s.Rational(3,5),0,s.Rational(4,5)]),
          "B":s.Matrix([0,s.Rational(4,5),s.Rational(3,5)])}
    assert all((n.dot(n)==1) for n in axes.values())
    swap=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
    c,st=s.Rational(4,5),s.Rational(3,5)
    U=c*s.eye(4)-I*st*swap
    Hfree=s.kronecker_product(H,eye)+s.kronecker_product(eye,H)
    assert (U.H*U-s.eye(4)).applyfunc(s.simplify)==s.zeros(4)
    assert swap*Hfree-Hfree*swap==s.zeros(4)

    def clean(m):
        return m.applyfunc(s.simplify)
    def state(b):
        return clean((eye+sum((b[k]*sig[k] for k in range(3)),s.zeros(2)))/2)
    def bloch(rho):
        return clean(s.Matrix([s.trace(rho*x) for x in sig]))
    def trace_b(joint):
        return clean(s.Matrix(2,2,lambda i,j:sum(joint[2*i+a,2*j+a] for a in range(2))))
    def trace_s(joint):
        return clean(s.Matrix(2,2,lambda a,b:sum(joint[2*i+a,2*i+b] for i in range(2))))
    def energy(rho):
        return s.simplify(s.trace(H*rho))
    def collision(rho):
        joint=clean(U*s.kronecker_product(rho,bath)*U.H)
        return trace_b(joint),trace_s(joint)
    def measure(rho,n):
        sn=sum((n[k]*sig[k] for k in range(3)),s.zeros(2))
        return clean((rho+sn*rho*sn)/2)
    def free(rho,phase):
        rot=s.diag(s.exp(-I*phase/2),s.exp(I*phase/2))
        return clean(rot*rho*rot.H)
    def sequence(rho,order,phase):
        stages=[rho]
        stages.append(measure(stages[-1],axes[order[0]]))
        stages.append(free(stages[-1],phase))
        stages.append(measure(stages[-1],axes[order[1]]))
        out,bout=collision(stages[-1])
        stages.append(out)
        return stages,bout

    # Affine reservoir Bloch map, obtained from a full joint unitary.
    center,bout=collision(eye/2)
    d=bloch(center)
    K=s.Matrix.hstack(*(bloch(collision(state(s.eye(3)[:,i]))[0])-d for i in range(3)))
    thermal_fixed=clean(collision(bath)[0]-bath)
    assert thermal_fixed==s.zeros(2)
    # Trace-distance contraction for this specific bath and swap angle.
    kgram=clean(K.T*K)
    assert kgram==s.diag(s.Rational(292,625),s.Rational(292,625),s.Rational(256,625))
    contraction=s.sqrt(s.Rational(292,625))
    assert bool(contraction<1)

    cases=[]
    for phase in (s.Integer(0),s.pi/2,s.pi,3*s.pi/2):
        for order in ("AB","BA"):
            rotated=clean(s.Matrix([[s.cos(phase),-s.sin(phase),0],
                                    [s.sin(phase),s.cos(phase),0],[0,0,1]]))
            first,last=axes[order[0]],axes[order[1]]
            P=clean(last*last.T*rotated*first*first.T)
            F=clean(K*P)
            bstar=clean((s.eye(3)-F).inv()*d)
            assert bool(s.simplify(bstar.dot(bstar))<=1)
            start=state(bstar)
            stages,bout=sequence(start,order,phase)
            assert clean(stages[-1]-start)==s.zeros(2)
            e=[energy(x) for x in stages]
            WA=s.simplify(e[1]-e[0])
            Wfree=s.simplify(e[2]-e[1])
            WB=s.simplify(e[3]-e[2])
            Q=s.simplify(e[4]-e[3])
            bath_gain=s.simplify(energy(bout)-energy(bath))
            assert Wfree==0
            assert s.simplify(Q+bath_gain)==0
            assert s.simplify(WA+WB+Q)==0
            # Positive work is pulse energy supplied to the system. Q is
            # operational bath-ancilla energy transfer; an outgoing ancilla
            # can carry coherence, so no unique heat/ergotropy split is claimed.
            cases.append({"order":order,"phase":str(phase),
                          "stationary_bloch_exact":[str(x) for x in bstar],
                          "stationary_bloch_numeric":[float(x) for x in bstar],
                          "energy_stages_exact":[str(x) for x in e],
                          "start_energy":float(e[0]),"work_first_readout":float(WA),
                          "work_second_readout":float(WB),"work_free":float(Wfree),
                          "total_readout_work":float(WA+WB),"reservoir_energy_to_system":float(Q),
                          "bath_energy_gain":float(bath_gain),
                          "first_law_residual_exact":str(s.simplify(WA+WB+Q)),
                          "purity_start":float(s.trace(start*start))})

    # Native-specific counterpart-axis control: opposite labelled ports have
    # identical nonselective channel, while their selected branches differ.
    test=s.Matrix([s.Rational(1,5),s.Rational(2,5),s.Rational(3,5)])
    rho=state(test)
    assert measure(rho,axes["A"])==measure(rho,-axes["A"])
    assert min(float(s.Matrix(x["stationary_bloch_numeric"]).norm()) for x in cases)>0
    bycase={(x["order"],x["phase"]):x for x in cases}
    assert bycase[("AB","pi/2")]["stationary_bloch_exact"]!=bycase[("BA","pi/2")]["stationary_bloch_exact"]
    assert bycase[("AB","pi/2")]["start_energy"]!=bycase[("BA","pi/2")]["start_energy"]

    # Conditional continuum diagnostic, NOT a pressure derived from the qubit.
    # Isotropic radiation subsystem held at constant rho_r by a dust source.
    # N=log(a/a0), H>0, Q=4 H rho_r; total stress includes the source.
    N=s.symbols("N",real=True)
    rr,rs0,Hubble=s.symbols("rho_r rho_s0 H",positive=True)
    source=(rs0+s.Rational(4,3)*rr)*s.exp(-3*N)-s.Rational(4,3)*rr
    assert s.simplify(s.diff(source,N)+3*source+4*rr)==0
    assert s.simplify(s.diff(source+rr,N)+3*(source+rr+rr/3))==0
    effective_readout_pressure=s.simplify(rr/3-4*Hubble*rr/(3*Hubble))
    assert effective_readout_pressure==-rr
    exhaustion=s.log(1+3*rs0/(4*rr))/3
    assert s.simplify(source.subs(N,exhaustion))==0

    result={"assertion_tested":"eight exact stationary readout/delay/thermal-collision cycles, full bare-energy first law and unique contraction bound",
            "software":{"python":platform.python_version(),"sympy":s.__version__},
            "inputs":{"system_H":"sigma_z/2, gap=hbar=1", "bath":"diag(1/4,3/4), beta*gap=log3",
                      "axis_A":["3/5","0","4/5"],"axis_B":["0","4/5","3/5"],
                      "swap_cos":"4/5","swap_sin":"3/5", "meter_free_H":"0 in ideal readout dilation; switching work retained"},
            "reservoir_affine_offset":str(d),"reservoir_linear_map":str(K),
            "contraction_bound_exact":str(contraction),"contraction_bound_numeric":float(contraction),
            "cases":cases,
            "conditional_cosmology_control":{
                "hypotheses":"H>0, constant positive radiation density rho_r, dust source rho_s>=0, standard GR and isotropic fluid stress with no independent Lambda or other gravitating component; pressure is NOT derived from the qubit",
                "required_injection":"Q=4 H rho_r",
                "rewritten_subsystem_effective_pressure":str(effective_readout_pressure),
                "source_density_vs_log_scale_factor":str(source),
                "positive_source_exhaustion_log_scale_factor":str(exhaustion),
                "total_acceleration_source":"rho_total+3p_total = rho_s+2rho_r > 0 while rho_s>=0",
                "interpretation":"A replenished constant subsystem can mimic p_eff=-rho in its rewritten continuity equation, yet ordinary positive-pressure source+subsystem do not accelerate in GR."},
            "non_claims":["Full Bloch-ball comparison, not a native real-disk frame assignment",
                          "Fixed reservoir state, axes, gap and timing are explicit inputs",
                          "Readout energy changes are supplied/absorbed as apparatus pulse work",
                          "Reservoir refresh and meter reset resources are not computed or declared free",
                          "Outgoing ancillas can have coherence; Q denotes energy transfer, not a proved unique thermodynamic heat/ergotropy decomposition",
                          "Repeated protocol steady state is not a spacetime vacuum with pressure=-density",
                          "No physical time, mode density, stress tensor or Lambda predicted",
                          "An additive Hamiltonian constant shifts absolute energy but not probabilities, work or heat"]}
    Path(args.output).write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))


if __name__=="__main__":
    main()
