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
        in_file = file.read()
        file.close()
        return in_file

    def add(self, *products):
        prod_in_mag = self.get_products()
        # print(type(products[1]))
        # print(len(products))
        # print(products[1].name)
        # print(products[1])
        for i in range(len(products)):
            #print(prod_in_mag)
            new_prod = products[i].name

            if new_prod in prod_in_mag:
                print(f'Продукт {new_prod} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{products[i]}\n')
                file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
s1.add(p1,p2,p3)
print(s1.get_products())