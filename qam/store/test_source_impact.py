import hashlib
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

from sqlalchemy import func, select

from qam.store.registry import register, register_guard, register_review
from qam.store.orm import store_session
from qam.store.snapshots import create_snapshot, read_snapshot
from qam.store.matrix_check import verify, read_receipt
from qam.store.source_impact import freshness_report, impact_report


class SourceImpactTests(unittest.TestCase):
    def test_drift_dependencies_evidence_and_historical_results(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            db = root / 'store.sqlite3'
            definition_file = root / 'definition.tex'
            definition_file.write_text('Square rational matrix', encoding='utf-8')
            seed_file = root / 'seed.json'
            seed_file.write_text('[[1,0],[0,0]]', encoding='utf-8')
            evidence_file = root / 'review.txt'
            evidence_file.write_text('Fixture review', encoding='utf-8')

            def provenance(path):
                return {'path': path.name, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                        'revision': 'fixture', 'locator': 'whole file'}

            definition = register(db, root, {'object_id': 'definition', 'kind': 'definition',
                'frame': 'comparison', 'status': 'conditional', 'source': provenance(definition_file),
                'payload': {'title': 'Matrix', 'body': 'Square rational matrix', 'scope': 'test', 'assumptions': []}})['version_hash']
            seed = register(db, root, {'object_id': 'seed', 'kind': 'seed',
                'frame': 'comparison', 'status': 'conditional', 'source': provenance(seed_file),
                'payload': {'title': 'P', 'value': [[1, 0], [0, 0]], 'value_type': 'rational-matrix',
                    'origin': 'fixture', 'definition_version': definition, 'assumptions': []}})['version_hash']
            receipt = verify(db, {'projector': seed})
            guard = register_guard(db, root, {'subject': seed, 'target': definition,
                'title': 'Interpretation', 'obligation': 'Identify native meaning',
                'source': provenance(definition_file)})['guard_hash']
            register_review(db, root, {'kind': 'guard', 'subject': guard, 'previous': None,
                'status': 'open', 'reviewer': 'fixture', 'reason': 'Still open',
                'evidence': provenance(evidence_file)})
            snapshot = create_snapshot(db, 'source-test')['snapshot_hash']
            saved = read_snapshot(db, snapshot)
            self.assertEqual(freshness_report(db, snapshot, root)['result'], 'matches')
            dependencies = impact_report(db, snapshot, [definition])
            self.assertIn(seed, dependencies['dependent_versions'])
            self.assertIn(receipt['receipt_hash'], dependencies['affected_receipts'])
            self.assertIn(guard, dependencies['affected_guards'])
            evidence_file.write_text('Changed fixture review', encoding='utf-8')
            changed = freshness_report(db, snapshot, root)
            self.assertEqual(changed['result'], 'review-needed')
            self.assertEqual(changed['impact']['roots'], [])
            self.assertTrue(changed['evidence_changes'])
            self.assertIn(seed, changed['evidence_impact']['affected_versions'])
            self.assertTrue(changed['containing_snapshots'])
            definition_file.write_text('Changed definition', encoding='utf-8')
            with store_session(db) as (session, models):
                before = session.scalar(select(func.count()).select_from(models.qstore_ledger))
            changed = freshness_report(db, snapshot, root)
            self.assertEqual(changed['impact']['roots'], [definition])
            self.assertIn(seed, changed['impact']['affected_versions'])
            self.assertEqual(read_snapshot(db, snapshot), saved)
            self.assertEqual(read_receipt(db, receipt['receipt_hash'])['result'], 'passed')
            with store_session(db) as (session, models):
                self.assertEqual(session.scalar(select(func.count()).select_from(models.qstore_ledger)), before)
            run = subprocess.run([sys.executable, '-m', 'qam.tools.store_db', 'freshness',
                '--db', str(db), '--hash', snapshot, '--repo', str(root)], capture_output=True, text=True)
            self.assertEqual(run.returncode, 1)
            self.assertEqual(json.loads(run.stdout)['result'], 'review-needed')
            seed_file.unlink()
            self.assertTrue(any(row['status'] == 'missing' for row in freshness_report(db, snapshot, root)['sources']))


if __name__ == '__main__':
    unittest.main()
