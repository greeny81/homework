# def f1(number):
#     print('In f1')
#     return 10 / number
#
# def f2():
#     print('Good day')
#     #result_f1 = f1(0)
#     result_f1 = 0
#     for i in range(-2, 2):
#         result_f1 += f1(i)
#         print(result_f1)
#     return  result_f1
# try:
#     total = f2()# НЕ будет иметь значения т.к. при делении на 0 сразу прилетим в 'except'
#     print(total)
# except ZeroDivisionError as err:
#     print(f'Error: {err} but program not crush')
#
#=======ПРИМЕР 3========
def f1(number):

    return 10 / number

def f2():
    print('Good day')
    #result_f1 = f1(0)
    result_f1 = 0
    for i in range(-2, 2, 1):
        try:
            result_f1 += f1(i)
            print(result_f1)
        except ZeroDivisionError as err:
            print(f'Error in f1(): {err} ')
    return  result_f1 / 1
try:
    total = f2()# НЕ будет иметь значения т.к. при делении на 0 сразу прилетим в 'except'
    print(f'Result:{total}')
except ZeroDivisionError as err:
    print(f'Error: {err} but program not crush')

