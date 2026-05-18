import os

print("==== Log File Analyzer ====")

# Log file name
log_file = "server_log.txt"

# Auto create sample log file
if not os.path.exists(log_file):

    with open(log_file, "w") as file:
        file.write("INFO: Server Started\n")
        file.write("INFO: User Login Success\n")
        file.write("WARNING: High Memory Usage\n")
        file.write("ERROR: Database Connection Failed\n")
        file.write("INFO: File Uploaded\n")
        file.write("ERROR: Invalid Password Attempt\n")

print("Sample log file created: server_log.txt")

# Read log file
with open(log_file, "r") as file:
    logs = file.readlines()

# Counters
info_count = 0
warning_count = 0
error_count = 0

# Analyze logs
for line in logs:

    if "INFO" in line:
        info_count += 1

    elif "WARNING" in line:
        warning_count += 1

    elif "ERROR" in line:
        error_count += 1

# Display Results
print("\n==== Log Analysis Result ====\n")

print("INFO Messages   :", info_count)
print("WARNING Messages:", warning_count)
print("ERROR Messages  :", error_count)

# Show suspicious activity
if error_count > 0:
    print("\nWARNING: Errors detected in log file!")
