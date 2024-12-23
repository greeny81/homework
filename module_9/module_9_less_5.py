#itertools
import  sys
from itertools import repeat

ex_iterator = repeat('4', 100000)
print(ex_iterator)
print(f'Size: {sys.getsizeof(ex_iterator)}')

ex_str = "4" * 100000
print(f'Size:{sys.getsizeof(ex_str)}')

class Iter:
    def __init__(self):
        self.f = 'F elem'
        self.s = 'S elem'
        self.t = 'T elem'

    def __iter__(self):
        self.i = 0 #Count is zero!
        return self #return Link self

    def __next__(self):#return elem
        self.i += 1
        if self.i == 1:
            return self.f
        if self.i == 2:
            return self.s
        if self.i == 3:
            return self.t
        if self.i == 4:
            return "End list count"
        raise StopIteration() #no more return

obj = Iter()
print(obj)
for value in obj:#метод next каждый проход. Если StopIteration - в обьекте нет больше элементов.
    print(value)
#FOR ==>>
try:
    while True:
        value = obj.__next__()
        print(value)
except StopIteration:
    #pass
    print('End iteration')

############# Фибоначчи циклом FOR
def fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
print(fibonacci(10))
############# Фибоначчи Итератором
class Fibo:

    def __init__(self, n):
        self.i, self.a, self.b, self.n = 0,0,1,n
    def __iter__(self):
        self.i, self.a, self.b = 0,0,1
        return self
    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b
        return self.a

fib = Fibo(20)
print(fib)
for value in fib:
    print(value)