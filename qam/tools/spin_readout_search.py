"""Exact inverse search for one-copy spin counting effects."""

import argparse
from fractions import Fraction
from hashlib import sha256
from pathlib import Path


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


def solve(weights):
    forced, scalar = sector_effects(weights)
    witness, obstruction = axis_effect(weights)
    return {
        "forced": {str(spin): value for spin, value in forced.items()},
        "scalar": {str(spin): str(value) for spin, value in scalar.items()},
        "axis": None if witness is None else {
            str(label): str(value) for label, value in sorted(witness.items())
        },
        "obstruction": obstruction,
    }


def report_lines(frame, result):
    yield f"{frame}: forced scalar blocks by 2j: {result['forced']}"
    yield f"{frame}: unique rotationally invariant effect by 2j: {result['scalar']}"
    if result["obstruction"]:
        yield f"{frame}: single-axis access impossible: {result['obstruction']}"
    else:
        yield f"{frame}: single-axis witness by 2m: {result['axis']}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-twice-spin", type=int, default=3,
                        help="largest 2j in the OP1 example (default: 3)")
    parser.add_argument("--cache", type=Path, help="optional SQLite cache path")
    args = parser.parse_args()
    if args.max_twice_spin < 1:
        parser.error("--max-twice-spin must be at least 1")
    spins = range(1, args.max_twice_spin + 1)
    for frame, weights in (
        ("M", dict.fromkeys(spins, 2)),
        ("T", {spin: 2 * int(spin == 1) for spin in spins}),
    ):
        if args.cache is None:
            result = solve(weights)
        else:
            from qam.tools.readout_db import cached_readout

            identity = {
                "readout": "op1.spin-counting-effects",
                "frame": frame,
                "weights_by_twice_spin": weights,
                "method": "exact-rational, one copy per irrep",
                "implementation_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
            }
            result, hit = cached_readout(args.cache, identity, lambda: solve(weights))
            print(f"{frame}: cache {'hit' if hit else 'miss'}")
        for line in report_lines(frame, result):
            print(line)

if __name__ == "__main__":
    main()
