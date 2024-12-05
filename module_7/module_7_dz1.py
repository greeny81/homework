from pprint import pprint

class Product:
    def __init__(self, name, weight, cat):
        self.name = name
        self.weight = weight
        self.category = cat
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        ret = file.read()
        file.close()
        return ret

    def add(self, *products):
        prod_in = self.get_products()
        print('gggg',prod_in)
        for number in products:
            print(number)

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1)