"""MCP access to the bounded HDL/MMA reference comparison."""

import json
import os
import shutil
import subprocess
import sys

from typing_extensions import NotRequired, TypedDict

from qsc_mcp_server import MAX_OUTPUT_CHARS, PROJECT_ROOT


class HdlCheckResult(TypedDict):
    ok: bool
    returncode: NotRequired[int]
    result: NotRequired[dict]
    error: NotRequired[str]
    output_tail: NotRequired[str]


def _command(synthesis: bool) -> list[str]:
    tools = ("iverilog", "vvp", "yosys") if synthesis else ("iverilog", "vvp")
    use_wsl = (os.name == "nt" and not all(shutil.which(tool) for tool in tools)
               and shutil.which("wsl.exe"))
    python = [use_wsl, "--exec", "python3"] if use_wsl else [sys.executable]
    command = [*python, "-B", "-X", "utf8", "-m", "qam.examples.zuse_machine.hdl.check", "--json"]

    # A portable WSL installation may keep its launchers in the local build tree.
    for tool in tools:
        launcher = PROJECT_ROOT / "build" / "hdl-tools" / tool
        if use_wsl and launcher.is_file():
            command.extend([f"--{tool}", launcher.relative_to(PROJECT_ROOT).as_posix()])
        elif tool == "yosys":
            command.append("--yosys")
    return command


def run_qam_hdl_check(synthesis: bool = False) -> HdlCheckResult:
    """Compare both SystemVerilog tape controllers with MMA on the 209 reference cases.

    Returns stop reasons, clock counts and the increment trace. With synthesis=true,
    also reports generic Yosys cell counts before FPGA mapping. Requires Icarus
    Verilog, and Yosys for synthesis. Runs a fixed suite with temporary files.
    """
    try:
        completed = subprocess.run(
            _command(synthesis), cwd=PROJECT_ROOT, capture_output=True, text=True,
            encoding="utf-8", errors="replace", timeout=55, check=False,
        )
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "HDL/MMA comparison exceeded 55 seconds."}
    except OSError as error:
        return {"ok": False, "error": str(error)}

    if completed.returncode != 0:
        diagnostics = "\n".join(part.strip() for part in (completed.stdout, completed.stderr) if part.strip())
        return {"ok": False, "returncode": completed.returncode,
                "error": diagnostics[-MAX_OUTPUT_CHARS:]}
    try:
        result = json.loads(completed.stdout)
    except ValueError:
        return {"ok": False, "returncode": completed.returncode,
                "error": "HDL runner did not return JSON.",
                "output_tail": completed.stdout[-MAX_OUTPUT_CHARS:]}
    return {"ok": True, "returncode": completed.returncode, "result": result}
