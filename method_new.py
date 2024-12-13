class User:
    __instance = None
    def __new__(cls, *args, **kwargs):#ЕСЛИ НЕ ВОЗВРАЩАЕТ ОБЬЕКТ НЕ БУДЕТ СОЗДАН
        print(args)
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        print('Я в ините')
        self.args = args
        #self.kwargs = kwargs
        #self.name = kwargs.get('name')
        #self.age = kwargs.get('age')
        for key, values in kwargs.items(): #Когда неизвестно сколько прилетит
            setattr(self, key, values)


other = [1, 22, 3]
user = {'name': 'Den', 'age': 25, 'gender' : 'male'}
user1 = User(other, user, name = 'Den')
#user2 = User()
print(user1.args)
#print(user1.kwards)
del user1
user1 = User(*other, **user)
print(user1.args)
print(user1.name)
print(user1.age)
print(user1.gender)

#print(id(user1), id(user2))
#print(user1 is user2)
