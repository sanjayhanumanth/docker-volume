import os
import time

# Default to /data so it works with your --mount
file_path = os.getenv("LOG_PATH", "/data/log.txt")

# Create directory if not exists
os.makedirs(os.path.dirname(file_path), exist_ok=True)

while True:
    try:
        with open(file_path, "a") as f:
            f.write("Hello from Docker Volume!\n")

        print(f"Written to {file_path}", flush=True)
        time.sleep(5)


    except Exception as e:
        print(f"Error: {e}", flush=True)
        time.sleep(5)