"""Stdio MCP entry point for executing MML pair batches."""

from qsc_mcp_server import FastMCP, replay_qam_batch_report, run_qam_mml_batch, run_qam_pair_batch


if __name__ == "__main__":
    server = FastMCP("qsc-qam-batch")
    server.add_tool(run_qam_mml_batch)
    server.add_tool(run_qam_pair_batch)
    server.add_tool(replay_qam_batch_report)
    server.run()
