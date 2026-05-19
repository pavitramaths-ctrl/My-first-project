# SHA256 Password Hasher
# Python Version: 3.14

import hashlib

print("==== SHA256 Password Hasher ====\n")

# User input
password = input("Enter password: ")

# Convert password to bytes
password_bytes = password.encode('utf-8')

# Create SHA256 hash
hashed_password = hashlib.sha256(password_bytes).hexdigest()

# Display result
print("\nSHA256 Hashed Password:")
print(hashed_password)
