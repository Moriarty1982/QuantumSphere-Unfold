"""Shared source-pinned, explicitly declared review bookkeeping."""

import json
from sqlalchemy import select

from qam.store.orm import store_session
from qam.store.registry import latest_review, register_review, register_link


class SourceReview:
    def __init__(self, database, repo, source, source_hash, evidence):
        self.database = database
        self.repo = repo
        self.source = source
        self.source_hash = source_hash
        self.evidence = evidence

    def find(self, object_id):
        with store_session(self.database) as (session, models):
            rows = list(session.scalars(select(models.qstore_versions).where(models.qstore_versions.object_id == object_id)))
            valid = []
            for row in rows:
                sources = list(session.scalars(select(models.qstore_sources).where(models.qstore_sources.version_hash == row.version_hash)))
                if any(item.source_path == self.source and item.source_hash == self.source_hash for item in sources):
                    valid.append((row.version_hash, json.loads(row.payload_json)))
            if len(valid) != 1:
                raise ValueError(f'Expected one source-pinned version of {object_id}')
            return valid[0]

    def assess(self, kind, subject, status, reason):
        with store_session(self.database) as (session, models):
            previous = latest_review(session, models, kind, subject)
            if previous:
                payload = json.loads(previous.payload_json)
                if previous.status == status and payload['reason'] == reason and payload['evidence'] == self.evidence:
                    return previous.review_hash
            previous_hash = previous.review_hash if previous else None
        return register_review(self.database, self.repo, {'kind': kind, 'subject': subject,
            'previous': previous_hash, 'status': status, 'reviewer': 'Codex self-review 2026-11-11',
            'reason': reason, 'evidence': self.evidence})['review_hash']

    def reviewed_link(self, source, target, kind, reason):
        key = register_link(self.database, {'source': source, 'target': target, 'kind': kind,
                             'status': 'declared', 'description': reason})['relation_hash']
        self.assess('relation', key, 'reviewed', reason)
        return key
