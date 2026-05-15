import re

print("=== Password Strength Checker ===")

password = input("Enter Password: ")

strength = 0

# Length Check
if len(password) >= 8:
    strength += 1

# Uppercase Check
if re.search("[A-Z]", password):
    strength += 1

# Lowercase Check
if re.search("[a-z]", password):
    strength += 1

# Number Check
if re.search("[0-9]", password):
    strength += 1

# Special Character Check
if re.search("[@#$%^&*!]", password):
    strength += 1

# Result
if strength <= 2:
    print("Weak Password")
elif strength == 3 or strength == 4:
    print("Medium Password")
else:
    print("Strong Password")
