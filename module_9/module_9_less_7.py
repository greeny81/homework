# - 1 Simple Decorator
def null_decorator(func):
    return func
# def greet():
#     return 'Hello!'

#gr = null_decorator(greet)#ret <function greet at 0x00000286603DCCA0>
#print(gr())#Hello!

# - 2 @ Для декора функции за 1 шаг
# @null_decorator
# def greet():
#     return ('Helllo')
# print(greet())

# -3 еще одна нужная функция внутри декоратора

def upper(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@upper
def greet():
    return 'Helloooo'
print(greet())