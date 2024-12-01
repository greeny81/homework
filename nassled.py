from setuptools.command.build_py import build_py


class Human:
    head = True
    # def __init__(self):\
    #     self.about()
    def say_name(self):
        print('Hello!')

class Student(Human):#Дочерний класс от Human
    head = False
    def about(self):
        print('Im student')

    def say_name(self):
        print('Hello!')

class Teacher(Human):
    pass

#human = Human()
student = Student()
teacher = Teacher()
print(student.head)#Cначала смотрит в Student если нет то в Human
student.say_name() #из класса student
teacher.say_name() # ИЗ родительского