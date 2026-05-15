import re

print("=== Input Sanitization ===")

text = input("Enter Text: ")

# Remove spaces from start and end
text = text.strip()

# Remove special characters
text = re.sub(r'[^a-zA-Z0-9 ]', '', text)

# Convert into lowercase
text = text.lower()

print("Sanitized Text:", text)
