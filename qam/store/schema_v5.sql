CREATE TABLE qstore_papers (
    paper_hash TEXT PRIMARY KEY,
    paper_id TEXT NOT NULL,
    snapshot_hash TEXT NOT NULL REFERENCES qstore_snapshots(snapshot_hash),
    previous_hash TEXT UNIQUE REFERENCES qstore_papers(paper_hash),
    payload_json TEXT NOT NULL CHECK(json_valid(payload_json))
);
CREATE UNIQUE INDEX qstore_first_paper ON qstore_papers(paper_id) WHERE previous_hash IS NULL;
CREATE TRIGGER qstore_papers_no_update BEFORE UPDATE ON qstore_papers BEGIN
    SELECT RAISE(ABORT, 'Paper versions are immutable');
END;
CREATE TRIGGER qstore_papers_no_delete BEFORE DELETE ON qstore_papers BEGIN
    SELECT RAISE(ABORT, 'Paper versions are immutable');
END;
INSERT INTO qstore_schema(version) VALUES (5);
