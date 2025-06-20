import hashlib
import os
import time
from datetime import datetime

# Files to monitor
FILES_TO_MONITOR = ["important_info.txt"]

# Store baseline hashes
def hash_file(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()

def generate_baseline():
    baseline = {}
    for file in FILES_TO_MONITOR:
        if os.path.exists(file):
            baseline[file] = hash_file(file)
    return baseline

# Monitor loop
def monitor_files(baseline):
    print("[*] Monitoring files for changes... Press Ctrl+C to stop.")
    while True:
        for file in FILES_TO_MONITOR:
            if os.path.exists(file):
                current_hash = hash_file(file)
                if current_hash != baseline.get(file):
                    alert_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    print(f"[ALERT] {file} was modified at {alert_time}!")
                    with open("file_alerts.log", "a") as log:
                        log.write(f"[{alert_time}] {file} integrity changed!\n")
                    baseline[file] = current_hash
        time.sleep(5)  # Check every 5 seconds

# Run
if __name__ == "__main__":
    baseline_hashes = generate_baseline()
    monitor_files(baseline_hashes)