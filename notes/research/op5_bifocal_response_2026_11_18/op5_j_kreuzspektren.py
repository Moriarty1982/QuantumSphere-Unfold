"""Build and certify synthetic OP5 split cross-spectra using exact fractions."""

import argparse
from fractions import Fraction as F
from itertools import product
import json
from math import prod

from op5_j_kalibrierprofile import build_profiles


NODES = (1, 2, 3, 4, 6, 9, 10)
POLES = (4, 9, 16)
MODES = ("gravity_gain", "split_transfer", "correlated_gravity_residual")
OMEGA = [prod(x - z for z in NODES if z != x) for x in NODES]
BASIS = [[x**k for x in NODES] for k in range(len(POLES))]
SIGMA = [F(x + 2, 3 * 10**10) for x in NODES]


def raw_spectra(x, amplitudes):
    gain, transfer, residual = amplitudes
    response = sum(F(1, x + mass_squared) for mass_squared in POLES)
    spectra = dict.fromkeys(("p_12", "p_1g", "p_1b", "p_b2", "p_bg", "p_bb"), F(0))
    for signal, tracer, noise1, noise2, other in product((-1, 1), repeat=5):
        split1 = response * (signal + tracer) + F(noise1, 5)
        split2 = (1 + transfer * F(x, 100)) * (response * (signal + tracer) + F(noise2, 7))
        gravity = (1 + gain / 100) * (signal + 3 * tracer + other)
        gravity += residual * F(x**2, 100) * signal
        spectra["p_12"] += split1 * split2 / 32
        spectra["p_1g"] += split1 * gravity / 32
        spectra["p_1b"] += split1 * tracer / 32
        spectra["p_b2"] += tracer * split2 / 32
        spectra["p_bg"] += tracer * gravity / 32
        spectra["p_bb"] += F(tracer**2, 32)
    return spectra


def input_bins(scale):
    bins = []
    for x in NODES:
        nominal = raw_spectra(x, (F(0),) * len(MODES))
        modes = {}
        for i, name in enumerate(MODES):
            injected = raw_spectra(x, tuple(scale if j == i else F(0) for j in range(len(MODES))))
            modes[name] = {key: injected[key] - nominal[key] for key in nominal}
        bins.append({"x": x, "spectra": nominal, "modes": modes})
    return bins


def gram(weights):
    return [
        [sum(w * a * b for w, a, b in zip(weights, row, col)) for col in BASIS]
        for row in BASIS
    ]


def positive_definite(matrix):
    # Leading principal minors of the symmetric 3-by-3 matrix.
    (a, b, c), (_, d, e), (_, _, f) = matrix
    determinant = a * (d * f - e**2) - b * (b * f - e * c) + c * (b * e - d * c)
    return a > 0 and a * d - b**2 > 0 and determinant > 0


def excludes_two_poles(profiles):
    for corner in product((-1, 1), repeat=len(MODES)):
        weights = []
        for row, sigma, denominator in zip(profiles, SIGMA, OMEGA):
            shifted = row["response"] + sum(sign * row["profiles"][mode] for sign, mode in zip(corner, MODES))
            width = sigma + row["nonlinear_remainder"]
            weights.append(shifted / denominator - width / abs(denominator))
        if not positive_definite(gram(weights)):
            return False
    return True


def check_injections(bins, profiles, scale):
    for raw, profile in zip(bins, profiles):
        x = raw["x"]
        response = sum(F(1, x + mass_squared) for mass_squared in POLES)
        assert profile["response"] == response
        for point in product((-1, 0, 1), repeat=len(MODES)):
            injected = raw_spectra(x, tuple(scale * sign for sign in point))
            for key, nominal in raw["spectra"].items():
                expected = nominal + sum(sign * raw["modes"][mode][key] for sign, mode in zip(point, MODES))
                assert injected[key] == expected
            p = injected
            numerator = p["p_12"] * p["p_bb"] - p["p_1b"] * p["p_b2"]
            denominator = p["p_1g"] * p["p_bb"] - p["p_1b"] * p["p_bg"]
            linear = sum(sign * profile["profiles"][mode] for sign, mode in zip(point, MODES))
            assert abs(numerator / denominator - response - linear) <= profile["nonlinear_remainder"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scale", type=F, default=F("1e-5"))
    output = parser.add_mutually_exclusive_group()
    output.add_argument("--raw", action="store_true", help="emit input for the calibration profile calculator")
    output.add_argument("--bracket", action="store_true", help="bracket the first loss of the matrix certificate")
    args = parser.parse_args()
    if not 0 <= args.scale <= F(1, 2):
        parser.error("--scale must lie in [0, 1/2]")

    if args.bracket:
        lo, hi = F(0), F("1e-3")
        assert excludes_two_poles(build_profiles(input_bins(lo)))
        assert not excludes_two_poles(build_profiles(input_bins(hi)))
        for _ in range(28):
            mid = (lo + hi) / 2
            if excludes_two_poles(build_profiles(input_bins(mid))):
                lo = mid
            else:
                hi = mid
        result = {"last_certified_scale": lo, "certificate_loss_upper_bound": hi,
                  "decimal_interval": [float(lo), float(hi)]}
    else:
        bins = input_bins(args.scale)
        if args.raw:
            result = {"bins": bins}
        else:
            profiles = build_profiles(bins)
            check_injections(bins, profiles, args.scale)
            result = {"scale": args.scale, "measurement_half_widths": SIGMA, "bins": profiles,
                      "excludes_two_poles_with_linear_contact": excludes_two_poles(profiles)}
    print(json.dumps(result, default=str, indent=2))


if __name__ == "__main__":
    main()
