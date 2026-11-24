MAX_INPUT_LENGTH = 500

def validate_input(message):
    # Remove unnecessary whitespace
    message = message.strip()

    # Check if the message is empty
    if not message:
        return None

    # Check if the message exceeds the maximum length
    if len(message) > MAX_INPUT_LENGTH:
        return None

    return message

user_input = input("You: ")
validated_input = validate_input(user_input)

if validated_input is None:
    print("Error: Input cannot be empty or exceed 500 characters.")
else:
    print(f"Validated input: {validated_input}")
    print(f"Input length: {len(validated_input)} characters")