import time
from record_classes import TUNERS


t = TUNERS()

t._read_cfg()

dev,tun,lock = t.get_tuner()
print(f'tun={tun}, dev={dev}')


with lock:
    time.sleep(40)

t.put_tuner(tun,lock)
