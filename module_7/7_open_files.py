import io
from pprint import pprint

f_name = 'sample2.txt'
# file = open(f_name, 'r') # r , w, a,  append + b- binar file
# pprint(file.read())
# file.close()
#
# file = open(f_name, 'w')
# #file.read()  ERROR mode 'w'
# file.write('Hello world dsfgfdg')
# file.close()
#
# file = open(f_name, 'a')
# file.write('\nnew text')
# file.close()
# file = open(f_name, 'r')
# print(file.tell())# возвращает положение курсора 0
# pprint(file.read())# Курсор переместится в конец
# print(file.tell())# 29
# pprint(file.read())# Вернет пустоту
# print(file.seek(15))# Переместит курсор на 15 позицию
# pprint(file.read())#Прочитает остаток 15+
# print(file.tell())# 29
# file.close()
#=================lesson 2
# file = open(f_name, 'r', encoding='utf-8')
# print(file.writable()) #Проверка файла на возможность записи , чтения , поиска
# print(file.readable()) #Проверка файла на возможность записи , чтения , поиска
# print(file.seekable()) #Проверка файла на возможность записи , чтения , поиска
# print(file.buffer) #Просмотр различных параметров print(file. ..........)
# print(file.tell())
# pprint(file.read())
# print(file.tell())
# file.seek(15)
# file.write('new text')
# print(file.tell())
#=========================lesson 3 'WITH'
name = 'sample2.txt'
#with EXPR as TARG: схема
#     ACTION
with open(name, encoding='UTF-8') as file:
    for line in file:
        #print(line, end='')
        for char in line:
            print(char, end='')# c end='' выведет как и line , без - побуквенно
    print(file.tell())
    #с WITH файл автоматом закрывается


