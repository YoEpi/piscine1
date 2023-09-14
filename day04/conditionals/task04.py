
user_input = input("Please enter an integer: ")

try:
    number = int(user_input)
    
    if number == 42 or number <= 21 or number % 2 == 0 or (number // 2) < 21 or (number % 2 == 1 and number >= 45):
        print("OK")
    else:
        print("You got it wrong, my poor friend!")
except ValueError:
    print("Invalid input. Please enter a valid integer.")