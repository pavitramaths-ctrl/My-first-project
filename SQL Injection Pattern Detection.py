print("=== SQL Injection Pattern Detection ===")

user_input = input("Enter Login Input: ")

# SQL Injection keywords
sql_patterns = [
    "SELECT",
    "DROP",
    "DELETE",
    "INSERT",
    "UPDATE",
    "OR 1=1",
    "--",
    "' OR '1'='1"
]

# Convert input to uppercase
check_input = user_input.upper()

found = False

for pattern in sql_patterns:
    if pattern in check_input:
        found = True
        break

# Result
if found:
    print("Warning: Possible SQL Injection Detected!")
else:
    print("Input Looks Safe")
