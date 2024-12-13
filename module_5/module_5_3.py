# def check_val(input_val):
#     if not isinstance(input_val, int):
#         print('Операнд должен быть типом int')
#         exit()
#     else:
#         return True

class House():

    @staticmethod
    def check_val(input_val):
        if not isinstance(input_val, int):
            print('Операнд должен быть типом int')
            exit()
        else:
            return True


    def __init__(self, name, num) :
        self.name = name
        self.number_of_floors = num

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
       return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __add__(self, val_):
        if House.check_val(val_):
            self.number_of_floors += val_
        #print(f' New floors: {self.number_of_floors}')
        #return House(self.name,self.number_of_floors)
            return self

    def __iadd__(self, val_):
        if House.check_val(val_):
            self.number_of_floors += val_
            return self

    def __radd__(self, val_):
        if House.check_val(val_):
            self.number_of_floors += val_
            return self

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def go_to(self, floor):
        if floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, floor + 1):
                print(i)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# __str__
print(h1)
print(h2)
# __eq__
print(h1 == h2)
# __add__
h1 = h1 + 10
print(h1)
print(h1 == h2)
# __iadd__
h1 += 10
print(h1)
# __radd__
h2 = 10 + h2
# __gt__
print(h2)
print(h1 > h2)
# __ge__
print(h1 >= h2)
# __lt__
print(h1 < h2)
# __le__
print(h1 <= h2)
# __ne__
print(h1 != h2)