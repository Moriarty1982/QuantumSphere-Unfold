"""Consistent full-SQLite backups and verified restoration to a new file."""

from contextlib import closing
import hashlib
import json
import os
from pathlib import Path
import shutil
import sqlite3
import tempfile
import time

from qam.store.registry import canonical, digest


def readonly(path):
    return sqlite3.connect(Path(path).resolve().as_uri() + '?mode=ro', uri=True, timeout=30)


def file_hash(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def database_inventory(path):
    with closing(readonly(path)) as db:
        if db.execute('PRAGMA integrity_check').fetchall() != [('ok',)]:
            raise ValueError('SQLite integrity check failed')
        if db.execute('PRAGMA foreign_key_check').fetchone() is not None:
            raise ValueError('SQLite foreign-key check failed')
        names = [row[0] for row in db.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")]
        counts = {}
        for name in names:
            identifier = '"' + name.replace('"', '""') + '"'
            counts[name] = db.execute('SELECT count(*) FROM ' + identifier).fetchone()[0]
        return counts


def create_backup(database, destination):
    source = Path(database).resolve()
    if not source.is_file():
        raise ValueError('Source database does not exist')
    destination = Path(destination).resolve()
    destination.mkdir(parents=True, exist_ok=False)
    output = destination / 'qam.sqlite3'
    deadline = time.monotonic() + 30

    def progress(status, remaining, total):
        if time.monotonic() > deadline:
            raise TimeoutError('SQLite backup exceeded 30 seconds; incomplete output has no manifest')

    with closing(readonly(source)) as src, closing(sqlite3.connect(output)) as dst:
        src.backup(dst, pages=256, progress=progress, sleep=0.1)
    counts = database_inventory(output)
    manifest = {'format': 'qstore-database-backup-v1', 'database': 'qam.sqlite3',
                'sha256': file_hash(output), 'bytes': output.stat().st_size,
                'table_rows': counts, 'sqlite_version': sqlite3.sqlite_version,
                'backup_code_sha256': file_hash(Path(__file__)),
                'scope': 'Complete SQLite database, including QAM evidence, store snapshots and paper versions; '
                         'external source files and generated PDFs remain separate artifacts'}
    (destination / 'manifest.json').write_text(canonical(manifest) + '\n', encoding='utf-8')
    return {'directory': str(destination), 'manifest_hash': digest(manifest),
            'database_sha256': manifest['sha256'], 'tables': len(counts)}


def check_backup(directory):
    directory = Path(directory).resolve()
    manifest = json.loads((directory / 'manifest.json').read_text(encoding='utf-8'))
    if manifest.get('format') != 'qstore-database-backup-v1' or manifest.get('database') != 'qam.sqlite3':
        raise ValueError('Unsupported database backup format')
    database = directory / 'qam.sqlite3'
    if database.is_symlink():
        raise ValueError('Backup database must be a regular local file')
    if file_hash(database) != manifest['sha256'] or database.stat().st_size != manifest['bytes']:
        raise ValueError('Backup database hash or size mismatch')
    if database_inventory(database) != manifest['table_rows']:
        raise ValueError('Backup database inventory mismatch')
    return manifest


def restore_backup(directory, destination):
    manifest = check_backup(directory)
    source = Path(directory).resolve() / 'qam.sqlite3'
    destination = Path(destination).absolute()
    if destination.exists() or destination.is_symlink():
        raise FileExistsError('Restore requires a new database path')
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(prefix='qam-restore-', suffix='.sqlite3',
                                     dir=destination.parent, delete=False) as stream:
        temporary = Path(stream.name)
    try:
        with source.open('rb') as src, temporary.open('wb') as dst:
            shutil.copyfileobj(src, dst)
        if file_hash(temporary) != manifest['sha256']:
            raise ValueError('Restored bytes do not match verified backup')
        if database_inventory(temporary) != manifest['table_rows']:
            raise ValueError('Restored database inventory mismatch')
        # Windows rename refuses replacement; POSIX link has the same guarantee.
        if os.name == 'nt':
            os.rename(temporary, destination)
        else:
            os.link(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)
    return {'database': str(destination), 'database_sha256': manifest['sha256'],
            'manifest_hash': digest(manifest), 'result': 'restored'}
