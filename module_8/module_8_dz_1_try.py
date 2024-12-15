def add_everything_up(a, b):
    try:
        ret = round(a + b, 3)
    except TypeError as err:
        ret = str(a)+str(b)
    return ret

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))