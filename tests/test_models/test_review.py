import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def test_review(self):
        r = Review()
        self.assertTrue(hasattr(r, "place_id"))
        self.assertTrue(hasattr(r, "user_id"))
        self.assertTrue(hasattr(r, "text"))
