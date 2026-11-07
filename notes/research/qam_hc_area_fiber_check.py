"""Check the b=0 threshold using weighted magnetic-state counts."""

from math import comb, exp, isqrt


def minimal_share(total_area):
    """Use units of a(1/2) and twice the magnetic quantum number."""
    spins = []
    for area in range(1, total_area + 1):
        dimension = isqrt(3 * area**2 + 1)
        if dimension**2 == 3 * area**2 + 1:
            weight = 2.0**-area * total_area ** (-(area - 1) / 3)
            spins.append((area, range(1 - dimension, dimension, 2), weight))

    counts = [{} for _ in range(total_area + 1)]
    counts[0][0] = 1.0
    for used, row in enumerate(counts):
        for area, projections, weight in spins:
            if used + area > total_area:
                break
            target = counts[used + area]
            for projection, count in row.items():
                for step in projections:
                    key = projection + step
                    target[key] = target.get(key, 0.0) + count * weight

    final = counts[total_area]
    singlets = final.get(0, 0.0) - final.get(2, 0.0)
    half = total_area // 2
    pure = comb(total_area, half) / ((half + 1) * 2**total_area)
    return pure / singlets


if __name__ == "__main__":
    for size in (8, 32, 64, 128, 256):
        print(f"{size:3d}  {minimal_share(size):.9f}")
    print(f"limit  {exp(-7 / 16):.9f}")
