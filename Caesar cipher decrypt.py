print("=== Caesar Cipher Decrypt ===")

# Get encrypted message
message = input("Enter encrypted message: ")

# Get shift value
shift = int(input("Enter shift value: "))

decrypted_text = ""

# Decrypt each character
for char in message:

    # Decrypt uppercase letters
    if char.isupper():
        decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

    # Decrypt lowercase letters
    elif char.islower():
        decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

    # Keep spaces, numbers, symbols unchanged
    else:
        decrypted_text += char

# Display decrypted message
print("\nDecrypted Message:", decrypted_text)
