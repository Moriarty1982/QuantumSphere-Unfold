"""Finite/symbolic controls for a relational neutral-frame interpretation.

This is a declared scalar comparison model, not a native QSC action.
It deliberately distinguishes neutral mean, mixing and vacuum stress.
"""
import argparse
import json
from pathlib import Path
import platform

import mpmath as mp
import sympy as s


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    a,b,d,w=s.symbols("a b d w",real=True)
    midpoint=(a+b)/2
    midpoint_shift=s.simplify(((a+d)+(b+d))/2-midpoint-d)
    assert midpoint_shift==0
    variance=s.factor(w*a*a+(1-w)*b*b-(w*a+(1-w)*b)**2)
    assert s.simplify(variance-w*(1-w)*(a-b)**2)==0

    x=s.symbols("x",real=True)
    potential=s.tanh(x/2)**2
    derivative=s.diff(potential,x)
    assert s.simplify(derivative-s.tanh(x/2)/s.cosh(x/2)**2)==0
    assert derivative.subs(x,0)==0
    assert s.simplify(s.diff(potential,x,2).subs(x,0))==s.Rational(1,2)
    # For finite real x, sech^2(x/2)>0, so the only stationary point is x=0.

    eta=s.diag(-1,1,1,1)
    kplus=s.Matrix([1,1,0,0]); kminus=s.Matrix([1,-1,0,0])
    tensor=kplus*kplus.T+kminus*kminus.T
    assert tensor==s.diag(2,2,0,0)
    assert s.trace(tensor*eta)==0
    # Cannot be -rho*g with nonzero rho: vacuum trace is -4 rho, streams trace0.
    v=s.symbols("v",real=True)
    boost=s.Matrix([[s.cosh(v),-s.sinh(v),0,0],[-s.sinh(v),s.cosh(v),0,0],[0,0,1,0],[0,0,0,1]])
    assert s.simplify(boost*eta*boost.T-eta)==s.zeros(4)
    rho=s.symbols("rho",real=True)
    assert s.simplify(boost*(-rho*eta)*boost.T+rho*eta)==s.zeros(4)

    # A/B comparison of opposite internal state vectors and a partial reflection.
    b1,b2=s.symbols("b1 b2",real=True)
    sx=s.Matrix([[0,1],[1,0]]); sy=s.Matrix([[0,-s.I],[s.I,0]]); sz=s.diag(1,-1)
    dm=(s.eye(2)+b1*sz+b2*sx)/2
    partial=s.simplify((dm+sx*dm*sx)/2)
    full=s.simplify((dm+sy*dm*sy)/2)
    assert partial==(s.eye(2)+b2*sx)/2
    assert full==s.eye(2)/2
    assert s.simplify(s.trace(dm*dm)-(1+b1*b1+b2*b2)/2)==0

    mp.mp.dps=45
    g=mp.mpf(".2375")/(mp.log(2)/(mp.pi*mp.sqrt(3)))
    q=(g-1)/(g+1); beta=mp.sqrt(q); rapidity=mp.atanh(beta)
    chi=2*rapidity
    q_rel=mp.tanh(chi/2)**2
    assert abs(q_rel-q)<mp.mpf("1e-40")
    sample=[]
    for common in (mp.mpf(-3),mp.mpf(0),mp.mpf(".7"),mp.mpf(4)):
        left=rapidity+common; right=-rapidity+common
        n=(left+right)/2
        rel=mp.tanh((left-right)/2)**2
        assert abs(rel-q)<mp.mpf("1e-40")
        sample.append({"common_shift":common,"neutral_midpoint":n,"relative_q":rel,
                       "mean_squared_beta_relative_to_midpoint":(mp.tanh(left-n)**2+mp.tanh(right-n)**2)/2,
                       "squared_mean_beta_relative_to_midpoint":((mp.tanh(left-n)+mp.tanh(right-n))/2)**2})

    # Dimensional distinctions, with input H0, not a derived cosmological scale.
    c=mp.mpf(299792458)
    mpc=mp.mpf("3.0856775814913673e22")
    hubble=mp.mpf("67.4")*1000/mpc
    ell=mp.mpf("1.616255e-35")
    omega=1-q
    curvature_from_fraction=3*omega*hubble*hubble/(c*c)
    planck_scaled=q/(ell*ell)
    observed=mp.mpf("1.1e-52")

    # Positive kinetic/potential scalar comparison, c=hbar=1.
    # rho=K+V, p=K-V; w=-1 only for K=0 and positive nonzero V.
    scalar_states=[]
    for kinetic in (mp.mpf(0),mp.mpf(".1"),mp.mpf(1)):
        scalar_states.append({"kinetic_in_M4_units":kinetic,"potential_in_M4_units":q,
                              "w":(kinetic-q)/(kinetic+q)})

    result={"assertion_tested":"midpoint/common-shift identity, variance identity, scalar-potential derivative, vacuum Lorentz covariance, two-beam trace and density-matrix mixture distinctions",
            "software":{"python":platform.python_version(),"sympy":s.__version__,"mpmath":mp.__version__},
            "symbolic":{"midpoint_shift_error":str(midpoint_shift),"variance":str(variance),
                        "relative_potential_derivative":str(derivative),
                        "symmetric_beam_T_contravariant":str(tensor),"beam_trace":0,
                        "partial_JB_average":str(partial),"full_duality_average":str(full)},
            "inputs":{"gBI":"0.2375","H0_km_s_Mpc":"67.4","ellP_m":ell,"comparison_Lambda_m_minus2":observed},
            "gL":g,"beta_squared":q,"eta":rapidity,"relative_chi":chi,
            "q_relative":q_rel,"neutral_samples":sample,
            "potential_slope_at_native_separation_in_M4_units":mp.tanh(chi/2)/mp.cosh(chi/2)**2,
            "scalar_comparison_equations_of_state":scalar_states,
            "dimensional_controls":{"q_over_ellP_squared_m_minus2":planck_scaled,
                                    "ratio_to_comparison_observed_Lambda":planck_scaled/observed,
                                    "OmegaLambda_candidate":omega,
                                    "Lambda_from_Omega_and_input_H0_m_minus2":curvature_from_fraction,
                                    "Lambda_ellP_squared_comparison":observed*ell*ell},
            "non_claims":["No native QSC action or spacetime map established",
                          "Real rapidity midpoint is not the native complex tachyon boost",
                          "Density-matrix mixture is not an invertible observer-frame transformation",
                          "H0 and Planck length are input scales, not derived outputs",
                          "Neutrality does not remove variance or derive vacuum pressure",
                          "No OP5 closure or physical prediction"]}
    Path(args.output).write_text(json.dumps(result,indent=2,default=lambda z:mp.nstr(z,35)),encoding="utf-8")
    print(json.dumps(result,indent=2,default=lambda z:mp.nstr(z,16)))


if __name__=="__main__":
    main()
