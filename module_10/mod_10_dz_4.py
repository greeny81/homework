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


        while self.queue.qsize() != 0:
            for t in tables:# только занятые столы
                for g in guests:# все гости
                    if g.name == t.guest and not g.is_alive():# этот гость за столом
                        #print(t.guest,t.number,g.name,g.is_alive())
                        print(f'{g.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {t.number} свободен')
                        que_guest = self.queue.get()# Берем гостя из очереди
                        print(f'{que_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}')
                        t.guest = que_guest.name
                        que_guest.start()

        print('End qSize:',self.queue.qsize())

guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman','Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
tables = [Table(number) for number in range(1, 6)]

# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guest()