# Password Generator
# Python Version: 3.14

import random
import string

print("==== Password Generator ====\n")

# User input
length = int(input("Enter password length: "))

# Characters to use
characters = (
    string.ascii_letters +     # A-Z and a-z
    string.digits +            # 0-9
    string.punctuation         # Special symbols
)

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display password
print("\nGenerated Password:")
print(password)
