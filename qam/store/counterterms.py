"""Counterterm registry: local, effective compensation terms with guard inheritance.

A counterterm-scheme records a placeholder or phenomenological compensation term
delta_i(mu, R; theta_i) next to a protected structural core. It is never a
derivation. The registry only enforces bookkeeping:

* required fields, rational parameter bounds and at least one open guard;
* an append-only lifecycle per scheme version, stored as counterterm-transition
  versions (placeholder -> partially_constrained -> structurally_matched | deprecated);
* dependency resolution over declared/reviewed edges and inheritance of open
  guards from every scheme that is not structurally_matched;
* a re-audit ledger event listing downstream versions at every status change;
* an exact residual check Delta = F - delta on declared rational sample points;
* a term-role check (structural_core / counterterm_compensation), kept apart
  from the front/back index roles of qam-role-audit/2;
* fit provenance (fitted_on, including discrete scans) and a blindness check:
  a dependent statement tested against fitted data is reported as not_blind;
* Delta reported against the tolerance and against the fit uncertainty of theta,
  so a derivation that deviates from the fit is never adopted silently.

The intended use is rapid prototyping: a placeholder is registered first and
later replaced by a derivation F_i; the registry keeps that replacement honest.

Passing checks never close OP1-OP5, C5 or C6/T2 and never certify physics.
"""

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
import sys

from sqlalchemy import select

from qam.store.orm import store_session
from qam.store.registry import canonical, digest, latest_review, require_text, source_record


SCHEME = 'counterterm-scheme'
TRANSITION = 'counterterm-transition'
EDGE = 'depends-on-counterterm'
DEPENDENCY_EDGES = {'requires', 'interpreted-by', EDGE}
STATUSES = ('placeholder', 'partially_constrained', 'structurally_matched', 'deprecated')
ALLOWED = {
    'placeholder': {'partially_constrained', 'deprecated'},
    'partially_constrained': {'structurally_matched', 'deprecated'},
    'structurally_matched': {'deprecated'},
    'deprecated': set(),
}
PARAMETER_ROLES = {'fit_parameter', 'regulator_cutoff', 'fixed_input'}
DISCRETE = 'discrete_choice'
BASIS_KINDS = {'lagrangian_operator', 'readout'}
TERM_ROLES = {'structural_core', 'counterterm_compensation'}
INDEX_ROLES = {'readout', 'frame', 'observer', 'language', 'address',
               'structure', 'action', 'field', 'transport', 'operator'}
POLYNOMIAL = 'qam-polynomial-v1'
RESIDUAL_CHECKER = 'qam-counterterm-residual-v1'
ROLE_CHECKER = 'qam-term-role-v1'
BLINDNESS_CHECKER = 'qam-counterterm-blindness-v1'
MAX_OPTIONS = 64
MAX_DEGREE = 16
MAX_SAMPLES = 256
SCHEME_FIELDS = {'title', 'target_sector', 'operator_basis', 'compensation_function', 'reference_scale',
                 'matching_condition', 'rg_flow', 'validity_domain', 'magnitude_convention',
                 'replacement_tolerance', 'open_guards', 'assumptions', 'scope', 'fitted_on', 'known_tensions'}
SCOPE = ('Local, effective and readout-dependent bookkeeping; no derivation, no global closure; '
         'OP1-OP5, C5 and C6/T2 stay open')
RATIONAL = re.compile(r'[+-]?\d+(?:/[1-9]\d*)?')
NAME = re.compile(r'[A-Za-z][A-Za-z0-9_]{0,63}')


def rational(value, name):
    if type(value) is int:
        value = str(value)
    if not isinstance(value, str) or len(value) > 256 or not RATIONAL.fullmatch(value):
        raise ValueError(f'{name} must be an integer or exact rational string')
    return Fraction(value)


def validate_polynomial(form, parameters, name):
    if not isinstance(form, dict) or set(form) != {'type', 'variable', 'coefficients'}:
        raise ValueError(f'{name} requires type, variable and coefficients')
    if form['type'] != POLYNOMIAL:
        raise ValueError(f'{name} type must be {POLYNOMIAL}')
    if not isinstance(form['variable'], str) or not NAME.fullmatch(form['variable']):
        raise ValueError(f'{name} variable must be an identifier')
    coefficients = form['coefficients']
    if not isinstance(coefficients, list) or not 1 <= len(coefficients) <= MAX_DEGREE + 1:
        raise ValueError(f'{name} needs 1 to {MAX_DEGREE + 1} coefficients (constant term first)')
    for entry in coefficients:
        if isinstance(entry, str) and NAME.fullmatch(entry):
            if entry not in parameters:
                raise ValueError(f'{name} coefficient {entry} is not a declared parameter')
        else:
            rational(entry, f'{name} coefficient')


