"""Stdio MCP entry point for querying a QAM snapshot."""

from qsc_mcp_server import (
    FastMCP, audit_qam_batch_report, compare_qam_batch_reports, find_qam_claims, get_qam_receipt,
    list_qam_batch_reports, list_qam_receipts,
    read_qam_batch_report,
)


def read_qam_receipt(receipt_hash: str, trace: bool = False, summary: bool = False) -> dict:
    """Verify a saved MMA receipt and optionally return its premise trace or summary."""
    return get_qam_receipt(receipt_hash, trace=trace, summary=summary)


if __name__ == "__main__":
    server = FastMCP("qsc-qam")
    server.add_tool(find_qam_claims)
    server.add_tool(list_qam_receipts)
    server.add_tool(read_qam_receipt)
    server.add_tool(read_qam_batch_report)
    server.add_tool(list_qam_batch_reports)
    server.add_tool(compare_qam_batch_reports)
    server.add_tool(audit_qam_batch_report)
    server.run()
