class House():
    def __init__(self, name, num) :
        self.name = name
        self.number_of_floors = num
    def go_to(self, floor):
        if floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, floor + 1):
                print(i)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)