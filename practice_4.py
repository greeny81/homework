#import math
from math import sin

a = 3
print(sin(a))
exit()

import pack_module_4.alg
data_1  = list(map(int, input('Введи числа через пробел').split()))
data_2  = list(map(int, input('Введи числа через пробел').split()))
data_3  = list(map(int, input('Введи числа через пробел').split()))

pack_module_4.alg.bubble_sort(data_1)
pack_module_4.alg.selection_sort(data_2)
pack_module_4.alg.insertion_sort(data_3)

print("Пузырьковая сортировка ", data_1)
print("Выбором сортировка ", data_2)
print("Сортировка вставкой", data_3)