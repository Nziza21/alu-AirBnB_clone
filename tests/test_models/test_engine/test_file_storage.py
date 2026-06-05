#!/usr/bin/python3
"""Tests for FileStorage"""

import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test FileStorage"""

    def test_instance(self):
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_all_returns_dict(self):
        self.assertIsInstance(FileStorage().all(), dict)


if __name__ == "__main__":
    unittest.main()
