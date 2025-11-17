#This script creates a SHA-256 hash of a file and alerts you if the file changes later
import hashlib
import time
import os

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def monitor_file(file_path, interval=5):
    if not os.path.exists(file_path):
        print("File not found.")
        return

    print(f"Monitoring changes in: {file_path}")
    old_hash = calculate_hash(file_path)

    while True:
        time.sleep(interval)
        new_hash = calculate_hash(file_path)

        if new_hash != old_hash:
            print("⚠️ ALERT: FILE HAS BEEN MODIFIED!")
            print(f"Old Hash: {old_hash}")
            print(f"New Hash: {new_hash}")
            old_hash = new_hash
        else:
            print("No change detected...")

if __name__ == "__main__":
    path = input("Enter file path to monitor: ")
    monitor_file(path)
