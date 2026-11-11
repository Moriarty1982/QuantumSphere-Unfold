CREATE TABLE qstore_snapshots (
    snapshot_hash TEXT PRIMARY KEY,
    label TEXT NOT NULL,
    payload_json TEXT NOT NULL CHECK(json_valid(payload_json))
);
CREATE TRIGGER qstore_snapshots_no_update BEFORE UPDATE ON qstore_snapshots BEGIN
    SELECT RAISE(ABORT, 'Snapshots are immutable');
END;
CREATE TRIGGER qstore_snapshots_no_delete BEFORE DELETE ON qstore_snapshots BEGIN
    SELECT RAISE(ABORT, 'Snapshots are immutable');
END;
INSERT INTO qstore_schema(version) VALUES (4);
