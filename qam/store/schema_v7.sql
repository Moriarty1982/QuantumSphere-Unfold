INSERT INTO qstore_object_types(name, description) VALUES ('counterterm-scheme', 'Local, effective compensation term delta_i with operator basis, bounded parameters, validity domain and open guards; never a derivation.');
INSERT INTO qstore_object_types(name, description) VALUES ('counterterm-transition', 'Append-only lifecycle step of one counterterm-scheme version (placeholder, partially_constrained, structurally_matched, deprecated).');
CREATE TRIGGER qstore_object_types_no_update BEFORE UPDATE ON qstore_object_types BEGIN
    SELECT RAISE(ABORT, 'Object type catalogue is migration-owned');
END;
CREATE TRIGGER qstore_object_types_no_delete BEFORE DELETE ON qstore_object_types BEGIN
    SELECT RAISE(ABORT, 'Object type catalogue is migration-owned');
END;
INSERT INTO qstore_schema(version) VALUES (7);
