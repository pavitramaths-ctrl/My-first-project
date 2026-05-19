import os

print("==== Directory Scanner ====\n")

# Get directory path from user
directory = input("Enter directory path: ")

try:
    # Check if directory exists
    if os.path.exists(directory):

        print("\n==== Files and Folders ====\n")

        # List files and folders
        items = os.listdir(directory)

        for item in items:
            full_path = os.path.join(directory, item)

            # Check type
            if os.path.isfile(full_path):
                print("[FILE]  ", item)

            elif os.path.isdir(full_path):
                print("[FOLDER]", item)

    else:
        print("\nDirectory does not exist!")

except Exception as e:
    print("\nError:", e)
