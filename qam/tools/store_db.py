"""Initialize the versioned QAM object-store namespace in the local SQLite database."""

import argparse
import json
from pathlib import Path
import sqlite3


def apply_sql(db, path):
    # Execute complete statements without executescript's implicit commit.
    statement = ''
    for line in path.read_text(encoding='utf-8').splitlines(keepends=True):
        statement += line
        if sqlite3.complete_statement(statement):
            db.execute(statement)
            statement = ''
    if statement.strip():
        raise ValueError(f'Incomplete migration in {path.name}')


def initialize(path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    resources = Path(__file__).resolve().parents[1] / 'store'
    catalogue = json.loads((resources / 'catalogue_v1.json').read_text(encoding='utf-8'))
    db = sqlite3.connect(path, timeout=30)
    try:
        db.execute('PRAGMA foreign_keys=ON')
        # Take the write lock before inspecting the version, including first use.
        db.execute('BEGIN IMMEDIATE')
        exists = db.execute("SELECT 1 FROM sqlite_master WHERE name='qstore_schema'").fetchone()
        versions = db.execute('SELECT version FROM qstore_schema ORDER BY version').fetchall() if exists else []
        if len(versions) > 6 or versions != [(n,) for n in range(1, len(versions) + 1)]:
            raise ValueError(f'Unsupported store schema versions: {versions}')
        if not versions:
            apply_sql(db, resources / 'schema_v1.sql')
            db.executemany('INSERT INTO qstore_object_types VALUES (?,?)', catalogue.items())
            db.execute('INSERT INTO qstore_ledger(event_type,payload_json) VALUES (?,?)',
                       ('schema-initialized', json.dumps({'schema': 1, 'catalogue': 'catalogue_v1.json'})))
        stored = dict(db.execute('SELECT name,description FROM qstore_object_types'))
        if stored != catalogue:
            raise ValueError('Stored type catalogue differs from catalogue_v1.json')
        for version in range(2, 7):
            if (version,) not in versions:
                apply_sql(db, resources / f'schema_v{version}.sql')
                db.execute('INSERT INTO qstore_ledger(event_type,payload_json) VALUES (?,?)',
                           ('schema-migrated', json.dumps({'schema': version})))
        db.commit()
        return {'schema': 6, 'object_types': len(stored),
                'objects': db.execute('SELECT count(*) FROM qstore_objects').fetchone()[0]}
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', nargs='?', choices=['initialize', 'status', 'store', 'link', 'guard', 'guards', 'review', 'verify', 'receipt', 'snapshot', 'snapshot-read', 'snapshot-check', 'select', 'export', 'scrub', 'view', 'freshness', 'impact', 'paper-save', 'paper-read', 'paper-export', 'edition-save', 'edition-read', 'edition-export', 'backup', 'backup-check', 'restore', 'import-inventory', 'inventory-view'], default='initialize')
    parser.add_argument('--db', type=Path, default=Path('build/qam.sqlite3'))
    parser.add_argument('--request', type=Path)
    parser.add_argument('--hash')
    parser.add_argument('--label')
    parser.add_argument('--out', type=Path)
    parser.add_argument('--archive', type=Path)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    if args.command in {'edition-save', 'edition-read', 'edition-export'}:
        from qam.store.editions import save_edition, read_edition, export_edition

        if args.command == 'edition-save':
            if args.request is None:
                parser.error('--request is required for edition-save')
            result = save_edition(args.db, args.repo, json.loads(args.request.read_text(encoding='utf-8-sig')))
        else:
            if not args.hash:
                parser.error('--hash is required for edition-read and edition-export')
            if args.command == 'edition-export':
                if args.out is None:
                    parser.error('--out is required for edition-export')
                result = export_edition(args.db, args.repo, args.hash, args.out)
            else:
                result = read_edition(args.db, args.hash)
                if args.out:
                    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
                    result = {'edition_hash': result['edition_hash'], 'edition_id': result['edition_id'], 'sections': len(result['sections'])}
        print(json.dumps(result, ensure_ascii=False))
        return
    if args.command == 'inventory-view':
        from qam.store.manuscript_import import overview_from_snapshot

        if not args.hash or args.request is None:
            parser.error('--hash and --request are required for inventory-view')
        request = json.loads(args.request.read_text(encoding='utf-8-sig'))
        if not isinstance(request, dict) or set(request) != {'root'}:
            parser.error('Inventory view request requires root only')
        text = overview_from_snapshot(args.db, args.hash, request['root'])
        if args.out is None:
            print(text)
        else:
            with args.out.open('x', encoding='utf-8') as stream:
                stream.write(text)
            print(json.dumps({'file': str(args.out)}))
    elif args.command == 'import-inventory':
        from qam.store.manuscript_import import import_manuscript, overview
        from qam.store.snapshots import create_snapshot

        if args.out is None:
            parser.error('--out is required for import-inventory reports')
        args.out.mkdir(parents=True, exist_ok=False)
        result = import_manuscript(args.db, args.repo)
        result['snapshot'] = create_snapshot(args.db, 'manuscript-inventory-' + result['generation'][:16])
        (args.out / 'overview.md').write_text(overview(result), encoding='utf-8')
        (args.out / 'import.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
        print(json.dumps(result, ensure_ascii=False))
    elif args.command in {'backup', 'backup-check', 'restore'}:
        from qam.store.backup import create_backup, check_backup, restore_backup

        if args.command == 'backup':
            if args.out is None:
                parser.error('--out is required for backup')
            result = create_backup(args.db, args.out)
        else:
            if args.archive is None:
                parser.error('--archive is required for backup-check and restore')
            if args.command == 'restore':
                if args.out is None:
                    parser.error('--out is required for restore')
                result = restore_backup(args.archive, args.out)
            else:
                manifest = check_backup(args.archive)
                result = {'result': 'passed', 'sha256': manifest['sha256'], 'table_rows': manifest['table_rows']}
        print(json.dumps(result, ensure_ascii=False))
    elif args.command in {'paper-save', 'paper-read', 'paper-export'}:
        from qam.store.papers import save_paper, read_paper, export_paper

        if args.command == 'paper-save':
            if args.request is None:
                parser.error('--request is required for paper-save')
            result = save_paper(args.db, json.loads(args.request.read_text(encoding='utf-8-sig')))
        else:
            if not args.hash:
                parser.error('--hash is required for paper-read and paper-export')
            if args.command == 'paper-export':
                if args.out is None:
                    parser.error('--out is required for paper-export')
                result = export_paper(args.db, args.hash, args.out)
            else:
                result = read_paper(args.db, args.hash)
        print(json.dumps(result, ensure_ascii=False))
    elif args.command in {'freshness', 'impact'}:
        from qam.store.source_impact import freshness_report, impact_report

        if not args.hash:
            parser.error('--hash is required for freshness and impact')
        if args.command == 'freshness':
            result = freshness_report(args.db, args.hash, args.repo)
        else:
            if not args.request:
                parser.error('--request is required for impact')
            request = json.loads(args.request.read_text(encoding='utf-8-sig'))
            if not isinstance(request, dict) or set(request) != {'roots'}:
                parser.error('Impact request requires roots only')
            result = impact_report(args.db, args.hash, request['roots'])
        print(json.dumps(result, ensure_ascii=False))
        if result.get('result') == 'review-needed':
            raise SystemExit(1)
    elif args.command in {'select', 'export', 'scrub', 'view'}:
        from qam.store.selection import select_versions

        if not args.hash or not args.request:
            parser.error('--hash and --request are required for select')
        request = json.loads(args.request.read_text(encoding='utf-8-sig'))
        if not isinstance(request, dict) or set(request) != {'roots'}:
            parser.error('Selection request requires roots only')
        if args.command == 'view':
            from qam.store.argument_view import markdown

            document = markdown(select_versions(args.db, args.hash, request['roots']))
            if args.out is None:
                print(document)
            else:
                with args.out.open('x', encoding='utf-8') as stream:
                    stream.write(document)
                print(json.dumps({'file': str(args.out)}))
            return
        elif args.command == 'export':
            from qam.store.latex_export import export

            if args.out is None:
                parser.error('--out is required for export')
            result = export(args.db, args.hash, request['roots'], args.out)
        elif args.command == 'scrub':
            from qam.store.scrub import scrub

            result = scrub(select_versions(args.db, args.hash, request['roots']))
        else:
            result = select_versions(args.db, args.hash, request['roots'])
        print(json.dumps(result, ensure_ascii=False))
        if args.command == 'scrub' and result['result'] != 'passed':
            raise SystemExit(1)
    elif args.command in {'snapshot', 'snapshot-read', 'snapshot-check'}:
        from qam.store.snapshots import create_snapshot, read_snapshot

        if args.command == 'snapshot':
            if not args.label:
                parser.error('--label is required for snapshot')
            result = create_snapshot(args.db, args.label)
        else:
            if not args.hash:
                parser.error('--hash is required for snapshot-read')
            result = read_snapshot(args.db, args.hash)
            if args.command == 'snapshot-check':
                from qam.store.integrity import inspect_snapshot

                result = inspect_snapshot(result)
        print(json.dumps(result, ensure_ascii=False))
    elif args.command == 'verify':
        from qam.store.matrix_check import verify

        if args.request is None:
            parser.error('--request is required for verify')
        result = verify(args.db, json.loads(args.request.read_text(encoding='utf-8-sig')))
        print(json.dumps(result, ensure_ascii=False))
        if result['result'] != 'passed':
            raise SystemExit(1)
    elif args.command == 'receipt':
        from qam.store.matrix_check import read_receipt

        if not args.hash:
            parser.error('--hash is required for receipt')
        print(json.dumps(read_receipt(args.db, args.hash), ensure_ascii=False))
    elif args.command in {'store', 'link', 'guard', 'review'}:
        from qam.store.registry import register, register_link, register_guard, register_review

        if args.request is None:
            parser.error('--request is required for store, link, guard and review')
        request = json.loads(args.request.read_text(encoding='utf-8-sig'))
        if args.command == 'store':
            result = register(args.db, args.repo, request)
        elif args.command == 'guard':
            result = register_guard(args.db, args.repo, request)
        elif args.command == 'review':
            result = register_review(args.db, args.repo, request)
        else:
            result = register_link(args.db, request)
        print(json.dumps(result))
    elif args.command == 'guards':
        from sqlalchemy import select
        from qam.store.orm import store_session
        from qam.store.registry import latest_review

        with store_session(args.db) as (session, models):
            rows = session.scalars(select(models.qstore_guards).order_by(models.qstore_guards.guard_hash))
            result = []
            for row in rows:
                review = latest_review(session, models, 'guard', row.guard_hash)
                status = review.status if review else row.status
                if status == 'open':
                    result.append({'guard_hash': row.guard_hash, 'subject': row.subject_version,
                                   'target': row.target_version, 'status': status,
                                   'review_hash': review.review_hash if review else None,
                                   **json.loads(row.payload_json)})
        print(json.dumps(result, ensure_ascii=False))
    elif args.command == 'status':
        from sqlalchemy import func, select
        from qam.store.orm import store_session

        with store_session(args.db) as (session, models):
            result = {
                'schema': session.scalar(select(func.max(models.qstore_schema.version))),
                'object_types': session.scalar(select(func.count()).select_from(models.qstore_object_types)),
                'objects': session.scalar(select(func.count()).select_from(models.qstore_objects)),
                'access': 'sqlalchemy',
            }
        print(json.dumps(result))
    else:
        print(json.dumps(initialize(args.db)))


if __name__ == '__main__':
    main()
