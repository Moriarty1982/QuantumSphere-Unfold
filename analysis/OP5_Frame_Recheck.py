"""Bounded OP5 frame diagnostics; run through the computation-audit runner.

No infinite zero-sum error certificate or physical Lambda identification.
The finite spectral sample uses independently generated mpmath zeros.
"""
import argparse
import json
import platform
from pathlib import Path

import mpmath as mp
import sympy as sp


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--zeros-from")
    args = parser.parse_args()
    mp.mp.dps = 35
    zeros = ([mp.mpf(z) for z in json.loads(Path(args.zeros_from).read_text(encoding="utf-8"))["zeros"]]
             if args.zeros_from else [mp.im(mp.zetazero(k)) for k in range(1, 129)])
    g = mp.mpf("0.2375") / (mp.log(2) / (mp.pi * mp.sqrt(3)))
    beta2 = (g - 1) / (g + 1)
    eta = mp.atanh(mp.sqrt(beta2))
    scale = mp.exp(eta)

    def integral(factor, length, n=128):
        return 2 * mp.fsum(mp.sin(length * factor * z) / (factor * z) for z in zeros[:n])

    def accelerated(factor, length, n):
        # Conditional infinite interpretation: all zeros critical-line and
        # symmetric summation; N terms in two absolutely convergent remainders.
        a = length * factor
        assert 0 < a < mp.log(2)
        f = mp.exp(a) - mp.log(2 * mp.pi) - mp.log(1 - mp.exp(-2*a))/2
        z = zeros[:n]
        return (mp.exp(-a/2)*f
                - mp.fsum(mp.cos(a*t)/(mp.mpf(".25")+t*t) for t in z)
                + mp.fsum(mp.sin(a*t)/(2*t*(mp.mpf(".25")+t*t)) for t in z))/factor

    cases = []
    for name, freqbase, cutoffbase in (("historical_A_A", g, g),
                                      ("replace_frequency_only_C_A", scale, g),
                                      ("replace_cutoff_only_A_C", g, scale),
                                      ("replace_both_C_C", scale, scale)):
        length = cutoffbase**(-mp.mpf("1.5"))
        freqfactor = 1/freqbase
        rhs = mp.mpf("1.5")*length - mp.log(length) - length**2/24 - mp.euler - beta2*length**2
        row = {"case": name, "frequency_factor": freqfactor, "length": length,
               "phase_length": freqfactor*length, "legacy_rhs": rhs,
               "finite_sum_128": integral(freqfactor, length)}
        for n in (64,128):
            value = accelerated(freqfactor, length, n)
            row[f"accelerated_{n}"] = value
            row[f"legacy_defect_{n}"] = value-rhs
        cases.append(row)

    # Exact finite-sum covariance, with unrelated finite scales as controls.
    base_length = mp.mpf(".21")
    base = integral(1, base_length)
    covariance = []
    for a in (mp.mpf(".5"), 1/g, 1/scale, mp.mpf(2)):
        err = abs(a*integral(a, base_length/a)-base)
        assert err < mp.mpf("1e-30")
        covariance.append({"frequency_factor":a,"phase_preserving_length":base_length/a,"absolute_error":err})

    t = sp.symbols("t", positive=True)
    old_r = -sp.exp(-t/2)/(sp.exp(t)-1)
    corrected = sp.exp(t/2)-sp.exp(-t/2)/(sp.exp(2*t)-1)
    old_series = sp.series(old_r,t,0,3)
    corrected_series = sp.series(corrected,t,0,3)
    assert sp.limit(t*old_r,t,0,dir="+") == -1
    assert sp.limit(t*corrected,t,0,dir="+") == -sp.Rational(1,2)
    u=sp.exp(t/2)
    primitive=2*u-2/u+sp.log((u+1)/(u-1))/2-sp.atan(u)
    assert sp.simplify(sp.diff(primitive,t)-corrected) == 0

    # Corrected prime-free smooth density: this is NOT the unsmeared
    # infinite ordinate-only trace without an RH/model assumption.
    def density(x):
        return mp.exp(x/2)-mp.exp(-x/2)/mp.expm1(2*x)

    lo=mp.mpf(".08"); hi=mp.mpf(".2")
    bump=lambda x:(x-lo)**2*(hi-x)**2
    pairing=mp.quad(lambda x:density(x)*bump(x),[lo,hi])
    a=1/scale
    pulled_pairing=mp.quad(lambda u:density(a*u)*bump(a*u),[lo/a,hi/a])
    assert abs(a*pulled_pairing-pairing)<mp.mpf("1e-30")

    # Endpoint finite part at arbitrary declared subtraction scale mu=1.
    # Integrate from delta then use the analytic small-x series below delta.
    def fp(length):
        delta=mp.mpf("1e-6")
        regular_integral=(mp.mpf(7)*delta/4+delta**2/96+3*delta**3/32
                          +mp.quad(lambda x:density(x)+1/(2*x),[delta,length]))
        return regular_integral-mp.log(length)/2

    def fp_closed(length):
        u=mp.exp(length/2)
        return 2*u-2/u+mp.log((u+1)/(u-1))/2-mp.atan(u)-mp.log(2)+mp.pi/4

    spectral_constant=(mp.log(2*mp.pi)+mp.euler)/2
    conditional_spectral=[]
    for row in cases:
        phase=row["phase_length"]
        j=fp_closed(phase)
        assert abs(j-fp(phase)) < mp.mpf("1e-24")
        spectral=(j-spectral_constant)/row["frequency_factor"]
        conditional_spectral.append({"case":row["case"],"closed_form_spectral_value":spectral,
                                     "legacy_rhs":row["legacy_rhs"],
                                     "legacy_defect":spectral-row["legacy_rhs"],
                                     "quadrature_check_error":abs(j-fp(phase))})

    # A freely chosen scale is a fitted, different cutoff problem, NOT the
    # covariant transport of a fixed observable. Retain this positive control
    # rather than claiming that no alternative numerical scale can give a root.
    def free_scale_defect(h):
        length=h**(-mp.mpf("1.5"))
        spectral=h*(fp_closed(length/h)-spectral_constant)
        target=mp.mpf("1.5")*length-mp.log(length)-length**2/24-mp.euler-beta2*length**2
        return spectral-target
    fitted_scale=mp.findroot(free_scale_defect,(mp.mpf(3),mp.mpf(4)))
    assert abs(free_scale_defect(fitted_scale))<mp.mpf("1e-30")
    with mp.workdps(55):
        check_g=mp.mpf(".2375")/(mp.log(2)/(mp.pi*mp.sqrt(3)))
        check_q=(check_g-1)/(check_g+1)
        check_L=check_g**(-mp.mpf("1.5"))
        reference=check_g*(fp_closed(check_L/check_g)-(mp.log(2*mp.pi)+mp.euler)/2)
        precision_delta=abs(reference-conditional_spectral[0]["closed_form_spectral_value"])
        assert precision_delta<mp.mpf("1e-30")

    corrected_cases=[]
    for name,freqbase,cutbase in (("historical_cutoff",g,g),("new_scale_cutoff",scale,scale)):
        length=cutbase**(-mp.mpf("1.5"))
        factor=1/freqbase
        # Pull back BOTH M and Z; keep physical subtraction scale transformed.
        # F'_mu' = F_1(factor*length)/factor with mu'=1/factor.
        value=fp(factor*length)/factor
        corrected_cases.append({"case":name,"frequency_factor":factor,"length":length,
                                "subtraction_scale":1/factor,"finite_part":value,
                                "unjustified_old_target_for_comparison_only":beta2*length**2})

    result={"assertion_tested":"128-zero finite covariance, four declared factor substitutions, symbolic endpoint residues and one smooth prime-free pairing",
            "software":{"python":platform.python_version(),"mpmath":mp.__version__,"sympy":sp.__version__},
            "precision_decimal_digits":mp.mp.dps,"gL":g,"beta_squared":beta2,"eta":eta,"scale_exp_eta":scale,
            "zeros":zeros,"cases":cases,"finite_covariance":covariance,
            "old_R_series":str(old_series),"corrected_density_series":str(corrected_series),
            "compact_pairing":{"support":[lo,hi],"base":pairing,"pulled":pulled_pairing,"factor":a},
            "conditional_spectral_constant":spectral_constant,
            "conditional_closed_form_cases":conditional_spectral,
            "closed_form_precision_check_35_vs_55":precision_delta,
            "free_scale_fit_not_a_frame_solution":{"fixed_beta_squared":beta2,"fitted_scale":fitted_scale,
                   "bracket_defects":[free_scale_defect(mp.mpf(3)),free_scale_defect(mp.mpf(4))],
                   "residual":free_scale_defect(fitted_scale),
                   "interpretation":"Free scale changes the phase/cutoff and holds an untransported target fixed. Numerical fit, not a derived frame transition or physical closure."},
            "corrected_finite_part_cases":corrected_cases,
            "non_claims":["No certified infinite tail bound","No physical target or action derived",
                          "No OP5 closure","Factor substitutions are diagnostics, not a passive frame derivation",
                          "Finite-part subtraction scale is declared, not fixed by physical theory"]}
    dest=Path(args.output)
    dest.write_text(json.dumps(result,indent=2,default=lambda v:mp.nstr(v,32)),encoding="utf-8")
    print(json.dumps({k:result[k] for k in ("gL","scale_exp_eta","cases","finite_covariance","old_R_series","corrected_density_series","corrected_finite_part_cases","conditional_closed_form_cases")},indent=2,default=lambda v:mp.nstr(v,15)))


if __name__ == "__main__":
    main()
