from threading import  Thread, Event
import time

def first_worker():
    print('First worker run')
    print(event.is_set())
    event.wait()
    print('First worker continue')
    time.sleep(2)
    print('First worker stop')

def second_worker():
    print('Second worker run')
    time.sleep(10)
    print('Second worker stop')
    event.set()
    print(event.is_set())

event = Event()

th1 = Thread(target=first_worker)
th2 = Thread(target=second_worker)
th1.start()
th2.start()


#

