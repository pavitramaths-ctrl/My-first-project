import hashlib

print("==== Compare SHA256 Hashes ====\n")

# First password
password1 = input("Enter first password: ")

# Second password
password2 = input("Enter second password: ")

# Convert to SHA256 hashes
hash1 = hashlib.sha256(password1.encode()).hexdigest()
hash2 = hashlib.sha256(password2.encode()).hexdigest()

# Display hashes
print("\nFirst Password Hash:")
print(hash1)

print("\nSecond Password Hash:")
print(hash2)

# Compare hashes
print("\n==== Result ====")

if hash1 == hash2:
    print("Both hashes are MATCHING")
else:
    print("Hashes are DIFFERENT")
