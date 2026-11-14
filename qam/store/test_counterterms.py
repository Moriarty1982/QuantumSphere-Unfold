"""CT-000-TEST: registry fixture only. No physical counterterm is registered here."""

import copy
import hashlib
import json
from pathlib import Path
import sqlite3
from tempfile import TemporaryDirectory
import unittest

from sqlalchemy import select

from qam.store.counterterms import (check_blindness, check_residual, check_term_roles, read_lifecycle,
                                    register_scheme, register_transition, resolve_dependencies)
from qam.store.orm import store_session
from qam.store.registry import register, register_link
from qam.store.snapshots import create_snapshot
from qam.tools.store_db import apply_sql, initialize


CLAIM = 'Dummy statement S_0 uses the placeholder delta_0.'
FOLLOWER = 'Dummy statement S_1 requires S_0.'
CORE = 'Dummy core statement C_0 has no compensation term.'
DATUM = {'label': 'dummy-target-y', 'source': 'fixture-data', 'version': 'v0', 'value': '3/5 +- 1/100'}
OTHER = {'label': 'dummy-target-z', 'source': 'fixture-data', 'version': 'v0', 'value': '1 +- 1/10'}


def provenance(path):
    return {'path': path.name, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'revision': 'CT-000-TEST', 'locator': 'whole file'}


def scheme_payload():
    return {
        'title': 'CT-000-TEST placeholder delta_0',
        'target_sector': 'test-fixture-only',
        'operator_basis': {'kind': 'lagrangian_operator', 'expression': r'\mathcal{O}_0 = 1 (dummy)',
                           'frame': 'test-frame'},
        'compensation_function': {
            'symbolic': r'\delta_0(x) = \theta_0 + \theta_1 x',
            'parameters': {
                'theta_0': {'value': '1/10', 'bounds': ['-1', '1'], 'role': 'fit_parameter'},
                'theta_1': {'value': '1/2', 'bounds': ['0', '1'], 'role': 'regulator_cutoff'},
            },
            'form': {'type': 'qam-polynomial-v1', 'variable': 'x', 'coefficients': ['theta_0', 'theta_1']},
        },
        'reference_scale': 'x_0 = 0 (dummy)',
        'matching_condition': r'\delta_0(x_0) = \theta_0 (dummy)',
        'rg_flow': None,
        'validity_domain': {'variable': 'x', 'interval': ['0', '1'], 'samples': ['0', '1/2', '1'],
                            'description': 'dummy unit interval'},
        'magnitude_convention': 'signed',
        'replacement_tolerance': '1/100',
        'open_guards': [{'title': 'GUARD-CT000-NO-DERIVATION', 'obligation': 'Fixture placeholder, never derived'},
                        {'title': 'GUARD-LOCAL-READOUT-ONLY', 'obligation': 'Local test readout only'}],
        'assumptions': ['Test fixture without physical meaning'],
        'scope': 'CT-000-TEST only',
        'fitted_on': {'method': 'dummy least squares', 'parameters': ['theta_0'], 'data': [DATUM],
                      'uncertainty': {'theta_0': '1/50'}, 'scan': None},
        'known_tensions': [],
    }


def discrete_payload():
    payload = scheme_payload()
    payload['title'] = 'CT-000-TEST discrete readout unit'
    payload['operator_basis'] = {'kind': 'readout', 'expression': 'dummy readout flux Phi_test',
                                 'frame': 'test-frame'}
    payload['compensation_function'] = {
        'symbolic': r'\delta_0 = u (dummy unit choice)',
        'parameters': {'u': {'value': '1/2', 'options': ['1/4', '1/2', '1'], 'role': 'discrete_choice'}},
        'form': {'type': 'qam-polynomial-v1', 'variable': 'x', 'coefficients': ['u']},
    }
    payload['fitted_on'] = {'method': 'dummy scan over units', 'parameters': ['u'], 'data': [DATUM, OTHER],
                            'uncertainty': {}, 'scan': {'trials': 12, 'hits': 1, 'chance_expectation': '1/4'}}
    payload['known_tensions'] = [{'description': 'dummy own convention disagrees', 'convention': 'fixture rule',
                                  'delta': '3 units', 'source': 'ct000.tex'}]
    return payload


