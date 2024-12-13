from class_objects import Human


class House():
    houses_history = []
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        return object.__new__(cls)

    def __init__(self, name, num) :
        self.name = name
        self.number_of_floors = num
    def go_to(self, floor):
        if floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, floor + 1):
                print(i)

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
