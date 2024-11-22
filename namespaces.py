import math #Область видимости импортированых


d = 5
def square(x): #Обьемлющая для функции even
    #d = x ** 2 #d local square
    d = x ** 2 #квадрат d
    def even(x): #d global d = 5
        nonlocal d #d с уровня выше square
        d = x / 2
        #d = x * 2 # d local even
        if d % 2 == 0:
            print('Четное')
        else:
            print('Нечетное')
    even(x)
    return d

a = 5
b = square(4)
print(a)
print(b)


