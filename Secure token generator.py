# Secure Token Generator
# Python Version: 3.14

import secrets
import string

print("==== Secure Token Generator ====\n")

# User input
length = int(input("Enter token length: "))

# Characters for token
characters = string.ascii_letters + string.digits

# Generate secure token
token = ''.join(secrets.choice(characters) for _ in range(length))

# Display token
print("\nGenerated Secure Token:")
print(token)
