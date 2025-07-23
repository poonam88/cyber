import time
import random

# Sample log messages
logs = [
    "User admin failed to login from IP 192.168.1.5",
    "SSH connection established from 10.10.10.10",
    "SQL injection attempt detected in query",
    "File /etc/passwd accessed unexpectedly",
    "High CPU usage on server X",
    "Successful login by root",
    "Alert: Malware signature matched"
]

def stream_logs(output_file="logs_stream.txt", delay=3):
    while True:
        log = random.choice(logs)
        with open(output_file, "a") as f:
            f.write(log + "\n")
        print(f"Written log: {log}")
        time.sleep(delay)

# Uncomment below to run standalone
# stream_logs()
