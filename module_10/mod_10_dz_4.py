from queue import Queue
import threading
from random import randint
from time import sleep


class Table:
    def __init__(self, num):
        self.number = num
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *args):
        self.queue = Queue()
        self.tables = args

    def guest_arrival(self, *guests):
        for tbl in self.tables:
            for gs in guests:
                if not tbl.guest:
                    tbl.guest = gs.name
                    print(f'{gs.name} сел(-а) за стол номер {tbl.number}')
                    guests = tuple(item for item in guests if item.name != gs.name)
                    gs.start()

        for guest in guests:
            self.queue.put(guest)
            print(f'{guest.name} в очереди')



    def discuss_guest(self):
        while self.queue.qsize() > 0:
            i = 0;
            print(f'======={self.queue.qsize()}======')
            for t in tables:# только занятые столы
                #print(f'table:{t.number} guest: {t.guest}')
                for g in guests:# все гости
                    #print(f'cur{g.name}')
                    if g.name == t.guest:# этот гость за столом
                        #print(f'check{g.name} live:{g.is_alive()}')
                        if not g.is_alive():# thread гостя умер
                            #print(t.guest,t.number,g.name,g.is_alive())
                            print(f'{g.name} покушал(-а) и ушёл(ушла)')
                            print(f'Стол номер {t.number} свободен')
                            que_guest = self.queue.get()# Берем гостя из очереди
                            print(f'{que_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}')
                            que_guest.start()

        print('end',self.queue.qsize())

guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman','Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
tables = [Table(number) for number in range(1, 6)]
print(tables)
guests = [Guest(name) for name in guests_names]
print(guests)
cafe = Cafe(*tables)
print(cafe.__dir__())
cafe.guest_arrival(*guests)
cafe.discuss_guest()