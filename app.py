import os
import time

file_path = os.getenv("LOG_PATH", "./data/log.txt")

os.makedirs(os.path.dirname(file_path), exist_ok=True)

counter = 1

while True:
    try:
        with open(file_path, "a") as f:
            line = f"{counter} - Hello from Docker Volume!\n"
            f.write(line)

        print(line.strip(), flush=True)  # optional (for docker logs)

        counter += 1
        time.sleep(5)

    except Exception as e:
        print(f"Error: {e}", flush=True)
        time.sleep(5)