import  multiprocessing
import  threading
import time

count = 0

def first_worker(n):
    global count
    for i in range(n):
        count += 1
        time.sleep(1)
        print('First  work +', count)
    print('First worker END change count', count)

def second_worker(n):
    global count
    for i in range(n):
        count += 1
        time.sleep(1)
        print('Sec work +', count)
    print('Second worker END change  count', count)

# th1 = threading.Thread(target=first_worker, args=(10,))
# th2 = threading.Thread(target=second_worker, args=(5,))
# th1.start()
# th2.start()

if __name__  == '__main__':#У процессов будет своя память
    process1 = multiprocessing.Process(target=first_worker, args=(10,))
    process2 = multiprocessing.Process(target=second_worker, args=(12,))
    process1.start()
    process2.start()