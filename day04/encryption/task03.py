# Function to perform Vigenere encryption and decryption
def vigenere_cipher(text, key, decrypt=False):
    key_length = len(key)
    result = []

    for i, char in enumerate(text):
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.upper()) - ord('A')

            # Reverse the shift for decryption
            if decrypt:
                shift = 26 - shift

            if char.isupper():
                # Encrypt/Decrypt uppercase characters
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                # Encrypt/Decrypt lowercase characters
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))

            result.append(encrypted_char)
        else:
            # Preserve non-alphabetic characters
            result.append(char)

    return ''.join(result)

# Prompt the user for the mode (encrypt or decrypt)
mode = input("Enter 'encrypt' or 'decrypt': ").strip().lower()

if mode not in ['encrypt', 'decrypt']:
    print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
    exit()

# Prompt the user for the text and key
text = input("Enter the text: ")
key = input("Enter the key: ")

if mode == 'encrypt':
    encrypted_text = vigenere_cipher(text, key)
    print("Encrypted text:", encrypted_text)
else:
    decrypted_text = vigenere_cipher(text, key, decrypt=True)
    print("Decrypted text:", decrypted_text)
