"""Exact inverse search for one-copy spin counting effects."""

import argparse
from fractions import Fraction


def sector_effects(weights):
    """Return sharp effects forced by trace, and scalar rotational witnesses."""
    forced = {}
    scalar = {}
    for spin, weight in sorted(weights.items()):
        if type(spin) is not int or spin < 0 or not isinstance(weight, (int, Fraction)):
            raise ValueError("Use nonnegative integer 2j labels and exact rational weights.")
        dimension = spin + 1
        if not 0 <= weight <= dimension:
            raise ValueError(f"Weight at 2j={spin} is outside [0, {dimension}].")
        if weight in (0, dimension):
            forced[spin] = int(weight == dimension)
        scalar[spin] = Fraction(weight) / dimension
    return forced, scalar


def axis_effect(weights):
    """Find a shared diagonal f(2m), or return an exact obstruction."""
    sector_effects(weights)
    effect = {}
    for parity in (0, 1):
        previous_spin = None
        previous_weight = 0
        previous_labels = set()
        for spin in sorted(s for s in weights if s % 2 == parity):
            labels = set(range(-spin, spin + 1, 2))
            added = labels - previous_labels
            increment = weights[spin] - previous_weight
            if not 0 <= increment <= len(added):
                return None, (
                    f"2j={previous_spin} -> {spin}: required trace increment "
                    f"{increment}, allowed [0, {len(added)}]"
                )
            effect.update(dict.fromkeys(sorted(added), Fraction(increment) / len(added)))
            previous_spin, previous_weight, previous_labels = spin, weights[spin], labels
    return effect, None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-twice-spin", type=int, default=3,
                        help="largest 2j in the OP1 example (default: 3)")
    args = parser.parse_args()
    if args.max_twice_spin < 1:
        parser.error("--max-twice-spin must be at least 1")
    spins = range(1, args.max_twice_spin + 1)
    for frame, weights in (
        ("M", dict.fromkeys(spins, 2)),
        ("T", {spin: 2 * int(spin == 1) for spin in spins}),
    ):
        forced, scalar = sector_effects(weights)
        print(f"{frame}: forced scalar blocks by 2j: {forced}")
        print(f"{frame}: unique rotationally invariant effect by 2j: "
              f"{ {spin: str(value) for spin, value in scalar.items()} }")
        witness, obstruction = axis_effect(weights)
        if obstruction:
            print(f"{frame}: single-axis access impossible: {obstruction}")
        else:
            print(f"{frame}: single-axis witness by 2m: "
                  f"{ {label: str(value) for label, value in sorted(witness.items())} }")


if __name__ == "__main__":
    main()
