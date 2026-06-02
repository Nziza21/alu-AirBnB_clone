import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_create(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, "id"))

    def test_save(self):
        obj = BaseModel()
        old = obj.updated_at
        obj.save()
        self.assertNotEqual(old, obj.updated_at)
