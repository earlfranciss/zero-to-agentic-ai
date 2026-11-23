running = True

while running:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        running = False
        print("Goodbye!")
    else:
        print("You said: ", user_message)