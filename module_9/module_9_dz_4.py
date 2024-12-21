import random

class MysticBall:
    def __init__(self, *wrd):
        self.words = wrd
    def __call__(self):
        return random.choice(self.words)
#------
first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda  x , y : x == y , first, second))
print(result)
#-------
def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(str(data_set))
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())