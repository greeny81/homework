
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(k)-len(v) for k, v in zip(first,second) if len(k) != len(v))
second_result = (len(first[i]) == len(second[i]) for i in range(0, len(first)))

print(list(first_result))
print(list(second_result))