# - 1 Simple Decorator
import sys
import time
#
# def null_decorator(func):
#     return func
# # def greet():
# #     return 'Hello!'
#
# #gr = null_decorator(greet)#ret <function greet at 0x00000286603DCCA0>
# #print(gr())#Hello!
#
# # - 2 @ Для декора функции за 1 шаг
# # @null_decorator
# # def greet():
# #     return ('Helllo')
# # print(greet())
#
# # -3 еще одна нужная функция внутри декоратора
#
# def upper(func):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#     return wrapper
#
# @upper
# def greet():
#     return 'Helloooo'
# print(greet())

########
def time_track(func):
    def surr(*args, **kwargs):

        started_at = time.time()

        result = func(*args, **kwargs)#digits

        ended_at = time.time()
        elapsed = round((ended_at - started_at), 4)
        print(f'Funct time:{elapsed} sec.')
        return result
    return surr

@time_track #Выведет время выполнения 
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


#sys.set_int_max_str_digits(1000)
result = digits(3141, 5926, 2718, 2818)
print(result)