def evaluate(form, parameters, point):
    """Exact Horner evaluation; returns None when a named coefficient has no value."""
    total = Fraction(0)
    for entry in reversed(form['coefficients']):
        if isinstance(entry, str) and NAME.fullmatch(entry):
            value = parameters[entry]['value']
            if value is None:
                return None
            entry = value
        total = total * point + rational(entry, 'coefficient')
    return total


def validate_parameter(key, spec):
    if not NAME.fullmatch(key):
        raise ValueError('Parameter names must be identifiers')
    if isinstance(spec, dict) and spec.get('role') == 'orientation_sign':
        raise ValueError(f'Parameter {key}: the orientation sign o_R is not a counterterm parameter; '
                         'keep it as an explicit factor outside |delta_i|')
    if isinstance(spec, dict) and spec.get('role') == DISCRETE:
        if set(spec) != {'value', 'options', 'role'}:
            raise ValueError(f'Discrete parameter {key} requires value, options and role')
        options = spec['options']
        if not isinstance(options, list) or not 2 <= len(options) <= MAX_OPTIONS:
            raise ValueError(f'Discrete parameter {key} needs 2 to {MAX_OPTIONS} options')
        for option in options:
            require_text(option, f'{key} option')
        if len(set(options)) != len(options):
            raise ValueError(f'Discrete parameter {key} has duplicate options')
        if spec['value'] is not None and spec['value'] not in options:
            raise ValueError(f'Discrete parameter {key} value is not one of its options')
        return
    if not isinstance(spec, dict) or set(spec) != {'value', 'bounds', 'role'}:
        raise ValueError(f'Parameter {key} requires value, bounds and role')
    if spec['role'] not in PARAMETER_ROLES:
        raise ValueError(f'Parameter {key} role must be one of {sorted(PARAMETER_ROLES | {DISCRETE})}')
    bounds = spec['bounds']
    if not isinstance(bounds, list) or len(bounds) != 2:
        raise ValueError(f'Parameter {key} bounds must be [lower, upper]')
    lower, upper = (rational(item, f'{key} bound') for item in bounds)
    if lower > upper:
        raise ValueError(f'Parameter {key} lower bound exceeds upper bound')
    if spec['value'] is not None and not lower <= rational(spec['value'], f'{key} value') <= upper:
        raise ValueError(f'Parameter {key} value lies outside its declared bounds')


def validate_fit(fit, parameters):
    """fitted_on is null when every theta is set by declaration, else the fit provenance."""
    if fit is None:
        return
    fields = {'method', 'parameters', 'data', 'uncertainty', 'scan'}
    if not isinstance(fit, dict) or set(fit) != fields:
        raise ValueError(f'fitted_on requires exactly {sorted(fields)}')
    require_text(fit['method'], 'fitted_on.method')
    names = fit['parameters']
    if not isinstance(names, list) or not names or len(set(names)) != len(names):
        raise ValueError('fitted_on.parameters must list distinct fitted parameter names')
    for name in names:
        if name not in parameters:
            raise ValueError(f'fitted_on names undeclared parameter {name}')
    data = fit['data']
    if not isinstance(data, list) or not data:
        raise ValueError('fitted_on.data must list the target data')
    seen = set()
    for item in data:
        if not isinstance(item, dict) or set(item) != {'label', 'source', 'version', 'value'}:
            raise ValueError('Each fitted datum requires label, source, version and value')
        for name, value in item.items():
            require_text(value, f'fitted datum {name}')
        if (item['source'], item['label']) in seen:
            raise ValueError('Duplicate fitted datum')
        seen.add((item['source'], item['label']))
    uncertainty = fit['uncertainty']
    if not isinstance(uncertainty, dict):
        raise ValueError('fitted_on.uncertainty must map fitted continuous parameters to rational sigma')
    for name, sigma in uncertainty.items():
        if name not in names or parameters[name]['role'] == DISCRETE:
            raise ValueError(f'Uncertainty for {name} needs a fitted continuous parameter')
        if rational(sigma, f'{name} uncertainty') < 0:
            raise ValueError('Uncertainties must be nonnegative')
    scan = fit['scan']
    if scan is not None:
        if not isinstance(scan, dict) or set(scan) != {'trials', 'hits', 'chance_expectation'}:
            raise ValueError('scan requires trials, hits and chance_expectation')
        trials, hits = scan['trials'], scan['hits']
        if type(trials) is not int or type(hits) is not int or trials < 1 or not 0 <= hits <= trials:
            raise ValueError('scan needs integer trials >= 1 and 0 <= hits <= trials')
        if rational(scan['chance_expectation'], 'chance_expectation') < 0:
            raise ValueError('chance_expectation must be nonnegative')


