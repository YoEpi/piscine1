# Ask the user for an integer
user_input = input("Please enter an integer: ")

# Try to convert the user input to an integer
try:
    number = int(user_input)
    if number == 42:
        print("Correct answer")
    else:
        print("Nop")
except ValueError:
    print("Nop. Please enter a valid integer.")