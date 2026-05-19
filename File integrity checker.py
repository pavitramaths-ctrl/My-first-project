# File Integrity Checker
# Python Version: 3.14

import hashlib

print("==== File Integrity Checker ====\n")

# Get file name from user
file_name = input("Enter file name: ")

try:
    # Create SHA256 hash object
    sha256_hash = hashlib.sha256()

    # Open file in binary mode
    with open(file_name, "rb") as file:

        # Read file in chunks
        while chunk := file.read(4096):
            sha256_hash.update(chunk)

    # Final hash value
    file_hash = sha256_hash.hexdigest()

    print("\nSHA256 File Hash:")
    print(file_hash)

except FileNotFoundError:
    print("\nError: File not found!")

except Exception as e:
    print("\nError:", e)
