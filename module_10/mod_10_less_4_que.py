#FIFO  - first IN - first OUT
from queue import Queue
import threading
import time

def getter(que):
    while True:
        time.sleep(4)
        item = que.get()
        print(threading.current_thread(),'Get elem ', item)

q = Queue(maxsize=10)
t1 = threading.Thread(target=getter, args=(q,), daemon=True)
t1.start()

for i in range(10):
    time.sleep(2)
    q.put(i)
    print(threading.current_thread(), 'Put elem', i)


# q.put(5)
# print(q.get(timeout=2))
# print('End programm')