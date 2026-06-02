import unittest
from models.state import State


class TestState(unittest.TestCase):

    def test_state_creation(self):
        s = State()
        self.assertTrue(hasattr(s, "name"))
