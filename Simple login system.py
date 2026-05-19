# Simple Login System
# Python Version: 3.14

print("==== Simple Login System ====\n")

# Stored username and password
stored_username = "admin"
stored_password = "1234"

# User input
username = input("Enter username: ")
password = input("Enter password: ")

# Check login
print("\n==== Login Result ====")

if username == stored_username and password == stored_password:
    print("Login Successful")
else:
    print("Invalid Username or Password")
