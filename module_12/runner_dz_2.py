
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
        cls.all_results = {}

    def setUp(self):

        self.r1 = Runner('Усэйн', 10)
        self.r2 = Runner('Андрей', 9)
        self.r3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print(f'In tearDownClass')
        for i in cls.all_results:
            print(cls.all_results[i])


    def test_t1(self):
        t1 = Tournament(90, self.r1, self.r3)
        TournamentTest.all_results[0] = t1.start()
        max_Key = max(TournamentTest.all_results[0], key=int)
        self.assertEqual(TournamentTest.all_results[0][max_Key], 'Ник')

    def test_t2(self):
        t2 = Tournament(90, self.r2, self.r3)
        TournamentTest.all_results[1] = t2.start()
        max_Key = max(TournamentTest.all_results[1], key=int)
        self.assertEqual(TournamentTest.all_results[1][max_Key], 'Ник')

    def test_t3(self):
        t3 = Tournament(90, self.r1, self.r2, self.r3)
        TournamentTest.all_results[2] = t3.start()
        max_Key = max(TournamentTest.all_results[2], key=int)
        self.assertEqual(TournamentTest.all_results[2][max_Key], 'Ник')


# tt = TournamentTest()
# tt.setUp()
# tt.setUpClass()
# tt.test_tour(90, tt.r1 , tt.r2)



