import string

def check_password(check_type, n, password):
    if check_type == "lower":
        count = sum(1 for char in password if char.islower())
        return count >= n
    elif check_type == "upper":
        count = sum(1 for char in password if char.isupper())
        return count >= n
    elif check_type == "special":
        special_chars = set(string.punctuation)
        count = sum(1 for char in password if char in special_chars)
        return count >= n
    elif check_type == "numeric":
        count = sum(1 for char in password if char.isdigit())
        return count >= n
    else:
        raise ValueError("Invalid check_type. Supported values: 'lower', 'upper', 'special', 'numeric'")

# Example usages:
result1 = check_password("lower", 4, "mysecretpassword")
result2 = check_password("special", 2, "mysecretpassword")

print(f"Password meets lowercase check: {result1}")
print(f"Password meets special character check: {result2}")
