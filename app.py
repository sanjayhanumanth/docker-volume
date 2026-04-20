import time
import os

file_path = "./data/log.txt"

# Create folder if not exists
os.makedirs("./data", exist_ok=True)

while True:
    with open(file_path, "a") as f:
        f.write("Hello from Docker Volume!\n")
    print("Written to file...")
    time.sleep(5)