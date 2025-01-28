from unittest import TestCase

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name



class RunnerTest(TestCase):
    def test_walk(self):
        self.assertEqual(begun.distance, 50)
    def test_run(self):
        self.assertEqual(begun1.distance, 100)
    def test_challenge(self):
        self.assertNotEqual(begun.distance, begun1.distance)

begun = Runner('Smith')
begun1 = Runner('John')
for i in range(0, 10):
    begun.walk()
    begun1.run()

