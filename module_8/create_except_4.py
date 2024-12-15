# def greet_person(person_name):
#     if person_name == 'Volan':
#         raise Exception("We no  love you Volan")
#     print(f'Hi, {person_name}')
#
# greet_person('Dear student')
# greet_person('Volan')
#
#===============2
# try:
#     raise NameError('Hi ')
# except NameError as err:
#     print(f'Except type {type(err)} miss params:{err.args}')
#     raise #Кидает ошибку на уровень выше
#================3



# class ProZero(Exception):
#     pass
#
# def f(a, b):
#     if b == 0:
#         raise ProZero('Div by zero!')
#     return a / b
#
# print(f(5, 0))
#=================4
class ProZero(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info

def f(a, b):
    if b == 0:
        raise ProZero('Div by zero!', {'a': a,'b':b})
    return a / b

try:
    result = f(10, 0)
    print(result)
except ProZero as err:
    print("Got ERROR")
    print(f'Error msg: {err.message}')
    print(f'Advanced info: {err.extra_info}')