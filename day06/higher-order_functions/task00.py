import string

def contains_n_lowercase_letters(s, n):
    count = sum(1 for char in s if char.islower())
    return count >= n

def contains_n_uppercase_letters(s, n):
    count = sum(1 for char in s if char.isupper())
    return count >= n

def contains_n_characters(s, n):
    return len(s) >= n

def contains_n_special_characters(s, n):
    special_chars = set(string.punctuation)
    count = sum(1 for char in s if char in special_chars)
    return count >= n

def contains_n_numbers(s, n):
    count = sum(1 for char in s if char.isdigit())
    return count >= n

# Example usage:
s = "Hello123World!"
n = 3

print(contains_n_lowercase_letters(s, n))  # Check if s contains at least 3 lowercase letters
print(contains_n_uppercase_letters(s, n))  # Check if s contains at least 3 uppercase letters
print(contains_n_characters(s, n))         # Check if s contains at least 3 characters
print(contains_n_special_characters(s, n))  # Check if s contains at least 3 special characters
print(contains_n_numbers(s, n))            # Check if s contains at least 3 numbers
