import inspect
from pprint import pprint

import requests



some_string = 'Just string'
some_number = 33
some_list = [some_string, some_number]

def some_function(param, param_2 = 'n/a'):
    print('Input params', param, param_2)

class SomeClass:
    def __init__(self):
        self.attribute_1 = 23
        self.attribute_2 = 'ggwp'

    def some_class_method(self, value):
        self.attribute_1 = value
        print('Class attrib_1:', self.attribute_1)

some_obj = SomeClass()

new_func = some_function

#=====1 Аттрибут класса __name__
print('1 Аттрибут класса __name__')
print(some_function.__name__)
print(SomeClass.__name__)
print(requests.__name__)
print(new_func.__name__)
#print(some_string.__name__) # ERR не имеет имени 'str' object has no attribute '__name__'

#=====2 Типы
print(type(some_number))
print(type(some_number) is int)
print(type(requests))
print(type(requests.get))
#=====3 Dir Все атрибуты  и методы объекта
#pprint(dir(requests))
#pprint(dir())# объекты области видимости - тут глобальная

#=====4 hasattr() проверка на существование аттрибута
print(hasattr(some_obj, 'attribute_1'))
print(hasattr(some_obj, 'attribute_3'))

#=====5 getattr() значение аттрибута
print(getattr(some_obj, 'attribute_1'))
print(getattr(some_obj, 'attribute_3', 'Такого аттр нет!'))

for attr_name in dir(requests):
    attr = getattr(requests, attr_name)
    print(attr_name, type(attr))
#====== callable() - проверка на возможность вызвать обьект
print('---Callable()---')
print(callable(some_string))#FALSE
print(callable(some_function))#TRUE
print(callable(some_obj.attribute_2))#FALSE
print(callable(some_obj.some_class_method))#TRUE

#====== isinstance() проверка является ли объект экземпляром класса
print('---Isinstance---')
print(isinstance(some_number, str))#FALSE
print(isinstance(some_number, int))#TRUE
print(isinstance(some_number, SomeClass))#FALSE
print(isinstance(some_obj, SomeClass))#TRUE

#=========== Модуль inspect - https://docs.python.org/3/library/inspect.html
#   Этот модуль предоставляет четыре основных вида услуг: проверка типов,
#получение исходного кода, проверка классов и функций и проверка стека интерпретатора.
#   Функции, помогающие получить информацию о живых объектах -- модули, классы, методы,
#функции, трассировки, объекты фрейма и объекты кода
print('---Inspect ---')
print(inspect.ismodule(requests))
print(inspect.ismodule(some_obj))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))
print(inspect.isbuiltin(requests))

some_func_mod = inspect.getmodule(some_function)
print(type(some_func_mod), some_func_mod)


#Этот модуль обеспечивает доступ к некоторым переменным, используемым
#или поддерживаемым интерпретатором, и к функциям, которые тесно взаимодействуют
#с интерпретатором. Он всегда доступен.
import sys
print('SYS')
#Путь к интерпретатору
print(sys.executable)
# Текущая ОС
print(sys.platform)
# Версия python
print(sys.version, sys.version_info)
# Параметры командной строки
print(sys.argv)
# пути поиска каталогов для Python
print(sys.path)
# Модули загруженые в текущий момент
print('modules')
#pprint(sys.modules)
print('__bui')
# __builtins__ псевдо модуль содержащий встроенные в интерпретатор константы, функции ..
#pprint(dir(__builtins__))

def facto(n):
    if n == 1:
        return 1
    else:
        return n * facto(n - 1)

sys.setrecursionlimit(1500)

print(facto(1099))
print(sys.getsizeof(facto))

