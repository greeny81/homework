#Словари
#Ключ не может быть списком
#Неупорядоченая коллекция
phone_book = {'Denis': 8542343444, 'Max': 823423543}
#Словарь изменяемая структура
phone_book['Denis'] = 8324423545555
phone_book['Anton'] = 83345366435
#Удаление по ключу
# del phone_book['Max']
#Обновление нескольких пар сразу
phone_book.update({'Denis': 55555555,'Saha': 2342323444,'Alex': 835452344})
print(phone_book)
#print(phone_book.get('Denis'))
#print(phone_book['Kam']) #Ошибка если нет ключа
#print(phone_book.get('Kam','ret')) #Нет ошибки если нет ключа
#========POP
a = phone_book.pop('Max')
print(phone_book)
list_ = [1,2,3,4]
b = list_.pop(1)
print(list_, a, b)
#========KEYS====VALUES====ITEMS
print(phone_book.keys()) #Вывод ключей
print(phone_book.values())#Вывод значений
print(phone_book.items())#Вывод КЛЮЧ - ЗНАЧЕНИЕ

phone_book['Anton'] = [83345366435, 8432234322] # Значение как список ,изменяемый тип данных
print(phone_book)
#Множества
# - не содержит одинаковых значений
# - нет возможности обратиться по индексу list[0]
set_ = {1,2,3,4,5,1,2,3,4, 'String', True,(1,2,3)}
print(set_)
#вывод множества изи списка
list_ = [1,1,1,1,2,2,3,333,3,2,2]
print(set(list_))
#замена списка на множество
list_ = set(list_)
print(list_)
#Удаление элементов
list_.remove(2) #Ошибка если нет элемента
list_.discard(7) #Нет ошибки если нет элемента
print(list_)
list_.add(888)
print(list_)


