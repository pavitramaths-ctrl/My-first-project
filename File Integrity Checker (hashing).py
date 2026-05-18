import hashlib

# Function to generate SHA-256 hash
def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while True:
                data = file.read(4096)
                if not data:
                    break
                sha256.update(data)

        return sha256.hexdigest()

    except FileNotFoundError:
        return "File not found!"

# Get file path from user
file_path = input("Enter file path: ")

# Generate hash
file_hash = calculate_hash(file_path)

# Display hash
print("\nSHA-256 Hash:")
print(file_hash)
