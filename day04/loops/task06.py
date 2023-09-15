n = int(input("Enter an integer (n): "))

user_input = input("Enter a string: ")

if n == 0: 
    exit()
def contains_vowel(user_input):
    vowels = "AEIOUaeiou"
    for char in user_input:
        if char in vowels:
            return True
    return False

if contains_vowel(user_input) :
    print (n)

elif n >= 42:
    print(n)

else: 
    print(user_input)

