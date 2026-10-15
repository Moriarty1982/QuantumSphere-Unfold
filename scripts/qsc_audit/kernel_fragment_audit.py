"""Exact finite-data checks for the local kernel construction.

Payloads are supplied integer codes, not recovered native QAM carriers.
Closure equivalence must be supplied and is validated, never inferred or
silently completed. Readout values are already post-class-map values.
No numerical tolerance, physical guard or global activation is inferred.
"""

from itertools import product


def audit_factorization(normal_forms, values):
    """Check fibre constancy and equality of partial-function domains."""
    if not set(values).issubset(normal_forms):
        raise ValueError("Readout domain is outside the supplied normal-form domain")
    factor = {}
    constant = True
    for payload, value in values.items():
        if value != value:
            raise ValueError("Readout equality must be reflexive; NaN is not accepted")
        key = normal_forms[payload]
        if key in factor and factor[key] != value:
            constant = False
        else:
            factor[key] = value
    observed = {normal_forms[payload] for payload in values}
    saturated = all((payload in values) == (key in observed)
                    for payload, key in normal_forms.items())
    return {
        "constant_on_fibres": constant,
        "domain_saturated": saturated,
        "total_on_fragment": set(values) == set(normal_forms),
        "exact_partial_factorization": constant and saturated,
        "factor_on_observed_classes": factor if constant else None,
    }


class FiniteKernelFragment:
    """A supplied nonempty finite set with a validated closure equivalence."""

    def __init__(self, payloads, closure_pairs):
        payloads = tuple(payloads)
        if not payloads or any(type(a) is not int or a < 0 for a in payloads):
            raise ValueError("Payload codes must be nonempty, nonnegative integers")
        if len(set(payloads)) != len(payloads):
            raise ValueError("Duplicate payload code")
        self.payloads = tuple(sorted(payloads))
        pairs = tuple(tuple(pair) for pair in closure_pairs)
        if any(len(pair) != 2 or any(type(a) is not int or a not in payloads for a in pair)
               for pair in pairs):
            raise ValueError("Closure pair outside the payload fragment")
        relation = frozenset(pairs)
        if any((a, a) not in relation for a in payloads):
            raise ValueError("Closure relation is not reflexive")
        if any((b, a) not in relation for a, b in relation):
            raise ValueError("Closure relation is not symmetric")
        if any((a, c) not in relation
               for a, b in relation for b2, c in relation if b == b2):
            raise ValueError("Closure relation is not transitive")
        self.closure = relation
        self.normal_forms = {a: min(b for b in payloads if (a, b) in relation)
                             for a in payloads}

    def _payload(self, payload):
        if type(payload) is not int or payload not in self.normal_forms:
            raise ValueError("Payload is outside the supplied fragment")
        return payload

    def state(self, tag, payload):
        if type(tag) is not int or tag not in (0, 1):
            raise ValueError("Only the explicitly declared pre-/post-shift state tags are supported")
        return tag, self._payload(payload)

    def project(self, state):
        if not isinstance(state, tuple) or len(state) != 2:
            raise ValueError("Expected a tagged state pair")
        tag, payload = state
        return self.state(tag, payload)[1]

    def normal_form(self, payload):
        return self.normal_forms[self._payload(payload)]

    def transport_preserved(self, edges):
        pairs = [(self._payload(a), self._payload(b)) for a, b in edges]
        return all(pair in self.closure for pair in pairs)

    def audit_readout(self, values):
        for payload in values:
            self._payload(payload)
        return audit_factorization(self.normal_forms, values)

    def audit_aggregation(self, arity, table):
        """Exhaustively check a supplied total operation; cost is exponential."""
        if type(arity) is not int or arity < 1:
            raise ValueError("Aggregation arity must be a positive integer")
        inputs = tuple(product(self.payloads, repeat=arity))
        for row in table:
            if not isinstance(row, tuple) or len(row) != arity:
                raise ValueError("Aggregation input must be an argument tuple")
            for payload in row:
                self._payload(payload)
        if set(table) != set(inputs):
            raise ValueError("Aggregation table must cover exactly the fragment power")
        for value in table.values():
            self._payload(value)
        quotient = {}
        congruent = True
        common_class_preserved = True
        for row in inputs:
            key = tuple(self.normal_form(a) for a in row)
            output = self.normal_form(table[row])
            if key in quotient and quotient[key] != output:
                congruent = False
            else:
                quotient[key] = output
            if len(set(key)) == 1 and output != key[0]:
                common_class_preserved = False
        diagonal = all(self.normal_form(table[(a,) * arity]) == self.normal_form(a)
                       for a in self.payloads)
        return {
            "congruent_on_classes": congruent,
            "diagonal_class_preserved": diagonal,
            "common_class_preserved": common_class_preserved,
            "quotient_operation": quotient if congruent else None,
            "local_routed_gate": congruent and diagonal,
            "scope": "supplied finite table only; no native or global activation",
        }
