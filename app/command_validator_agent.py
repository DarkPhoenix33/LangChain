"""
command_validator_agent.py
Validates if a PowerShell command is safe / correct.
"""
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI

def get_command_validation_chain(openai_api_key: str) -> LLMChain:
    """
    Returns an LLMChain that takes 'command' as input
    and outputs either 'VALIDATED' or 'REJECTED'.
    """
    prompt = PromptTemplate(
        input_variables=["command"],
        template="""
You are a system command expert. 
1. Check if this PowerShell command is syntactically valid.
2. Check if it is obviously malicious or destructive (e.g. removing system directories).
3. Stopping an IIS app pool is typically a normal admin task, so it's not malicious.
4. Return EXACTLY one of:
   - "VALIDATED" if the command is safe and correct,
   - "REJECTED" if it's obviously harmful or invalid.

Command to validate:
{command}
        """
    )

    llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0, model_name="gpt-3.5-turbo")
    return LLMChain(llm=llm, prompt=prompt)
