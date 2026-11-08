"""Interval verification of the finite-copy echo pointer."""
import argparse

from mpmath import iv

from qam_flux_verify_echo import propagate, table


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--positive-only", action="store_true")
    positive_only = parser.parse_args().positive_only
    iv.dps = 40
    flip = table("qam_flux_common_flip_controls.txt")
    forward = table("qam_flux_robust_controls.txt")
    mirrored = [(-x, y) for x, y in reversed(forward)]
    copy_time = (3 if positive_only else 1) * iv.pi / 2
    wait = 20 * iv.pi - 60 - copy_time / 2
    half_flip = iv.matrix([[1 + iv.j, 1 - iv.j], [1 - iv.j, 1 + iv.j]]) / 2
    ceilings = tuple(map(iv.mpf, ("0.003989", "0.002097", "0.003883")))
    maxima = [iv.mpf(0) for _ in ceilings]
    for label in (-3, -1, 1, 2, 3):
        target = int(abs(label) == 3)
        for step in range(-50, 51):
            z = label + iv.mpf(step) / 1000
            gate = propagate(flip, z)
            idle = iv.matrix([[iv.exp(-iv.j*z*wait), 0], [0, iv.exp(iv.j*z*wait)]])
            before = propagate(forward, z) * gate * idle * gate
            state = iv.matrix([[before[0, 0], 0], [before[1, 0], 0]])
            drift = iv.matrix([[iv.exp(-iv.j*z*copy_time/2), 0],
                               [0, iv.exp(iv.j*z*copy_time/2)]])
            for control in (1, 0):
                row = iv.matrix([[state[control, 0], state[control, 1]]]) * half_flip
                state[control, 0], state[control, 1] = row[0, 0], row[0, 1]
                state = gate * drift * state
            echo = gate * propagate(mirrored, z) * gate
            state = (-iv.exp(-iv.j*z*wait)) * (echo * state)
            error = iv.sqrt(sum(abs(state[a, p] - int(p == target and a == 0))**2
                                for a in range(2) for p in range(2)))
            wrong = iv.sqrt(sum(abs(state[a, 1-target])**2 for a in range(2)))
            leakage = iv.sqrt(sum(abs(state[1, p])**2 for p in range(2)))
            for index, (value, ceiling) in enumerate(zip((error, wrong, leakage), ceilings)):
                if value.b > maxima[index]:
                    maxima[index] = value.b
                if positive_only:
                    continue
                if not value.b < ceiling.a:
                    raise ArithmeticError(f"Grid ceiling failed at {label=}, {step=}")
    addition = (40 * iv.pi)**2 / 8_000_000
    bounds = (ceilings[0] + addition, (ceilings[1] + addition)**2,
              (ceilings[2] + addition)**2)
    if positive_only:
        bounds = (maxima[0] + addition, (maxima[1] + addition)**2,
                  (maxima[2] + addition)**2)
        for name, value in zip(("state error", "wrong", "leakage"), bounds):
            print(f"{name}: {value}")
        return
    for value, limit in zip(bounds, ("0.005964", "0.00001658", "0.00003431")):
        if not value.b < iv.mpf(limit).a:
            raise ArithmeticError(f"Interval ceiling {limit} failed")
    print("505 points enclosed: state error < 0.005964, wrong < 1.658e-5, leakage < 3.431e-5")


if __name__ == "__main__":
    main()
