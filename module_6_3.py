import random
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        new_coord = [item * self.speed for item in self._cords]
        if new_coord[2] < 0:
            print("t's too deep, i can't dive :(")
        else:
            self._cords = new_coord
    def speak(self,snd):
        print(snd)


class Bird(Animal):
    def __init__(self, speed):
        self.beak = True
        super().__init__(speed)

    def lay_eggs(self):
        print(f'Here are(is) {random.randint(1, 4)} eggs for you')

    #def speak(snd):
     #   super().speak(snd)

class Duckbill(Bird):

    def __init__(self, speed):
        self.sound = 'Click-click-click'
        super().__init__(speed)

    def speak(self):
        super().speak(self.sound)
        

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        pass
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

db = Duckbill(10)

print(db.live)
print(db.beak)
print(db.speed)
db.speak()
db.lay_eggs()
print(Duckbill.mro())