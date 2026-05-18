import os
import shutil
from datetime import datetime

print("==== AUTO BACKUP SCRIPT ====")

# Source folder
source_folder = input("Enter source folder path: ")

# Backup folder
backup_folder = input("Enter backup folder path: ")

# Check source folder exists
if not os.path.exists(source_folder):
    print("Error: Source folder not found!")
    exit()

# Create backup folder if not exists
if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)

# Current date and time
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Backup folder name
backup_name = f"backup_{timestamp}"

# Full backup path
destination = os.path.join(backup_folder, backup_name)

try:
    # Copy folder
    shutil.copytree(source_folder, destination)

    print("\nBackup completed successfully!")
    print("Backup saved at:")
    print(destination)

except Exception as e:
    print("Error:", e)
