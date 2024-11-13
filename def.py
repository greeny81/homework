import random

def say_hello(name, ageg):
    print(name, "hello", ageg)
say_hello('pit', 32)

def lott():
    tikets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win1 = random.choice(tikets)
    tikets.remove(win1)
    win2 = random.choice(tikets)
    return win1, win2

won1, won2 = lott()
print(won1, won2)
print(lott())
print(lott() + lott())

def test(a=2, b=True):
    print(a, b)
test()
test('ddd', 56)
test([23, 33])
test(*[44, 55])
