#максимум в списке
def find_max(list_):
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return  max_
tlist = [1, 56, 76, 33, 43, 89, 34, 12, 0]
print(find_max(tlist))

#Подсчет четных чисел в списке
def count_even(list_):
    counter = 0
    for i in list_:
        if i % 2 == 0 and i != 0:
            counter += 1
    return counter
print(count_even(tlist))
#Уникальный список
def unique(tlist_):
    new_list = []
    for i in tlist_:
        if i not in new_list:
            new_list.append(i)
    return new_list
ulist = [1, 2, 3 ,4 ,5 ,6, 7, 8 , 9, 10, 8, 7, 6 , 5 ,4 , 3, 2 ,1 , 1]
print(unique(ulist))