def validate_scheme(payload, frame=None):
    if not isinstance(payload, dict) or set(payload) != SCHEME_FIELDS:
        raise ValueError(f'{SCHEME} payload requires exactly {sorted(SCHEME_FIELDS)}')
    for name in ('title', 'target_sector', 'reference_scale', 'matching_condition', 'scope'):
        require_text(payload[name], name)
    basis = payload['operator_basis']
    if not isinstance(basis, dict) or set(basis) != {'kind', 'expression', 'frame'}:
        raise ValueError('operator_basis requires kind, expression and frame')
    if basis['kind'] not in BASIS_KINDS:
        raise ValueError(f'operator_basis.kind must be one of {sorted(BASIS_KINDS)}')
    require_text(basis['expression'], 'operator_basis.expression')
    require_text(basis['frame'], 'operator_basis.frame')
    if frame is not None and basis['frame'] != frame:
        raise ValueError('operator_basis frame must equal the declared frame (Konvention F)')
    tensions = payload['known_tensions']
    if not isinstance(tensions, list):
        raise ValueError('known_tensions must be a list')
    for item in tensions:
        if not isinstance(item, dict) or set(item) != {'description', 'convention', 'delta', 'source'}:
            raise ValueError('Each known tension requires description, convention, delta and source')
        for name, value in item.items():
            require_text(value, f'known tension {name}')
    if payload['rg_flow'] is not None:
        require_text(payload['rg_flow'], 'rg_flow')
    if not isinstance(payload['assumptions'], list):
        raise ValueError('assumptions must be a list of explicit statements')
    for item in payload['assumptions']:
        require_text(item, 'assumption')
    function = payload['compensation_function']
    if not isinstance(function, dict) or set(function) != {'symbolic', 'parameters', 'form'}:
        raise ValueError('compensation_function requires symbolic, parameters and form')
    require_text(function['symbolic'], 'compensation_function.symbolic')
    parameters = function['parameters']
    if not isinstance(parameters, dict):
        raise ValueError('parameters must map names to declarations')
    for key, spec in parameters.items():
        validate_parameter(key, spec)
    validate_fit(payload['fitted_on'], parameters)
    domain = payload['validity_domain']
    if not isinstance(domain, dict) or set(domain) != {'variable', 'interval', 'samples', 'description'}:
        raise ValueError('validity_domain requires variable, interval, samples and description')
    require_text(domain['description'], 'validity_domain.description')
    if not isinstance(domain['variable'], str) or not NAME.fullmatch(domain['variable']):
        raise ValueError('validity_domain.variable must be an identifier')
    interval = domain['interval']
    if not isinstance(interval, list) or len(interval) != 2:
        raise ValueError('validity_domain.interval must be [lower, upper]')
    lower, upper = (rational(item, 'interval bound') for item in interval)
    if lower > upper:
        raise ValueError('validity_domain interval is empty')
    samples = domain['samples']
    if not isinstance(samples, list) or not 1 <= len(samples) <= MAX_SAMPLES:
        raise ValueError(f'validity_domain needs 1 to {MAX_SAMPLES} sample points')
    for point in samples:
        if not lower <= rational(point, 'sample point') <= upper:
            raise ValueError('Sample points must lie in the declared validity interval')
    if function['form'] is not None:
        validate_polynomial(function['form'], parameters, 'compensation_function.form')
        if function['form']['variable'] != domain['variable']:
            raise ValueError('Compensation form and validity domain must use the same variable')
    if payload['magnitude_convention'] not in {'signed', 'magnitude'}:
        raise ValueError('magnitude_convention must be signed or magnitude')
    if rational(payload['replacement_tolerance'], 'replacement_tolerance') < 0:
        raise ValueError('replacement_tolerance must be nonnegative')
    guards = payload['open_guards']
    if not isinstance(guards, list) or not guards:
        raise ValueError('A counterterm scheme must carry at least one open guard')
    for guard in guards:
        if not isinstance(guard, dict) or set(guard) != {'title', 'obligation'}:
            raise ValueError('Each open guard requires title and obligation')
        require_text(guard['title'], 'guard title')
        require_text(guard['obligation'], 'guard obligation')
    return payload


def version_identity(session, models, key):
    row = session.get(models.qstore_versions, key)
    if row is None:
        raise ValueError(f'Version {key} is not registered')
    obj = session.get(models.qstore_objects, row.object_id)
    identity = {'format': 'qstore-version-v1', 'object_id': row.object_id, 'kind': obj.object_type,
                'frame': row.frame, 'status': row.status, 'payload': json.loads(row.payload_json)}
    if digest(identity) != key:
        raise ValueError(f'Version {key} hash is invalid')
    return identity


