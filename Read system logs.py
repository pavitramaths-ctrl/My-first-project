print("==== Read System Logs ====\n")

# Log file name
log_file = input("Enter log file name: ")

try:
    # Open and read file
    with open(log_file, "r", encoding="utf-8") as file:
        logs = file.readlines()

    print("\n==== Log File Content ====\n")

    # Display logs line by line
    for line in logs:
        print(line.strip())

except FileNotFoundError:
    print("\nError: Log file not found!")

except Exception as e:
    print("\nError:", e)
