import time
import sys

def func_gen_dec(precision):
    print('Получил точность для вывода результа, начинаем создавать декоратор')
    def dec(func):
        print(f'Декоратор принял функцию digits которую нужно отдекорировать {func} ,"\n"начинает создавать функцию обертку')
        def wrapper(*args, **kwargs):
            started_at = time.time()
            print('digits - является wrapper ! Запускаем реальную функцию с передачей в функ-обертку параметров и запоминаем результ')
            result = func(*args, **kwargs)#Вызывается изначальная digits
            print(f'тут используется {precision} он запомнится в замыкании surrogate')
            ended_at = time.time()
            elapsed = round(ended_at - started_at, precision)
            print(f'Funct worked {elapsed} sec.')
            print('Возвращаем что вернула реальная функция')
            return result
        print('декоратор создал ФУНКЦИЮ-Обертку и возвращает (WRAPPER)')
        return wrapper
    print('Декоратор создан и пора его вернуть func_gen_dec')
    return dec

@func_gen_dec(precision=2)
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))

# time_track_precision_6 = func_gen_dec(precision=5)
# digits = time_track_precision_6(digits)
result = digits(3141, 5926, 2718, 2818)
print(result)