"""Bounded OP1 route search over a declared catalogue of QAM operations."""

from collections import Counter
from fractions import Fraction
from functools import cmp_to_key
from math import comb, gcd, isqrt

from qam.tools.spin_readout_search import axis_effect


START = "M:spin-sectors"
TARGET = "T:minimal-spin-effect"
OPERATIONS = {
    "passive-frame": (START, "T:spin-sectors", "frame_change", None),
    "read-all-preserved-sectors": ("T:spin-sectors", TARGET, "identity_readout", None),
    "u1-readout": (START, TARGET, "selection", None),
    "quadratic-access": (START, "T:quadratic-flux", "observable_access", "native_quadratic_flux"),
    "quadratic-delta": ("T:quadratic-flux", TARGET, "selection", "native_quadratic_spectral_filter"),
    "reference-exchange": (START, "T:joint-singlet", "coupling", "native_reference_exchange"),
    "singlet-delta": ("T:joint-singlet", TARGET, "selection", "native_coherent_singlet_filter"),
}


# sin(k*pi/4) represented as a + b*sqrt(2), with exact coefficients.
SINE = ((0, 0), (0, Fraction(1, 2)), (1, 0), (0, Fraction(1, 2)),
        (0, 0), (0, Fraction(-1, 2)), (-1, 0), (0, Fraction(-1, 2)))


