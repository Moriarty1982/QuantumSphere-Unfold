"""Reproduce the conditional Koide phase-overlap fit and its controls."""

import cmath
import math


MASSES = (0.51099895, 105.6583755, 1776.93)


def finite_gap_target(roots, mean, gap, omega):
    direct = 1 + math.sqrt(2)
    normalized = tuple(root / mean for root in roots)
    second_moment = sum(value**2 for value in normalized) / 3
    linear = 1 + direct / gap
    scale = 2 / (linear + math.sqrt(linear**2 - 4 * second_moment / gap))
    poles = tuple(scale * value for value in normalized)
    static = tuple(pole + pole * (direct - pole) / gap for pole in poles)
    return math.sqrt(2) * sum(value * omega**(-k-1) for k, value in enumerate(static)) / 3


def equal_weight_minimum_real(imaginary, count):
    """Minimum mean cosine at fixed mean sine in the positive root chamber."""
    end_sine = math.sin(math.pi / 12)
    end_cosine = math.cos(math.pi / 12)
    if abs(imaginary) > end_sine:
        return math.inf
    upper = min(count - 1, math.floor(count * (imaginary + end_sine) / (2 * end_sine)))
    remaining = count * imaginary - (2 * upper - count + 1) * end_sine
    return ((count - 1) * end_cosine + math.sqrt(1 - remaining**2)) / count


def main():
    roots = tuple(map(math.sqrt, MASSES))
    mean = sum(roots) / 3
    omega = cmath.exp(2j * math.pi / 3)
    target = math.sqrt(2) * sum(x * omega**(-k) for k, x in enumerate(roots)) / (3 * mean)
    center = cmath.phase(target)

    def sample(phase):
        return tuple(mean * (1 + math.sqrt(2) * (cmath.exp(1j * phase) * omega**k).real)
                     for k in range(3))

    reference = 2 * math.pi / 3 + 2 / 9
    relative = target * cmath.exp(-1j * reference)
    h = math.acos(relative.real)
    weight = (1 + relative.imag / math.sin(h)) / 2
    assert 0 <= weight <= 1
    upper, lower = sample(reference + h), sample(reference - h)
    coherent = tuple((weight * x + (1 - weight) * y)**2 for x, y in zip(upper, lower))
    incoherent = tuple(weight * x**2 + (1 - weight) * y**2 for x, y in zip(upper, lower))
    assert all(math.isclose(x, y, abs_tol=1e-10) for x, y in zip(coherent, MASSES))
    print(f"Mirror pair: orbit half-width={3*h:.12f} rad, upper weight={weight:.12f}")
    print(f"Root average: {coherent}; mass average: {incoherent}")

    # Mirrored parabolas in a Beltrami disk chart, with curvature b dx∧dy.
    length, height = 0.5, 0.125
    enclosed_area = 4 * length * height / 3
    fitted_curvature = 2 * h / enclosed_area
    for label, curvature, upper_weight in (
        ("flat", 0.0, 0.5),
        ("fitted curvature, equal weights", fitted_curvature, 0.5),
        ("fitted curvature and weights", fitted_curvature, weight),
    ):
        half_phase = curvature * enclosed_area / 2
        masses = tuple(
            (upper_weight * x + (1 - upper_weight) * y)**2
            for x, y in zip(sample(reference + half_phase), sample(reference - half_phase))
        )
        print(f"Transport {label}: curvature={curvature:.9f}, masses={masses}")

    for count in range(2, 17):
        positions = tuple(k - (count - 1) / 2 for k in range(count))
        lo, hi = 0.0, math.pi / (count - 1)
        for _ in range(55):
            step = (lo + hi) / 2
            radius = sum(math.cos(k * step) for k in positions) / count
            if radius > abs(target):
                lo = step
            else:
                hi = step
        step = (lo + hi) / 2
        readings = tuple(sample(center + k * step) for k in positions)
        assert all(min(reading) >= 0 for reading in readings)
        fitted = tuple((sum(values) / count)**2 for values in zip(*readings))
        assert all(math.isclose(x, y, abs_tol=1e-10) for x, y in zip(fitted, MASSES))
        print(f"N={count:2d}, orbit step={3*step:.12f} rad, masses={fitted}")

    for gap in (68, 100):
        target = finite_gap_target(roots, mean, gap, omega)
        allowed = [
            count for count in range(2, 17)
            if equal_weight_minimum_real(target.imag, count) <= target.real
            <= math.sqrt(1 - target.imag**2)
        ]
        print(f"D={gap}, feasible counts through 16: {allowed}")


if __name__ == "__main__":
    main()
