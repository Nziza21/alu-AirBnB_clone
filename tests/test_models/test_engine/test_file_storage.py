#!/usr/bin/python3
"""Tests for FileStorage"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up file after tests"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance(self):
        """Test instance creation"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_file_path(self):
        """Test __file_path attribute"""
        self.assertEqual(
            FileStorage._FileStorage__file_path,
            "file.json"
        )

    def test_objects(self):
        """Test __objects attribute"""
        self.assertIsInstance(
            FileStorage._FileStorage__objects,
            dict
        )

    def test_all_returns_dict(self):
        """Test all()"""
        self.assertIsInstance(
            self.storage.all(),
            dict
        )

    def test_new(self):
        """Test new()"""
        obj = BaseModel()
        self.storage.new(obj)

        key = "{}.{}".format(
            obj.__class__.__name__,
            obj.id
        )

        self.assertIn(
            key,
            self.storage.all()
        )

    def test_save(self):
        """Test save()"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        self.assertTrue(
            os.path.exists("file.json")
        )

    def test_reload(self):
        """Test reload()"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        storage2 = FileStorage()
        storage2.reload()

        self.assertIsInstance(
            storage2.all(),
            dict
        )


if __name__ == "__main__":
    unittest.main()
