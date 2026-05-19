# Basic Port Scanner
# Python Version: 3.14

import socket

print("==== Basic Port Scanner ====\n")

# User input
target = input("Enter Target IP or Domain: ")

# Common ports to scan
ports = [20, 21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 8080]

print(f"\nScanning Target: {target}\n")

# Scan ports
for port in ports:
    try:
        # Create socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set timeout
        s.settimeout(1)

        # Try connection
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")

        s.close()

    except KeyboardInterrupt:
        print("\nScan Stopped")
        break

    except socket.gaierror:
        print("Hostname could not be resolved")
        break

    except Exception as e:
        print("Error:", e)
        break

print("\nScan Completed")
