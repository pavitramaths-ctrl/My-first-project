failed_attempts = 0
max_attempts = 3

correct_password = "admin123"

print("==== Brute Force Detection System ====")

while True:

    password = input("Enter Password: ")

    # Correct password
    if password == correct_password:
        print("Access Granted!")
        break

    # Wrong password
    else:
        failed_attempts += 1

        print("Wrong Password!")
        print("Failed Attempts:", failed_attempts)

        # Brute force detection
        if failed_attempts >= max_attempts:
            print("\nWARNING: Possible Brute Force Attack Detected!")
            break
