import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

model = os.getenv("OPENROUTER_MODEL")

print("AI Playground")
print(f"Model: {model}")
print("Type 'exit' to quit the program.\n")

running = True

while running:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        running = False
        print("Goodbye!")
    else:
        response = client.responses.create(
            model=model,
            input=user_message
        )

        print(f"\nAI: {response.output_text}\n")