import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def test_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_inheritance(self):
        user = User()
        self.assertIsInstance(user, User)


if __name__ == "__main__":
    unittest.main()
