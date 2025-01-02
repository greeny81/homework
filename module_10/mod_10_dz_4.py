from queue import Queue
import threading
from random import randint
from time import sleep


class Table():
    def __init__(self, num):
        self.number = num
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(randint(3, 10))

class Cafe():
    def __init__(self, *args):
        self.queue = Queue()
        self.tables = args

    def guest_arrival(self, *guests):

        for gs in guests:
            for tbl in self.tables:
                if not tbl.guest:
                   tbl.guest = gs.name
                   print(f'{gs.name} сел(-а) за стол номер {tbl.number}')
                   guests = tuple(item for item in guests if item.name != gs.name)
                   gs.start()
                   break
        #print(guests)
        for gs in guests:
            self.queue.put(gs)
            print(f'{gs.name} в очереди')



    def discuss_guest(self):
        print(self.queue.empty())
        pass
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman','Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
tables = [Table(number) for number in range(1, 6)]
print(tables)
guests = [Guest(name) for name in guests_names]
print(guests)
cafe = Cafe(*tables)
print(cafe.__dir__())
cafe.guest_arrival(*guests)
cafe.discuss_guest()