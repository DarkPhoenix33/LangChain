"""
powershell_executor.py
Executes a PowerShell command via subprocess.
"""

import subprocess
from langchain.tools import BaseTool

class PowerShellExecutorTool(BaseTool):
    name = "powershell_executor"
    description = "Executes a PowerShell command on Windows."

    def _run(self, command: str) -> str:
        try:
            ps_command = ["powershell.exe", "-Command", command]
            result = subprocess.run(ps_command, capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout.strip()
            else:
                return f"ERROR: {result.stderr.strip()}"
        except Exception as e:
            return f"Exception while running command: {str(e)}"

    async def _arun(self, command: str) -> str:
        raise NotImplementedError("Async execution not implemented.")
