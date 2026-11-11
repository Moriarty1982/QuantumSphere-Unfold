CREATE TABLE qstore_reviews (
    review_hash TEXT PRIMARY KEY,
    guard_hash TEXT REFERENCES qstore_guards(guard_hash),
    relation_hash TEXT REFERENCES qstore_relations(relation_hash),
    previous_hash TEXT UNIQUE REFERENCES qstore_reviews(review_hash),
    status TEXT NOT NULL,
    payload_json TEXT NOT NULL CHECK(json_valid(payload_json)),
    CHECK ((guard_hash IS NOT NULL AND relation_hash IS NULL AND status IN ('open','satisfied','failed'))
        OR (relation_hash IS NOT NULL AND guard_hash IS NULL AND status IN ('proposed','declared','reviewed','rejected')))
);
CREATE UNIQUE INDEX qstore_first_guard_review ON qstore_reviews(guard_hash) WHERE previous_hash IS NULL;
CREATE UNIQUE INDEX qstore_first_relation_review ON qstore_reviews(relation_hash) WHERE previous_hash IS NULL;
CREATE TRIGGER qstore_reviews_no_update BEFORE UPDATE ON qstore_reviews BEGIN
    SELECT RAISE(ABORT, 'Reviews are immutable');
END;
CREATE TRIGGER qstore_reviews_no_delete BEFORE DELETE ON qstore_reviews BEGIN
    SELECT RAISE(ABORT, 'Reviews are immutable');
END;
CREATE TRIGGER qstore_guards_no_update BEFORE UPDATE ON qstore_guards BEGIN
    SELECT RAISE(ABORT, 'Use a guard review');
END;
CREATE TRIGGER qstore_guards_no_delete BEFORE DELETE ON qstore_guards BEGIN
    SELECT RAISE(ABORT, 'Guards are immutable');
END;
CREATE TRIGGER qstore_relations_no_update BEFORE UPDATE ON qstore_relations BEGIN
    SELECT RAISE(ABORT, 'Use a relation review');
END;
CREATE TRIGGER qstore_relations_no_delete BEFORE DELETE ON qstore_relations BEGIN
    SELECT RAISE(ABORT, 'Relations are immutable');
END;
INSERT INTO qstore_schema(version) VALUES (2);
