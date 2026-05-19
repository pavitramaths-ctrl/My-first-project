# Base64 Encode and Decode
# Python Version: 3.14

import base64

print("==== Base64 Encode / Decode ====\n")

print("1. Encode Text")
print("2. Decode Text")

choice = input("\nEnter your choice (1 or 2): ")

# Encode
if choice == "1":
    text = input("\nEnter text to encode: ")

    encoded_text = base64.b64encode(text.encode()).decode()

    print("\nEncoded Text:")
    print(encoded_text)

# Decode
elif choice == "2":
    text = input("\nEnter Base64 text to decode: ")

    decoded_text = base64.b64decode(text.encode()).decode()

    print("\nDecoded Text:")
    print(decoded_text)

else:
    print("\nInvalid Choice")
