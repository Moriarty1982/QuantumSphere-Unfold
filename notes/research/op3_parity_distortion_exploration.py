"""OP3 exploration with an explicit comparison monitor, separate from historical T_N.

Both planar extensions act as x -> -x on the visible axis.
For R = [[-1, b], [0, 1]], det(R.T R) = 1 and trace(R.T R) = 2 + b**2.
Thus trace(R.T R) = K + 1/K, where K >= 1 is the singular-value ratio.
"""

from fractions import Fraction


def classify_window(samples, radius, lipschitz, shear, squared_limit):
    points = sorted(samples)
    observed = max(abs(shear(point)) for point in points)
    if observed**2 > squared_limit:
        return "violation"

    gaps = [right - left for left, right in zip(points, points[1:])]
    cover_radius = max(radius + points[0], radius - points[-1],
                       max(gaps, default=Fraction(0)) / 2)
    upper = min(
        observed + lipschitz * cover_radius,
        *(abs(shear(point)) + lipschitz * (radius + abs(point)) for point in points),
    )
    return "certified" if upper**2 <= squared_limit else "undecided"


def main():
    limit = Fraction(2)
    shear_squared_limit = limit + 1 / limit - 2
    for shear in (Fraction(0), Fraction(1, 2), Fraction(1)):
        trace = 2 + shear**2
        passes = trace <= limit + 1 / limit
        print(f"b={shear}: trace={trace}, K <= {limit}: {passes}")

    # For R(x, y) = (-x + y**2, y), the largest |b| on |y| <= r is 2r.
    for radius in (Fraction(1, 4), Fraction(1, 2)):
        max_shear_squared = (2 * radius)**2
        passes = max_shear_squared <= shear_squared_limit
        print(f"r={radius}: max b^2={max_shear_squared}, window passes: {passes}")

    # The shear b(y) = 2y is Lipschitz with constant 2.
    for radius in (Fraction(1, 4), Fraction(1, 2)):
        for samples in ((Fraction(0),), (-radius, Fraction(0), radius)):
            result = classify_window(samples, radius, 2, lambda y: 2 * y, shear_squared_limit)
            print(f"r={radius}, samples={len(samples)}: {result}")

    # R(x, y) = (-x + 4y**2 - 8y**4, y) hides shear between the coarse samples.
    radius = Fraction(1, 2)
    coarse = (-radius, Fraction(0), radius)
    refined = (*coarse, Fraction(1, 4))
    for samples in (coarse, refined):
        # b'(y) = 8 - 96y**2, so |b'| <= 16 on this window.
        result = classify_window(
            samples, radius, 16, lambda y: 8 * y * (1 - 4 * y**2), shear_squared_limit,
        )
        print(f"interior control, samples={len(samples)}: {result}")

    # For g(y) = 4y² - 8y⁴, the centered slope differs from g'(y) by -32yh².
    point = Fraction(1, 4)
    step = Fraction(1, 8)

    def transverse_readout(y):
        return 4 * y**2 - 8 * y**4

    def centered_slope(readout, step):
        return (readout(point + step) - readout(point - step)) / (2 * step)

    slope = centered_slope(transverse_readout, step)
    error = 32 * abs(point) * step**2
    lower = max(Fraction(0), abs(slope) - error)
    print(f"transverse readout: slope={slope}, error={error}, "
          f"violation certified={lower**2 > shear_squared_limit}")
    half_step_slope = centered_slope(transverse_readout, step / 2)
    extrapolated = (4 * half_step_slope - slope) / 3
    print(f"two step sizes: half-step slope={half_step_slope}, extrapolated={extrapolated}, "
          f"matches exact derivative={extrapolated == 8 * point * (1 - 4 * point**2)}")

    def higher_order_readout(y):
        return transverse_readout(y) + y**6

    estimate = (4 * centered_slope(higher_order_readout, step / 2)
                - centered_slope(higher_order_readout, step)) / 3
    # The derivative of the five-node interpolation product at the center is h^4/4.
    # The center value has zero weight in the derivative of the interpolant.
    fifth_derivative_bound = 720 * (abs(point) + step)
    remainder_bound = fifth_derivative_bound * step**4 / 480
    exact_shear = 8 * point * (1 - 4 * point**2) + 6 * point**5
    lower = max(Fraction(0), abs(estimate) - remainder_bound)
    print(f"higher-order control: estimate={estimate}, bound={remainder_bound}, "
          f"actual error={abs(estimate - exact_shear)}, "
          f"violation certified={lower**2 > shear_squared_limit}")

    # In the historical fold chart, the sheet and parity flips act independently.
    fold_coordinate = Fraction(1, 4)
    parity = 1
    for name, sheet_sign, parity_sign in (
        ("identity", 1, 1),
        ("fold", -1, 1),
        ("parity", 1, -1),
        ("mixed", -1, -1),
    ):
        new_coordinate = sheet_sign * fold_coordinate
        new_parity = parity_sign * parity
        width_change = abs(new_coordinate**2 - fold_coordinate**2)
        sheet_change = abs(new_coordinate - fold_coordinate)
        parity_change = abs(new_parity - parity)
        print(f"historical chart, {name}: width change={width_change}, "
              f"sheet change={sheet_change}, parity change={parity_change}")
        probe = Fraction(1, 8)
        probe_slope = (sheet_sign * probe - sheet_sign * (-probe)) / (2 * probe)
        print(f"fold point, {name}: endpoint={(0, new_parity)}, sheet slope={probe_slope}")
        for readout_error in (probe / 2, probe):
            slope_error = readout_error / probe
            lower, upper = probe_slope - slope_error, probe_slope + slope_error
            inferred = "fold" if upper < 0 else "no fold" if lower > 0 else "undecided"
            print(f"fold point, {name}, readout error <= {readout_error}: {inferred}")


if __name__ == "__main__":
    main()
