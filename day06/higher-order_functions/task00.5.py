def funA():
    in_mot = input("Entrez un mot: ")
    nb = int(input("checks if s contains at least [Enter your number] uppercase: "))
    
    lowercase_count = 0

    for char in in_mot:
        if char.islower():
            lowercase_count += 1

        if lowercase_count >= nb:
            return True
    
    return False


def funB():
    in_mot = input("Entrez un mot: ")
    nb = int(input("checks if s contains at least [Enter your number] uppercase: "))
    uppercase_count = 0
    for char in in_mot:
        if char.isupper():
            uppercase_count += 1
        
        if uppercase_count >= nb:
            return True
        
    return False
def funC():
    in_mot = input("Entrez un mot: ")
    nb = int(input("checks if s contains at least [Enter your number] characters: "))
    len_word = 0
    len_word = len(in_mot)
        
    if len_word >= nb:
        return True
        
    return False
def funD():
    in_mot = input("Entrez un mot: ")
    nb = int(input("checks if s contains at least [Enter your number] special characters: "))
    special_count = 0
    for char in in_mot:
        if char.isalpha() == False and char.isalnum() == False:
            special_count += 1
        
        if special_count >= nb:
            return True
        
    return False
def funE():
    in_mot = input("Entrez un mot: ")
    nb = int(input("checks if s contains at least [Enter your number] numbers: "))
    nb_count = 0
    for char in in_mot:
        if char.isdigit():
            nb_count += 1
        
        if nb_count >= nb:
            return True
        
    return False

if funE() == True:
    print("True")
else:
    print("False")