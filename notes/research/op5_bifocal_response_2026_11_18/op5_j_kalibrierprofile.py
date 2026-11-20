"""Generate bounded OP5 calibration profiles from real split-map spectra."""

import argparse
from fractions import Fraction
import json
from pathlib import Path

SPECTRA = ("p_12", "p_1g", "p_1b", "p_b2", "p_bg", "p_bb")


def spectrum_values(values, *, complete):
    unknown = set(values) - set(SPECTRA)
    missing = set(SPECTRA) - set(values) if complete else set()
    if unknown or missing:
        raise ValueError(f"unknown spectra {sorted(unknown)}, missing spectra {sorted(missing)}")
    return {name: Fraction(values.get(name, 0)) for name in SPECTRA}


def build_profiles(bins):
    """Evaluate nominal responses, linear profiles and uniform remainder bounds."""
    output = []
    expected_modes = None
    for row in bins:
        x = Fraction(row["x"])
        if x < 0 or (output and x <= Fraction(output[-1]["x"])):
            raise ValueError("x must be nonnegative and strictly increasing")
        try:
            result = calibrate_bin(row)
        except ValueError as error:
            raise ValueError(f"x={x}: {error}") from error
        modes = set(result["profiles"])
        if expected_modes is not None and modes != expected_modes:
            raise ValueError(f"x={x}: supply the same named modes in all bins")
        expected_modes = modes
        output.append({"x": x, **result})
    if not output:
        raise ValueError("at least one bin is required")
    return output


def calibrate_bin(row):
    p = spectrum_values(row["spectra"], complete=True)
    modes = {
        name: spectrum_values(change, complete=False)
        for name, change in row["modes"].items()
    }
    bounds = {key: sum(abs(mode[key]) for mode in modes.values()) for key in SPECTRA}
    if p["p_bb"] <= bounds["p_bb"]:
        raise ValueError("tracer autospectrum can reach zero")

    numerator = p["p_12"] * p["p_bb"] - p["p_1b"] * p["p_b2"]
    denominator = p["p_1g"] * p["p_bb"] - p["p_1b"] * p["p_bg"]
    if denominator == 0:
        raise ValueError("nominal partial cross-spectrum can reach zero")
    response = numerator / denominator
    profiles = {}
    linear_denominator_bound = 0
    for name, delta in modes.items():
        delta_n = (
            delta["p_12"] * p["p_bb"] + p["p_12"] * delta["p_bb"]
            - delta["p_1b"] * p["p_b2"] - p["p_1b"] * delta["p_b2"]
        )
        delta_d = (
            delta["p_1g"] * p["p_bb"] + p["p_1g"] * delta["p_bb"]
            - delta["p_1b"] * p["p_bg"] - p["p_1b"] * delta["p_bg"]
        )
        profiles[name] = (delta_n - response * delta_d) / denominator
        linear_denominator_bound += abs(delta_d)

    quadratic_n = bounds["p_12"] * bounds["p_bb"] + bounds["p_1b"] * bounds["p_b2"]
    quadratic_d = bounds["p_1g"] * bounds["p_bb"] + bounds["p_1b"] * bounds["p_bg"]
    delta_d_bound = linear_denominator_bound + quadratic_d
    denominator_margin = abs(denominator) - delta_d_bound
    if denominator_margin <= 0:
        raise ValueError("partial cross-spectrum is not bounded away from zero")
    remainder = (
        quadratic_n + abs(response) * quadratic_d
        + sum(map(abs, profiles.values())) * delta_d_bound
    ) / denominator_margin
    return {
        "response": response,
        "profiles": profiles,
        "nonlinear_remainder": remainder,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON object with a bins array")
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"), parse_float=Fraction)
        result = build_profiles(data["bins"])
    except (KeyError, TypeError, ValueError, ZeroDivisionError) as error:
        parser.error(str(error))
    print(json.dumps({"bins": result}, default=str, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
