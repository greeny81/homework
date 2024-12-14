
def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    if isinstance(numbers, int):
        return None

    for i in numbers:
        try:
            result += i
        except TypeError as err:
            incorrect_data += 1
            print(f'В numbers записан некорректный тип данных: {i}')
    return {'result' : result, 'incorrect_data' : incorrect_data}

def calculate_average(numbers):
    res = personal_sum(numbers)
    if res:
        try:
            tot_aver = res['result'] / (len(numbers) - res['incorrect_data'])
        except ZeroDivisionError as err:
            return 0
        return tot_aver
    else:
        return res


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
