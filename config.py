import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env if present

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")
