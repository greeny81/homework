class Human:
    def __init__(self, name, age):
        self.name = name
        self.age =  age
        self.say_info()

    #def __del__(self): # Срабатывает по завершении кода
        #print(f'{self.name} deleted')

    def __len__(self):
        return self.age

    def __lt__(self, other): #СРАВНЕНИЕ  '<' 1й  обьект , 2й обьект
        return self.age < other.age

    def __gt__(self, other): #СРАВНЕНИЕ  '>' 1й  обьект , 2й обьект
        return  self.age > other.age

    def __eq__(self, other): # ==
        return self.name == other.name and self.age == other.age

    def __bool__(self):
        return  bool(self.age)

    def __str__(self):
        return f'Я {self.name}'

    def say_info(self):
        print(f'Меня зовут {self.name} , мне {self.age} лет')

    def birthday(self):
        self.age += 1
        print(f'У {self.name} ДР мне теперь {self.age}')

den = Human('Den', 21)
max = Human('Max', 21)
ser = Human('Den', 21)
den.surname = "Иванов"
#den.say_info()
#del den
max.birthday()
print(len(den))
#input()
#print(den.name, den.surname, den.age)
#print(max.name, max.age)
print(den < max)
print(den > max)
print(max == den) #False
print(den == ser) #True
print(max)