def store_version(session, models, object_id, kind, frame, status, payload, source):
    identity = {'object_id': object_id, 'kind': kind, 'frame': frame, 'status': status, 'payload': payload}
    version = digest({'format': 'qstore-version-v1', **identity})
    obj = session.get(models.qstore_objects, object_id)
    if obj is not None and obj.object_type != kind:
        raise ValueError('Stable object identity cannot change type')
    if obj is None:
        session.add(models.qstore_objects(object_id=object_id, object_type=kind))
        session.flush()
    created = session.get(models.qstore_versions, version) is None
    if created:
        session.add(models.qstore_versions(version_hash=version, object_id=object_id,
                    payload_json=canonical(payload), status=status, frame=frame))
        session.flush()
        session.add(models.qstore_ledger(event_type='STORE', payload_json=canonical({'version_hash': version})))
    query = select(models.qstore_sources).filter_by(version_hash=version, source_path=source['path'],
        source_hash=source['sha256'], source_revision=source['revision'], locator=source['locator'])
    if session.scalar(query) is None:
        session.add(models.qstore_sources(version_hash=version, source_path=source['path'],
                    source_hash=source['sha256'], source_revision=source['revision'], locator=source['locator']))
        session.add(models.qstore_ledger(event_type='SOURCE', payload_json=canonical({'version_hash': version, **source})))
    return version, created


def register_scheme(path, repo, request):
    """Store one counterterm-scheme version and its open guards atomically."""
    if not isinstance(request, dict) or set(request) != {'object_id', 'frame', 'status', 'payload', 'source'}:
        raise ValueError('Counterterm registration requires object_id, frame, status, payload and source')
    for name in ('object_id', 'frame', 'status'):
        require_text(request[name], name)
    if request['status'] not in {'imported-unreviewed', 'declared', 'conditional'}:
        raise ValueError('Registration does not grant review or withdrawal status')
    if request['frame'] == 'unspecified':
        raise ValueError('A counterterm needs an explicit readout frame')
    payload = validate_scheme(request['payload'], request['frame'])
    source = source_record(repo, request['source'])
    guards = []
    with store_session(path) as (session, models):
        version, _ = store_version(session, models, request['object_id'], SCHEME, request['frame'],
                                   request['status'], payload, source)
        for guard in payload['open_guards']:
            guard_payload = {'title': guard['title'], 'obligation': guard['obligation'], 'source': source}
            key = digest({'format': 'qstore-guard-v1', 'subject': version, 'target': None,
                          'status': 'open', 'payload': guard_payload})
            if session.get(models.qstore_guards, key) is None:
                session.add(models.qstore_guards(guard_hash=key, subject_version=version, target_version=None,
                            status='open', payload_json=canonical(guard_payload)))
                session.add(models.qstore_ledger(event_type='GUARD', payload_json=canonical({'guard_hash': key})))
            guards.append(key)
    return {'version_hash': version, 'lifecycle': 'placeholder', 'guards': guards}


def transitions(session, models, scheme):
    """Return the ordered lifecycle chain of one scheme version."""
    object_id = f'{TRANSITION}:{scheme}'
    rows = {row.version_hash: json.loads(row.payload_json) for row in session.scalars(
        select(models.qstore_versions).where(models.qstore_versions.object_id == object_id))}
    by_previous = {}
    for key, payload in rows.items():
        if payload['scheme'] != scheme:
            raise ValueError('Transition belongs to another scheme')
        by_previous.setdefault(payload['previous'], []).append(key)
    chain, cursor = [], None
    while cursor in by_previous:
        heads = by_previous[cursor]
        if len(heads) != 1:
            raise ValueError('Counterterm lifecycle has conflicting transitions')
        cursor = heads[0]
        chain.append({'transition_hash': cursor, **rows[cursor]})
    if len(chain) != len(rows):
        raise ValueError('Counterterm lifecycle contains detached transitions')
    return chain


def lifecycle(session, models, scheme):
    chain = transitions(session, models, scheme)
    head = chain[-1] if chain else None
    return {'scheme': scheme, 'status': head['to'] if head else 'placeholder',
            'head': head['transition_hash'] if head else None,
            'replacement': head['replacement'] if head else None, 'chain': chain}


def relation_heads(session, models):
    """Current relation status after reviews, as in source_impact."""
    status = {}
    for row in session.scalars(select(models.qstore_relations)):
        review = latest_review(session, models, 'relation', row.relation_hash)
        status[row.relation_hash] = review.status if review else row.status
    return status


def edges(session, models):
    status = relation_heads(session, models)
    forward, backward = {}, {}
    for row in session.scalars(select(models.qstore_relations)):
        if row.relation_type in DEPENDENCY_EDGES and status[row.relation_hash] in {'declared', 'reviewed'}:
            forward.setdefault(row.source_version, set()).add((row.target_version, row.relation_type))
            backward.setdefault(row.target_version, set()).add(row.source_version)
    return forward, backward


def object_type(session, models, version):
    row = session.get(models.qstore_versions, version)
    return None if row is None else session.get(models.qstore_objects, row.object_id).object_type


def dependents(session, models, roots):
    _, backward = edges(session, models)
    seen, pending = set(), list(roots)
    while pending:
        for key in backward.get(pending.pop(), set()) - seen - set(roots):
            seen.add(key)
            pending.append(key)
    return sorted(seen)


