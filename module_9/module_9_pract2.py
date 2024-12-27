import time
def memoize_func(fun):
    mem = {}
    def wrapper(*args):
        print(f'Wrapper с аргументами {args} mem:{mem}')
        if args not in mem:
            mem[args] = fun(*args)
            return f'wrapper done res={mem[args]}'
        else:
            return f'!!!Entry already exists {mem[args]}'
    return wrapper

@memoize_func
def func(a, b):
    print(f' Функция вычисляет:{a} {b}')
    return a ** b

print(func(3, 5), '')
print(func(3, 4), '')
print(func(3, 5), '')
print(func(3, 4), '')
print(func(3, 1), '')
print(func(3, 5), '')
