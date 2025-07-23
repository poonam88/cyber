from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

fake_logs = [
    "Login failed for user admin from 192.168.1.10",
    "Disk space running low on server xyz",
    "Multiple login attempts detected",
    "User uploaded suspicious file",
    "Normal operation log entry",
    "Connection timed out from IP 172.16.0.1"
]

@app.route("/get-logs", methods=["GET"])
def get_logs():
    # Simulate returning 5 random logs
    logs = random.choices(fake_logs, k=5)
    return jsonify({"logs": logs})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
