#GIL (global interpreter lock)
import datetime
from threading import Thread
import  json
# def count_up(name, n):
#     for i in range(n):
#         print(name, i, sep=": ")
#
# t1 = Thread(target=count_up, args=('Thr1', 5))
# t2 = Thread(target=count_up, args=('Thr2', 5))
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()
res = []
threads = []
files = ["f1.json", "f2.json", "f3.json", "f4.json"]

def worker(file):
    with open(file, "r") as f:
        data = json.load(f)
        res.extend(data)

start =  datetime.datetime.now()

for i in range(len(files)):
    t = Thread(target=worker, args=(files[i], ))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(sum(res))
end =  datetime.datetime.now()
print(end - start)