from filelock import Timeout, FileLock

file_path = "high_ground.txt"
lock_path = "high_ground.txt.lock"

lock = FileLock(lock_path, timeout=1)


lock.acquire()
try:
    with open(file_path, "a") as f:
        f.write("General Kenobi!")
finally:
    lock.release()

