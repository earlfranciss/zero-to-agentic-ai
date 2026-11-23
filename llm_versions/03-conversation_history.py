import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

model = os.getenv("OPENROUTER_MODEL")

conversation_history = []

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
        conversation_history.append({
            "role": "user",
            "content": user_message
        })

        response = client.chat.completions.create(
            model=model,
            messages=conversation_history
        )
        
        ai_message = response.choices[0].message.content

        conversation_history.append({
            "role": "assistant",
            "content": ai_message
        })

        print(f"\nAI: {ai_message}\n")