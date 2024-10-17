phone_book = {'Denis': 8542343444, 'Max': 823423543}
phone_book['Denis'] = 8324423545555
phone_book['Anton'] = 83345366435
#del phone_book['Max']
phone_book.update({'Saha': 2342323444,'Alex': 835452344})
print(phone_book)
#print(phone_book.get('Denis'))
#ERROR
#print(phone_book['Kam'])
#NO ERROR
#print(phone_book.get('Kam','ret'))
#========POP
a = phone_book.pop('Max')
print(phone_book)
list_ = [1,2,3,4]
b = list_.pop(1)
print(list_, a, b)
#========KEYS====VALUES====ITEMS
print(phone_book.keys())
print(phone_book.values())
print(phone_book.items())

phone_book['Anton'] = [83345366435, 8432234322] # Значение как список ,изменяемый тип данных
print(phone_book)