class CountertermRegistryTests(unittest.TestCase):
    def setUp(self):
        self.folder = TemporaryDirectory()
        self.root = Path(self.folder.name)
        self.db = self.root / 'store.sqlite3'
        self.source = self.root / 'ct000.tex'
        self.source.write_text('\n'.join([CLAIM, FOLLOWER, CORE, 'Mock structure function F_0.']), encoding='utf-8')
        self.evidence = self.root / 'review.txt'
        self.evidence.write_text('CT-000-TEST review note', encoding='utf-8')

    def tearDown(self):
        self.folder.cleanup()

    def scheme_request(self, payload=None, object_id='CT-000-TEST'):
        return {'object_id': object_id, 'frame': 'test-frame', 'status': 'conditional',
                'payload': payload or scheme_payload(), 'source': provenance(self.source)}

    def statement(self, object_id, latex, dependencies=()):
        return register(self.db, self.root, {'object_id': object_id, 'kind': 'claim', 'frame': 'test-frame',
            'status': 'conditional', 'source': provenance(self.source),
            'payload': {'title': object_id, 'latex': latex, 'assumptions': [],
                        'dependencies': list(dependencies)}})['version_hash']

    def structure(self, object_id, coefficients):
        definition = register(self.db, self.root, {'object_id': object_id + '-definition', 'kind': 'definition',
            'frame': 'test-frame', 'status': 'conditional', 'source': provenance(self.source),
            'payload': {'title': 'Mock F_0', 'body': 'Mock structure function', 'scope': 'test',
                        'assumptions': []}})['version_hash']
        return register(self.db, self.root, {'object_id': object_id, 'kind': 'seed', 'frame': 'test-frame',
            'status': 'conditional', 'source': provenance(self.source),
            'payload': {'title': 'F_0', 'value': {'type': 'qam-polynomial-v1', 'variable': 'x',
                                                  'coefficients': coefficients},
                        'value_type': 'qam-polynomial-v1', 'origin': 'mock', 'assumptions': [],
                        'definition_version': definition}})['version_hash']

    def transition(self, scheme, previous, status, replacement=None, receipt=None):
        return register_transition(self.db, self.root, {'scheme': scheme, 'previous': previous, 'status': status,
            'reviewer': 'fixture', 'reason': f'move to {status}', 'evidence': provenance(self.evidence),
            'replacement': replacement, 'receipt': receipt})

    def test_schema_v7_and_upgrade_from_v6(self):
        self.assertEqual(initialize(self.db)['schema'], 7)
        resources = Path(__file__).resolve().parent
        legacy = self.root / 'legacy.sqlite3'
        db = sqlite3.connect(legacy)
        catalogue = json.loads((resources / 'catalogue_v1.json').read_text(encoding='utf-8'))
        apply_sql(db, resources / 'schema_v1.sql')
        db.executemany('INSERT INTO qstore_object_types VALUES (?,?)', catalogue.items())
        for version in range(2, 7):
            apply_sql(db, resources / f'schema_v{version}.sql')
        db.commit()
        db.close()
        self.assertEqual(initialize(legacy)['object_types'], len(catalogue) + 2)
        with store_session(legacy) as (session, models):
            names = set(session.scalars(select(models.qstore_object_types.name)))
        self.assertTrue({'counterterm-scheme', 'counterterm-transition'} <= names)

    def test_fixture_registration_inheritance_and_matching(self):
        # (a) register the placeholder delta_0 with its open guards.
        stored = register_scheme(self.db, self.root, self.scheme_request())
        scheme = stored['version_hash']
        self.assertEqual(len(stored['guards']), 2)
        self.assertEqual(register_scheme(self.db, self.root, self.scheme_request())['version_hash'], scheme)
        self.assertEqual(read_lifecycle(self.db, scheme)['status'], 'placeholder')

        # (b) guard propagation to dummy statements, including a transitive one.
        claim = self.statement('S_0', CLAIM)
        follower = self.statement('S_1', FOLLOWER, [claim])
        register_link(self.db, {'source': claim, 'target': scheme, 'kind': 'depends-on-counterterm',
                                'status': 'declared', 'description': 'S_0 uses delta_0'})
        with self.assertRaises(ValueError):
            register_link(self.db, {'source': follower, 'target': claim, 'kind': 'depends-on-counterterm',
                                    'status': 'declared', 'description': 'target is not a scheme'})
        for version in (claim, follower):
            resolved = resolve_dependencies(self.db, version)
            self.assertEqual(resolved['inherited_guards'], sorted(stored['guards']))
            self.assertEqual(resolved['counterterms'][0]['status'], 'placeholder')

        # Term roles: compensation term passes, silent core-only use fails.
        compensation = {'label': 'delta_0 O_0', 'role': 'counterterm_compensation', 'scheme': scheme,
                        'absorbs': [], 'orientation': None}
        core = {'label': 'L_core', 'role': 'structural_core', 'scheme': None, 'absorbs': [], 'orientation': None}
        self.assertEqual(check_term_roles(self.db, {'statement': claim, 'terms': [core, compensation]})['result'],
                         'passed')
        silent = check_term_roles(self.db, {'statement': follower, 'terms': [core]})
        self.assertEqual([item['rule'] for item in silent['findings']], ['T5-silent-dependency'])
        rules = {item['rule'] for item in check_term_roles(self.db, {'statement': claim, 'terms': [
            {**core, 'role': 'operator'},
            {**core, 'absorbs': [scheme]},
            {**compensation, 'orientation': {'symbol': 'o_R', 'absorbed': True}}]})['findings']}
        self.assertEqual(rules, {'T1-index-role', 'T3-unlogged-absorption', 'T4-orientation-absorbed'})
        undeclared = check_term_roles(self.db, {'statement': follower, 'terms': [compensation]})
        self.assertIn('T2-undeclared-dependency', {item['rule'] for item in undeclared['findings']})

        # Blindness: testing against the fitted datum is not blind, also transitively.
        fitted = {key: DATUM[key] for key in ('label', 'source', 'version')}
        unrelated = {'label': 'dummy-target-w', 'source': 'fixture-data', 'version': 'v0'}
        for version in (claim, follower):
            report = check_blindness(self.db, {'statement': version, 'tested_against': [fitted]})
            self.assertEqual((report['result'], report['verdict']), ('failed', 'not_blind'))
        clean = check_blindness(self.db, {'statement': claim, 'tested_against': [unrelated]})
        self.assertEqual(clean['verdict'], 'blind-with-respect-to-registered-fits')

        # (c) mock structure F_0 and residual Delta_0 = F_0 - delta_0, against tolerance and fit band.
        close = self.structure('F_0', ['21/200', '1/2'])
        middle = self.structure('F_0-middle', ['23/200', '1/2'])
        far = self.structure('F_0-far', ['3/10', '1/2'])
        passed = check_residual(self.db, {'scheme': scheme, 'replacement': close})
        self.assertEqual((passed['result'], passed['verdict']), ('passed', 'compatible-within-tolerance'))
        self.assertEqual({item['residual'] for item in passed['residuals']}, {'1/200'})
        self.assertEqual({item['fit_band'] for item in passed['residuals']}, {'1/50'})
        inside = check_residual(self.db, {'scheme': scheme, 'replacement': middle})
        self.assertEqual((inside['result'], inside['verdict']),
                         ('failed', 'exceeds-tolerance-within-fit-uncertainty'))
        failed = check_residual(self.db, {'scheme': scheme, 'replacement': far})
        self.assertEqual((failed['result'], failed['max_abs_residual'], failed['verdict']),
                         ('failed', '1/5', 'deviates-from-fit'))

        # Lifecycle: no shortcut, re-audit flags, receipt gate, stale predecessor.
        with self.assertRaises(ValueError):
            self.transition(scheme, None, 'structurally_matched', close, passed['receipt_hash'])
        step = self.transition(scheme, None, 'partially_constrained')
        self.assertEqual(step['reaudit']['affected_versions'], sorted([claim, follower]))
        self.assertIsNone(self.transition(scheme, None, 'partially_constrained')['reaudit'])
        with self.assertRaises(ValueError):
            self.transition(scheme, step['transition_hash'], 'structurally_matched', far, failed['receipt_hash'])
        with self.assertRaises(ValueError):
            self.transition(scheme, step['transition_hash'], 'structurally_matched',
                            middle, inside['receipt_hash'])
        with self.assertRaises(ValueError):
            self.transition(scheme, step['transition_hash'], 'structurally_matched', far, passed['receipt_hash'])
        with self.assertRaises(ValueError):
            self.transition(scheme, None, 'deprecated')
        matched = self.transition(scheme, step['transition_hash'], 'structurally_matched',
                                  close, passed['receipt_hash'])
        resolved = resolve_dependencies(self.db, follower)
        self.assertEqual(resolved['inherited_guards'], [])
        self.assertEqual(resolved['counterterms'][0]['replacement'], close)
        self.assertIn(close, resolved['closure'])
        self.assertEqual(check_term_roles(self.db, {'statement': claim, 'terms': [
            {**core, 'absorbs': [scheme]}]})['result'], 'passed')
        with store_session(self.db) as (session, models):
            events = [json.loads(row.payload_json) for row in session.scalars(select(models.qstore_ledger).where(
                models.qstore_ledger.event_type == 'COUNTERTERM-REAUDIT'))]
        self.assertEqual([event['to'] for event in events], ['partially_constrained', 'structurally_matched'])

        # Deprecation re-opens inheritance and is terminal.
        retired = self.transition(scheme, matched['transition_hash'], 'deprecated')
        resolved = resolve_dependencies(self.db, follower)
        self.assertEqual(resolved['inherited_guards'], sorted(stored['guards']))
        self.assertEqual(resolved['deprecated_dependencies'], [scheme])
        with self.assertRaises(ValueError):
            self.transition(scheme, retired['transition_hash'], 'partially_constrained')
        self.assertEqual(len(read_lifecycle(self.db, scheme)['chain']), 3)
        self.assertTrue(create_snapshot(self.db, 'CT-000-TEST')['snapshot_hash'])

    def test_validator_rejections(self):
        def broken(change):
            payload = scheme_payload()
            change(payload)
            with self.assertRaises(ValueError):
                register_scheme(self.db, self.root, self.scheme_request(payload, 'CT-000-BAD'))

        parameters = lambda payload: payload['compensation_function']['parameters']
        broken(lambda payload: payload.update(open_guards=[]))
        broken(lambda payload: payload.pop('scope'))
        broken(lambda payload: parameters(payload)['theta_0'].update(value='2'))
        broken(lambda payload: parameters(payload)['theta_0'].update(bounds=['1', '-1']))
        broken(lambda payload: parameters(payload)['theta_0'].update(value=0.1))
        broken(lambda payload: parameters(payload)['theta_1'].update(role='orientation_sign'))
        broken(lambda payload: payload['validity_domain'].update(samples=['2']))
        broken(lambda payload: payload.update(magnitude_convention='absolute'))
        broken(lambda payload: payload['compensation_function']['form'].update(coefficients=['theta_9']))
        broken(lambda payload: payload['operator_basis'].update(frame='other-frame'))
        broken(lambda payload: payload['operator_basis'].update(kind='lagrangian'))
        broken(lambda payload: payload['fitted_on'].update(parameters=['theta_9']))
        broken(lambda payload: payload['fitted_on'].update(data=[]))
        broken(lambda payload: payload['fitted_on'].update(uncertainty={'theta_1': '1/10'}))
        broken(lambda payload: payload['fitted_on'].update(scan={'trials': 3, 'hits': 4, 'chance_expectation': '0'}))
        broken(lambda payload: payload.update(known_tensions=[{'description': 'missing fields'}]))
        broken(lambda payload: parameters(payload).update(
            k={'value': '2', 'options': ['1', '3'], 'role': 'discrete_choice'}))
        broken(lambda payload: parameters(payload).update(
            k={'value': None, 'options': ['1'], 'role': 'discrete_choice'}))
        with store_session(self.db) as (session, models):
            self.assertIsNone(session.get(models.qstore_objects, 'CT-000-BAD'))
        with self.assertRaises(ValueError):
            register(self.db, self.root, {'object_id': 'CT-000-BAD', 'kind': 'counterterm-scheme',
                'frame': 'test-frame', 'status': 'conditional', 'payload': scheme_payload(),
                'source': provenance(self.source)})

    def test_magnitude_convention_rejects_absorbed_sign(self):
        payload = scheme_payload()
        payload['magnitude_convention'] = 'magnitude'
        payload['compensation_function']['parameters']['theta_1'].update(value='-1/2', bounds=['-1', '1'])
        scheme = register_scheme(self.db, self.root, self.scheme_request(payload, 'CT-000-MAG'))['version_hash']
        structure = self.structure('F_0-mag', ['1/10', '-1/2'])
        receipt = check_residual(self.db, {'scheme': scheme, 'replacement': structure})
        self.assertEqual(receipt['result'], 'failed')
        self.assertIn('orientation sign', receipt['error'])
        claim = self.statement('S_0', CLAIM)
        register_link(self.db, {'source': claim, 'target': scheme, 'kind': 'depends-on-counterterm',
                                'status': 'declared', 'description': 'S_0 uses |delta_0|'})
        term = {'label': '|delta_0| O_0', 'role': 'counterterm_compensation', 'scheme': scheme,
                'absorbs': [], 'orientation': None}
        rules = [item['rule'] for item in check_term_roles(self.db, {'statement': claim, 'terms': [term]})['findings']]
        self.assertEqual(rules, ['T4-orientation-missing'])
        explicit = copy.deepcopy(term)
        explicit['orientation'] = {'symbol': 'o_R', 'absorbed': False}
        self.assertEqual(check_term_roles(self.db, {'statement': claim, 'terms': [explicit]})['result'], 'passed')

    def test_discrete_scan_readout_basis_and_known_tension(self):
        stored = register_scheme(self.db, self.root, self.scheme_request(discrete_payload(), 'CT-000-TEST-DISCRETE'))
        scheme = stored['version_hash']
        claim = self.statement('S_0', CLAIM)
        register_link(self.db, {'source': claim, 'target': scheme, 'kind': 'depends-on-counterterm',
                                'status': 'declared', 'description': 'S_0 uses the chosen unit'})
        entry = resolve_dependencies(self.db, claim)['counterterms'][0]
        self.assertEqual(entry['fitted_on']['scan'], {'trials': 12, 'hits': 1, 'chance_expectation': '1/4'})
        self.assertEqual(entry['known_tensions'][0]['delta'], '3 units')
        report = check_blindness(self.db, {'statement': claim, 'tested_against': [
            {'label': 'dummy-target-z', 'source': 'fixture-data', 'version': 'v1'}]})
        self.assertEqual(report['verdict'], 'not_blind')
        self.assertFalse(report['findings'][0]['same_version'])
        receipt = check_residual(self.db, {'scheme': scheme, 'replacement': self.structure('F_0', ['1/2'])})
        self.assertEqual((receipt['result'], receipt['known_tensions']), ('passed', discrete_payload()['known_tensions']))

    def test_unvalued_parameter_blocks_residual(self):
        payload = scheme_payload()
        payload['compensation_function']['parameters']['theta_0']['value'] = None
        scheme = register_scheme(self.db, self.root, self.scheme_request(payload, 'CT-000-OPEN'))['version_hash']
        receipt = check_residual(self.db, {'scheme': scheme, 'replacement': self.structure('F_0', ['0', '1/2'])})
        self.assertEqual((receipt['result'], receipt['residuals']), ('blocked', []))


if __name__ == '__main__':
    unittest.main()
