CREATE TABLE IF NOT EXISTS qstore_schema (
    version INTEGER PRIMARY KEY,
    applied_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS qstore_object_types (
    name TEXT PRIMARY KEY,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS qstore_objects (
    object_id TEXT PRIMARY KEY,
    object_type TEXT NOT NULL REFERENCES qstore_object_types(name)
);

CREATE TABLE IF NOT EXISTS qstore_versions (
    version_hash TEXT PRIMARY KEY,
    object_id TEXT NOT NULL REFERENCES qstore_objects(object_id),
    payload_json TEXT NOT NULL CHECK(json_valid(payload_json)),
    status TEXT NOT NULL CHECK(status IN
        ('imported-unreviewed','declared','conditional','reviewed','withdrawn')),
    frame TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS qstore_sources (
    source_id INTEGER PRIMARY KEY,
    version_hash TEXT NOT NULL REFERENCES qstore_versions(version_hash),
    source_path TEXT NOT NULL,
    source_hash TEXT NOT NULL,
    source_revision TEXT NOT NULL,
    locator TEXT NOT NULL,
    UNIQUE(version_hash, source_path, source_hash, source_revision, locator)
);

CREATE TABLE IF NOT EXISTS qstore_relations (
    relation_hash TEXT PRIMARY KEY,
    source_version TEXT NOT NULL REFERENCES qstore_versions(version_hash),
    target_version TEXT NOT NULL REFERENCES qstore_versions(version_hash),
    relation_type TEXT NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('proposed','declared','reviewed','rejected')),
    payload_json TEXT NOT NULL CHECK(json_valid(payload_json))
);

CREATE TABLE IF NOT EXISTS qstore_guards (
    guard_hash TEXT PRIMARY KEY,
    subject_version TEXT NOT NULL REFERENCES qstore_versions(version_hash),
    target_version TEXT REFERENCES qstore_versions(version_hash),
    status TEXT NOT NULL CHECK(status IN ('open','satisfied','failed')),
    payload_json TEXT NOT NULL CHECK(json_valid(payload_json))
);

CREATE TABLE IF NOT EXISTS qstore_ledger (
    event_id INTEGER PRIMARY KEY,
    event_type TEXT NOT NULL,
    payload_json TEXT NOT NULL CHECK(json_valid(payload_json)),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER IF NOT EXISTS qstore_versions_no_update
BEFORE UPDATE ON qstore_versions BEGIN
    SELECT RAISE(ABORT, 'Object versions are immutable');
END;
CREATE TRIGGER IF NOT EXISTS qstore_versions_no_delete
BEFORE DELETE ON qstore_versions BEGIN
    SELECT RAISE(ABORT, 'Object versions are immutable');
END;
CREATE TRIGGER IF NOT EXISTS qstore_ledger_no_update
BEFORE UPDATE ON qstore_ledger BEGIN
    SELECT RAISE(ABORT, 'Ledger is append-only');
END;
CREATE TRIGGER IF NOT EXISTS qstore_ledger_no_delete
BEFORE DELETE ON qstore_ledger BEGIN
    SELECT RAISE(ABORT, 'Ledger is append-only');
END;

INSERT INTO qstore_schema(version) VALUES (1);
