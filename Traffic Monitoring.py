import time
from datetime import datetime
import psutil

print("==== Network Traffic Monitor ====")

try:
    while True:
        # Get network I/O statistics
        net_io = psutil.net_io_counters()

        bytes_sent = net_io.bytes_sent
        bytes_recv = net_io.bytes_recv
        packets_sent = net_io.packets_sent
        packets_recv = net_io.packets_recv

        # Convert bytes to MB
        sent_mb = bytes_sent / (1024 * 1024)
        recv_mb = bytes_recv / (1024 * 1024)

        # Current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("\n==============================")
        print("Time:", current_time)
        print("==============================")
        print(f"Data Sent     : {sent_mb:.2f} MB")
        print(f"Data Received : {recv_mb:.2f} MB")
        print(f"Packets Sent  : {packets_sent}")
        print(f"Packets Recv  : {packets_recv}")

        # Wait 5 seconds
        time.sleep(5)

except KeyboardInterrupt:
    print("\nMonitoring Stopped.")
