#Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
my_dict = {'Sergey': 1991, 'Evgeniy': 1994, 'Artem': 1998, 'Max': 1986}
print('Dict:',my_dict)
#Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
print('Existing value:',my_dict['Evgeniy'])
print('Not existing value:',my_dict.get('SVETLANA'))
#Добавьте ещё две произвольные пары того же формата в словарь my_dict.
my_dict.update({'Yura' : 1999, 'Kate' : 1991})
print(my_dict)
#Удалите одну из пар в словаре по существующему ключу из словаря my_dict
#и выведите значение из этой пары на экран.
rem = my_dict.pop('Evgeniy')
print('Удалена пара с ключем \"Evgeniy\" и значением:', rem )
print(my_dict)

# Создайте переменную my_set
# и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
my_set = {1, 2, 3, 'String', 4, 5, 6, True, 'True', 2, 3, 5, 'String'}
print('\nSet:',my_set)
#Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.add(7)
my_set.add('False')
my_set.discard(1)
print('Modified set:',my_set)