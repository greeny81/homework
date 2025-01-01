import threading

counter = 0
lock  = threading.Lock()#Поставить блок на поток. остальные ждут.

def increment(name):
    global counter
    try:
        lock.acquire() # activate BLOCK
        for i in range(100):
            counter += 1
            print(name, counter, lock.locked())
    except:
        pass
    finally:
        lock.release()# disable BLOCK

def decrement(name):
    global counter
    #lock.acquire()# activate BLOCK
    with lock: #Более короткий вариант
        for i in range(100):
            counter -= 1
            print(name, counter, lock.locked())
    #lock.release()

thread1 = threading.Thread(target=increment, args=('thred1',))
thread2 = threading.Thread(target=decrement, args=('thred2',))
thread3 = threading.Thread(target=increment, args=('thred3',))
thread4 = threading.Thread(target=decrement, args=('thred4',))

thread1.start()
#thread3.start()
thread2.start()
#thread4.start()
