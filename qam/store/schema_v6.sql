CREATE TABLE qstore_editions (
 edition_hash TEXT PRIMARY KEY,
 edition_id TEXT NOT NULL,
 snapshot_hash TEXT NOT NULL REFERENCES qstore_snapshots(snapshot_hash),
 previous_hash TEXT UNIQUE REFERENCES qstore_editions(edition_hash),
 payload_json TEXT NOT NULL CHECK(json_valid(payload_json))
);
CREATE UNIQUE INDEX qstore_first_edition ON qstore_editions(edition_id) WHERE previous_hash IS NULL;
CREATE TABLE qstore_edition_sections (
 edition_hash TEXT NOT NULL REFERENCES qstore_editions(edition_hash),
 ordinal INTEGER NOT NULL,
 section_key TEXT NOT NULL,
 title TEXT NOT NULL,
 PRIMARY KEY (edition_hash, ordinal), UNIQUE (edition_hash, section_key)
);
CREATE TABLE qstore_edition_members (
 edition_hash TEXT NOT NULL,
 section_ordinal INTEGER NOT NULL,
 ordinal INTEGER NOT NULL,
 version_hash TEXT NOT NULL REFERENCES qstore_versions(version_hash),
 usage TEXT NOT NULL CHECK(usage IN ('prose','argument','candidate')),
 PRIMARY KEY (edition_hash, section_ordinal, ordinal),
 FOREIGN KEY (edition_hash,section_ordinal) REFERENCES qstore_edition_sections(edition_hash,ordinal)
);
CREATE TRIGGER editions_no_update BEFORE UPDATE ON qstore_editions BEGIN SELECT RAISE(ABORT,'Edition revisions are immutable'); END;
CREATE TRIGGER editions_no_delete BEFORE DELETE ON qstore_editions BEGIN SELECT RAISE(ABORT,'Edition revisions are immutable'); END;
CREATE TRIGGER edition_sections_no_update BEFORE UPDATE ON qstore_edition_sections BEGIN SELECT RAISE(ABORT,'Edition sections are immutable'); END;
CREATE TRIGGER edition_sections_no_delete BEFORE DELETE ON qstore_edition_sections BEGIN SELECT RAISE(ABORT,'Edition sections are immutable'); END;
CREATE TRIGGER edition_members_no_update BEFORE UPDATE ON qstore_edition_members BEGIN SELECT RAISE(ABORT,'Edition members are immutable'); END;
CREATE TRIGGER edition_members_no_delete BEFORE DELETE ON qstore_edition_members BEGIN SELECT RAISE(ABORT,'Edition members are immutable'); END;
INSERT INTO qstore_schema(version) VALUES (6);
