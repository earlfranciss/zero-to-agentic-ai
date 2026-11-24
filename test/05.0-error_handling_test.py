try:
    user_input = input("Enter an integer: ")
    number = int(user_input)
    result = 100 / number
    print(f"The result is: {result}")

except ValueError:
    print("Error: Please enter a valid integer.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

print("Program finished.")