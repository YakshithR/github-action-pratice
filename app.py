import time
import os
from datetime import datetime

APP_NAME = "VYROXXx"
PORT = 5000

print("=" * 40)
print(f"{APP_NAME} APPLICATION STARTED")
print("=" * 40)

print(f"Process ID: {os.getpid()}")
print(f"Port: {PORT}")
print(f"Started at: {datetime.now()}")

while True:
    print(f"[{datetime.now()}] Application is running...")
    time.sleep(10)
