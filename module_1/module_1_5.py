immutable_var = tuple((1,2,3,True,[10,20]))
#print(type(immutable_var))
print("immutable_var:",immutable_var)
#immutable_var[3] = False
#immutable_var[3] = False TypeError: объект кортеж не поддерживает назначение элементов

mutable_list = ["apple", "banan", "coconut", False, 2, "String"]
#print(mutable_list)
mutable_list[2] = "Клубника"
mutable_list.append("55")
mutable_list.remove(mutable_list[1])
print("mutable_list:",mutable_list)