user_input = input("Please enter a passphrase: ")

# Try to convert the user input to an integer
try:
    
    if user_input == "open sesame" :
        print("Access granted”")
    elif user_input == "will you open, you goddamn !¤*@¡' ":
        print("Access fucking granted")
    else:
        print("Permission denied")
except ValueError:
    print("Nop. Please enter a valid string.")