"""Check HDL tool discovery and execution through the real MCP stdio transport."""

import argparse
import asyncio
from pathlib import Path
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def check(synthesis):
    server = Path(__file__).with_name("qam_batch_server.py").resolve()
    parameters = StdioServerParameters(
        command=sys.executable, args=["-B", str(server)], cwd=server.parents[1],
    )
    async with stdio_client(parameters) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            tools = await session.list_tools()
            if "run_qam_hdl_check" not in {tool.name for tool in tools.tools}:
                raise AssertionError("The batch server did not publish run_qam_hdl_check")
            response = await session.call_tool("run_qam_hdl_check", {"synthesis": synthesis})
            data = getattr(response, "structured_content", getattr(response, "structuredContent", None))
            is_error = getattr(response, "is_error", getattr(response, "isError", False))
            if is_error or not data or not data.get("ok"):
                raise AssertionError(f"HDL MCP call failed: {response}")
            result = data["result"]
            increment = result["examples"][0]
            if (result["case_count"], increment["direct_cycles"], increment["cyclic_cycles"],
                    increment["final"]["tape"], increment["stop"]) != (209, 4, 24, [0, 0, 0, 1], "halted"):
                raise AssertionError(f"Unexpected result: {result}")
            if synthesis and not all(result["generic_cells"][key] > 0 for key in ("direct", "cyclic")):
                raise AssertionError(f"Missing synthesis data: {result}")
            print(f"MCP HDL/MMA: {result['case_count']} cases; 4 direct clocks, 24 cyclic clocks.")
            if synthesis:
                print(f"Generic Yosys cells: {result['generic_cells']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--synthesis", action="store_true")
    asyncio.run(asyncio.wait_for(check(parser.parse_args().synthesis), timeout=65))
