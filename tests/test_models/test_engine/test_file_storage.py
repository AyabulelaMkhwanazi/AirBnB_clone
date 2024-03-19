#!/usr/bin/python3
"""
This module contains unittests for the class 'FileStorage'.
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import unittest


class TestFileStorage(unittest.TestCase):
    """
    Unittests for the FileStorage class.
    """
    def setUp(self):
        """
        Set up for the tests.
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Clean up after each test.
        """
        self.storage.__objects = {}

    def test_objects_type(self):
        """
        Test that __objects is a dictionary.
        """
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """
        Test that new adds an object to __objects.
        """
        bm = BaseModel()
        self.storage.new(bm)
        key = "{}.{}".format(type(bm).__name__, bm.id)
        self.assertIn(key, self.storage.all())

    def test_save_and_reload(self):
        """
        Test that save serializes __objects and reload deserializes it.
        """
        bm = BaseModel()
        self.storage.new(bm)
        self.storage.save()
        self.storage.__objects = {}
        self.storage.reload()
        key = "{}.{}".format(type(bm).__name__, bm.id)
        self.assertIn(key, self.storage.all())

    def test_file_path(self):
        """
        Test that __file_path is a string.
        """
        self.assertIsInstance(self.storage._FileStorage__file_path, str)

    def test_save_creates_file(self):
        """
        Test that save creates a file.
        """
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload_with_nonexistent_file(self):
        """
        Test that reload handles a nonexistent file.
        """
        try:
            os.remove(self.storage._FileStorage__file_path)
        except FileNotFoundError:
            pass
        self.storage.reload()  # Should not raise an exception


if __name__ == "__main__":
    unittest.main()
