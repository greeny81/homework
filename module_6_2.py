class Vehicle:
    def __init__(self, *args):
        self.owner = str(args[0])
        self.__model = str(args[1])
        self.__color = str(args[2])
        self.__engine_power = int(args[3])
        self.__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет:  {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self, clr):
        if clr.lower() in self.__COLOR_VARIANTS:
            self.__color = clr
        else:
            print(f'Нельзя сменить цвет на {clr}')




class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    def get_passengers(self, num):
        if int(num) > self.__PASSENGERS_LIMIT:
            print(f'\nСедан не вмещает много людей! {num - self.__PASSENGERS_LIMIT} человека лишние.')
        else:
            print('Садитесь... поехали!')

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()

vehicle1.get_passengers(7)
vehicle1.get_passengers(5)