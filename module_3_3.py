def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# print_params()
# print_params(b = 25)
# print_params(c = [1,2,3])
values_list = [33, True, 'werwer']
values_dict = {'a': 'qwerty', 'b' : 55, 'c': 66}

# print_params(*values_list)
# print_params(**values_dict)

values_list_2 = ['ffff', 34]

print_params(*values_list_2, 42)