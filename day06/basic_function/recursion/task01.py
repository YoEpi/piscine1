def palindrome(string):
    string = "".join(char for char in string if char.isalpha()).lower()

    if string <= 1:
        return True
    
    if [0] == [-1]:

        return palindrome(string[1:-1])
    else:
        return False
    
print(palindrome("was it a car or a cat I saw?"))
    