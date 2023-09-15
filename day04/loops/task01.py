
user_input = input("Enter a string: ")

# Initialize an empty string to store the result
result = ""


for char in user_input:
    result += char * 2


print(result)
