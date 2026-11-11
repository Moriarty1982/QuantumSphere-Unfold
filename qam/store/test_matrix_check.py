import copy
import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
import subprocess
import sys

from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError

from qam.store.registry import register, register_guard
from qam.store.orm import store_session
from qam.store.matrix_check import verify, read_receipt


class MatrixCheckTests(unittest.TestCase):
    def test_exact_checks_provenance_failures_and_guards(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / 'fixture.tex'
            source.write_text('Rational matrices in a declared comparison frame', encoding='utf-8')
            db = root / 'store.sqlite3'
            definition_request = {
                'object_id': 'matrix-definition', 'kind': 'definition', 'frame': 'comparison', 'status': 'conditional',
                'payload': {'title': 'Matrix', 'body': 'Square rational matrix', 'scope': 'test',
                            'assumptions': ['Native interpretation is not supplied']},
                'source': {'path': source.name, 'sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                           'revision': 'test', 'locator': 'line 1'}}
            definition = register(db, root, definition_request)['version_hash']

            def seed(name, value, frame='comparison'):
                request = copy.deepcopy(definition_request)
                request.update(object_id=name, kind='seed', frame=frame)
                request['payload'] = {'title': name, 'value': value, 'value_type': 'rational-matrix',
                                      'origin': 'test fixture', 'assumptions': [], 'definition_version': definition}
                return register(db, root, request)['version_hash']

            projector = seed('P', [['1/2', '1/2'], ['1/2', '1/2']])
            identity = seed('I', [[1, 0], [0, 1]])
            guard = register_guard(db, root, {'subject': projector, 'target': definition,
                'title': 'Open interpretation', 'obligation': 'Identify the native projector',
                'source': definition_request['source']})['guard_hash']
            passed = verify(db, {'projector': projector, 'transport': identity})
            self.assertEqual(passed['result'], 'passed')
            self.assertTrue(passed['guards'])
            self.assertTrue(any(item.get('guard_hash') == guard for item in passed['guards']))
            self.assertEqual(passed, read_receipt(db, passed['receipt_hash']))
            self.assertEqual(verify(db, passed['request'])['receipt_hash'], passed['receipt_hash'])
            request_file = root / 'check.json'
            request_file.write_text(json.dumps(passed['request']), encoding='utf-8')
            command = [sys.executable, '-m', 'qam.tools.store_db', 'verify',
                       '--db', str(db), '--request', str(request_file)]
            run = subprocess.run(command, capture_output=True, text=True, check=True)
            self.assertEqual(json.loads(run.stdout)['result'], 'passed')
            transport = seed('M', [[1, 0], [0, 2]])
            failed = verify(db, {'projector': projector, 'transport': transport})
            self.assertEqual(failed['result'], 'failed')
            request_file.write_text(json.dumps(failed['request']), encoding='utf-8')
            run = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(run.returncode, 1)
            self.assertEqual(json.loads(run.stdout)['result'], 'failed')
            self.assertEqual(failed['residuals']['commutator_residual'], [['0', '-1/2'], ['1/2', '0']])
            bad = seed('float', [[0.5]])
            self.assertEqual(verify(db, {'projector': bad})['result'], 'blocked')
            ragged = seed('ragged', [[1, 0], [0]])
            self.assertEqual(verify(db, {'projector': ragged})['result'], 'blocked')
            self.assertEqual(verify(db, {'projector': 'missing'})['result'], 'blocked')
            scalar = seed('scalar', [[1]])
            self.assertEqual(verify(db, {'projector': projector, 'transport': scalar})['result'], 'blocked')
            changed = seed('P', [[2, 0], [0, 0]])
            self.assertEqual(verify(db, {'projector': changed})['result'], 'failed')
            self.assertEqual(read_receipt(db, passed['receipt_hash'])['inputs'][projector]['payload']['value'],
                             [['1/2', '1/2'], ['1/2', '1/2']])
            with store_session(db) as (session, models):
                self.assertEqual(session.scalar(select(func.count()).select_from(models.qstore_check_inputs).where(
                    models.qstore_check_inputs.receipt_hash == passed['receipt_hash'])), 3)
            with self.assertRaises(IntegrityError):
                with store_session(db) as (session, models):
                    session.get(models.qstore_checks, passed['receipt_hash']).result = 'failed'


if __name__ == '__main__':
    unittest.main()
