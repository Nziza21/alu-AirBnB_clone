import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_amenity(self):
        a = Amenity()
        self.assertTrue(hasattr(a, "name"))
