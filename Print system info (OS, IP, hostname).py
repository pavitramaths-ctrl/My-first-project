# System Information Program
# Python Version: 3.14

import platform
import socket


def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception:
        return "Unable to get IP Address"


print("==== System Information ====\n")

# Operating System Information
print("Operating System :", platform.system())
print("OS Version       :", platform.version())

# Computer Name
hostname = socket.gethostname()
print("Hostname         :", hostname)

# IP Address
print("IP Address       :", get_ip_address())

# Processor Information
print("Processor        :", platform.processor())

# Machine Type
print("Machine          :", platform.machine())

# Python Version
print("Python Version   :", platform.python_version())
