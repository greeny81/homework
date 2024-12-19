def by_3(x):
    return x * 3

def is_odd(x):#нечет
    return x % 2


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

result = map(by_3, filter(is_odd, my_numbers))#is_odd=>[3, 1, 1, 5, 9]=>by_3=>[9, 3, 3, 15, 27]
print(list(result))

#Списковая сборка
result = [x * 4 for x in my_numbers]# по сути функция аналог map !!
print(result)
result = [x * 2 for  x in  my_numbers if x > 5]# ...,9...,6  => [18, 12] аналог filter
print(result)
result = [x * 3 for  x in  my_numbers if x % 2]# Только нечет * 3 и добавляется
print(result)
result = [x *2 if x > 3 else x * 10 for x in my_numbers]# если х > 3 => x*2 иначе x*10
print(result)#[3, 1, 4, 1, 5, 9, 2, 6]=>[30, 10, 8, 10, 10, 18, 20, 12]
#Операции над определенными даннымиx
my_numbers = ['A', 1, 4, 'B', 5, 'C', 2, 6]
result = [x if type(x) == str else x * 5 for x in my_numbers]#if type(x) == str - если строка просто добавить х
print(result,'\n')#['A', 5, 20, 'B', 25, 'C', 10, 30]
#Вложеные циклы
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
th_numbers = [2, 7, 1, 8, 2, 8, 1, 8]
result = [x * y for x in my_numbers for y in th_numbers]
print(result, len(result))
result = [x * y for x in my_numbers for y in th_numbers if x % 2]
print(result)
result = [x * y for x in my_numbers for y in th_numbers if x % 2 and y // 2]
print(result,'\n')

#ГЕНЕРАТОРЫ
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = {x for x in my_numbers}#{1, 2, 3, 4, 5, 6, 9} множество(УПОРЯДОЧЕНО И УНИКАЛЬНО)
print(result)
th_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = {x: x ** 2 for x in my_numbers}#словарь {3: 9, 1: 1, 4: 16, 5: 25, 9: 81, 2: 4, 6: 36}
print(result)