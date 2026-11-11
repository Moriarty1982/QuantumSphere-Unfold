"""SQLAlchemy mappings over the versioned, migration-owned QAM store schema."""

from contextlib import contextmanager
from pathlib import Path
from types import SimpleNamespace

from sqlalchemy import MetaData, URL, create_engine, event
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

from qam.tools.store_db import initialize


def open_engine(path):
    """Open SQLite with FK checks and explicit transaction control on every connection."""
    engine = create_engine(
        URL.create('sqlite+pysqlite', database=str(Path(path).resolve())),
        connect_args={'timeout': 30},
    )

    @event.listens_for(engine, 'connect')
    def configure_connection(connection, record):
        connection.isolation_level = None
        cursor = connection.cursor()
        try:
            cursor.execute('PRAGMA foreign_keys=ON')
        finally:
            cursor.close()

    @event.listens_for(engine, 'begin')
    def begin_transaction(connection):
        connection.exec_driver_sql('BEGIN IMMEDIATE')

    return engine


@contextmanager
def store_session(path=Path('build/qam.sqlite3')):
    """Yield a transactional (Session, mapped classes) pair; commit only on success.

    Reflection keeps SQL migrations authoritative, including their checks and
    triggers. Typed link registration is a separate domain operation. Automatic
    relationship naming is disabled because links have two version endpoints.
    """
    initialize(path)
    engine = open_engine(path)
    try:
        metadata = MetaData()
        metadata.reflect(engine, only=lambda name, metadata: name.startswith('qstore_'))
        models = automap_base(metadata=metadata)
        models.prepare(generate_relationship=lambda *args, **kwargs: None)
        classes = dict(models.classes.items())
        # Automap omits pure association tables; expose their rows explicitly too.
        for name, table in metadata.tables.items():
            if name not in classes:
                model = type(name, (), {})
                models.registry.map_imperatively(model, table)
                classes[name] = model
        with Session(engine) as session, session.begin():
            yield session, SimpleNamespace(**classes)
    finally:
        engine.dispose()