def open_guards(session, models, version):
    result = []
    for guard in session.scalars(select(models.qstore_guards).where(
            models.qstore_guards.subject_version == version).order_by(models.qstore_guards.guard_hash)):
        review = latest_review(session, models, 'guard', guard.guard_hash)
        status = review.status if review else guard.status
        if status != 'satisfied':
            result.append({'guard_hash': guard.guard_hash, 'status': status,
                           'title': json.loads(guard.payload_json)['title']})
    return result


def resolve(session, models, version):
    """Follow dependencies of one version; collect counterterms and inherited guards."""
    forward, _ = edges(session, models)
    seen, pending, schemes = {version}, [version], {}
    while pending:
        current = pending.pop()
        targets = set(forward.get(current, set()))
        if object_type(session, models, current) == SCHEME:
            state = lifecycle(session, models, current)
            inherits = state['status'] != 'structurally_matched'
            scheme_payload = version_identity(session, models, current)['payload']
            schemes[current] = {'scheme': current, 'status': state['status'], 'inherits_guards': inherits,
                                'replacement': state['replacement'], 'fitted_on': scheme_payload['fitted_on'],
                                'known_tensions': scheme_payload['known_tensions'],
                                'guards': open_guards(session, models, current) if inherits else []}
            if state['replacement']:
                # Once matched, the replacement's own guards and prerequisites take over.
                targets.add((state['replacement'], 'replacement'))
        for target, _ in sorted(targets):
            if target not in seen:
                seen.add(target)
                pending.append(target)
    inherited = sorted({guard['guard_hash'] for item in schemes.values() for guard in item['guards']})
    replacement_guards = sorted({guard['guard_hash'] for item in schemes.values() if item['replacement']
                                 for guard in open_guards(session, models, item['replacement'])})
    return {'version': version, 'counterterms': [schemes[key] for key in sorted(schemes)],
            'inherited_guards': inherited, 'replacement_guards': replacement_guards,
            'deprecated_dependencies': sorted(key for key, item in schemes.items() if item['status'] == 'deprecated'),
            'closure': sorted(seen), 'scope': SCOPE}


def resolve_dependencies(path, version):
    require_text(version, 'version')
    with store_session(path) as (session, models):
        version_identity(session, models, version)
        return resolve(session, models, version)


def guard_snapshot(session, models, versions):
    result = []
    for key in sorted(versions):
        for guard in open_guards(session, models, key):
            result.append({'version': key, **guard})
    return result


def store_receipt(session, models, checker, result, receipt, inputs, event):
    key = digest(receipt)
    if session.get(models.qstore_checks, key) is None:
        session.add(models.qstore_checks(receipt_hash=key, checker=checker,
                    checker_hash=receipt['checker_hash'], result=result, receipt_json=canonical(receipt)))
        session.flush()
        for version in sorted(inputs):
            session.add(models.qstore_check_inputs(receipt_hash=key, version_hash=version))
        session.add(models.qstore_ledger(event_type=event, payload_json=canonical({'receipt_hash': key})))
    return key


