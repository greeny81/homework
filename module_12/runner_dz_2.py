from unittest import TestCase




class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                #print(f'{participant} = {participant.distance} - {self.full_distance}')
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)
                    #print(finishers)

        return finishers


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        print('TClass')
        cls.all_results = {}

    def setUp(self):
        print('SetUp')
        self.r1 = Runner('Усэйн', 10)
        self.r2 = Runner('Андрей', 9)
        self.r3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print('TClass')
        print(f'Tear {cls.all_results}')


    def test_tour(self):
        t1 = Tournament(90, self.r1, self.r3)
        t2 = Tournament(90, self.r2, self.r3)
        t3 = Tournament(90, self.r1, self.r2, self.r3)

        print(t1.start())
        print(t2.start())
        print(t3.start())




