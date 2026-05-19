# Password Strength Checker
# Python Version: 3.14

import string

print("==== Password Strength Checker ====\n")

# Get password from user
password = input("Enter your password: ")

score = 0

# Check password length
if len(password) >= 8:
    score += 1

# Check uppercase letter
if any(char.isupper() for char in password):
    score += 1

# Check lowercase letter
if any(char.islower() for char in password):
    score += 1

# Check digit
if any(char.isdigit() for char in password):
    score += 1

# Check special character
if any(char in string.punctuation for char in password):
    score += 1

# Display result
print("\n==== Password Strength Result ====")

if score == 5:
    print("Strength : Very Strong")
elif score == 4:
    print("Strength : Strong")
elif score == 3:
    print("Strength : Medium")
elif score == 2:
    print("Strength : Weak")
else:
    print("Strength : Very Weak")
