# list = ['f','ff','dfd']
# list2 = [2,3,5,6,1]
# sum_ = 0
# for i in range(len(list2)):
#     list[i] = 'ffffffff'
    # sum_ += list2[i]
#
# print(list)
# print (sum_)


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