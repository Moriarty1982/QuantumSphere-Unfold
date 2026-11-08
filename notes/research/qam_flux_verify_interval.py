"""Enclose the fixed pulse's grid amplitudes using mpmath interval arithmetic."""
from pathlib import Path

from mpmath import iv


def wrong_amplitude(controls, label, offset):
    z = label + offset
    left, right = iv.mpc(1), iv.mpc(0)
    for x, y in controls:
        rate = iv.sqrt(x*x + y*y + z*z)
        diagonal = iv.cos(rate / 2)
        scale = -iv.j * iv.sin(rate / 2) / rate
        left, right = (
            (diagonal + scale*z)*left + scale*(x - iv.j*y)*right,
            scale*(x + iv.j*y)*left + (diagonal - scale*z)*right,
        )
    return abs(left if abs(label) == 3 else right)


def main():
    iv.dps = 40
    table = Path(__file__).with_name("qam_flux_robust_controls.txt")
    controls = [tuple(map(iv.mpf, line.split())) for line in table.read_text().splitlines()]
    ceiling = iv.mpf("0.001297")
    for label in (-3, -1, 1, 2, 3):
        for step in range(-50, 51):
            amplitude = wrong_amplitude(controls, label, iv.mpf(step) / 1000)
            if not amplitude.b < ceiling.a:
                raise ArithmeticError(f"Grid ceiling not verified at {label=}, {step=}")
    duration = iv.mpf(len(controls)) / 2
    interval_error = (ceiling + duration**2 / 8_000_000)**2
    if not interval_error.b < iv.mpf("0.00000173").a:
        raise ArithmeticError("Interval ceiling not verified")
    print("505 grid amplitudes enclosed; interval wrong probability < 1.73e-6")


if __name__ == "__main__":
    main()
