import random
import threading
from time import sleep


class Bank():
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(1, 20):
            dep = random.randint(50, 500)
            self.balance += dep
            print(f'Пополнение: {dep}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.01)

    def withdrawal(self):
        for i in range(1, 20):
            withd = random.randint(50, 500)
            print(f'Запрос на {withd}')
            if withd <= self.balance:
                self.balance -= withd
                print(f'Снятие: {withd}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.withdrawal, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()