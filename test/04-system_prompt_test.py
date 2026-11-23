
system_prompt = """
You are a helpful AI programming tutor.

Your responsibilities:
- Explain technical concepts in beginner-friendly language.
- Use simple examples when explaining concepts.
- Break complicated topics into smaller steps.
- Avoid overwhelming the user with too much information.
"""

conversation_history = []

conversation_history.append({
    "role": "system",
    "content": system_prompt
})

conversation_history.append({
    "role": "user",
    "content": "Explain what an API is."
})

print("System Prompt:")
print(conversation_history[0]["content"])

print("\nConversation History:")
print(conversation_history)
