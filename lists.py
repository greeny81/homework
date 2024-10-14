# food = ["apple", "banan", "coconut"]
# print(food[0])
# #food[0] = "peach"
# print(food)
#
# food.append(True)
# print(food)
# food.extend(["string",2])
# print(food)
# #food.remove("apple")
# food.remove(food[0])
# print(food)
# print("coconut" in food)
# print("coconut" not in food)
# print(food[1:3])

tuple_ = 1,2,3,4
tuple_2 = (1,2,3,4, True, "String")
list_ = [1,2,3,4, True, "String"]
tuple_3 = tuple([1,2,3,4,6])
print(type(tuple_))
print(tuple_2)
print(list_)

print(tuple_2.__sizeof__())
print(list_.__sizeof__())


tuple_ = ([1,2], 2)
print(tuple_)
tuple_[0][0] = 9
print(tuple_)

tuple_ = ([1,2], 2) + (33, 2)
print(tuple_)
tuple_ =(1,2) * 3
print(tuple_)