print("==== Detect Login Attempts ====\n")

# Correct credentials
correct_username = "admin"
correct_password = "1234"

# Maximum attempts
max_attempts = 3
attempt = 0

# Login loop
while attempt < max_attempts:

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    # Check credentials
    if username == correct_username and password == correct_password:
        print("\nLogin Successful")
        break

    else:
        attempt += 1
        remaining = max_attempts - attempt

        print("\nInvalid Username or Password")

        if remaining > 0:
            print("Remaining Attempts:", remaining)

# Block after maximum attempts
if attempt == max_attempts:
    print("\nToo Many Failed Login Attempts!")
    print("Access Blocked")