def rotation_mean(angle, twice_spin):
    """Return the exact normalized character as rational coefficients of 1 and sqrt(2)."""
    dimension = twice_spin + 1
    if angle == 360:
        return Fraction((-1)**twice_spin), Fraction(0)
    a, b = SINE[(dimension * (angle // 90)) % 8]
    if angle == 90:
        return Fraction(2 * b, dimension), Fraction(a, dimension)
    return Fraction(a, dimension), Fraction(b, dimension)


def generate_rotation_routes(angles, limit):
    operations, constructions, failures = {}, [], {}
    for angle in angles:
        spectrum = {j: rotation_mean(angle, j) for j in range(1, limit + 1)}
        target_value = spectrum[1]
        collisions = [j for j, value in spectrum.items() if j != 1 and value == target_value]
        rotation = f"rotation-{angle}"
        average = f"axis-mean-{angle}"
        selector = f"spectral-delta-{angle}"
        rotation_state = f"T:{rotation}"
        mean_state = f"T:{average}"
        operations[rotation] = (START, rotation_state, "rotation", "native_gravitational_spin_rotation")
        operations[average] = (rotation_state, mean_state, "coherent_average", "native_coherent_axis_mean")
        operations[selector] = (mean_state, TARGET, "spectral_filter", "native_axis_mean_spectral_filter")
        if collisions:
            failures[selector] = f"Target character also occurs at 2j={collisions}."
        competitors = sorted(set(spectrum.values()) - {target_value})
        half_integer_competitors = sorted({value for j, value in spectrum.items()
                                           if j > 1 and j % 2})
        half_collisions = [j for j in collisions if j % 2]
        prefiltered_path = None
        if 360 in angles and angle != 360 and not half_collisions and len(half_integer_competitors) < len(competitors):
            prefilter = "half-integer-prefilter"
            half_rotation = f"half-integer-{rotation}"
            half_average = f"half-integer-{average}"
            half_selector = f"half-integer-{selector}"
            operations[prefilter] = (
                START, "T:half-integer-spins", "central_character_filter",
                "native_coherent_spin_parity",
            )
            operations[half_rotation] = (
                "T:half-integer-spins", f"T:{half_rotation}", "rotation",
                "native_gravitational_spin_rotation",
            )
            operations[half_average] = (
                f"T:{half_rotation}", f"T:{half_average}", "coherent_average",
                "native_coherent_axis_mean",
            )
            operations[half_selector] = (
                f"T:{half_average}", TARGET, "spectral_filter",
                "native_axis_mean_spectral_filter",
            )
            prefiltered_path = [prefilter, half_rotation, half_average, half_selector]
        relational_path = None
        if angle == 90 and not collisions:
            relational_path = ["rotor-coupling-90", "rotor-return-90", "spectral-delta-90"]
            operations["rotor-coupling-90"] = (
                START, "T:spin-and-axis-rotor", "invariant_coupling",
                "native_gravitational_axis_rotor",
            )
            operations["rotor-return-90"] = (
                "T:spin-and-axis-rotor", mean_state, "coherent_reference_return",
                "native_rotor_singlet_return",
            )
        constructions.append({
            "rule": "normalized SU(2) character of a coherent axis average",
            "angle_degrees": angle,
            "operations": [rotation, average, selector],
            "target_value_basis_1_sqrt2": [str(value) for value in target_value],
            "collisions_by_twice_spin": collisions,
            "polynomial_filter": None if collisions else {
                "degree": len(competitors),
                "roots_basis_1_sqrt2": [[str(value) for value in root] for root in competitors],
            },
            "after_half_integer_prefilter": {
                "rotation_degrees": 360,
                "degree": None if half_collisions else len(half_integer_competitors),
                "operations": prefiltered_path,
                "roots_basis_1_sqrt2": [
                    [str(value) for value in root] for root in half_integer_competitors
                ],
                "collisions_by_twice_spin": half_collisions,
            } if 360 in angles else None,
            "relational_axis_mean": {
                "operations": relational_path,
                "sufficient_reference_dimension": (limit + 1)**2,
            } if relational_path else None,
            "finite_axis_quadrature": {
                "azimuth_points": limit + 1,
                "gauss_legendre_nodes": limit // 2 + 1,
                "axis_count": (limit + 1) * (limit // 2 + 1),
                "exact_polynomial_degree": limit,
            },
        })
    return operations, constructions, failures


def fiber_dimensions(units, point_quotient=None, right_singlet_phase=False, spins=None):
    """Count singlets in ordered spin lists at exact area units*a(1/2)."""
    if type(units) is not int or not 2 <= units <= 100 or units % 2:
        raise ValueError("Use an even exact_fiber_units value in [2, 100]")
    # Positive Pell solutions give the only spin species on this exact fiber.
    species = []
    dimension, area = 2, 1
    while area <= units:
        if spins is None or dimension - 1 in spins:
            species.append((area, range(1 - dimension, dimension, 2)))
        dimension, area = 2 * dimension + 3 * area, dimension + 2 * area

    if (type(right_singlet_phase) is not bool and right_singlet_phase != "actual") or (right_singlet_phase and point_quotient is None):
        raise ValueError("right_singlet_phase requires a point quotient and false, true or actual")
    if point_quotient in ("cyclic", "dihedral"):
        if units > 64:
            raise ValueError("Point-quotient fiber counting supports at most 64 units")
        return (quotient_singlets(units, species, point_quotient, right_singlet_phase),
                quotient_singlets(units, species[:1], point_quotient, right_singlet_phase))
    if point_quotient is not None:
        raise ValueError("Use point_quotient cyclic or dihedral")

    weights = [Counter() for _ in range(units + 1)]
    weights[0][0] = 1
    for total in range(1, units + 1):
        for area, magnetic_labels in species:
            if area > total:
                break
            for weight, count in weights[total - area].items():
                for label in magnetic_labels:
                    weights[total][weight + label] += count
    # In each integer-spin irrep, weight zero minus weight one counts singlets.
    incoming = weights[units][0] - weights[units][2]
    outgoing = comb(units, units // 2) // (units // 2 + 1)
    return incoming, outgoing


def quotient_singlets(units, species, quotient, right_singlet_phase):
    """Project at each list length, acting on the list and its spin factors."""
    def trace(cycles):
        states = Counter({(0, 0): 1})
        remaining = sum(cycles)
        for length in cycles:
            remaining -= length
            updated = Counter()
            for (area, magnetic), count in states.items():
                for weight, labels in species:
                    total = area + length * weight
                    if total + remaining > units:
                        break
                    for label in labels:
                        updated[total, magnetic + length * label] += count
            states = updated
        return states[units, 0] - states[units, 2]

    if right_singlet_phase == "actual":
        return actual_right_singlets(units, species, quotient)

    result = 0
    for points in range(1, units + 1):
        if right_singlet_phase and points % 2:
            continue
        cycle_types = Counter()
        for shift in range(points):
            count = gcd(points, shift)
            sign = (-1)**(points // 2 * shift) if right_singlet_phase else 1
            cycle_types[(points // count,) * count] += sign
        group_size = points
        if quotient == "dihedral":
            group_size *= 2
            for axis in range(points):
                fixed = 1 if points % 2 else 2 * int(axis % 2 == 0)
                sign = (-1)**(points // 2 * axis) if right_singlet_phase else 1
                cycle_types[(1,) * fixed + (2,) * ((points - fixed) // 2)] += sign
        numerator = sum(multiplicity * trace(cycles)
                        for cycles, multiplicity in cycle_types.items())
        dimension, remainder = divmod(numerator, group_size)
        if remainder:
            raise ArithmeticError("Nonintegral invariant dimension")
        result += dimension
    return result


def cycle_profile(permutation):
    visited = set()
    profile = []
    for start in range(len(permutation)):
        point = start
        counts = [0, 0]
        while point not in visited:
            visited.add(point)
            counts[point % 2] += 1
            point = permutation[point]
        if sum(counts):
            profile.append(tuple(counts))
    return tuple(sorted(profile))



def actual_right_singlets(units, species, quotient):
    """Count balanced maximal right singlets with their spin-dependent phase."""
    def trace(profile, swaps_groups):
        states = Counter({(0, 0, 0, 0): 1})
        remaining = sum(even + odd for even, odd in profile)
        for even, odd in profile:
            length = even + odd
            remaining -= length
            updated = Counter()
            for (area, magnetic, balance, parity), count in states.items():
                for weight, labels in species:
                    total = area + length * weight
                    if total + remaining > units:
                        break
                    twice_spin = len(labels) - 1
                    difference = balance + (even - odd) * twice_spin
                    phase = (parity + even * twice_spin) % 2 if swaps_groups else 0
                    for label in labels:
                        updated[total, magnetic + length * label, difference, phase] += count
            states = updated
        return (states[units, 0, 0, 0] - states[units, 2, 0, 0]
                - states[units, 0, 0, 1] + states[units, 2, 0, 1])

    result = 0
    for points in range(2, units + 1, 2):
        profiles = Counter()
        for shift in range(points):
            profiles[cycle_profile([(i + shift) % points for i in range(points)]), shift % 2] += 1
        if quotient == "dihedral":
            for axis in range(points):
                profiles[cycle_profile([(axis - i) % points for i in range(points)]), axis % 2] += 1
        numerator = sum(multiplicity * trace(profile, swap)
                        for (profile, swap), multiplicity in profiles.items())
        dimension, remainder = divmod(numerator, sum(profiles.values()))
        if remainder:
            raise ArithmeticError("Nonintegral spin-dependent invariant dimension")
        result += dimension
    return result


def radical_sign(terms):
    """Sign of a sum of distinct square-free radicals with rational coefficients."""
    terms = {base: coefficient for base, coefficient in terms.items() if coefficient}
    if set(terms) <= {1}:
        rational = terms.get(1, 0)
        return (rational > 0) - (rational < 0)
    scale = 16
    while True:
        lower = upper = 0
        for base, coefficient in terms.items():
            floor = isqrt(base * scale * scale)
            ceiling = floor + int(base != 1)
            lower += coefficient * (floor if coefficient > 0 else ceiling)
            upper += coefficient * (ceiling if coefficient > 0 else floor)
        if lower >= 0:
            return 1
        if upper <= 0:
            return -1
        scale *= 2


def compare_radical_areas(left, right):
    difference = Counter(dict(left))
    difference.subtract(dict(right))
    return radical_sign(difference)


def squarefree_parts(value):
    coefficient, squarefree = 1, value
    for factor in range(2, isqrt(value) + 1):
        while squarefree % (factor * factor) == 0:
            squarefree //= factor * factor
            coefficient *= factor
    return squarefree, coefficient


def radical_carrier(spins):
    """Identify the multiquadratic field of a declared finite spin carrier."""
    radicands = sorted({squarefree_parts(3 * spin * (spin + 2))[0] for spin in spins})
    classes = {1}
    for base in radicands:
        classes.update(base * member // gcd(base, member)**2 for member in tuple(classes))
    degree = len(classes)
    return {
        "twice_spins": spins,
        "squarefree_radicands": radicands,
        "field_degree": degree,
        "norm_separation_power": degree - 1,
        "complete_radical_basis": len(radicands) == degree,
        "critical_loss_power": (str(Fraction(2, degree - 1))
                                if degree > 1 and len(radicands) == degree else None),
    }


def window_dimensions(units, width, point_quotient=None, right_singlet_phase=False, spins=None):
    """Exact radical-sector counts for a small rational area window."""
    def compare(area, bound):
        difference = dict(area)
        difference[1] = difference.get(1, 0) - 3 * bound
        return radical_sign(difference)

    species = []
    labels = range(1, 2 * (units + 1)) if spins is None else spins
    for twice_spin in labels:
        dimension = twice_spin + 1
        atom = squarefree_parts(3 * (dimension**2 - 1))
        if compare((atom,), units + width) > 0:
            break
        species.append((atom, range(1 - dimension, dimension, 2)))

    actual = right_singlet_phase == "actual"

    def advance(level, cycle, swap):
        even, odd = cycle
        length = even + odd
        next_level = {}
        for area, weights in level.items():
            for (base, coefficient), labels in species:
                combined = dict(area)
                combined[base] = combined.get(base, 0) + length * coefficient
                new_area = tuple(sorted(combined.items()))
                if compare(new_area, units + width) > 0:
                    break
                target = next_level.setdefault(new_area, Counter())
                spin = len(labels) - 1
                for (magnetic, balance, phase), multiplicity in weights.items():
                    difference = balance + (even - odd) * spin if actual else 0
                    sign = (phase + even * spin) % 2 if actual and swap else 0
                    for label in labels:
                        target[magnetic + length * label, difference, sign] += multiplicity
        return next_level

    def singlet_trace(level):
        return {area: weights[0, 0, 0] - weights[2, 0, 0]
                      - weights[0, 0, 1] + weights[2, 0, 1]
                for area, weights in level.items() if compare(area, units) >= 0}

    initial = {(): Counter({(0, 0, 0): 1})}
    counts = Counter()
    level = initial
    for points in range(1, units + 1):
        level = advance(level, (int(points % 2 == 1), int(points % 2 == 0)), False)
        if point_quotient is None:
            counts.update(singlet_trace(level))
            continue
        if right_singlet_phase and points % 2:
            continue
        cycle_types = Counter()

        def record(permutation, swap):
            profile = cycle_profile(permutation)
            if not actual:
                profile = tuple(sorted((even + odd, 0) for even, odd in profile))
            sign = (-1)**(points // 2 * swap) if right_singlet_phase is True else 1
            cycle_types[profile, swap if actual else False] += sign

        for shift in range(points):
            record([(i + shift) % points for i in range(points)], shift % 2)
        group_size = points
        if point_quotient == "dihedral":
            group_size *= 2
            for axis in range(points):
                record([(axis - i) % points for i in range(points)], axis % 2)
        projected = Counter()
        for (cycles, swap), multiplicity in cycle_types.items():
            if not multiplicity:
                continue
            state = level if len(cycles) == points else initial
            if len(cycles) != points:
                for cycle in cycles:
                    state = advance(state, cycle, swap)
            for area, value in singlet_trace(state).items():
                projected[area] += multiplicity * value
        for area, value in projected.items():
            dimension, remainder = divmod(value, group_size)
            if remainder:
                raise ArithmeticError("Nonintegral window invariant dimension")
            counts[area] += dimension
    return {area: count for area, count in sorted(counts.items()) if count}


def check_channel(channel):
    """Necessary tests for a deterministic channel on a declared area carrier."""
    fields = {"input_dimension", "output_dimension", "environment_dimension",
              "area_preservation", "noninteger_inputs", "neutral_gapped_environment"}
    fiber = None
    if isinstance(channel, dict) and set(channel) - {"point_quotient", "right_singlet_phase", "spin_species"} == {
        "window_units", "window_width", "environment_dimension"
    }:
        units = channel["window_units"]
        raw_width = channel["window_width"]
        if type(units) is not int or not 2 <= units <= 100 or units % 2:
            raise ValueError("Use even window_units in [2, 100]")
        if not isinstance(raw_width, str):
            raise ValueError("window_width must be a rational string")
        try:
            width = Fraction(raw_width)
        except (ValueError, ZeroDivisionError) as error:
            raise ValueError("window_width must be a rational string") from error
        if not 0 < width < 1:
            raise ValueError("window_width must be strictly between zero and one")
        point_quotient = channel.get("point_quotient")
        if point_quotient not in (None, "cyclic", "dihedral"):
            raise ValueError("Use point_quotient cyclic or dihedral")
        environment = channel["environment_dimension"]
        if type(environment) is not int or environment < 1:
            raise ValueError("Environment dimension must be a positive integer")
        right_phase = channel.get("right_singlet_phase", False)
        spins = channel.get("spin_species")
        if "spin_species" in channel:
            if (not isinstance(spins, list)
                    or any(type(spin) is not int or not 1 <= spin <= 24 for spin in spins)
                    or 1 not in spins or len(set(spins)) != len(spins)):
                raise ValueError("spin_species must contain distinct integer 2j labels in [1, 24], including 1")
            spins = sorted(spins)
        carrier = None
        if spins is not None:
            carrier = radical_carrier(spins)
            degree = carrier["field_degree"]
            if degree == 1:
                lower = Fraction(1)
            else:
                # For each radical, half the conjugates reverse its sign.
                # AM-GM bounds the product of the other D-1 conjugates.
                conjugate_mean = width + Fraction(degree, degree - 1) * (units + width)
                lower = 1 / (3**degree * conjugate_mean**(degree - 1))
            carrier["positive_residual_lower_bound"] = str(lower)
            carrier["window_certified_exact_only"] = width < lower
        exact_area = ((1, 3 * units),)
        if carrier and carrier["window_certified_exact_only"]:
            incoming, outgoing = fiber_dimensions(units, point_quotient, right_phase, spins)
            counts = {exact_area: incoming} if incoming else {}
            count_method = "norm-certified exact fiber"
        else:
            if units > 10:
                raise ValueError("Windows above 10 units require a finite spin carrier and an exact-only certificate")
            _, outgoing = fiber_dimensions(units, point_quotient, right_phase, spins)
            counts = window_dimensions(units, width, point_quotient, right_phase, spins)
            count_method = "exact radical window enumeration"
        fiber = {"window_units": units, "window_width": str(width),
                 "model": "ordered SU(2) singlets, labels encode 3*area as radical sums",
                 "point_quotient": point_quotient, "right_singlet_phase": right_phase,
                 "input_dimension": sum(counts.values()),
                 "output_dimension": outgoing}
        fiber["count_method"] = count_method
        if carrier is not None:
            fiber["radical_carrier"] = carrier
        positive_areas = [area for area in counts if area != exact_area]
        if positive_areas:
            nearest = min(positive_areas, key=cmp_to_key(compare_radical_areas))
            residual = Counter(dict(nearest))
            residual[1] -= 3 * units
            fiber["first_positive_residual"] = {
                "three_times_residual": [[base, coefficient]
                                         for base, coefficient in sorted(residual.items())
                                         if coefficient],
                "input_dimension": counts[nearest],
            }
        if not counts or not outgoing:
            return {"fiber": fiber, "minimum_environment_dimension": None,
                    "exclusions": ["The projected input or output carrier is empty."],
                    "scope": "Exact window with the declared point character."}
        environment = channel["environment_dimension"]
        sectors = {
            "0" if area == ((1, 3 * units),) else str(area): {
                "input_dimension": count,
                "environment_dimension": environment if area == ((1, 3 * units),) else 0,
            }
            for area, count in counts.items()
        }
        channel = {
            "input_dimension": sum(counts.values()), "output_dimension": outgoing,
            "environment_dimension": environment, "area_preservation": "exact",
            "noninteger_inputs": any(label != "0" for label in sectors), "neutral_gapped_environment": True,
            "area_sectors": sectors,
        }
    if isinstance(channel, dict) and set(channel) - {"point_quotient", "right_singlet_phase"} == {
        "exact_fiber_units", "environment_dimension"
    }:
        units = channel["exact_fiber_units"]
        point_quotient = channel.get("point_quotient")
        right_phase = channel.get("right_singlet_phase", False)
        incoming, outgoing = fiber_dimensions(units, point_quotient, right_phase)
        fiber = {"exact_fiber_units": units, "input_dimension": incoming,
                 "output_dimension": outgoing,
                 "model": "ordered spin lists, full SU(2) singlets",
                 "point_quotient": point_quotient, "right_singlet_phase": right_phase}
        environment = channel["environment_dimension"]
        if type(environment) is not int or environment < 1:
            raise ValueError("Environment dimension must be a positive integer")
        if not incoming or not outgoing:
            return {
                "fiber": fiber,
                "minimum_environment_dimension": None,
                "exclusions": ["The projected input or output carrier is empty."],
                "scope": "Exact fiber with the declared point character.",
            }
        channel = {"input_dimension": incoming, "output_dimension": outgoing,
                   "environment_dimension": channel["environment_dimension"],
                   "area_preservation": "exact", "noninteger_inputs": False,
                   "neutral_gapped_environment": False}
    if not isinstance(channel, dict) or set(channel) - {"area_sectors"} != fields:
        raise ValueError("Channel check requires dimensions, area mode and two spectrum flags")
    dimensions = [channel[name] for name in
                  ("input_dimension", "output_dimension", "environment_dimension")]
    if any(type(value) is not int or value < 1 for value in dimensions):
        raise ValueError("Channel dimensions must be positive integers")
    if channel["area_preservation"] not in ("exact", "window") or any(
        type(channel[name]) is not bool for name in
        ("noninteger_inputs", "neutral_gapped_environment")
    ):
        raise ValueError("Use area mode exact/window and Boolean spectrum flags")
    input_dim, output_dim, environment_dim = dimensions
    minimum = (input_dim + output_dim - 1) // output_dim
    exclusions = []
    if environment_dim < minimum:
        exclusions.append("Input dimension exceeds the visible output times environment dimension.")
    if (channel["area_preservation"] == "exact" and channel["noninteger_inputs"]
            and channel["neutral_gapped_environment"]):
        exclusions.append("A noninteger area residual below one has no environment eigenvalue.")
    # The environment dimension bounds the number of Kraus operators in
    # a Ja branch when all hidden outputs are included in that environment.
    upper = min(Fraction(1), Fraction(output_dim * environment_dim, input_dim))
    if (channel["area_preservation"] == "exact" and channel["noninteger_inputs"]
            and channel["neutral_gapped_environment"]):
        success_scope = "Dimension bound only; noninteger residual sectors cannot succeed."
    else:
        success_scope = "Uniform input; environment dimension bounds the Ja Kraus rank."
    result = {
        "minimum_environment_dimension": minimum,
        "selective_success_upper_bound": str(upper),
        "selective_success_scope": success_scope,
        "exclusions": exclusions,
        "scope": ("Necessary tests on declared dimensions; the spectrum test assumes a window "
                  "of width below one, integer minimal-spin output, and additive area."),
    }
    if "area_sectors" in channel:
        sectors = channel["area_sectors"]
        if channel["area_preservation"] != "exact" or not isinstance(sectors, dict) or not sectors:
            raise ValueError("area_sectors requires exact area mode and a nonempty sector mapping")
        if any(not isinstance(label, str) or not label
               or not isinstance(sector, dict)
               or set(sector) != {"input_dimension", "environment_dimension"}
               or type(sector["input_dimension"]) is not int or sector["input_dimension"] < 1
               or type(sector["environment_dimension"]) is not int or sector["environment_dimension"] < 0
               for label, sector in sectors.items()):
            raise ValueError("Each area sector needs a label, positive input and nonnegative environment dimension")
        if (sum(sector["input_dimension"] for sector in sectors.values()) != input_dim
                or sum(sector["environment_dimension"] for sector in sectors.values()) > environment_dim):
            raise ValueError("Area-sector dimensions must match the input and fit the environment")
        nonzero = {label for label in sectors if label != "0"}
        if bool(nonzero) != channel["noninteger_inputs"]:
            raise ValueError("Use label 0 for the exact sector and declare nonzero residuals consistently")
        if channel["neutral_gapped_environment"] and any(
            sectors[label]["environment_dimension"] for label in nonzero
        ):
            raise ValueError("A neutral gapped environment cannot supply nonzero residuals below one")
        per_sector = {}
        accepted = 0
        for label, sector in sorted(sectors.items()):
            incoming = sector["input_dimension"]
            available = sector["environment_dimension"]
            required = (incoming + output_dim - 1) // output_dim
            capacity = min(incoming, output_dim * available)
            per_sector[label] = {"minimum_environment_dimension": required,
                                 "accepted_dimension_upper_bound": capacity}
            accepted += capacity
            if available < required:
                exclusions.append(f"Insufficient environment dimension at area residual {label}.")
        result["area_sectors"] = per_sector
        result["minimum_environment_dimension_by_area"] = sum(
            sector["minimum_environment_dimension"] for sector in per_sector.values()
        )
        result["selective_success_upper_bound"] = str(Fraction(accepted, input_dim))
        result["selective_success_scope"] = (
            "Uniform input and declared orthogonal residual eigenspaces; "
            "sector dimensions are supplied, not derived."
        )
    if fiber is not None:
        result["fiber"] = fiber
    return result


def search(arguments, guards):
    required = {"start", "target", "operations", "max_steps", "max_twice_spin"}
    if not isinstance(arguments, dict) or set(arguments) - {"rotation_angles", "channel"} != required:
        raise ValueError("SEARCH_ROUTE requires start, target, operations, max_steps and max_twice_spin")
    if arguments["start"] != START or arguments["target"] != TARGET:
        raise ValueError("SEARCH_ROUTE currently supports the declared OP1 endpoints")
    allowed = arguments["operations"]
    steps, limit = arguments["max_steps"], arguments["max_twice_spin"]
    if (not isinstance(allowed, list) or any(
        not isinstance(name, str) or name not in OPERATIONS for name in allowed
    ) or len(set(allowed)) != len(allowed)):
        raise ValueError("Use distinct operation names from the OP1 catalogue")
    if type(steps) is not int or not 1 <= steps <= 7 or type(limit) is not int or not 1 <= limit <= 200:
        raise ValueError("Use integer max_steps in [1, 7] and max_twice_spin in [1, 200]")

    angles = arguments.get("rotation_angles", [])
    if (not isinstance(angles, list)
            or any(type(angle) is not int or angle not in (90, 180, 360) for angle in angles)
            or len(angles) != len(set(angles))):
        raise ValueError("Use distinct rotation angles from 90, 180 and 360 degrees")
    generated, constructions, failures = generate_rotation_routes(angles, limit)
    operations = {**OPERATIONS, **generated}
    allowed = allowed + list(generated)

    weights = {j: 2 * int(j == 1) for j in range(1, limit + 1)}
    witness, obstruction = axis_effect(weights)
    pending = [(START, [], [])]
    routes = []
    excluded = []
    while pending:
        state, path, obligations = pending.pop(0)
        if state == TARGET:
            routes.append({"operations": path, "open_guards": obligations})
            continue
        if len(path) == steps:
            continue
        for name in allowed:
            source, target, kind, guard = operations[name]
            if source != state:
                continue
            candidate = path + [name]
            reason = failures.get(name)
            if name == "u1-readout":
                reason = obstruction
            elif name == "read-all-preserved-sectors" and limit > 1:
                reason = "Passive transport preserves higher-spin sectors, starting with 2j=2."
            if reason:
                excluded.append({"operations": candidate, "reason": reason})
                continue
            unresolved = obligations + [guard] if guard and guards.get(guard, {}).get("status") is not True else obligations
            pending.append((target, candidate, unresolved))
    result = {
        "routes": routes, "excluded": excluded, "constructions": constructions,
        "operations": {name: dict(zip(("source", "target", "kind", "guard"), operations[name]))
                       for name in allowed},
        "axis_witness": None if witness is None or "u1-readout" not in allowed else {
            str(label): str(value) for label, value in witness.items()
        },
        "scope": "Finite OP1 model, one copy per spin; operation guards are declarations.",
    }
    if "channel" in arguments:
        result["channel_check"] = check_channel(arguments["channel"])
    return result
