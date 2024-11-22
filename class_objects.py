class Human:
    def __init__(self, name, age):
        self.name = name
        self.age =  age
        self.say_info()

    def say_info(self):
        print(f'Меня зовут {self.name} , мне {self.age} лет')

    def birthday(self):
        self.age += 1
        print(f'У меня ДР мне теперь {self.age}')

den = Human('Den', 21)
max = Human('Max', 25)
den.surname = "Иванов"

den.birthday()
#print(den.name, den.surname, den.age)
#print(max.name, max.age)

