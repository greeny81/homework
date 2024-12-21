# Иногда нам нужно создать функцию, которая будет делать
# очень короткую математическую операцию. Для этого придумали
# лямбда-функции. Это такие очень коротенькие функции, которые
# прям на месте создаются, на месте же вызываются
from pprint import pprint

my_func = lambda x: x + 10

print(my_func(x=42))

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result =map(lambda x:x+10,my_numbers)
print(list(result))

#===Лямбда-функция может принимать как несколько параметров, так и не одного.

they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]
result = map(lambda x, y: x+y, my_numbers,they_numbers)
print(list(result))

# лямбда-функции ограниченное применение. Они создаются в процессе выполнения кода
# и из-за этого могут просадить быстродействия. Это в принципе и логично.
# Они плохо специализируются могут быть проблемы в крупных фреймворках
# Не надо пытаться записать сложное выражение в лямбда-функцию. Для этого у нас есть ключевое слово «def»

def get_multi_v1(n):
    if n == 2:
        def multi(x):
            return x * 2
    elif n == 3:
        def multi(x):
            return  x * 3
    else:
        def multi(x):
            return x * n
    return multi
#get_multi_v1 функция высшего порядка она возвращает функции
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
by_2 = get_multi_v1(2)#возвращает ФУНКЦИЮ !!!! x * 2
by_3 = get_multi_v1(3)
print(by_2)
result = map(by_2, my_numbers)# map(x * 2, my_numbers[x1, x2,....])
print(list(result))
result = map(by_3, my_numbers)
print(list(result))

by_5 = get_multi_v1(5)
print(by_5(x=11))

by_10 = get_multi_v1(10)
by_100= get_multi_v1(100)

print(list(map(by_10, my_numbers)))

def matrix(some_list):

    def multi_col(x):
        res = []
        for element in some_list:
            res.append(element * x)
        return res

    return multi_col

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
th_numbers = [2, 7, 1, 8, 2, 8, 1, 8]

matrix_on_my_num = matrix(my_numbers)#funct [3 * x, 1 * x, 4 * x, 1 * x, 5 * x, 9 * x, 2 * x, 6 * x]

result = map(matrix_on_my_num, th_numbers)
pprint(list(result))#[[6, 2, 8, 2, 10, 18, 4, 12], [21, 7, 28, 7, 35, 63, 14, 42], .....

print('\n===')

my_numbers.extend([100, 200])
result = map(matrix_on_my_num, th_numbers)
pprint(list(result))

#Создание объекта который можно вызвать
class Multip:

    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        #если есть такой метод у класса ТО его можно вызвать
        return x * self.n

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

by_100500 = Multip(n=100500)
result = by_100500(x=2)
print(result)#201000

result = map(by_100500, my_numbers)
print(list(result))#[301500, 100500, 402000, 100500, 502500, 904500, 201000, 603000]
