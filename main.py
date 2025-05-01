import sys
from app.agent_manager import process_user_request
from config import OPENAI_API_KEY
def main():
    print("Welcome to the Agentic Command App (PowerShell + WebAdministration)!")
    print("Enter a natural language request to generate and validate a command.")
    print("Example: 'Stop the IIS application pool named MyAppPool'")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Your request> ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting.")
            sys.exit(0)

        confirm_execute = input("Execute after validation? (y/n) [default=n]: ").strip().lower()
        execute_flag = (confirm_execute == "y")

        result = process_user_request(
            user_request=user_input,
            openai_api_key=OPENAI_API_KEY,
            execute=execute_flag
        )

        print("\n--- RESULT ---")
        print(result)
        print("-------------\n")


if __name__ == "__main__":
    main()
