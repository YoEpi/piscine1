def decalage_alphabet(caractere, decalage):
    if 'a' <= caractere <= 'z':
        min_char, max_char = 'a', 'z'
    elif 'A' <= caractere <= 'Z':
        min_char, max_char = 'A', 'Z'
    else:
        # Le caractère n'est pas une lettre, ne le décalez pas.
        return caractere

    decale = ord(caractere) + decalage
    if decale < ord(min_char):
        decale += 25
    elif decale > ord(max_char):
        decale -= 25

    return chr(decale)

def decaler_chaine(chaine, decalage):
    resultat = ""
    for caractere in chaine:
        resultat += decalage_alphabet(caractere, decalage)
    return resultat

chaine = str(input("Write your string: "))
decalage = int(input("Choose the kay: "))
chaine_decalee = decaler_chaine(chaine, decalage)
print(chaine_decalee)