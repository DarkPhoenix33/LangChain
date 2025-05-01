"""
agent_manager.py
Orchestrates:
1) Generating a command from the user's request.
2) Validating the command.
3) (Optionally) executing it in PowerShell.
"""

from app.command_generator_agent import get_command_generation_chain
from app.command_validator_agent import get_command_validation_chain
from app.tools.powershell_executor import PowerShellExecutorTool

def process_user_request(
    user_request: str,
    openai_api_key: str,
    execute: bool = False
) -> str:
    """
    1. Generate the command via LLM
    2. Validate the command
    3. Execute (optionally) if validated
    """

    # Step 1: Generate the command
    command_chain = get_command_generation_chain(openai_api_key)
    generated_command = command_chain.run(instruction=user_request).strip()

    if generated_command.upper() == "INVALID REQUEST":
        return "Could not generate a valid command for this request."

    # Step 2: Validate the command
    validation_chain = get_command_validation_chain(openai_api_key)
    validation_result = validation_chain.run(command=generated_command).strip()

    if validation_result != "VALIDATED":
        return f"Command was rejected by validator. Reason: {validation_result}"

    # Step 3: Execute if user allowed
    if execute:
        executor = PowerShellExecutorTool()
        exec_result = executor.run(generated_command)
        return f"Command Executed:\n{generated_command}\n\nOutput:\n{exec_result}"
    else:
        return f"Command generated and validated, but not executed:\n{generated_command}"