def checker_hash():
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def check_residual(path, request):
    """Evaluate Delta = F - delta exactly on the declared samples of the validity domain."""
    if not isinstance(request, dict) or set(request) != {'scheme', 'replacement'}:
        raise ValueError('Residual check requires scheme and replacement version hashes')
    for name, value in request.items():
        require_text(value, name)
    inputs, values, error, result, verdict = {}, [], None, 'blocked', 'undetermined'
    with store_session(path) as (session, models):
        scheme = version_identity(session, models, request['scheme'])
        replacement = version_identity(session, models, request['replacement'])
        inputs = {request['scheme']: scheme, request['replacement']: replacement}
        if scheme['kind'] != SCHEME:
            raise ValueError('scheme must be a counterterm-scheme version')
        payload = scheme['payload']
        tolerance = rational(payload['replacement_tolerance'], 'replacement_tolerance')
        maximum = None
        try:
            if replacement['kind'] != 'seed' or replacement['payload']['value_type'] != POLYNOMIAL:
                raise ValueError(f'Replacement must be a seed with value_type {POLYNOMIAL}')
            if replacement['frame'] != scheme['frame']:
                raise ValueError('Replacement and counterterm frames differ; declare a frame map first (Konvention F)')
            function = payload['compensation_function']
            if function['form'] is None:
                raise ValueError('Counterterm has no evaluable form')
            structure = replacement['payload']['value']
            validate_polynomial(structure, {}, 'replacement')
            if structure['variable'] != payload['validity_domain']['variable']:
                raise ValueError('Replacement uses another variable than the validity domain')
            magnitude_failures = []
            fit = payload['fitted_on'] or {'uncertainty': {}}
            sigma = {name: rational(value, 'uncertainty') for name, value in fit['uncertainty'].items()}
            coefficients = function['form']['coefficients']
            for point in payload['validity_domain']['samples']:
                x = rational(point, 'sample point')
                delta = evaluate(function['form'], function['parameters'], x)
                if delta is None:
                    raise ValueError('A counterterm parameter has no value; the residual is undetermined')
                structural = evaluate(structure, {}, x)
                if payload['magnitude_convention'] == 'magnitude' and delta < 0:
                    magnitude_failures.append(str(x))
                # delta is linear in each named coefficient: |d delta / d theta_k| = |sum of x^j| over its slots.
                band = sum((abs(sum(x ** j for j, entry in enumerate(coefficients) if entry == name)) * value
                            for name, value in sigma.items()), Fraction(0))
                shift = structural - delta
                values.append({'point': str(x), 'delta': str(delta), 'structure': str(structural),
                               'residual': str(shift), 'fit_band': str(band),
                               'within_tolerance': abs(shift) <= tolerance, 'within_fit_band': abs(shift) <= band})
            maximum = max(abs(Fraction(item['residual'])) for item in values)
            within = maximum <= tolerance
            result = 'passed' if within and not magnitude_failures else 'failed'
            if within:
                verdict = 'compatible-within-tolerance'
            elif all(item['within_fit_band'] for item in values):
                verdict = 'exceeds-tolerance-within-fit-uncertainty'
            else:
                verdict = 'deviates-from-fit'
            if magnitude_failures:
                error = ('Negative |delta_i| at ' + ', '.join(magnitude_failures)
                         + '; an orientation sign may have been absorbed')
        except (ValueError, KeyError, TypeError) as exc:
            error, values = str(exc), []
        receipt = {'format': 'qstore-check-v1', 'checker': RESIDUAL_CHECKER, 'checker_hash': checker_hash(),
                   'request': request, 'inputs': inputs, 'result': result, 'error': error,
                   'residuals': values, 'max_abs_residual': None if maximum is None else str(maximum),
                   'tolerance': str(tolerance), 'verdict': verdict,
                   'fitted_on': payload['fitted_on'], 'known_tensions': payload['known_tensions'],
                   'adoption': 'Only compatible-within-tolerance may support structurally_matched; any other '
                               'verdict keeps delta_i and reports Delta_i as the deviation of the derivation',
                   'guards': guard_snapshot(session, models, inputs),
                   'assertion_tested': '|F(x) - delta(x)| <= tolerance at every declared sample point x',
                   'scope': 'Finitely many declared rational samples; not a bound on the whole validity domain; '
                            + SCOPE}
        key = store_receipt(session, models, RESIDUAL_CHECKER, result, receipt, inputs, 'VERIFY')
    return {'receipt_hash': key, **receipt}


def register_transition(path, repo, request):
    """Append one lifecycle step and flag downstream versions for re-audit."""
    fields = {'scheme', 'previous', 'status', 'reviewer', 'reason', 'evidence', 'replacement', 'receipt'}
    if not isinstance(request, dict) or set(request) != fields:
        raise ValueError(f'Transition requires exactly {sorted(fields)}')
    for name in ('scheme', 'reviewer', 'reason'):
        require_text(request[name], name)
    if request['status'] not in STATUSES or request['status'] == 'placeholder':
        raise ValueError('Target status must be partially_constrained, structurally_matched or deprecated')
    matched = request['status'] == 'structurally_matched'
    for name in ('previous', 'replacement', 'receipt'):
        if request[name] is not None:
            require_text(request[name], name)
    if matched != (request['replacement'] is not None) or matched != (request['receipt'] is not None):
        raise ValueError('Exactly structurally_matched requires a replacement and a passed residual receipt')
    evidence = source_record(repo, request['evidence'])
    with store_session(path) as (session, models):
        scheme = version_identity(session, models, request['scheme'])
        if scheme['kind'] != SCHEME:
            raise ValueError('Transition subject must be a counterterm-scheme version')
        state = lifecycle(session, models, request['scheme'])
        payload = {'scheme': request['scheme'], 'previous': request['previous'], 'from': state['status'],
                   'to': request['status'], 'reviewer': request['reviewer'], 'reason': request['reason'],
                   'replacement': request['replacement'], 'receipt': request['receipt'],
                   'assessment': 'declared-human-or-agent-transition'}
        for item in state['chain']:
            existing = {key: item[key] for key in ('scheme', 'previous', 'to', 'reviewer', 'reason',
                                                    'replacement', 'receipt')}
            if existing == {key: payload[key] for key in existing}:
                return {'transition_hash': item['transition_hash'], 'status': item['to'], 'reaudit': None}
        if request['previous'] != state['head']:
            raise ValueError('Stale transition predecessor; read the current lifecycle head')
        if request['status'] not in ALLOWED[state['status']]:
            raise ValueError(f'Transition {state["status"]} -> {request["status"]} is not allowed')
        if matched:
            row = session.get(models.qstore_checks, request['receipt'])
            if row is None:
                raise ValueError('Unknown residual receipt')
            receipt = json.loads(row.receipt_json)
            if digest(receipt) != request['receipt'] or receipt['checker'] != RESIDUAL_CHECKER:
                raise ValueError('Receipt is not a valid residual receipt')
            if receipt['request'] != {'scheme': request['scheme'], 'replacement': request['replacement']}:
                raise ValueError('Residual receipt checks another scheme or replacement')
            if receipt['result'] != 'passed':
                raise ValueError('Residual exceeds tolerance or is undetermined; the shift Delta is reported in the receipt')
        key, _ = store_version(session, models, f'{TRANSITION}:{request["scheme"]}', TRANSITION,
                               scheme['frame'], 'declared', payload, evidence)
        affected = dependents(session, models, [request['scheme']])
        reaudit = {'format': 'qstore-counterterm-reaudit-v1', 'scheme': request['scheme'], 'transition': key,
                   'from': state['status'], 'to': request['status'], 'affected_versions': affected,
                   'meaning': 'review candidates; recompute Delta_i and inherited guards, nothing is revoked'}
        session.add(models.qstore_ledger(event_type='COUNTERTERM-REAUDIT', payload_json=canonical(reaudit)))
    return {'transition_hash': key, 'status': request['status'], 'reaudit': reaudit}


