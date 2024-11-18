# def test_func(*params):
#     print("Type:", type(params))
#     print(params)
#
# test_func(1, 2, 3, 4) # кортеж

def summator(txt, *params, type="sum"):
    sum = 0
    for i in params:
        sum += i
    return f'{txt}: {sum} {type}'

#print(summator("summa",1, 3, 4, 6, type="summator"))

# def info(value, *types, name_a="den", **values ):
# #Позиционный параметр, поз параметры, именной параметр, кортеж
#     print("Type:", type(values))
#     print("Argum:", values)
#     for key, value in values.items():
#         print(key, value)
#     print(types)
#
# info("Параметры всех типов", 2, 3, 4, name_a="Den", course = "Python")

def my_sum(n, *args, txt="Сумма чисел:"):
    #ПОзиционный параметр, переменное кол-во позиц. параметров, именованный параметр
    s = 0
    for i in range(len(args)):
        s += args[i] ** n #Степень
    print(txt + ":", s)

my_sum(1, 1, 2, 3, 4, 5)
my_sum(2, 2, 3, 4, 5, txt="Сумма квадратов")