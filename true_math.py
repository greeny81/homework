cor = ((), 1, 2, 3)
for item in cor:
    print(f'item {item} type {type(item)}')
print(len(cor[0]))

from math import inf
def divide(first, second):
    if second:
        return first / second
    else:
        return inf

