# list = ['f','ff','dfd']
# list2 = [2,3,5,6,1]
# sum_ = 0
# for i in range(len(list2)):
#     list[i] = 'ffffffff'
    # sum_ += list2[i]
#
# print(list)
# print (sum_)
def print_names2(a, b, c):
    print(a, b, c)

def print_names3(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)

list_ = [1, 2, 3]
print_names2(list_, 2, 3)
print_names2(*list_)

list_2 = [1, 3]
print_names2(7, *list_2)
print_names2(*list_2, 55)

dict_ = {'a' : 11, 'b' : 22, 'c': 33}
dict_2 = {'a': 11, 'b': 22, 'd': 44} # ERROR 'd'
print_names2(**dict_)

print_names3(**dict_2)

lst = [1, 2]
intc = {'c': 33}

print_names2(*lst, intc)
print_names2(*lst, **intc)

exit()
def print_names(*params): # *args, **kwargs
    print(params)
    print(*params)
print_names(1, 2, 4 ,6)


exit()

sender = "university.help@gmail.com"
rec = "urban.teacher@mail.uk"
suff = (".com",".ru",".net")

print(sender.endswith(suff))
print(rec.endswith(suff))

exit()
for i in range(1,11):
    for j in range(1,11):
        print(f' {i} x {j} = {i * j}')

dict_  = {'a' : 1, 'b' : 2, 'c' : 4}

for i in dict_:
    print(i, dict_[i])

for i , k in dict_.items():
    print(i, k)