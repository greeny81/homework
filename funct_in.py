# int() --> int(input())
# float() -->
# bool()
# str()
# list()
# tuple()
# dict()
# set()



def helper():
    """
    Это функция описание

    """
    pass

print(help(helper))
print(list('abgr'))
salary = [2300, 1800, 5000, 7600, 1234.44]
print(sum(salary), len(salary))
avg = round(sum(salary)/len(salary), 2)

print("Средняя:", avg)
print("Summ:", round(sum(salary), 1))
print("Max:", round(max(salary), 1))
print("Min:", round(min(salary), 1))

names = ['Денис', 'Егор', 'Катя','Женя','Антон']
zipped = zip(names, salary) #Слияние
print(zipped)# Получаем ОБЬЕКТ!!!
zp = dict(zipped)# Преобразуем в словарь
print (zp)
print(zp['Денис'] , " - ЗП Дениса")

a = [True, False, False]
print(any(a)) #Хотя бы 1 TRUE вернет True
b = [1, 0 , 0]
print(any(b)) # True
#ALL
print(all(a)) #FALSE
c = [1, 1, 1]
print(all(c))# TRUE
#DIR
print(dir(c))#ДОСТУПНЫЕ МЕТОДЫ
#isinstance()
dd = 'dd'
ff = 55
print(isinstance(dd, str))
print(isinstance(ff, int))
s = [1, 1, 1]
h = [1, 1, 1]
print(s == h)#TRUE
print(s is h)#FALSE
print(id(s))#1433533550080

print(id(h))#1433533550144
d = h
print(id(d))#1433533550144

print(id(2))
print(id(4))
print(id(2))

#HELP
#print(help(h))
#print(help(print))
