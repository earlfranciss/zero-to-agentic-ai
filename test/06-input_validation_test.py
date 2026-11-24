def validate_input(message):
    # Remove unnecessary whitespace
    message = message.strip()

    # Check if the message is empty
    if not message:
        return None

    return message

# Get user input and validate it
user_input = input("You: ")
validated_input = validate_input(user_input)

if validated_input is None:
    print("Error: Input cannot be empty.")
else:
    print(f"Validated input: {validated_input}")