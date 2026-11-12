"""Known-data exploration. No optimization, prediction, phase scan or native fit."""
import itertools
import json
import sys
from decimal import Decimal, localcontext
from pathlib import Path

BASE = Path(__file__).resolve().parent

def evaluate(values):
    e, mu, tau = values
    roots = [v.sqrt() for v in values]
    total = sum(values)
    return {
        "K": total / sum(roots)**2,
        "mass_triangle_deficit_MeV": tau-mu-e,
        "triangle_deficit_fraction_of_tau": (tau-mu-e)/tau,
        "minimum_relative_multiplier_spread_necessary": tau/(mu+e),
        "root_triangle_deficit_sqrt_MeV": roots[2]-roots[1]-roots[0],
        "tau_over_e": tau/e,
        "tau_over_mu": tau/mu,
        "rank1_best_relative_Frobenius_error_for_mass_matrix": ((e*e+mu*mu)/sum(v*v for v in values)).sqrt(),
        "equal_left_right_diagonal_Z_normalized_to_tau": [tau/v for v in values],
        "left_only_diagonal_Z_normalized_to_tau": [(tau/v)**2 for v in values],
    }

def stringify(value):
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, dict):
        return {k: stringify(v) for k, v in value.items()}
    if isinstance(value, list):
        return [stringify(v) for v in value]
    return value

def main():
    data = json.loads((BASE/'inputs.json').read_text(encoding='utf-8'))
    with localcontext() as ctx:
        ctx.prec = 50
        m = list(map(Decimal, data['masses']))
        u = list(map(Decimal, data['uncertainties']))
        central = evaluate(m)
        corners = [evaluate([a+s*b for a,b,s in zip(m,u,signs)])
                   for signs in itertools.product([-1,1], repeat=3)]
        envelope = {key: [min(row[key] for row in corners), max(row[key] for row in corners)]
                    for key in ('K', 'mass_triangle_deficit_MeV', 'minimum_relative_multiplier_spread_necessary')}
        # Independent exact-decimal check of the decisive mass inequality.
        assert central['mass_triangle_deficit_MeV'] == Decimal('1670.76062554931')
        assert central['K'] > Decimal('0.5')
        # Hand-computable controls for an admissible degenerate triangle and equal masses.
        control = [Decimal(1),Decimal(1),Decimal(0)]
        assert sum(control)/sum(v.sqrt() for v in control)**2 == Decimal('0.5')
        assert abs(evaluate([Decimal(1)]*3)['K']-Decimal(1)/3) < Decimal('1e-48')
        result = stringify({'central':central, 'individual_uncertainty_box_corners':envelope,
                            'corner_count':8, 'precision_decimal_digits':50,
                            'status':'known-data diagnostic; not a native reconstruction'})
    dest = Path(sys.argv[1])
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result['central'],indent=2))

if __name__ == '__main__':
    main()
