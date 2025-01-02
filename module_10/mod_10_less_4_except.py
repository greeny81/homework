import threading
import time

def some_func():
    time.sleep(2)
    raise Exception

def excepthook(args):
    print(args.thread.name, args.thread.is_alive())

def thread_func():
    try:
        some_func()
    except Exception as err:
        print(f'Err {err}')

t1 = threading.Thread(target=thread_func)
t2 = threading.Thread(target=thread_func)

t1.start()
t2.start()
t1.join()
t2.join()
#
threading.excepthook = excepthook
t1 = threading.Thread(target=some_func)
t2 = threading.Thread(target=some_func)
t1.start()
t2.start()
t1.join()
t2.join()
