
try:
    i = 0
    trube = a + b
    print(10 / i)
    print('Done')
# except (ZeroDivisionError, NameError):
#     print('ERRRR Div by zero')
except ZeroDivisionError:
    print('ERRRR Div by zero')

except NameError as ggg:
    print(f"ERRRR a and b нет таких   {ggg}")

try:
    #file = open("gg.txt")
    print('Start')
except OSError as oer:
    print(f'ERRR {oer}')
else:
    print('Если ошибки не произожло')
finally:
    print('Это выполниться полюбому!')

