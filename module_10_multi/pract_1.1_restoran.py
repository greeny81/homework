import random
import time
from threading import Thread
import  queue

class Bulka(Thread):
    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        while True:
            time.sleep(1)#time ready Bulka
            if random.random() > 0.5:  # ran.ran return 0...1 |>0.9 = 10 %
                print('Булка подгорела!')
                self.queue.put('Булка подгорела!')
            else:
                print('Норм булка готова!')
                self.queue.put('Норм булка')

class Kotleta(Thread):
    def __init__(self, queue, count):
        self.queue = queue
        self.count = count
        super().__init__()

    def run(self):

        while self.count:
            print(f'Готовых булок:{self.queue.qsize()}')
            bulka = self.queue.get()
            if bulka == 'Норм булка':
                time.sleep(random.randint(1, 3))# Create Bulka+kotleta
                print('Кладем котлету в булку.')
                self.count -= 1
            print('Осталось сделать ', self.count , ' бургеров')

queue = queue.Queue(maxsize=10)

t1 = Bulka(queue)
t2 = Kotleta(queue, 20)

t1.start()
t2.start()
t1.join()
t2.join()
