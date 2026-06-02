import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def test_city(self):
        c = City()
        self.assertTrue(hasattr(c, "state_id"))
        self.assertTrue(hasattr(c, "name"))
