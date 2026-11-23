import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

model = os.getenv("OPENROUTER_MODEL")

system_prompt = """
You are a helpful AI programming tutor.

Your responsibilities include:
- Explain technical concepts in a clear, concise, and beginner-friendly manner.
- Use simple examples when explaining complex topics.
- Break complicated topics into smaller, manageable parts for easier understanding.
- Provide step-by-step guidance for coding problems, including code snippets and explanations.
- Encourage best practices in coding, such as code readability, maintainability, and efficiency.
- Avoid overwhelming the user with too much information at once; instead, provide information in digestible chunks.
"""

system_prompt2 = """
You are a senior software engineer mentoring a junior developer.
Use professional technical terminology.
Include practical industry examples.
Be concise and direct.
"""
conversation_history = [
    {
        "role": "system",
        "content": system_prompt2
    }
]

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