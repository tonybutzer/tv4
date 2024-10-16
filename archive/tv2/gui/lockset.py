import os
import time
from filelock import Timeout, FileLock

file_path = "high_ground.txt"
lock_path = "high_ground.txt.lock"

lock = FileLock(lock_path, timeout=1)

# The lock object supports multiple ways for acquiring the lock, including the ones used to acquire standard Python thread locks:

with lock:
    with open(file_path, "a") as f:
        f.write("Hello there!")
        time.sleep(30)

'''
lock.acquire()
try:
    with open(file_path, "a") as f:
        f.write("General Kenobi!")
finally:
    lock.release()
'''