def read_lifecycle(path, scheme):
    with store_session(path) as (session, models):
        if version_identity(session, models, scheme)['kind'] != SCHEME:
            raise ValueError('Not a counterterm-scheme version')
        return lifecycle(session, models, scheme)


def check_term_roles(path, request):
    """Check structural_core / counterterm_compensation markings of one statement version."""
    if not isinstance(request, dict) or set(request) != {'statement', 'terms'}:
        raise ValueError('Term-role check requires statement and terms')
    require_text(request['statement'], 'statement')
    terms = request['terms']
    if not isinstance(terms, list) or not terms:
        raise ValueError('terms must be a nonempty list')
    findings = []
    with store_session(path) as (session, models):
        statement = version_identity(session, models, request['statement'])
        if statement['kind'] in {SCHEME, TRANSITION}:
            raise ValueError('Term roles describe statements, not counterterm records')
        forward, _ = edges(session, models)
        direct = {target for target, kind in forward.get(request['statement'], set()) if kind == EDGE}
        inputs = {request['statement']: statement}
        for index, term in enumerate(terms):
            if not isinstance(term, dict) or set(term) != {'label', 'role', 'scheme', 'absorbs', 'orientation'}:
                raise ValueError('Each term requires label, role, scheme, absorbs and orientation')
            require_text(term['label'], 'label')
            if not isinstance(term['absorbs'], list):
                raise ValueError('absorbs must be a list of scheme version hashes')
            orientation = term['orientation']
            if orientation is not None and (not isinstance(orientation, dict)
                                            or set(orientation) != {'symbol', 'absorbed'}
                                            or not isinstance(orientation['absorbed'], bool)):
                raise ValueError('orientation must be null or {symbol, absorbed: bool}')

            def fail(rule, message):
                findings.append({'term': index, 'label': term['label'], 'rule': rule, 'message': message})

            role = term['role']
            if role not in TERM_ROLES:
                if role in INDEX_ROLES:
                    fail('T1-index-role', f'{role} is a front/back index role of qam-role-audit/2, not a term role')
                else:
                    fail('T1-unknown-role', f'Unknown term role {role!r}')
                continue
            if role == 'counterterm_compensation':
                scheme = term['scheme']
                if not isinstance(scheme, str) or object_type(session, models, scheme) != SCHEME:
                    fail('T2-missing-scheme', 'Compensation term must name a registered counterterm-scheme version')
                    continue
                inputs[scheme] = version_identity(session, models, scheme)
                if scheme not in direct:
                    fail('T2-undeclared-dependency', f'Statement lacks a declared {EDGE} edge to this scheme')
                if term['absorbs']:
                    fail('T2-compensation-absorbs', 'Only a structural_core term can absorb a matched scheme')
                if orientation is not None and orientation['absorbed']:
                    fail('T4-orientation-absorbed',
                         f'Orientation sign {orientation["symbol"]} absorbed into |delta_i|; keep o_R explicit')
                if inputs[scheme]['payload']['magnitude_convention'] == 'magnitude' and orientation is None:
                    fail('T4-orientation-missing', 'Magnitude convention requires an explicit orientation factor')
            else:
                if term['scheme'] is not None:
                    fail('T3-core-with-scheme', 'structural_core terms do not carry a counterterm scheme')
                for scheme in term['absorbs']:
                    if not isinstance(scheme, str) or object_type(session, models, scheme) != SCHEME:
                        fail('T3-unknown-absorbed', 'Absorbed entry is not a counterterm-scheme version')
                        continue
                    inputs[scheme] = version_identity(session, models, scheme)
                    status = lifecycle(session, models, scheme)['status']
                    if status != 'structurally_matched':
                        fail('T3-unlogged-absorption',
                             f'Absorbing a {status} counterterm into the core needs a logged structural match')
                if orientation is not None and orientation['absorbed']:
                    fail('T4-orientation-absorbed', 'Orientation sign must stay an explicit factor')
        resolved = resolve(session, models, request['statement'])
        compensation = {term.get('scheme') for term in terms if isinstance(term, dict)
                        and term.get('role') == 'counterterm_compensation'}
        for item in resolved['counterterms']:
            if item['status'] != 'structurally_matched' and not compensation:
                findings.append({'term': None, 'label': None, 'rule': 'T5-silent-dependency',
                                 'message': f'Only structural_core terms, but depends on {item["status"]} '
                                            f'counterterm {item["scheme"]}'})
        result = 'failed' if findings else 'passed'
        receipt = {'format': 'qstore-check-v1', 'checker': ROLE_CHECKER, 'checker_hash': checker_hash(),
                   'request': request, 'inputs': inputs, 'result': result, 'findings': findings,
                   'inherited_guards': resolved['inherited_guards'],
                   'assertion_tested': 'Term-role bookkeeping rules T1-T5; separate from qam-role-audit/2 index roles',
                   'scope': 'Declared markings only; no parsing of LaTeX and no physical check; ' + SCOPE}
        key = store_receipt(session, models, ROLE_CHECKER, result, receipt, inputs, 'VERIFY')
    return {'receipt_hash': key, **receipt}


