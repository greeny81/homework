# def funct_gen(n):
#     i = 0
#     while i != n:
#         yield i
#         i += 1
#
# obj = funct_gen(10)
# print(obj)
# for i in obj:
#     print(i)
#################
import time


def fib_1(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return  result

def fib_2(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib1 = fib_1(n=10)
print(fib1)
for value in fib1:
    print(value)

fib2 = fib_2(n=10)#
print(fib2)       #      Выполнить и Прочитать
for value in fib2:#         можно только
    print(value)  #      -----ОДИН РАЗ-------

###################
start = time.time()

def fib_3():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for value in fib_3():
    print(value)
    if value > 100 ** 6:
        break
fin = time.time()
print((fin - start) * 1000, 'ms')

####### ===========FAST READ FILES============ #########
def read_big_file(file_name):
    with open(file_name, "r", encoding='utf-8') as file:
        for line in file:
            yield line.strip()

for ln in read_big_file('example.txt'):
    print(ln)

