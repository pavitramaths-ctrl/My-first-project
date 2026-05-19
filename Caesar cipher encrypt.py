print("=== Caesar Cipher Encrypt ===")

# Get message from user
message = input("Enter message: ")

# Get shift value
shift = int(input("Enter shift value: "))

encrypted_text = ""

# Encrypt each character
for char in message:
    
    # Encrypt uppercase letters
    if char.isupper():
        encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    
    # Encrypt lowercase letters
    elif char.islower():
        encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    
    # Keep spaces, numbers, symbols unchanged
    else:
        encrypted_text += char

# Display encrypted message
print("\nEncrypted Message:", encrypted_text)
