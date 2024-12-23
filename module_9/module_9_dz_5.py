class StepValueError(ValueError):
    pass

class Iterator:
    start = 0
    stop = 0
    step = 0
    point = 0
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')

        self.start = start
        self.stop = stop
        self.step = step
        self.point = self.start

    def __iter__(self):
        self.point = self.start
        return self
    def __next__(self):
        self.point += self.step
        if (self.step>0 and self.point > self.stop) or (self.step<0 and self.point < self.stop):
            raise StopIteration()
        return self.point

# try:
#     iter1 = Iterator(100, 200, 0)
#     print(iter1)
#     for i in iter1:
#         print(i, end=' ')
# except StepValueError:
#     print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