def check_blindness(path, request):
    """Report not_blind when a statement is tested against data its counterterms were fitted on."""
    if not isinstance(request, dict) or set(request) != {'statement', 'tested_against'}:
        raise ValueError('Blindness check requires statement and tested_against')
    require_text(request['statement'], 'statement')
    data = request['tested_against']
    if not isinstance(data, list) or not data:
        raise ValueError('tested_against must list the comparison data')
    for item in data:
        if not isinstance(item, dict) or set(item) != {'label', 'source', 'version'}:
            raise ValueError('Each comparison datum requires label, source and version')
        for name, value in item.items():
            require_text(value, f'comparison datum {name}')
    with store_session(path) as (session, models):
        inputs = {request['statement']: version_identity(session, models, request['statement'])}
        resolved = resolve(session, models, request['statement'])
        findings = []
        for scheme in resolved['counterterms']:
            inputs[scheme['scheme']] = version_identity(session, models, scheme['scheme'])
            fit = scheme['fitted_on']
            if fit is None:
                continue
            fitted = {(item['source'], item['label']): item for item in fit['data']}
            for item in data:
                hit = fitted.get((item['source'], item['label']))
                if hit is not None:
                    findings.append({'scheme': scheme['scheme'], 'status': scheme['status'], 'datum': item,
                                     'fitted_version': hit['version'],
                                     'same_version': hit['version'] == item['version'], 'scan': fit['scan']})
        verdict = 'not_blind' if findings else 'blind-with-respect-to-registered-fits'
        result = 'failed' if findings else 'passed'
        receipt = {'format': 'qstore-check-v1', 'checker': BLINDNESS_CHECKER, 'checker_hash': checker_hash(),
                   'request': request, 'inputs': inputs, 'result': result, 'verdict': verdict,
                   'findings': findings, 'inherited_guards': resolved['inherited_guards'],
                   'assertion_tested': 'No comparison datum (source, label) occurs in fitted_on of a counterterm '
                                       'in the dependency closure',
                   'scope': 'Only registered fits are known; unregistered tuning cannot be excluded. '
                            'A not_blind result must be reported as such (AGENTS: Nicht blind = offen sagen); '
                            + SCOPE}
        key = store_receipt(session, models, BLINDNESS_CHECKER, result, receipt, inputs, 'VERIFY')
    return {'receipt_hash': key, **receipt}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('command', choices=['store', 'transition', 'residual', 'roles', 'blindness', 'resolve',
                                            'lifecycle'])
    parser.add_argument('--db', default='build/qam.sqlite3')
    parser.add_argument('--repo', default='.')
    parser.add_argument('--request', help='JSON request file (store, transition, residual, roles)')
    parser.add_argument('--hash', help='Version hash (resolve, lifecycle)')
    args = parser.parse_args(argv)
    request = json.loads(Path(args.request).read_text(encoding='utf-8')) if args.request else None
    if args.command == 'store':
        result = register_scheme(args.db, args.repo, request)
    elif args.command == 'transition':
        result = register_transition(args.db, args.repo, request)
    elif args.command == 'residual':
        result = check_residual(args.db, request)
    elif args.command == 'blindness':
        result = check_blindness(args.db, request)
    elif args.command == 'roles':
        result = check_term_roles(args.db, request)
    elif args.command == 'resolve':
        result = resolve_dependencies(args.db, args.hash)
    else:
        result = read_lifecycle(args.db, args.hash)
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2, sort_keys=True)
    print()
    return 1 if isinstance(result, dict) and result.get('result') == 'failed' else 0


if __name__ == '__main__':
    sys.exit(main())
