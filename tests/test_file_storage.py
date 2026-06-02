import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def test_storage(self):
        fs = FileStorage()
        self.assertEqual(type(fs.all()), dict)
