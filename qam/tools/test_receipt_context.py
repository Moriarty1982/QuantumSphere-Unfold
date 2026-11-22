"""Check receipt context selection against SQLite, with optional Icarus parity."""

from contextlib import closing
from itertools import product
import json
from pathlib import Path
import shutil
from tempfile import TemporaryDirectory
import unittest

from qam.tools import readout_db, receipt_context


class ReceiptContextTests(unittest.TestCase):
    def setUp(self):
        tmp = TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.db = readout_db.connect(Path(tmp.name) / "qam.sqlite3")
        self.addCleanup(self.db.close)
        self.context = "a" * 128
        self.other = "b" * 128
        records = [
            (self.context, "M", "guard"),
            (self.context, "T", "continue"),
            (self.other, "M", "continue"),
            (self.context, None, "guard"),
            (self.context, 5, "guard"),
            (self.context, "M", "guard"),
        ]
        for number, (context, frame, status) in enumerate(records):
            request = {"arguments": {"frame": frame}}
            self.db.execute("INSERT INTO mma_receipts VALUES (?, ?, ?, ?, ?, ?)",
                            (str(number), context, "READOUT", status, json.dumps(request), "{}"))

    def test_exact_scope_and_order(self):
        result = receipt_context.select(self.db, context_hash=self.context.upper(), frame="M",
                                        status="guard", limit=2)
        self.assertEqual([row["receipt_hash"] for row in result["receipts"]], ["5", "0"])
        self.assertEqual(result["backend"], "sqlite")
        self.assertEqual(receipt_context.select(self.db, frame="5")["receipts"], [])
        self.assertEqual(receipt_context.select(self.db, frame="m")["receipts"], [])
        self.assertIsNone(receipt_context.select(self.db, limit=2)["receipts"][1]["frame"])

    def test_reject_bad_query(self):
        for field in ({"context_hash": "local"}, {"frame": ""}, {"limit": 51}, {"status": "open"}):
            with self.subTest(field=field), self.assertRaises(ValueError):
                receipt_context.select(self.db, **field)

    @unittest.skipUnless(shutil.which("iverilog") and shutil.which("vvp"), "requires Icarus Verilog")
    def test_hdl_and_sqlite_match_for_all_filter_masks(self):
        for scope, frame, status in product((None, self.context), (None, "M"), (None, "guard")):
            filters = {"context_hash": scope, "frame": frame, "status": status, "limit": 3}
            with self.subTest(filters=filters):
                hdl = receipt_context.select(self.db, backend="hdl", **filters)
                sqlite = receipt_context.select(self.db, **filters)
                self.assertEqual(hdl["scanned"], 6)
                self.assertEqual(hdl["receipts"], sqlite["receipts"])
        missing = receipt_context.select(self.db, backend="hdl", frame="missing")
        self.assertEqual(missing["receipts"], [])
        with closing(readout_db.connect(":memory:")) as empty:
            result = receipt_context.select(empty, backend="hdl")
            self.assertEqual((result["receipts"], result["scanned"]), ([], 0))


if __name__ == "__main__":
    unittest.main()
