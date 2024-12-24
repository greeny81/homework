import sys
import time


def time_track(func):
    def surr(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = round((ended_at - started_at), 4)
        print(f'Funct time:{elapsed} sec.')
        return result
    return surr


def digits(*args):
    total = 1
    for number in args:
        total *= number ** 500
    return len(str(total))


sys.set_int_max_str_digits(100000)
result = digits(3141, 5926, 2718, 2818)
print(result)