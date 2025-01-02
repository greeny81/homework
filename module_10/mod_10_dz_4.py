from queue import Queue
import threading
import time
from random import randint
from threading import Thread
from time import sleep


class Table():
    def __init__(self, num):
        self.number = num

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.start()

    def run(self):
        sleep(randint(3, 10))

class Cafe():
    def __init__(self, *args):
        self.queue = Queue()
        self.tables = args

    def guest_arrival(self, *guests):
        pass
    def discuss_guest(self):
        pass
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman','Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
tables = [Table(number) for number in range(1, 6)]
print(tables)
guests = [Guest(name) for name in guests_names]
print(guests)
cafe = Cafe(*tables)
print(cafe.__dir__())
cafe.guest_arrival(*guests)