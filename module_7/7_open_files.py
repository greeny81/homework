from pprint import pprint

f_name = 'sample2.txt'
file = open(f_name, 'r') # r , w, a,  append + b- binar file
pprint(file.read())
file.close()

file = open(f_name, 'w')
#file.read()  ERROR mode 'w'
file.write('Hello world dsfgfdg')
file.close()

file = open(f_name, 'a')
file.write('\nnew text')
file.close()

file = open(f_name, 'r')
print(file.tell())# возвращает положение курсора 0
pprint(file.read())# Курсор переместится в конец
print(file.tell())# 29
pprint(file.read())# Вернет пустоту
print(file.seek(15))# Переместит курсор на 15 позицию
pprint(file.read())#Прочитает остаток 15+
file.close()
