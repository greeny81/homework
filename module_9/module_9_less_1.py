# 1 - функция это обьект



def get_russian_names():
    return ["Ваня", "Коля", "Маша"]

def get_british_names():
    #print(["ВJack", "Mikael", "Hungry"])
    return ["ВJack", "Mikael", "Hungry"]


# #get_russian_names()
# print(type(get_russian_names))
# print(get_russian_names.__name__)
# # 2 - можно присвоить функцию другой переменной
# print("\n*2")
#
# my_funct = get_russian_names
# print(my_funct())
# print(my_funct.__name__)

# 3 - c функцией можно работать как с обьектом
name_getters = [get_russian_names, get_british_names]
for name_getter in name_getters:
    print(name_getter())
# ['Ваня', 'Коля', 'Маша']
# ['ВJack', 'Mikael', 'Hungry']

#4 - функцие принимаемые на вход другие функции с аргументами
print('\n*4')
def adder(args):
    res = 0
    for number in args:
        res += number
    return res
def multiplier(args):
    res = 1
    for number in args:
        res *= number
    return res

def process_numbers(numbers, function):
    result = function(numbers)
    print(f'RESULT: {result}')

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
process_numbers(my_numbers, adder)
process_numbers(my_numbers, multiplier)

# 5 - map применяет функцию к каждому элементу последовательности и формирует список результатов
print('\n*5')

def mul_by_2(x):
    return x * 2

result = map(mul_by_2, my_numbers )
print(result)
print(list(result))

#filter вычисляет функцию для каждого элемента и добавляет элемент в список результатов
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print('\n*6')
def is_odd(x):
    return x % 2 # ост. от деления

result = filter(is_odd, my_numbers)# if True
print(result)
print(list(result))
print(type(list(result)))
rlist = list(result)
ret = map(mul_by_2, rlist)
print(rlist, list(ret))