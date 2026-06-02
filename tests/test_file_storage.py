import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def test_all_returns_dict(self):
        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)

    def test_new_adds_object(self):
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)

        key = f"BaseModel.{obj.id}"
        self.assertIn(key, storage.all())


if __name__ == "__main__":
    unittest.main()
