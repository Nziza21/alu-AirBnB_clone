import unittest
from models.place import Place


class TestPlace(unittest.TestCase):

    def test_place(self):
        p = Place()
        self.assertTrue(hasattr(p, "city_id"))
        self.assertTrue(hasattr(p, "name"))
        self.assertTrue(hasattr(p, "price_by_night"))
