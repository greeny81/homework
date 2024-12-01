class Human:
    def __init__(self, name, group):
        self.name = name
        super().__init__(group)
        super().about()
#<class '__main__.Human'> ===> <class '__main__.StudentGroup'>
    def info(self):
        print(f'My name {self.name}')

class StudentGroup:
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f'{self.name} in group {self.group}')


class Student(Human, StudentGroup):
    def __init__(self, name, place, group):
        super().__init__(name, group)
        self.place = place
        super().info()

# human = Human('Andru')
# print(human.name)
student = Student('John','jj', 'group num23')
print(Student.mro())#Иерархия класса
#[<class '__main__.Student'>,
# <class '__main__.Human'>,
# <class '__main__.StudentGroup'>,
# <class 'object'>]
