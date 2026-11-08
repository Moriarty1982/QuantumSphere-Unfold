"""Bounded OP1 route search over a declared catalogue of QAM operations."""

from fractions import Fraction

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


def search(arguments, guards):
    required = {"start", "target", "operations", "max_steps", "max_twice_spin"}
    if not isinstance(arguments, dict) or set(arguments) - {"rotation_angles"} != required:
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
    return {
        "routes": routes, "excluded": excluded, "constructions": constructions,
        "operations": {name: dict(zip(("source", "target", "kind", "guard"), operations[name]))
                       for name in allowed},
        "axis_witness": None if witness is None or "u1-readout" not in allowed else {
            str(label): str(value) for label, value in witness.items()
        },
        "scope": "Finite OP1 model, one copy per spin; operation guards are declarations.",
    }
