import unittest
from src.person import Person
from src.bus_stop import BusStop

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.waverley_bus_stop = BusStop("Waverly Station")
        self.person = Person("Guido van Rossum", 64, self.waverley_bus_stop)

    #@unittest.skip("Delete this line to run the test")
    def test_person_has_name(self):
        self.assertEqual("Guido van Rossum", self.person.name)

    #@unittest.skip("Delete this line to run the test")
    def test_person_has_age(self):
        self.assertEqual(64, self.person.age)

    #@unittest.skip("Delete this line to run the test")
    def test_person_has_destination(self):
        self.assertEqual("Waverly Station", self.waverley_bus_stop.name)
