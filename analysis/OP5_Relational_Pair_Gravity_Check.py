"""Conditional symmetric scalar pair and vacuum-level ambiguity controls.

No claim that the comparison potential is the native QSC action. All
dimensional coefficients and the potential shape are declared inputs.
"""
import argparse
import json
import platform
from pathlib import Path

import mpmath as mp
import sympy as s


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",required=True)
    args=p.parse_args()
    eta1,eta2,N,chi,shift=s.symbols("eta1 eta2 N chi shift",real=True)
    f,lam,G,A=s.symbols("f lam G A",positive=True)
    C=s.symbols("C",real=True)
    U=C+lam*f**4*(s.cosh(eta1-eta2)-G)**2
    rel=U.subs({eta1:N+chi/2,eta2:N-chi/2},simultaneous=True)
    assert s.simplify(s.diff(rel,N))==0
    assert s.simplify(rel-rel.subs(chi,-chi))==0
    assert s.simplify(U-U.subs({eta1:eta1+shift,eta2:eta2+shift},simultaneous=True))==0
    assert s.diff(s.diff(rel,chi),C)==0
    grad=s.diff(rel,chi)
    hessian=s.hessian(U,(eta1,eta2))
    # Assume G>1 explicitly for the real, nonzero pair branch.
    xstar=s.acosh(G)
    hstar=s.simplify(hessian.subs({eta1:xstar/2,eta2:-xstar/2}))
    c0=2*lam*f**4*(G**2-1)
    assert s.simplify(hstar-c0*s.Matrix([[1,-1],[-1,1]]))==s.zeros(2)
    assert s.simplify(hstar*s.Matrix([1,1]))==s.zeros(2,1)
    assert s.simplify(hstar*s.Matrix([1,-1])-2*c0*s.Matrix([1,-1]))==s.zeros(2,1)
    # Original kinetic term is -f²/2 sum_i (partial eta_i)².
    # Consequently the normalized relative mass squared is 2*c0/f².
    mass2=4*lam*f**2*(G**2-1)
    assert s.simplify(2*c0/f**2-mass2)==0
    assert s.simplify(rel.subs(chi,xstar)-C)==0
    assert s.simplify(grad.subs(chi,xstar))==0
    assert s.simplify(grad.subs(chi,0))==0
    origin_curvature=s.simplify(s.diff(rel,chi,2).subs(chi,0))
    assert s.simplify(origin_curvature-2*lam*f**4*(1-G))==0

    # Opposite bilinear mass signs do NOT imply opposite determinant weights.
    tau,q=s.symbols("tau q",positive=True)
    assert s.simplify(s.exp(-tau*q)+s.exp(tau*q)-2*s.cosh(tau*q))==0
    signed_difference=s.simplify(s.exp(-tau*q)-s.exp(tau*q))
    kernel_series=s.series(2*s.cosh(tau*q),tau,0,5)

    # A volume-independent reference subtraction does not cancel the metric
    # volume response; a local volume counterterm does and changes the theory.
    volume,volume0,rho=s.symbols("volume volume0 rho",real=True)
    S=-rho*volume
    assert s.diff(S-S.subs(volume,volume0),volume)==-rho
    assert s.diff(S+rho*volume,volume)==0

    mp.mp.dps=45
    g=mp.mpf(".2375")/(mp.log(2)/(mp.pi*mp.sqrt(3)))
    chi0=mp.acosh(g)
    q0=mp.tanh(chi0/2)**2
    cases=[]
    for center in (mp.mpf(-2),mp.mpf(0),mp.mpf(".8")):
        for vacuum in (mp.mpf(-1),mp.mpf(0),mp.mpf(1)):
            left=center+chi0/2; right=center-chi0/2
            d=left-right
            slope=2*(mp.cosh(d)-g)*mp.sinh(d)
            energy=vacuum+(mp.cosh(d)-g)**2
            assert abs(slope)<mp.mpf("1e-40")
            assert abs(energy-vacuum)<mp.mpf("1e-40")
            # Comparison A=1/2,f=1,lambda=1 in unspecified mass units.
            cases.append({"neutral_center":center,"vacuum_offset":vacuum,
                          "eta1":left,"eta2":right,"relative_q":mp.tanh(d/2)**2,
                          "potential_gradient":slope,"vacuum_density":energy,
                          "Lambda_cos":energy,"Einstein_space_R":4*energy,
                          "relative_mass_squared":4*(g*g-1),
                          "center_mass_squared":0})

    result={"assertion_tested":"Conditional exchange/common-shift-invariant doubled-scalar minima, Hessian, nine constant-background Einstein families and additive vacuum ambiguity",
            "software":{"python":platform.python_version(),"mpmath":mp.__version__,"sympy":s.__version__},
            "model":"S=int sqrt(-g)[A R-f²/2 sum_i(partial eta_i)²-C-lambda f^4(cosh(eta1-eta2)-G)^2], A,f,lambda>0,G>1",
            "symbolic":{"U_N_chi":str(rel),"dU_dchi":str(grad),"minimum_pair_hessian":str(hstar),
                        "relative_mass_squared":str(mass2),"origin_second_derivative":str(origin_curvature),
                        "Lambda_cos_at_minimum":"C/(2A)","curvature_R_at_minimum":"2C/A",
                        "same_weight_opposite_mass_heat_series":str(kernel_series),
                        "opposite_weight_difference":str(signed_difference)},
            "historical_parameter":{"G":g,"chi_star":chi0,"relative_q":q0},
            "finite_backgrounds":cases,
            "non_claims":["Potential shape is a constructed matching penalty, not a derived native action",
                          "G is an input comparison datum, not independently predicted",
                          "Scalar scale line is not the native complex tachyon sector or a proved spacetime map",
                          "Stable relative scalar mass is a local tree-level check, not full quantum/global stability",
                          "Vacuum offset C remains independent input; no small Lambda prediction",
                          "Negative bilinear squared-mass example is not assigned a native determinant"]}
    Path(args.output).write_text(json.dumps(result,indent=2,default=lambda z:mp.nstr(z,35)),encoding="utf-8")
    print(json.dumps(result,indent=2,default=lambda z:mp.nstr(z,16)))


if __name__=="__main__":
    main()
