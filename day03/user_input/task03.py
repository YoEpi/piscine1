
user_input = input("Please enter a whole number: ")

# convertir user input en integer
try:
    number = int(user_input)
    result = type(number)
    print(f"The data type is {result}")
except ValueError:
    print("Invalid input. Please enter a valid whole number.")