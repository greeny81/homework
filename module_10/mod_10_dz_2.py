import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        #self.enemy = 100
        self.counter = 0

    def war(self, name, power, enemy):
        while enemy:
            enemy = enemy - power
            self.counter += 1
            print(f'{self.name}, сражается {self.counter} день(дня)..., осталось {enemy} воинов.')
            time.sleep(1)


    def run(self):
        print(f'{self.name}, на нас напали!"')
        self.war(self.name, self.power, 100)
        print(f'{self.name} одержал победу спустя {self.counter} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()