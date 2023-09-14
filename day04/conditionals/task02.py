# Ask the user for an integer
user_input = input("Please enter an integer: ")

# Try to convert the user input to an integer
try:
    number = int(user_input)
    if number % 2 == 0 :
        print("This integer is even”")
    else:
        print("This integer is odd")
except ValueError:
    print("Nop. Please enter a valid integer.")