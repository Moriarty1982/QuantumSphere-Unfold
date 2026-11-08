"""Interval check of the full echo pointer, including finite auxiliary flips."""
from pathlib import Path

from mpmath import iv


def table(name):
    return [tuple(map(iv.mpf, line.split()))
            for line in Path(__file__).with_name(name).read_text().splitlines()]


def propagate(controls, z):
    result = iv.eye(2)
    for x, y in controls:
        rate = iv.sqrt(x*x + y*y + z*z)
        c = iv.cos(rate / 2)
        s = -iv.j * iv.sin(rate / 2) / rate
        result = iv.matrix([[c+s*z, s*(x-iv.j*y)],
                            [s*(x+iv.j*y), c-s*z]]) * result
    return result


def main():
    iv.dps = 40
    flip = table("qam_flux_common_flip_controls.txt")
    forward = table("qam_flux_robust_controls.txt")
    mirrored = [(-x, y) for x, y in reversed(forward)]
    wait = 15 * iv.pi - 44
    ceilings = tuple(map(iv.mpf, ("0.003295", "0.001898", "0.002591")))
    for label in (-3, -1, 1, 2, 3):
        target = int(abs(label) == 3)
        for step in range(-50, 51):
            z = label + iv.mpf(step) / 1000
            gate = propagate(flip, z)
            idle = iv.matrix([[iv.exp(-iv.j*z*wait), 0], [0, iv.exp(iv.j*z*wait)]])
            before = propagate(forward, z) * gate * idle * gate
            echo = gate * propagate(mirrored, z) * gate
            phase = iv.exp(-iv.j*z*wait)
            branches = [[phase * before[p, 0] * echo[a, p] for a in range(2)]
                        for p in range(2)]
            error = iv.sqrt(sum(abs(branches[p][a] - int(p == target and a == 0))**2
                                for p in range(2) for a in range(2)))
            wrong = iv.sqrt(sum(abs(v)**2 for v in branches[1-target]))
            leakage = iv.sqrt(sum(abs(branch[1])**2 for branch in branches))
            for value, ceiling in zip((error, wrong, leakage), ceilings):
                if not value.b < ceiling.a:
                    raise ArithmeticError(f"Grid ceiling failed at {label=}, {step=}")
    addition = (30 * iv.pi)**2 / 8_000_000
    bounds = (ceilings[0] + addition, (ceilings[1] + addition)**2,
              (ceilings[2] + addition)**2)
    for value, limit in zip(bounds, ("0.004406", "0.00000906", "0.00001371")):
        if not value.b < iv.mpf(limit).a:
            raise ArithmeticError(f"Interval ceiling {limit} failed")
    print("505 points enclosed: state error < 0.004406, wrong < 9.06e-6, leakage < 1.371e-5")


if __name__ == "__main__":
    main()
