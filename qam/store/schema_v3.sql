CREATE TABLE qstore_checks (
    receipt_hash TEXT PRIMARY KEY,
    checker TEXT NOT NULL,
    checker_hash TEXT NOT NULL,
    result TEXT NOT NULL CHECK(result IN ('passed','failed','blocked')),
    receipt_json TEXT NOT NULL CHECK(json_valid(receipt_json))
);
CREATE TABLE qstore_check_inputs (
    receipt_hash TEXT NOT NULL REFERENCES qstore_checks(receipt_hash),
    version_hash TEXT NOT NULL REFERENCES qstore_versions(version_hash),
    PRIMARY KEY(receipt_hash,version_hash)
);
CREATE TRIGGER qstore_checks_no_update BEFORE UPDATE ON qstore_checks BEGIN
    SELECT RAISE(ABORT, 'Check receipts are immutable');
END;
CREATE TRIGGER qstore_checks_no_delete BEFORE DELETE ON qstore_checks BEGIN
    SELECT RAISE(ABORT, 'Check receipts are immutable');
END;
CREATE TRIGGER qstore_check_inputs_no_update BEFORE UPDATE ON qstore_check_inputs BEGIN
    SELECT RAISE(ABORT, 'Check inputs are immutable');
END;
CREATE TRIGGER qstore_check_inputs_no_delete BEFORE DELETE ON qstore_check_inputs BEGIN
    SELECT RAISE(ABORT, 'Check inputs are immutable');
END;
INSERT INTO qstore_schema(version) VALUES (3);
