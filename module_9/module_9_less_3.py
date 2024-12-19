import time
from random import random

#Генератор используется там
# где надо производить
# затратные операции
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

result = (x ** 100 for x in my_numbers)
print(result)#<generator object <genexpr> at 0x000001A0610BAAC0> ссылка на генераторную сборку
print('1й раз')
for elem in result:
    print(elem) #Только сейчас будут вычисления
print('2й раз')
for elem in result:
    print(elem) #Ничего не будет!!! выполняется только 1 раз
print('другой пример')

start_time = time.time()

res = (x ** 3000 for x in my_numbers)
print(res)

print('\nFOR:')
for i in res:
    print('\n',i)

finish_time = time.time()
print(f'Время в милисекундах: {(finish_time-start_time)*1000}')

print('\n Посл. пример.')
list_1 = [1, 5, 9, 29, 4]
list_2 = [5, 2, 9, 1, 2]

ran = range(10, 30)#[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
zp = zip (list_1, list_2)#(1, 5), (5, 2), (9, 9), (29, 1), (4, 2)]
mp = map(str, list_1)#['1', '5', '9', '29', '4']

print(ran, zp, mp)

print(list(ran))
print(list(zp))
print(list(mp))