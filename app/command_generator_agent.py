"""
command_generator_agent.py

Defines a LangChain LLMChain for turning a natural language request
into a PowerShell command using ChatOpenAI and WebAdministration,
without any literal curly braces in the prompt text.
"""

from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI

def get_command_generation_chain(openai_api_key: str) -> LLMChain:
    """
    Returns an LLMChain that takes 'instruction' as input
    and outputs a single command or "INVALID REQUEST".
    """
    # IMPORTANT: No curly braces except for {instruction} below.
    prompt_text = """
You are a helpful assistant specialized in writing correct, safe, minimal PowerShell commands
on Windows that use the WebAdministration module for IIS tasks.

Rules:
1. If the user wants an IIS action (like listing or stopping app pools), 
   you can use Import-Module WebAdministration plus cmdlets like Get-IISAppPool, Stop-WebAppPool, etc.
2. If the user requests something unrelated to IIS, generate a normal PowerShell command.
3. If the request is impossible or very destructive, output "INVALID REQUEST".
4. Provide only the final PowerShell command (no extra explanations).

User request: {instruction}
"""

    prompt = PromptTemplate(
        input_variables=["instruction"],
        template=prompt_text
    )

    llm = ChatOpenAI(
        openai_api_key=openai_api_key,
        temperature=0,
        model_name="gpt-4.1"  # or "gpt-4" if you prefer
    )

    return LLMChain(llm=llm, prompt=prompt)
