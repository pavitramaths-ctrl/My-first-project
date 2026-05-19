# Duplicate File Detector
# Python Version: 3.14

import os
import hashlib

print("==== Duplicate File Detector ====\n")

# Get folder path
folder_path = input("Enter folder path: ")
# Store file hashes
hashes = {}

try:
    # Walk through directory
    for root, dirs, files in os.walk(folder_path):

        for file in files:

            file_path = os.path.join(root, file)

            try:
                # Create SHA256 hash
                sha256 = hashlib.sha256()

                # Read file in binary mode
                with open(file_path, "rb") as f:
                    while chunk := f.read(4096):
                        sha256.update(chunk)

                file_hash = sha256.hexdigest()

                # Check duplicate
                if file_hash in hashes:
                    print("\nDuplicate Found:")
                    print("Original :", hashes[file_hash])
                    print("Duplicate:", file_path)

                else:
                    hashes[file_hash] = file_path

            except Exception as e:
                print("\nCould not read file:", file_path)
                print("Error:", e)

except Exception as e:
    print("\nError:", e)

print("\nScan Completed")
